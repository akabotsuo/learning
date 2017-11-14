import sqlite3
from db.SQL import *
from ChatGame.Followers import follow_check
from db.SQL_tables import *
from ChatGame.Followers import *


def init_once():
    followers_table_init()
    champions_table_init()
    database_table()
    try:
        new_follower("Followers", "ehemil", "Green")
        new_follower("Followers", "senzore", "Red")
    except:
        pass
