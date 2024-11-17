import csv, json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    ...  # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, 'r') as file:
        reader = csv.reader(file)
        result, i = [], 0
        for row in reader:
            if i == 0:
                zagolovok = [i for i in row]
            else:
                result.append({zagolovok[i] :row[i] for i in range(len(row))})
            i += 1
    with open(OUTPUT_FILENAME,'w') as file:
        json.dump(result, file, indent=4)
    ...  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    task()