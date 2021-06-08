import random


streaks = 0
for i in range(100000):
    global new, old
    for j in range(6):
        new = random.randint(0, 1)
        if j != 0 and new != old:
            break
        old = new
    if old == new:
        streaks += 1
print(streaks/1000)
print(100/(2)**5)