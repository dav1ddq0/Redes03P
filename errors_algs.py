def xor(n1, n2):
    result = []

    for i in range(1, len(n2)):
        if n1[i] == n2[i]:
            result.append('0')
        else:
            result.append('1')
    
    return ''.join(result)

crc_key = '1001'

def mod2div(divident, divisor):
    # Number of bits to be XORed at a time.
    pick = len(divisor)
    # Slicing the divident to appropriate
    # length for particular step
    tmp = divident[0 : pick]
    while pick < len(divident):
        if tmp[0] == '1':
            # replace the divident by the result
            # of XOR and pull 1 bit down
            tmp = xor(divisor, tmp) + divident[pick]
        else:   # If leftmost bit is '0'
            # If the leftmost bit of the dividend (or the
            # part used in each step) is 0, the step cannot
            # use the regular divisor; we need to use an
            # all-0s divisor.
            tmp = xor('0'*pick, tmp) + divident[pick]
        # increment pick to move further
        pick += 1
    
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)

    remainder = tmp
    return remainder

def CRCEncode(data):
    # x^3+x+1 representing en bin like 1 0 1 1 
    # Add n-1 zeroes at end of data where n is len of key
    l_key = len(crc_key)
    appended_data = data + '0'*(l_key-1)
    remainder = mod2div(appended_data, crc_key)
    
    return remainder    

def CRCDecode(data):
    # x^3+x+1 representing en bin like 1 0 1 1 
    # Add n-1 zeroes at end of data where n is len of key 
    remainder = mod2div(data)
    
    return remainder

def CheckError(remainder):
    return remainder == 0