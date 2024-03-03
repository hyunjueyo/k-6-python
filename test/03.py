print("3-1")
names=['선영','나혜','하언','선호']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

print("3-2")
print(f"안녕~ {names[0]}, {names[1]}야!")

print("3-4")
guests=['엄마','아빠','언니']
print(f"{guests[0]},{guests[1]},{guests[2]}! 저녁 식사에 초대합니다.")

print("3-5")
guests[1] = '남이이모'
print(f"{guests[0]},{guests[1]},{guests[2]}! 저녁 식사에 초대합니다.")

print("3-6")
guests.insert(0,'큰이모')
guests.insert(2,'막내이모')
guests.append('송연이언니')
print(f"{guests[0]},{guests[1]},{guests[2]},{guests[3]},{guests[4]}! 저녁 식사에 초대합니다.")

print("3-7")
