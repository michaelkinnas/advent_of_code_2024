file = open('./day_1/data', 'r')
lists = file.read().replace("\n", "   ").split("   ")

column_1 = []
column_2 = []
for i, num in enumerate(lists):
    if i % 2 == 0:
        column_1.append(int(num))
    else:
        column_2.append(int(num))

column_1.sort()
column_2.sort()
differences = [abs(num1 - num2) for num1, num2 in zip(column_1, column_2)]
print(sum(differences))

similarities = []
for num1 in column_1:
    similarities.append(column_2.count(num1) * num1)

print(sum(similarities))


    

