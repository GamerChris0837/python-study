score = int(input("점수?"))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
elif score >= 50:
    grade = "E"
else:
    grade = "F"

print("등급 : ", grade)


print("기능 선택")
print("1. 더하기")
print("2. 빼기")
print("3. 곱하기")
print("4. 나누기")
print()

s = input("계산기 기능을 선택하세요(1/2/3/4) :")

num1 = int(input("첫 번째 숫자를 입력하세요 :"))
num2 = int(input("두 번째 숫자를 입력하세요 :"))

if s == "1":
    print("%d + %d = [%d]" % (num1, num2, num1 + num2))
elif s == "2":
    print("%d - %d = [%d]" % (num1, num2, num1 - num2))
elif s == "3":
    print("%d * %d = [%d]" % (num1, num2, num1 * num2))
elif s == "4":
    print("%d / %d = [%d]" % (num1, num2, num1 / num2))
else:
    print("똑바로 안 쓰나?")
