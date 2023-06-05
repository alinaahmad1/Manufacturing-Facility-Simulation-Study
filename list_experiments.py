#just a file to test stuff, not important code.

listy = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
listy_2 = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]

dick = {
    'list1': listy,
    'list2': listy_2
    }

print(dick)

for key in dick:
    for i in range(int(len(dick[key])*0.1)):
        temp_list = dick[key]
        del(temp_list[0])
    dick[key] = temp_list

print(dick)