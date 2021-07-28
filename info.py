import random
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
import devs 
import pyodbc

ConnectServer: bool = False
NomeServer: str
NomeBanco: str

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

def LimparCampos2():
    Processos2.TempoExecucao_1.setText("")
    Processos2.OrdemChegada_1.setText("")
    Processos2.Prioridade_1.setText("")
    Processos2.TempoExecucao_2.setText("")
    Processos2.OrdemChegada_2.setText("")
    Processos2.Prioridade_2.setText("")

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

def LimparCampos3():
    Processos3.TempoExecucao_1.setText("")
    Processos3.OrdemChegada_1.setText("")
    Processos3.Prioridade_1.setText("")
    Processos3.TempoExecucao_2.setText("")
    Processos3.OrdemChegada_2.setText("")
    Processos3.Prioridade_2.setText("")
    Processos3.TempoExecucao_3.setText("")
    Processos3.OrdemChegada_3.setText("")
    Processos3.Prioridade_3.setText("")

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

def LimparCampos4():
    Processos4.TempoExecucao_1.setText("")
    Processos4.OrdemChegada_1.setText("")
    Processos4.Prioridade_1.setText("")
    Processos4.TempoExecucao_2.setText("")
    Processos4.OrdemChegada_2.setText("")
    Processos4.Prioridade_2.setText("")
    Processos4.TempoExecucao_3.setText("")
    Processos4.OrdemChegada_3.setText("")
    Processos4.Prioridade_3.setText("")
    Processos4.TempoExecucao_4.setText("")
    Processos4.OrdemChegada_4.setText("")
    Processos4.Prioridade_4.setText("")

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

def LimparCampos5():
    Processos5.TempoExecucao_1.setText("")
    Processos5.OrdemChegada_1.setText("")
    Processos5.Prioridade_1.setText("")
    Processos5.TempoExecucao_2.setText("")
    Processos5.OrdemChegada_2.setText("")
    Processos5.Prioridade_2.setText("")
    Processos5.TempoExecucao_3.setText("")
    Processos5.OrdemChegada_3.setText("")
    Processos5.Prioridade_3.setText("")
    Processos5.TempoExecucao_4.setText("")
    Processos5.OrdemChegada_4.setText("")
    Processos5.Prioridade_4.setText("")
    Processos5.TempoExecucao_5.setText("")
    Processos5.OrdemChegada_5.setText("")
    Processos5.Prioridade_5.setText("")

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

def LimparCampos6():
    Processos6.TempoExecucao_1.setText("")
    Processos6.OrdemChegada_1.setText("")
    Processos6.Prioridade_1.setText("")
    Processos6.TempoExecucao_2.setText("")
    Processos6.OrdemChegada_2.setText("")
    Processos6.Prioridade_2.setText("")
    Processos6.TempoExecucao_3.setText("")
    Processos6.OrdemChegada_3.setText("")
    Processos6.Prioridade_3.setText("")
    Processos6.TempoExecucao_4.setText("")
    Processos6.OrdemChegada_4.setText("")
    Processos6.Prioridade_4.setText("")
    Processos6.TempoExecucao_5.setText("")
    Processos6.OrdemChegada_5.setText("")
    Processos6.Prioridade_5.setText("")
    Processos6.TempoExecucao_6.setText("")
    Processos6.OrdemChegada_6.setText("")
    Processos6.Prioridade_6.setText("")
####################################### 6 PROCESSOS ##############################################
def GerarCrit7(index):
    if Processos7.TipoEscala.currentText() == 'SJF':
        Processos7.TipoDesempate.setEnabled(True)
        Processos7.TipoDesempate.clear()
        Processos7.TipoDesempate.addItem("FIFO")
        Processos7.TipoDesempate.addItem("Por Prioridade")
    elif Processos7.TipoEscala.currentText() == 'Por Prioridade':
        Processos7.TipoDesempate.setEnabled(True)
        Processos7.TipoDesempate.clear()
        Processos7.TipoDesempate.addItem("FIFO")
        Processos7.TipoDesempate.addItem("SJF")
    elif Processos7.TipoEscala.currentText() == 'FIFO':
        Processos7.TipoDesempate.setEnabled(False)

    
