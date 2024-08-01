import os 
from pathlib import Path
from sqlite3 import connect , Connection , Cursor , IntegrityError

conn : Connection | None = None
curs : Cursor | None = None

def get_db(name: str|None , reset: bool = False) : 
    global conn , curs 
    if conn: 
        if not reset:
            return
        conn = None