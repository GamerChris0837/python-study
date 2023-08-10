# find() 메소드로 문자열 찾기
string1="Python is fun!"
print(string1)

x=string1.find("fun")   # 10은 "fun"의 "f"의 인덱스 번호를 의미함.
print(x)

# replace() 메소드로 문자열 치환하기
string1="사과는 맛있다. 나는 사과를 제일 좋아한다."
print(string1)

x=string1.replace("사과","수박")
print(x)

#전화번호에서 하이픈(-) 삭제하기
phone1="010-4936-4227"
print(phone1)

phone2=phone1.replace("-","")
print(phone2)

#split() 메소드 사용 예시
hello="Have a great day"
print(hello)

list1=hello.split(" ")   # " "(공백)으로 요소를 나눔.
print(list1)
print(type(list1))

for i in range(0,len(list1)):
    print("list1[%d] : %s"% (i,list1[i]))

# join() 메소드로 리스트를 문자열로 변환하기
names=["황예린","홍지수","안지영"]
print(names)

x="/".join(names)
print(x)

# 전화번호에 하이픈(-) 삽입된 문자열로 변환하기
phone1=["010","4936","4227"]
print(phone1)

phone2="-".join(phone1)
print(phone2)

# 리스트 문자열에서 하이픈(-) 삭제하기
phone_list=["010-1111-2222","010-3333-4444",
"010-5555-6666","010-7777-8888","010-9999-0000"]
print(phone_list)

phone_list2=[]
for number in phone_list:
    x=number.replace("-","")

    phone_list2.append(x)

print(phone_list2)

# 리스트 문자열에서 문자 치환하기
sentences=["Love me, love my dog.",
"No news os good news.","Blood is thicker than water."]

for sentence in sentences:
    x=sentence.replace(" ","_")
    print(x)
# find() : 문자열에서 특정 문자열을 찾아 위치(인덱스 번호)를 구함.
# replace() : 문자열에서 특정 문자열을 다른 문자열로 치환함.
# split() : 특정 문자열을 기준으로 문자열을 쪼개서 리스트에 저장함.
# join(): 리스트의 요소를 하나로 묶어서 문자열로 변환함.