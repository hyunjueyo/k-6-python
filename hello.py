# # 0228 복습
# print('hello!')

# # 백준 입력값은 자동으로 줌
# a,b = input().split()
# # a= int(a), b= int(b)
# print(int(a)+int(b))

# a,b = input().split()
# print(a+b)
# print(a-b)
# print(a*b)
# print(int(a/b)) # int(a/b)로 바꿔줘야 소수로 안 나올껄
# print(a%b)

# # 길이 재는 거
# s, len(input())

# a= list()
# b= []
# b=[1,2,3,4,5] #생성
# b[3] #조회 ->4

a= [1,2,3,4,5]
print(a)
print(a[::-1])

for s in 'abcde':
    print(s)

print()

for i in range(5):
    print(i)

print((type([1,2,3,4,5])))

d={1: 'a',
   2: 'b',
   3: 'c',
   4: 'd',
   5: 'e'}
print(d)

for i in d: #오늘 배우는 거.
    print(i) #

print()

for i in (1,2,3,4,5):
    print(i)

#5장 복습
for i in range(1, 6):
    if i % 2 == 0:
        print(i, 'even')
    else:
        print(i, 'odd')
#라인을 잘 맞춰줘야 해요 F8누르면 오류로 바로 감
for i in range(1, 6):
    if i % 2 == 0:
        print(i, 'even')
    elif (i %3 ==0):
        print(i, '3')
    else: #마지막에 꼭 끝내줘야함
        print(i, 'odd') 
        # print('unknown')
#자바랑 다른 것 : and랑 or을 씀
        
#백준 조건문 위에 두 문제 풀기
# a,b = input().split()
# a,b = int(a), int(b)
# if a>b:
#      print('>')
# if a<b:
#      print('<')
# if a==b:
#      print('==')    

# input은 string타입
def input2():
    return '1 2'
print(type(input2()))

#단계별로 하고 싶으면
s= input()
a, b = s.split()
a, b = int(a), int(b)
#같은 거임
a,b = int('a'), int('b')
print(a, b)
# #구구단
# N = input().split()
# N = int(N)
# for n in range(1, N+1):
#     if 

s= input().split()
print(len(s))

a= input().split()
a= int(a)

#최대 최소 구하는 거
lst ={1, 2, 3, 4, 5}
print(max(lst))