def demo():
    print("Start")
    yield 1
    print("Middle")
    yield 2
    print("End")

gen1=demo()    
print(next(gen1))  # Output: Start \n 1
print(next(gen1))  # Output: Middle \n 2