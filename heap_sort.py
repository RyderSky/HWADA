def hesort(input_ar):
    n = len(input_ar)
    for x in range(n // 2 - 1, -1, -1):
        heap(input_ar, n, x)
    for x in range(n - 1, 0, -1):
        input_ar[x], input_ar[0] = input_ar[0], input_ar[x]
        heap(input_ar, x, 0)
    return input_ar

def heap(input_ar, n, x):
    current = x
    left = 2 * x + 1
    right = 2 * x + 2
    if left < n and input_ar[left] > input_ar[current]:
        current = left
    if right < n and input_ar[right] > input_ar[current]:
        current = right
    if current != x:
        input_ar[x], input_ar[current] = input_ar[current], input_ar[x]
        heap(input_ar, n, current)
        
example_ar = [45, 1, 23, 698, 74, 125, 632, 547, 256]
print("Sorting array: ", example_ar)
print("Sorted  array: ", hesort(example_ar))