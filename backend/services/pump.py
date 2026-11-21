from config.config import PUMP_CONFIG

class Pump:
    BATCH_SIZE = 10_000
    def __init__(self, repository, analytics_db, file_manager):
        self.repository = repository
        self.analytics_db = analytics_db
        self.file_manager = file_manager
        self.table_name = self.repository.MODEL.__tablename__

    def run(self):
        filename = self.generate_jsonl_file()
        #uploaded_file = self.file_manager.upload_file(filename)
        #self.analytics_db.load_table_from_file(self.table_name, uploaded_file)

    def generate_jsonl_file(self):
        filepath = f'./tmp/pump_{self.table_name}.jsonl'
        with open(filepath, 'w') as f:
            rs = self.repository.get_list(filter=None, page_size = self.BATCH_SIZE)

            while len(rs) > 0:
                for pg_row in rs:
                    json_line = {c: pg_row.__dict__[c] for c in PUMP_CONFIG[self.table_name]}
                    f.write(str(json_line) + "\n")
                last_id = rs[-1].id
                rs = self.repository.get_list(filter=f"id >{last_id}", page_size = self.BATCH_SIZE)
        return filepath
        