import time
import fileinput

FILENAME = "hundred_mil.txt"

def testing():
     time_start = time.perf_counter()

     with fileinput.input(FILENAME, encoding="utf-8") as file:
          for line in file:
               continue

     time_end = time.perf_counter()
     print(time_end-time_start)

# TODO: Use class, object for each dict entry
def real_thing():
     time_start = time.perf_counter()
     with fileinput.input(FILENAME, encoding="utf-8") as file:
          for line in file:
               city_temp = {}
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
                    avg = city_temp[city][4]
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

     time_end = time.perf_counter()
     print(time_end-time_start)


def main():
     testing()


if __name__ == "__main__":
     main()
