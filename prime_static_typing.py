import time


def is_prime(number: int) -> bool:
    for factor in range(2,number):
        if number % factor == 0:
            return False
    return True



def run():
    t0 = time.time()
    print(is_prime(5780))
    t1 = time.time()
    print("Time elapsed: ", t1 - t0) ## CPU seconds elapsed (floating point)




if __name__ == '__main__':
    run()