def right_angle_triangle(n):
    for i in range(1, n + 1):
        print('* ' * n - i * i)

n = int(input("Enter the number of rows: "))
right_angle_triangle(n)

