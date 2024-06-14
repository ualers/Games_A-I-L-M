import os

# Caminho para os arquivos de rótulo
label_path = 'images'

# Função para alterar classes nos rótulos
def convert_classes_to_zero(label_path):
    for label_file in os.listdir(label_path):
        if label_file.endswith('.txt'):
            label_file_path = os.path.join(label_path, label_file)

            with open(label_file_path, 'r') as file:
                lines = file.readlines()

            converted_lines = []
            for line in lines:
                parts = line.strip().split()
                if len(parts) == 5:
                    parts[0] = '0'
                    converted_lines.append(' '.join(parts) + '\n')

            with open(label_file_path, 'w') as file:
                file.writelines(converted_lines)

# Chamar a função para alterar classes nos rótulos
convert_classes_to_zero(label_path)
