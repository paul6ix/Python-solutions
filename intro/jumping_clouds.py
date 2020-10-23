def jumpingOnClouds(c):
    energy = 0
    i = 0
    while i < n - 1:
        if i + 2 >= n or c[i + 2] == 1:
            i = i + 1
            energy = energy + 1
        else:
            i = i + 2
            energy = energy + 1
    return energy
