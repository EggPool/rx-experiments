"""
Mining simulator for RandomX, based upon maths, stats, and real miner dataset.
(c) 2019 - EggdraSyl
"""

from math import log
from random import choices

# To be tuned more precisely with more experimental data
MINER_LUCK = (0.5, 0.9, 0.99)
LUCK_WEIGHTS = (1, 8, 1)


class MinerSimulator:
    def __init__(self, hash_rate: int):
        self.hash_rate = hash_rate

    @classmethod
    def HEX(cls, hash: int) -> str:
        return hash.to_bytes(32, "big").hex()

    @classmethod
    def find_nums_for_luck(cls, luck: float, number_of_hashes: int) -> []:
        previous = 0
        for i in range(1, 63):
            proba = (1 / 16) ** i  # probability to get i zeros for a single hash
            num_hashes = log(1 - luck) / log(
                1 - proba
            )  # number of required hashes to get i 0s with given luck.
            if num_hashes > number_of_hashes:
                return i, previous
            previous = num_hashes
        return 63, 3e77  #  Max

    def get_min_hash(self, verbose: bool = False) -> int:
        """Returns min hash "found" over 1 minute, given current hashrate.
           several calls will not return the same value.
        """
        number_of_hashes = 60 * self.hash_rate
        luck = choices(MINER_LUCK, LUCK_WEIGHTS)[0]
        num0, numh = self.find_nums_for_luck(luck, number_of_hashes)
        hash = int(num0 * "0" + (64 - num0) * "f", 16)  # rough min hash approx
        hash_tuned = int(hash * numh / number_of_hashes)
        if verbose:
            print("Number of hashes", number_of_hashes)
            print("Luck", luck)
            print("num0, numh", num0, numh)
            print("hash", self.HEX(hash))
            print("hash_tuned", self.HEX(hash_tuned))
        return hash_tuned
