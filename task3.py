import os

def merge_files():
    folder_path = '/Users/golubcikovkirill/Desktop/Projects/for Netology VSC/Open file Python/files'  # Путь к папке с файлами
    files = os.listdir(folder_path)  # Получаем список всех файлов в папке
    file_data = []

    # Чтение файлов и сбор данных
    for filename in files:
        file_path = os.path.join(folder_path, filename)  # Полный путь к файлу
        if os.path.isfile(file_path):  # Проверяем, что это файл
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                file_data.append((filename, len(lines), lines))  # Сохраняем имя файла, количество строк и содержимое

    # Сортировка файлов по количеству строк
    file_data.sort(key=lambda x: x[1])

    # Запись в итоговый файл
    with open('/Users/golubcikovkirill/Desktop/Projects/for Netology VSC/Open file Python/merged_file.txt', 'w', encoding='utf-8') as result_file:
        for filename, line_count, lines in file_data:
            result_file.write(f'{filename}\n')  # Записываем имя файла
            result_file.write(f'{line_count}\n')  # Записываем количество строк
            result_file.writelines(lines)  # Записываем содержимое файла

# Вызов функции для объединения файлов
if __name__ == "__main__":
    merge_files()




