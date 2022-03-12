import copy
import random
# import sys

def lotos(seed=None):

    number = [1,  2,  3,  6,  7,  10, 11, 12, 13, 16, 19,  20,  21,  24,  25,
              26,  30,  31,  35,  42]

    loto = []

    #  print (len(number))

    if seed is not None and seed != "":
        # print("[USAGE] python3 {} [seeds]".format(sys.argv[0]))
        random.seed(a=seed)

    for i in range(5):
        line = copy.deepcopy(number)
        for i in range(len(number) - 6):
            del line[random.randint(0, len(line) - 1)]
        loto.append(line)

    return loto

#    for line in loto:
#        print(line)

