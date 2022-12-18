def isPowerOfTwo( n: int) -> bool:
    #         1 = 1
    #       1 0 = 2
    #     1 0 0 = 4
    #   1 0 0 0 = 8
    # 1 0 0 0 0  = 16
    # print(str(bin(n))[3:])
    if str(bin(n))[2] == '1' and str(bin(n))[3:] == ''.join(['0' for i in range(len(str(bin(n))[3:]))]):
        return True
    else: return False