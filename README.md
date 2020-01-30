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

## Tuples

### Exercise 7

Given three variables, a, b and c, swap them without using temporary variables.

Sample input:
```python
# a = 5, b = 3, c = 2
(5, 3, 2)
('Hi', 'Ola', 'xD')
```

Sample output:
```python
# a = 2, b = 5, c = 3
(2, 5, 3)
('xD', 'Hi', 'Ola')
```

### Exercise 8

Create a function that returns both minimum and maximum value of given list.

Sample input:
```python
exercise_8([10, 2, 5, -3, -1])
exercise_8([5, 2, 8, 4])
```

Sample output:
```python
(-1, 10)
(2, 8)
```

### Exercise 9

Create a function that returns True, if given tuple contains mutable element.

Sample input:
```python
exercise_9((10, 2, 5, [4, 8, 2], 3, 5))
exercise_9((5, 2.5, 8, 4, 'Hi', -5, True, 6))
```

Sample output:
```python
#Element at index 3 is list that can be changed
True
#All elements of given tuple are immutable objects
False
```

## Sets

### Exercise 10

Create a function that returns set with neighbor numbers of given set.

Sample input:
```python
exercise_10({1, 5, 9})
exercise_10({2, 5, 7, 8, 10})
```

Sample output:
```
{0, 2, 4, 6, 8, 10}
{1, 3, 4, 6, 7, 8, 9, 11}
```

### Exercise 11

Create a function that returns difference of given 2 sets.
(The difference of sets A,B consists of elements that are in A but not in B).
  
Sample input:
```python
#A = {1, 2, 3, 4}, B = {3, 5, 7}
exercise_11({1, 2, 3, 4}, {3, 5, 7})
exercise_11({12, 15, 16, 20, 95}, {1, 2, 3, 16, 17, 20})
```

Sample output:
```
{1, 2, 4}
{12, 15, 95}
```

### Exercise 12

Create a function that returns a set with values from given list, if some number already exists in the set, take it to the power of two, three ... while it's in the set.

Sample input:
```python
exercise_12([1, 2, 2])
exercise_12([1, 2, 2, 3, 4])
```

Sample output:
```
{1, 2, 4}
{1, 2, 3, 4, 16}
```

### Exercise 13

Create a function that returns Yes, if there can be formed palindrome text using given list of number, or No, if there is no way to make a palindrome. 

Sample input:
```python
exercise_13([1,2,3,4,1])
exercise_13([1,2,3,1,2])
```

Sample Output:
```
No
Yes
```

### Exercise 14

Create a function that returns list of numbers from the given list, that are more than given number N;

Sample input:
```python
exercise_14([11,2,44,23], 10)
exercise_14([1,200,45,-67], 45)
```

Sample Output:
```
{11,44,23}
{200}
```

### Exercise 15

Create a function that returns number of odd numbers that are on even positions;

Sample input:
```python
exercise_15([0,3,11,2,44,23,4])
exercise_15([22,23,24,33,34,35])
```

Sample Output:
```
2
3
```
