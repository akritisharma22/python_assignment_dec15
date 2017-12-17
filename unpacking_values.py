def fnc():
    return ("Hello", 45, 23.3)


temp=fnc()

x,y,z=temp

print('The function returned the following values using unpacking:\n'+x, y, z, sep='\n')