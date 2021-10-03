print("pls input the number of units used")
units = int(input())  
c1 , c2, c3, c4 = 0,0,0,0
i = 0
if i<=50: c1 += i*0.5
if i>=51 and i<=150: c2+= i*0.75
if i>=151 and i<=250: c3+= i*1.25
if i>=251 and i<=units: c4+= i*1.5

total_charges = c1+c2+c3+c4
final_charges = total_charges + total_charges*17/100
print(final_charges)
    

    



  
        



