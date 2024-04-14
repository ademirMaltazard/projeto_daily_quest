from PyQt5 import uic, QtWidgets
import mysql.connector
from PyQt5.QtWidgets import QTreeWidgetItem, QRadioButton

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='daily_quest_database'
)

print('CONECTADO COM SUCESSO AO BANCO daily_quest_database')
cursor = conexao.cursor(dictionary=True)

loggedUser = {}

#  FUNÇÕES
def CheckLogin():
    userLogin = loginScreen.lineEdit_login.text()
    userPassword = loginScreen.lineEdit_password.text()

    query = 'SELECT * FROM users WHERE login_user = %s'
    cursor.execute(query, (userLogin,))
    result = cursor.fetchone()

    if result is None:
        alertScreen.show()
    else:
        if result['password_user'] == userPassword:
            #print(result['login_user'])
            global loggedUser
            loggedUser = result
            ShowQuests()
            loginScreen.close()
        else:
            alertScreen.show()


def CloseScreenAlert():
    alertScreen.close()
    loginScreen.lineEdit_login.setText('')
    loginScreen.lineEdit_password.setText('')

def ShowQuests():
    missionScreen.show()
    query = f'SELECT * FROM exercises WHERE status_exercise = "ativado"'
    cursor.execute(query)
    activeQuest = cursor.fetchall()
    print(activeQuest)

    # missionScreen.treeWidget_quest
    # print('passou')
    #
    # row = 0
    # for indice in activeQuest:
    #     print('quantidade: ', indice['quantity_exercise'])
    #     # missionScreen.treeWidget_quest.setItem(row, 0, QRadioButton().create())
    #     missionScreen.treeWidget_quest.setItem(row, 1, QtWidgets.QTreeWidgetItem(indice['quantity_exercise']))
    #

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