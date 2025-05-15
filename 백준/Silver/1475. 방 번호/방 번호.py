import math

room_number = input().strip()

digit_count = [0] * 10 

for digit in room_number:
    digit_count[int(digit)] += 1

six_nine_count = digit_count[6] + digit_count[9]
digit_count[6] = digit_count[9] = math.ceil(six_nine_count / 2)

min_sets = max(digit_count)

print(min_sets)
