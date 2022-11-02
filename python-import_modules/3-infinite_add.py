#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ad = 0
    for i in sys.argv[1:]:
        ad += int(i)
    print(ad)
