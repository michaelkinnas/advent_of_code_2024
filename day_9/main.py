data = open('day_9/data.txt', 'r').read()
data = [int(x) for x in data]

disk_image = []
for i, value in enumerate(data):
    if i % 2 == 0:
        for j in range(value):
            disk_image.append(i // 2)
    else:
        for j in range(value):
            disk_image.append('.')


left_cursor = 0
right_cursor = len(disk_image)-1
while left_cursor < right_cursor:
    if disk_image[left_cursor] == '.':
        while right_cursor > left_cursor:
            if disk_image[right_cursor] == '.':
                right_cursor -= 1
            else:
                disk_image[left_cursor] = disk_image[right_cursor]
                disk_image[right_cursor] = '.'
                break
    left_cursor += 1

checksum = 0
for i in range(len(disk_image)):
    if disk_image[i] == '.': break
    checksum += i * disk_image[i]

print("Part 1: ", checksum)




#rebuild disk image for part 2
disk_image = []
for i, value in enumerate(data):
    if i % 2 == 0:
        for j in range(value):
            disk_image.append(i // 2)
    else:
        for j in range(value):
            disk_image.append('.')

lp = 0
rp = len(disk_image) - 1
while rp > 0:
    if rp == '.':
        rp -= 1
    else:
        fsize = 1
        file_id = disk_image[rp]
        rm = rp
        while file_id == disk_image[rm]:
            rm -= 1
        fsize = rp - rm

        while True:
            while disk_image[lp] != '.':
                lp += 1            
            lm = lp
            
            while lm < len(disk_image) and  disk_image[lm] == '.':
                lm += 1
            empty_space = lm - lp
            
            #if left pointer reaches the right measure pointer go to next number
            if lp >= rm: 
                lp = 0
                rp = rm
                break
           
            #check if empty space is enought else continue searching
            if empty_space >= fsize:
                for k in range(fsize):
                    disk_image[lp+k] = disk_image[rp-k]
                    disk_image[rp-k] = '.'
                rp = rm
                lp = 0
                break
            else:
                lp = lm # continue searching for empty space       

checksum = 0
for i in range(len(disk_image)):
    if disk_image[i] == '.': continue
    checksum += i * disk_image[i]

print("Part 2: ", checksum)