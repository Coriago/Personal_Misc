import sys
import random


nums = []

def is_duplicate(l, r):
    for n in l:
        if r == n:
            return True
    return False

for n in range(24):
    randNum = random.randint(1, 300)
    if is_duplicate(nums, randNum) == True:
        n -= 1
    else:
        nums.append(randNum)
print nums
