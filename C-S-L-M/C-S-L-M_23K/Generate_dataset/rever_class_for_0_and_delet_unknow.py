import os

# Caminho para os arquivos de rótulo
label_path = 'images'

# Função para converter classes, remover linhas com classe 1 e excluir arquivos vazios com suas imagens correspondentes
def convert_classes_and_clean_files(label_path):
    for label_file in os.listdir(label_path):
        if label_file.endswith('.txt'):
            label_file_path = os.path.join(label_path, label_file)
            image_file_path = os.path.splitext(label_file_path)[0] + '.jpg'  # Supondo que as imagens são .jpg

            with open(label_file_path, 'r') as file:
                lines = file.readlines()

            # Remover linhas com classe 1
            cleaned_lines = []
            for line in lines:
                parts = line.strip().split()
                if len(parts) == 5 and parts[0] != '1':
                    parts[0] = '0'  # Converter todas as classes restantes para 0
                    cleaned_lines.append(' '.join(parts) + '\n')

            # Se o arquivo estiver vazio após a limpeza, remover arquivo de rótulo e imagem correspondente
            if not cleaned_lines:
                os.remove(label_file_path)
                if os.path.exists(image_file_path):
                    os.remove(image_file_path)
            else:
                with open(label_file_path, 'w') as file:
                    file.writelines(cleaned_lines)

# Chamar a função para alterar classes, remover linhas e excluir arquivos vazios
convert_classes_and_clean_files(label_path)
