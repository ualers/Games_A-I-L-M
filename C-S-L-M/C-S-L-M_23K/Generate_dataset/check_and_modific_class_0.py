import os

# Caminho para os arquivos de rótulo
label_path = 'train'

# Função para converter classes para 0 e contar arquivos modificados
def convert_classes_and_count_modifications(label_path):
    modified_count = 0
    total_files = 0

    for label_file in os.listdir(label_path):
        if label_file.endswith('.txt'):
            label_file_path = os.path.join(label_path, label_file)
            total_files += 1

            with open(label_file_path, 'r') as file:
                lines = file.readlines()

            converted_lines = []
            modified = False
            for line in lines:
                parts = line.strip().split()
                if len(parts) == 5:
                    if parts[0] != '0':
                        parts[0] = '0'
                        modified = True
                    converted_lines.append(' '.join(parts) + '\n')

            if modified:
                with open(label_file_path, 'w') as file:
                    file.writelines(converted_lines)
                modified_count += 1

    return modified_count, total_files

# Chamar a função para converter classes e contar modificações
modified_count, total_files = convert_classes_and_count_modifications(label_path)
print(f'Total de arquivos: {total_files}')
print(f'Total de arquivos modificados: {modified_count}')
