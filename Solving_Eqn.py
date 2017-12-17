def solve_for_y(x_values):
    m=45
    c=0.5

    print("the value of m,c and is:{} {}".format(m, c))
    print("the equation is y=m*x+c")
    for x in x_values:
        y=m*x+c
        print("\nwhen x={} \nthen y={:.2f}".format(x,y))


solve_for_y([1, 2.3, 5.6, 7, 78])


