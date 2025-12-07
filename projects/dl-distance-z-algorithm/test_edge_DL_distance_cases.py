import unittest
from dl_distance import near_exact_pattern_matching as near_exact_pattern_matching
# from naive_dl_algorithm import validated_dl_matches as near_exact_pattern_matching

class TestFixedEdgeDLMatches(unittest.TestCase):
    def test_edge_case_0(self):
        text = 'abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab'
        pattern = 'ab'
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_1(self):
        text = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        pattern = 'aaa'
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_2(self):
        text = 'ababababababababababababababababababababababababababababababababababababababababababababababababababababababababab'
        pattern = 'ababab'
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_3(self):
        text = 'abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc'
        pattern = 'abc'
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_4(self):
        text = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        pattern = 'aa'
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_5(self):
        text = 'abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc'
        pattern = 'abcabc'
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_6(self):
        text = 'abababababababababababababababababababababababababababababababababababababababababababababababababababab'
        pattern = 'abab'
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_7(self):
        text = 'abcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabcabc'
        pattern = 'abc'
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_8(self):
        text = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        pattern = 'a'
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_9(self):
        text = 'ababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab'
        pattern = 'abab'
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_10(self):
        text = 'xai'
        pattern = 'xaizrubpbm'
        expected = []
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_11(self):
        text = 'ixc'
        pattern = 'ixcshshkmh'
        expected = []
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_12(self):
        text = 'rl'
        pattern = 'rlqvjihvcc'
        expected = []
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_13(self):
        text = 'myzzz'
        pattern = 'myzzzrdiso'
        expected = []
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_14(self):
        text = 'gtuz'
        pattern = 'gtuzmbzyvc'
        expected = []
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_15(self):
        text = 'q'
        pattern = 'qcwcrtoqwc'
        expected = []
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_16(self):
        text = 'x'
        pattern = 'xgyvmlozuj'
        expected = []
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_17(self):
        text = 'shp'
        pattern = 'shppefuqqw'
        expected = []
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_18(self):
        text = 'lnv'
        pattern = 'lnvldflgrj'
        expected = []
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_19(self):
        text = 'v'
        pattern = 'vobrjpehxf'
        expected = []
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_20(self):
        text = 'wawpyzestergarnckpnsxciwry'
        pattern = 'wawmkz'
        expected = []
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_21(self):
        text = 'kngsmmsrziwwnpbgyseezijocn'
        pattern = 'kygsmm'
        expected = [1]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_22(self):
        text = 'bpskffgrvjlfnkxtzzneviatgv'
        pattern = 'bpskrd'
        expected = []
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_23(self):
        text = 'paguencfhhitufkucxuqovvaly'
        pattern = 'pakuen'
        expected = [1]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_24(self):
        text = 'mogkgrefhxqdfhaihqnsjgxwst'
        pattern = 'mogkgk'
        expected = [1]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_25(self):
        text = 'lzawsjvnwhpnfhqejbqshjkkew'
        pattern = 'lzawaf'
        expected = []
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_26(self):
        text = 'peponuhouotxaoxqehgehmbpem'
        pattern = 'pepogn'
        expected = [1]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_27(self):
        text = 'pzvxierxugnkyrrxuodtdnsnoj'
        pattern = 'pzvzfe'
        expected = []
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_28(self):
        text = 'chlzudqifxfitarcpjiodspssc'
        pattern = 'phlzuf'
        expected = []
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_29(self):
        text = 'jqlqscqrtiqrqoyxbtqkwwkesb'
        pattern = 'jqgmsc'
        expected = []
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_30(self):
        text = 'xyzzptmyn'
        pattern = 'zptmyy'
        expected = [4]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_31(self):
        text = 'xyzjrwddl'
        pattern = 'jrwddh'
        expected = [4]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_32(self):
        text = 'xyzjxuncezz'
        pattern = 'jxuncs'
        expected = [4]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_33(self):
        text = 'xyzxhdkfezz'
        pattern = 'xhdkfh'
        expected = [4]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_34(self):
        text = 'xhtjpjhzz'
        pattern = 'htjpjg'
        expected = [2]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_35(self):
        text = 'xthnhqfy'
        pattern = 'thnhqs'
        expected = [2]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_36(self):
        text = 'xyjjjgy'
        pattern = 'xyjjjx'
        expected = [1]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_37(self):
        text = 'xgswaugy'
        pattern = 'gswaub'
        expected = [2]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_38(self):
        text = 'xrrxqjqy'
        pattern = 'rrxqja'
        expected = [2]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_39(self):
        text = 'xijietey'
        pattern = 'ijietk'
        expected = [2]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_40(self):
        text = 'pocrxpocrxpocrxpxdaaxrcoppocrx'
        pattern = 'pocrx'
        expected = [1, 2, 5, 6, 7, 10, 11, 12, 25, 26, 27]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_41(self):
        text = 'dmwbmdmwbmdmwbmgbzvxmbwmddmwbm'
        pattern = 'dmwbm'
        expected = [1, 2, 5, 6, 7, 10, 11, 12, 25, 26, 27]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_42(self):
        text = 'lkvkylkvkylkvkyldhhvykvkllkvky'
        pattern = 'lkvky'
        expected = [1, 2, 5, 6, 7, 10, 11, 12, 25, 26, 27]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_43(self):
        text = 'etxiyetxiyetxiywvovhyixteetxiy'
        pattern = 'etxiy'
        expected = [1, 2, 5, 6, 7, 10, 11, 12, 25, 26, 27]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_44(self):
        text = 'qfdpwqfdpwqfdpwiucgawpdfqqfdpw'
        pattern = 'qfdpw'
        expected = [1, 2, 5, 6, 7, 10, 11, 12, 25, 26, 27]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_45(self):
        text = 'xtskvxtskvxtskvcexeqvkstxxtskv'
        pattern = 'xtskv'
        expected = [1, 2, 5, 6, 7, 10, 11, 12, 25, 26, 27]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_46(self):
        text = 'jdijjjdijjjdijjmhypijjidjjdijj'
        pattern = 'jdijj'
        expected = [1, 2, 5, 6, 7, 10, 11, 12, 22, 25, 26, 27]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_47(self):
        text = 'wabwnwabwnwabwngjnucnwbawwabwn'
        pattern = 'wabwn'
        expected = [1, 2, 5, 6, 7, 10, 11, 12, 25, 26, 27]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_48(self):
        text = 'tbhbvtbhbvtbhbvmkkfivbhbttbhbv'
        pattern = 'tbhbv'
        expected = [1, 2, 5, 6, 7, 10, 11, 12, 25, 26, 27]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_49(self):
        text = 'acoxyacoxyacoxyinraayxocaacoxy'
        pattern = 'acoxy'
        expected = [1, 2, 5, 6, 7, 10, 11, 12, 25, 26, 27]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_50(self):
        text = 'aanydtestiozedvbfpjlrrhewwebnc'
        pattern = 'p'
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_51(self):
        text = 'xeudnyujyrbutgyfskswxkzslmqnkb'
        pattern = 'z'
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_52(self):
        text = 'coowpevbufecusdtxzwnwwrljaykjw'
        pattern = 'o'
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_53(self):
        text = 'zxknphzefofpxxkbeakbplfzqopqrb'
        pattern = 'f'
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_54(self):
        text = 'wnxsoxzsgkhhgnqmerdizadvakiptv'
        pattern = 'i'
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_55(self):
        text = 'kdwyiumuqquydnnsrfsukzrkpcyiac'
        pattern = 'j'
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_56(self):
        text = 'pagagfzalortyhcgvdvbuafhbyntls'
        pattern = 'm'
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_57(self):
        text = 'ojfnnfqipfrfjmmaloecwiizxiwnot'
        pattern = 'y'
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_58(self):
        text = 'upjltwrxkcgdosehxdbtyclizinmwy'
        pattern = 'd'
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_59(self):
        text = 'cfvlzzddahpucllytvdqlgbtvpmfuy'
        pattern = 'w'
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_60(self):
        text = 'iiiiiiiiiiiiiiiiiiiiiiiiiiii'
        pattern = 'iii'
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_61(self):
        text = 'llllllllllllllllllllll'
        pattern = 'll'
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_62(self):
        text = 'ggggggggggggggggggggg'
        pattern = 'gggg'
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_63(self):
        text = 'jjjjjjjjjjjjjjjjjjjjjjjjjj'
        pattern = 'jjjjj'
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_64(self):
        text = 'dddddddddddddddddddddddd'
        pattern = 'ddd'
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_65(self):
        text = 'yyyyyyyyyyyyyyyyyyyyyyyyy'
        pattern = 'yy'
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_66(self):
        text = 'ooooooooooooooooooooooooooo'
        pattern = 'ooo'
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_67(self):
        text = 'iiiiiiiiiiiiiiiiiiiiiiiii'
        pattern = 'ii'
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_68(self):
        text = 'hhhhhhhhhhhhhhhhhhhhh'
        pattern = 'hh'
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_69(self):
        text = 'gggggggggggggggggggggggggggggg'
        pattern = 'gggg'
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_70(self):
        text = ''
        pattern = 'qccp'
        expected = []
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_71(self):
        text = ''
        pattern = 'zrlq'
        expected = []
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_72(self):
        text = ''
        pattern = 'wsgm'
        expected = []
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_73(self):
        text = ''
        pattern = 'rjla'
        expected = []
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_74(self):
        text = ''
        pattern = 'hjzr'
        expected = []
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_75(self):
        text = ''
        pattern = 'tkgx'
        expected = []
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_76(self):
        text = ''
        pattern = 'dqnz'
        expected = []
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_77(self):
        text = ''
        pattern = 'pjoi'
        expected = []
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_78(self):
        text = ''
        pattern = 'yabk'
        expected = []
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_79(self):
        text = ''
        pattern = 'xqau'
        expected = []
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_edge_case_80(self):
        text = ''
        pattern = 'a'
        expected = []
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
