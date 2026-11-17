product = {
    "name":"Ghar Face Wash",
    "price":700,
    "description":"Natural face wash, removes TAN",
    "ingredients":"Lactic Acide",
    "expiryDate":"31-12-2027",
    "quantity": 10
}

totalStockValue = product.get("price") * product.get("quantity")
print("Total Stock Value of",product.get("name"),"=",totalStockValue)