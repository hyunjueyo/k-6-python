#함수의 매개변수로 함수 전달하기
def ten_times(func):
    for i in range(5):
        func()

def print_hello():
    print("hello")
ten_times(print_hello) #함수를 전달

def print_work():
    print('coding')
ten_times(print_work)

#파라메타를 전달하는 거 
def add(x,y) :
    return x+y

def minus(x,y) :
    return x-y

def apply_operation(operationm, x, y):
    return operationm(x,y)

result = apply_operation(add,3,4)
result = apply_operation(minus,3,4)

#람다식