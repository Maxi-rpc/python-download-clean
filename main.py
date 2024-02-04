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
    count = 0
    path_file = path_origin + file
    path_destination = ''

    for ext in ext_docs:
        if ext in file_ext:
            path_destination = path_documents
        
    for ext in ext_music:
        if ext in file_ext:
            path_destination = path_music

    if path_destination != '':
        print(f'Se movera el archivo: {file} a la carpeta {path_destination}')
        shutil.move(path_file, path_destination)
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
