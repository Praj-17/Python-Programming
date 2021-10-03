print("Enter Actual price ")
actual_price = int(input())
print("Enter Selling price ")
selling_price = int(input())
returns = selling_price - actual_price
if returns >0:  print("profit of rs: ", returns)
elif returns<0: print("loss of rs: ", returns*-1)