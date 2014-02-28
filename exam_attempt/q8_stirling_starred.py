# Question 8*: Числа Белла и Стирлинга

# Количество способов разбиения n элементов в k не пустых множеств называется
# числом Стирлинга S(n, k) второго рода 
# (http://ru.wikipedia.org/wiki/Числа_Стирлинга_второго_рода). Например, группа людей
# Dave, Sarah, Peter и Andy могут быть разбиты на две группы следующими способами:


# 1.   Dave, Sarah, Peter         Andy
# 2.   Dave, Sarah, Andy          Peter
# 3.   Dave, Andy, Peter          Sarah
# 4.   Sarah, Andy, Peter         Dave
# 5.   Dave, Sarah                Andy, Peter
# 6.   Dave, Andy                 Sarah, Peter
# 7.   Dave, Peter                Andy, Sarah

# поэтому S(4,2) = 7

# Если вместо разбиения на 2 группы мы будем разбивать их на одну группу, то у нас 
# есть только один способ сделать это:

# 1. Dave, Sarah, Peter, Andy

# поэтому S(4,1) = 1

# ..или на 4 группы - тоже только 1 способ:

# 1. Dave        Sarah          Peter         Andy

# поэтому S(4,4) = 1

# На большее количество непустых групп, чем 4, разбить 4х человек нельзя

# Формула для вычисления чисел Стирлинга:

#  S(n, k) = k*S(n-1, k) + S(n-1, k-1)

# Далее, число Белла - это количество всех неупорядоченных разбиений n элементного 
# множества. (http://ru.wikipedia.org/wiki/Числа_Белла)
# То есть, B(n) это сумма S(n,k) для k=1,2,....,n

# Реализуйте две процедуры, stirling и bell. stirling принимает на вход два натуральных
# числа, первое - количество элементов, второе - количество множеств, на которые разбиваются
# элементы. (n и k в формуле числа Стирлинга, соответственно). Процедура возвращает 
# число Стирлинга.
# Процедура bell принимает натуральное число n, и возвращает число Белла B(n).



            


print stirling(1,1)
#>>> 1
print stirling(2,1)
#>>> 1
print stirling(2,2)
#>>> 1
print stirling(2,3)
#>>>0

print stirling(3,1)
#>>> 1
print stirling(3,2)
#>>> 3
print stirling(3,3)
#>>> 1

print stirling(4,1)
#>>> 1
print stirling(4,2)
#>>> 7
print stirling(4,3)
#>>> 6
print stirling(4,4)
#>>> 1

print stirling(5,1)
#>>> 1
print stirling(5,2)
#>>> 15
print stirling(5,3)
#>>> 25
print stirling(5,4)
#>>> 10
print stirling(5,5)
#>>> 1

print stirling(20,15)
#>>> 452329200

print bell(1)
#>>> 1
print bell(2)
#>>> 2
print bell(3)
#>>> 5
print bell(4)
#>>> 15
print bell(5)
#>>> 52
print bell(15)
#>>> 1382958545
