def qsort(input_ar):
    if len(input_ar) <= 1:
        return input_ar
    else:
        pivot = input_ar[len(input_ar) // 2]
        left = []
        middle = []
        right = []
        for x in input_ar:
            if x < pivot:
                left.append(x)
            elif x == pivot:
                middle.append(x)
            else:
                right.append(x)
        return qsort(left) + middle + qsort(right)

example_ar = [45, 1, 23, 698, 74, 125, 632, 547, 256]
print("Sorting array: ", example_ar)
print("Sorted  array: ", qsort(example_ar))