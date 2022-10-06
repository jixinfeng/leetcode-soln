"""
Description:
    Count the number of prime numbers less than a non-negative number, n.

Credits:
    Special thanks to @mithmatt for adding this problem and creating all test
    cases.

Hint:
    Let's start with a isPrime function. To determine if a number is prime, we
    need to check if it is not divisible by any number less than n. The runtime
    complexity of isPrime function would be O(n) and hence counting the total
    prime numbers up to n would be O(n2). Could we do better?
    
    As we know the number must not be divisible by any number > n / 2, we can
    immediately cut the total iterations half by dividing only up to n / 2.
    Could we still do better?
    
    Let's write down all of 12's factors:
        2 × 6 = 12
        3 × 4 = 12
        4 × 3 = 12
        6 × 2 = 12

    As you can see, calculations of 4 × 3 and 6 × 2 are not necessary.
    Therefore, we only need to consider factors up to √n because, if n is
    divisible by some number p, then n = p × q and since p ≤ q, we could derive
    that p ≤ √n.
    
    Our total runtime has now improved to O(n1.5), which is slightly better. Is
    there a faster approach?
    
    public int countPrimes(int n) {
       int count = 0;
       for (int i = 1; i < n; i++) {
          if (isPrime(i)) count++;
       }
       return count;
    }
    
    private boolean isPrime(int num) {
       if (num <= 1) return false;
       // Loop's ending condition is i * i <= num instead of i <= sqrt(num)
       // to avoid repeatedly calling an expensive function sqrt().
       for (int i = 2; i * i <= num; i++) {
          if (num % i == 0) return false;
       }
       return true;
    }
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        is_prime = [False, False] + [True] * (n - 2)
        for i in range(2, int(sqrt(n)) + 1):
            if is_prime[i]:
                for j in range(i ** 2, n, i):
                    is_prime[j] = False

        return sum(is_prime)


"""
too slow, time limit exceeded for n=499979
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        primes = [2]
        candidates = list(range(3, n, 2))[::-1]
        cache = []
        while candidates or cache:
            curr_prime = candidates.pop()
            primes.append(curr_prime)
            while candidates:
                c = candidates.pop()
                if c % curr_prime != 0:
                    cache.append(c)
            
            candidates = cache[::-1]
            cache = []
        
        return len(primes)
"""
