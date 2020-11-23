inpuNumber = eval(input("Escolha um número: "))
array = [1, 15, 2, 7, 2, 5, 7, 1, 4]


def AvaliarSeSomavel(a):
    for x in array:
        for y in array:
            if x+y == a:
                return True
    return False


print(AvaliarSeSomavel(inpuNumber))
