from sqlalchemy import create_engine, update, insert, text, inspect
from sqlalchemy.orm import sessionmaker


from config.config import get_env_db_config

class BaseRepository:
    DEFAULT_PAGE_SIZE = 10

    def __init__(self, db_config = None):
        if not db_config:
            db_config = get_env_db_config()
        self.schema = db_config["schema"]
        self.engine = create_engine(db_config["connection"])
        self.__set_schema__(db_config["schema"])

    def __get_all__(self, klass, filter = None, order_by = None, page_size = DEFAULT_PAGE_SIZE):
        with self.__new_session__() as session:
            q = session.query(klass)

            if filter is not None:
                #q = q.filter(filter)
                # sqlalchemy.exc.ProgrammingError: (psycopg2.errors.DuplicateAlias) el nombre de tabla «game_records» fue especificado más de una vez
                q = q.filter(text(filter))
            if order_by:
                q = q.order_by(order_by)
            return q.limit(page_size).all()

    def __get_one_by_filter__(self, klass, filter):
        with self.__new_session__() as session:
            return session.query(klass).filter(filter).first()

    def __new_session__(self):
        Session = sessionmaker(bind=self.engine)
        return Session()

    def __execute_query__(self, query):
        with self.engine.begin() as connection:
            connection.execute(text(f"""SET search_path = {self.schema};"""))
            if isinstance(query, str):
                query = text(query)
            return connection.execute(query)

    def __update__(self, klass, id, props):
        q = update(klass).where(klass.id==id).values(props)
        self.__execute_query__(q)

    def __insert__(self, klass, obj):
        d = obj.__dict__
        columns = inspect(klass).columns
        for k in list(d.keys()):
            if k not in columns.keys():
                del d[k]

        q = insert(klass).values(d).returning(klass)
        res = self.__execute_query__(q)
        new_id = res.scalars().first()
        return self.__get_one_by_filter__(klass, klass.id == new_id)

    def __set_schema__(self, schema):
        sql = f"""SET search_path = {schema};"""
        self.__execute_query__(sql)