import sqlite3

SQL_CREATE = "CREATE TABLE entities (entity TEXT PRIMARY KEY, label TEXT, occurrences TEXT)"
SQL_SELECT = "SELECT * FROM entities"
SQL_INSERT = "INSERT INTO entities VALUES (?, ?, ?)"
SQL_UPDATE = "UPDATE entities SET occurrences= occurrences + (?) WHERE entity=(?)"


class DatabaseConnection(object):

    def __init__(self, filename):
        self.connection = sqlite3.connect(filename, check_same_thread=False)

    def create_schema(self):
        try:
            self.connection.execute(SQL_CREATE)
        except sqlite3.OperationalError:
            print("Warning: the table was already created, ignoring...")

    def get(self, entity=None):
        cursor = (self.connection.execute(f'{SQL_SELECT} WHERE entity="{entity}"')
                  if entity is not None else self.connection.execute(SQL_SELECT))
        return cursor.fetchall()

    def add(self, entity, label):
        try:
            self.connection.execute(SQL_INSERT, (entity, label, 1))
            self.connection.commit()
        except sqlite3.IntegrityError:
            self.connection.execute(SQL_UPDATE, (1, entity))
            self.connection.commit()


def create_db(db_name=None):
    dbname = db_name if db_name else 'tmp'
    connection = DatabaseConnection(f'{dbname}.sqlite')
    connection.create_schema()
    return connection


if __name__ == '__main__':
    create_db()
