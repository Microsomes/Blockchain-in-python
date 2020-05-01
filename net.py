
##establishes connection to other nodes

import sqlite3


class Nodes:
    
    def addNode(self):
        pass

    def init(self):
        print("init init")
        db= sqlite3.connect("nodes.db")
        cur= db.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS clients (id INTEGER PRIMARY KEY AUTOINCREMENT, ver TEXT, hostname TEXT, lastAccessedunix TEXT)")
        db.commit()
        db.close()

    

