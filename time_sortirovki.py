import git_5_cortirovok as gs
import time
from random import randint as ran

a = [10, 100, 1000, 10000, 10**7]
mas = []
for n in a:
    mas.append([ran(0, 100) for i in range(n)])
start = time.time()
#gs.bubble_sort(mas[4])
#gs.select_sort(mas[4])
#gs.insertion_sort(mas[4])
#gs.quick_sort(mas[4], 0, len(mas[4])-1)
gs.gnom_sort(mas[0])
end = time.time()
tim = end - start
print(tim)
