import random
##### PIP INSTALL PYQT5 ############# <- Interface Gráfica
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
###########################################################
import devs 
##### PIP INSTALL PYODBC ############ <- Conexão SQL Server
import pyodbc
###########################################################
import GerarDocumento
##### BIBLIOTECA PARA SALVAR DIRETÓRIO ##### <- salvar = tk() / salvar.withdraw() / DiretorioSelecionado = filedialog.askdirectory()
from tkinter import filedialog
from tkinter import *
import os


ConnectServer: bool = False
NomeServer: str
NomeBanco: str


####### GERA OS OBJETOS DA INTERFACE DE SELEÇÃO DE ESCALONAMENTO #################
###### TAMBÉM GERA OS MÉTODOS QUE SERÃO UTILIZADO POR CADA INTERFACE ##########

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
            devs.GerarTabela(devs.calcularFIFO(processos), True)
        elif TipoEscalonamento == 'SJF':
            if Processos2.TipoDesempate.currentText() == 'FIFO':
                devs.GerarTabela(devs.calcularSJF(processos, 1), True)
            elif Processos2.TipoDesempate.currentText() == 'Por Prioridade':
                devs.GerarTabela(devs.calcularSJF(processos, 2), True)
        elif TipoEscalonamento == 'Por Prioridade':
            if Processos2.TipoDesempate.currentText() == 'FIFO':
                devs.GerarTabela(devs.calcularPorPrioridade(processos, 2), True)
            elif Processos2.TipoDesempate.currentText() == 'SJF':
                devs.GerarTabela(devs.calcularPorPrioridade(processos, 1), True)
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

def GerarRel2():
    TipoEscalonamento = Processos2.TipoEscala.currentText()
    try:
        processos = [
            ('P1', int(Processos2.TempoExecucao_1.text()), int(Processos2.OrdemChegada_1.text()), int(Processos2.Prioridade_1.text())),
            ('P2', int(Processos2.TempoExecucao_2.text()), int(Processos2.OrdemChegada_2.text()), int(Processos2.Prioridade_2.text())),
        ]
        if TipoEscalonamento == 'FIFO':
            val = GerarDocumento.GerarRelatorio(processos, devs.calcularFIFO(processos), devs.GerarTabela(devs.calcularFIFO(processos), False), 'FIFO', 'Nenhum')
            if val:
                QMessageBox.about(Processos2, "Arquivo Salvo", "Seu arquivo foi salvo com sucesso!")
        ####################################### SJF - TEMPO DE EXECUÇÃO ##############################################
        elif TipoEscalonamento == 'SJF':
            if Processos2.TipoDesempate.currentText() == 'FIFO':
                val = GerarDocumento.GerarRelatorio(processos, devs.calcularSJF(processos, 1), devs.GerarTabela(devs.calcularSJF(processos, 1), False), 'SJF', 'FIFO')
                if val:
                    QMessageBox.about(Processos2, "Arquivo Salvo", "Seu arquivo foi salvo com sucesso!")
            elif Processos2.TipoDesempate.currentText() == 'Por Prioridade':
                val = GerarDocumento.GerarRelatorio(processos, devs.calcularSJF(processos, 2), devs.GerarTabela(devs.calcularSJF(processos, 2), False), 'SJF', 'POR PRIORIDADE')
                if val:
                    QMessageBox.about(Processos2, "Arquivo Salvo", "Seu arquivo foi salvo com sucesso!")
        ####################################### POR PRIORIDADE ##############################################
        elif TipoEscalonamento == 'Por Prioridade': 
            if Processos2.TipoDesempate.currentText() == 'FIFO':
                val = GerarDocumento.GerarRelatorio(processos, devs.calcularPorPrioridade(processos, 2), devs.GerarTabela(devs.calcularPorPrioridade(processos, 2), False), 'POR PRIORIDADE', 'FIFO')
                if val:
                    QMessageBox.about(Processos2, "Arquivo Salvo", "Seu arquivo foi salvo com sucesso!")
            elif Processos2.TipoDesempate.currentText() == 'SJF':
                val = GerarDocumento.GerarRelatorio(processos, devs.calcularPorPrioridade(processos, 1), devs.GerarTabela(devs.calcularPorPrioridade(processos, 1), False), 'POR PRIORIDADE', 'SJF')
                if val:
                    QMessageBox.about(Processos2, "Arquivo Salvo", "Seu arquivo foi salvo com sucesso!")
    except ValueError:
        QMessageBox.about(Processos2, "Error Detectado", "Não foi possível salvar este modelo.\n\nVerifique se não existe campos vazios.")

def GerarSQL2():
    TipoEscalonamento = Processos2.TipoEscala.currentText()
    if ConnectServer == True:
        try:
            processos = [
                ('P1', int(Processos2.TempoExecucao_1.text()), int(Processos2.OrdemChegada_1.text()), int(Processos2.Prioridade_1.text())),
                ('P2', int(Processos2.TempoExecucao_2.text()), int(Processos2.OrdemChegada_2.text()), int(Processos2.Prioridade_2.text())),
            ]
            if TipoEscalonamento == 'FIFO':
                val = GerarDocumento.GerarRelatorioSQL(processos, devs.calcularFIFO(processos), devs.GerarTabela(devs.calcularFIFO(processos), False), 'FIFO', 'Nenhum', Processos2)
        ####################################### SJF - TEMPO DE EXECUÇÃO ##############################################
            elif TipoEscalonamento == 'SJF':
                if Processos2.TipoDesempate.currentText() == 'FIFO':
                    val = GerarDocumento.GerarRelatorioSQL(processos, devs.calcularSJF(processos, 1), devs.GerarTabela(devs.calcularSJF(processos, 1), False), 'SJF', 'FIFO', Processos2)
                elif Processos2.TipoDesempate.currentText() == 'Por Prioridade':
                    val = GerarDocumento.GerarRelatorioSQL(processos, devs.calcularSJF(processos, 2), devs.GerarTabela(devs.calcularSJF(processos, 2), False), 'SJF', 'POR PRIORIDADE', Processos2)
        ####################################### POR PRIORIDADE ##############################################
            elif TipoEscalonamento == 'Por Prioridade': 
                if Processos2.TipoDesempate.currentText() == 'FIFO':
                    val = GerarDocumento.GerarRelatorioSQL(processos, devs.calcularPorPrioridade(processos, 2), devs.GerarTabela(devs.calcularPorPrioridade(processos, 2), False), 'POR PRIORIDADE', 'FIFO', Processos2)
                elif Processos2.TipoDesempate.currentText() == 'SJF':
                    val = GerarDocumento.GerarRelatorioSQL(processos, devs.calcularPorPrioridade(processos, 1), devs.GerarTabela(devs.calcularPorPrioridade(processos, 1), False), 'POR PRIORIDADE', 'SJF', Processos2)
        except ValueError:
            QMessageBox.about(Processos2, "Error Detectado", "Não foi possível salvar este modelo.\n\nVerifique se não existe campos vazios.")
    else:
        QMessageBox.about(Processos2, "Sem Conexão", "Você precisa estar conectado para salvar os dados no banco de dados!")

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
            devs.GerarTabela(devs.calcularFIFO(processos), True)
        elif TipoEscalonamento == 'SJF':
            if Processos3.TipoDesempate.currentText() == 'FIFO':
                devs.GerarTabela(devs.calcularSJF(processos, 1), True)
            elif Processos3.TipoDesempate.currentText() == 'Por Prioridade':
                devs.GerarTabela(devs.calcularSJF(processos, 2), True)
        elif TipoEscalonamento == 'Por Prioridade':
            if Processos3.TipoDesempate.currentText() == 'FIFO':
                devs.GerarTabela(devs.calcularPorPrioridade(processos, 2), True)
            elif Processos3.TipoDesempate.currentText() == 'SJF':
                devs.GerarTabela(devs.calcularPorPrioridade(processos, 1), True)
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

