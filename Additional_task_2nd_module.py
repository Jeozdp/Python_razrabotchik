def generate_pairs(n):
    pairs = []

    for i in range(1, n):
        for j in range(i + 1, n + 1):
            pairs.append(str(i) + str(j))

    return pairs


def generate_password(n):
    pairs = generate_pairs(n)
    result = ''

    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if (n % (i + j)) == 0:
                result += str(i) + str(j)

    return result

n = 12
print(generate_password(n))