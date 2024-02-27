name= "ade lovelace"
print(name)
# 대문자로 시작
print(name.title())
# 모두 대문자로
print(name.upper()) 
# 모두 소문자로
print(name.lower())

# first_name ="ada"
# last_name="lovelace"
# # f-문자열의 f는 format을 뜻함
# full_name=f"{first_name}\t{last_name.title()}!"
# print(full_name)

print('language: \npython\tjava')
last_name=' lovelace '
last_name.lstrip

bicycles=['trek','cannondale','redline','specialized']
print (bicycles)
print (bicycles[0])
print (bicycles[3])
# 마지막에서 첫번째 요소 반환
print (bicycles[-1])
# 마지막에서 두번째 요소 반환
print (bicycles[-2])

message=f"bicycles was a {bicycles[0].title()}"
print(message)

motorcycles=['honda', 'yamaha', 'suzuki']
print(motorcycles)
# 요소 바꾸기
motorcycles[0]='ducati'
print(motorcycles)
# append() : 리스트 마지막에 요소 추가 
motorcycles.append('GM')
print(motorcycles)
# insert(1,'') : 원하는 위치에 요소 삽입
motorcycles.insert(1,'Samcheonri')
print(motorcycles)
# del : 요소 삭제하기
del motorcycles[0]
print(motorcycles)
# pop() : 리스트의 마지막 요소를 제거하는 동시에 해당 요소를 반환 
motorcycles.pop()
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(popped_motorcycles)

print(f'the last owned motor was a {popped_motorcycles.title()}')

motorcycles2=['honda', 'ducati', 'yamaha', 'suzuki', 'ducati']
motorcycles2.remove('ducati')
# ducati 두개 중 한 개만 제거됨, 두개 다 제거 하려면 루프를 사용해야함.
print(motorcycles2)
