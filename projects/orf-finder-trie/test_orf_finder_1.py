from orf_finder import OrfFinder
import unittest
from time import time

start = time()

class TestOrfFinder(unittest.TestCase):
    def test_orf_finder(self):
        genome1 = OrfFinder("AAABBBCCC")
        test_cases = [
            (genome1.find("AAA", "BB"), ["AAABB", "AAABBB"]),
            (genome1.find("BB", "A"), []),
            (genome1.find("AA", "BC"), ["AABBBC", "AAABBBC"]),
            (genome1.find("A", "B"), ["AAAB", "AAABB", "AAABBB", "AAB", "AABB", "AABBB", "AB", "ABB", "ABBB"]),
            (genome1.find("AA", "A"), ["AAA"]),
            (genome1.find("AAAB", "BBB"), []),
            (genome1.find("B", "C"), ["BBBCCC", "BBBCC", "BBCCC", "BC", "BCC", "BBC", "BCCC", "BBBC", "BBCC"]),
        ]

        for i, (output, expected) in enumerate(test_cases, 1):
            with self.subTest(test=i):
                self.assertEqual(sorted(output), sorted(expected))

    def test_orf_finder_trie(self):
        genome2 = OrfFinder("BBAA")
        test_cases = [
            (genome2.find("B", "A"), ["BA", "BAA", "BBAA", "BBA"]),
            (genome2.find("BB", "AA"), ["BBAA"]),
            (genome2.find("A", "A"), ["AA"]),
            (genome2.find("BBA", "A"), ["BBAA"]),
            (genome2.find("A", "B"), []),
            (genome2.find("A", "AA"), []),
            (genome2.find("A", "BB"), []),
            (genome2.find("B", "AA"), ["BAA", "BBAA"]),
        ]
        for i, (output, expected) in enumerate(test_cases, 1):
            with self.subTest(test=i):
                self.assertEqual(sorted(output), sorted(expected))

    def test_orf_finder_trie_2(self):
        genome3 = OrfFinder("ABCABC")
        test_cases = [
            (genome3.find("A", "C"), ["ABC", "ABC", "ABCABC"]),
            (genome3.find("A", "B"), ["AB", "AB", "ABCAB"]),
            (genome3.find("B", "C"), ["BC", "BC", "BCABC"]),
            (genome3.find("C", "A"), ["CA"]),
            (genome3.find("AB", "C"), ["ABC", "ABC", "ABCABC"]),
            (genome3.find("C", "C"), ["CABC"]),
            (genome3.find("ABCABC", "ABCABC"), [])
        ]

        for i, (output, expected) in enumerate(test_cases, 1):
            with self.subTest(test=i):
                self.assertEqual(sorted(output), sorted(expected))

    def test_ord_finder_trie_3(self):
        genome4 = OrfFinder("DCBBBB")
        test_cases = [
            (genome4.find("B", "BB"), ["BBB", "BBB", "BBBB"])
        ]

        for i, (output, expected) in enumerate(test_cases, 1):
            with self.subTest(test=i):
                self.assertEqual(sorted(output), sorted(expected))



if __name__ == "__main__":
    unittest.main()
    print("All test cases passed :D.")
    print("Execution time: ", time()-start)