try:
    print("start code")
    print(error)
    print("end code")
except:
    print("no problem")
print("any code...")


def checker(var_1):
    if type(var_1)!=str:
        raise TapeError(f"Сорі, ми не працюємо з {type(var_1)}, ам теба str")
    else:
        return var_1
checker(1234)
