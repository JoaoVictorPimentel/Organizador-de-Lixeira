import shutil
import os
import glob

fontes = r'C:\Users\joaov\Downloads'
arquivos = os.listdir(fontes)

destino1 = r'C:\Users\joaov\Downloads\Zips'
destino2 = r'C:\Users\joaov\Downloads\Aplicativos'
destino3 = r'C:\Users\joaov\Downloads\Imagens'
destino4 = r'C:\Users\joaov\Downloads\Pdf'

arquivosZip = glob.glob(os.path.join(r'C:\Users\joaov\Downloads\*.zip'))
arquivosExe = glob.glob(os.path.join(r'C:\Users\joaov\Downloads\*.exe'))
arquivosGif = glob.glob(os.path.join(r'C:\Users\joaov\Downloads\*.gif'))
arquivosPng = glob.glob(os.path.join(r'C:\Users\joaov\Downloads\*.png'))
arquivosJpg = glob.glob(os.path.join(r'C:\Users\joaov\Downloads\*.jpg'))
arquivosPdf = glob.glob(os.path.join(r'C:\Users\joaov\Downloads\*.pdf'))

for arquivos in arquivosZip:
    if os.path.isfile(arquivos):
        shutil.move(arquivos, destino1)

for arquivos in arquivosExe:
    if os.path.isfile(arquivos):
        shutil.move(arquivos, destino2)

for arquivos in arquivosGif:
    if os.path.isfile(arquivos):
        shutil.move(arquivos, destino3)

for arquivos in arquivosPng:
    if os.path.isfile(arquivos):
        shutil.move(arquivos, destino3)

for arquivos in arquivosJpg:
    if os.path.isfile(arquivos):
        shutil.move(arquivos, destino3)

for arquivos in arquivosPdf:
    if os.path.isfile(arquivos):
        shutil.move(arquivos, destino4)


