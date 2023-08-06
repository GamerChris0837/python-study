# 2단 구구단 만들기
a=2

for b in range(1,10):   # 1 ~ 9
    print("%d * %d = %d"% (a,b,a*b))

# 전체 구구단 표 만들기
print("-"*30)

for a in range(2,10):
    for b in range(1,10):
        print("%d * %d = %d"% (a,b,a*b))

    print("-"*30)