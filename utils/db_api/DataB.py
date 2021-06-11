import sqlite3


class db:
    def __init__(self, path_to_db='Users.db'):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False,
                fetchall=False, commit=False):
        if not parameters:
            parameters = tuple()
        data = None
        connection = self.connection
        cursor = connection.cursor()
        cursor.execute(sql, parameters)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    def create_table_users(self):
        sql = '''
        CREATE TABLE Users (
        UserId int,
        login_login varchar(255),
        login_password varchar(255),
        PRIMARY KEY (UserId)
        );
        '''
        self.execute(sql, commit=True)

    def add_user_to_Db(self, id: int, login_login: str, login_password: str):
        sql = 'INSERT INTO Users(UserId, login_login, login_password) VALUES(?, ?, ?)'
        parameters = (id, login_login, login_password)
        self.execute(sql, parameters=parameters, commit=True)

    def delete_user_from_db(self, id: int):
        sql = f"DELETE FROM Users Where UserId = {id}"
        self.execute(sql,commit=True)

    def select_user(self, id: int):
        sql = f'SELECT * FROM Users where UserId = {id}'
        return self.execute(sql,fetchone=True)

    def select_all(self):
        sql = 'SELECT * FROM Users'
        return self.execute(sql,fetchall=True)

    def logger(statement):
        print(f'Executing:{statement}')
