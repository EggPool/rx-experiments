"""
Generate hash samples to get a practical sense of RX hashes output and hash/diff relationship
"""

from pyrx import PyRX
import json
import random
from time import time


ALPHABET = "0123456789abcdef"

PYRX = PyRX()


def get_header():
    # random test header
    part1 = "".join(random.choices(ALPHABET, k=46))
    part2 = "{nonce}"
    part3 = "0000000000000028acfa28a803d2000000000000000000000000000000000000"
    part4 = "".join(random.choices(ALPHABET, k=64))
    return part1 + part2 + part3 + part4


def get_nonce(size: int=10):
    return "".join(random.choices(ALPHABET, k=size))


def make_dataset(num: int):
    # best hash of a 10k batch
    # 100 times
    seed_hash = bytes.fromhex('4181a493b397a733b083639334bc32b407915b9a82b7917ac361816f0a1f5d4d')  # sha256(yadacoin65000)
    # if not isinstance(nonce, int):
    #    nonce = int(nonce, 16)

    data = []
    random.seed("seed for dataset {}".format(num))
    for i in range(100):
        header = get_header()
        best = bytes.fromhex('f' * 64)
        best_nonce = 0
        start = time()
        for j in range(10000):
            nonce = get_nonce()
            buffer = header.format(nonce=nonce)
            bh = PYRX.get_rx_hash(buffer, seed_hash, i, 8)
            if bh < best:
                best = bh
                best_nonce = nonce
        data.append([header, i, best_nonce, best.hex()])
        print(int(time()-start), i, best.hex())
    with open("data/data_{}.json".format(num), "w") as fp:
        json.dump(data, fp, indent=2)


if __name__ == '__main__':
    make_dataset(1)
