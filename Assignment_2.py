def motion(x):
    velocities = []
    for i in range(len(x)-1):
        a = (x[i+1][0] - x[i][0])/(x[i+1][1] - x[i][1])
        velocities.append(a)
    print(velocities)

    if velocities.count(a) == len(x)-1:
        print('Uniform Motion')
    else:
        print('Non Uniform motion')

motion([(0,0),(5,1),(10,2),(15,3)])

# input = [(0,0),(5,1),(10,2),(15,3)]
# input = [(0,0),(5,1),(10,2),(15,4)]



















