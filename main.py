from PyQt5 import  uic,QtWidgets
import sqlite3


def listar_dados():
    tela_2.show()
    banco = sqlite3.connect('banco_cadastro.db') 
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM dados")
    dados_lidos = cursor.fetchall()
    tela_2.tableWidget.setRowCount(len(dados_lidos))
    tela_2.tableWidget.setColumnCount(3)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 3):
           tela_2.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    
    banco.close()
    

def salvar_dados():
    nome = tela.lineEdit.text()
    endereco = tela.lineEdit_3.text()
    email = tela.lineEdit_2.text()
    
    try:
        banco = sqlite3.connect('banco_cadastro.db') 
        cursor = banco.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS dados (nome text,endereco text,email text)")
        cursor.execute("INSERT INTO dados VALUES ('"+nome+"','"+endereco+"','"+email+"')")
        banco.commit() 
        banco.close()
        tela.lineEdit.setText("")
        tela.lineEdit_2.setText("")
        tela.lineEdit_3.setText("")
        print("Dados inseridos com sucesso!")

    except sqlite3.Error as erro:
        print("Erro ao inserir os dados: ",erro)
   
app=QtWidgets.QApplication([])
tela=uic.loadUi("formulario.ui")
tela_2 = uic.loadUi("listar_dados.ui") 
tela.pushButton.clicked.connect(salvar_dados)
tela.pushButton_2.clicked.connect(listar_dados)

tela.show()
app.exec()


