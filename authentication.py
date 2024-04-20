import sqlite3
import base64


class Account:
    def check_have_account(self, encode_signin_password):
        with sqlite3.connect('movies_project.db') as connection:
            cursor = connection.cursor()
            cursor.execute('''SELECT * FROM Account WHERE nick = ? OR email = ? AND password = ?''',
                           (self.signin_nick_for_db, self.signin_email_for_db, encode_signin_password))
            account = cursor.fetchone()
        if account:
            print('Login successful!')
            return True
        else:
            print('Invalid credentials.')
            return False

    def signin(self):
        self.signin_nick_for_db = input('Please enter Nick:\t')
        self.signin_email_for_db = input('Please enter Email:\t')
        self.signin_password_for_db = input('Please enter Password:\t')
        encode_signin_password = base64.b64encode(self.signin_password_for_db.encode()).decode()
        return self.check_have_account(encode_signin_password)

    def registration(self):
        self.login_nick_for_db = input('Please enter your Nick:\t')
        self.login_email_for_db = input('Please enter your Email:\t')
        self.login_password_for_db = input('Please enter your Password:\t')
        encode_login_password = base64.b64encode(self.login_password_for_db.encode()).decode()
        return self.input_info_for_login(encode_login_password)

    def input_info_for_login(self, encode_login_password):
        with sqlite3.connect('movies_project.db') as connection:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO Account(nick, email, password) VALUES (?, ?, ?)',
                           (self.login_nick_for_db, self.login_email_for_db, encode_login_password))
            account = cursor.fetchone()
        if account:
            print('Registration successful!')
            return True
        else:
            print('Invalid credentials.')
            return False

    def account_info(self):
        self.loves_film_name = input('Enter your loves film name:\t')
        self.loves_serial_name = input('Enter your loves serial name:\t')
        self.loves_genre_name1 = input('Enter your loves genre name one:\t')
        self.loves_genre_name2 = input('Enter your loves genre name two:\t')
        self.loves_genre_name3 = input('Enter your loves genre name three:\t')
        self.loves_actor_name = input('Enter your loves actor name:\t')
        self.input_info_for_account_info()

    def input_info_for_account_info(self):
        with sqlite3.connect('movies_project.db') as connection:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO Account_info(loves_film_name, loves_serial_name, loves_genre_name1, '
                           'loves_genre_name2, loves_genre_name3, loves_actor) VALUES (?, ?, ?, ?, ?, ?)',
                           (self.loves_film_name, self.loves_serial_name, self.loves_genre_name1,
                            self.loves_genre_name2, self.loves_genre_name3, self.loves_actor_name))
        print("Information entered successfully.")
