"""
(c) 2019 - EggdraSyl
"""

from minersimulator import MinerSimulator


if __name__ == "__main__":
    simu = MinerSimulator(167)  # 167 H/s, small i5 cpu - around 10 KH/min
    print("167")
    for i in range(10):
        simu.get_min_hash(verbose=True)
        print("--")
    print("20000")
    simu.hash_rate = 20000
    for i in range(10):
        simu.get_min_hash(verbose=True)
        print("--")
