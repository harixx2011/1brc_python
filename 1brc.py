import time
import fileinput

FILENAME = "measurements/10mil.txt"
TESTCITY = "Barton"  # "Lapa"


class City:
    def __init__(self, name, temperature):
        self.name = name
        self.min = temperature
        self.max = temperature
        self.sum = temperature
        self.count = 1

    def avg(self):
        return round(self.sum / self.count, 1)

    def __str__(self):
        return f"City:{self.name}={self.min}/{self.avg()}/{self.max}"


def using_class():
    # TODO: Try reading file in chunks
    # with open(FILENAME, encoding="utf-8") as file:
    #     while True:
    #         chunk = file.read(1024)

    with open(FILENAME, "r", encoding="utf-8") as file:
        cities = {}
        for line in file:
            split_line = line.strip().split(";")
            city_name = split_line[0]
            temperature = round(float(split_line[1]), 1)

            if city_name not in cities:
                cities[city_name] = City(city_name, temperature)
            else:
                if temperature < cities[city_name].min:
                    cities[city_name].min = temperature
                elif temperature > cities[city_name].max:
                    cities[city_name].max = temperature
                cities[city_name].count += 1
                cities[city_name].sum += temperature

        print(cities[TESTCITY])


def baseline():
    with fileinput.input(FILENAME, encoding="utf-8") as file:
        city_temp = {}
        for line in file:
            x = line.strip().split(";")
            city = x[0]
            temperature = round(float(x[1]), 1)

            # Entry for this city doesn't exist yet so has to be created
            if city not in city_temp:
                min = max = sum = avg = temperature
                count = 1
                city_temp[city] = (min, max, sum, count, avg)
            # All other cases
            else:
                min = city_temp[city][0]
                max = city_temp[city][1]
                sum = city_temp[city][2]
                count = city_temp[city][3]
                sum += temperature
                count += 1
                avg = (sum / count)

                if temperature < min:
                    min = temperature
                    city_temp[city] = (min, max, sum, count, avg)
                elif temperature > max:
                    max = temperature
                    city_temp[city] = (min, max, sum, count, avg)

                city_temp[city] = (min, max, sum, count, avg)

    print(f"City:{TESTCITY}={city_temp[TESTCITY][0]}/{round(city_temp[TESTCITY][4],1)}/{city_temp[TESTCITY][1]}")


def main():
    print("Time 1 starts now:")
    time_start = time.perf_counter()
    baseline()
    time_end = time.perf_counter()
    print(f"Duration = {round(time_end - time_start, 2)}")

    print("Time 2 starts now:")
    time_start = time.perf_counter()
    using_class()
    time_end = time.perf_counter()
    print(round(time_end - time_start, 2))


if __name__ == "__main__":
    main()
