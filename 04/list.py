# range() 1~4
for value in range(1,5) : 
    print(value)

print()

# 0~5
for value in range(6) : 
    print(value)

print()

# list[0~5]
numbers = list(range(6))
print(numbers)

# set{0~5}
numbers = set(range(6))
print(numbers)

# list[1~10, 2씩 증가], 세번째 있는 건 step
numbers = list(range(1,10,2))
print(numbers)

# 치환문은 코드의 식별성을 위해 띄어써라
# : 은 루트의 시작
squares = []
for value in range(1,11):
    # square은 list의 변수, value**은 값의 제곱
    square = value ** 2
    squares.append(square)
print(squares)
# 루트 안에 없어도 value 값(10)을 출력할 수 있다.
print(value)

# 4.3.4 리스트 내포, 위 수식을 간단하게.
# 리스트를 for문으로 만듬
squares = [value**2 for value in range(1,11)]
print(squares) 

# list -> slice : 앞부터 3번째에 슬라이스, 인덱스가 0부터인 거 잊지말기!
print(squares[0:3])
print(squares[:3])
# 예시 https://codetorial.net/tips_and_examples/list_slicing.html  
print(squares[-3:])
print(squares[-3:-2])
print(squares[:-2])
# 리스트 값 복사 (주소 복사X)
print(squares[:])
# +스텝 (세번째는 step)
print(squares[::2])
# 거꾸로
print(squares[::-1])
print(squares[::-3])
# 반반
print(squares[:3],squares[3:])

# shallo/deep copy
players= ['charles', 'martina', 'michael', 'florence', 'eli']
for player in players[:3]:
    print(player.title())

    my_foods = ['pizza', 'falafel', 'carrot cake']
    freind_foods = my_foods[:] #deep copy
    # freind_foods = my_foods #shallow copy
    my_foods.append('cannoli')
    print(my_foods)
    print(freind_foods)

# 듀플
dimensions = (10,20)
# dimensions = [10,20] 이렇게 쓰면 오류 안 남
# dimensions[0] = 30
print(dimensions)
# 듀플 순회하기
for dimension in dimensions:
    print(dimension)
# 듀플 덮어쓰기 : 듀플을 가리키는 변수에 새 값 할당 가능
dimension = (200,50)