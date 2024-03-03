bicycles = ['trek', 'cannondale', 'redline', 'specialized']

# ['trek', 'cannondale', 'redline', 'specialized']
print (bicycles)
# 첫번째 인덱스 반환 ->trek
print (bicycles[0]) 
# 마지막에서 첫번째 인덱스 반환 ->specialized
print (bicycles[-1])
# 마지막에서 두번째 인덱스 반환 ->redline
print (bicycles[-2])

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
