def make_abba(a, b):
    """
    Given two strings, a and b, return the result of 
    putting them together in the order abba, e.g. "Hi" 
    and "Bye" returns "HiByeByeHi".
    """
    return a + b * 2 + a

print(make_abba("Hi", "Bye"))

# print(str(a, b, b, a))