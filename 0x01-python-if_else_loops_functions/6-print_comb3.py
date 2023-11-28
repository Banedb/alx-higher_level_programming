#!/usr/bin/python3
for i in range(1, 100):
    if i != 89:
        if i < 10 or str(i)[0] < str(i)[1]:
            print("{:02}".format(i), end=", ")
    else:
        print("{}".format(i))
