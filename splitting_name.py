def name():
    full_name=input("\nEnter you full name: ")
    return full_name.split(" ")


temp=name()
if(len(temp)==3):
    first_name, middle_name, last_name=temp
    print('First name: {}\nMiddle name: {}\nLast name: {}'.format(first_name, middle_name, last_name))

else:
    first_name, last_name=temp
    print('First name: {}\nLast name: {}'.format(first_name, last_name))