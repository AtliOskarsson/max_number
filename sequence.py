n = int(input("Enter the length of the sequence: ")) # Do not change this line

first = 1
second = 0
third = 0
sequence = 0
for i in range(n):
    sequence = first + second + third
    third = second
    second = first
    first = sequence
    if sequence == 2:
        third = 0
    print(sequence, end=", ")


