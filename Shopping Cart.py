def shopping_cart_app():
    foods = []
    prices = []
    total = 0
    while True:
        print("1 to add to list, 2 to check total list, 3 to reset")
        choice = int(input("Choice: "))

        if choice == 1:
            add_food = str(input("Food: "))
            add_price = float(input("Price: "))
            add_quantity = int(input("Quantity: "))
            cost = add_price * add_quantity
            foods.append(add_food)
            prices.append(add_price)
            total += cost

        elif choice == 2:
            for add_food in foods:
                print(add_food)
                
            print(f"Your total is ${total}")

        elif choice == 3:
            foods.clear()
            prices.clear()
            total = 0

shopping_cart_app()
    

                
