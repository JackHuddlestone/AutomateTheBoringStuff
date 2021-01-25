import pyinputplus as pyip

print('|| WELCOME TO MY SANDWICH SHOP')
print('|| PLEASE COMPLETE YOUR ORDER BELOW\n|| =========================')

#bread input and cost
bread = pyip.inputMenu(['Wheat', 'White', 'Sourdough'], prompt='|| Please select your bread.\n')
bread_cost = 1 #white bread cost
if bread.lower() == 'wheat' or bread.lower() == 'sourdough':
    bread_cost = 2 #wheat or sourdough bread cost

#protein input
protein = pyip.inputMenu(['Chicken', 'Turkey', 'Ham', 'Tofu'], prompt='\n|| Please select your protein.\n')
protein_cost = 2 #tofu and turkey cost.
if protein.lower() == 'chicken' or protein.lower() == 'ham':
    protein_cost = 3 #chicken and ham cost

#cheese input, as well as selection
cheese = pyip.inputYesNo(prompt='\n|| Would you like cheese? ')
cheese_cost = 0
if cheese.lower() == 'yes':
    cheese_cost = 1
    cheese_type = pyip.inputMenu(['Cheddar', 'Swiss', 'Mozzarella'], prompt='\n|| What cheese would you like?\n')

#dressing prompt
dressing = pyip.inputYesNo(prompt='\n|| Do you want mayo, mustard, lettuce and tomato? ')
dressing_cost = 0 #costs nothing for no dressing.
if dressing.lower() == 'yes':
    dressing_cost = 0.5 #50p for dressing.

#quantity of sandwiches
quantity = pyip.inputInt(prompt='\n|| How many sandwiches would you like? ', default=1)

#total cost
total_cost = bread_cost + protein_cost + cheese_cost + dressing_cost #gets initial cost
total_cost = total_cost * quantity #times it by the amount of sandwiches
total_tax = (total_cost * 0.20) + total_cost

print('\nPrinting receipt...')
print('|| =========================')
print('|| RECEIPT: ')
print('|| =========================')
print(f'|| Bread: {bread.title()} - £{bread_cost}')
print(f'|| Protein: {protein.title()} - £{protein_cost}')
if cheese_cost > 0:
    print(f'|| Cheese: {cheese_type.title()} - £{cheese_cost}')
if dressing_cost > 0:
    print(f'|| Dressing - £{dressing_cost}')
if quantity > 1:
    print(f'|| Quantity - x{quantity}')
print(f'||\n|| TOTAL ext. VAT - £{total_cost}')
print(f'|| TOTAL inv. VAT - £{total_tax}')
print('|| =========================')