def GerarRel3():
    TipoEscalonamento = Processos3.TipoEscala.currentText()
    try:
        processos = [
            ('P1', int(Processos3.TempoExecucao_1.text()), int(Processos3.OrdemChegada_1.text()), int(Processos3.Prioridade_1.text())),
            ('P2', int(Processos3.TempoExecucao_2.text()), int(Processos3.OrdemChegada_2.text()), int(Processos3.Prioridade_2.text())),
            ('P3', int(Processos3.TempoExecucao_3.text()), int(Processos3.OrdemChegada_3.text()), int(Processos3.Prioridade_3.text())),
        ]
        if TipoEscalonamento == 'FIFO':
            val = GerarDocumento.GerarRelatorio(processos, devs.calcularFIFO(processos), devs.GerarTabela(devs.calcularFIFO(processos), False), 'FIFO', 'Nenhum')
            if val:
                QMessageBox.about(Processos3, "Arquivo Salvo", "Seu arquivo foi salvo com sucesso!")
        ####################################### SJF - TEMPO DE EXECUÇÃO ##############################################
        elif TipoEscalonamento == 'SJF':
            if Processos3.TipoDesempate.currentText() == 'FIFO':
                val = GerarDocumento.GerarRelatorio(processos, devs.calcularSJF(processos, 1), devs.GerarTabela(devs.calcularSJF(processos, 1), False), 'SJF', 'FIFO')
                if val:
                    QMessageBox.about(Processos3, "Arquivo Salvo", "Seu arquivo foi salvo com sucesso!")
            elif Processos3.TipoDesempate.currentText() == 'Por Prioridade':
                val = GerarDocumento.GerarRelatorio(processos, devs.calcularSJF(processos, 2), devs.GerarTabela(devs.calcularSJF(processos, 2), False), 'SJF', 'POR PRIORIDADE')
                if val:
                    QMessageBox.about(Processos3, "Arquivo Salvo", "Seu arquivo foi salvo com sucesso!")
        ####################################### POR PRIORIDADE ##############################################
        elif TipoEscalonamento == 'Por Prioridade': 
            if Processos3.TipoDesempate.currentText() == 'FIFO':
                val = GerarDocumento.GerarRelatorio(processos, devs.calcularPorPrioridade(processos, 2), devs.GerarTabela(devs.calcularPorPrioridade(processos, 2), False), 'POR PRIORIDADE', 'FIFO')
                if val:
                    QMessageBox.about(Processos3, "Arquivo Salvo", "Seu arquivo foi salvo com sucesso!")
            elif Processos3.TipoDesempate.currentText() == 'SJF':
                val = GerarDocumento.GerarRelatorio(processos, devs.calcularPorPrioridade(processos, 1), devs.GerarTabela(devs.calcularPorPrioridade(processos, 1), False), 'POR PRIORIDADE', 'SJF')
                if val:
                    QMessageBox.about(Processos3, "Arquivo Salvo", "Seu arquivo foi salvo com sucesso!")
    except ValueError:
        QMessageBox.about(Processos3, "Error Detectado", "Não foi possível salvar este modelo.\n\nVerifique se não existe campos vazios.")

def GerarSQL3():
    TipoEscalonamento = Processos3.TipoEscala.currentText()
    if ConnectServer == True:
        try:
            processos = [
                ('P1', int(Processos3.TempoExecucao_1.text()), int(Processos3.OrdemChegada_1.text()), int(Processos3.Prioridade_1.text())),
                ('P2', int(Processos3.TempoExecucao_2.text()), int(Processos3.OrdemChegada_2.text()), int(Processos3.Prioridade_2.text())),
                ('P3', int(Processos3.TempoExecucao_3.text()), int(Processos3.OrdemChegada_3.text()), int(Processos3.Prioridade_3.text())),
                ]
            if TipoEscalonamento == 'FIFO':
                val = GerarDocumento.GerarRelatorioSQL(processos, devs.calcularFIFO(processos), devs.GerarTabela(devs.calcularFIFO(processos), False), 'FIFO', 'Nenhum', Processos3)
        ####################################### SJF - TEMPO DE EXECUÇÃO ##############################################
            elif TipoEscalonamento == 'SJF':
                if Processos3.TipoDesempate.currentText() == 'FIFO':
                    val = GerarDocumento.GerarRelatorioSQL(processos, devs.calcularSJF(processos, 1), devs.GerarTabela(devs.calcularSJF(processos, 1), False), 'SJF', 'FIFO', Processos3)
                elif Processos3.TipoDesempate.currentText() == 'Por Prioridade':
                    val = GerarDocumento.GerarRelatorioSQL(processos, devs.calcularSJF(processos, 2), devs.GerarTabela(devs.calcularSJF(processos, 2), False), 'SJF', 'POR PRIORIDADE', Processos3)
        ####################################### POR PRIORIDADE ##############################################
            elif TipoEscalonamento == 'Por Prioridade': 
                if Processos3.TipoDesempate.currentText() == 'FIFO':
                    val = GerarDocumento.GerarRelatorioSQL(processos, devs.calcularPorPrioridade(processos, 2), devs.GerarTabela(devs.calcularPorPrioridade(processos, 2), False), 'POR PRIORIDADE', 'FIFO', Processos3)
                elif Processos3.TipoDesempate.currentText() == 'SJF':
                    val = GerarDocumento.GerarRelatorioSQL(processos, devs.calcularPorPrioridade(processos, 1), devs.GerarTabela(devs.calcularPorPrioridade(processos, 1), False), 'POR PRIORIDADE', 'SJF', Processos3)
        except ValueError:
            QMessageBox.about(Processos3, "Error Detectado", "Não foi possível salvar este modelo.\n\nVerifique se não existe campos vazios.")
    else:
        QMessageBox.about(Processos3, "Sem Conexão", "Você precisa estar conectado para salvar os dados no banco de dados!")

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
            devs.GerarTabela(devs.calcularFIFO(processos), True)
        elif TipoEscalonamento == 'SJF':
            if Processos4.TipoDesempate.currentText() == 'FIFO':
                devs.GerarTabela(devs.calcularSJF(processos, 1), True)
            elif Processos4.TipoDesempate.currentText() == 'Por Prioridade':
                devs.GerarTabela(devs.calcularSJF(processos, 2), True)
        elif TipoEscalonamento == 'Por Prioridade':
            if Processos4.TipoDesempate.currentText() == 'FIFO':
                devs.GerarTabela(devs.calcularPorPrioridade(processos, 2), True)
            elif Processos4.TipoDesempate.currentText() == 'SJF':
                devs.GerarTabela(devs.calcularPorPrioridade(processos, 1), True)
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

