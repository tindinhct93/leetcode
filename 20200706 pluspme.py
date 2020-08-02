def plusOne(digits):
    n = len(digits)
    i = n - 1
    digits[n - 1] += 1
    while digits[i] == 10 and i > 0:
        digits[i] = 0
        digits[i - 1] += 1
        i -= 1
    if digits[0] == 10:
        digits = [0] * n
        digits.insert(0, 1)
    return digits

print(plusOne([4,3,2,1]))
print(plusOne([8,9,9,9]))