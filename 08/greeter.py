# def 함수정의, 콜론 다음이 바디, """"""은 독스트링이라는 주석
def greet_user():
    """단순한 인사말을 표시합니다"""
    print("hello")

greet_user()
help(greet_user) #document string을 출력해줌
print(greet_user.__doc__) #document string만 출력해줌

# 함수에 정보 전달
def greet_user(username):
    """단순한 인사말을 표시합니다"""
    print(f"hello, {username.title()}!")

greet_user('jesse')

# username 스트링은 immutable (구글 파이썬 스트링 변수 immutable 변경 검색) 책에는 설명이 없음
def greet_user(username):
    """단순한 인사말을 표시합니다"""
    print(f"hello, {username.title()}!")
    username = 'kim'
input_name = 'jesse'
greet_user(input_name) #함수 호출
input_name = 'kim' #값 변경이 아니라 변수를 다시 설정
print(input_name)

# 196p
def describe_pet(animal_type, pet_name):
    """"반려동물 정보를 표시합니다"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster', 'harry')
# 키워드 값을 넣어주면 순서 상관없이 동작한다.(자바에 없음)
describe_pet(pet_name='harry', animal_type='hamster')

# 기본값 지정
def describe_pet(pet_name, animal_type='dog'):
    """"반려동물 정보를 표시합니다"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='willie')
describe_pet('willie')

# 단순한 값 반환하기
def get_formatted_name(first_name, last_name):
    """실제 이름을 깔끔한 형식으로 반환합니다"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# 인수를 옵션으로 만들기
def get_formatted_name(first_name, middle_name, last_name):
    """실제 이름을 깔끔한 형식으로 반환합니다"""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi', 'lee', 'hendrix')
print(musician)  