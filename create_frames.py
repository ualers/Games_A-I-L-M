import cv2
import os
import uuid

# Função para gerar um nome de arquivo aleatório
def generate_random_filename():
    return str(uuid.uuid4()) + ".png"

# Carregar o vídeo
video_path = "1.mp4"
cap = cv2.VideoCapture(video_path)

# Diretório onde os frames serão salvos
output_dir = "datasets/naruto_data_2"
os.makedirs(output_dir, exist_ok=True)

frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Gerar um nome de arquivo aleatório
    filename = generate_random_filename()
    filepath = os.path.join(output_dir, filename)

    # Salvar o frame como PNG
    cv2.imwrite(filepath, frame)
    frame_count += 1

    # Exibir progresso
    if frame_count % 100 == 0:
        print(f"{frame_count} frames processados.")

cap.release()
print("Processamento concluído.")
