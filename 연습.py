# 쓸데 없는 거
id=input("아이디 : ")
password=input("비번 : ")

print("아이디 :",id)
print("비밀번호 :",password)
a=int(input("아무 번호 : "))

if a==1:
    print("1")
elif a==2:
    print("22")
else:
    print(":)")

# 알바 급여 계산기
print("아르바이트 급여 계산 프로그램")
print("🎉 시급")
print("- 주간 근무 : 10,000원")
print("- 야간 근무 : 주간 시급 * 15")
print()

pay=10000

a=int(input("1(주간 근무) 또는 2(야간 근무)를 입력 해주세요 : "))
work=int(input("근무 시간을 입력 해주세요 : "))