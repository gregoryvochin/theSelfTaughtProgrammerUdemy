def findSolo(my_list):
    soloSoFar = []
    for i in my_list:
        if my_list.count(i) == 1:
            soloSoFar.append(i)

    return soloSoFar

my_list = [11, 11, 2, 2, 3, 3, 4, 4, 77, 77, 22, 22, 100, 420, 69]

print(findSolo(my_list))
