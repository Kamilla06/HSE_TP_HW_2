def _min(array):
    min_val = array[0]
    for i in range(1, len(array)):
        if array[i] < min_val:
            min_val = array[i]
    return min_val

def _max(array):
    max_val = array[0]
    for i in range(1, len(array)):
        if array[i] > max_val:
            max_val = array[i]
    return max_val

def _sum(array):
    Sum = array[0]
    for i in range(1, len(array)):
        Sum += array[i]
    return Sum

def _mult(array):
    mult = array[0]
    for i in range(1, len(array)):
        mult *= array[i]
    return mult

def main(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        s = file.readline()
        correct_string = '1234567890- '
        for char in s:
            if correct_string.find(char) == -1:
                return f'ERROR\nFile is incoect'
        array = list(map(int, s.split()))
    return f'Минимальное число: {_min(array)}\nМаксимальное число: {_max(array)}\nРезультат сложения: {_sum(array)}\nРеультат умножения: {_mult(array)}'


if __name__ == '__main__':
    print(main(input('Введите название файла с числами: ')))

