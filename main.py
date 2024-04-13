from PyQt5 import uic, QtWidgets
import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='daily_quest_database'
)

print('CONECTADO COM SUCESSO AO BANCO daily_quest_database')
cursor = conexao.cursor(dictionary=True)

cursor.execute('SELECT * FROM users')
resultado = cursor.fetchall()
print(resultado)

#  AÇÕES

login_screen = uic.loadUi('loginScreen')