# 8.4.1 함수 내부에서 리스트 수정하기 + 책에 없는 내용
# 함수내에서 수정 가능하다. 함수 내부의 리스트는 변경가능한 객체 : mutable
# mutable(값이 변함) / immutable(값이 변하지 않음) 검색해서 설명
# https://ledgku.tistory.com/54

# 숫자형 (Number) : immutable
x=1
y=x
y+=3
print(x) #->1
print(y) #->4

# 문자열 (String) : immutable
x='abcd'
y=x
y += 'e'
print(x)
print(y)

# 리스트 (List) : mutable
x=[1,2]
y=x
print(y)
y.append(3)
print(x)
print(y)


# # 출력할 디자인이 저장된 리스트
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# # 남은 게 없을 때까지 디자인 출력
# # 출력한 디자인을 completed_models로 옮김
# while unprinted_designs: #빈 리스트면 false
#     current_design = unprinted_designs.pop() #한개씩 삭제
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)

# # 완료된 디자인 표시
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#         print(completed_model)


# 함수 두개 추가
def print_models(unprinted_designs, completed_models): #리스트가 parameter이면 mutable
    while unprinted_designs: #빈 리스트면 false
        current_design = unprinted_designs.pop() #한개씩 삭제
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """출력된 모델을 모두 표시합니다"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

#immutable 변수는 튜플, 숫자, 스트링, 불리언
#immutable 객체를 함수로 전달 -> 변하지 않는 거 확인하기 
def modify_string(s): #string 값을 전달받음
    s= s + "world"#변수 s는 원래 변수가 가리키는 주소와 다름
    print(s) #함수 안에서는 출력 결과 => helloworld
st = "hello"
modify_string(st)
print(st)    #함수 밖에서는 출력 결과 => hello

#deep copy 설명
lst = [1,2,3]
lst_two = lst[:] #슬라이싱
print(lst_two)
lst.append(4)
print(lst)
print(lst_two)

print()
#shadow copy 설명
lst2=lst
lst2.append(5)
print(lst2)
print(lst)