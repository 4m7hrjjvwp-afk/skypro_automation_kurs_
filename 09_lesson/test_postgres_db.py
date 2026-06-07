from sqlalchemy import create_engine
from sqlalchemy.sql import text
from dotenv import load_dotenv
import os

load_dotenv()

db_connection_string = my_url_database


def test_db_connection():
    db = os.getenv(create_engine(db_connection_string))
    names = db.table_names()
    assert names[0] == 'subject'


def test_insert():
    db = os.getenv(create_engine(db_connection_string))
    max_id = db.execute("select MAX(subject_id) from subject").fetchone()[0]
    new_id = max_id + 1 if max_id else 1
    sql = text("insert into subject(\"subject_title\", \"subject_id\") "
               "values(:new_subject, :new_id)")
    fetched_subject = db.execute(f"SELECT subject_title FROM subject "
                                 f"WHERE subject_id={new_id}").fetchone()
    assert fetched_subject[0] == new_subject
    db.execute(sql, new_subject='Psychology', new_id=id)


def test_update():
    db = os.getenv(create_engine(db_connection_string))
    sql = text("update subject set subject_title = :update_title where id = :id")
    db.execute(sql, update_title='PSYchology', id=16)


def test_delete():
    db = create_engine(db_connection_string)
    sql = text("delete from subject where id = :id")
    db.execute(sql, id=16)
