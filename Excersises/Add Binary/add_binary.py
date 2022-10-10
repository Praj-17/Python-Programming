from more_itertools import difference


def addBinary(a: str, b: str) -> str:
    if int(a) == 0: 
        return b
    elif int(b) == 0: 
        return a
    else: 
        #Checking weather they are of same length, if not adding leading zeros to the smaller one
        #Adding leading zeros to handle carry condition
        if len(a) != len(b):
            difference = len(a) - len(b)
            if len(a) >len(b):              
               for i in range(difference):
                   b = '0' + b
            else:
                for i in range(-1*difference):
                   a = '0' + a
           
        a = '0' + a 
        b = '0' + b 
        answer = ''
        carry = 0
        for i,j in zip(reversed(a),reversed(b)):
            if int(i) + int(j) + carry == 0:
                answer = '0' + answer
                carry = 0
            elif int(i) + int(j) + carry == 1:
                answer = '1' + answer
                carry = 0
            elif int(i) + int(j) + carry == 2:
                answer = '0' + answer
                carry = 1
            elif int(i) + int(j) + carry == 3:
                answer = '1' + answer
                carry = 1
        return str(int(answer)  )
    
print(addBinary('11', '1'))
    