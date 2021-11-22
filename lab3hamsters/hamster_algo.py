class Hamster:
    def __init__(self, h, g):
        self.h = h
        self.g = g

    def how_much_hamster_will_eat(self, number_of_hamsters):

        food_needed = self.h + self.g * number_of_hamsters
        return food_needed


def max_number_of_hamsters(inp_file):
    with open(inp_file, mode="r")as file:
        s = int(file.readline())
        # number of all hamsters
        c = int(file.readline())

        # need to look through all of the hamsters
        hamsters = []
        i = 0
        while i < c:
            h1, g1 = file.readline().split(" ")
            h1, g1 = int(h1), int(g1)

            # check if input is suitable for conditions
            if h1 <= s:
                hamsters.append(Hamster(h1, g1))
            i += 1

    # attribute how_much_hamster_will_eat changes from number of hamsters for each Hamster

    number = 1
    if hamsters[0].h > s:
        return 0
    elif hamsters[0].h == s:
        return number
    while number <= len(hamsters):
        consume = 0
        hamsters.sort(key=lambda hamster: hamster.how_much_hamster_will_eat(number-1))

        for i in range(number):
            consume += hamsters[i].how_much_hamster_will_eat(number-1)
        if consume < s:
            number += 1
        elif consume == s:
            return number
        else:
            break
    number -= 1
    return number


if __name__ == '__main__':
    input_file = input("Please set the pass to the input file:")
    n = max_number_of_hamsters(input_file)

    print("Max number of hamsters:", n, " Also save as a file hamsters_output")

    with open("hamsters_output.txt", mode="w+") as external_file:
        external_file.write("Max number of hamsters:")
        external_file.write(f"{n}")
        external_file.close()
