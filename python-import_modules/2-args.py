#!/usr/bin/python3
if _name_ == "_main_":
    import sys
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 argument:")
    elif len(sys.argv) > 2:
        print(f"{len(sys.argv) - 1} arguments:")
    i = 1
    for arg in sys.argv[1:]:
        print(f"{i}: {arg}")
        i += 1
