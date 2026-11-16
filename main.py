"""Calculating Approximation of Pi using Leibniz formula."""

total = 0
i = 0
term = int(input("Enter the number of terms to approximate Pi: "))

while i < term:
    j = 2*i + 1
    i += 1

    if i % 2 == 0:
     total += 1/j
    else:
     total -= 1/j

    
PI = total*4
print("The PI: ", PI )

