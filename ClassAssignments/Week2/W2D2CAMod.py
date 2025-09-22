import W2D2CAArg

# Only positional
print("Bill 1:", W2D2CAArg.calculate_bill(500, 2))

# With custom tax
print("Bill 2:", W2D2CAArg.calculate_bill(500, 2, tax=0.1))

# With custom discount
print("Bill 3:", W2D2CAArg.calculate_bill(500, 2, discount=50))
# With custom tax and discount
print("Bill 4:", W2D2CAArg.calculate_bill(500, 2, tax=0.08, discount=100))
