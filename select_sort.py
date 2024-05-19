def sesort(input_ar):
    if len(input_ar) <= 1:
        return input_ar
    for x in range(len(input_ar)-1, 0, -1):
        current = x
        for i in range(0, x):
            if input_ar[i] > input_ar[current]:
                current = i
        input_ar[x], input_ar[current] = input_ar[current], input_ar[x]
    return input_ar
    
example_ar = [45, 1, 23, 698, 74, 125, 632, 547, 256]
print("Sorting array: ", example_ar)
print("Sorted  array: ", sesort(example_ar))