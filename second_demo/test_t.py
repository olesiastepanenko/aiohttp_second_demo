import itertools
from datetime import datetime
import time
#
start_time = datetime.now()
input_arr = []
l = 4
# 0:00:22.700248 (99990000) - 10 000 permutations
# 0:00:12.698168 (49995000) - 10 000 combinations
# 0:00:14.978342 (49995000) - 10 000combinations(reversed)
n = 2
N = 4
res = []
# step = l//n
for x in range(l):
    input_arr.append(x)

# res = list(itertools.permutations(input_arr, 2))
# res = list(itertools.combinations(input_arr, 2))
# print(datetime.now() - start_time)

# start_time = datetime.now()
# res1 = list(itertools.combinations(reversed(input_arr), 2))
# print(datetime.now() - start_time)
# print("res", len(res))

# print("res1", len(res))
# print(input_arr)
# start_time = datetime.now()

# tempEl = -1
# tempSecEl = -1
# i=-1
# первое ядро первый проход
# for el in input_arr[:step]:
#     for secEl in input_arr[step:step*2]:
#         res.append((el, secEl))
#         res.append((secEl, el))
#         print(len(res))
#     tempEl = el
# for elem in input_arr[:step]:
#     for i in input_arr[:step]:
#         if elem!=i:
#             res.append((i, elem))
# # print("res", len(res))
#
# for e in input_arr[step:step*2]:
#     for j in input_arr[step:step * 2]:
#         if e!=j:
#             res.append((j, e))

# print(datetime.now() - start_time)
# print("res", len(res))

# делим арр на 2 части
# первая перемешивает 1 половину
# start_time = datetime.now()
# a1 = list(itertools.product(input_arr[:step], repeat=2))
# res = res + a1
# print(datetime.now() - start_time)
#
# start_time = datetime.now()
# # вторая перемешивает 2 половину
# a2 = list(itertools.product(input_arr[step:step * 2], repeat=2))
# res = res + a2
# print(datetime.now() - start_time)
#
# start_time = datetime.now()
# # третья перемешивает половины между собой
# a3 = list(itertools.product(input_arr[:step], input_arr[step:step * 2]))
# res = res + a3
# print(datetime.now() - start_time)
#
# start_time = datetime.now()
# # четвертая перемешивает половины между собой в обратном порядке
# r1 = list(reversed(input_arr[:step]))
# r2 = list(reversed(input_arr[step:2*step]))
# a4 = list(itertools.product(r2, r1))
# res = res + a4
# print(datetime.now() - start_time)
# #
# print(res, len(res))
res = list(itertools.product(input_arr, repeat=2))
print(len(res))

step = len(res)//N
newRes = []
for i in range(0, N):
    if i+1 == N:
        newRes.append(res[i*step:])
        print(res[i*step:])
    else:
        newRes.append(res[i*step:i*step + step])
        print(res[i*step:i*step + step])
print(newRes)

# newRes = to_lists(res, N)
# print(newRes)

