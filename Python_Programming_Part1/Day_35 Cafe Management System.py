menu={"PIZZA":40,"PASTA":50,"BURGER":60,"SALAD":70,"COFEE":80}

print("!!!!...WELCOME TO PYTHON RESTAURANT...!!!!")
print("Pizza:RS.40\nPasta:RS.50\nBurger:RS.60\nSalad:RS.70\nCofee:RS.80")

order_Total=0


item_1=input("Enter the name of item you want to order : ")
if item_1 in menu:
    order_Total+=menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available yet")

for i in range(1,10):
    another_order=input("DO you want to add another item?(yes/No)")
    if another_order=="yes":
        item_2=input("Enter the name of item you want to order : ")
        if item_2 in menu:
            order_Total+=menu[item_2]
            print(F"Your item {item_2} has been added to your order")
        else:
            print(f"Ordered item {item_2} is not available yet")
    else:
        break


print(f"The total amount of items is {order_Total}")
