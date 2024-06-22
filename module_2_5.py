def get_matrix(n, m, value):                # Объявляем функцию get_matrix и записываем в ней параметры n, m , value
    matrix = []                             # Создаём пустой список matrix внутри функции get_matrix
    for i in range(n):                      # Первый(внешний) цикл for для кол-ва строк матрицы, n повторов
        matrix.append([])                   # В первом цикле добавляем пустой список в список matrix
        for j in range(m):                  # Второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов
            matrix[i].append(value)         # Во втором цикле пополняем ранее добавленный пустой список значениями value
    return (matrix)                         # После всех циклов возвращаем значение переменной matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)                              # Выведите на экран(консоль) результат работы функции get_matix
print(result2)                              # Выведите на экран(консоль) результат работы функции get_matix
print(result3)                              # Выведите на экран(консоль) результат работы функции get_matix
