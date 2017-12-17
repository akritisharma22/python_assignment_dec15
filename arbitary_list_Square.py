def square(list):
    new_list=[]
    print("the list is {}".format(list))
    for each in list:
        square= each**2
        new_list.append(square)

    return new_list



print("the squared list is{}".format(square([1,2,3,4,5,6])))


