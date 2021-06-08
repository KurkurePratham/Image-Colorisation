n = int(input("NO. of values:"))
values = []
for i in range(n):
    ele = int(input("Enter " + str(i+1) + "th value:"))
    values.append(ele)
smallest = min(values)
largest = max(values)
acc_sort = [0] * (largest - smallest + 1)
repetition = [0] * (largest - smallest + 1)
for i in range(n):
    acc_sort[values[i] - smallest] = values[i]
    repetition[values[i] - smallest] += 1
for i in range(largest - smallest + 1):
    for j in range(repetition[i]):
        print(acc_sort[i], end =" ")
