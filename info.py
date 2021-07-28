import random
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
import devs 

# int(Forms2.TempoExecucao_1.text()), int(Forms2.OrdemChegada_1.text()), int(Forms2.Prioridade_1.text())
####################################### 2 PROCESSOS ##############################################
def GerarCrit2(index):
    if Processos2.TipoEscala.currentText() == 'SJF':
        Processos2.TipoDesempate.setEnabled(True)
        Processos2.TipoDesempate.clear()
        Processos2.TipoDesempate.addItem("FIFO")
        Processos2.TipoDesempate.addItem("Por Prioridade")
    elif Processos2.TipoEscala.currentText() == 'Por Prioridade':
        Processos2.TipoDesempate.setEnabled(True)
        Processos2.TipoDesempate.clear()
        Processos2.TipoDesempate.addItem("FIFO")
        Processos2.TipoDesempate.addItem("SJF")
    elif Processos2.TipoEscala.currentText() == 'FIFO':
        Processos2.TipoDesempate.setEnabled(False)

    
def GerarTabela2():
    TipoEscalonamento = Processos2.TipoEscala.currentText()
    try:
        processos = [
            ('P1', int(Processos2.TempoExecucao_1.text()), int(Processos2.OrdemChegada_1.text()), int(Processos2.Prioridade_1.text())),
            ('P2', int(Processos2.TempoExecucao_2.text()), int(Processos2.OrdemChegada_2.text()), int(Processos2.Prioridade_2.text())),
            ]
        if TipoEscalonamento == 'FIFO':
            devs.GerarTabela(devs.calcularFIFO(processos))
        elif TipoEscalonamento == 'SJF':
            if Processos2.TipoDesempate.currentText() == 'FIFO':
                devs.GerarTabela(devs.calcularSJF(processos, 1))
            elif Processos2.TipoDesempate.currentText() == 'Por Prioridade':
                devs.GerarTabela(devs.calcularSJF(processos, 2))
        elif TipoEscalonamento == 'Por Prioridade':
            if Processos2.TipoDesempate.currentText() == 'FIFO':
                devs.GerarTabela(devs.calcularPorPrioridade(processos, 2))
            elif Processos2.TipoDesempate.currentText() == 'SJF':
                devs.GerarTabela(devs.calcularPorPrioridade(processos, 1))
    except ValueError:
        QMessageBox.about(Processos2, "Error Detectado", "Falta valores ou algo foi digitado errado!")

def GerarNum2():
    Processos2.TempoExecucao_1.setText(str(random.randrange(1, 101)))
    Processos2.OrdemChegada_1.setText('1')
    Processos2.Prioridade_1.setText(str(random.randrange(1, 256)))
    Processos2.TempoExecucao_2.setText(str(random.randrange(1, 101)))
    Processos2.OrdemChegada_2.setText('2')
    Processos2.Prioridade_2.setText(str(random.randrange(1, 256)))
####################################### 3 PROCESSOS ##############################################
def GerarCrit3(index):
    if Processos3.TipoEscala.currentText() == 'SJF':
        Processos3.TipoDesempate.setEnabled(True)
        Processos3.TipoDesempate.clear()
        Processos3.TipoDesempate.addItem("FIFO")
        Processos3.TipoDesempate.addItem("Por Prioridade")
    elif Processos3.TipoEscala.currentText() == 'Por Prioridade':
        Processos3.TipoDesempate.setEnabled(True)
        Processos3.TipoDesempate.clear()
        Processos3.TipoDesempate.addItem("FIFO")
        Processos3.TipoDesempate.addItem("SJF")
    elif Processos3.TipoEscala.currentText() == 'FIFO':
        Processos3.TipoDesempate.setEnabled(False)

    
