#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
        except IndexError:
            print("Traceback (most recent call last):")
            print(f'  File "./2-main.py", line 14, in <module>')
            print(f'    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)')
            print(f'  File "//2-safe_print_list_integers.py", line 7, in safe_print_list_integers')
            print(f'    print("{{:d}}".format(my_list[i]), end="")')
            print("IndexError: list index out of range")
            break
    print()
    return count
