from matplotlib.collections import LineCollection
import matplotlib.pyplot as ps
#import io
from docx import Document
#import pandas as pd
import numpy as np
#import datetime



#processos = [('P1', 15, 1, 4),('P2',20, 2, 3),('P3', 20, 3, 1),('P4', 45, 4, 2)]
#processos = [('P1', 7, 1, 2),('P2', 12, 2, 3),('P3', 40, 3, 4),('P4', 25, 4, 2),('P5', 36, 5, 1),('P6', 20, 6, 3)]
#processos = [('P1', 15, 1, 3),('P2',30, 2, 1),('P3', 5, 3, 4),('P4', 10, 4, 2)]
#ORDEM DE CHEGADA
def calcularFIFO(valor): #Recebe list ('Nome Processo', 'Tempo de execução', 'Ordem de chegada', 'Prioridade')
    tempoEspera = [] #Pega a list de tempo de espera por processo
    tempoAux = 0    
    tempoTotal = 0   #Pega o tempo total gasto
    tempoList = []   #Pega a list do tempo total gasto
    tempoMedioEspera = 0 #Pega a média por processamento
    processosExecutados = [] #Pega a descrição dos processos
    process = sorted(valor, key = lambda test: test[2])
    for x in range(len(process)):
        if len(tempoEspera) == 0:
            tempoEspera.append(tempoAux)
            tempoTotal += process[x][1]
            tempoList.append(tempoTotal)
            processosExecutados.append(process[x][0])
        else: 
            tempoAux += process[x-1][1]
            tempoTotal += process[x][1]
            tempoList.append(tempoTotal)
            tempoEspera.append(tempoAux)
            processosExecutados.append(process[x][0])
    tempoMedioEspera = sum(tempoEspera)/len(process)
    return process, tempoEspera, tempoTotal, tempoList, tempoMedioEspera, processosExecutados, valor 
    #Retorna: process             <- vetor dos processos ordenados por prioridade   
    #         tempoEspera         <- vetor em lista por tempo de espera
    #         tempoTotal          <- Tempo total utilizado
    #         templist            <- Lista do tempo total
    #         tempoMedioEspera    <- calculo do tempo médio de espera
    #         processosExecutados <- Ordem dos processos executados (p1,p2...)  
    #         valor               <- Retorna a lista de processos 


#MENOR TEMPO - Tempo de execução
def calcularSJF(valor, ordem): #Recebe list ('Nome Processo', 'Tempo de execução', 'Ordem de chegada', 'Prioridade')
    tempoEspera = [] #Pega a list de tempo de espera por processo
    tempoAux = 0    
    tempoTotal = 0   #Pega o tempo total gasto
    tempoList = []   #Pega a list do tempo total gasto
    tempoMedioEspera = 0 #Pega a média por processamento
    processosExecutados = [] #Pega a descrição dos processos
    #Ordem = 1 (Ordem de chegada - FIFO), Ordem = 2 (Ordem de prioridade - Por Prioridade)
    if ordem == 1:
            process = sorted(valor, key = lambda test: (test[1], test[2]))
    if ordem == 2:
        process = sorted(valor, key = lambda test: (test[1], test[3]))
    for x in range(len(process)):
        if len(tempoEspera) == 0:
            tempoEspera.append(tempoAux)
            tempoTotal += process[x][1]
            tempoList.append(tempoTotal)
            processosExecutados.append(process[x][0])
        else: 
            tempoAux += process[x-1][1]
            tempoTotal += process[x][1]
            tempoList.append(tempoTotal)
            tempoEspera.append(tempoAux)
            processosExecutados.append(process[x][0])
    tempoMedioEspera = sum(tempoEspera)/len(process)
    return process, tempoEspera, tempoTotal, tempoList, tempoMedioEspera, processosExecutados, valor  
    #Retorna: process             <- vetor dos processos ordenados por prioridade   
    #         tempoEspera         <- vetor em lista por tempo de espera
    #         tempoTotal          <- Tempo total utilizado
    #         templist            <- Lista do tempo total
    #         tempoMedioEspera    <- calculo do tempo médio de espera
    #         processosExecutados <- Ordem dos processos executados (p1,p2...)   
    #         valor               <- Retorna a lista de processos 

