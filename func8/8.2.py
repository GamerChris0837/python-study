# 소수 여부 판별하기
def is_prime(n):
    prime=True # prime의 초깃값은 True
    if n>1: # n이 2부터 시작
        for i in range(2,n): # n:2~n-1
            if n%i==0: # i로 나눈 나머지가 0이면
                prime=False # prime을 False로 설정

    return prime

number=int(input("수를 입력하세요 :"))

if is_prime(number):
    print("소수!")
else:
    print("소수X!")

# 1~N 세제곱 합계 구하기
def square_sum(n):
    sm=0
    for i in range(1,n+1): # i:1~n
        sm=sm+(i*i*i) # 누적합계 sm 구함

    return sm

N=int(input("N의 값을 입력하세요 :"))
print(square_sum(N))

# 회문(Palindrome) : 똑바로 읽어도 거꾸로 읽어도 똑같은 단어나 문장

# 회문인지 판별하기
def is_palindrome(s):
    for i in range(0,int(len(s)/2)): # 문자열의 좌측 절반 읽음
        if s[i]!=s[len(s)-i-1]: # 좌측과 우측 인덱스가 다른지 비교
            return False

    return True

string=input("문장 or 단어?")

if is_palindrome(string):
    print("%s은(는) 회문!"% string)
else:
    print("%s은(는) 회문X!"% string)

# 문장 단어 반대로 하기
