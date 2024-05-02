import mysql.connector

class databaseCRUD:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='daily_quest_database'
        )

        print('CONECTADO COM SUCESSO AO BANCO daily_quest_database')
        self.cursor = self.conexao.cursor(dictionary=True)

    def SearchOne(self, userLogin):
        query = 'SELECT * FROM users WHERE login_user = %s'
        self.cursor.execute(query, (userLogin,))
        result = self.cursor.fetchone()
        return result

    def SearchExercise(self):
        query = f'SELECT * FROM exercises WHERE status_exercise = "ativado"'
        print(query)
        self.cursor.execute(query)
        activeQuest = self.cursor.fetchall()
        return activeQuest

    def SerachPunition(self):
        query = f'SELECT * FROM punition WHERE status_punition = "ativado"'
        self.cursor.execute(query)
        activePunition = self.cursor.fetchall()
        return activePunition

#result = databaseCRUD().SearchByStatus()
#print(result)
