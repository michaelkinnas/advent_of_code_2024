stones = [572556, 22, 0, 528, 4679021, 1, 10725, 2790]
cache = {}

def blink(stone, iteration, cache):
    if (stone, iteration) in cache: return cache[(stone, iteration)]
    if iteration == 0:
        cache[(stone, iteration)] = 1
        return 1
    if stone == 0:
        result = blink(1, iteration - 1, cache)
        cache[(stone, iteration)] = result
        return result
    stri = str(stone)
    if len(stri) % 2 == 0:
        split_point = len(stri) // 2
        lh = stri[:split_point]
        rh = stri[split_point:]
        result = blink(int(lh), iteration - 1, cache) + blink(int(rh), iteration - 1, cache)
        cache[(stone, iteration)] = result
        return result
    result = blink(2024 * stone, iteration - 1, cache)
    cache[(stone, iteration)] = result
    return result


print(f"Part 1: {sum([blink(x, 25, cache) for x in stones])}")
print(cache)
# print(f"Part 2: {sum([blink(x, 75, cache) for x in stones])}")