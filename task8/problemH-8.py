
t_str = input()
if t_str:
    t = int(t_str)
    
    for _ in range(t):
       
        n = int(input())
        a = list(map(int, input().split()))
        result = max(a) - min(a)
        print(result)