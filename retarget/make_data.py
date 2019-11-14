"""
Create data for simulations
(c) 2019 - EggdraSyl
"""

import json

# from mockup import Blockchain, Block
from minersimulator import MinerSimulator
from math import sin, pi


SPECIAL_MIN_TIME = 5 * 60


def init_stable(
    start,
    end,
    block_time=60,
    target="0000000000000028acfa28a803d2000000000000000000000000000000000000",
    file="stable.json",
):
    start_time = 0
    blocks = []
    for height in range(start, end):
        block = {
            "time": start_time,
            "height": height,
            "special_min": True if block_time > SPECIAL_MIN_TIME else False,
            "target": target,
            "block_time": block_time,  # This one is not native.
        }
        start_time += block_time
        blocks.append(block)
    with open("data/init/{}".format(file), "w") as fp:
        json.dump(blocks, fp)


def hash_stable(hash_count: int, hash_rate:int, file="stable.json"):
    simu = MinerSimulator(hash_rate)
    hashes = []
    for i in range(hash_count):
        hashes.append((simu.hash_rate, simu.HEX(simu.get_min_hash())))
    with open("data/live/{}".format(file), "w") as fp:
        json.dump(hashes, fp, indent=2)


def hash_arithmetic(hash_count: int, start: int, increment: int, file="arithmetic.json"):
    simu = MinerSimulator(start)
    hashes = []
    for i in range(hash_count):
        hashes.append((simu.hash_rate, simu.HEX(simu.get_min_hash())))
        simu.hash_rate += increment
    with open("data/live/{}".format(file), "w") as fp:
        json.dump(hashes, fp, indent=2)


def hash_step(hash_count: int, start: int, h_end: int, file="step.json"):
    simu = MinerSimulator(start)
    hashes = []
    for i in range(hash_count):
        hashes.append((simu.hash_rate,simu.HEX(simu.get_min_hash())))
        if i == hash_count//2:
            simu.hash_rate = h_end
    with open("data/live/{}".format(file), "w") as fp:
        json.dump(hashes, fp, indent=2)


def hash_sinus(hash_count: int, base: int, amplitude: int, period: int, file="sinus.json"):
    simu = MinerSimulator(base)
    hashes = []
    for i in range(hash_count):
        hashes.append((simu.hash_rate,simu.HEX(simu.get_min_hash())))
        simu.hash_rate = base + amplitude * sin(i * 2 * pi / period)
    with open("data/live/{}".format(file), "w") as fp:
        json.dump(hashes, fp, indent=2)


if __name__ == "__main__":
    init_stable(
        0,
        1000,
        block_time=3600,
        target="0000000000000028acfa28a803d2000000000000000000000000000000000000",
        file="stable_3600_14.json",
    )
    init_stable(
        0,
        1000,
        block_time=60 * 5,
        target="000000ffffffffff28acfa28a803d20000000000000000000000000000000000",
        file="stable_300_6.json",
    )
    init_stable(
        0,
        1000,
        block_time=60 * 5,
        target="00000ffffffffff28acfa28a803d200000000000000000000000000000000000",
        file="stable_300_5.json",
    )
    init_stable(
        0,
        1000,
        block_time=60 * 5,
        target="0000ffffffffff28acfa28a803d2000000000000000000000000000000000000",
        file="stable_300_4.json",
    )
    init_stable(
        0,
        1000,
        block_time=60 * 5,
        target="000ffffffffff28acfa28a803d2000000000000000000000000000000000000",
        file="stable_300_3.json",
    )

    hash_stable(10000, 167, file="stable_167.json")
    hash_stable(10000, 1670, file="stable_1670.json")
    hash_stable(10000, 16700, file="stable_16700.json")

    hash_arithmetic(10000, 167, 16, file="arithmetic_167_16.json")

    hash_step(10000, 167, 500, file="step_up_167_500.json")
    hash_step(10000, 500, 167, file="step_down_500_167.json")

    hash_sinus(10000, 300, 150, 60*12, file="sinus_300_150_720.json")
    hash_sinus(10000, 300, 100, 1440, file="sinus_300_100_1440.json")
    hash_sinus(10000, 300, 100, 2880, file="sinus_300_100_2880.json")
