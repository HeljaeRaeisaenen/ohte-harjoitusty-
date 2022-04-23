'''Logging in and out'''
from database_connection import get_database_connection, close_database_connection


class Logging:
    '''Class containing all the methods for handling users and logging.
    Attributes:
        _connection = connection to the database used
        '''

    def __init__(self, connection):
        '''Setup the connection, call method for creating tables.
        '''
        self._connection = connection
        self._create_tables()

    def _create_tables(self):
        cursor = self._connection.cursor()

        cursor.execute('''
            create table if not exists users (
                username text primary key,
                password text
            );
        ''')

        self._connection.commit()

    def find_username(self, username):
        '''Search for a username. If doesn't exist, return False.
        Args:
            username = name to be searched, string
        Returns:
            bool
        '''
        cursor = self._connection.cursor()

        cursor.execute(
            "select username from users where username=?", (username,))

        rows = cursor.fetchall()
        if rows:
            return True
        return False

    def verify_password(self, username: str, password: str):
        '''Verify that the password matches the username
        Args:
            username = name to be searched, string
            password = password to be searched, string
        Returns:
            bool'''
        cursor = self._connection.cursor()

        cursor.execute(
            "select * from users where username=? and password=?", (username, password,))
        rows = cursor.fetchall()

        if rows:
            return True
        return False

    def create_username(self, name: str, password: str):
        '''Save a new username-password pair
        Args:
            username = name to be saved, string
            password = password to be saved, string
        '''
        sql_statement = ''' INSERT INTO users(username, password)
              VALUES(?,?) '''
        cursor = self._connection.cursor()
        cursor.execute(sql_statement, (name, password))
        self._connection.commit()

    def close_connection(self):
        '''Close the database'''
        close_database_connection(self._connection)


if __name__ == '__main__':
    l = Logging(get_database_connection())
    #l.create_username("jaako", "pouta")
    l.find_username("jaako")
    print(l.verify_password("jaako", "pouta"))