def GerarRel4():
    TipoEscalonamento = Processos4.TipoEscala.currentText()
    try:
        processos = [
            ('P1', int(Processos4.TempoExecucao_1.text()), int(Processos4.OrdemChegada_1.text()), int(Processos4.Prioridade_1.text())),
            ('P2', int(Processos4.TempoExecucao_2.text()), int(Processos4.OrdemChegada_2.text()), int(Processos4.Prioridade_2.text())),
            ('P3', int(Processos4.TempoExecucao_3.text()), int(Processos4.OrdemChegada_3.text()), int(Processos4.Prioridade_3.text())),
            ('P4', int(Processos4.TempoExecucao_4.text()), int(Processos4.OrdemChegada_4.text()), int(Processos4.Prioridade_4.text()))
            ]
        if TipoEscalonamento == 'FIFO':
            val = GerarDocumento.GerarRelatorio(processos, devs.calcularFIFO(processos), devs.GerarTabela(devs.calcularFIFO(processos), False), 'FIFO', 'Nenhum')
            if val:
                QMessageBox.about(Processos4, "Arquivo Salvo", "Seu arquivo foi salvo com sucesso!")
        ####################################### SJF - TEMPO DE EXECUÇÃO ##############################################
        elif TipoEscalonamento == 'SJF':
            if Processos4.TipoDesempate.currentText() == 'FIFO':
                val = GerarDocumento.GerarRelatorio(processos, devs.calcularSJF(processos, 1), devs.GerarTabela(devs.calcularSJF(processos, 1), False), 'SJF', 'FIFO')
                if val:
                    QMessageBox.about(Processos4, "Arquivo Salvo", "Seu arquivo foi salvo com sucesso!")
            elif Processos4.TipoDesempate.currentText() == 'Por Prioridade':
                val = GerarDocumento.GerarRelatorio(processos, devs.calcularSJF(processos, 2), devs.GerarTabela(devs.calcularSJF(processos, 2), False), 'SJF', 'POR PRIORIDADE')
                if val:
                    QMessageBox.about(Processos4, "Arquivo Salvo", "Seu arquivo foi salvo com sucesso!")
        ####################################### POR PRIORIDADE ##############################################
        elif TipoEscalonamento == 'Por Prioridade': 
            if Processos4.TipoDesempate.currentText() == 'FIFO':
                val = GerarDocumento.GerarRelatorio(processos, devs.calcularPorPrioridade(processos, 2), devs.GerarTabela(devs.calcularPorPrioridade(processos, 2), False), 'POR PRIORIDADE', 'FIFO')
                if val:
                    QMessageBox.about(Processos4, "Arquivo Salvo", "Seu arquivo foi salvo com sucesso!")
            elif Processos4.TipoDesempate.currentText() == 'SJF':
                val = GerarDocumento.GerarRelatorio(processos, devs.calcularPorPrioridade(processos, 1), devs.GerarTabela(devs.calcularPorPrioridade(processos, 1), False), 'POR PRIORIDADE', 'SJF')
                if val:
                    QMessageBox.about(Processos4, "Arquivo Salvo", "Seu arquivo foi salvo com sucesso!")
    except ValueError:
        QMessageBox.about(Processos4, "Error Detectado", "Não foi possível salvar este modelo.\n\nVerifique se não existe campos vazios.")

def GerarSQL4():
    TipoEscalonamento = Processos4.TipoEscala.currentText()
    if ConnectServer == True:
        try:
            processos = [
                ('P1', int(Processos4.TempoExecucao_1.text()), int(Processos4.OrdemChegada_1.text()), int(Processos4.Prioridade_1.text())),
                ('P2', int(Processos4.TempoExecucao_2.text()), int(Processos4.OrdemChegada_2.text()), int(Processos4.Prioridade_2.text())),
                ('P3', int(Processos4.TempoExecucao_3.text()), int(Processos4.OrdemChegada_3.text()), int(Processos4.Prioridade_3.text())),
                ('P4', int(Processos4.TempoExecucao_4.text()), int(Processos4.OrdemChegada_4.text()), int(Processos4.Prioridade_4.text()))
                ]
            if TipoEscalonamento == 'FIFO':
                val = GerarDocumento.GerarRelatorioSQL(processos, devs.calcularFIFO(processos), devs.GerarTabela(devs.calcularFIFO(processos), False), 'FIFO', 'Nenhum', Processos4)
        ####################################### SJF - TEMPO DE EXECUÇÃO ##############################################
            elif TipoEscalonamento == 'SJF':
                if Processos4.TipoDesempate.currentText() == 'FIFO':
                    val = GerarDocumento.GerarRelatorioSQL(processos, devs.calcularSJF(processos, 1), devs.GerarTabela(devs.calcularSJF(processos, 1), False), 'SJF', 'FIFO', Processos4)
            elif Processos4.TipoDesempate.currentText() == 'Por Prioridade':
                val = GerarDocumento.GerarRelatorioSQL(processos, devs.calcularSJF(processos, 2), devs.GerarTabela(devs.calcularSJF(processos, 2), False), 'SJF', 'POR PRIORIDADE', Processos4)
        ####################################### POR PRIORIDADE ##############################################
            elif TipoEscalonamento == 'Por Prioridade': 
                if Processos4.TipoDesempate.currentText() == 'FIFO':
                    val = GerarDocumento.GerarRelatorioSQL(processos, devs.calcularPorPrioridade(processos, 2), devs.GerarTabela(devs.calcularPorPrioridade(processos, 2), False), 'POR PRIORIDADE', 'FIFO', Processos4)
            elif Processos4.TipoDesempate.currentText() == 'SJF':
                val = GerarDocumento.GerarRelatorioSQL(processos, devs.calcularPorPrioridade(processos, 1), devs.GerarTabela(devs.calcularPorPrioridade(processos, 1), False), 'POR PRIORIDADE', 'SJF', Processos4)
        except ValueError:
            QMessageBox.about(Processos4, "Error Detectado", "Não foi possível salvar este modelo.\n\nVerifique se não existe campos vazios.")
    else:
        QMessageBox.about(Processos4, "Sem Conexão", "Você precisa estar conectado para salvar os dados no banco de dados!")

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
            devs.GerarTabela(devs.calcularFIFO(processos), True)
        elif TipoEscalonamento == 'SJF':
            if Processos5.TipoDesempate.currentText() == 'FIFO':
                devs.GerarTabela(devs.calcularSJF(processos, 1), True)
            elif Processos5.TipoDesempate.currentText() == 'Por Prioridade':
                devs.GerarTabela(devs.calcularSJF(processos, 2), True)
        elif TipoEscalonamento == 'Por Prioridade':
            if Processos5.TipoDesempate.currentText() == 'FIFO':
                devs.GerarTabela(devs.calcularPorPrioridade(processos, 2), True)
            elif Processos5.TipoDesempate.currentText() == 'SJF':
                devs.GerarTabela(devs.calcularPorPrioridade(processos, 1), True)
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

def GerarRel5():
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
            val = GerarDocumento.GerarRelatorio(processos, devs.calcularFIFO(processos), devs.GerarTabela(devs.calcularFIFO(processos), False), 'FIFO', 'Nenhum')
            if val:
                QMessageBox.about(Processos5, "Arquivo Salvo", "Seu arquivo foi salvo com sucesso!")
        ####################################### SJF - TEMPO DE EXECUÇÃO ##############################################
        elif TipoEscalonamento == 'SJF':
            if Processos5.TipoDesempate.currentText() == 'FIFO':
                val = GerarDocumento.GerarRelatorio(processos, devs.calcularSJF(processos, 1), devs.GerarTabela(devs.calcularSJF(processos, 1), False), 'SJF', 'FIFO')
                if val:
                    QMessageBox.about(Processos5, "Arquivo Salvo", "Seu arquivo foi salvo com sucesso!")
            elif Processos5.TipoDesempate.currentText() == 'Por Prioridade':
                val = GerarDocumento.GerarRelatorio(processos, devs.calcularSJF(processos, 2), devs.GerarTabela(devs.calcularSJF(processos, 2), False), 'SJF', 'POR PRIORIDADE')
                if val:
                    QMessageBox.about(Processos5, "Arquivo Salvo", "Seu arquivo foi salvo com sucesso!")
        ####################################### POR PRIORIDADE ##############################################
        elif TipoEscalonamento == 'Por Prioridade': 
            if Processos5.TipoDesempate.currentText() == 'FIFO':
                val = GerarDocumento.GerarRelatorio(processos, devs.calcularPorPrioridade(processos, 2), devs.GerarTabela(devs.calcularPorPrioridade(processos, 2), False), 'POR PRIORIDADE', 'FIFO')
                if val:
                    QMessageBox.about(Processos5, "Arquivo Salvo", "Seu arquivo foi salvo com sucesso!")
            elif Processos5.TipoDesempate.currentText() == 'SJF':
                val = GerarDocumento.GerarRelatorio(processos, devs.calcularPorPrioridade(processos, 1), devs.GerarTabela(devs.calcularPorPrioridade(processos, 1), False), 'POR PRIORIDADE', 'SJF')
                if val:
                    QMessageBox.about(Processos5, "Arquivo Salvo", "Seu arquivo foi salvo com sucesso!")
    except ValueError:
        QMessageBox.about(Processos5, "Error Detectado", "Não foi possível salvar este modelo.\n\nVerifique se não existe campos vazios.")

