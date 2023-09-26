#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    try:
        for i in range(list_length):
            try:
                list1 = float(my_list_1[i])
                list2 = float(my_list_2[i])
                if list2 == 0:
                    result.append(0)
                    print("division by 0")
                else:
                    result.append(list1 / list2)
            except ValueError:
                result.append(0)
                print("wrong type")
            except IndexError:
                result.append(0)
                print("out of range")
    except ZeroDivisionError:
        result.append(0)
        print("division by 0")
    finally:
        return result
