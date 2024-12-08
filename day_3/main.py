data = open('day_3/data', 'r').read()

valid_digits = [str(x) for x in range(10)]

result = 0
for i, char in enumerate(data):
    if data[i:i+4] == "mul(":
        if data[i+4] in valid_digits and data[i+5] == ',':
            first_num = int(data[i+4])
            cursor = 6
        elif data[i+4] in valid_digits and data[i+5] in valid_digits and data[i+6] == ',':
            first_num = int(data[i+4:i+6])
            cursor = 7
        elif data[i+4] in valid_digits and data[i+5] in valid_digits and data[i+6] in valid_digits and data[i+7] == ',':
            first_num = int(data[i+4:i+7])
            cursor = 8
        else:
            continue

        if data[i + cursor] in valid_digits and data[i+cursor+1] == ')':
            second_num = int(data[i + cursor])
        elif data[i + cursor] in valid_digits and data[i+cursor+1] in valid_digits and data[i+cursor+2] == ')':
            second_num = int(data[i + cursor:i+cursor+2])
        elif data[i + cursor] in valid_digits and data[i+cursor+1] in valid_digits and data[i+cursor+2] in valid_digits and data[i+cursor+3] == ')':
            second_num = int(data[i + cursor:i+cursor+3])
        else: 
            continue
        
        result += first_num * second_num        

print("Part 1: ", result)

#part 2

result2 = 0
enabled = True
for i, char in enumerate(data):
    # print(data[i:i+7])
    if data[i:i+7] == "don't()":
        
        enabled = False
    
    if data[i:i+4] == "do()":
        enabled = True

    if data[i:i+4] == "mul(" and enabled:
        if data[i+4] in valid_digits and data[i+5] == ',':
            first_num = int(data[i+4])
            cursor = 6
        elif data[i+4] in valid_digits and data[i+5] in valid_digits and data[i+6] == ',':
            first_num = int(data[i+4:i+6])
            cursor = 7
        elif data[i+4] in valid_digits and data[i+5] in valid_digits and data[i+6] in valid_digits and data[i+7] == ',':
            first_num = int(data[i+4:i+7])
            cursor = 8
        else:
            continue

        if data[i + cursor] in valid_digits and data[i+cursor+1] == ')':
            second_num = int(data[i + cursor])
        elif data[i + cursor] in valid_digits and data[i+cursor+1] in valid_digits and data[i+cursor+2] == ')':
            second_num = int(data[i + cursor:i+cursor+2])
        elif data[i + cursor] in valid_digits and data[i+cursor+1] in valid_digits and data[i+cursor+2] in valid_digits and data[i+cursor+3] == ')':
            second_num = int(data[i + cursor:i+cursor+3])
        else: 
            continue
        
        result2 += first_num * second_num

print("Part 2: ", result2)