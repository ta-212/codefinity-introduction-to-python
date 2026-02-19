# The item's discount and stock status have been defined
discounted = False
lowStock = True

movingProduct = discounted or lowStock
print(movingProduct)

movingProduct = True
promotion = not movingProduct
print("Is the item eligible for promotion?", promotion)
