try:
    print("start code")
    print(error)
    print("end code")
except:
    print("no problem")
print("any code...")

"""
def checker(var_1):
    if type(var_1)!=str:
        raise TapeError(f"Сорі, ми не працюємо з {type(var_1)}, ам теба str")
    else:
        return var_1
checker(1234)
"""

class BuildingHouseError(Exception):
    def __str__(self):
        return "Щось не те, дуже багато матеріалів"


def checker_material_building(amount, limit):
    if amount > limit:
        return "Достатньо матеріалів!"
    else:
        raise BuildingHouseError()
checker_material_building(10, 300)



