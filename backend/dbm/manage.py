# Fernando Lavarreda
# Manage the reads and writes to db

import sqlite3 as sql

def call_beam(dbloc:str, name:str)->list:
    db = sql.connect(dbloc)
    cursor = db.cursor()
    matches = list(cursor.execute("""SELECT * FROM beam WHERE name LIKE ?;""", (f"{name}%",)))
    db.close()
    return matches


def call_material(dbloc:str, name:str):
    db = sql.connect(dbloc)
    cursor = db.cursor()
    match = list(cursor.execute("""SELECT * FROM material WHERE name=(?);""", (name,)).fetchone())
    db.close()
    return match


def write_beams(dbloc:str, info:list):
    db = sql.connect(dbloc)
    cursor = db.cursor()
    cursor.executemany("""INSERT INTO beam VALUES(?, ?, ?, ?, ?, ?)""", info)
    db.commit()
    db.close()


def write_materials(dbloc:str, info:list):
    db = sql.connect(dbloc)
    cursor = db.cursor()
    cursor.executemany("""INSERT INTO material VALUES(?, ?, ?, ?)""", info)
    db.commit()
    db.close()