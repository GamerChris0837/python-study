# 학습 내용

## 리스트(list)

### 🎉 리스트 생성 방법

```
list1 = [1,2,3,"사","오"]
print(list1)

결과 : [1,2,3,'사','오']
```

```
list2 = list(range(1,11,2))
print(list2)

결과 : [1,3,5,7,9]
```

---

### 🎉 메소드(Method)

* #### 메소드(Method) 정의

```
객체에 소속된 함수
```

* #### append() 메소드

```
예) list1.append(100)
리스트 list1의 맨 뒤에 100의 값을 추가함.
```

* #### find()  메소드

```
예) string1="Python is fun!"
print(string1)

x=string1.find("fun")   # 10은 "fun"의 "f"의 인덱스 번호를 의미함.
print(x)
```

* #### replace() 메소드

```
string1="사과는 맛있다. 나는 사과를 제일 좋아한다."
print(string1)

x=string1.replace("사과","수박")
print(x)
사과를 수박으로 변경함
```

* #### join() 메소드

```
예) names=["황예린","홍지수","안지영"]
print(names)

x="/".join(names)
print(x)
요소 사이사이에 "/"을 삽입함
```
### 🎉 메소드(Method) 간단 정리

```
find() : 문자열에서 특정 문자열을 찾아 위치(인덱스 번호)를 구함.
replace() : 문자열에서 특정 문자열을 다른 문자열로 치환함.
split() : 특정 문자열을 기준으로 문자열을 쪼개서 리스트에 저장함.
join(): 리스트의 요소를 하나로 묶어서 문자열로 변환함.
```