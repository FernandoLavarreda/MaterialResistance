# Fernando Lavarreda
# Manage information of the app

import sqlite3 as sql


def build(DBLOC = "")->None:
    db = sql.connect(DBLOC)
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE beam( name VARCHAR(20) UNIQUE,
                                        type VARCHAR(10),
                                        inertia INTEGER,
                                        area INTEGER,
                                        height INTEGER,
                                        weight INTEGER,
                                        );
                                        """)
    cursor.execute("""CREATE TABLE material( name VARCHAR(20) UNIQUE,
                                            ymodulus REAL,
                                            comp_stress REAL,
                                            ten_stress REAL
                                            );""")
    db.commit()
    db.close()