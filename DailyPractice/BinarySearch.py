def search(number, des):
    low = 0
    upper = len(number) - 1
    while low <= upper:
        mid = (low + upper) / 2
        if number[mid] < des:
            low = mid + 1
        elif number[mid] > des:
            upper = mid - 1
        else:
            return mid
    return -1

number = [1, 4, 2, 6, 7, 3, 9, 8]
number.sort()
find = search(number, 2)
print("Find index is " + str(find) if find >= 0 else "GG")
