# while문으로 1~10 합계 구하기
sum=0
i=1

while i<=10:
    sum=sum+i
    print("i의 값 : %2d => 합계 : %d"% (i,sum))

    i=i+1

# while문으로 5의 배수 합계 구하기
sum=0
i=500   # i의 값을 500으로 설정

while i<=600:
    if i %5==0:   # 5의 배수인지 체크
        sum=sum+i

    i=i+1

print("500부터 600까지의 5의 배수 합계 : %d"% (sum))

# while문으로 영어 모음 개수 구하기
s = "Python is widely used by a number of big companies."

i=0
count=0 # 모음 개수 카운트 변수 count를 0으로 초기화

print("모음 :",end="")

while i<=len(s)-1: #len(s)는 문자열 s의 문자 개수를 구함
    