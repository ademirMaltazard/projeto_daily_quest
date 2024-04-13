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
loggeduser = {}

#  FUNÇÕES
def CheckLogin():
    userLogin = loginScreen.lineEdit_login.text()
    userPassword = loginScreen.lineEdit_password.text()

    query = 'SELECT * FROM users WHERE login_user = %s'
    cursor.execute(query, (userLogin,))
    result = cursor.fetchall()
    print(result)

    if len(result) <= 0:
        alertScreen.show()
    else:
        if result[0]['password_user'] == userPassword:
            print(result[0]['login_user'])
            global loggeduser
            loggeduser = result[0]
            loginScreen.close()
            missionScreen.show()
        else:
            alertScreen.show()


def CloseScreenAlert():
    alertScreen.close()
    loginScreen.lineEdit_login.setText('')
    loginScreen.lineEdit_password.setText('')

#  GERANDO UMA APLICAÇÃO
app = QtWidgets.QApplication([])

#  CARREGAR ARQUIVO UI
loginScreen = uic.loadUi('loginScreen.ui')
missionScreen = uic.loadUi('missionScreen.ui')
alertScreen = uic.loadUi('alert.ui')

#  AÇÕES
loginScreen.pushButton_login.clicked.connect(CheckLogin)
alertScreen.pushButton_confirm.clicked.connect(CloseScreenAlert)

#  EXIBIR NA TELA
loginScreen.show()
app.exec()