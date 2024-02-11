import sqlite3

class Database:
    def __init__(self) -> None:
        self.conn=sqlite3.connect('db.db',check_same_thread=False)
        self.cursor = self.conn.cursor()


    def get_user(self,id):
        self.cursor.execute(f"SELECT name FROM users WHERE id={id}")
        return self.cursor.fetchone()
    

    def register(self,name,id):
        self.cursor.execute(f'INSERT INTO users (id, name) VALUES (?, ?)',(id, name))
        self.conn.commit()
        return True    

    def update_balance(self,id,balance,status):
        if status:
            self.cursor.execute(f'UPDATE users SET balance=balance+?',(balance,id))
        else:
            self.cursor.execute(f'UPDATE users SET balance=balance+?',(balance,id))
        self.conn.commit()
        return True
