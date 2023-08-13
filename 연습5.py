# 길이 환산표
print("-"*30)
print("  cm   mm    m     inch")
print("-"*30)

for cm in range(1,101):
    mm=cm*10
    m=cm*0.01
    inch=cm*1/2.54
    print("%3d  %.2f  %.2f  %.4f"% (cm,mm,m,inch))

print("-"*30)

# 무게 환산표
print("-"*30)
print("%5s %5s %5s"% ("킬로그램","파운드","온스"))
print("-"*30)

for kg in range(100,201,2):
    pound=kg*2.205
    ounce=kg*35.274
    print("%7d   %7.1f   %7.1f"% (kg,pound,ounce))

print("-"*30)

# 접근 정보 제어
admin_info={"id":"GChr1s","password":"0837"}

x=input("아이디를 입력하세요 : ")
y=input("비밀번호를 입력하세요 : ")

if x==admin_info["id"] and y==admin_info["password"]:
    print("Access Granted")
else:
    print("Access Denied")

# 특정 범위 내의 정수 합계 구하기
start=int(input("첫번째 정수를 적으세요 : "))
end=int(input("두번째 정수를 적으세요 : "))
def sum_int(start,end):
    total=0
    for i in range(start,end+1):
        total=total+i
    print("%d ~ %d 정수 합계 : %d"% (start,end,total))

sum_int(start,end)

# 선형 탐색으로 최솟값 찾기
def find_min(n):
    smallest=n[0]
    for i in range(1,len(n)):
        if n[i]<smallest:
            smallest=n[i]

    return smallest

data=[6,3,-2,12,5,-3,17,9,13,16]
print(data)

min_value=find_min(data)
print('최솟값 :',min_value)

# 이진 탐색으로 내림차순에서 특정 값을 찾기
def binary_search(n,x):
    start=0
    end=len(n)-1

    while start<=end:
        mid=(start+end)//2
        if x==n[mid]:
            return mid
        elif x>n[mid]:
            end=mid-1
        else:
            start=mid+1

    return -1

data=[93,91,89,87,80,61,55,43,41,38,32,30,25,20,8,2]
print(data)

search_num=int(input("찾는 수를 적으세요 : "))
index=binary_search(data,search_num)
print('%d의 인덱스 번호 : %d'% (search_num,index))

# 짝수 홀수 판별하기

x=int(input("양의 정수를 입력하세요 : "))

if x%2==0:
    print("짝수!")
else:
    print("홀수!")

# 모듈
import hello

hello.greet1("chris")
hello.greet2("GChr1s")