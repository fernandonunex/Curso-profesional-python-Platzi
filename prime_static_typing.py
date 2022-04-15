import time


def is_prime(number: int) -> bool:
    """This function evaluates if a number is a prime or not

    Args:
        number (int): any number integer positive

    Returns:
        bool: Returs True if is prime and False if is not prime
    """
    for factor in range(2, number):
        if number % factor == 0:
            return False
    return True


def is_prime_v2(number: int) -> bool:
    """This function evaluates if a number is a prime or not

    Args:
        number (int): any number integer positive

    Returns:
        bool: Returs True if is prime and False if is not prime
    """
    factors_list = [factor for factor in range(
        2, number) if number % factor == 0]

    return len(factors_list) == 0


def run():
    # Test for function V_1 (for and ifs)
    print("\nFor function V_1 (for and ifs)")
    t0 = time.time()
    # print(is_prime(5780107))   #Number that is not prime
    print(is_prime(7919))  # Number that is prime
    t1 = time.time()
    print("Time elapsed: ", t1 - t0)  # CPU seconds elapsed (floating point)

    # Test for function V_2 (List comprenhensions)
    print("\nFor function V_2 (List comprenhensions)")
    t0 = time.time()
    # print(is_prime_v2(5780107))    #Number that is not prime
    print(is_prime_v2(7919))  # Number that is prime
    t1 = time.time()
    print("Time elapsed: ", t1 - t0)  # CPU seconds elapsed (floating point)


if __name__ == '__main__':
    run()