def GerarTabela3():
    TipoEscalonamento = Processos3.TipoEscala.currentText()
    try:
        processos = [
            ('P1', int(Processos3.TempoExecucao_1.text()), int(Processos3.OrdemChegada_1.text()), int(Processos3.Prioridade_1.text())),
            ('P2', int(Processos3.TempoExecucao_2.text()), int(Processos3.OrdemChegada_2.text()), int(Processos3.Prioridade_2.text())),
            ('P3', int(Processos3.TempoExecucao_3.text()), int(Processos3.OrdemChegada_3.text()), int(Processos3.Prioridade_3.text())),
            ]
        if TipoEscalonamento == 'FIFO':
            devs.GerarTabela(devs.calcularFIFO(processos))
        elif TipoEscalonamento == 'SJF':
            if Processos3.TipoDesempate.currentText() == 'FIFO':
                devs.GerarTabela(devs.calcularSJF(processos, 1))
            elif Processos3.TipoDesempate.currentText() == 'Por Prioridade':
                devs.GerarTabela(devs.calcularSJF(processos, 2))
        elif TipoEscalonamento == 'Por Prioridade':
            if Processos3.TipoDesempate.currentText() == 'FIFO':
                devs.GerarTabela(devs.calcularPorPrioridade(processos, 2))
            elif Processos3.TipoDesempate.currentText() == 'SJF':
                devs.GerarTabela(devs.calcularPorPrioridade(processos, 1))
    except ValueError:
        QMessageBox.about(Processos3, "Error Detectado", "Falta valores ou algo foi digitado errado!")

def GerarNum3():
    Processos3.TempoExecucao_1.setText(str(random.randrange(1, 101)))
    Processos3.OrdemChegada_1.setText('1')
    Processos3.Prioridade_1.setText(str(random.randrange(1, 256)))
    Processos3.TempoExecucao_2.setText(str(random.randrange(1, 101)))
    Processos3.OrdemChegada_2.setText('2')
    Processos3.Prioridade_2.setText(str(random.randrange(1, 256)))
    Processos3.TempoExecucao_3.setText(str(random.randrange(1, 101)))
    Processos3.OrdemChegada_3.setText('3')
    Processos3.Prioridade_3.setText(str(random.randrange(1, 256)))
####################################### 4 PROCESSOS ##############################################
def GerarCrit4(index):
    if Processos4.TipoEscala.currentText() == 'SJF':
        Processos4.TipoDesempate.setEnabled(True)
        Processos4.TipoDesempate.clear()
        Processos4.TipoDesempate.addItem("FIFO")
        Processos4.TipoDesempate.addItem("Por Prioridade")
    elif Processos4.TipoEscala.currentText() == 'Por Prioridade':
        Processos4.TipoDesempate.setEnabled(True)
        Processos4.TipoDesempate.clear()
        Processos4.TipoDesempate.addItem("FIFO")
        Processos4.TipoDesempate.addItem("SJF")
    elif Processos4.TipoEscala.currentText() == 'FIFO':
        Processos4.TipoDesempate.setEnabled(False)

    
def GerarTabela4():
    TipoEscalonamento = Processos4.TipoEscala.currentText()
    try:
        processos = [
            ('P1', int(Processos4.TempoExecucao_1.text()), int(Processos4.OrdemChegada_1.text()), int(Processos4.Prioridade_1.text())),
            ('P2', int(Processos4.TempoExecucao_2.text()), int(Processos4.OrdemChegada_2.text()), int(Processos4.Prioridade_2.text())),
            ('P3', int(Processos4.TempoExecucao_3.text()), int(Processos4.OrdemChegada_3.text()), int(Processos4.Prioridade_3.text())),
            ('P4', int(Processos4.TempoExecucao_4.text()), int(Processos4.OrdemChegada_4.text()), int(Processos4.Prioridade_4.text()))
            ]
        if TipoEscalonamento == 'FIFO':
            devs.GerarTabela(devs.calcularFIFO(processos))
        elif TipoEscalonamento == 'SJF':
            if Processos4.TipoDesempate.currentText() == 'FIFO':
                devs.GerarTabela(devs.calcularSJF(processos, 1))
            elif Processos4.TipoDesempate.currentText() == 'Por Prioridade':
                devs.GerarTabela(devs.calcularSJF(processos, 2))
        elif TipoEscalonamento == 'Por Prioridade':
            if Processos4.TipoDesempate.currentText() == 'FIFO':
                devs.GerarTabela(devs.calcularPorPrioridade(processos, 2))
            elif Processos4.TipoDesempate.currentText() == 'SJF':
                devs.GerarTabela(devs.calcularPorPrioridade(processos, 1))
    except ValueError:
        QMessageBox.about(Processos4, "Error Detectado", "Falta valores ou algo foi digitado errado!")

