# remove() : 제거할 인덱스의 값만 알고 있을 때
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

# remove() 메서드 역시 제거한 값을 반환함
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(f"\nA {too_expensive.title()} is too expensive for me.")

print("\n지정한 값과 일치하는 첫 번째 요소만 제거함")
motorcycles2=['honda', 'ducati', 'yamaha', 'suzuki', 'ducati']
motorcycles2.remove('ducati')
# ducati 두개 중 한 개만 제거됨, 두개 다 제거 하려면 루프를 사용해야함.
print(motorcycles2)