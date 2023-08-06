# for문에서 리스트 사용 예
colors=["빨간색","파란색","노란색","검정색","초록색"]

for color in colors:
    print("난 %s을 좋아함!"% color)   # %s는 문자열

# for문에서 range() 함수 사용 예
colors=["빨간색","파란색","노란색","검정색","초록색"]

n=len(colors)   # len() 함수 : 리스트의 길이
for i in range(0,n):   # i의 값 : 0 ~ 4
    print("난 %s을 좋아함!"% colors[i])   # i : colors의 인덱스

# while문에서 리스트 사용 예
animals=["코끼리","호랑이","사슴","펭귄","여우"]

i=0
while i<len(animals):   # len() 함수 : 리스트 길이
    print(animals[i])   # animals[i] : 인덱스 i의 요소

    i=i+1