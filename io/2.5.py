name="이지안"
print(name)

a=10
b=20
print(a,b,a-b,100)

# 키워드 'sep="/"'을 이용하여
# '2023 3 7'를 '2023/3/7'로 출력함.
year=2023
month=3
day=7
print(year,month,day,sep="/")

# 키워드 'sep="-"'을 이용하여
# '010 4936 4227'을 '010-4936-4227'로 출력함.
hp1="010"
hp2="4936"
hp3="4227"
print(hp1,hp2,hp3,sep="-")

# 키워드 'sep=""'을 이용하여
# '10000 원'을 '10000원'으로 출력함.
price=10000
print(price,"원",sep="")

# %d = 정수형(Interger) 숫자
# %f = 실수형(Floading Point) 숫자
# %.1f = 실수에서 소수점 첫째 자리(둘째 자리에서 반올림)까지 구함.
#s = 문자열(String)
x=25
y=3.3
animal="호랑이"
print("%d %f %s"% (x,y,animal))
print("%.1f"% y)

# 이스케이프 코드
# \n = 줄 바꿈
# \t = 탭
# \\ = 역슬래쉬(\) 출력
# \' = 단 따옴표(') 출력
# \" = 쌍 따옴표(") 출력
print("안녕하세요.\n반갑습니다.")
print("안녕하세요.\t반갑습니다.")
print("\\")
print("\'")
print("\"") 