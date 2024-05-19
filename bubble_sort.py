def busort(input_ar):
    if len(input_ar) <= 1:
        return input_ar
    shift = False
    for x in range(0, len(input_ar)-1):
        if input_ar[x] > input_ar[x+1]:
            shift = True
            input_ar[x], input_ar[x+1] = input_ar[x+1], input_ar[x]
    if shift == True:
        busort(input_ar) 
    return input_ar
        
example_ar = [45, 1, 23, 698, 74, 125, 632, 547, 256]
print("Sorting array: ", example_ar)
print("Sorted  array: ", busort(example_ar))