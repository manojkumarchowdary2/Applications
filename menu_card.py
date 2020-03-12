#Menu Card
menu={'Idly':20,'Dosa':25,'Roti':25,'Chapati':30,'Gaare':20,
      'Pulihora':40,'Fried Rice':50,'Noodles':40,'Plate Meals':50,'Full Meals':70,
     'Tea':10,'Coffee':15,'Cool Drink':20}
print('Items available...\n')
for item,price in menu.items():
    print(item,'Rs/-',price)
bill=0
items=input('Give your order:').split(',')
for item in items:
    if item in menu.keys():
        bill+=menu[item]
    elif item not in menu.keys():
        print('Sorry!',item,'not available')
print('Your bill=','Rs',bill,'/-')
