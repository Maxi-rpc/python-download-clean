import os
import shutil

# soft_config
tittle = 'Limpieza de descargas'
path_origin = 'F:\\Downloads\\'
path_documents = 'C:\\Users\\Max\\Documents\\'
path_music = 'F:\\Música\\'
ext_docs = ['.pdf', '.xls', '.docx']
ext_music = ['.mp3', '.m4a']

def move_to_folder(file, file_ext):
    isMove = False
    for ext in ext_docs:
        if ext in file_ext:
            print(f'Se movera el archivo: {file} a la carpeta {path_documents}')
            shutil.move(path_origin + file, path_documents)
            isMove = True
        
    for ext in ext_music:
        if ext in file_ext:
            print(f'Se movera el archivo: {file} a la carpeta {path_music}')
            shutil.move(path_origin + file, path_music)
            isMove = True

    count = 0
    if isMove:
        count = 1
        
    return count


def ordenar(archivos):
    cont = 0
    for item in archivos:
        arch_ext = item[-5:]
        unidad = move_to_folder(item, arch_ext)
        cont = cont + unidad
    return cont
        

def main():
    print(tittle)
    list_archivos = os.listdir(path_origin)
    count = ordenar(list_archivos)
    
    cont_total = len(list_archivos)
    print(f'Se movieron: {count} / {cont_total}')
    



main()
