import random

def demo():
    for i in range(10):
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        d = d1 + d2
        print(f"{i+1}: {d1} + {d2} = {d}")


demo()