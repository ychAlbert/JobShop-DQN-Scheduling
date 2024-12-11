import math
import random

class Problem:
    def __init__(self, rand_time, num_jobs, num_mach):
        self.rand_time = rand_time
        self.num_jobs = num_jobs
        self.num_mach = num_mach

VERIFY = 0  # 1: produce the verification file
FIRMACIND = 0  # 0,1: first machine index

if VERIFY == 1:
    S = [
        Problem(0, 0, 0),
        Problem(873654221, 20, 5),
        Problem(0, 0, 0)
    ]
else:
    S = [
        Problem(0, 0, 0),
        Problem(873654221, 20, 5),
        Problem(379008056, 20, 5),
        Problem(1866992158, 20, 5),
        Problem(216771124, 20, 5),
        Problem(495070989, 20, 5),
        Problem(402959317, 20, 5),
        Problem(1369363414, 20, 5),
        Problem(2021925980, 20, 5),
        Problem(573109518, 20, 5),
        Problem(88325120, 20, 5),
        Problem(587595453, 20, 10),
        Problem(1401007982, 20, 10),
        Problem(873136276, 20, 10),
        Problem(268827376, 20, 10),
        Problem(1634173168, 20, 10),
        Problem(691823909, 20, 10),
        Problem(73807235, 20, 10),
        Problem(1273398721, 20, 10),
        Problem(2065119309, 20, 10),
        Problem(1672900551, 20, 10),
        Problem(479340445, 20, 20),
        Problem(268827376, 20, 20),
        Problem(1958948863, 20, 20),
        Problem(918272953, 20, 20),
        Problem(555010963, 20, 20),
        Problem(2010851491, 20, 20),
        Problem(1519833303, 20, 20),
        Problem(1748670931, 20, 20),
        Problem(1923497586, 20, 20),
        Problem(1829909967, 20, 20),
        Problem(1328042058, 50, 5),
        Problem(200382020, 50, 5),
        Problem(496319842, 50, 5),
        Problem(1203030903, 50, 5),
        Problem(1730708564, 50, 5),
        Problem(450926852, 50, 5),
        Problem(1303135678, 50, 5),
        Problem(1273398721, 50, 5),
        Problem(587288402, 50, 5),
        Problem(248421594, 50, 5),
        Problem(1958948863, 50, 10),
        Problem(575633267, 50, 10),
        Problem(655816003, 50, 10),
        Problem(1977864101, 50, 10),
        Problem(93805469, 50, 10),
        Problem(1803345551, 50, 10),
        Problem(49612559, 50, 10),
        Problem(1899802599, 50, 10),
        Problem(2013025619, 50, 10),
        Problem(578962478, 50, 10),
        Problem(1539989115, 50, 20),
        Problem(691823909, 50, 20),
        Problem(655816003, 50, 20),
        Problem(1315102446, 50, 20),
        Problem(1949668355, 50, 20),
        Problem(1923497586, 50, 20),
        Problem(1805594913, 50, 20),
        Problem(1861070898, 50, 20),
        Problem(715643788, 50, 20),
        Problem(464843328, 50, 20),
        Problem(896678084, 100, 5),
        Problem(1179439976, 100, 5),
        Problem(1122278347, 100, 5),
        Problem(416756875, 100, 5),
        Problem(267829958, 100, 5),
        Problem(1835213917, 100, 5),
        Problem(1328833962, 100, 5),
        Problem(1418570761, 100, 5),
        Problem(161033112, 100, 5),
        Problem(304212574, 100, 5),
        Problem(1539989115, 100, 10),
        Problem(655816003, 100, 10),
        Problem(960914243, 100, 10),
        Problem(1915696806, 100, 10),
        Problem(2013025619, 100, 10),
        Problem(1168140026, 100, 10),
        Problem(1923497586, 100, 10),
        Problem(167698528, 100, 10),
        Problem(1528387973, 100, 10),
        Problem(993794175, 100, 10),
        Problem(450926852, 100, 20),
        Problem(1462772409, 100, 20),
        Problem(1021685265, 100, 20),
        Problem(83696007, 100, 20),
        Problem(508154254, 100, 20),
        Problem(1861070898, 100, 20),
        Problem(26482542, 100, 20),
        Problem(444956424, 100, 20),
        Problem(2115448041, 100, 20),
        Problem(118254244, 100, 20),
        Problem(471503978, 200, 10),
        Problem(1215892992, 200, 10),
        Problem(135346136, 200, 10),
        Problem(1602504050, 200, 10),
        Problem(160037322, 200, 10),
        Problem(551454346, 200, 10),
        Problem(519485142, 200, 10),
        Problem(383947510, 200, 10),
        Problem(1968171878, 200, 10),
        Problem(540872513, 200, 10),
        Problem(2013025619, 200, 20),
        Problem(475051709, 200, 20),
        Problem(914834335, 200, 20),
        Problem(810642687, 200, 20),
        Problem(1019331795, 200, 20),
        Problem(2056065863, 200, 20),
        Problem(1342855162, 200, 20),
        Problem(1325809384, 200, 20),
        Problem(1988803007, 200, 20),
        Problem(765656702, 200, 20),
        Problem(1368624604, 500, 20),
        Problem(450181436, 500, 20),
        Problem(1927888393, 500, 20),
        Problem(1759567256, 500, 20),
        Problem(606425239, 500, 20),
        Problem(19268348, 500, 20),
        Problem(1298201670, 500, 20),
        Problem(2041736264, 500, 20),
        Problem(379756761, 500, 20),
        Problem(28837162, 500, 20),
        Problem(0, 0, 0)
    ]

def unif(seed, low, high):
    m = 2147483647
    a = 16807
    b = 127773
    c = 2836

    k = seed // b
    seed = a * (seed % b) - k * c
    if seed < 0:
        seed += m
    value_0_1 = seed / m

    return int(low + math.floor(value_0_1 * (high - low + 1)))

def generate_flow_shop(p):
    global d
    time_seed = S[p].rand_time
    d = [[0] * 501 for _ in range(21)]

    for i in range(S[p].num_mach):
        for j in range(S[p].num_jobs):
            d[i][j] = unif(time_seed, 1, 99)

def write_problem(p):
    with open(f"ta{p:03d}", "w") as f:
        f.write(f"{S[p].num_jobs} {S[p].num_mach}\n")
        for j in range(S[p].num_jobs):
            for i in range(S[p].num_mach):
                f.write(f"{i + FIRMACIND} {d[i][j]:2d} ")
            f.write("\n")

def main():
    i = 1
    while S[i].rand_time:
        generate_flow_shop(i)
        write_problem(i)
        i += 1

if __name__ == "__main__":
    main()
