x = int(input('сколько тебе лет ? '))

def funk(a):
    if a < 18:
        print('доступ закрыт')
    else:
        print('доступ окрыт')
funk(x)




def newfunk(age):
    return age >= 18

age = int(input('сколько тебе лет ? '))

print('доступ открыт' if newfunk(age) else 'доступ закрыт')