def GerarNum4():
    Processos4.TempoExecucao_1.setText(str(random.randrange(1, 101)))
    Processos4.OrdemChegada_1.setText('1')
    Processos4.Prioridade_1.setText(str(random.randrange(1, 256)))
    Processos4.TempoExecucao_2.setText(str(random.randrange(1, 101)))
    Processos4.OrdemChegada_2.setText('2')
    Processos4.Prioridade_2.setText(str(random.randrange(1, 256)))
    Processos4.TempoExecucao_3.setText(str(random.randrange(1, 101)))
    Processos4.OrdemChegada_3.setText('3')
    Processos4.Prioridade_3.setText(str(random.randrange(1, 256)))
    Processos4.TempoExecucao_4.setText(str(random.randrange(1, 101)))
    Processos4.OrdemChegada_4.setText('4')
    Processos4.Prioridade_4.setText(str(random.randrange(1, 256)))

####################################### 5 PROCESSOS ##############################################
def GerarCrit5(index):
    if Processos5.TipoEscala.currentText() == 'SJF':
        Processos5.TipoDesempate.setEnabled(True)
        Processos5.TipoDesempate.clear()
        Processos5.TipoDesempate.addItem("FIFO")
        Processos5.TipoDesempate.addItem("Por Prioridade")
    elif Processos5.TipoEscala.currentText() == 'Por Prioridade':
        Processos5.TipoDesempate.setEnabled(True)
        Processos5.TipoDesempate.clear()
        Processos5.TipoDesempate.addItem("FIFO")
        Processos5.TipoDesempate.addItem("SJF")
    elif Processos5.TipoEscala.currentText() == 'FIFO':
        Processos5.TipoDesempate.setEnabled(False)

    
def GerarTabela5():
    TipoEscalonamento = Processos5.TipoEscala.currentText()
    try:
        processos = [
            ('P1', int(Processos5.TempoExecucao_1.text()), int(Processos5.OrdemChegada_1.text()), int(Processos5.Prioridade_1.text())),
            ('P2', int(Processos5.TempoExecucao_2.text()), int(Processos5.OrdemChegada_2.text()), int(Processos5.Prioridade_2.text())),
            ('P3', int(Processos5.TempoExecucao_3.text()), int(Processos5.OrdemChegada_3.text()), int(Processos5.Prioridade_3.text())),
            ('P4', int(Processos5.TempoExecucao_4.text()), int(Processos5.OrdemChegada_4.text()), int(Processos5.Prioridade_4.text())),
            ('P5', int(Processos5.TempoExecucao_5.text()), int(Processos5.OrdemChegada_5.text()), int(Processos5.Prioridade_5.text()))        
            ]
        if TipoEscalonamento == 'FIFO':
            devs.GerarTabela(devs.calcularFIFO(processos))
        elif TipoEscalonamento == 'SJF':
            if Processos5.TipoDesempate.currentText() == 'FIFO':
                devs.GerarTabela(devs.calcularSJF(processos, 1))
            elif Processos5.TipoDesempate.currentText() == 'Por Prioridade':
                devs.GerarTabela(devs.calcularSJF(processos, 2))
        elif TipoEscalonamento == 'Por Prioridade':
            if Processos5.TipoDesempate.currentText() == 'FIFO':
                devs.GerarTabela(devs.calcularPorPrioridade(processos, 2))
            elif Processos5.TipoDesempate.currentText() == 'SJF':
                devs.GerarTabela(devs.calcularPorPrioridade(processos, 1))
    except ValueError:
        QMessageBox.about(Processos5, "Error Detectado", "Falta valores ou algo foi digitado errado!")

