# Programming Principles II

## Lab 1

Problems from Informatics python [course](https://informatics.mccme.ru/course/view.php?id=156):

1. Типы данных: все задачи
2. Целочисленная арифметика: 5 задач
3. Условная инструкция: 5 задач
4. Цикл for: 5 задач
5. Действительные (вещественные) числа: 5 задач
6. Строки: 5 задач
7. Цикл while: 5 задач
8. Функция, рекурсия: 5 задач

## Lab 2

### Exercise 1

Create a function that returns element at index `i` in input list. 

Sample input:
```python
# index = 3
exercise_1([10, 3, 4, 5, 9], 3)
exercise_1([10, 3, 4, 5, 9], 4)
```

Sample output:
```python
5
9
```

### Exercise 2

Create a function that collects only values with even index from a given list

Sample input:
```python
exercise_2([10, 3, 4, 5, 9])
exercise_2([9, 0, 12, 3, 4, 56, 9, 16])
```

Sample output:
```python
[10, 4, 9]
[9, 12, 4, 9]
```

### Exercise 3

Create a function that mutates elements to square after given index. Elements *before* given index do not change.

Sample input:
```python
# index = 4, all numbers after index 4 should change to their squares
# [..., 4, 5, 9] -> [..., 4 * 4, 5 * 5, 9 * 9]
exercise_3([10, 3, 4, 5, 9], 2)
exercise_3([9, 0, 12, 3, 4, 56, 9, 16], 6)
```

Sample output:
```python
[10, 3, 16, 25, 81]
[9, 0, 12, 3, 4, 56, 81, 256]
```

### Exercise 4

Create a function that reverses a given list.

Sample input:
```python
exercise_4([10, 3, 4, 5, 9])
exercise_4([9, 0, 12, 3, 4, 56, 9, 16])
```

Sample output:
```python
[9, 5, 4, 3, 10]
[16, 9, 56, 4, 3, 12, 0, 9]
```

### Exercise 5

Create a function that deletes elements after given index.

Sample input:
```python
#index = 2
exercise_5([10, 3, 4, 5, 9], 1)
exercise_5([9, 0, 12, 3, 4, 56, 9, 16], 7)
```

Sample output:
```python
[10]
[9, 0, 12, 3, 4, 56, 9]
```

### Exercise 6

Create a function that inserts elements at given index and then deletes elements after given index.

Sample input:
```python
#index insert = 2, index delete from = 4, elements to insert = [1, 2, 3]
exercise_6([10, 3, 4, 5, 9], 3, 4, [1, 2, 3])
exercise_6([9, 0, 12, 3, 4, 56, 9, 16], 7)
```

Sample output:
```python
# [1, 2, 3] are inserted in position 2 -> [10, 1, 2, 3, 3, 4, 5, 9]
# elements at index 4 are deleted -> [10, 1, 2, 3]
[10]
[9, 0, 12, 3, 4, 56, 9]
```