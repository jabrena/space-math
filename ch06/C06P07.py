def combination(n, k):
    if k == 0 or k == n:
        return str(1)
    else:
        return str(int(combination(n - 1, k - 1)) + int(combination(n - 1, k)))


def pascals_triangle(rows):
    for row in range(rows):
        answer = ""

        for column in range(row + 1):
            answer += combination(row, column) + " "

        print(answer)


pascals_triangle(10)
