from sqlalchemy import create_engine
from sqlalchemy.sql import text
from dotenv import load_dotenv
import os

load_dotenv()

db_connection_string = os.getenv("my_url_database")


def test_db_connection():
    db = create_engine(db_connection_string)
    names = db.table_names()
    assert names[0] == 'subject'


def test_insert():
    db = create_engine(db_connection_string)
    max_id = db.execute("select MAX(subject_id) from subject").fetchone()[0]
    new_id = max_id + 1 if max_id else 1
    sql = text("insert into subject(\"subject_title\", \"subject_id\") "
               "values(:new_subject, :new_id)")
    db.execute(sql, new_subject='Psychology', new_id=new_id)
    new_subject = 'Psychology'
    fetched_subject = db.execute(f"SELECT subject_title FROM subject "
                                 f"WHERE subject_id={new_id}").fetchone()
    assert fetched_subject[0] == new_subject
    db.execute(text("delete from subject where subject_id = :id"),
               {"id": new_id})


def test_update():
    db = create_engine(db_connection_string)
    sql = text("update subject set subject_title = :update_title "
               "where subject_id = :id")
    updated = db.execute(sql, update_title='PSYchology', id=16)
    update_title = 'PSYchology'
    assert updated["subject_title"] == update_title
    db.execute(text("delete from subject where subject_title = :title"),
               {"title": update_title})


def test_delete():
    db = create_engine(db_connection_string)
    sql = text("delete from subject where subjaect_id = :id")
    db.execute(sql, id=16)
    chek = db.execute(text("select * from subject_id = :id"),
                      {"id": 16}).fetchone()
    assert chek is None