def GerarNum5():
    Processos5.TempoExecucao_1.setText(str(random.randrange(1, 101)))
    Processos5.OrdemChegada_1.setText('1')
    Processos5.Prioridade_1.setText(str(random.randrange(1, 256)))
    Processos5.TempoExecucao_2.setText(str(random.randrange(1, 101)))
    Processos5.OrdemChegada_2.setText('2')
    Processos5.Prioridade_2.setText(str(random.randrange(1, 256)))
    Processos5.TempoExecucao_3.setText(str(random.randrange(1, 101)))
    Processos5.OrdemChegada_3.setText('3')
    Processos5.Prioridade_3.setText(str(random.randrange(1, 256)))
    Processos5.TempoExecucao_4.setText(str(random.randrange(1, 101)))
    Processos5.OrdemChegada_4.setText('4')
    Processos5.Prioridade_4.setText(str(random.randrange(1, 256)))
    Processos5.TempoExecucao_5.setText(str(random.randrange(1, 101)))
    Processos5.OrdemChegada_5.setText('5')
    Processos5.Prioridade_5.setText(str(random.randrange(1, 256)))

####################################### 6 PROCESSOS ##############################################
def GerarCrit6(index):
    if Processos6.TipoEscala.currentText() == 'SJF':
        Processos6.TipoDesempate.setEnabled(True)
        Processos6.TipoDesempate.clear()
        Processos6.TipoDesempate.addItem("FIFO")
        Processos6.TipoDesempate.addItem("Por Prioridade")
    elif Processos6.TipoEscala.currentText() == 'Por Prioridade':
        Processos6.TipoDesempate.setEnabled(True)
        Processos6.TipoDesempate.clear()
        Processos6.TipoDesempate.addItem("FIFO")
        Processos6.TipoDesempate.addItem("SJF")
    elif Processos6.TipoEscala.currentText() == 'FIFO':
        Processos6.TipoDesempate.setEnabled(False)

    
def GerarTabela6():
    TipoEscalonamento = Processos6.TipoEscala.currentText()
    try:
        processos = [
            ('P1', int(Processos6.TempoExecucao_1.text()), int(Processos6.OrdemChegada_1.text()), int(Processos6.Prioridade_1.text())),
            ('P2', int(Processos6.TempoExecucao_2.text()), int(Processos6.OrdemChegada_2.text()), int(Processos6.Prioridade_2.text())),
            ('P3', int(Processos6.TempoExecucao_3.text()), int(Processos6.OrdemChegada_3.text()), int(Processos6.Prioridade_3.text())),
            ('P4', int(Processos6.TempoExecucao_4.text()), int(Processos6.OrdemChegada_4.text()), int(Processos6.Prioridade_4.text())),
            ('P5', int(Processos6.TempoExecucao_5.text()), int(Processos6.OrdemChegada_5.text()), int(Processos6.Prioridade_5.text())),
            ('P6', int(Processos6.TempoExecucao_6.text()), int(Processos6.OrdemChegada_6.text()), int(Processos6.Prioridade_6.text()))          
            ]
        if TipoEscalonamento == 'FIFO':
            devs.GerarTabela(devs.calcularFIFO(processos))
        elif TipoEscalonamento == 'SJF':
            if Processos6.TipoDesempate.currentText() == 'FIFO':
                devs.GerarTabela(devs.calcularSJF(processos, 1))
            elif Processos6.TipoDesempate.currentText() == 'Por Prioridade':
                devs.GerarTabela(devs.calcularSJF(processos, 2))
        elif TipoEscalonamento == 'Por Prioridade':
            if Processos6.TipoDesempate.currentText() == 'FIFO':
                devs.GerarTabela(devs.calcularPorPrioridade(processos, 2))
            elif Processos6.TipoDesempate.currentText() == 'SJF':
                devs.GerarTabela(devs.calcularPorPrioridade(processos, 1))
    except ValueError:
        QMessageBox.about(Processos6, "Error Detectado", "Falta valores ou algo foi digitado errado!")

