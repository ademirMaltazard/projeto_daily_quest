from PyQt5 import uic, QtWidgets, QtCore
from db import databaseCRUD


loggedUser = {}

#  FUNÇÕES
def CheckLogin():
    global loggedUser
    userLogin = loginScreen.lineEdit_login.text()
    userPassword = loginScreen.lineEdit_password.text()

    result = databaseCRUD().SearchOne(userLogin)

    if result is None:
        alertScreen.show()
        loginScreen.lineEdit_login.setText("")
        loginScreen.lineEdit_password.setText("")
    else:
        if result['password_user'] == userPassword:
            loggedUser = result
            ShowDailyQuest()
            loginScreen.close()
        else:
            result = None
            alertScreen.show()
            loginScreen.lineEdit_login.setText("")
            loginScreen.lineEdit_password.setText("")

def CreateNewUser():
    name = singinScreen.lineEdit_name.text()
    login = singinScreen.lineEdit_login.text()
    password = singinScreen.lineEdit_password.text()
    confirmPassword = singinScreen.lineEdit_confirmPassword.text()
    cod = singinScreen.lineEdit_code.text()

    print(name, login, password, confirmPassword, cod)
    if (password == confirmPassword and name != '' and login != ''):
        databaseCRUD().CreateNewUser(name, login, password, cod)
        singinScreen.lineEdit_name.setText('')
        singinScreen.lineEdit_login.setText('')
        singinScreen.lineEdit_password.setText('')
        singinScreen.lineEdit_confirmPassword.setText('')
        singinScreen.lineEdit_code.setText('')
    else:
        alertScreen.show()
def CloseScreenAlert():
    alertScreen.close()
    loginScreen.lineEdit_login.setText('')
    loginScreen.lineEdit_password.setText('')

def ShowDailyQuest():
    missionScreen.show()
    activeQuest = databaseCRUD().SearchExercise()
    missionScreen.tableWidget_quest.setRowCount(len(activeQuest))

    row = 0
    for indice in activeQuest:
        missionScreen.tableWidget_quest.setItem(row, 0, QtWidgets.QTableWidgetItem(indice["quantity_exercise"]))
        missionScreen.tableWidget_quest.setItem(row, 1, QtWidgets.QTableWidgetItem(indice["name_exercise"]))
        row += 1

    activePunition = databaseCRUD().SerachPunition()
    missionScreen.tableWidget_punition.setRowCount(len(activePunition))

    row = 0
    for indice in activePunition:
        missionScreen.tableWidget_punition.setItem(row, 0, QtWidgets.QTableWidgetItem(indice["name_punition"]))
        missionScreen.tableWidget_punition.setItem(row, 1, QtWidgets.QTableWidgetItem(indice["quantity_punition"]))
        missionScreen.tableWidget_punition.setItem(row, 2, QtWidgets.QTableWidgetItem(indice["description_punition"]))
        row += 1

def ReturnScreen(ui1, ui2):
    ui1.close()
    ui2.show()

def SiginToLogin():
    ReturnScreen(singinScreen, loginScreen)

def LoginToSingin():
    ReturnScreen(loginScreen, singinScreen)

def MissionToLogin():
    global loggedUser
    ReturnScreen(missionScreen, loginScreen)
    loginScreen.lineEdit_login.setText("")
    loginScreen.lineEdit_password.setText("")
    loggedUser = {}


#  GERANDO UMA APLICAÇÃO
app = QtWidgets.QApplication([])

#  CARREGAR ARQUIVO UI
loginScreen = uic.loadUi('loginScreen.ui')
missionScreen = uic.loadUi('missionScreen.ui')
singinScreen = uic.loadUi('singinScreen.ui')
alertScreen = uic.loadUi('alert.ui')

#  AÇÕES
alertScreen.pushButton_confirm.clicked.connect(CloseScreenAlert)
loginScreen.pushButton_login.clicked.connect(CheckLogin)
loginScreen.pushButton_singin.clicked.connect(LoginToSingin)
singinScreen.pushButton_singin.clicked.connect(CreateNewUser)
singinScreen.pushButton_logout.clicked.connect(SiginToLogin)
missionScreen.pushButton_logout.clicked.connect(MissionToLogin)

#  EXIBIR NA TELA
loginScreen.show()
app.exec()
