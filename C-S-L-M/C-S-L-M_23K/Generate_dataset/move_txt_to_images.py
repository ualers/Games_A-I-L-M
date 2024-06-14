import os
import shutil

# Caminhos para as pastas
labels_path = 'labels'
images_path = 'images'

# Função para mover arquivos .txt da pasta labels para a pasta images
def move_labels_to_images(labels_path, images_path):
    for label_file in os.listdir(labels_path):
        if label_file.endswith('.txt'):
            label_file_path = os.path.join(labels_path, label_file)
            destination_path = os.path.join(images_path, label_file)

            # Mover o arquivo .txt para a pasta images
            shutil.move(label_file_path, destination_path)
            print(f'Movido: {label_file_path} -> {destination_path}')

# Chamar a função para mover os arquivos
move_labels_to_images(labels_path, images_path)
