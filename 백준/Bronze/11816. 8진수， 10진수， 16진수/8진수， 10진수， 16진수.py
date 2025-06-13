import sys

targetNum = sys.stdin.readline().strip()

def hex_to_int(hex_str):
    hex_digits = hex_str[2:]
    total = 0
    power = 0
    for digit in reversed(hex_digits):
        total += int(digit, 16) * (16 ** power)
        power += 1
    print(total)

def oct_to_int(oct_str):
    oct_digits = oct_str[1:]
    total = 0
    power = 0
    for digit in reversed(oct_digits):
        total += int(digit, 8) * (8 ** power)
        power += 1
    print(total)


if len(targetNum) > 1 and targetNum.startswith('0x'):
    hex_to_int(targetNum)
elif len(targetNum) > 1 and targetNum.startswith('0'):
    oct_to_int(targetNum)
else:
    print(int(targetNum))