def GerarTabela7():
    TipoEscalonamento = Processos7.TipoEscala.currentText()
    try:
        processos = [
            ('P1', int(Processos7.TempoExecucao_1.text()), int(Processos7.OrdemChegada_1.text()), int(Processos7.Prioridade_1.text())),
            ('P2', int(Processos7.TempoExecucao_2.text()), int(Processos7.OrdemChegada_2.text()), int(Processos7.Prioridade_2.text())),
            ('P3', int(Processos7.TempoExecucao_3.text()), int(Processos7.OrdemChegada_3.text()), int(Processos7.Prioridade_3.text())),
            ('P4', int(Processos7.TempoExecucao_4.text()), int(Processos7.OrdemChegada_4.text()), int(Processos7.Prioridade_4.text())),
            ('P5', int(Processos7.TempoExecucao_5.text()), int(Processos7.OrdemChegada_5.text()), int(Processos7.Prioridade_5.text())),
            ('P6', int(Processos7.TempoExecucao_6.text()), int(Processos7.OrdemChegada_6.text()), int(Processos7.Prioridade_6.text())),
            ('P7', int(Processos7.TempoExecucao_7.text()), int(Processos7.OrdemChegada_7.text()), int(Processos7.Prioridade_7.text()))           
            ]
        if TipoEscalonamento == 'FIFO':
            devs.GerarTabela(devs.calcularFIFO(processos))
        elif TipoEscalonamento == 'SJF':
            if Processos7.TipoDesempate.currentText() == 'FIFO':
                devs.GerarTabela(devs.calcularSJF(processos, 1))
            elif Processos7.TipoDesempate.currentText() == 'Por Prioridade':
                devs.GerarTabela(devs.calcularSJF(processos, 2))
        elif TipoEscalonamento == 'Por Prioridade':
            if Processos7.TipoDesempate.currentText() == 'FIFO':
                devs.GerarTabela(devs.calcularPorPrioridade(processos, 2))
            elif Processos7.TipoDesempate.currentText() == 'SJF':
                devs.GerarTabela(devs.calcularPorPrioridade(processos, 1))
    except ValueError:
        QMessageBox.about(Processos7, "Error Detectado", "Falta valores ou algo foi digitado errado!")

def GerarNum7():
    Processos7.TempoExecucao_1.setText(str(random.randrange(1, 101)))
    Processos7.OrdemChegada_1.setText('1')
    Processos7.Prioridade_1.setText(str(random.randrange(1, 256)))
    Processos7.TempoExecucao_2.setText(str(random.randrange(1, 101)))
    Processos7.OrdemChegada_2.setText('2')
    Processos7.Prioridade_2.setText(str(random.randrange(1, 256)))
    Processos7.TempoExecucao_3.setText(str(random.randrange(1, 101)))
    Processos7.OrdemChegada_3.setText('3')
    Processos7.Prioridade_3.setText(str(random.randrange(1, 256)))
    Processos7.TempoExecucao_4.setText(str(random.randrange(1, 101)))
    Processos7.OrdemChegada_4.setText('4')
    Processos7.Prioridade_4.setText(str(random.randrange(1, 256)))
    Processos7.TempoExecucao_5.setText(str(random.randrange(1, 101)))
    Processos7.OrdemChegada_5.setText('5')
    Processos7.Prioridade_5.setText(str(random.randrange(1, 256)))
    Processos7.TempoExecucao_6.setText(str(random.randrange(1, 101)))
    Processos7.OrdemChegada_6.setText('6')
    Processos7.Prioridade_6.setText(str(random.randrange(1, 256)))
    Processos7.TempoExecucao_7.setText(str(random.randrange(1, 101)))
    Processos7.OrdemChegada_7.setText('6')
    Processos7.Prioridade_7.setText(str(random.randrange(1, 256)))

def LimparCampos7():
    Processos7.TempoExecucao_1.setText("")
    Processos7.OrdemChegada_1.setText("")
    Processos7.Prioridade_1.setText("")
    Processos7.TempoExecucao_2.setText("")
    Processos7.OrdemChegada_2.setText("")
    Processos7.Prioridade_2.setText("")
    Processos7.TempoExecucao_3.setText("")
    Processos7.OrdemChegada_3.setText("")
    Processos7.Prioridade_3.setText("")
    Processos7.TempoExecucao_4.setText("")
    Processos7.OrdemChegada_4.setText("")
    Processos7.Prioridade_4.setText("")
    Processos7.TempoExecucao_5.setText("")
    Processos7.OrdemChegada_5.setText("")
    Processos7.Prioridade_5.setText("")
    Processos7.TempoExecucao_6.setText("")
    Processos7.OrdemChegada_6.setText("")
    Processos7.Prioridade_6.setText("")
    Processos7.TempoExecucao_7.setText("")
    Processos7.OrdemChegada_7.setText("")
    Processos7.Prioridade_7.setText("")
