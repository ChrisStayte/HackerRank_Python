def print_formatted(number):
    paddingsize = (len("{0:b}".format(number)) + 1)
    for i in range (1, number + 1):
        decimal, octal, hexadecimal, binary = str(int(i)), str(int(oct(i))), "%X" % i, "{0:b}".format(i)
        print decimal.rjust(paddingsize - 1) + octal.rjust(paddingsize) + hexadecimal.rjust(paddingsize) + binary.rjust(paddingsize)
