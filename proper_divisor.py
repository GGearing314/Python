def properDivisors(number):
    output=list()
    for i in range(1,number):
        if number%i==0:
            output.append(i)
    return output