def GerarSQL5():
    TipoEscalonamento = Processos5.TipoEscala.currentText()
    if ConnectServer == True:
        try:
            processos = [
                ('P1', int(Processos5.TempoExecucao_1.text()), int(Processos5.OrdemChegada_1.text()), int(Processos5.Prioridade_1.text())),
                ('P2', int(Processos5.TempoExecucao_2.text()), int(Processos5.OrdemChegada_2.text()), int(Processos5.Prioridade_2.text())),
                ('P3', int(Processos5.TempoExecucao_3.text()), int(Processos5.OrdemChegada_3.text()), int(Processos5.Prioridade_3.text())),
                ('P4', int(Processos5.TempoExecucao_4.text()), int(Processos5.OrdemChegada_4.text()), int(Processos5.Prioridade_4.text())),
                ('P5', int(Processos5.TempoExecucao_5.text()), int(Processos5.OrdemChegada_5.text()), int(Processos5.Prioridade_5.text()))        
                ]
            if TipoEscalonamento == 'FIFO':
                val = GerarDocumento.GerarRelatorioSQL(processos, devs.calcularFIFO(processos), devs.GerarTabela(devs.calcularFIFO(processos), False), 'FIFO', 'Nenhum', Processos5)
        ####################################### SJF - TEMPO DE EXECUÇÃO ##############################################
            elif TipoEscalonamento == 'SJF':
                if Processos5.TipoDesempate.currentText() == 'FIFO':
                    val = GerarDocumento.GerarRelatorioSQL(processos, devs.calcularSJF(processos, 1), devs.GerarTabela(devs.calcularSJF(processos, 1), False), 'SJF', 'FIFO', Processos5)
                elif Processos5.TipoDesempate.currentText() == 'Por Prioridade':
                    val = GerarDocumento.GerarRelatorioSQL(processos, devs.calcularSJF(processos, 2), devs.GerarTabela(devs.calcularSJF(processos, 2), False), 'SJF', 'POR PRIORIDADE', Processos5)
        ####################################### POR PRIORIDADE ##############################################
            elif TipoEscalonamento == 'Por Prioridade': 
                if Processos5.TipoDesempate.currentText() == 'FIFO':
                    val = GerarDocumento.GerarRelatorioSQL(processos, devs.calcularPorPrioridade(processos, 2), devs.GerarTabela(devs.calcularPorPrioridade(processos, 2), False), 'POR PRIORIDADE', 'FIFO', Processos5)
                elif Processos5.TipoDesempate.currentText() == 'SJF':
                    val = GerarDocumento.GerarRelatorioSQL(processos, devs.calcularPorPrioridade(processos, 1), devs.GerarTabela(devs.calcularPorPrioridade(processos, 1), False), 'POR PRIORIDADE', 'SJF', Processos5)
        except ValueError:
            QMessageBox.about(Processos5, "Error Detectado", "Não foi possível salvar este modelo.\n\nVerifique se não existe campos vazios.")
    else:
        QMessageBox.about(Processos5, "Sem Conexão", "Você precisa estar conectado para salvar os dados no banco de dados!")

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
            devs.GerarTabela(devs.calcularFIFO(processos), True)
        elif TipoEscalonamento == 'SJF':
            if Processos6.TipoDesempate.currentText() == 'FIFO':
                devs.GerarTabela(devs.calcularSJF(processos, 1), True)
            elif Processos6.TipoDesempate.currentText() == 'Por Prioridade':
                devs.GerarTabela(devs.calcularSJF(processos, 2), True)
        elif TipoEscalonamento == 'Por Prioridade':
            if Processos6.TipoDesempate.currentText() == 'FIFO':
                devs.GerarTabela(devs.calcularPorPrioridade(processos, 2), True)
            elif Processos6.TipoDesempate.currentText() == 'SJF':
                devs.GerarTabela(devs.calcularPorPrioridade(processos, 1), True)
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

def GerarRel6():
    TipoEscalonamento = Processos6.TipoEscala.currentText()
    try:
        processos = [
            ('P1', int(Processos6.TempoExecucao_1.text()), int(Processos6.OrdemChegada_1.text()), int(Processos6.Prioridade_1.text())),
            ('P2', int(Processos6.TempoExecucao_2.text()), int(Processos6.OrdemChegada_2.text()), int(Processos6.Prioridade_2.text())),
            ('P3', int(Processos6.TempoExecucao_3.text()), int(Processos6.OrdemChegada_3.text()), int(Processos6.Prioridade_3.text())),
            ('P4', int(Processos6.TempoExecucao_4.text()), int(Processos6.OrdemChegada_4.text()), int(Processos6.Prioridade_4.text())),
            ('P5', int(Processos6.TempoExecucao_5.text()), int(Processos6.OrdemChegada_5.text()), int(Processos6.Prioridade_5.text())),
            ('P6', int(Processos6.TempoExecucao_6.text()), int(Processos6.OrdemChegada_6.text()), int(Processos6.Prioridade_6.text())),
            ]
        if TipoEscalonamento == 'FIFO':
            val = GerarDocumento.GerarRelatorio(processos, devs.calcularFIFO(processos), devs.GerarTabela(devs.calcularFIFO(processos), False), 'FIFO', 'Nenhum')
            if val:
                QMessageBox.about(Processos6, "Arquivo Salvo", "Seu arquivo foi salvo com sucesso!")
        ####################################### SJF - TEMPO DE EXECUÇÃO ##############################################
        elif TipoEscalonamento == 'SJF':
            if Processos6.TipoDesempate.currentText() == 'FIFO':
                val = GerarDocumento.GerarRelatorio(processos, devs.calcularSJF(processos, 1), devs.GerarTabela(devs.calcularSJF(processos, 1), False), 'SJF', 'FIFO')
                if val:
                    QMessageBox.about(Processos6, "Arquivo Salvo", "Seu arquivo foi salvo com sucesso!")
            elif Processos6.TipoDesempate.currentText() == 'Por Prioridade':
                val = GerarDocumento.GerarRelatorio(processos, devs.calcularSJF(processos, 2), devs.GerarTabela(devs.calcularSJF(processos, 2), False), 'SJF', 'POR PRIORIDADE')
                if val:
                    QMessageBox.about(Processos6, "Arquivo Salvo", "Seu arquivo foi salvo com sucesso!")
        ####################################### POR PRIORIDADE ##############################################
        elif TipoEscalonamento == 'Por Prioridade': 
            if Processos6.TipoDesempate.currentText() == 'FIFO':
                val = GerarDocumento.GerarRelatorio(processos, devs.calcularPorPrioridade(processos, 2), devs.GerarTabela(devs.calcularPorPrioridade(processos, 2), False), 'POR PRIORIDADE', 'FIFO')
                if val:
                    QMessageBox.about(Processos6, "Arquivo Salvo", "Seu arquivo foi salvo com sucesso!")
            elif Processos6.TipoDesempate.currentText() == 'SJF':
                val = GerarDocumento.GerarRelatorio(processos, devs.calcularPorPrioridade(processos, 1), devs.GerarTabela(devs.calcularPorPrioridade(processos, 1), False), 'POR PRIORIDADE', 'SJF')
                if val:
                    QMessageBox.about(Processos6, "Arquivo Salvo", "Seu arquivo foi salvo com sucesso!")
    except ValueError:
        QMessageBox.about(Processos6, "Error Detectado", "Não foi possível salvar este modelo.\n\nVerifique se não existe campos vazios.")

