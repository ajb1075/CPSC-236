#Challenged myself to do each function on one line

def is_prime(number: int) -> (bool, int): return (num_factors := sum([1 for i in range(1, number + 1) if number % i == 0])) == 2, num_factors

def valid (number: int) -> bool: return number in range(2,5001) 