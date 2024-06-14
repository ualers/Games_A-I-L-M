import os

# Caminho para os arquivos de rótulo
label_path = 'images'

# Função para converter classes e excluir arquivos vazios com suas imagens correspondentes
def convert_classes_and_remove_empty_files(label_path):
    for label_file in os.listdir(label_path):
        if label_file.endswith('.txt'):
            label_file_path = os.path.join(label_path, label_file)
            image_file_path = os.path.splitext(label_file_path)[0] + '.jpg'  # Supondo que as imagens são .jpg

            with open(label_file_path, 'r') as file:
                lines = file.readlines()

            if not lines:  # Se o arquivo está vazio, remove o arquivo de rótulo e a imagem correspondente
                os.remove(label_file_path)
                if os.path.exists(image_file_path):
                    os.remove(image_file_path)
            else:  # Caso contrário, converte as classes para 0
                converted_lines = []
                for line in lines:
                    parts = line.strip().split()
                    if len(parts) == 5:
                        parts[0] = '0'
                        converted_lines.append(' '.join(parts) + '\n')

                with open(label_file_path, 'w') as file:
                    file.writelines(converted_lines)

# Chamar a função para alterar classes e remover arquivos vazios
convert_classes_and_remove_empty_files(label_path)