def GerarSQL6():
    TipoEscalonamento = Processos6.TipoEscala.currentText()
    if ConnectServer == True:
        try:
            processos = [
                ('P1', int(Processos6.TempoExecucao_1.text()), int(Processos6.OrdemChegada_1.text()), int(Processos6.Prioridade_1.text())),
                ('P2', int(Processos6.TempoExecucao_2.text()), int(Processos6.OrdemChegada_2.text()), int(Processos6.Prioridade_2.text())),
                ('P3', int(Processos6.TempoExecucao_3.text()), int(Processos6.OrdemChegada_3.text()), int(Processos6.Prioridade_3.text())),
                ('P4', int(Processos6.TempoExecucao_4.text()), int(Processos6.OrdemChegada_4.text()), int(Processos6.Prioridade_4.text())),
                ('P5', int(Processos6.TempoExecucao_5.text()), int(Processos6.OrdemChegada_5.text()), int(Processos6.Prioridade_5.text())),
                ('P6', int(Processos6.TempoExecucao_6.text()), int(Processos6.OrdemChegada_6.text()), int(Processos6.Prioridade_6.text())),
                ]
            if TipoEscalonamento == 'FIFO':
                val = GerarDocumento.GerarRelatorioSQL(processos, devs.calcularFIFO(processos), devs.GerarTabela(devs.calcularFIFO(processos), False), 'FIFO', 'Nenhum', Processos6)
        ####################################### SJF - TEMPO DE EXECUÇÃO ##############################################
            elif TipoEscalonamento == 'SJF':
                if Processos6.TipoDesempate.currentText() == 'FIFO':
                    val = GerarDocumento.GerarRelatorioSQL(processos, devs.calcularSJF(processos, 1), devs.GerarTabela(devs.calcularSJF(processos, 1), False), 'SJF', 'FIFO', Processos6)
                elif Processos6.TipoDesempate.currentText() == 'Por Prioridade':
                    val = GerarDocumento.GerarRelatorioSQL(processos, devs.calcularSJF(processos, 2), devs.GerarTabela(devs.calcularSJF(processos, 2), False), 'SJF', 'POR PRIORIDADE', Processos6)
        ####################################### POR PRIORIDADE ##############################################
            elif TipoEscalonamento == 'Por Prioridade': 
                if Processos6.TipoDesempate.currentText() == 'FIFO':
                    val = GerarDocumento.GerarRelatorioSQL(processos, devs.calcularPorPrioridade(processos, 2), devs.GerarTabela(devs.calcularPorPrioridade(processos, 2), False), 'POR PRIORIDADE', 'FIFO', Processos6)
                elif Processos6.TipoDesempate.currentText() == 'SJF':
                    val = GerarDocumento.GerarRelatorioSQL(processos, devs.calcularPorPrioridade(processos, 1), devs.GerarTabela(devs.calcularPorPrioridade(processos, 1), False), 'POR PRIORIDADE', 'SJF', Processos6)
        except ValueError:
            QMessageBox.about(Processos6, "Error Detectado", "Não foi possível salvar este modelo.\n\nVerifique se não existe campos vazios.")
    else:
        QMessageBox.about(Processos6, "Sem Conexão", "Você precisa estar conectado para salvar os dados no banco de dados!")

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
            devs.GerarTabela(devs.calcularFIFO(processos), True)
        elif TipoEscalonamento == 'SJF':
            if Processos7.TipoDesempate.currentText() == 'FIFO':
                devs.GerarTabela(devs.calcularSJF(processos, 1), True)
            elif Processos7.TipoDesempate.currentText() == 'Por Prioridade':
                devs.GerarTabela(devs.calcularSJF(processos, 2), True)
        elif TipoEscalonamento == 'Por Prioridade':
            if Processos7.TipoDesempate.currentText() == 'FIFO':
                devs.GerarTabela(devs.calcularPorPrioridade(processos, 2), True)
            elif Processos7.TipoDesempate.currentText() == 'SJF':
                devs.GerarTabela(devs.calcularPorPrioridade(processos, 1), True)
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
    Processos7.OrdemChegada_7.setText('7')
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

def GerarRel7():
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
            val = GerarDocumento.GerarRelatorio(processos, devs.calcularFIFO(processos), devs.GerarTabela(devs.calcularFIFO(processos), False), 'FIFO', 'Nenhum')
            if val:
                QMessageBox.about(Processos7, "Arquivo Salvo", "Seu arquivo foi salvo com sucesso!")
        ####################################### SJF - TEMPO DE EXECUÇÃO ##############################################
        elif TipoEscalonamento == 'SJF':
            if Processos7.TipoDesempate.currentText() == 'FIFO':
                val = GerarDocumento.GerarRelatorio(processos, devs.calcularSJF(processos, 1), devs.GerarTabela(devs.calcularSJF(processos, 1), False), 'SJF', 'FIFO')
                if val:
                    QMessageBox.about(Processos7, "Arquivo Salvo", "Seu arquivo foi salvo com sucesso!")
            elif Processos7.TipoDesempate.currentText() == 'Por Prioridade':
                val = GerarDocumento.GerarRelatorio(processos, devs.calcularSJF(processos, 2), devs.GerarTabela(devs.calcularSJF(processos, 2), False), 'SJF', 'POR PRIORIDADE')
                if val:
                    QMessageBox.about(Processos7, "Arquivo Salvo", "Seu arquivo foi salvo com sucesso!")
        ####################################### POR PRIORIDADE ##############################################
        elif TipoEscalonamento == 'Por Prioridade': 
            if Processos7.TipoDesempate.currentText() == 'FIFO':
                val = GerarDocumento.GerarRelatorio(processos, devs.calcularPorPrioridade(processos, 2), devs.GerarTabela(devs.calcularPorPrioridade(processos, 2), False), 'POR PRIORIDADE', 'FIFO')
                if val:
                    QMessageBox.about(Processos7, "Arquivo Salvo", "Seu arquivo foi salvo com sucesso!")
            elif Processos7.TipoDesempate.currentText() == 'SJF':
                val = GerarDocumento.GerarRelatorio(processos, devs.calcularPorPrioridade(processos, 1), devs.GerarTabela(devs.calcularPorPrioridade(processos, 1), False), 'POR PRIORIDADE', 'SJF')
                if val:
                    QMessageBox.about(Processos7, "Arquivo Salvo", "Seu arquivo foi salvo com sucesso!")
    except ValueError:
        QMessageBox.about(Processos7, "Error Detectado", "Não foi possível salvar este modelo.\n\nVerifique se não existe campos vazios.")

