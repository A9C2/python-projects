#! python3
# problem_10.py - Find the sum of all the primes below two million.

def sieve(n):
    bool_list = [True for x in range(n-1)]
    prime_list = []

    for i in range(len(bool_list)):
        if bool_list[i]:
            prime_list.append(i+2)
            for k in range(1, (len(bool_list)+1) // (i+2)):
                bool_list[i + (i+2) * k] = False
                
    return prime_list

print(sum(sieve(2_000_000)))