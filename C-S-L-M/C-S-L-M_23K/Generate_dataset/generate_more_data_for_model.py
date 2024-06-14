import json
import cv2
import torch
import os
from ultralytics import YOLO

# Carregar o modelo treinado
model = YOLO("23K_5_epoch/best.pt")

def visualize_predictions(image_path, predictions, output_image_path):
    image = cv2.imread(image_path)
    height, width, _ = image.shape
    txt_lines = []
    
    for pred in predictions:
        confidence = pred['confidence']
        if confidence > 0.7:  # Verificar se a confiança é maior que 0.7
            x = int(pred['x'])
            y = int(pred['y'])
            w = int(pred['width'])
            h = int(pred['height'])
            class_id = pred['class_id']
            

            # Calcular as coordenadas normalizadas
            x_center = x / width
            y_center = y / height
            norm_width = w / width
            norm_height = h / height
            
            # Adicionar linha ao txt_lines
            txt_lines.append(f"{class_id} {x_center:.6f} {y_center:.6f} {norm_width:.6f} {norm_height:.6f}\n")
            
            # Desenhar a caixa delimitadora
            start_point = (x - w // 2, y - h // 2)
            end_point = (x + w // 2, y + h // 2)
            cv2.rectangle(image, start_point, end_point, (255, 0, 0), 2)
            
            # Adicionar o rótulo
            label = f"{pred['class']} ({confidence:.2f})"
            cv2.putText(image, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    
    # Salvar a imagem com as predições
    cv2.imwrite(output_image_path, image)
    print(f"Imagem salva em: {output_image_path}")
    
    # Salvar os rótulos no arquivo txt
    txt_path = output_image_path.replace(".jpg", ".txt").replace(".png", ".txt")
    with open(txt_path, 'w') as f:
        f.writelines(txt_lines)
    print(f"Rótulos salvos em: {txt_path}")

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

            # Adicionar as informações da predição à lista apenas se a confiança for maior que 0.7
            if confidence > 0.5:
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

def process_directory(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    for filename in os.listdir(input_directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(input_directory, filename)
            output_image_path = os.path.join(output_directory, filename)
            output_json_path = os.path.join(output_directory, filename.replace(".jpg", ".json").replace(".png", ".json"))

            # Extrair predições e salvar em um arquivo JSON
            extract_predictions(image_path, output_json_path)

            # Carregar as predições do JSON
            with open(output_json_path, 'r') as json_file:
                data = json.load(json_file)
                predictions = data["predictions"]

            # Visualizar as predições e salvar rótulos
            visualize_predictions(image_path, predictions, output_image_path)
            
            # Excluir o arquivo JSON
            os.remove(output_json_path)
            print(f"Arquivo JSON {output_json_path} excluído.")

# Caminho para o diretório de entrada
input_directory = "teste"

# Caminho para o diretório de saída
output_directory = "output_teste"

# Processar todas as imagens no diretório de entrada
process_directory(input_directory, output_directory)
