import albumentations as A
import cv2
import numpy as np
import random
import os
import uuid
from datetime import datetime

# Função para desnormalizar a imagem
def denormalize(image, mean, std):
    mean = np.array(mean, dtype=np.float32)
    std = np.array(std, dtype=np.float32)
    image = image * std + mean
    image = np.clip(image, 0, 1)
    image = (image * 255).astype(np.uint8)
    return image

# Função para ajustar a cor e salvar a imagem com nome aleatório
def ajuste_Cor(image_path, output_directory):
    bright = random.uniform(0.2, 0.5)
    contrastt = random.uniform(0.2, 0.5)
    saturatio = random.uniform(0.2, 0.5)
    hu = random.uniform(0.2, 0.5)
    
    # Definindo a sequência de ajustes de cor
    adjustment_pipeline = A.Compose([
        A.RandomBrightnessContrast(p=1.0),
        A.ColorJitter(brightness=bright, contrast=contrastt, saturation=saturatio, hue=hu),
        A.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
    ])
    
    # Carregar a imagem
    image = cv2.imread(image_path)
    adjusted_image = adjustment_pipeline(image=image)['image']

    # Desnormalizar a imagem
    denormalized_image = denormalize(adjusted_image, mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225))
    
    # Gerar um nome de arquivo altamente aleatório
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    unique_id = uuid.uuid4()
    base_name = os.path.basename(image_path)
    base_name_without_ext = os.path.splitext(base_name)[0]
    new_name = f'{timestamp}_{unique_id}_{base_name}'
    new_txt_name = f'{timestamp}_{unique_id}_{base_name_without_ext}.txt'

    # Salvar a imagem ajustada
    cv2.imwrite(os.path.join(output_directory, new_name), denormalized_image)

    # Caminho para o arquivo de rótulo correspondente
    label_path = os.path.splitext(image_path)[0] + '.txt'
    if os.path.exists(label_path):
        # Copiar o arquivo de rótulo para a pasta de saída
        new_label_path = os.path.join(output_directory, new_txt_name)
        with open(label_path, 'r') as f:
            labels = f.readlines()
        with open(new_label_path, 'w') as f:
            f.writelines(labels)

# Caminho para a pasta contendo as imagens
pasta = 'teste_data'
output_directory = 'output_directory'
os.makedirs(output_directory, exist_ok=True)
for _ in range(5):
    # Processar cada arquivo na pasta
    for item in os.listdir(pasta):
        if item.endswith('.jpg'):  # Filtrar apenas arquivos de imagem
            image_path = os.path.join(pasta, item)
            ajuste_Cor(image_path, output_directory)
