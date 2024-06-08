import subprocess
def executar_instalacao_de_bibliotecas():
    caminho_python = "python"
    pacotes = ['ultralytics', 'pytorch']
    comando_pip = [caminho_python, "-m", "pip", "install"]
    comando_pip.extend(pacotes)
    subprocess.call(comando_pip)
executar_instalacao_de_bibliotecas() 

from ultralytics import YOLO

# para marcar as imagens
# https://www.makesense.ai/

# Model	    size    mAPval  Speed       Speed       params  FLOPs
#           (pixels) 50-95  CPU ONNX A100 TensorRT   (M)     (B)
#                           (ms)        (ms)
# YOLOv8n	640	    37.3	80.4	    0.99	    3.2	    8.7
# YOLOv8s	640	    44.9	128.4	    1.20	    11.2	28.6
# YOLOv8m	640	    50.2	234.7	    1.83	    25.9	78.9
# YOLOv8l	640	    52.9	375.2	    2.39	    43.7	165.2
# YOLOv8x	640	    53.9	479.1	    3.53	    68.2	257.8
def main():
    import torch
    print(torch.__version__)

    print("GPU Configurada:", torch.cuda.is_available())
    print("Total de GPUs", torch.cuda.device_count())

    if torch.cuda.is_available():
        print("GPU Atual:", torch.cuda.current_device())
        print("Device", torch.cuda.device(0))
        print("Device Name", torch.cuda.get_device_name(0))
    else:
        print("Nenhuma GPU configurada")

    model = YOLO("yolov8x.pt") 

    model.train(data="naruto.yaml", epochs=20, device=0, batch=1)  # ,device='cpu'
    model.val()  


if __name__ == '__main__':
    main()
