import os
import win32com.client
import subprocess
#Replace excel=comtype.client.blablabla to

'''
wdFormatPDF = 17
in_file=os.getcwd()+"\RelatorioPIPE-2021-08-16-6800.docx"
out_file=os.getcwd()+"\RelatorioPIPE-2021-08-16-6800.pdf"
word=win32com.client.DispatchEx("Word.Application")
#word.Visible = True
doc=word.Documents.Open(in_file) # Abre o arquivo docx
doc.SaveAs(out_file, FileFormat=wdFormatPDF) # Faz a conversão em PDF
doc.Close() # Fecha o arquivo .docx
#word.Visible = False
word.Quit() # Fechar aplicação
'''
#os.chdir(os.getcwd()+"\\RelatorioPIPE-2021-08-16-9597.pdf")
#os.system(os.getcwd()+"\\RelatorioPIPE-2021-08-16-9597.pdf")
#os.startfile(os.getcwd()+"\\RelatorioPIPE-2021-08-16-9520.docx")
