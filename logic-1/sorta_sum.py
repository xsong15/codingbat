def sorta_sum(a, b):
    """
    Given 2 ints, a and b, return their sum. However, 
    sums in the range 10..19 inclusive, are forbidden, 
    so in that case just return 20.
    """
    if 10 <= a+b <= 19:
        return 20
    else:
        return a+b

    # abSum = a + b
    # return 20 if abSum in range(10, 20) else abSum

print(sorta_sum(3, 4)) #→ 7
print(sorta_sum(9, 4)) #→ 20
print(sorta_sum(10, 11)) #→ 21