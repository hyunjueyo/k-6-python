# 65p 연습문제
friend_name = 'kim hyunju'
print(f"안녕하세요. {friend_name}, 오늘 파이썬 배워 보는 게 어떨까요?")

print(friend_name.upper())
print(friend_name.lower())
print(friend_name.title())

# 85p 연습문제 꼭 해보세요

# 102p 연습문제

# 117p
#8-09
def show_messages(messages):
    for message in messages:
        print(message)

messages = ["안녕", "반가워", "잘가"]
show_messages(messages)

print()
#8-10
def send_messages(messages, sent_messages):
    while messages:
        current_messages = messages.pop()
        print(f"Sending messages: {current_messages}") 
        sent_messages.append(current_messages)

def show_messages(messages):
    print("\nAll messages")
    for message in messages:
        print(message)

messages = ["안녕", "반가워", "잘가"]
sent_messages = []

send_messages(messages, sent_messages)
show_messages(messages)

# 218p 연습문제 검사할거야