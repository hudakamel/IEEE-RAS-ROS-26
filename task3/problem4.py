import random
def get_unique_lottery():
    num=set()
    for i in range(6):
        x=random.randint(1,51)
        num.add(x)
    
    print(num)
get_unique_lottery()