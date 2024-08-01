import sqlite3 
from models.creature import Creatures

DB_NAME = "cryptid.db"
conn = sqlite3.connect(DB_NAME)
