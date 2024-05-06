def stuff(data):
    return data.replace('11111','111110')

def destuff(data):
    return data.replace('111110', '11111')



data = input("Enter String = ")
stuffing = stuff(data)
print("Stuffing String = ",stuffing)
destuffing = destuff(stuffing)
print("Destuffing String = ",destuffing)