#MENOR PRIORIDADE
def calcularPorPrioridade(valor, ordem: int): #Recebe list ('Nome Processo', 'Tempo de execução', 'Ordem de chegada', 'Prioridade')
    tempoEspera = [] #Pega a list de tempo de espera por processo
    tempoAux = 0    
    tempoTotal = 0   #Pega o tempo total gasto
    tempoList = []   #Pega a list do tempo total gasto
    tempoMedioEspera = 0 #Pega a média por processamento
    processosExecutados = [] #Pega a descrição dos processos
    #Ordem = 1 (critério tempo de execução - SJF), Ordem = 2 (critério ordem de chegada - FIFO)
    if ordem == 1:
        process = sorted(valor, key = lambda test: (test[3], test[1]))
    if ordem == 2:
        process = sorted(valor, key = lambda test: (test[3], test[2]))
    for x in range(len(process)):
        if len(tempoEspera) == 0:
            tempoEspera.append(tempoAux)
            tempoTotal += process[x][1]
            tempoList.append(tempoTotal)
            processosExecutados.append(process[x][0])
        else: 
            tempoAux += process[x-1][1]
            tempoTotal += process[x][1]
            tempoList.append(tempoTotal)
            tempoEspera.append(tempoAux)
            processosExecutados.append(process[x][0])
    tempoMedioEspera = sum(tempoEspera)/len(process)
    return process, tempoEspera, tempoTotal, tempoList, tempoMedioEspera, processosExecutados, valor  
    #Retorna: process             <- vetor dos processos ordenados por prioridade   
    #         tempoEspera         <- vetor em lista por tempo de espera
    #         tempoTotal          <- Tempo total utilizado
    #         templist            <- Lista do tempo total
    #         tempoMedioEspera    <- calculo do tempo médio de espera
    #         processosExecutados <- Ordem dos processos executados (p1,p2...)   
    #         valor               <- Retorna a lista de processos 

def test(valor):
    ps.ylabel('Tempo de Execução (ns)')
    ps.xlabel('Processos')
    ps.axis(ymin=0 ,ymax = valor[2]+50)
    #ps.plot(processos, tempo, label='Tempo de Execução', marker='o') #(y, x, 'legenda', 'pontos')
    ps.grid(True) #Deixar tabelado
    ps.stem(valor[5], valor[3])
    ps.show()
    #ps.savefig('SalveArquivo.png') salvar arquivo

def CriarTabela(processos, inicio, fim):
    # VARIAVEIS DE CONSTRUÇÃO DO GRÁFICO
    y = processos # PROCESSOS DA TABELA Y
    c = []  # TIPO USADO (quantidade de processos)
    for x in y:
        c.append(1)
    xinicio = inicio #Inicio processo
    xfim = fim # Fim processo
    # CORES DA TABELA
    color_mapper = np.vectorize(lambda x: {0: 'red', 1: 'blue'}.get(x))
    # Traça uma linha de acordo com os dados apresentados
    ps.hlines(y, xinicio, xfim, colors=color_mapper(c), lw=25)
    #plt.hlines(cps, s_load, f_load, colors="red", lw=4)
    ps.ylabel('PROCESSOS')
    ps.xlabel('Tempo de Execução (ns)')
    ps.grid(True) #Deixar tabelado
    ps.show()

def GerarTabela(valor, exibir: bool): #Gera Tabela de Gantt e retorna os valores
    p = valor
    xini = valor[1]#p[1]
    xfim = valor[3]
    tempototal = valor[2]
    y = p[5]
    processos = []
    inicio = []
    fim = []
    tups = []
    inicial = 0
    while inicial < len(y):
        tups.append([y[inicial], xini[inicial], xfim[inicial]])
        inicial+=1
    process = sorted(tups, key = lambda test: test[0])
    for x in process:
        processos.append(x[0])
        inicio.append(x[1])
        fim.append(x[2])
    if exibir == True:
        CriarTabela(processos, inicio, fim)
    return processos, inicio, fim, tempototal, valor[6] 
    '''
    # VARIAVEIS DE CONSTRUÇÃO DO GRÁFICO
    y = valor[5] # PROCESSOS DA TABELA Y
    c = []  # TIPO USADO (quantidade de processos)
    for x in y:
        c.append(0)
    xinicio = valor[1] #Inicio processo
    xfim = valor[3] # Fim processo
    # CORES DA TABELA
    color_mapper = np.vectorize(lambda x: {0: 'red', 1: 'blue'}.get(x))
    # Plot a line for every line of data in your file
    ps.hlines(y, xinicio, xfim, colors=color_mapper(c))
    ps.ylabel('Tempo de Execuçao (ns)')
    ps.xlabel('Processos')
    ps.grid(True) #Deixar tabelado
    ps.show()
    '''
#test()

#GerarDocumento.GerarDocumento(processos, calcularFIFO(processos), GerarTabela(calcularFIFO(processos), False), 'FIFO', 'Nenhum')