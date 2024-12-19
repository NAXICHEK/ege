from itertools import permutations

def meshanina(x):
    result = list(permutations(x))
    return [list(item) for item in result]

print(meshanina([524, 673 ,234]))