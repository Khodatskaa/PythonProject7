goods = ['Tomato', 4.55, 'Mango', 89.72, 'Bell pepper', 43.88, 'Grapes', 71.55, 'Cantaloupe', 102.74]
users = {}
admins = {}
basket = []

admin_email_pattern = '@admin.com'

is_login_true = False
is_admin = False

try:
    with open("user.txt", "w") as file:
            file.write("aaaa@gmail.com:55555aaaaa\n")

except Exception as e:
    print(e)

try:
    with open("user.txt", "r") as file:
        contents = file.readlines()
        if len(contents) == 0:
            print("No users found")
        for user_info in contents:
            user_info = user_info.strip().split(":")
            if len(user_info) == 2:
                admin = user_info[0]
                password = user_info[1]
                admins[admin] = password

except Exception as e:
    print(e)

try:
    with open("admins.txt", "w") as file:
            file.write("al@admin.com:qwerty\n")

except Exception as e:
    print(e)

try:
    with open("admins.txt", "r") as file:
        contents = file.readlines()
        if len(contents) == 0:
            print("No admins found")
        for admin_info in contents:
            admin_info = admin_info.strip().split(":")
            if len(admin_info) == 2:
                admin = admin_info[0]
                password = admin_info[1]
                admins[admin] = password

except Exception as e:
    print(e)


try:
    while True:
        while True:
            login = input("Enter login: ")
            password = input("Enter password: ")
            if admin_email_pattern in login:
                if login not in admins:
                    print("This administrator does not exist. Try again")
                    continue
                if admins[login] == password:
                    print("You are logged in as an administrator")
                    is_admin = True
                    break
                else:
                    print("Incorrect password. Try again")
                    continue
            elif login in users:
                if users[login] == password:
                    print(f"You are logged in as user - {login}")
                    break
                else:
                    print("Incorrect password")
            else:
                print("User with this login does not exist")
                print("Want to register?")
                answer = input("Enter yes or no: ")
                if answer.lower() == 'yes':
                    users[login] = password
                    print("You are successfully registered")
                    print("You can log in")

        while True:
            if is_admin:
                print('You are logged in as an administrator')
                print('To log out, enter "exit"')
                print('To add an item, enter "add"')
                print('To delete an item, enter "del"')
                print('To log out from the administrator mode, enter "exit admin"')
                answer = input("Enter a command: ")
                if answer == 'exit':
                    exit()
                elif answer == 'add':
                    name = input("Enter item name: ")
                    price = float(input("Enter item price: "))
                    goods.append(name)
                    goods.append(price)
                    print("Item added")
                elif answer == 'del':
                    name = input("Enter item name: ")
                    if name in goods:
                        item_index = goods.index(name)
                        del goods[item_index:item_index + 2]
                        print("Item deleted")
                    else:
                        print("This item does not exist")
                elif answer == 'exit admin':
                    is_admin = False
                    break
                else:
                    print("Invalid command. Try again.")
            else:
                counter = 0
                for i in range(0, len(goods), 2):
                    counter += 1
                    print(f"{counter}: {goods[i]}\t\t{goods[i + 1]:.2f}")
                print('What item would you like to buy?')
                print('To log out, enter "exit"')
                answer = input("Enter item name: ")

                if answer == 'exit':
                    print('Would you like to log out?')
                    answer = input("Enter yes or no: ")
                    if answer.lower() == 'yes':
                        print('Goodbye!')
                        exit()
                    else:
                        break
                else:
                    if answer in goods:
                        basket.append(answer)
                        print("Item added to cart")
                    else:
                        print("This item does not exist")

        while True:
            if basket:
                print("Your Shopping Cart:")
                total_price = 0

                for item in basket:
                    item_index = goods.index(item)
                    item_name = item
                    item_price = float(goods[item_index + 1])
                    total_price += item_price

                    print(f"{item_name}: ${item_price:.2f}")

                print(f"Total Price: ${total_price:.2f}")

                print("Menu:")
                print("1. Add Item to Cart")
                print("2. View Cart")
                print("3. Calculate Total Price")
                print("4. Complete Purchase")
                print("5. Log Out")

                user_choice = input("Enter your choice: ")

                if user_choice == "1":
                    item_to_add = input("Enter the item you want to add to your cart: ")
                    if item_to_add in goods:
                        basket.append(item_to_add)
                        print(f"{item_to_add} has been added to your cart.")
                    else:
                        print("Item not found in the list.")
                elif user_choice == "2":
                    print("Your Shopping Cart:")
                    for item in basket:
                        item_index = goods.index(item)
                        item_name = item
                        item_price = float(goods[item_index + 1])
                        print(f"{item_name}: {item_price:.2f}")
                    print(f"Total Price: {total_price:.2f}")
                elif user_choice == "3":
                    print(f"Total Price: {total_price:.2f}")
                elif user_choice == "4":
                    if basket:
                        print(f"Total Price: {total_price:.2f}")
                        print("Thank you for your purchase!")
                        basket = []
                    else:
                        print("Your cart is empty.")
                elif user_choice == "5":
                    print("Logging out...")
                    break
                else:
                    print("Invalid choice. Please try again.")
            else:
                break


except Exception as e:
    print(e)
