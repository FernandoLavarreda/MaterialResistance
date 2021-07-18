# Fernando Lavarreda
# Manage information of the app

import sys
import sqlite3 as sql
from manage import write_beams
from outer import load as ld


def build(DBLOC = "")->None:
    db = sql.connect(DBLOC)
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE beam( name VARCHAR(20) UNIQUE,
                                        type VARCHAR(10),
                                        inertia INTEGER,
                                        area INTEGER,
                                        height INTEGER,
                                        weight INTEGER
                                        );
                                        """)
    cursor.execute("""CREATE TABLE material( name VARCHAR(20) UNIQUE,
                                            ymodulus REAL,
                                            comp_stress REAL,
                                            ten_stress REAL
                                            );""")
    db.commit()
    db.close()

# Assign colums separetely
# Call it from the main root folder
if __name__ == "__main__":
    build(sys.argv[1])
    if len(sys.argv)>2:
        cols = {"name":85, "type":1, "inertia":121, "area":88,"height":89, "weight":87}
        write_beams(sys.argv[1], ld.beam_xlsx(sys.argv[2], sys.argv[3], [i for i in range(int(sys.argv[4]), int(sys.argv[5]))], cols))