"""Asking user how many decimal places he want in e and calculate up to that precision."""

"""so here let us take 3 variables"""
total = 1
j = 1
i = 1

"""Take user's input"""
n = int(input("Enter decimal places: "))

while i <= n:
    j *= i
    total += 1/j
    i += 1

total = round(n)

print("The e: ", total)
    