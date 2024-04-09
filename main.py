import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title='selecione uma pasta')

lista_arquivos = os.listdir(caminho)

locais = {
    'imagens':['.png', '.jpg', '.jpeg'],
    'planinhas': ['.xls'],
    'pdf': ['.pdf'],
    'word': ['.docx'],
    'csv':['.csv']
}

for arquivos in lista_arquivos:
    nome, extensao = os.path.splitext(f'{caminho}/{arquivos}')
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f'{caminho}/{pasta}'):
                os.mkdir(f'{caminho}/{pasta}')
            os.rename(f'{caminho}/{arquivos}', f'{caminho}/{pasta}/{arquivos}')