def encoding(msg,num):


    newlist = []

    for i in range(len(msg)):
        newmsg = ord(msg[i])
        
        if num > 0:
            cezr = newmsg - num
            if cezr < 65:
                z = 65 - cezr
                cznum = 91 - z
                newlist.append(chr(cznum))       
            else:
                newlist.append(chr(cezr))
        elif num < 0 :
            cezr = newmsg + num
            if cezr < 65:
                z = 65 - cezr
                cznum = 91 - z
                newlist.append(chr(cznum))
            else:
                newlist.append(chr(cezr))

    decoded_msg = "".join(newlist)
    print(decoded_msg)


    print(newlist)


def decoding(msg,num):
    newlist = []

    for i in range(len(msg)):
        newmsg = ord(msg[i])
        cezr = newmsg + num
        # print(cezr)
        if cezr > 90:
            z = cezr - 90
            # print(z)
            cznum = 65 + z
            newlist.append(chr(cznum))
        else:
            newlist.append(chr(cezr))
    print(newlist)



def decoding_last(msg, num):
    newlist = []
    if num > 0:
        for i in range(len(msg)):
            newmsg = ord(msg[i])
            cezr = newmsg + num
            if cezr > 90:
                z = cezr - 90
                cznum = 64 + z
                newlist.append(chr(cznum))
            else:
                newlist.append(chr(cezr))
    elif num < 0:
        for i in range(len(msg)):
            newmsg = ord(msg[i])
            cezr = newmsg - num
            if cezr > 90:
                z = cezr - 90
                cznum = 64 + z
                newlist.append(chr(cznum))
            else:
                newlist.append(chr(cezr))
    decoded_msg = "".join(newlist)
    return decoded_msg




encoding('WELC',23)
encoding('OMET',25)
encoding('OACS',23)
encoding('FIRS',26)
encoding('TMEET',19)

print(decoding_last('RZGX',23))
print(decoding_last('VTLA',25))
print(decoding_last('BNPF',23))
print(decoding_last('VYHI',26))
print(decoding_last('MFXXM',19))


