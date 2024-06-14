import os
import shutil

# Caminhos para as pastas
source_path = 'images'
destination_path = 'C:/Users/ualer/OneDrive/Área de Trabalho/csgo/Dataset_100k/C-S-L-M_Dataset_40k_class_1/train'

# Função para mover arquivos da pasta source para a pasta destination
def move_files(source_path, destination_path):
    # Certificar-se de que o diretório de destino existe
    os.makedirs(destination_path, exist_ok=True)

    # Percorrer todos os arquivos na pasta source
    for file_name in os.listdir(source_path):
        # Definir o caminho completo do arquivo
        source_file_path = os.path.join(source_path, file_name)
        destination_file_path = os.path.join(destination_path, file_name)

        # Mover o arquivo para a pasta de destino
        shutil.move(source_file_path, destination_file_path)
        print(f'Movido: {source_file_path} -> {destination_file_path}')

# Chamar a função para mover os arquivos
move_files(source_path, destination_path)
