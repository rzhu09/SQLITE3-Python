import sqlite3

def connect():

    connection = sqlite3.connect('Database_1')
    cur_sor = connection.cursor()
    cur_sor.execute("CREATE TABLE IF NOT EXISTS Database_1 (Id INTEGER PRIMARY KEY, date text, spendings integer, exercise text, study text, meals text, games text)")
    connection.commit()
    connection.close()


def insert(date, spendings, exercise, study, meals, games):

    connection = sqlite3.connect('Database_1')
    cur_sor = connection.cursor()
    cur_sor.execute("INSERT INTO Database_1 VALUES (NULL, ?,?,?,?,?,?)", (date, spendings, exercise, study, meals, games) )
    connection.commit()
    connection.close()


def view():
    connection = sqlite3.connect('Database_1')
    cur_sor = connection.cursor()
    cur_sor.execute("SELECT * FROM Database_1")
    row = cur_sor.fetchall()
    connection.commit()
    connection.close()
    return row


def delete(id):

    connection = sqlite3.connect('Database_1')
    cur_sor = connection.cursor()
    cur_sor.execute("DELETE FROM Database_1 WHERE id = ?", (id,))
    connection.commit()
    connection.close()


def search(date = '', spendings = '', exercise = '', study = '', meals = '', games = ''):

    connection = sqlite3.connect('Database_1')
    cur_sor = connection.cursor()
    cur_sor.execute("SELECT * FROM Database_1 WHERE date = ? OR spendings = ? OR exercise = ? OR study = ? OR meals = ? OR games = ?", (date, spendings, exercise, study, meals, games))
    row = cur_sor.fetchall()
    connection.commit()
    connection.close()
    return row

def update(id, date, spendings, exercise, study, meals, games):
    connection = sqlite3.connect('Database_1')
    cur_sor = connection.cursor()
    cur_sor.execute("""UPDATE Database_1 SET date = ?, spendings = ?, exercise = ?, study = ?, meals = ?, games = ? WHERE id = ?""", (date, spendings, exercise, study, meals, games, id) )
    connection.commit()
    connection.close()

connect()

#update(2,'1-12-2019', 200, 'lazy', 'lazy study', 'ate pot rice', 'csgo')

#print(view())