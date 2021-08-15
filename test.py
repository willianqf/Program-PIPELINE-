import pyodbc

def conexaobanco(sqlconect, banco): #Conexão com SQL Server
    #conexao = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';UID='+username+';PWD='+ password
    conexao = "Driver={SQL Server Native Client 11.0};Server="+sqlconect+";Database="+banco+";Trusted_Connection=yes;"
    return pyodbc.connect(conexao)

cur = conexaobanco('WILLIANQUIRINO\SQLEXPRESS', 'PIPESQL')
cursor = cur.cursor()
values = "DELETE FROM BancoPipe WHERE COD_Pipe = '95TUrBSf24efNcBOnNF2hHc'" ## DADO DELETADO
cursor.execute(values) 
cursor.commit()