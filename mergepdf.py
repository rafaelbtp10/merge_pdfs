import os
import time
from tkinter.filedialog import asksaveasfilename, askdirectory
import PyPDF2 as pypdf

merger = pypdf.PdfMerger()
print('='*30)
print(str('Escolha o diretório dos PDFs').center(30))
time.sleep(0.5)
diretoriopdfs = askdirectory()
lista_arquivos = os.listdir(diretoriopdfs)

for arquivo in lista_arquivos:
    if '.pdf' in arquivo:
        print('Mesclando...')
        time.sleep(0.25)
        merger.append(f'{diretoriopdfs}/{arquivo}')
print('='*30)
print(str('Escolha onde salvar o PDF unificado.').center(30))
time.sleep(0.5)
merger.write(asksaveasfilename(defaultextension=".pdf"))
print('='*30)
print(str('FIM.').center(30))
