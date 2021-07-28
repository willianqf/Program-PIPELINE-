from docx import Document
from docx.enum.style import WD_STYLE_TYPE # Define estilo para paragrafo
from docx.enum.table import WD_TABLE_ALIGNMENT # Define estilo para paragrafo
from docx.enum.text import WD_ALIGN_PARAGRAPH #Define alinhamento de paragráfo
from docx.shared import Pt #Define tamanho da fonte
from docx.shared import RGBColor #Define a cor da fonte
from docx.shared import Inches #Define tamanho

stre = 'FIFO'
valor = {
    "Titulo":"Calculo de Escalonamento de Processos",
    "Informações": [
        {
            "Test1":"Processo realizado: \nBase de Calculo: ",
            "Texto":"Aqui vai um texto",
            "Image":"PipesTransparent.png",
            "Table":["A","b","c"],
        }
    ]
}
def GerarDocumento():
    documento = Document()
    documento.add_heading("Titulo Atribuido", 0) #Definir Titulo ('Titulo', (peso))
    documento.add_paragraph("Adiciona um paragrafo no documento")
    documento.save("NomeDoDocumento.docx") #Salva o documento no local do script


document = Document()
styles = document.styles

# Style Paragraph
p = styles.add_style("Paragraph", WD_STYLE_TYPE.PARAGRAPH)
p.font.name = "Calibri"
p.font.size = Pt(11)

#Style Heading 2
h2 = styles.add_style("H2", WD_STYLE_TYPE.PARAGRAPH)
h2.font.name = "Calibri"
h2.font.size = Pt(13)
h2.font.color.rgb = RGBColor(79, 129, 189)
h2.font.bold = False #Define se vai ser negrito ou não

#Style Heading 3
h3 = styles.add_style("H3", WD_STYLE_TYPE.PARAGRAPH)
h3.font.name = "Calibri"
h3.font.size = Pt(12)
h3.font.color.rgb = RGBColor(79, 129, 189)
h3.font.bold = False #Define se vai ser negrito ou não

document.add_heading(valor.get('Titulo'), 0)
for var in valor.get('Informações'):
    document.add_picture(var.get("Image"), width=Inches(1.25))
    document.add_paragraph(var.get("Table"), style="H3")
    document.add_paragraph(var.get("Test1"), style="H2")
    document.add_paragraph(var.get("Text"), style="Paragraph")
    document.add_paragraph(var.get("Image"), style="H3")
    table = document.add_table(rows = 1, cols=3, style="Table Grid") #CRIA UMA TABELA (row = linhas, cols = colunas, formatação)
    table.aligment = WD_TABLE_ALIGNMENT.CENTER #Define tipo de alinhamento
    table.autofit = False #Define espaçamento (Verdadeiro ou Falso)
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = "col1"
    hdr_cells[1].text = "col2"
    hdr_cells[2].text = "col3"
    row_cells = table.add_row().cells
    for index, var2 in enumerate(var.get("Table")):
        row_cells[index].text = var2

document.save("SavarDados.docx")