def GerarNum6():
    Processos6.TempoExecucao_1.setText(str(random.randrange(1, 101)))
    Processos6.OrdemChegada_1.setText('1')
    Processos6.Prioridade_1.setText(str(random.randrange(1, 256)))
    Processos6.TempoExecucao_2.setText(str(random.randrange(1, 101)))
    Processos6.OrdemChegada_2.setText('2')
    Processos6.Prioridade_2.setText(str(random.randrange(1, 256)))
    Processos6.TempoExecucao_3.setText(str(random.randrange(1, 101)))
    Processos6.OrdemChegada_3.setText('3')
    Processos6.Prioridade_3.setText(str(random.randrange(1, 256)))
    Processos6.TempoExecucao_4.setText(str(random.randrange(1, 101)))
    Processos6.OrdemChegada_4.setText('4')
    Processos6.Prioridade_4.setText(str(random.randrange(1, 256)))
    Processos6.TempoExecucao_5.setText(str(random.randrange(1, 101)))
    Processos6.OrdemChegada_5.setText('5')
    Processos6.Prioridade_5.setText(str(random.randrange(1, 256)))
    Processos6.TempoExecucao_6.setText(str(random.randrange(1, 101)))
    Processos6.OrdemChegada_6.setText('6')
    Processos6.Prioridade_6.setText(str(random.randrange(1, 256)))

################################### CARREGAR PROCESSOS #########################################
def carregarprocessos():
    valor = int(SelectProcess.process.currentText())
    SelectProcess.close()
    if valor == 2:
        Processos2.show()
    elif valor == 3:
        Processos3.show()
    elif valor == 4:
        Processos4.show()
    elif valor == 5:
        Processos5.show()
    elif valor == 6:
        Processos6.show()

def abrirprocessos(valor):
    print('abrindo com entrada')
    if valor == 2:
        Processos2.show()
    elif valor == 3:
        Processos3.show()
    elif valor == 4:
        Processos4.show()
    elif valor == 5:
        Processos5.show()
    elif valor == 6:
        Processos6.show()
####################################  MAIN  #########################################################
def abrirselect():
    SelectProcess.show()

#####################################################################################################
if __name__ == '__main__':
    Aplicativo = QtWidgets.QApplication([]) #Usar via .ui
    SQLlogin = uic.loadUi("SQL-Login.ui") #Selecionar arquivo .ui
    #################### 2 PROCESSOS ##########################################
    Processos2 = uic.loadUi("Processos2.ui")
    Processos2.GerarTabela.clicked.connect(GerarTabela2)
    Processos2.GerarRandom.triggered.connect(GerarNum2)
    Processos2.TipoEscala.activated.connect(GerarCrit2)
    #################### 3 PROCESSOS ##########################################
    Processos3 = uic.loadUi("Processos3.ui")
    Processos3.GerarTabela.clicked.connect(GerarTabela3)
    Processos3.GerarRandom.triggered.connect(GerarNum3)
    Processos3.TipoEscala.activated.connect(GerarCrit3)
    #################### 4 PROCESSOS ##########################################
    Processos4 = uic.loadUi("Processos4.ui")
    Processos4.GerarTabela.clicked.connect(GerarTabela4)
    Processos4.GerarRandom.triggered.connect(GerarNum4)
    Processos4.TipoEscala.activated.connect(GerarCrit4)
    #################### 5 PROCESSOS ##########################################
    Processos5 = uic.loadUi("Processos5.ui")
    Processos5.GerarTabela.clicked.connect(GerarTabela5)
    Processos5.GerarRandom.triggered.connect(GerarNum5)
    Processos5.TipoEscala.activated.connect(GerarCrit5)
    #################### 6 PROCESSOS ##########################################
    Processos6 = uic.loadUi("Processos6.ui")
    Processos6.GerarTabela.clicked.connect(GerarTabela6)
    Processos6.GerarRandom.triggered.connect(GerarNum6)
    Processos6.TipoEscala.activated.connect(GerarCrit6)
    ################### Seleção Processos #####################################
    SelectProcess = uic.loadUi("ProcessosSelect.ui")
    SelectProcess.LoadProcess.clicked.connect(carregarprocessos)
    ####################    Main    ###########################################
    Main = uic.loadUi("Main.ui")
    Main.AbrirProcesso.clicked.connect(abrirselect)
    Main.show()
    Aplicativo.exec() #Executar programa