def GerarSQL7():
    TipoEscalonamento = Processos7.TipoEscala.currentText()
    if ConnectServer == True:
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
                val = GerarDocumento.GerarRelatorioSQL(processos, devs.calcularFIFO(processos), devs.GerarTabela(devs.calcularFIFO(processos), False), 'FIFO', 'Nenhum', Processos7)
        ####################################### SJF - TEMPO DE EXECUÇÃO ##############################################
            elif TipoEscalonamento == 'SJF':
                if Processos7.TipoDesempate.currentText() == 'FIFO':
                    val = GerarDocumento.GerarRelatorioSQL(processos, devs.calcularSJF(processos, 1), devs.GerarTabela(devs.calcularSJF(processos, 1), False), 'SJF', 'FIFO', Processos7)
                elif Processos7.TipoDesempate.currentText() == 'Por Prioridade':
                    val = GerarDocumento.GerarRelatorioSQL(processos, devs.calcularSJF(processos, 2), devs.GerarTabela(devs.calcularSJF(processos, 2), False), 'SJF', 'POR PRIORIDADE', Processos7)
        ####################################### POR PRIORIDADE ##############################################
            elif TipoEscalonamento == 'Por Prioridade': 
                if Processos7.TipoDesempate.currentText() == 'FIFO':
                    val = GerarDocumento.GerarRelatorioSQL(processos, devs.calcularPorPrioridade(processos, 2), devs.GerarTabela(devs.calcularPorPrioridade(processos, 2), False), 'POR PRIORIDADE', 'FIFO', Processos7)
                elif Processos7.TipoDesempate.currentText() == 'SJF':
                    val = GerarDocumento.GerarRelatorioSQL(processos, devs.calcularPorPrioridade(processos, 1), devs.GerarTabela(devs.calcularPorPrioridade(processos, 1), False), 'POR PRIORIDADE', 'SJF', Processos7)
        except ValueError:
            QMessageBox.about(Processos7, "Error Detectado", "Não foi possível salvar este modelo.\n\nVerifique se não existe campos vazios.")
    else:
        QMessageBox.about(Processos7, "Sem Conexão", "Você precisa estar conectado para salvar os dados no banco de dados!")
################################### CARREGAR PROCESSOS #########################################
### CARREGA A QUANTIDADE DE PROCESSOS DISPONIVEL E LIMPA OS CAMPOS DIGITADOS ANTERIORMENTE ####
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

def conexaobanco(nomeserver: str, nomebanco: str): # CONEXÃO COM O BANCO -> (cursor de conexão)
    #conexao = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';UID='+username+';PWD='+ password
    conexao = "Driver={SQL Server Native Client 11.0};Server="+nomeserver+";Database="+nomebanco+";Trusted_Connection=yes;"
    return pyodbc.connect(conexao)

def buttonverif(): # VERIFICA SE FOI DIGITADO ALGO NO CAMPO LOGIN
    if len(SQLlogin.SQLname.text()) > 8 and SQLlogin.SelectAut.currentText() == 'SQL Windows':
        SQLlogin.Connect.setEnabled(True)
    else:
        if len(SQLlogin.SQLLogin_Name.text()) > 6 and len(SQLlogin.SQLLogin_Senha.text()) > 6:
            SQLlogin.Connect.setEnabled(True)
        else:
            SQLlogin.Connect.setEnabled(False)

def sqlserver(): # HABILITA OS OBJETOS DE LOGIN e PASSWORD CASO O CAMPO DE SQL SERVER SEJA FALSO
    if SQLlogin.SelectAut.currentText() == 'SQL Server':
        SQLlogin.label_name.setEnabled(True)
        SQLlogin.label_senha.setEnabled(True)
        SQLlogin.SQLLogin_Name.setEnabled(True)
        SQLlogin.SQLLogin_Senha.setEnabled(True)
        SQLlogin.ShowSenha.setEnabled(True)
    else:
        SQLlogin.label_name.setEnabled(False)
        SQLlogin.label_senha.setEnabled(False)
        SQLlogin.SQLLogin_Name.setEnabled(False)
        SQLlogin.SQLLogin_Senha.setEnabled(False)
        SQLlogin.ShowSenha.setEnabled(False)
        SQLlogin.SQLLogin_Name.setText("")
        SQLlogin.SQLLogin_Senha.setText("")

def mostrarsenha():
    if SQLlogin.SQLLogin_Senha.echoMode() == 2:
        SQLlogin.SQLLogin_Senha.setEchoMode(QtWidgets.QLineEdit.Normal)
    else:
        SQLlogin.SQLLogin_Senha.setEchoMode(QtWidgets.QLineEdit.Password)

def ConnectarServidor(): # FUNÇÃO QUE PASSA AS INFORMAÇÕES AS VARIÁVEIS GLOBAIS!
    if SQLlogin.SelectAut.currentText() == 'SQL Windows':
            msq = QMessageBox()
            msq.setWindowTitle("Aviso de Conexão") #Define o titulo
            msq.setText('Você conectará com o banco: \n'+str(SQLlogin.SQLname.text())) #Define descrição
            msq.setInformativeText("\nDeseja mesmo conectar?") #Define descrição secundária
            msq.setIcon(QMessageBox.Warning) #Abre mensagem de atenção
            msq.setStandardButtons(QMessageBox.Yes|QMessageBox.Cancel) #Criar opções de click na mensagem
            resposta = msq.exec_()
            if resposta == QMessageBox.Yes:
                try:
                    global NomeServer
                    global NomeBanco
                    global ConnectServer
                    ### EXECUTA O CURSOR PARA TESTAR SE A CONEXÃO É REALIZADA
                    ### CASO NÃO, RETORNA ERRO DE CONEXÃO E AS VARIÁVEIS NÃO SÃO PASSADAS
                    con = conexaobanco(SQLlogin.SQLname.text(), 'PIPESQL')
                    cursor = con.cursor()
                    cursor.close()
                    con.close()
                    NomeServer = SQLlogin.SQLname.text()
                    NomeBanco = 'PIPESQL'
                    ConnectServer = True
                    QMessageBox.about(SQLlogin, "Conexão Realidade", "Conexão sucedida!\nVocê agora está conectado ao banco.\n\n"+NomeServer)
                    SQLlogin.close()
                except pyodbc.InterfaceError:
                    QMessageBox.about(SQLlogin, "Erro de Conexão", "O banco não existe ou o servidor está incorreto!")
                except Exception:
                    QMessageBox.about(SQLlogin, "Erro de Conexão", "O banco demorou a responder. Verifique se não existe dados errados")
    else:
        QMessageBox.about(SQLlogin, "Manutenção!", "Em breve será possível fazer o login em um servidor!")
        '''                  CRIAR FUNÇÃO           '''
    
def devinfo():
    QMessageBox.about(Main, "Creditos", "Programa desenvolvido em 20/07/2021\nDeveloper: Willian Quirino / Dev Back-End\n\nPrograma desenvolvido para fins acadêmicos que visa o calculo de tabelas escalonadas para projetos de sistemas operacionais.\nO programa tem como apriomoramento de criação de tabelas FIFO/SJT/Por Prioridade utilizando processos de escalas junto a tabela de Gantt.\n\n\nO projeto pode ser acessado junto ao seu código fonte em:\ngithub.com/willianqf/Program-PIPELINE-")
def devinfo2():
    QMessageBox.about(Main, "Informações do Programa", "Este programa tem fins de calculo de escalonamento para processos operacionais.\n\nCalculos disponíiveis: FIFO/SJF/Por Prioridade\n\nComo usar o programa?\nDeve-se utilizar a quantidade de processos que queira calcular no botão 'Calcular Processos'\n\nComo gero um relatório?\nO programa oferece um local que pode ser alterado no momento do save de relatório. O relatório é gerado em PDF contendo a tabela de processo junto ao gráfico de Gantt\n\nO programa é de código aberto?\nO programa pode ser acessado com seu código fonte através do canal do GIT disponível nos créditos\n\nComo conecto com o banco de dados local?\nVocê precisa ter o SQL Server instalado na sua máquina para poder usar a conexão com o banco. Basta pegar o indereço NOME\SQLEXPRESS")

