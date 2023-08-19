# 딕셔너리에 요소 추가
scores = {"kor": 100, "eng": 100, "math": 100}
print(scores)

scores["music"] = 100  # {'music': 100} 추가
print(scores)

# 딕셔너리 요소 수정
words = {"door": "문", "chair": "의자", "table": "책상", "house": "집"}
print(words)

words["table"] = "테이블"
print(words)

words["house"] = "하우스"
print(words)

# 딕셔너리 요소 삭제
car = {"brand": "mclaren", "model": "720s", "start": 2017, "year": 2023}
print(car)

x = car.pop("start")  # "start" 요소 추출과 동시에 해당 요소 삭제
print(x)

print(car)

# 딕셔너리 전제 요소 삭제
car = {"brand": "mclaren", "model": "720s", "start": 2017, "year": 2023}

car.clear()  # 딕셔너리 car의 전체 요소 삭제
print(car)
