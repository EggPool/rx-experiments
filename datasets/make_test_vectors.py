"""
Generate hash samples to get a practical sense of RX hashes output and hash/diff relationship
"""

from pyrx import PyRX
import json
import random


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


def make_test_vectors(num: int):

    seed_hash = bytes.fromhex(
        '4181a493b397a733b083639334bc32b407915b9a82b7917ac361816f0a1f5d4d')  # sha256(yadacoin65000)

    data = []
    random.seed("seed for test vector {}".format(num))
    nonce_base = get_nonce()
    header = get_header()
    for i in range(1000):
        nonce = int(nonce_base, 16) + i
        nonce_hex = nonce.to_bytes(10, "big").hex()
        buffer = header.format(nonce=nonce_hex)
        bh = PYRX.get_rx_hash(buffer, seed_hash, i, 8)
        data.append([header, i, nonce_hex, bh.hex()])
    with open("data/vector_{}.json".format(num), "w") as fp:
        json.dump(data, fp, indent=2)


if __name__ == '__main__':
    for i in range(10):
        make_test_vectors(i + 1)