####################################  MAIN  #########################################################
def abrirselect():
    SelectProcess.show()

def abrirsql():
    global ConnectServer
    global NomeServer
    if ConnectServer == False:
        SQLlogin.show()
    else:
        QMessageBox.about(Main, "Conexão já realizada", "Você já está conectado com o banco:\n\n"+NomeServer)
def DesconectarSQL():
    global ConnectServer
    global NomeServer
    global NomeBanco
    if ConnectServer == True:
        msq = QMessageBox()
        msq.setWindowTitle("Aviso de Conexão") #Define o titulo
        msq.setText('Você está prestes a desconectar com o banco: \n'+NomeServer) #Define descrição
        msq.setInformativeText("\nDeseja mesmo desconectar?") #Define descrição secundária
        msq.setIcon(QMessageBox.Warning) #Abre mensagem de atenção
        msq.setStandardButtons(QMessageBox.Yes|QMessageBox.Cancel) #Criar opções de click na mensagem
        resposta = msq.exec_()
        if resposta == QMessageBox.Yes:
            banco = NomeServer
            ConnectServer = False
            NomeServer = ""
            NomeBanco = ""
            QMessageBox.about(Main, "Banco Desconectado", "Você foi desconectado ao banco:\n\n"+banco)
            SQLAccess.close()
    else:
        QMessageBox.about(Main, "Sem Conexão", "Você ainda não está conectado a nenhum banco")

def CarregarPIPE():
    global ConnectServer
    global NomeServer
    global NomeBanco
    if ConnectServer == True:
        SQLAccess.show()
        #print(os.getcwd()) #Pega o diretório atual do programa
        '''
            TESTAR BANCO DE DADOS
        '''
        '''
        conexao = conexaobanco(NomeServer, NomeBanco)
        cursor = conexao.cursor()
        cursor.execute("SELECT PDF_Pipe FROM BancoPipe WHERE COD_Pipe = '3iDeD2dj8CyzkN6FX5C3Z31'")
        val = cursor.fetchone()
        if val:
            for x in val:
                doguinho = open('WillianTest.pdf', 'wb')
                doguinho.write(x)
                doguinho.close()
                print("Linha1: "+str(x))
        '''
    else:
        QMessageBox.about(Main, "Conexão não realizada", "Você precisa estar com o banco conectado para realizar consultas!")
############################### SQL ACCESS ############################################################
def deletar(valor):
    global NomeBanco
    global NomeServer
    msq = QMessageBox()
    msq.setWindowTitle("Deletar Arquivo") #Define o titulo
    msq.setText('Você está prestes a deletar o arquivo do sistema!\nCódigo do Arquivo: {0}\n'.format(valor)) #Define descrição
    msq.setInformativeText("\nDeseja mesmo Deletar?") #Define descrição secundária
    msq.setIcon(QMessageBox.Warning) #Abre mensagem de atenção
    msq.setStandardButtons(QMessageBox.Yes|QMessageBox.Cancel) #Criar opções de click na mensagem
    resposta = msq.exec_()
    if resposta == QMessageBox.Yes:
        ### DELETA DADOS DO BANCO ### <- USA-SE PADRÃO COD_Pipe
        conexao = conexaobanco(NomeServer, NomeBanco)
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM BancoPipe WHERE COD_Pipe = '{0}'".format(valor))
        cursor.commit()
        QMessageBox.about(SQLview, "Deletado com Sucesso", "O arquivo do banco foi apagado do banco com sucesso!")
        ListarDados()
        
def download(valor):
    global NomeBanco
    global NomeServer
    ### PEGA O DIRETORIO QUE O USUÁRIO QUER SALVAR NO COMPUTADOR
    Diretorio = Tk()
    Diretorio.withdraw()
    DiretorioSelecionado = filedialog.askdirectory()
    ############################################################
    print(DiretorioSelecionado)
    conexao = conexaobanco(NomeServer, NomeBanco)
    cursor = conexao.cursor()
    cursor.execute("SELECT PDF_Pipe FROM BancoPipe WHERE COD_Pipe = '{0}'".format(valor))
    val = cursor.fetchone()
    if val:
        for x in val:
            ### SALVA O ARQUIVO EM FORMATO .PDF NO DIRETORIO SELECIONADO
            doguinho = open(DiretorioSelecionado+'\PIPE-Code-'+valor+'.pdf', 'wb')
            doguinho.write(x)
            doguinho.close()
            if DiretorioSelecionado:
                QMessageBox.about(SQLview, "Dado Concluido", "O arquivo foi transferido para o diretório especificado!")
    
def ListarDados():
    conexao = conexaobanco(NomeServer, NomeBanco)
    cursor = conexao.cursor()
    cursor.execute("SELECT COD_Pipe FROM BancoPipe")
    val = cursor.fetchall()
    SQLview.tabela.setRowCount(len(val))
    SQLview.tabela.setColumnCount(3)
    for x in range(0, len(val)):
        for y in range(1):
            #### GERA UM TABLEWIDGET COM TODAS AS INFORMAÇÕES DO BANCO #########
            codigo = str(val[x][y])
            botaoDel = QtWidgets.QPushButton('Deletar')
            botaoDel.setStyleSheet('QPushButton {background-color:#A60100; font:bold; font-size:10px}')
            botaoDow = QtWidgets.QPushButton('Baixar')
            botaoDow.setStyleSheet('QPushButton {background-color:#0FB328; font:bold; font-size:10px}')
            #botaoDel.clicked.connect(test)
            #botaoDel.clicked.connect(lambda: deletar('{0}'.format(SQLview.tabela.item(x, y).text())))
            #botaoDel.clicked.connect(lambda: deletar('{0}'.format(SQLview.tabela.item(x, y).text())))
            #botaoDel.clicked.connect(lambda who=str(codigo+""): deletar(who))
            ###### GERA TODOS OS BOTÕES DO BANCO DE CADA LINHA ##############
            ##### SÃO CRIADA AS FUNÇÕES PASSANDO O PARAMETRO O COD_Pipe ########
            botaoDel.clicked.connect (lambda state, x = codigo: deletar(x))
            botaoDow.clicked.connect (lambda state, x = codigo: download(x))
            SQLview.tabela.setItem(x, y, QtWidgets.QTableWidgetItem(codigo))
            SQLview.tabela.setCellWidget(x, 1, botaoDel)
            SQLview.tabela.setCellWidget(x, 2, botaoDow)
            header = SQLview.tabela.horizontalHeader()       
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
    SQLview.show()

def AcessarCodigo():
    SQLcodigo.show()

