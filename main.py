from PyQt5 import uic, QtWidgets, QtCore
from db import databaseCRUD


loggedUser = {}

#  FUNÇÕES
def CheckLogin():
    userLogin = loginScreen.lineEdit_login.text()
    userPassword = loginScreen.lineEdit_password.text()

    result = databaseCRUD().SearchOne(userLogin)

    if result is None:
        print(result)
        alertScreen.show()
    else:
        if result['password_user'] == userPassword:
            global loggedUser
            loggedUser = result
            ShowQuests()
            loginScreen.close()
        else:
            result = None
            alertScreen.show()
            print(result)


def CloseScreenAlert():
    alertScreen.close()
    loginScreen.lineEdit_login.setText('')
    loginScreen.lineEdit_password.setText('')

def ShowQuests():
    missionScreen.show()
    activeQuest = databaseCRUD().SearchExercise()
    print(activeQuest)
    missionScreen.tableWidget_quest.setRowCount(len(activeQuest))

    row = 0
    for indice in activeQuest:
        print((indice))
        missionScreen.tableWidget_quest.setItem(row, 0, QtWidgets.QTableWidgetItem(indice["quantity_exercise"]))
        missionScreen.tableWidget_quest.setItem(row, 1, QtWidgets.QTableWidgetItem(indice["name_exercise"]))
        row += 1

    activePunition = databaseCRUD().SerachPunition()
    print(activePunition)
    missionScreen.tableWidget_punition.setRowCount(len(activePunition))

    row = 0
    for indice in activePunition:
        print((indice))
        missionScreen.tableWidget_punition.setItem(row, 0, QtWidgets.QTableWidgetItem(indice["name_punition"]))
        missionScreen.tableWidget_punition.setItem(row, 1, QtWidgets.QTableWidgetItem(indice["quantity_punition"]))
        missionScreen.tableWidget_punition.setItem(row, 2, QtWidgets.QTableWidgetItem(indice["description_punition"]))
        row += 1

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