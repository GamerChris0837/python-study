# 주민번호로 성별 찾기
x=int(input("주민번호 뒷자리 첫 번째 숫자를 입력하세요 : "))

if x%2==1:
    print("남자!")
elif x%2==0:
    print("여자!")
else:
    print("중성!")