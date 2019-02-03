def displayInventory(inventory):

    total_items = 0

    print('Inventory:')

    for item, number in inventory.items():
        print(str(number) + ' ' + item)
        total_items += number

    print('Total number of items: ' + str(total_items))

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1

inventory = {
        'rope': 1,
        'torch': 6,
        'gold coin': 42,
        'dagger': 1,
        'arrow': 12,
        }
displayInventory(inventory)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(inventory, dragonLoot)
displayInventory(inventory)
