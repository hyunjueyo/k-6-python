# >>> x,y = 11,22
# >>> y,x = x,y
# >>> x
# 22
# >>> y
# 11
# >>>

def test():
    return (10,20)
a,b = test() #tuple 값을 리턴
print(f"a= {a}, b= {b}")

list = ['a', 'b', 'c', 'd']
# enumerate() 함수는 인덱스와 값을 줌, 리턴값이 tuple임. 그래서 i가 필요함. 이런 형태 참 많이 나와
for i, value in enumerate(list):
    print(f"i = {i}, value = {value}")

# 140p 5.4.2에 내용 추가
# if a == 0.0:/if a ==0 하지 않아도 if a:하면 파이썬에서는 간편하게 처리해줌


