import unittest
from sqlalchemy import inspect

from repositories.base_repository import BaseRepository
from models.player import Player
from models.difficulty_level import DifficultyLevel
from models.game_config import GameConfig
from models.game_record import GameRecord

from config.test import DB_CONFIG

db_conn = BaseRepository(DB_CONFIG)

class DBTestFramework(unittest.TestCase):
    def setUp(self):
        self.__clear_db__()

    def tearDown(self):
        self.__clear_db__()

    def create_player(self, key, name = 'Player', type = 'human'):
        args = locals()
        return self.__create_and_return_record__(Player, args)

    def create_difficulty_level(self, key='normal', rank=1, prob_win=0.9, prob_block_win=0.9, prob_uno=0.9, prob_block_uno=0.9, prob_majority=0, prob_block_majority=0):
        args = locals()
        return self.__create_and_return_record__(DifficultyLevel, args)

    def create_game_config(self, locale='es', difficulty_level='normal'):
        args = locals()
        return self.__create_and_return_record__(GameConfig, args)

    def create_game_record(self, winner="player1", player1_type="cpu", player2_type="cpu", difficulty="normal", rules={}, moves=['r0c0'], hash_id="hash"):
        args = locals()
        return self.__create_and_return_record__(GameRecord, args)

    def __create_and_return_record__(self, klass, args_dict):
        id = self.__create_record__(klass, args_dict)
        return self.__get_record__(klass, id)

    def __create_record__(self, klass, args_dict):
        columns = inspect(klass).columns

        for k in list(args_dict.keys()):
            if k not in columns.keys():
                del args_dict[k]
            else:
                v = args_dict[k]
        
                # match case
                if type(v) in (str, dict):
                    args_dict[k] = f"'{v}'"
                elif type(v) == list:
                    args_dict[k] = "'{" + (",").join(v) + "}'"
                else:
                    args_dict[k] = str(v)
                #args_dict[k] =  if type(v) == list else v


        table = klass.__tablename__
        sql = f"""
            INSERT INTO {DB_CONFIG['schema']}.{table} ({(",").join(args_dict.keys())})
            VALUES({(",").join(args_dict.values())})
            RETURNING id;
        """

        id = db_conn.__execute_query__(sql).mappings().all()[0]['id']
        return id

    def __get_record__(self, klass, id):
        #table = klass.__tablename__
        obj = db_conn.__get_one_by_filter__(klass, klass.id == id)
        
        #sql = f"""
        #    SELECT *
        #    FROM  {DB_CONFIG['schema']}.{table}
        #    WHERE id = {id}
        #"""
        #row = db_conn.__execute_query__(sql).mappings().all()[0]

        #props = {i[0]: i[1] for i in row.items()}

        #obj = klass()
        #obj.__dict__ = props
        return obj
    
    def __clear_db__(self):
        # this should be done with a testing framework integrated with db, but whatever
        # intentionally decoupling it from the application's implementation as much as possible
        sql = f"""
            DO $$
            DECLARE
                t record;
            BEGIN
                FOR t IN (SELECT tablename FROM pg_tables WHERE schemaname = '{DB_CONFIG['schema']}') 
                LOOP
                    EXECUTE 'TRUNCATE {DB_CONFIG['schema']}.' || t.tablename || ';';
                END LOOP;
            END;
            $$
        """
        db_conn.__execute_query__(sql)
