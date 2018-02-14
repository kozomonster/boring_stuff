def div42by(byNumer):
    try:
        return 42 / byNumer
    except ZeroDivisionError:
        print('error nie dziel przez 0')


print(div42by(4))
print(div42by(0))