################################### CARREGAR PROCESSOS #########################################
def carregarprocessos():
    valor = int(SelectProcess.process.currentText())
    SelectProcess.close()
    if valor == 2:
        LimparCampos2()
        Processos2.show()
    elif valor == 3:
        LimparCampos3()
        Processos3.show()
    elif valor == 4:
        LimparCampos4()
        Processos4.show()
    elif valor == 5:
        LimparCampos5()
        Processos5.show()
    elif valor == 6:
        LimparCampos6()
        Processos6.show()
    elif valor == 7:
        LimparCampos7()
        Processos7.show()

def abrirprocessos(valor):
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
    elif valor == 7:
        LimparCampos7()
        Processos7.show()
############################## CONNECTAR SQL ########################################################

def conexaobanco(nomeserver: str, nomebanco: str):
    #conexao = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';UID='+username+';PWD='+ password
    conexao = "Driver={SQL Server Native Client 11.0};Server="+nomeserver+";Database="+nomebanco+";Trusted_Connection=yes;"
    return pyodbc.connect(conexao)

def buttonverif():
    if len(SQLlogin.SQLname.text()) > 8 and SQLlogin.SelectAut.currentText() == 'SQL Windows':
        SQLlogin.Connect.setEnabled(True)
    else:
        if len(SQLlogin.SQLLogin_Name.text()) > 6 and len(SQLlogin.SQLLogin_Senha.text()) > 6:
            SQLlogin.Connect.setEnabled(True)
        else:
            SQLlogin.Connect.setEnabled(False)

def sqlserver():
    if SQLlogin.SelectAut.currentText() == 'SQL Server':
        SQLlogin.label_name.setEnabled(True)
        SQLlogin.label_senha.setEnabled(True)
        SQLlogin.SQLLogin_Name.setEnabled(True)
        SQLlogin.SQLLogin_Senha.setEnabled(True)
    else:
        SQLlogin.label_name.setEnabled(False)
        SQLlogin.label_senha.setEnabled(False)
        SQLlogin.SQLLogin_Name.setEnabled(False)
        SQLlogin.SQLLogin_Senha.setEnabled(False)
        SQLlogin.SQLLogin_Name.setText("")
        SQLlogin.SQLLogin_Senha.setText("")

def ConnectarServidor():
    if SQLlogin.SelectAut.currentText() == 'SQL Windows':
        try:
            global NomeServer
            global NomeBanco
            global ConnectServer
            con = conexaobanco(SQLlogin.SQLname.text(), 'PIPESQL')
            cursor = con.cursor()
            cursor.close()
            con.close()
            NomeServer = SQLlogin.SQLname.text()
            NomeBanco = 'PIPESQL'
            ConnectServer = True
            QMessageBox.about(SQLlogin, "Conexão Realidade", "O banco está connectado e pronto para ser usado!")
            SQLlogin.close()
        except pyodbc.InterfaceError:
            QMessageBox.about(SQLlogin, "Erro de Conexão", "O banco não existe ou o servidor está incorreto!")
        except Exception:
            QMessageBox.about(SQLlogin, "Erro de Conexão", "O banco demorou a responder. Verifique se não existe dados errados")
    else:
        print('Enviar senha e nome também')
    
def devinfo():
    QMessageBox.about(Main, "Creditos", "Programa desenvolvido em 20/07/2021\nDeveloper: Willian Quirino / Dev Back-End\n\nPrograma desenvolvido para fins acadêmicos que visa o calculo de tabelas escalonadas para projetos de sistemas operações.\nO programa tem como apriomoramento de criação de tabelas FIFO/SJT/Por Prioridade utilizando processos de escalas.\n\n\nContatos: https://github.com/willianqf/Program-PIPELINE-")
def devinfo2():
    QMessageBox.about(Main, "Informações do Programa", "Este programa tem fins de calculo de escalonamento para processos operacionais.\n\nCalculos disponíiveis: FIFO/SJF/Por Prioridade\n\nComo usar o programa?\nDeve-se utilizar a quantidade de processos que queira calcular no botão 'Calcular Processos'\n\nComo gero relatório?\nO programa oferece um local que pode ser alterado no momento do save de relatório\n\nO programa é de código aberto?\nO programa pode ser acessado com seu código fonte através do canal do GIT disponível nos créditos")

