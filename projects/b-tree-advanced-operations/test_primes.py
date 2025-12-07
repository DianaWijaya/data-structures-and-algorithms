import random
import unittest
from b_tree import millerRabinRandomisedPrimality as millerrabinprimality

# --- Helper function for Sieve of Eratosthenes ---
def _sieve(limit):
    """Generates primes up to a given limit using Sieve of Eratosthenes."""
    primes = []
    is_prime_list = [True] * (limit + 1)
    if limit >= 0:
      is_prime_list[0] = False
    if limit >= 1:
      is_prime_list[1] = False
    for p in range(2, limit + 1):
        if is_prime_list[p]:
            primes.append(p)
            for multiple in range(p * p, limit + 1, p):
                is_prime_list[multiple] = False
    return primes

# --- Unittest Class ---
class TestMillerRabin(unittest.TestCase):
    SIEVE_LIMIT = 1500
    K_ITERATIONS_FOR_TEST = 5 # Number of Miller-Rabin iterations for tests

    # Test case counts (approximate)
    TARGET_EVEN_COMPOSITES = 200
    TARGET_P1P2_COMPOSITES = 250 # p1 * p2
    TARGET_P_SQUARE_COMPOSITES = 150 # p * p
    TARGET_P1P2P3_COMPOSITES = 300 # p1 * p2 * p3 (adjust to get ~1000 total)

    @classmethod
    def setUpClass(cls):
        """Set up test data once for all tests."""
        print(f"Setting up test data for {cls.__name__}...")
        cls.sieve_primes = _sieve(cls.SIEVE_LIMIT)
        cls.odd_sieve_primes = [p for p in cls.sieve_primes if p > 2]

        # 1. Edge cases
        cls.edge_case_primes_to_test = [2, 3]
        cls.edge_case_composites_to_test = [0, 1, 4]
        
        # 2. Sieve primes (excluding those already in edge cases)
        cls.sieve_primes_to_test = [p for p in cls.sieve_primes if p not in cls.edge_case_primes_to_test]

        # 3. Even composites
        cls.even_composites_to_test = set()
        min_val, max_val = 6, cls.TARGET_EVEN_COMPOSITES * 20 + 100 # Range to pick from
        while len(cls.even_composites_to_test) < cls.TARGET_EVEN_COMPOSITES:
            n = random.randrange(min_val, max_val, 2) # Generate even numbers
            if n not in cls.sieve_primes and n not in cls.edge_case_composites_to_test:
                 cls.even_composites_to_test.add(n)
            if len(cls.even_composites_to_test) >= cls.TARGET_EVEN_COMPOSITES: break # Safety break
        cls.even_composites_to_test = list(cls.even_composites_to_test)[:cls.TARGET_EVEN_COMPOSITES]


        # 4. Odd composites: p1 * p2
        cls.odd_composites_p1p2_to_test = set()
        if len(cls.odd_sieve_primes) >= 2:
            all_combs = []
            for i in range(len(cls.odd_sieve_primes)):
                for j in range(i + 1, len(cls.odd_sieve_primes)): # Ensures p1 != p2 and unique pairs
                    all_combs.append(cls.odd_sieve_primes[i] * cls.odd_sieve_primes[j])
            
            if len(all_combs) <= cls.TARGET_P1P2_COMPOSITES:
                 cls.odd_composites_p1p2_to_test = set(all_combs)
            else:
                 cls.odd_composites_p1p2_to_test = set(random.sample(all_combs, cls.TARGET_P1P2_COMPOSITES))
        cls.odd_composites_p1p2_to_test = list(cls.odd_composites_p1p2_to_test)


        # 5. Odd composites: p * p (squares)
        cls.odd_composites_p_square_to_test = set()
        all_squares = [p*p for p in cls.odd_sieve_primes]
        if len(all_squares) <= cls.TARGET_P_SQUARE_COMPOSITES:
            cls.odd_composites_p_square_to_test = set(all_squares)
        else:
            cls.odd_composites_p_square_to_test = set(random.sample(all_squares, cls.TARGET_P_SQUARE_COMPOSITES))
        cls.odd_composites_p_square_to_test = list(cls.odd_composites_p_square_to_test)


        # 6. Odd composites: p1 * p2 * p3
        cls.odd_composites_p1p2p3_to_test = set()
        if len(cls.odd_sieve_primes) >= 3:
            # Generate a pool of p1*p2*p3 products and sample from it
            # This is more efficient than trying to hit an exact number of unique products directly
            # if the number of combinations is very large.
            # For TARGET_P1P2P3_COMPOSITES * 5 attempts, we should get enough unique products.
            attempts = 0
            max_product_generation_attempts = cls.TARGET_P1P2P3_COMPOSITES * 10
            
            while len(cls.odd_composites_p1p2p3_to_test) < cls.TARGET_P1P2P3_COMPOSITES and attempts < max_product_generation_attempts:
                try:
                    p1, p2, p3 = random.sample(cls.odd_sieve_primes, 3)
                    cls.odd_composites_p1p2p3_to_test.add(p1 * p2 * p3)
                except ValueError: # Not enough primes to sample 3 distinct ones
                    break 
                attempts += 1
        cls.odd_composites_p1p2p3_to_test = list(cls.odd_composites_p1p2p3_to_test)[:cls.TARGET_P1P2P3_COMPOSITES]


        # 7. Carmichael numbers
        cls.carmichael_numbers_to_test = [561, 1105, 1729, 2465, 2821, 6601, 8911]

        print(f"  Edge case primes: {len(cls.edge_case_primes_to_test)}")
        print(f"  Edge case composites: {len(cls.edge_case_composites_to_test)}")
        print(f"  Sieve primes: {len(cls.sieve_primes_to_test)}")
        print(f"  Even composites: {len(cls.even_composites_to_test)}")
        print(f"  Odd composites (p1*p2): {len(cls.odd_composites_p1p2_to_test)}")
        print(f"  Odd composites (p*p): {len(cls.odd_composites_p_square_to_test)}")
        print(f"  Odd composites (p1*p2*p3): {len(cls.odd_composites_p1p2p3_to_test)}")
        print(f"  Carmichael numbers: {len(cls.carmichael_numbers_to_test)}")
        total_tests = (len(cls.edge_case_primes_to_test) + len(cls.edge_case_composites_to_test) +
                       len(cls.sieve_primes_to_test) + len(cls.even_composites_to_test) +
                       len(cls.odd_composites_p1p2_to_test) + len(cls.odd_composites_p_square_to_test) +
                       len(cls.odd_composites_p1p2p3_to_test) + len(cls.carmichael_numbers_to_test))
        print(f"Total numbers prepared for testing: {total_tests}")
        print("Test data setup complete.")

    def test_edge_cases(self):
        """Test edge cases (0, 1, 2, 3, 4)."""
        for p in self.edge_case_primes_to_test:
            with self.subTest(num=p, type="prime"):
                self.assertTrue(millerrabinprimality(p, self.K_ITERATIONS_FOR_TEST), 
                                f"Edge case {p} should be prime.")
        for c in self.edge_case_composites_to_test:
            with self.subTest(num=c, type="composite"):
                self.assertFalse(millerrabinprimality(c, self.K_ITERATIONS_FOR_TEST),
                                 f"Edge case {c} should be composite.")

    def test_sieve_primes(self):
        """Test primes identified by Sieve of Eratosthenes."""
        for p in self.sieve_primes_to_test:
            with self.subTest(num=p):
                self.assertTrue(millerrabinprimality(p, self.K_ITERATIONS_FOR_TEST),
                                f"Sieve prime {p} should be prime.")

    def test_even_composites(self):
        """Test various even composite numbers."""
        for c in self.even_composites_to_test:
            with self.subTest(num=c):
                self.assertFalse(millerrabinprimality(c, self.K_ITERATIONS_FOR_TEST),
                                 f"Even composite {c} should be composite.")

    def test_odd_composites_product_two_primes(self):
        """Test odd composites formed by p1*p2."""
        for c in self.odd_composites_p1p2_to_test:
            with self.subTest(num=c):
                self.assertFalse(millerrabinprimality(c, self.K_ITERATIONS_FOR_TEST),
                                 f"Odd composite p1*p2 {c} should be composite.")

    def test_odd_composites_square_of_primes(self):
        """Test odd composites formed by p*p."""
        for c in self.odd_composites_p_square_to_test:
            with self.subTest(num=c):
                self.assertFalse(millerrabinprimality(c, self.K_ITERATIONS_FOR_TEST),
                                 f"Odd composite p*p {c} should be composite.")
                                 
    def test_odd_composites_product_three_primes(self):
        """Test odd composites formed by p1*p2*p3."""
        for c in self.odd_composites_p1p2p3_to_test:
            with self.subTest(num=c):
                self.assertFalse(millerrabinprimality(c, self.K_ITERATIONS_FOR_TEST),
                                 f"Odd composite p1*p2*p3 {c} should be composite.")

    def test_carmichael_numbers(self):
        """Test known Carmichael numbers (should be composite)."""
        for c in self.carmichael_numbers_to_test:
            with self.subTest(num=c):
                self.assertFalse(millerrabinprimality(c, self.K_ITERATIONS_FOR_TEST),
                                 f"Carmichael number {c} should be composite.")

if __name__ == '__main__':
    unittest.main()
