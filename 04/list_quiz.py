# https://velog.io/@jsomedev/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A6%AC%EC%8A%A4%ED%8A%B8List-2%EC%B0%A8%EC%9B%90-%EB%A6%AC%EC%8A%A4%ED%8A%B8-slicing-sorting-%EA%B9%8A%EC%9D%80-%EB%B3%B5%EC%82%AC-vs-%EC%96%95%EC%9D%80-%EB%B3%B5%EC%82%AC
# 리스트 덧셈
a = [1, 2]
b = [3, 4]
c = a + b 
print(c)

# 리스트 빼기 -> remove()사용
a = [1, 2, 3, 4]
b = [3, 4]
# c = a - b #에러, 파이썬에서 -가 없음
c1 = [x for x in a if x not in b]
c2 = list(set(a)-set(b))
print(c1)
print(c2)

# shallow copy/deep copy 여기 뭔가 이상
a=[10, 20, 30, 40, 50] 
# b= a   #shallow copy 얕은 복사->출력하면 100
b = a[0:3] #deep copy 깊은 복사 : 실제 값을 새로운 메모리 공간에 복사
a[0] = 100
print(b)

# shallow copy : 실제 값이 아닌 주소값을 복사
a = [[1,2,3],[4,5,6]]
b = a[:]
print(b) #[[1,2,3],[4,5,6]]
a[0][0] = 100

players= ['charles', 'martina', 'michael', 'florence', 'eli']
for player in players[:3]:
    print(player.title())
