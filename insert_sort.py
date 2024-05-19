def insort(input_ar):
    for x in range(1, len(input_ar)):
        current = input_ar[x]
        i = x - 1
        while i >= 0 and current < input_ar[i]:
            input_ar[i + 1] = input_ar[i]
            i -= 1
        input_ar[i + 1] = current
    return input_ar
        
example_ar = [45, 1, 23, 698, 74, 125, 632, 547, 256]
print("Sorting array: ", example_ar)
print("Sorted  array: ", insort(example_ar))