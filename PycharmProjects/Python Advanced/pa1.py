"Function"


def purchase_product (product_type, price, mobile_brand, material):
    if product_type == "mobile":
        if mobile_brand == "Apple":
            discount = 10
        else:
            discount = 5
    else:
        if material == "Leather":
            discount = 20
    total_price = price - price * discount / 100
    print("Total price of" + product_type + "is" + str(total_price))
