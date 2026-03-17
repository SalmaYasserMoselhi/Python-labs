def mario_pyramid(n):
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "*" * i
        print(spaces + stars)

mario_pyramid(4)