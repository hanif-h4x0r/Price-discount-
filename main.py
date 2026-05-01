def my_discount():
    try:
        price = float(input("Enter your price : "))
        discount = float(input("Enter your discount : "))
        
        if price <= 0:
            return "The price should be a number"
            
        if discount  < 0 or discount > 100:
            return "The discount should between 0 and 100"
            
        return price - (price * discount / 100)
        
    except ValueError:
        return "Please enter a valid number"
   
print(my_discount())
