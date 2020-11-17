from pizzapy import Customer, StoreLocator

customer = Customer('Truong', 'Ryan', 'ryanhoang2000@yahoo.com', '5153183898', '711 High St, Des Moines, IA, 50309')

my_local_dominos = StoreLocator.find_closest_store_to_customer(customer)
print(my_local_dominos)
print("\nMENU\n")

menu = my_local_dominos.get_menu()
#menu.search(Name = "Coke")

def searchMenu(menu):
	print("You are now searching the menu...")
	while True:
		item = input("Type an item to look for: ").strip().lower()

		if item != "" and len(item) > 1:
				item = item[0].upper() + item[1:]
		else:
			print("Invalid, exiting search....")
			break

		print(f"Results for: {item}")
		menu.search(Name = item)

#searchMenu(menu)
