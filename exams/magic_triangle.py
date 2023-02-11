def get_magic_triangle(integer):
    triangle = [[1], [1, 1]]

    for i in range(3, integer + 1):

        current_row = [(triangle[i - 2][n - 1] if n - 1 in range(len(triangle[i - 2])) else 0) +

                       (triangle[i - 2][n] if n in range(len(triangle[i - 2])) else 0)

                       for n in range(i)]

        triangle.append(current_row)

    return triangle
