# list = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
#
# print(list)
#
# length = len(list)
#
# for i in range(length):
#     for j in range(length):
#         print(list[i][j])

a = int(input('Enter column length: '))
c = int(input('Enter row length: '))


listin = []

for i in range(a):
    b = []
    for j in range(c):

        b.append(int(input()))
        listin.append(b)

print(listin)

for i in range(a):
    for j in range(c):
        print(listin[i][j])
    print()