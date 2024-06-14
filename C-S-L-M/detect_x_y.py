import json
import cv2
import torch
from ultralytics import YOLO

# Carregar o modelo treinado
model = YOLO("23K_5_epoch/best.pt")

# Função para realizar predições e extrair informações
def extract_predictions(image_path, output_json_path):
    # Carregar a imagem
    image = cv2.imread(image_path)
    
    # Realizar predições
    results = model(image)

    # Lista para armazenar as informações das predições
    predictions = []

    # Iterar sobre as predições
    for result in results:
        for box in result.boxes:
            x, y, w, h = box.xywh[0].tolist()  # Converte o tensor para lista de floats
            confidence = box.conf[0].item()  # Converte o tensor para float
            class_id = int(box.cls[0].item())  # Converte o tensor para int
            class_name = model.names[class_id]  # Obter o nome da classe

            # Adicionar as informações da predição à lista
            predictions.append({
                "x": x,
                "y": y,
                "width": w,
                "height": h,
                "confidence": confidence,
                "class": class_name,
                "class_id": class_id
            })

    # Salvar as predições em um arquivo JSON
    with open(output_json_path, 'w') as json_file:
        json.dump({"predictions": predictions}, json_file, indent=4)

# Caminho da imagem de entrada
image_path = "2.jpg"

# Caminho do arquivo JSON de saída
output_json_path = "predictions.json"

# Extrair predições e salvar em um arquivo JSON
extract_predictions(image_path, output_json_path)
