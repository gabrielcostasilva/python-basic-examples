def is_prime(n):
  return n > 1 and all(n % d for d in range(2, int(n**(1/2)) + 1))

if __name__ == "__main__":
    print(is_prime(-1))
    print(is_prime(0))
    print(is_prime(1))
    print(is_prime(2))
    print(is_prime(3))
    print(is_prime(4))
    print(is_prime(5))