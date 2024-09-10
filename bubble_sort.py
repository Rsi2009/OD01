mas = [8, 7, 4, 3, 8, 3, 5, 6, 1, 2]
n = 10
for run in range(n-1):
   for i in range(n-1-run):
       if mas[i] > mas[i + 1]:
           mas[i], mas[i + 1] = mas[i + 1], mas[i]
print(mas)
