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
                password text,
                timesused integer,
                average_wish_rate integer
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

        rows = cursor.fetchone()
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
        success = self.find_username(name)
        if success:
            return "username exists"
        sql_statement = ''' INSERT INTO users(username, password)
              VALUES(?,?) '''
        cursor = self._connection.cursor()
        cursor.execute(sql_statement, (name, password))
        self._connection.commit()
        return "ok"

    def add_statistics(self, username: str, wishrate: int):
        '''Add some fun facts to the database. Calculate new average percentage of wishes fulfilled
        '''
        success = self.find_username(username)
        if not success:
            return
        cursor = self._connection.cursor()

        cursor.execute(
            "select timesused, average_wish_rate from users where username=?", (username,))
        rows = cursor.fetchall()

        if not rows[0][0]:
            cursor.execute(
                "UPDATE users SET timesused=?, average_wish_rate=? where username=?",
                (1, wishrate, username,))
            self._connection.commit()
        else:
            cursor.execute(
                "select average_wish_rate from users where username=?",
                (username,))
            row = cursor.fetchone()
            new_avg = (row[0]+wishrate) // 2
            cursor.execute(
                "UPDATE users SET timesused=timesused+1, average_wish_rate=? where username=?",
                (new_avg, username,))
            self._connection.commit()

    def view_statistics(self, username: str):
        '''View timesused and average_wish_rate of username
        Args:
            username
        Returns:
            tuple ()'''
        cursor = self._connection.cursor()

        cursor.execute(
            "select timesused, average_wish_rate from users where username=?", (username,))
        rows = cursor.fetchone()
        if not rows:
            return 0, 0
        return rows[0], rows[1]

    def close_connection(self):
        '''Close the database'''
        close_database_connection(self._connection)


if __name__ == '__main__':
    l = Logging(get_database_connection())
    #l.create_username("jakko", "pouta")
    l.find_username("jakko")
    print(l.verify_password("jaako", "pouta"))
    l.add_statistics("jakko", 60)
    l.add_statistics("jakko", 90)
