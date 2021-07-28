import matplotlib.pyplot as ps
import io
from docx import Document

processos = [('P1', 15, 1, 4),('P2',20, 2, 3),('P3', 20, 3, 1),('P4', 45, 4, 2)]
#processos = [('P1', 7, 1, 2),('P2', 12, 2, 3),('P3', 40, 3, 4),('P4', 25, 4, 2),('P5', 36, 5, 1),('P6', 20, 6, 3)]

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
    return process, tempoEspera, tempoTotal, tempoList, tempoMedioEspera, processosExecutados 
    #Retorna: process             <- vetor dos processos ordenados por prioridade   
    #         tempoEspera         <- vetor em lista por tempo de espera
    #         tempoTotal          <- Tempo total utilizado
    #         templist            <- Lista do tempo total
    #         tempoMedioEspera    <- calculo do tempo médio de espera
    #         processosExecutados <- Ordem dos processos executados (p1,p2...)   


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
    return process, tempoEspera, tempoTotal, tempoList, tempoMedioEspera, processosExecutados 
    #Retorna: process             <- vetor dos processos ordenados por prioridade   
    #         tempoEspera         <- vetor em lista por tempo de espera
    #         tempoTotal          <- Tempo total utilizado
    #         templist            <- Lista do tempo total
    #         tempoMedioEspera    <- calculo do tempo médio de espera
    #         processosExecutados <- Ordem dos processos executados (p1,p2...)   

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
    return process, tempoEspera, tempoTotal, tempoList, tempoMedioEspera, processosExecutados 
    #Retorna: process             <- vetor dos processos ordenados por prioridade   
    #         tempoEspera         <- vetor em lista por tempo de espera
    #         tempoTotal          <- Tempo total utilizado
    #         templist            <- Lista do tempo total
    #         tempoMedioEspera    <- calculo do tempo médio de espera
    #         processosExecutados <- Ordem dos processos executados (p1,p2...)   


def GerarTabela(valor): #Gera Tabela de Gantt
    ps.ylabel('Tempo de Execuçao (ns)')
    ps.xlabel('Processos')
    ps.axis(ymin=0 ,ymax = valor[2]+50)
    #ps.plot(processos, tempo, label='Tempo de Execução', marker='o') #(y, x, 'legenda', 'pontos')
    ps.grid(True) #Deixar tabelado
    ps.stem(valor[5], valor[3])
    ps.show()
    #ps.savefig('SalveArquivo.png') salvar arquivo

def Test():    
    fig, gnt = ps.subplots() 
    gnt.set_ylim(0, 50) 
    gnt.set_xlim(0, 160) 
    gnt.set_xlabel('TEMPO (NS)') 
    gnt.set_ylabel('PROCESSOS') 
    gnt.set_yticks([15, 25, 35]) 
    gnt.set_yticklabels(['P1', 'P2', 'P3']) 
    gnt.grid(True) 
    gnt.broken_barh([(40, 50)], (30, 9), facecolors =('tab:orange')) 
    gnt.broken_barh([(110, 10), (150, 10)], (10, 9), 
                         facecolors ='tab:blue') 
    gnt.broken_barh([(10, 50), (100, 20), (130, 10)], (20, 9), 
                                  facecolors =('tab:red')) 
                                
    ps.show()


#GerarTabela(calcularFIFO(processos))
#test()