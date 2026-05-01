def my_discount(price, discount):
	price = float("Enter your price : ")
	discount = float("Enter your discount : ")
	if not isinstance(price, (int, float)) or not isinstance (discount, (int, float):
		return "The price and discount should be a number"

	return  price - (price * discount / 100)

print(my_discount(price, discount))
