x = int(input("양의 정수를 입력하세요 :"))

if x % 2 == 0:
    print("짝수!")
else:
    print("홀수!")


pilgi = int(input("필기시험 점수?"))
silgi = int(input("실기시험 점수?"))

if pilgi >= 95 and silgi >= 95:
    result = "합격"
else:
    result = "불합격"

print("- 필기시험 점수 : %d" % pilgi)
print("- 실기시험 점수 : %d" % silgi)
print("- 판정 : %s" % result)


char = input("영문 소문자 하나")

if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
    print("%s은(는) 모음이다." % char)
else:
    print("%s은(는) 자음이다." % char)
