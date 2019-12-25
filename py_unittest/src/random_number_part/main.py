
import random


class Omikuji(object):

    def generate_random_number(self):
        return random.random()

    def get_fortune(self, random_number):
        if random_number >= 0.9:
            return '大吉'
        return '凶'

    def get_lottery(self):
        random_number = self.generate_random_number()
        return self.get_fortune(random_number)


if __name__ == '__main__':
    omikuji = Omikuji()
    lottery = omikuji.get_lottery()
    print(lottery)
