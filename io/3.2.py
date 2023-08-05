# 비교 연산자 : >,<,==,!=,<=,>=
# 논리 연산자 : and, or, not

#비교 연산자 종류
# a==b : a와 b는 같다.
# a!=b : a와 b는 같지 않다.
# a>b : a는 b보다 크다.
# a>=b : a는 b보다 크거나 같다.
# a<b : a는 b보다 작다.
# a<=b : a는 b보다 작거나 같다.
print(5==5)

print(10>20)

print(8<=8)

a=10
b=20
print(a==b)
print(a!=b)
print(a%b>=10)

# 조건1 and 조건2 : 논리곱(and),
# 조건1과 조건2가 둘 다 참인 경우에만 참이 됨.

# 조건1 or 조건2 : 논리합(or),
# 조건1 또는 조건2 중 하나만 참이어도 참이 됨.

# not 조건 : 논리부정(not),
# 조건이 참이면 거짓, 거짓이면 참으로 해서 논리 값을 반대로 변경함.
score1=75
score=90
print(score1>=80 and score2>=80)

score3=85
score4=95
print(score3>=80 and score4>=80)

x=10
print(x%2==0 or x%6==0)

y=16
print(y%3==0 or y%5==0)

z=25
print(not z%2==0)
print(not z>10)