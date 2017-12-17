salary = [15000, 20000, 17000, 18900, 30000]

print("the salary after raise is:")
for index, each in enumerate (salary,start=1):
    total=(23/100)*each+each
    print("for employee {}, the total salary after 23% increase is {}" .format(index, total))
