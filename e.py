"""Asking user how many decimal places he want in e and calculate up to that precision."""

"""so here let us take 3 variables"""
total = 1
j = 1
i = 1

"""Take user's input"""
n = int(input("Enter decimal places: "))

previous = round(total,n)
while True:
    j *= i
    total += 1/j
    i += 1
    current =round(total,n)

    if current == previous:
        break

    previous = current


print(round(total, n))

