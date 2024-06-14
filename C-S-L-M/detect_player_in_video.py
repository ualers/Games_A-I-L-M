from ultralytics import YOLO
import cv2

# Carregar o modelo treinado
model = YOLO("23K_5_epoch/best.pt")

# Carregar o vídeo
video_path = "cs 2.mp4"
cap = cv2.VideoCapture(video_path)

# Obter as informações do vídeo
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec para salvar o vídeo
out = cv2.VideoWriter('output_video.mp4', fourcc, 30.0, (int(cap.get(3)), int(cap.get(4))))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Fazer a predição no frame
    results = model(frame)

    # Iterar sobre os resultados e processar o frame
    for result in results:
        # Obter a imagem com as predições
        annotated_frame = result.plot()

    # Escrever o frame anotado no vídeo de saída
    out.write(annotated_frame)

    # Mostrar o frame anotado (opcional)
    cv2.imshow('Frame', annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar os recursos
cap.release()
out.release()
cv2.destroyAllWindows()