def Pesquisar():
    valor = SQLcodigo.PesquisarTexto.text()
    SQLcodigo.PesquisarTexto.setText('')
    try:
        conexao = conexaobanco(NomeServer, NomeBanco)
        cursor = conexao.cursor()
        cursor.execute("SELECT COD_Pipe FROM BancoPipe WHERE COD_Pipe = '{0}'".format(valor))
        val = cursor.fetchall()
        if val:
            SQLcodigo.tabela.setRowCount(len(val))
            SQLcodigo.tabela.setColumnCount(3)
            for x in range(0, len(val)):
                for y in range(1):
                    codigo = str(val[x][y])
                    botaoDel = QtWidgets.QPushButton('Deletar')
                    botaoDel.setStyleSheet('QPushButton {background-color:#A60100; font:bold; font-size:10px}')
                    botaoDow = QtWidgets.QPushButton('Baixar')
                    botaoDow.setStyleSheet('QPushButton {background-color:#0FB328; font:bold; font-size:10px}')
                    #botaoDel.clicked.connect(test)
                    #botaoDel.clicked.connect(lambda: deletar('{0}'.format(SQLview.tabela.item(x, y).text())))
                    #botaoDel.clicked.connect(lambda: deletar('{0}'.format(SQLview.tabela.item(x, y).text())))
                    #botaoDel.clicked.connect(lambda who=str(codigo+""): deletar(who))
                    botaoDel.clicked.connect (lambda state, x = codigo: deletar(x))
                    botaoDow.clicked.connect (lambda state, x = codigo: download(x))
                    SQLcodigo.tabela.setItem(x, y, QtWidgets.QTableWidgetItem(codigo))
                    SQLcodigo.tabela.setCellWidget(x, 1, botaoDel)
                    SQLcodigo.tabela.setCellWidget(x, 2, botaoDow)
                    header = SQLcodigo.tabela.horizontalHeader()       
                    header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
                    header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
                    header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        else:
            QMessageBox.about(SQLcodigo, "Informações do Banco", "A sua busca não retornou nenhum dado")
    except Exception:
        QMessageBox.about(SQLcodigo, "Erro SQL", "Houve um erro ao fazer a consulta para o SQL")
def InfoBanco():
    global ConnectServer
    global NomeServer
    global NomeBanco 
    QMessageBox.about(SQLAccess, "Informações do Banco", "Você está conectado ao SQL\n{0}\n\nStatus de conexão: {1}\nNome do Banco: {2}".format(NomeServer, 'Connectado' if ConnectServer else 'Desconectado', NomeBanco))
#####################################################################################################
if __name__ == '__main__':
    Aplicativo = QtWidgets.QApplication([]) #Usar via .ui
    SQLlogin = uic.loadUi(os.getcwd()+"\\uic\\SQL-Login.ui") #Selecionar arquivo .ui
    SQLlogin.SQLname.textChanged.connect(buttonverif)
    SQLlogin.SelectAut.activated.connect(buttonverif)
    SQLlogin.SelectAut.activated.connect(sqlserver)
    SQLlogin.SQLLogin_Senha.textChanged.connect(buttonverif)
    SQLlogin.SQLLogin_Name.textChanged.connect(buttonverif)
    SQLlogin.Connect.clicked.connect(ConnectarServidor)
    SQLlogin.ShowSenha.clicked.connect(mostrarsenha)
    #################### 2 PROCESSOS ##########################################
    Processos2 = uic.loadUi(os.getcwd()+"\\uic\\Processos2.ui")
    Processos2.GerarTabela.clicked.connect(GerarTabela2)
    Processos2.GerarRandom.triggered.connect(GerarNum2)
    Processos2.TipoEscala.activated.connect(GerarCrit2)
    Processos2.LimparCampos.triggered.connect(LimparCampos2)
    Processos2.GerarRelatorio.clicked.connect(GerarRel2)
    Processos2.SalvarSQL.triggered.connect(GerarSQL2)
    #################### 3 PROCESSOS ##########################################
    Processos3 = uic.loadUi(os.getcwd()+"\\uic\\Processos3.ui")
    Processos3.GerarTabela.clicked.connect(GerarTabela3)
    Processos3.GerarRandom.triggered.connect(GerarNum3)
    Processos3.TipoEscala.activated.connect(GerarCrit3)
    Processos3.GerarRelatorio.clicked.connect(GerarRel3)
    Processos3.SalvarSQL.triggered.connect(GerarSQL3)
    #################### 4 PROCESSOS ##########################################
    Processos4 = uic.loadUi(os.getcwd()+"\\uic\\Processos4.ui")
    Processos4.GerarTabela.clicked.connect(GerarTabela4)
    Processos4.GerarRandom.triggered.connect(GerarNum4)
    Processos4.TipoEscala.activated.connect(GerarCrit4)
    Processos4.GerarRelatorio.clicked.connect(GerarRel4)
    Processos4.SalvarSQL.triggered.connect(GerarSQL4)
    #################### 5 PROCESSOS ##########################################
    Processos5 = uic.loadUi(os.getcwd()+"\\uic\\Processos5.ui")
    Processos5.GerarTabela.clicked.connect(GerarTabela5)
    Processos5.GerarRandom.triggered.connect(GerarNum5)
    Processos5.TipoEscala.activated.connect(GerarCrit5)
    Processos5.LimparCampos.triggered.connect(LimparCampos5)
    Processos5.GerarRelatorio.clicked.connect(GerarRel5)
    Processos5.SalvarSQL.triggered.connect(GerarSQL5)
    #################### 6 PROCESSOS ##########################################
    Processos6 = uic.loadUi(os.getcwd()+"\\uic\\Processos6.ui")
    Processos6.GerarTabela.clicked.connect(GerarTabela6)
    Processos6.GerarRandom.triggered.connect(GerarNum6)
    Processos6.TipoEscala.activated.connect(GerarCrit6)
    Processos6.LimparCampos.triggered.connect(LimparCampos6)
    Processos6.GerarRelatorio.clicked.connect(GerarRel6)
    Processos6.SalvarSQL.triggered.connect(GerarSQL6)
    #################### 7 PROCESSOS ##########################################
    Processos7 = uic.loadUi(os.getcwd()+"\\uic\\Processos7.ui")
    Processos7.GerarTabela.clicked.connect(GerarTabela7)
    Processos7.GerarRandom.triggered.connect(GerarNum7)
    Processos7.TipoEscala.activated.connect(GerarCrit7)
    Processos7.LimparCampos.triggered.connect(LimparCampos7)
    Processos7.GerarRelatorio.clicked.connect(GerarRel7)
    Processos7.SalvarSQL.triggered.connect(GerarSQL7)
    ################### Seleção Processos #####################################
    SelectProcess = uic.loadUi(os.getcwd()+"\\uic\\ProcessosSelect.ui")
    SelectProcess.LoadProcess.clicked.connect(carregarprocessos)
    ################### ACESSAR SQL ###########################################
    SQLAccess = uic.loadUi(os.getcwd()+"\\uic\\SQLAccess.ui")
    SQLview = uic.loadUi(os.getcwd()+"\\uic\\SQLview.ui")
    SQLcodigo = uic.loadUi(os.getcwd()+"\\uic\\SQLcodigo.ui")
    SQLcodigo.Pesquisar.clicked.connect(Pesquisar)
    SQLAccess.ListarDados.clicked.connect(ListarDados)
    SQLAccess.AcessarCodigo.clicked.connect(AcessarCodigo)
    SQLAccess.DesconectarBanco.triggered.connect(DesconectarSQL)
    SQLAccess.InfoBanco.triggered.connect(InfoBanco)
    ####################    Main    ###########################################
    arquivomain = os.getcwd()+"\\uic\\Main.ui"
    Main = uic.loadUi(arquivomain)
    Main.AbrirProcesso.clicked.connect(abrirselect)
    Main.ConectarSQL.clicked.connect(abrirsql)
    Main.CarregarPIPE.clicked.connect(CarregarPIPE)
    Main.cred.triggered.connect(devinfo)
    Main.infodev.triggered.connect(devinfo2)
    Main.DesconectarSQL.triggered.connect(DesconectarSQL)
    Main.show()
    Aplicativo.exec() #Executar programa
    # WILLIANQUIRINO\SQLEXPRESS