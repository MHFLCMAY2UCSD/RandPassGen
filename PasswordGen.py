import random


class Password:
    def __init__(self, value: int):
        self.length = 126
        self.random = 0
        self.iteration = value

    def random_ascii(self):
        password = [] * self.iteration

        for i in range(self.iteration):
            # Just to keep the values around the leter ascii value.
            self.random = random.randint(32, self.length)
            temp_rand = chr(self.random)
            password.append(temp_rand)

        return ''.join(password)