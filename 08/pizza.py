def make_pizza(size, *toppings): #tuple로 받음
    """주문 내용 요약"""
    print(f"\nMaking a {size}-inch pizza whith the follwing toppings:")
    for topping in toppings:
        print(f" - {topping}")
