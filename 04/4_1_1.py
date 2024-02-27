cars = ['bmw', 'audi', 'toyota', 'sabaru']
# 확장명 for 문. 자바-> for(int n : arr) sysout(n);
for car in cars: 
    print(car)
    print(f"my car is a {car}")
# for문에서 나오려면 커서를 맨 앞으로 옮겨주면 됨
print("리스트 출력 완료")

for car2 in cars:
    print('my car')
    for c2 in cars:
        print('중첩')
print("for문 종료")