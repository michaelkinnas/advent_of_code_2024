series = [572556, 22, 0, 528, 4679021, 1, 10725, 2790]
# series = [125, 17]


for k in range(25):
    # if k % 5 == 0: print(k) 
    i = 0
    while i < len(series):
        if series[i] == 0:
            series[i] = 1
            i += 1
        elif len(str(series[i])) % 2 == 0:
            stri = str(series[i])
            split_point = len(stri) // 2
            lh = stri[:split_point]
            rh = stri[split_point:]
            series[i] = int(lh)
            series.insert(i+1, int(rh))
            i += 2
        else:
            series[i] *= 2024
            i += 1

print(len(series))

# using strings (slower)
# for k in range(75):
#     if k % 5 == 0: print(k)   
#     i = 0
#     # print(series)
#     while i < len(series):
#         if series[i] == '0':
#             series[i] = '1'
#             i += 1
#         elif len(series[i]) % 2 == 0:
#             split_point = len(series[i]) // 2
#             # print(split_point)
#             lh = series[i][:split_point]
#             rh = series[i][split_point:]
#             series[i] = lh
#             series.insert(i+1, str(int(rh)))
#             i += 2
#         else:
#             new = int(series[i]) * 2024
#             series[i] = str(new)
#             i += 1