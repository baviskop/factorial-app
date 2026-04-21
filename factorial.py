# def cal_factorial(k):
#     if k == 0:
#         return 1
#     factorial = 0
#     for i in range(1, k+1):
#         factorial *= i
#     return factorial

def fact(k):
    if k == 0 or k == 1:
        return 1
    else:
        return k * fact(k-1)