####################################  MAIN  #########################################################
def abrirselect():
    SelectProcess.show()

def abrirsql():
    global ConnectServer
    if ConnectServer == False:
        SQLlogin.show()
    else:
        QMessageBox.about(Main, "Conexão já realizada", "Você já está conectado com o banco")

def CarregarPIPE():
    global ConnectServer
    if ConnectServer == True:
        print('Carregar PIPE')
    else:
        QMessageBox.about(Main, "Conexão não realizada", "Você precisa estar com o banco conectado para realizar consultas!")

#####################################################################################################
if __name__ == '__main__':
    Aplicativo = QtWidgets.QApplication([]) #Usar via .ui
    SQLlogin = uic.loadUi("SQL-Login.ui") #Selecionar arquivo .ui
    SQLlogin.SQLname.textChanged.connect(buttonverif)
    SQLlogin.SelectAut.activated.connect(buttonverif)
    SQLlogin.SelectAut.activated.connect(sqlserver)
    SQLlogin.SQLLogin_Senha.textChanged.connect(buttonverif)
    SQLlogin.SQLLogin_Name.textChanged.connect(buttonverif)
    SQLlogin.Connect.clicked.connect(ConnectarServidor)
    #################### 2 PROCESSOS ##########################################
    Processos2 = uic.loadUi("Processos2.ui")
    Processos2.GerarTabela.clicked.connect(GerarTabela2)
    Processos2.GerarRandom.triggered.connect(GerarNum2)
    Processos2.TipoEscala.activated.connect(GerarCrit2)
    Processos2.LimparCampos.triggered.connect(LimparCampos2)
    #################### 3 PROCESSOS ##########################################
    Processos3 = uic.loadUi("Processos3.ui")
    Processos3.GerarTabela.clicked.connect(GerarTabela3)
    Processos3.GerarRandom.triggered.connect(GerarNum3)
    Processos3.TipoEscala.activated.connect(GerarCrit3)
    Processos3.LimparCampos.triggered.connect(LimparCampos3)
    #################### 4 PROCESSOS ##########################################
    Processos4 = uic.loadUi("Processos4.ui")
    Processos4.GerarTabela.clicked.connect(GerarTabela4)
    Processos4.GerarRandom.triggered.connect(GerarNum4)
    Processos4.TipoEscala.activated.connect(GerarCrit4)
    Processos4.LimparCampos.triggered.connect(LimparCampos4)
    #################### 5 PROCESSOS ##########################################
    Processos5 = uic.loadUi("Processos5.ui")
    Processos5.GerarTabela.clicked.connect(GerarTabela5)
    Processos5.GerarRandom.triggered.connect(GerarNum5)
    Processos5.TipoEscala.activated.connect(GerarCrit5)
    Processos5.LimparCampos.triggered.connect(LimparCampos5)
    #################### 6 PROCESSOS ##########################################
    Processos6 = uic.loadUi("Processos6.ui")
    Processos6.GerarTabela.clicked.connect(GerarTabela6)
    Processos6.GerarRandom.triggered.connect(GerarNum6)
    Processos6.TipoEscala.activated.connect(GerarCrit6)
    Processos6.LimparCampos.triggered.connect(LimparCampos6)
    #################### 7 PROCESSOS ##########################################
    Processos7 = uic.loadUi("Processos7.ui")
    Processos7.GerarTabela.clicked.connect(GerarTabela7)
    Processos7.GerarRandom.triggered.connect(GerarNum7)
    Processos7.TipoEscala.activated.connect(GerarCrit7)
    Processos7.LimparCampos.triggered.connect(LimparCampos7)
    ################### Seleção Processos #####################################
    SelectProcess = uic.loadUi("ProcessosSelect.ui")
    SelectProcess.LoadProcess.clicked.connect(carregarprocessos)
    ####################    Main    ###########################################
    Main = uic.loadUi("Main.ui")
    Main.AbrirProcesso.clicked.connect(abrirselect)
    Main.ConectarSQL.clicked.connect(abrirsql)
    Main.CarregarPIPE.clicked.connect(CarregarPIPE)
    Main.cred.triggered.connect(devinfo)
    Main.infodev.triggered.connect(devinfo2)
    Main.show()
    Aplicativo.exec() #Executar programa
    # WILLIANQUIRINO\SQLEXPRESS