#test case = 9,9,9


def plusOne(digits: list[int]) -> list[int]:
    number = int(''.join(list(map(str, digits))))
    number +=1
    digits = list(map(int,list(str(number))))
    return digits

        
        