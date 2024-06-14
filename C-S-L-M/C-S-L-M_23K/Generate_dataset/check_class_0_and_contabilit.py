import os

# Caminho para os arquivos de rótulo
label_path = 'train'

# Função para verificar e contar arquivos que contêm a classe 0
def count_files_with_class_zero(label_path):
    count = 0
    total_files = 0

    for label_file in os.listdir(label_path):
        if label_file.endswith('.txt'):
            label_file_path = os.path.join(label_path, label_file)
            total_files += 1

            with open(label_file_path, 'r') as file:
                lines = file.readlines()

            contains_class_zero = any(line.strip().split()[0] == '0' for line in lines if len(line.strip().split()) == 5)

            if contains_class_zero:
                count += 1
        
    return count, total_files

# Chamar a função para verificar e contar arquivos que contêm a classe 0
count, total_files = count_files_with_class_zero(label_path)
print(f'Total de arquivos: {total_files}')
print(f'Total de arquivos que contêm a classe 0: {count}')
