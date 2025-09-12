amount = int(input("Enter withdrawal Amount : "))
if amount % 100 ==0:
    print("Amount Eligible for Withdrawal")
else:
    print("Please enter amount in mutliples of 100")
