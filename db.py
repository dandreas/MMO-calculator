import sqlite3

def getDb():
    db = sqlite3.connect(
        "ItemDB",
        detect_types=sqlite3.PARSE_DECLTYPES
    )
    db.row_factory = sqlite3.Row

    return db

def closeDb(e=None):
    global db

    if db is not None:
        db.close()

def initDb():
    global db
    with open('schema.sql') as schemaFile:
        db.executescript(schemaFile.read().decode('utf8'))

db = getDb()