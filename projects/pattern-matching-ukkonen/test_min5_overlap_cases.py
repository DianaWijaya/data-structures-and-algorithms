import unittest
from suffix_tree_matching import SuffixTree

def pattern_match(text, pattern):
    tree = SuffixTree(text)
    return tree.search_exact(pattern)

class TestMin5OverlappingCases(unittest.TestCase):
    def test_min5_overlap_case_0(self):
        self.assertEqual(pattern_match('ppppppppppppp', 'pp'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_min5_overlap_case_1(self):
        self.assertEqual(pattern_match('jbjbjbjbjbjbjbjbjb', 'jbjb'), [0, 2, 4, 6, 8, 10, 12, 14])

    def test_min5_overlap_case_2(self):
        self.assertEqual(pattern_match('rderderderderderderderderderderderderderderder', 'rder'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42])

    def test_min5_overlap_case_3(self):
        self.assertEqual(pattern_match('zzzzzzzzzzzzzz', 'zz'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_min5_overlap_case_4(self):
        self.assertEqual(pattern_match('oohoohoohoohoohoohoohoohoohoohooho', 'ooho'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30])

    def test_min5_overlap_case_5(self):
        self.assertEqual(pattern_match('jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj', 'jjj'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32])

    def test_min5_overlap_case_6(self):
        self.assertEqual(pattern_match('iuiuiuiuiuiuiuiuiuiuiuiuiuiuiuiuiui', 'iui'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32])

    def test_min5_overlap_case_7(self):
        self.assertEqual(pattern_match('hkhkhkhkhkhkhkh', 'hkh'), [0, 2, 4, 6, 8, 10, 12])

    def test_min5_overlap_case_8(self):
        self.assertEqual(pattern_match('aaaaaaaaaaaaaaaaaaa', 'aa'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])

    def test_min5_overlap_case_9(self):
        self.assertEqual(pattern_match('ycycycycycycycycycycycycycy', 'ycy'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])

    def test_min5_overlap_case_10(self):
        self.assertEqual(pattern_match('avtavtavtavtavtavtavtavta', 'avta'), [0, 3, 6, 9, 12, 15, 18, 21])

    def test_min5_overlap_case_11(self):
        self.assertEqual(pattern_match('nwcnwcnwcnwcnwcnwcnwcnwcnwcnwcn', 'nwcn'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27])

    def test_min5_overlap_case_12(self):
        self.assertEqual(pattern_match('fycfycfycfycfycfycfycfycfycfycfycfycfycfycfycfycfycfycf', 'fycf'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51])

    def test_min5_overlap_case_13(self):
        self.assertEqual(pattern_match('ttttttt', 'tt'), [0, 1, 2, 3, 4, 5])

    def test_min5_overlap_case_14(self):
        self.assertEqual(pattern_match('fffffffffffffffff', 'ff'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_min5_overlap_case_15(self):
        self.assertEqual(pattern_match('dfpdfpdfpdfpdfpdfpdfpdfpdfpdfpdfpd', 'dfpd'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30])

    def test_min5_overlap_case_16(self):
        self.assertEqual(pattern_match('lllllllllll', 'll'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_min5_overlap_case_17(self):
        self.assertEqual(pattern_match('qxvcqxvcqxvcqxvcqxvcqxvcqxvcqxvcqxvcqxvcqxvcqxvcqxvcq', 'qxvcq'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48])

    def test_min5_overlap_case_18(self):
        self.assertEqual(pattern_match('xxxxxxxxxxxxxxxxxxx', 'xx'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])

    def test_min5_overlap_case_19(self):
        self.assertEqual(pattern_match('xyhkxyhkxyhkxyhkxyhkxyhkxyhkxyhkxyhkxyhkx', 'xyhkx'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36])

    def test_min5_overlap_case_20(self):
        self.assertEqual(pattern_match('pfeopfeopfeopfeopfeopfeopfeopfeopfeopfeopfeopfeopfeopfeopfeopfeop', 'pfeop'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60])

    def test_min5_overlap_case_21(self):
        self.assertEqual(pattern_match('uqruqruqruqruqruqruqruqruqruqruqru', 'uqru'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30])

    def test_min5_overlap_case_22(self):
        self.assertEqual(pattern_match('iiiiiiiiiiiiiiiii', 'ii'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_min5_overlap_case_23(self):
        self.assertEqual(pattern_match('hhhhhhhhhhhhhhhhhhh', 'hh'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])

    def test_min5_overlap_case_24(self):
        self.assertEqual(pattern_match('uuuuuuuuuuuuuuu', 'uu'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_min5_overlap_case_25(self):
        self.assertEqual(pattern_match('jfjpjfjpjfjpjfjpjfjpjfjpjfjpjfjpjfjpjfjpjfjpjfjpjfjpj', 'jfjpj'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48])

    def test_min5_overlap_case_26(self):
        self.assertEqual(pattern_match('trlcftrlcftrlcftrlcftrlcftrlcft', 'trlcft'), [0, 5, 10, 15, 20, 25])

    def test_min5_overlap_case_27(self):
        self.assertEqual(pattern_match('vuvuvuvuvuvuvuvuvuvuvuvuvuvuv', 'vuv'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26])

    def test_min5_overlap_case_28(self):
        self.assertEqual(pattern_match('nananananananan', 'nan'), [0, 2, 4, 6, 8, 10, 12])

    def test_min5_overlap_case_29(self):
        self.assertEqual(pattern_match('bbbbbbbbbbbb', 'bb'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_min5_overlap_case_30(self):
        self.assertEqual(pattern_match('lvlvlvlvlvlvlvlvlvlvlvlvlvlvlvl', 'lvl'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28])

    def test_min5_overlap_case_31(self):
        self.assertEqual(pattern_match('wwwwwwwwwwwwwwww', 'ww'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_min5_overlap_case_32(self):
        self.assertEqual(pattern_match('pypypypypypypypyp', 'pyp'), [0, 2, 4, 6, 8, 10, 12, 14])

    def test_min5_overlap_case_33(self):
        self.assertEqual(pattern_match('vvvvvvvvvvv', 'vv'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_min5_overlap_case_34(self):
        self.assertEqual(pattern_match('nnnnnnnnnnnnnnnnnnnn', 'nn'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    def test_min5_overlap_case_35(self):
        self.assertEqual(pattern_match('rwrwrwrwrwrwrwrwrwr', 'rwr'), [0, 2, 4, 6, 8, 10, 12, 14, 16])

    def test_min5_overlap_case_36(self):
        self.assertEqual(pattern_match('eeeeeeeeeeeeeeeeeee', 'ee'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])

    def test_min5_overlap_case_37(self):
        self.assertEqual(pattern_match('ggggggg', 'gg'), [0, 1, 2, 3, 4, 5])

    def test_min5_overlap_case_38(self):
        self.assertEqual(pattern_match('iosiosiosiosiosiosiosiosiosiosiosiosiosiosiosiosiosiosi', 'iosi'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51])

    def test_min5_overlap_case_39(self):
        self.assertEqual(pattern_match('tctctctctctctctctctctctctctctctctct', 'tct'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32])

    def test_min5_overlap_case_40(self):
        self.assertEqual(pattern_match('dfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfd', 'dfd'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])

    def test_min5_overlap_case_41(self):
        self.assertEqual(pattern_match('jlrjlrjlrjlrjlrjlrjlrjlrjlrjlrj', 'jlrj'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27])

    def test_min5_overlap_case_42(self):
        self.assertEqual(pattern_match('kkkkkkkkkkk', 'kk'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_min5_overlap_case_43(self):
        self.assertEqual(pattern_match('tynvvtynvvtynvvtynvvtynvvtynvvtynvvtynvvtynvvtynvvtynvvtynvvtynvvtynvvtynvvtynvvtynvvtynvvtynvvt', 'tynvvt'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90])

    def test_min5_overlap_case_44(self):
        self.assertEqual(pattern_match('aaaaaaa', 'aa'), [0, 1, 2, 3, 4, 5])

    def test_min5_overlap_case_45(self):
        self.assertEqual(pattern_match('mldjcmldjcmldjcmldjcmldjcmldjcmldjcmldjcmldjcm', 'mldjcm'), [0, 5, 10, 15, 20, 25, 30, 35, 40])

    def test_min5_overlap_case_46(self):
        self.assertEqual(pattern_match('dqdqdqdqdqdqdqdqdqdqdqdqdqdqdqdqdqdqdqdqd', 'dqd'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38])

    def test_min5_overlap_case_47(self):
        self.assertEqual(pattern_match('iriririririririririririririririri', 'iri'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])

    def test_min5_overlap_case_48(self):
        self.assertEqual(pattern_match('sssssssssssssssssssss', 'ss'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_min5_overlap_case_49(self):
        self.assertEqual(pattern_match('eeeeeeeeeeeeeeeee', 'ee'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_min5_overlap_case_50(self):
        self.assertEqual(pattern_match('xbwxbwxbwxbwxbwxbwxbwxbwx', 'xbwx'), [0, 3, 6, 9, 12, 15, 18, 21])

    def test_min5_overlap_case_51(self):
        self.assertEqual(pattern_match('kkkkkkkkkkkkkkk', 'kk'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_min5_overlap_case_52(self):
        self.assertEqual(pattern_match('cccccccccc', 'cc'), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_min5_overlap_case_53(self):
        self.assertEqual(pattern_match('obobobobobobobobo', 'obo'), [0, 2, 4, 6, 8, 10, 12, 14])

    def test_min5_overlap_case_54(self):
        self.assertEqual(pattern_match('xxxxxxxxxxxxxxxxxx', 'xx'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    def test_min5_overlap_case_55(self):
        self.assertEqual(pattern_match('fyyfyyfyyfyyfyyfyyfyyfyyfyyfyyfyyfyyfyyfyyfyyfyyfyyfyyfyyfyyf', 'fyyf'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57])

    def test_min5_overlap_case_56(self):
        self.assertEqual(pattern_match('bwjbwjbwjbwjbwjbwjbwjbwjbwjbwjb', 'bwjb'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27])

    def test_min5_overlap_case_57(self):
        self.assertEqual(pattern_match('dddddddddddddd', 'dd'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_min5_overlap_case_58(self):
        self.assertEqual(pattern_match('mmmmmmmmm', 'mm'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_min5_overlap_case_59(self):
        self.assertEqual(pattern_match('kymkymkymkymkymkymkymkymkymkymkymkymkymkymkymkymkymk', 'kymk'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48])

    def test_min5_overlap_case_60(self):
        self.assertEqual(pattern_match('huyhuyhuyhuyhuyhuyhuyhuyhuyhuyhuyh', 'huyh'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30])

    def test_min5_overlap_case_61(self):
        self.assertEqual(pattern_match('yyyyyyyyyyyyyyy', 'yy'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_min5_overlap_case_62(self):
        self.assertEqual(pattern_match('rplwjrplwjrplwjrplwjrplwjrplwjrplwjrplwjrplwjrplwjrplwjrplwjrplwjr', 'rplwjr'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])

    def test_min5_overlap_case_63(self):
        self.assertEqual(pattern_match('ffffffffffffffffff', 'ff'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    def test_min5_overlap_case_64(self):
        self.assertEqual(pattern_match('rdrdrdrdrdrdrdrdrdrdrdrdrdrdrdrdrdrdrdrdr', 'rdr'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38])

    def test_min5_overlap_case_65(self):
        self.assertEqual(pattern_match('cogcogcogcogcogcogcogcogcogcogcogcogcogcogcogcogcogcogcogcogc', 'cogc'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57])

    def test_min5_overlap_case_66(self):
        self.assertEqual(pattern_match('cuacuacuacuacuacuacuacuacuacuacuacuacuacuac', 'cuac'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39])

    def test_min5_overlap_case_67(self):
        self.assertEqual(pattern_match('xehxehxehxehxehxehxehx', 'xehx'), [0, 3, 6, 9, 12, 15, 18])

    def test_min5_overlap_case_68(self):
        self.assertEqual(pattern_match('kkkkkkkkkk', 'kk'), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_min5_overlap_case_69(self):
        self.assertEqual(pattern_match('clclclclclclclclclclclclclclclclclclc', 'clc'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34])

    def test_min5_overlap_case_70(self):
        self.assertEqual(pattern_match('yyyyyyyyyyyyyyyyy', 'yy'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_min5_overlap_case_71(self):
        self.assertEqual(pattern_match('mmmmmmmmmmm', 'mm'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_min5_overlap_case_72(self):
        self.assertEqual(pattern_match('ljtljtljtljtljtljtljtljtljtljtljtljtljtljtl', 'ljtl'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39])

    def test_min5_overlap_case_73(self):
        self.assertEqual(pattern_match('xyxyxyxyxyxyxyxyxyxyxyxyxyx', 'xyx'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])

    def test_min5_overlap_case_74(self):
        self.assertEqual(pattern_match('nnnnnnnnnnnnnnn', 'nn'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_min5_overlap_case_75(self):
        self.assertEqual(pattern_match('umhumhumhumhumhumhumhumhumhumhumhumhumhumhumhumhumhu', 'umhu'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48])

    def test_min5_overlap_case_76(self):
        self.assertEqual(pattern_match('wwwwwwwwwwwwwwwwwwww', 'ww'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    def test_min5_overlap_case_77(self):
        self.assertEqual(pattern_match('gobgobgobgobgobgobgobgobgobgobgobgobgobgobgobgobgobg', 'gobg'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48])

    def test_min5_overlap_case_78(self):
        self.assertEqual(pattern_match('oheoheoheoheoheoheoheoheoheoheoheoheoheoheo', 'oheo'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39])

    def test_min5_overlap_case_79(self):
        self.assertEqual(pattern_match('zezezezezezezezezezezezezezezezezezezez', 'zez'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36])

    def test_min5_overlap_case_80(self):
        self.assertEqual(pattern_match('rjzrjzrjzrjzrjzrjzrjzrjzrjzrjzrjzrjzrjzr', 'rjzr'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36])

    def test_min5_overlap_case_81(self):
        self.assertEqual(pattern_match('gtgtgtgtgtgtgtgtgtgtgtgtgtgtgtgtgtgtg', 'gtg'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34])

    def test_min5_overlap_case_82(self):
        self.assertEqual(pattern_match('lqxlqxlqxlqxlqxlqxlqxlqxlqxlqxlqxlqxlqxlqxlqxlqxlqxlqxlqxl', 'lqxl'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54])

    def test_min5_overlap_case_83(self):
        self.assertEqual(pattern_match('aaaaaaaaaaaaaaaaaaa', 'aa'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])

    def test_min5_overlap_case_84(self):
        self.assertEqual(pattern_match('otckotckotckotckotckotcko', 'otcko'), [0, 4, 8, 12, 16, 20])

    def test_min5_overlap_case_85(self):
        self.assertEqual(pattern_match('jyjyjyjyjyjyjyjyj', 'jyj'), [0, 2, 4, 6, 8, 10, 12, 14])

    def test_min5_overlap_case_86(self):
        self.assertEqual(pattern_match('lklklklklklklklkl', 'lkl'), [0, 2, 4, 6, 8, 10, 12, 14])

    def test_min5_overlap_case_87(self):
        self.assertEqual(pattern_match('qchqchqchqchqchqchqchqchqchqchqchq', 'qchq'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30])

    def test_min5_overlap_case_88(self):
        self.assertEqual(pattern_match('pipipipipipipipipipipipip', 'pip'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22])

    def test_min5_overlap_case_89(self):
        self.assertEqual(pattern_match('wygxwygxwygxwygxwygxwygxw', 'wygxw'), [0, 4, 8, 12, 16, 20])

    def test_min5_overlap_case_90(self):
        self.assertEqual(pattern_match('lqlqlqlqlqlqlqlqlqlqlqlqlqlqlqlqlqlql', 'lql'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34])

    def test_min5_overlap_case_91(self):
        self.assertEqual(pattern_match('jifpjifpjifpjifpjifpjifpjifpj', 'jifpj'), [0, 4, 8, 12, 16, 20, 24])

    def test_min5_overlap_case_92(self):
        self.assertEqual(pattern_match('hqqyrhqqyrhqqyrhqqyrhqqyrhqqyrhqqyrhqqyrhqqyrh', 'hqqyrh'), [0, 5, 10, 15, 20, 25, 30, 35, 40])

    def test_min5_overlap_case_93(self):
        self.assertEqual(pattern_match('dwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwd', 'dwd'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34])

    def test_min5_overlap_case_94(self):
        self.assertEqual(pattern_match('iiiiiiii', 'ii'), [0, 1, 2, 3, 4, 5, 6])

    def test_min5_overlap_case_95(self):
        self.assertEqual(pattern_match('hkghkghkghkghkghkghkghkghkghkghkghkghkghkgh', 'hkgh'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39])

    def test_min5_overlap_case_96(self):
        self.assertEqual(pattern_match('mnfmnfmnfmnfmnfmnfm', 'mnfm'), [0, 3, 6, 9, 12, 15])

    def test_min5_overlap_case_97(self):
        self.assertEqual(pattern_match('ddddddddddddddddd', 'dd'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_min5_overlap_case_98(self):
        self.assertEqual(pattern_match('ejgaejgaejgaejgaejgaejgaejgaejgaejgaejgaejgae', 'ejgae'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40])

    def test_min5_overlap_case_99(self):
        self.assertEqual(pattern_match('ewaewaewaewaewaewaewaewaewaewaewaewaewaewaewae', 'ewae'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42])

    def test_min5_overlap_case_100(self):
        self.assertEqual(pattern_match('abjabjabjabjabjabjabjabjabjabjabjabjabjabjabjabjabjabjabjabja', 'abja'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57])

    def test_min5_overlap_case_101(self):
        self.assertEqual(pattern_match('kyyofkyyofkyyofkyyofkyyofkyyofkyyofkyyofkyyofkyyofkyyofkyyofkyyofkyyofkyyofkyyofkyyofkyyofkyyofk', 'kyyofk'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90])

    def test_min5_overlap_case_102(self):
        self.assertEqual(pattern_match('vvvvvvvvvvvvvvvvvvv', 'vv'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])

    def test_min5_overlap_case_103(self):
        self.assertEqual(pattern_match('hhhhhhhhhhhhhhhhhhh', 'hh'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])

    def test_min5_overlap_case_104(self):
        self.assertEqual(pattern_match('nfgnfgnfgnfgnfgnfgnfgnfgnfgnfgnfgnfgnfgnfgnfgn', 'nfgn'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42])

    def test_min5_overlap_case_105(self):
        self.assertEqual(pattern_match('yyyyyyyy', 'yy'), [0, 1, 2, 3, 4, 5, 6])

    def test_min5_overlap_case_106(self):
        self.assertEqual(pattern_match('cbjcbjcbjcbjcbjcbjcbjcbjcbjcbjcbjcbjcbjcbjcbjcbjcbjc', 'cbjc'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48])

    def test_min5_overlap_case_107(self):
        self.assertEqual(pattern_match('ssssssssss', 'ss'), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_min5_overlap_case_108(self):
        self.assertEqual(pattern_match('fffffffffffffff', 'ff'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_min5_overlap_case_109(self):
        self.assertEqual(pattern_match('wyqgwyqgwyqgwyqgwyqgwyqgwyqgwyqgwyqgwyqgwyqgwyqgwyqgwyqgwyqgwyqgwyqgw', 'wyqgw'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64])

    def test_min5_overlap_case_110(self):
        self.assertEqual(pattern_match('cccccccccccccccccc', 'cc'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    def test_min5_overlap_case_111(self):
        self.assertEqual(pattern_match('hhhhhhhhhh', 'hh'), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_min5_overlap_case_112(self):
        self.assertEqual(pattern_match('xrxrxrxrxrxrxrxrxrx', 'xrx'), [0, 2, 4, 6, 8, 10, 12, 14, 16])

    def test_min5_overlap_case_113(self):
        self.assertEqual(pattern_match('aaaaaaaaa', 'aa'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_min5_overlap_case_114(self):
        self.assertEqual(pattern_match('jtzjtzjtzjtzjtzjtzjtzjtzjtzjtzjtzjtzj', 'jtzj'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33])

    def test_min5_overlap_case_115(self):
        self.assertEqual(pattern_match('lllllllllllll', 'll'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_min5_overlap_case_116(self):
        self.assertEqual(pattern_match('nynynynynynynynynynynynynynynynynynynyn', 'nyn'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36])

    def test_min5_overlap_case_117(self):
        self.assertEqual(pattern_match('ryicryicryicryicryicryicryicryicryicryicryicryicryicr', 'ryicr'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48])

    def test_min5_overlap_case_118(self):
        self.assertEqual(pattern_match('roewzroewzroewzroewzroewzroewzroewzroewzroewzroewzroewzroewzroewzroewzroewzroewzroewzroewzroewzr', 'roewzr'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90])

    def test_min5_overlap_case_119(self):
        self.assertEqual(pattern_match('jjjjjjjjjjjj', 'jj'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_min5_overlap_case_120(self):
        self.assertEqual(pattern_match('bbbbbbbbbbbbbbb', 'bb'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_min5_overlap_case_121(self):
        self.assertEqual(pattern_match('sssssssss', 'ss'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_min5_overlap_case_122(self):
        self.assertEqual(pattern_match('zazazazazazazazazazazazazazazazazazazaz', 'zaz'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36])

    def test_min5_overlap_case_123(self):
        self.assertEqual(pattern_match('bzjbzjbzjbzjbzjbzjbzjbzjbzjbzjbzjbzjbzjbzjbzjbzjb', 'bzjb'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45])

    def test_min5_overlap_case_124(self):
        self.assertEqual(pattern_match('qqqqqqqqqqqqqqqqqqqqqqqqqqq', 'qqq'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])

    def test_min5_overlap_case_125(self):
        self.assertEqual(pattern_match('zvzvzvzvzvzvzvzvzvzvzvzvzvzvzvzvz', 'zvz'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])

    def test_min5_overlap_case_126(self):
        self.assertEqual(pattern_match('dohbdohbdohbdohbdohbdohbdohbdohbdohbdohbd', 'dohbd'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36])

    def test_min5_overlap_case_127(self):
        self.assertEqual(pattern_match('tttttttttttttttttttt', 'tt'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    def test_min5_overlap_case_128(self):
        self.assertEqual(pattern_match('irpirpirpirpirpirpirpirpirpirpirpirpirpirpi', 'irpi'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39])

    def test_min5_overlap_case_129(self):
        self.assertEqual(pattern_match('memememememememememem', 'mem'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])

    def test_min5_overlap_case_130(self):
        self.assertEqual(pattern_match('nnnnnnnnnnnn', 'nn'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_min5_overlap_case_131(self):
        self.assertEqual(pattern_match('uuuuuuuuuu', 'uu'), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_min5_overlap_case_132(self):
        self.assertEqual(pattern_match('mmmmmmmmmmmmmmm', 'mm'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_min5_overlap_case_133(self):
        self.assertEqual(pattern_match('jjjjjjjjjjj', 'jj'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_min5_overlap_case_134(self):
        self.assertEqual(pattern_match('zzzzzzzzzzzz', 'zz'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_min5_overlap_case_135(self):
        self.assertEqual(pattern_match('aanaanaanaanaanaanaanaanaanaanaanaanaanaanaanaanaanaana', 'aana'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51])

    def test_min5_overlap_case_136(self):
        self.assertEqual(pattern_match('txezmtxezmtxezmtxezmtxezmtxezmtxezmtxezmtxezmtxezmtxezmtxezmt', 'txezmt'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55])

    def test_min5_overlap_case_137(self):
        self.assertEqual(pattern_match('jyjyjyjyjyjyjyjyjyjyjyjyjyjyjyjyjyj', 'jyj'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32])

    def test_min5_overlap_case_138(self):
        self.assertEqual(pattern_match('dugdugdugdugdugdugdugdugdugdugdugdugdugdugd', 'dugd'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39])

    def test_min5_overlap_case_139(self):
        self.assertEqual(pattern_match('fffffffffff', 'ff'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_min5_overlap_case_140(self):
        self.assertEqual(pattern_match('gpgpgpgpgpgpgpgpgpgpgpgpgpgpgpgpg', 'gpg'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])

    def test_min5_overlap_case_141(self):
        self.assertEqual(pattern_match('oooooooooo', 'oo'), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_min5_overlap_case_142(self):
        self.assertEqual(pattern_match('sssssssssssss', 'ss'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_min5_overlap_case_143(self):
        self.assertEqual(pattern_match('ppppppppppppppp', 'pp'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_min5_overlap_case_144(self):
        self.assertEqual(pattern_match('aqxgaqxgaqxgaqxgaqxgaqxgaqxgaqxgaqxgaqxgaqxgaqxgaqxgaqxgaqxgaqxgaqxgaqxgaqxgaqxga', 'aqxga'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76])

    def test_min5_overlap_case_145(self):
        self.assertEqual(pattern_match('kkkkkkkkkkkkkkkkkkkkk', 'kk'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_min5_overlap_case_146(self):
        self.assertEqual(pattern_match('hhhhhhh', 'hh'), [0, 1, 2, 3, 4, 5])

    def test_min5_overlap_case_147(self):
        self.assertEqual(pattern_match('ayrayrayrayrayrayrayrayrayrayrayrayrayrayrayrayrayrayra', 'ayra'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51])

    def test_min5_overlap_case_148(self):
        self.assertEqual(pattern_match('hsdhsdhsdhsdhsdhsdhsdhsdhsdhsdhsdh', 'hsdh'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30])

    def test_min5_overlap_case_149(self):
        self.assertEqual(pattern_match('grtdgrtdgrtdgrtdgrtdgrtdgrtdgrtdgrtdgrtdgrtdgrtdgrtdgrtdgrtdgrtdg', 'grtdg'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60])

    def test_min5_overlap_case_150(self):
        self.assertEqual(pattern_match('tpjmtpjmtpjmtpjmtpjmtpjmtpjmtpjmtpjmtpjmtpjmtpjmtpjmt', 'tpjmt'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48])

    def test_min5_overlap_case_151(self):
        self.assertEqual(pattern_match('maemaemaemaemaemaemaemaemaemaemaemaemaemaem', 'maem'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39])

    def test_min5_overlap_case_152(self):
        self.assertEqual(pattern_match('papapapapapapapapapapapapapapapapapap', 'pap'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34])

    def test_min5_overlap_case_153(self):
        self.assertEqual(pattern_match('ffffffffffff', 'ff'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_min5_overlap_case_154(self):
        self.assertEqual(pattern_match('dkdkdkdkdkdkdkdkdkdkd', 'dkd'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])

    def test_min5_overlap_case_155(self):
        self.assertEqual(pattern_match('rjfrjfrjfrjfrjfrjfrjfrjfrjfr', 'rjfr'), [0, 3, 6, 9, 12, 15, 18, 21, 24])

    def test_min5_overlap_case_156(self):
        self.assertEqual(pattern_match('uuuuuuuuuuuuuuuuu', 'uu'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_min5_overlap_case_157(self):
        self.assertEqual(pattern_match('dfmkdfmkdfmkdfmkdfmkdfmkdfmkdfmkdfmkdfmkdfmkdfmkdfmkdfmkdfmkdfmkdfmkd', 'dfmkd'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64])

    def test_min5_overlap_case_158(self):
        self.assertEqual(pattern_match('hschschschschschschschschsch', 'hsch'), [0, 3, 6, 9, 12, 15, 18, 21, 24])

    def test_min5_overlap_case_159(self):
        self.assertEqual(pattern_match('zzzzzzzzzzzzzzzzzzzz', 'zz'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    def test_min5_overlap_case_160(self):
        self.assertEqual(pattern_match('hhhhhhhhhhhhh', 'hh'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_min5_overlap_case_161(self):
        self.assertEqual(pattern_match('yyyyyyyyyyyyy', 'yy'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_min5_overlap_case_162(self):
        self.assertEqual(pattern_match('rrrrrrrrrrrr', 'rr'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_min5_overlap_case_163(self):
        self.assertEqual(pattern_match('isaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisaisai', 'isai'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54])

    def test_min5_overlap_case_164(self):
        self.assertEqual(pattern_match('zzzzzzz', 'zz'), [0, 1, 2, 3, 4, 5])

    def test_min5_overlap_case_165(self):
        self.assertEqual(pattern_match('nnnnnnnnnnnnnnnnnnnn', 'nn'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    def test_min5_overlap_case_166(self):
        self.assertEqual(pattern_match('cffxcffxcffxcffxcffxcffxcffxcffxc', 'cffxc'), [0, 4, 8, 12, 16, 20, 24, 28])

    def test_min5_overlap_case_167(self):
        self.assertEqual(pattern_match('cccccccccccccccccc', 'cc'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    def test_min5_overlap_case_168(self):
        self.assertEqual(pattern_match('hmbhmbhmbhmbhmbhmbhmbhmbhmbhmbhmbhmbhmbhmbhmbhmbh', 'hmbh'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45])

    def test_min5_overlap_case_169(self):
        self.assertEqual(pattern_match('qkpwqkpwqkpwqkpwqkpwqkpwqkpwqkpwqkpwqkpwqkpwqkpwqkpwqkpwqkpwqkpwqkpwq', 'qkpwq'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64])

    def test_min5_overlap_case_170(self):
        self.assertEqual(pattern_match('ogogogogogogogogogogogogogogogo', 'ogo'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28])

    def test_min5_overlap_case_171(self):
        self.assertEqual(pattern_match('jjrcjjrcjjrcjjrcjjrcjjrcjjrcjjrcjjrcjjrcjjrcj', 'jjrcj'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40])

    def test_min5_overlap_case_172(self):
        self.assertEqual(pattern_match('uvghtuvghtuvghtuvghtuvghtuvghtuvghtuvghtuvghtuvghtuvghtu', 'uvghtu'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50])

    def test_min5_overlap_case_173(self):
        self.assertEqual(pattern_match('lllllllll', 'll'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_min5_overlap_case_174(self):
        self.assertEqual(pattern_match('xpsxpsxpsxpsxpsxpsxpsxpsxpsxpsxpsxpsxpsxpsxpsxpsxpsxpsx', 'xpsx'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51])

    def test_min5_overlap_case_175(self):
        self.assertEqual(pattern_match('vzavzavzavzavzavzavzavzav', 'vzav'), [0, 3, 6, 9, 12, 15, 18, 21])

    def test_min5_overlap_case_176(self):
        self.assertEqual(pattern_match('qmqmqmqmqmqmqmqmqmqmqmqmqmqmqmq', 'qmq'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28])

    def test_min5_overlap_case_177(self):
        self.assertEqual(pattern_match('zthxyzthxyzthxyzthxyzthxyzthxyzthxyzthxyzthxyzthxyzthxyzthxyzthxyzthxyzthxyz', 'zthxyz'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70])

    def test_min5_overlap_case_178(self):
        self.assertEqual(pattern_match('jyljyljyljyljyljyljyljyljyljyljyljyljyljyljylj', 'jylj'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42])

    def test_min5_overlap_case_179(self):
        self.assertEqual(pattern_match('icyicyicyicyicyicyicyicyicyicyicyicyicyicyicyicyicyicyicyi', 'icyi'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54])

    def test_min5_overlap_case_180(self):
        self.assertEqual(pattern_match('dodododododododod', 'dod'), [0, 2, 4, 6, 8, 10, 12, 14])

    def test_min5_overlap_case_181(self):
        self.assertEqual(pattern_match('vlxkvlxkvlxkvlxkvlxkvlxkvlxkvlxkvlxkvlxkv', 'vlxkv'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36])

    def test_min5_overlap_case_182(self):
        self.assertEqual(pattern_match('yncvyncvyncvyncvyncvyncvyncvyncvy', 'yncvy'), [0, 4, 8, 12, 16, 20, 24, 28])

    def test_min5_overlap_case_183(self):
        self.assertEqual(pattern_match('nnnnnnnnnnnn', 'nn'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_min5_overlap_case_184(self):
        self.assertEqual(pattern_match('iiiiiii', 'ii'), [0, 1, 2, 3, 4, 5])

    def test_min5_overlap_case_185(self):
        self.assertEqual(pattern_match('ddddddd', 'dd'), [0, 1, 2, 3, 4, 5])

    def test_min5_overlap_case_186(self):
        self.assertEqual(pattern_match('wwwwwwwwwwwwww', 'ww'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_min5_overlap_case_187(self):
        self.assertEqual(pattern_match('kkkkkkkkkkkkkkkkk', 'kk'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_min5_overlap_case_188(self):
        self.assertEqual(pattern_match('eeeeeee', 'ee'), [0, 1, 2, 3, 4, 5])

    def test_min5_overlap_case_189(self):
        self.assertEqual(pattern_match('riqriqriqriqriqriqriqriqriqriqriqriqr', 'riqr'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33])

    def test_min5_overlap_case_190(self):
        self.assertEqual(pattern_match('uuuuuuuuuu', 'uu'), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_min5_overlap_case_191(self):
        self.assertEqual(pattern_match('pepepepepepep', 'pep'), [0, 2, 4, 6, 8, 10])

    def test_min5_overlap_case_192(self):
        self.assertEqual(pattern_match('dpjgrdpjgrdpjgrdpjgrdpjgrdpjgrdpjgrdpjgrdpjgrdpjgrdpjgrdpjgrdpjgrdpjgrdpjgrdpjgrdpjgrdpjgrd', 'dpjgrd'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85])

    def test_min5_overlap_case_193(self):
        self.assertEqual(pattern_match('klklklklklklklklklklk', 'klk'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])

    def test_min5_overlap_case_194(self):
        self.assertEqual(pattern_match('uqxduqxduqxduqxduqxduqxduqxduqxduqxduqxduqxduqxduqxduqxduqxdu', 'uqxdu'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56])

    def test_min5_overlap_case_195(self):
        self.assertEqual(pattern_match('hhhhhhhhhhhhhh', 'hh'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_min5_overlap_case_196(self):
        self.assertEqual(pattern_match('zzzzzzzzzzzzz', 'zz'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_min5_overlap_case_197(self):
        self.assertEqual(pattern_match('eeeeeeeeeeeeeeeeeeee', 'ee'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    def test_min5_overlap_case_198(self):
        self.assertEqual(pattern_match('xvyxvyxvyxvyxvyxvyxvyxvyxvyxvyxvyx', 'xvyx'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30])

    def test_min5_overlap_case_199(self):
        self.assertEqual(pattern_match('ssssssssssssssssssss', 'ss'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    def test_min5_overlap_case_200(self):
        self.assertEqual(pattern_match('agagagagagagagagagagagagagagagagagagaga', 'aga'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36])

    def test_min5_overlap_case_201(self):
        self.assertEqual(pattern_match('krmfhkrmfhkrmfhkrmfhkrmfhkrmfhkrmfhkrmfhkrmfhkrmfhkrmfhkrmfhkrmfhkrmfhkrmfhkrmfhkrmfhkrmfhkrmfhk', 'krmfhk'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90])

    def test_min5_overlap_case_202(self):
        self.assertEqual(pattern_match('cccccccccccccccc', 'cc'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_min5_overlap_case_203(self):
        self.assertEqual(pattern_match('lzqyblzqyblzqyblzqyblzqyblzqyblzqybl', 'lzqybl'), [0, 5, 10, 15, 20, 25, 30])

    def test_min5_overlap_case_204(self):
        self.assertEqual(pattern_match('fffffffffffff', 'ff'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_min5_overlap_case_205(self):
        self.assertEqual(pattern_match('vgvgvgvgvgvgvgvgv', 'vgv'), [0, 2, 4, 6, 8, 10, 12, 14])

    def test_min5_overlap_case_206(self):
        self.assertEqual(pattern_match('tftftftftftftftftftftftftftf', 'tftf'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])

    def test_min5_overlap_case_207(self):
        self.assertEqual(pattern_match('jifjifjifjifjifjifjifjifjifjifjifjifj', 'jifj'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33])

    def test_min5_overlap_case_208(self):
        self.assertEqual(pattern_match('iiiiiiiiiiiiiiiiiiii', 'ii'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    def test_min5_overlap_case_209(self):
        self.assertEqual(pattern_match('zzzzzzzzzzzzzzz', 'zzz'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_min5_overlap_case_210(self):
        self.assertEqual(pattern_match('ylqylqylqylqylqylqylqylqylqylqylqy', 'ylqy'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30])

    def test_min5_overlap_case_211(self):
        self.assertEqual(pattern_match('kukukukukukukukukukukukuk', 'kuk'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22])

    def test_min5_overlap_case_212(self):
        self.assertEqual(pattern_match('xgkxgkxgkxgkxgkxgkxgkxgkxgkxgkxgkx', 'xgkx'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30])

    def test_min5_overlap_case_213(self):
        self.assertEqual(pattern_match('kkkkkkk', 'kk'), [0, 1, 2, 3, 4, 5])

    def test_min5_overlap_case_214(self):
        self.assertEqual(pattern_match('ddddddddd', 'dd'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_min5_overlap_case_215(self):
        self.assertEqual(pattern_match('rrrrrrrrrrrrrrrr', 'rr'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_min5_overlap_case_216(self):
        self.assertEqual(pattern_match('retretretretretretretretretretretretretr', 'retr'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36])

    def test_min5_overlap_case_217(self):
        self.assertEqual(pattern_match('iiiiiiiiiiiiiiii', 'iii'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_min5_overlap_case_218(self):
        self.assertEqual(pattern_match('hdhdhdhdhdhdhdhdhdhdhdhdhdhdhdhdhdhdhdhdh', 'hdh'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38])

    def test_min5_overlap_case_219(self):
        self.assertEqual(pattern_match('bysbysbysbysbysbysbysbysbysb', 'bysb'), [0, 3, 6, 9, 12, 15, 18, 21, 24])

    def test_min5_overlap_case_220(self):
        self.assertEqual(pattern_match('ggggggg', 'gg'), [0, 1, 2, 3, 4, 5])

    def test_min5_overlap_case_221(self):
        self.assertEqual(pattern_match('ddddddddddddddd', 'dd'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_min5_overlap_case_222(self):
        self.assertEqual(pattern_match('tttttttttttttttttttt', 'tt'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    def test_min5_overlap_case_223(self):
        self.assertEqual(pattern_match('zszszszszszsz', 'zsz'), [0, 2, 4, 6, 8, 10])

    def test_min5_overlap_case_224(self):
        self.assertEqual(pattern_match('vvvvvvvvvv', 'vv'), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_min5_overlap_case_225(self):
        self.assertEqual(pattern_match('nutbrnutbrnutbrnutbrnutbrnutbrn', 'nutbrn'), [0, 5, 10, 15, 20, 25])

    def test_min5_overlap_case_226(self):
        self.assertEqual(pattern_match('mmmmmmmmmm', 'mm'), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_min5_overlap_case_227(self):
        self.assertEqual(pattern_match('cyzgcyzgcyzgcyzgcyzgcyzgcyzgcyzgcyzgcyzgcyzgcyzgcyzgcyzgc', 'cyzgc'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52])

    def test_min5_overlap_case_228(self):
        self.assertEqual(pattern_match('uuuuuuuuuuuuuuuuuuuuu', 'uu'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_min5_overlap_case_229(self):
        self.assertEqual(pattern_match('hhhhhhhhhhhhhhhhhhhhh', 'hh'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_min5_overlap_case_230(self):
        self.assertEqual(pattern_match('edzedzedzedzedzedzedzedzedzedzedzedzedzedzedze', 'edze'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42])

    def test_min5_overlap_case_231(self):
        self.assertEqual(pattern_match('zzzzzzzzzzzzzzzzz', 'zz'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_min5_overlap_case_232(self):
        self.assertEqual(pattern_match('ttttttttttttt', 'tt'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_min5_overlap_case_233(self):
        self.assertEqual(pattern_match('jjjjjjjj', 'jj'), [0, 1, 2, 3, 4, 5, 6])

    def test_min5_overlap_case_234(self):
        self.assertEqual(pattern_match('dmlndmlndmlndmlndmlndmlndmlndmlndmlndmlndmlndmlndmlnd', 'dmlnd'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48])

    def test_min5_overlap_case_235(self):
        self.assertEqual(pattern_match('ssssssssssssss', 'ss'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_min5_overlap_case_236(self):
        self.assertEqual(pattern_match('gbgbgbgbgbgbgbgbg', 'gbg'), [0, 2, 4, 6, 8, 10, 12, 14])

    def test_min5_overlap_case_237(self):
        self.assertEqual(pattern_match('bejwbejwbejwbejwbejwbejwbejwbejwbejwbejwbejwbejwb', 'bejwb'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44])

    def test_min5_overlap_case_238(self):
        self.assertEqual(pattern_match('jjjjjjjjjjjjjjj', 'jj'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_min5_overlap_case_239(self):
        self.assertEqual(pattern_match('nxxnxxnxxnxxnxxnxxnxxnxxnxxnxxn', 'nxxn'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27])

    def test_min5_overlap_case_240(self):
        self.assertEqual(pattern_match('uuyfuuyfuuyfuuyfuuyfuuyfuuyfuuyfu', 'uuyfu'), [0, 4, 8, 12, 16, 20, 24, 28])

    def test_min5_overlap_case_241(self):
        self.assertEqual(pattern_match('mmmmmmmmm', 'mm'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_min5_overlap_case_242(self):
        self.assertEqual(pattern_match('ggggggggggggggg', 'gg'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_min5_overlap_case_243(self):
        self.assertEqual(pattern_match('zpzpzpzpzpzpzpzpzpzpzpzpzpzpz', 'zpz'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26])

    def test_min5_overlap_case_244(self):
        self.assertEqual(pattern_match('palpalpalpalpalpalpalpalpalpalpalpalpalp', 'palp'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36])

    def test_min5_overlap_case_245(self):
        self.assertEqual(pattern_match('eeeeeeeeeeeeee', 'ee'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_min5_overlap_case_246(self):
        self.assertEqual(pattern_match('uuuuuuuuuuuuuuuuu', 'uuu'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_min5_overlap_case_247(self):
        self.assertEqual(pattern_match('kkkkkkkkk', 'kk'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_min5_overlap_case_248(self):
        self.assertEqual(pattern_match('jjjjjjjjjjjjjjjj', 'jj'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_min5_overlap_case_249(self):
        self.assertEqual(pattern_match('jmwjmwjmwjmwjmwjmwjmwjmwjmwjmwjmwjmwjmwjmwjmwjmwjmwj', 'jmwj'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48])

    def test_min5_overlap_case_250(self):
        self.assertEqual(pattern_match('dsmdsmdsmdsmdsmdsmdsmdsmdsmdsmdsmdsmdsmd', 'dsmd'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36])

    def test_min5_overlap_case_251(self):
        self.assertEqual(pattern_match('jqvmkjqvmkjqvmkjqvmkjqvmkjqvmkjqvmkjqvmkjqvmkjqvmkjqvmkjqvmkjqvmkjqvmkj', 'jqvmkj'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65])

    def test_min5_overlap_case_252(self):
        self.assertEqual(pattern_match('ooooooooooooooooooooo', 'oo'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_min5_overlap_case_253(self):
        self.assertEqual(pattern_match('repreprepreprepreprepreprepreprepreprepreprepreprepreprepr', 'repr'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54])

    def test_min5_overlap_case_254(self):
        self.assertEqual(pattern_match('xxxxxxx', 'xx'), [0, 1, 2, 3, 4, 5])

    def test_min5_overlap_case_255(self):
        self.assertEqual(pattern_match('hhhhhhh', 'hh'), [0, 1, 2, 3, 4, 5])

    def test_min5_overlap_case_256(self):
        self.assertEqual(pattern_match('oeoeoeoeoeoeoeoeoeo', 'oeo'), [0, 2, 4, 6, 8, 10, 12, 14, 16])

    def test_min5_overlap_case_257(self):
        self.assertEqual(pattern_match('otototototototototototototototototototo', 'oto'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36])

    def test_min5_overlap_case_258(self):
        self.assertEqual(pattern_match('lgiplgiplgiplgiplgiplgipl', 'lgipl'), [0, 4, 8, 12, 16, 20])

    def test_min5_overlap_case_259(self):
        self.assertEqual(pattern_match('hzdxhzdxhzdxhzdxhzdxhzdxhzdxhzdxhzdxh', 'hzdxh'), [0, 4, 8, 12, 16, 20, 24, 28, 32])

    def test_min5_overlap_case_260(self):
        self.assertEqual(pattern_match('aaaaaaaaaaaaaa', 'aa'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_min5_overlap_case_261(self):
        self.assertEqual(pattern_match('tawtawtawtawtawtawtawtawtawtawtawt', 'tawt'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30])

    def test_min5_overlap_case_262(self):
        self.assertEqual(pattern_match('qqqqqqqqqqqq', 'qq'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_min5_overlap_case_263(self):
        self.assertEqual(pattern_match('tfmtfmtfmtfmtfmtfmtfmtfmtfmtfmtfmt', 'tfmt'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30])

    def test_min5_overlap_case_264(self):
        self.assertEqual(pattern_match('ppoaxppoaxppoaxppoaxppoaxppoaxppoaxppoaxppoaxppoaxppoaxppoaxppoaxppoaxppoaxppoaxppoaxppoaxppoaxppoaxp', 'ppoaxp'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95])

    def test_min5_overlap_case_265(self):
        self.assertEqual(pattern_match('yjyjyjyjyjyjyjyjyjyjyjyjyjyjyjyjyjyjyjyjy', 'yjy'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38])

    def test_min5_overlap_case_266(self):
        self.assertEqual(pattern_match('aaaaaaaaaaaaaaaaaaaaa', 'aa'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_min5_overlap_case_267(self):
        self.assertEqual(pattern_match('oooooooooo', 'oo'), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_min5_overlap_case_268(self):
        self.assertEqual(pattern_match('mmmmmmmmmmmm', 'mm'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_min5_overlap_case_269(self):
        self.assertEqual(pattern_match('nnnnnnnnn', 'nn'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_min5_overlap_case_270(self):
        self.assertEqual(pattern_match('ssssssssssssssssssssssssssssssssss', 'ssss'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])

    def test_min5_overlap_case_271(self):
        self.assertEqual(pattern_match('jjjjjjjjjjjjjjj', 'jj'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_min5_overlap_case_272(self):
        self.assertEqual(pattern_match('fzxfzxfzxfzxfzxfzxfzxfzxfzxfzxfzxfzxfzxfzxf', 'fzxf'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39])

    def test_min5_overlap_case_273(self):
        self.assertEqual(pattern_match('cccccccccccc', 'cc'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_min5_overlap_case_274(self):
        self.assertEqual(pattern_match('wrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrw', 'wrw'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34])

    def test_min5_overlap_case_275(self):
        self.assertEqual(pattern_match('icgicgicgicgicgicgicgicgicgicgicgicgicgicgicgi', 'icgi'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42])

    def test_min5_overlap_case_276(self):
        self.assertEqual(pattern_match('ogargogargogargogargogargogargogargo', 'ogargo'), [0, 5, 10, 15, 20, 25, 30])

    def test_min5_overlap_case_277(self):
        self.assertEqual(pattern_match('vgjvgjvgjvgjvgjvgjvgjvgjvgjvgjvgjvgjv', 'vgjv'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33])

    def test_min5_overlap_case_278(self):
        self.assertEqual(pattern_match('gggggggggg', 'gg'), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_min5_overlap_case_279(self):
        self.assertEqual(pattern_match('rsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsr', 'rsr'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34])

    def test_min5_overlap_case_280(self):
        self.assertEqual(pattern_match('yvmpyvmpyvmpyvmpyvmpyvmpyvmpy', 'yvmpy'), [0, 4, 8, 12, 16, 20, 24])

    def test_min5_overlap_case_281(self):
        self.assertEqual(pattern_match('ooooooooooooooo', 'oo'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_min5_overlap_case_282(self):
        self.assertEqual(pattern_match('yzkzgyzkzgyzkzgyzkzgyzkzgyzkzgyzkzgyzkzgyzkzgyzkzgyzkzgyzkzgyzkzgyzkzgyzkzgyzkzgyzkzgy', 'yzkzgy'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80])

    def test_min5_overlap_case_283(self):
        self.assertEqual(pattern_match('nnnnnnnnnnnnnnnnnnn', 'nn'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])

    def test_min5_overlap_case_284(self):
        self.assertEqual(pattern_match('cccccccccccccccccccc', 'cc'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    def test_min5_overlap_case_285(self):
        self.assertEqual(pattern_match('iiiiiiiiiiiiiiiiiiii', 'ii'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    def test_min5_overlap_case_286(self):
        self.assertEqual(pattern_match('jjjjjjjjj', 'jj'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_min5_overlap_case_287(self):
        self.assertEqual(pattern_match('ddddddd', 'dd'), [0, 1, 2, 3, 4, 5])

    def test_min5_overlap_case_288(self):
        self.assertEqual(pattern_match('aaaaaaaaaaaaa', 'aa'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_min5_overlap_case_289(self):
        self.assertEqual(pattern_match('zzzzzzz', 'zz'), [0, 1, 2, 3, 4, 5])

    def test_min5_overlap_case_290(self):
        self.assertEqual(pattern_match('ffffffffff', 'ff'), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_min5_overlap_case_291(self):
        self.assertEqual(pattern_match('vvvvvvvvvvvvvvvvvvvvv', 'vv'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_min5_overlap_case_292(self):
        self.assertEqual(pattern_match('hhhhhhhhhh', 'hh'), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_min5_overlap_case_293(self):
        self.assertEqual(pattern_match('jdjdjdjdjdjdjdjdjdjdjdj', 'jdj'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

    def test_min5_overlap_case_294(self):
        self.assertEqual(pattern_match('nrnrnrnrnrnrnrnrnrnrnrnrn', 'nrn'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22])

    def test_min5_overlap_case_295(self):
        self.assertEqual(pattern_match('dpstdpstdpstdpstdpstdpstdpstdpstdpstdpstdpstdpstdpstdpstdpstdpstdpstdpstd', 'dpstd'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68])

    def test_min5_overlap_case_296(self):
        self.assertEqual(pattern_match('cccccccccccc', 'cc'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_min5_overlap_case_297(self):
        self.assertEqual(pattern_match('uuuuuuuuuuuuuu', 'uu'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_min5_overlap_case_298(self):
        self.assertEqual(pattern_match('euxeuxeuxeuxeuxeuxeuxe', 'euxe'), [0, 3, 6, 9, 12, 15, 18])

    def test_min5_overlap_case_299(self):
        self.assertEqual(pattern_match('pppppppppppppppp', 'pp'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_min5_overlap_case_300(self):
        self.assertEqual(pattern_match('tttttttttttttttt', 'tt'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_min5_overlap_case_301(self):
        self.assertEqual(pattern_match('gugugugugugugugugugugugugugugugug', 'gug'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])

    def test_min5_overlap_case_302(self):
        self.assertEqual(pattern_match('mmmmmmmmmmmmmmmmm', 'mm'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_min5_overlap_case_303(self):
        self.assertEqual(pattern_match('xxxxxxxxxxxxx', 'xx'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_min5_overlap_case_304(self):
        self.assertEqual(pattern_match('eeeeeeeeeeeeeeeeeeeeeeeeeeeee', 'eee'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26])

    def test_min5_overlap_case_305(self):
        self.assertEqual(pattern_match('bbbbbbb', 'bb'), [0, 1, 2, 3, 4, 5])

    def test_min5_overlap_case_306(self):
        self.assertEqual(pattern_match('eeeeeeeeeeeeeee', 'ee'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_min5_overlap_case_307(self):
        self.assertEqual(pattern_match('mvmvmvmvmvmvmvmvmvmvmvmvmvmvmvmvmvmvmvm', 'mvm'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36])

    def test_min5_overlap_case_308(self):
        self.assertEqual(pattern_match('jywljywljywljywljywljywljywljywljywlj', 'jywlj'), [0, 4, 8, 12, 16, 20, 24, 28, 32])

    def test_min5_overlap_case_309(self):
        self.assertEqual(pattern_match('ssssssssssssssss', 'ss'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_min5_overlap_case_310(self):
        self.assertEqual(pattern_match('gegegegegegegegegeg', 'geg'), [0, 2, 4, 6, 8, 10, 12, 14, 16])

    def test_min5_overlap_case_311(self):
        self.assertEqual(pattern_match('ffffffff', 'ff'), [0, 1, 2, 3, 4, 5, 6])

    def test_min5_overlap_case_312(self):
        self.assertEqual(pattern_match('gergagergagergagergagergagergagergagergagergagergagergagergagergagergagergagergagergagergagergagergag', 'gergag'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95])

    def test_min5_overlap_case_313(self):
        self.assertEqual(pattern_match('hhhhhhhh', 'hh'), [0, 1, 2, 3, 4, 5, 6])

    def test_min5_overlap_case_314(self):
        self.assertEqual(pattern_match('bibibibibibibibibibibibibibibibib', 'bib'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])

    def test_min5_overlap_case_315(self):
        self.assertEqual(pattern_match('kkkkkkkkkkkkkkkkkkkkkk', 'kkk'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_min5_overlap_case_316(self):
        self.assertEqual(pattern_match('hauhauhauhauhauhauh', 'hauh'), [0, 3, 6, 9, 12, 15])

    def test_min5_overlap_case_317(self):
        self.assertEqual(pattern_match('zezezezezezezezezezez', 'zez'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])

    def test_min5_overlap_case_318(self):
        self.assertEqual(pattern_match('lglglglglglgl', 'lgl'), [0, 2, 4, 6, 8, 10])

    def test_min5_overlap_case_319(self):
        self.assertEqual(pattern_match('tmhlmtmhlmtmhlmtmhlmtmhlmtmhlmtmhlmtmhlmtmhlmtmhlmtmhlmtmhlmt', 'tmhlmt'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55])

    def test_min5_overlap_case_320(self):
        self.assertEqual(pattern_match('llllllllllll', 'lll'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_min5_overlap_case_321(self):
        self.assertEqual(pattern_match('bbbbbbb', 'bb'), [0, 1, 2, 3, 4, 5])

    def test_min5_overlap_case_322(self):
        self.assertEqual(pattern_match('lllllllllllllllllll', 'll'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])

    def test_min5_overlap_case_323(self):
        self.assertEqual(pattern_match('vvvvvvvvvvvvvv', 'vv'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_min5_overlap_case_324(self):
        self.assertEqual(pattern_match('fwqmfwqmfwqmfwqmfwqmfwqmfwqmfwqmfwqmfwqmfwqmfwqmfwqmfwqmfwqmfwqmfwqmfwqmfwqmf', 'fwqmf'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72])

    def test_min5_overlap_case_325(self):
        self.assertEqual(pattern_match('rgrgrgrgrgrgrgr', 'rgr'), [0, 2, 4, 6, 8, 10, 12])

    def test_min5_overlap_case_326(self):
        self.assertEqual(pattern_match('gggggggggg', 'gg'), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_min5_overlap_case_327(self):
        self.assertEqual(pattern_match('ttttttttt', 'tt'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_min5_overlap_case_328(self):
        self.assertEqual(pattern_match('ltpgltpgltpgltpgltpgltpgltpgl', 'ltpgl'), [0, 4, 8, 12, 16, 20, 24])

    def test_min5_overlap_case_329(self):
        self.assertEqual(pattern_match('yyyyyyyy', 'yy'), [0, 1, 2, 3, 4, 5, 6])

    def test_min5_overlap_case_330(self):
        self.assertEqual(pattern_match('rrrrrrrrrrrrrrrr', 'rr'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_min5_overlap_case_331(self):
        self.assertEqual(pattern_match('orvorvorvorvorvorvorvorvorvo', 'orvo'), [0, 3, 6, 9, 12, 15, 18, 21, 24])

    def test_min5_overlap_case_332(self):
        self.assertEqual(pattern_match('ldqldqldqldqldqldqldqldqldqldqldqldqldqldqldqldqldqldqldql', 'ldql'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54])

    def test_min5_overlap_case_333(self):
        self.assertEqual(pattern_match('injvinjvinjvinjvinjvinjvinjvinjvinjvinjvinjvinjvinjvinjvinjvinjvinjvinjvi', 'injvi'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68])

    def test_min5_overlap_case_334(self):
        self.assertEqual(pattern_match('rydrydrydrydrydrydrydrydrydrydr', 'rydr'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27])

    def test_min5_overlap_case_335(self):
        self.assertEqual(pattern_match('ksksksksksksksksksksksksksksksksksk', 'ksk'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32])

    def test_min5_overlap_case_336(self):
        self.assertEqual(pattern_match('hhrhhrhhrhhrhhrhhrhhrh', 'hhrh'), [0, 3, 6, 9, 12, 15, 18])

    def test_min5_overlap_case_337(self):
        self.assertEqual(pattern_match('jsjejsjejsjejsjejsjejsjejsjejsjej', 'jsjej'), [0, 4, 8, 12, 16, 20, 24, 28])

    def test_min5_overlap_case_338(self):
        self.assertEqual(pattern_match('mjmjmjmjmjmjmjmjmjmjmjmjmjmjmjm', 'mjm'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28])

    def test_min5_overlap_case_339(self):
        self.assertEqual(pattern_match('vvvvvvvv', 'vv'), [0, 1, 2, 3, 4, 5, 6])

    def test_min5_overlap_case_340(self):
        self.assertEqual(pattern_match('djdjdjdjdjdjd', 'djd'), [0, 2, 4, 6, 8, 10])

    def test_min5_overlap_case_341(self):
        self.assertEqual(pattern_match('tgtgtgtgtgtgtgtgtgtgtgtgt', 'tgt'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22])

    def test_min5_overlap_case_342(self):
        self.assertEqual(pattern_match('iiiiiii', 'ii'), [0, 1, 2, 3, 4, 5])

    def test_min5_overlap_case_343(self):
        self.assertEqual(pattern_match('zmzmzmzmzmzmzmzmzmzmzmzmz', 'zmz'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22])

    def test_min5_overlap_case_344(self):
        self.assertEqual(pattern_match('uuuuuuuuuuuu', 'uu'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_min5_overlap_case_345(self):
        self.assertEqual(pattern_match('jjjjjjjjjjjjjjj', 'jj'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_min5_overlap_case_346(self):
        self.assertEqual(pattern_match('ananananananananananananananananananana', 'ana'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36])

    def test_min5_overlap_case_347(self):
        self.assertEqual(pattern_match('qqqqqqqqqqqqqqqqqqqq', 'qq'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    def test_min5_overlap_case_348(self):
        self.assertEqual(pattern_match('qcnmqcnmqcnmqcnmqcnmqcnmqcnmq', 'qcnmq'), [0, 4, 8, 12, 16, 20, 24])

    def test_min5_overlap_case_349(self):
        self.assertEqual(pattern_match('cccccccccccccccccc', 'cc'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    def test_min5_overlap_case_350(self):
        self.assertEqual(pattern_match('pdopdopdopdopdopdopdopdopdopdopdopdopdopdopdopdopdop', 'pdop'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48])

    def test_min5_overlap_case_351(self):
        self.assertEqual(pattern_match('trtrtrtrtrtrtrtrtrtrtrtrtrtrtrtrtrtrtrt', 'trt'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36])

    def test_min5_overlap_case_352(self):
        self.assertEqual(pattern_match('sjlqqsjlqqsjlqqsjlqqsjlqqsjlqqsjlqqsjlqqsjlqqsjlqqsjlqqsjlqqs', 'sjlqqs'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55])

    def test_min5_overlap_case_353(self):
        self.assertEqual(pattern_match('rrrrrrrrrrrr', 'rr'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_min5_overlap_case_354(self):
        self.assertEqual(pattern_match('xxxxxxxxxxx', 'xx'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_min5_overlap_case_355(self):
        self.assertEqual(pattern_match('ufcufcufcufcufcufcufcufcufcufcufcufcufcufcufcufcufcu', 'ufcu'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48])

    def test_min5_overlap_case_356(self):
        self.assertEqual(pattern_match('zzzzzzzz', 'zz'), [0, 1, 2, 3, 4, 5, 6])

    def test_min5_overlap_case_357(self):
        self.assertEqual(pattern_match('fmrhdfmrhdfmrhdfmrhdfmrhdfmrhdfmrhdfmrhdfmrhdfmrhdfmrhdfmrhdfmrhdfmrhdfmrhdfmrhdfmrhdfmrhdfmrhdfmrhdf', 'fmrhdf'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95])

    def test_min5_overlap_case_358(self):
        self.assertEqual(pattern_match('vovovovovovovovovov', 'vov'), [0, 2, 4, 6, 8, 10, 12, 14, 16])

    def test_min5_overlap_case_359(self):
        self.assertEqual(pattern_match('fyofyofyofyofyofyofyofyofyofyofyof', 'fyof'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30])

    def test_min5_overlap_case_360(self):
        self.assertEqual(pattern_match('nhnhnhnhnhnhnhnhnhnhn', 'nhn'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])

    def test_min5_overlap_case_361(self):
        self.assertEqual(pattern_match('ggggggggggggggg', 'gg'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_min5_overlap_case_362(self):
        self.assertEqual(pattern_match('akdzakdzakdzakdzakdzakdzakdzakdzakdza', 'akdza'), [0, 4, 8, 12, 16, 20, 24, 28, 32])

    def test_min5_overlap_case_363(self):
        self.assertEqual(pattern_match('sqsqsqsqsqsqsqsqsqs', 'sqs'), [0, 2, 4, 6, 8, 10, 12, 14, 16])

    def test_min5_overlap_case_364(self):
        self.assertEqual(pattern_match('zsvzsvzsvzsvzsvzsvzsvzsvzsvzsvzsvz', 'zsvz'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30])

    def test_min5_overlap_case_365(self):
        self.assertEqual(pattern_match('jjjjjjjj', 'jj'), [0, 1, 2, 3, 4, 5, 6])

    def test_min5_overlap_case_366(self):
        self.assertEqual(pattern_match('brbrbrbrbrbrbrbrbrbrbrb', 'brb'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

    def test_min5_overlap_case_367(self):
        self.assertEqual(pattern_match('yyyyyyyyyyyyyyyyyyyy', 'yy'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    def test_min5_overlap_case_368(self):
        self.assertEqual(pattern_match('wwwwwwww', 'ww'), [0, 1, 2, 3, 4, 5, 6])

    def test_min5_overlap_case_369(self):
        self.assertEqual(pattern_match('nsnunsnunsnunsnunsnunsnunsnunsnun', 'nsnun'), [0, 4, 8, 12, 16, 20, 24, 28])

    def test_min5_overlap_case_370(self):
        self.assertEqual(pattern_match('nnnnnnnn', 'nn'), [0, 1, 2, 3, 4, 5, 6])

    def test_min5_overlap_case_371(self):
        self.assertEqual(pattern_match('hlymkhlymkhlymkhlymkhlymkhlymkhlymkhlymkhlymkhlymkhlymkhlymkhlymkhlymkhlymkh', 'hlymkh'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70])

    def test_min5_overlap_case_372(self):
        self.assertEqual(pattern_match('uuuuuuuuuuuuuuuuuuu', 'uu'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])

    def test_min5_overlap_case_373(self):
        self.assertEqual(pattern_match('saocsaocsaocsaocsaocsaocs', 'saocs'), [0, 4, 8, 12, 16, 20])

    def test_min5_overlap_case_374(self):
        self.assertEqual(pattern_match('ipipipipipipipipipipipipipipipipipipipi', 'ipi'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36])

    def test_min5_overlap_case_375(self):
        self.assertEqual(pattern_match('vvvvvvvvv', 'vvv'), [0, 1, 2, 3, 4, 5, 6])

    def test_min5_overlap_case_376(self):
        self.assertEqual(pattern_match('ggggggggggggggg', 'gg'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_min5_overlap_case_377(self):
        self.assertEqual(pattern_match('udjacudjacudjacudjacudjacudjacudjacudjacudjacudjacudjacudjacudjacudjacudjacudjacudjacudjacudjacudjacu', 'udjacu'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95])

    def test_min5_overlap_case_378(self):
        self.assertEqual(pattern_match('vvvvvvvvvvvvv', 'vv'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_min5_overlap_case_379(self):
        self.assertEqual(pattern_match('doxswdoxswdoxswdoxswdoxswdoxswdoxswdoxswdoxswdoxswd', 'doxswd'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45])

    def test_min5_overlap_case_380(self):
        self.assertEqual(pattern_match('qqqqqqqqqqqqqqqqqqq', 'qq'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])

    def test_min5_overlap_case_381(self):
        self.assertEqual(pattern_match('ddddddddddd', 'dd'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_min5_overlap_case_382(self):
        self.assertEqual(pattern_match('nvynvynvynvynvynvynvynvynvynvynvynvynvynvynvynvynvyn', 'nvyn'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48])

    def test_min5_overlap_case_383(self):
        self.assertEqual(pattern_match('iltiltiltiltiltiltilti', 'ilti'), [0, 3, 6, 9, 12, 15, 18])

    def test_min5_overlap_case_384(self):
        self.assertEqual(pattern_match('xxxxxxxxxxxx', 'xx'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_min5_overlap_case_385(self):
        self.assertEqual(pattern_match('hhhhhhhhhhh', 'hh'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_min5_overlap_case_386(self):
        self.assertEqual(pattern_match('ddddddddd', 'dd'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_min5_overlap_case_387(self):
        self.assertEqual(pattern_match('rrrrrrrrr', 'rr'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_min5_overlap_case_388(self):
        self.assertEqual(pattern_match('mmmmmmmmm', 'mm'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_min5_overlap_case_389(self):
        self.assertEqual(pattern_match('pyootpyootpyootpyootpyootpyootpyootpyootpyootpyootp', 'pyootp'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45])

    def test_min5_overlap_case_390(self):
        self.assertEqual(pattern_match('lryzwlryzwlryzwlryzwlryzwlryzwlryzwlryzwlryzwlryzwlryzwlryzwlryzwl', 'lryzwl'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])

    def test_min5_overlap_case_391(self):
        self.assertEqual(pattern_match('sssssss', 'ss'), [0, 1, 2, 3, 4, 5])

    def test_min5_overlap_case_392(self):
        self.assertEqual(pattern_match('nnnnnnnnnnnnnnnnnnnnn', 'nn'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_min5_overlap_case_393(self):
        self.assertEqual(pattern_match('rrrrrrrrrrrrrrrrrr', 'rr'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    def test_min5_overlap_case_394(self):
        self.assertEqual(pattern_match('uuuuuuuuuuuuuuuuuuu', 'uu'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])

    def test_min5_overlap_case_395(self):
        self.assertEqual(pattern_match('gungungungungungungungungungungungung', 'gung'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33])

    def test_min5_overlap_case_396(self):
        self.assertEqual(pattern_match('vvvvvvvvvvvvvvvvvvvv', 'vv'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    def test_min5_overlap_case_397(self):
        self.assertEqual(pattern_match('xfffuxfffuxfffuxfffuxfffuxfffux', 'xfffux'), [0, 5, 10, 15, 20, 25])

    def test_min5_overlap_case_398(self):
        self.assertEqual(pattern_match('skwyskwyskwyskwyskwyskwyskwyskwyskwyskwyskwyskwyskwyskwyskwyskwyskwyskwyskwyskwys', 'skwys'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76])

    def test_min5_overlap_case_399(self):
        self.assertEqual(pattern_match('pppppppppppppppppppp', 'pp'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    def test_min5_overlap_case_400(self):
        self.assertEqual(pattern_match('cccccccccccccccccc', 'cc'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    def test_min5_overlap_case_401(self):
        self.assertEqual(pattern_match('shshshshshshshshshshshshshshshshshs', 'shs'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32])

    def test_min5_overlap_case_402(self):
        self.assertEqual(pattern_match('nfinfinfinfinfinfinfinfinfinfinfinfinfinfinfinf', 'nfinf'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42])

    def test_min5_overlap_case_403(self):
        self.assertEqual(pattern_match('zjzjzjzjzjzjzjzjzjzjzjzjzjzjzjzjzjzjzjz', 'zjz'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36])

    def test_min5_overlap_case_404(self):
        self.assertEqual(pattern_match('aaaaaaaaaaaaaaaaaaa', 'aa'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])

    def test_min5_overlap_case_405(self):
        self.assertEqual(pattern_match('qqqqqqqqqqqqqqq', 'qq'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_min5_overlap_case_406(self):
        self.assertEqual(pattern_match('vwvwvwvwvwvwvwv', 'vwv'), [0, 2, 4, 6, 8, 10, 12])

    def test_min5_overlap_case_407(self):
        self.assertEqual(pattern_match('jvjvjvjvjvjvjvjvjvjvjvjvjvjvjvjvjvjvjvjvj', 'jvj'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38])

    def test_min5_overlap_case_408(self):
        self.assertEqual(pattern_match('ohohohohohohohohohohohoho', 'oho'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22])

    def test_min5_overlap_case_409(self):
        self.assertEqual(pattern_match('fffffffffffffffff', 'ff'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_min5_overlap_case_410(self):
        self.assertEqual(pattern_match('eieieieieieieieieie', 'eie'), [0, 2, 4, 6, 8, 10, 12, 14, 16])

    def test_min5_overlap_case_411(self):
        self.assertEqual(pattern_match('hhkhhkhhkhhkhhkhhkhhkhhkhhkhhkhhkhhkh', 'hhkh'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33])

    def test_min5_overlap_case_412(self):
        self.assertEqual(pattern_match('vsvsvsvsvsvsvsvsvsvsvsvsvsvsvsvsvsv', 'vsv'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32])

    def test_min5_overlap_case_413(self):
        self.assertEqual(pattern_match('fxfxfxfxfxfxfxfxfxfxfxfxfxfxfxfxf', 'fxf'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])

    def test_min5_overlap_case_414(self):
        self.assertEqual(pattern_match('zwbhizwbhizwbhizwbhizwbhizwbhizwbhizwbhizwbhizwbhizwbhizwbhizwbhizwbhizwbhizwbhizwbhizwbhizwbhizwbhiz', 'zwbhiz'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95])

    def test_min5_overlap_case_415(self):
        self.assertEqual(pattern_match('thmonthmonthmonthmonthmonthmont', 'thmont'), [0, 5, 10, 15, 20, 25])

    def test_min5_overlap_case_416(self):
        self.assertEqual(pattern_match('xxxxxxxxxxxx', 'xx'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_min5_overlap_case_417(self):
        self.assertEqual(pattern_match('oooooooooooooooooo', 'oo'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    def test_min5_overlap_case_418(self):
        self.assertEqual(pattern_match('qwaqwaqwaqwaqwaqwaqwaqwaqwaqwaqwaqwaqwaqwaqwaqwaqwaqwaqwaqwaq', 'qwaq'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57])

    def test_min5_overlap_case_419(self):
        self.assertEqual(pattern_match('wwwwwwwwwwwwwww', 'ww'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_min5_overlap_case_420(self):
        self.assertEqual(pattern_match('cxlpzcxlpzcxlpzcxlpzcxlpzcxlpzcxlpzcxlpzcxlpzcxlpzcxlpzcxlpzcxlpzcxlpzcxlpzcxlpzcxlpzcxlpzc', 'cxlpzc'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85])

    def test_min5_overlap_case_421(self):
        self.assertEqual(pattern_match('nnnnnnnnnnnnnnnnnnn', 'nn'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])

    def test_min5_overlap_case_422(self):
        self.assertEqual(pattern_match('ddddddddddddddddd', 'dd'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_min5_overlap_case_423(self):
        self.assertEqual(pattern_match('noednoednoednoednoednoednoednoednoednoednoednoednoednoednoednoednoednoednoednoedn', 'noedn'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76])

    def test_min5_overlap_case_424(self):
        self.assertEqual(pattern_match('vjvjvjvjvjvjvjvjvjvjvjvjvjvjv', 'vjv'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26])

    def test_min5_overlap_case_425(self):
        self.assertEqual(pattern_match('hhhhhhhhhhhhhhhhh', 'hh'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_min5_overlap_case_426(self):
        self.assertEqual(pattern_match('xwaxwaxwaxwaxwaxwaxwaxwaxwaxwaxwaxwaxwaxwaxwaxwaxwaxwaxwax', 'xwax'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54])

    def test_min5_overlap_case_427(self):
        self.assertEqual(pattern_match('gogogogogogog', 'gog'), [0, 2, 4, 6, 8, 10])

    def test_min5_overlap_case_428(self):
        self.assertEqual(pattern_match('vblvblvblvblvblvblvblvblvblvblvblvblvblvblvblvblvblvblvblvblv', 'vblv'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57])

    def test_min5_overlap_case_429(self):
        self.assertEqual(pattern_match('hhrthhrthhrthhrthhrthhrth', 'hhrth'), [0, 4, 8, 12, 16, 20])

    def test_min5_overlap_case_430(self):
        self.assertEqual(pattern_match('aaaaaaa', 'aa'), [0, 1, 2, 3, 4, 5])

    def test_min5_overlap_case_431(self):
        self.assertEqual(pattern_match('hlahlahlahlahlahlahlahlahlahlahlahlahlah', 'hlah'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36])

    def test_min5_overlap_case_432(self):
        self.assertEqual(pattern_match('kkkkkkkkkkkkkkkkkkk', 'kkk'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    def test_min5_overlap_case_433(self):
        self.assertEqual(pattern_match('yvxyvxyvxyvxyvxyvxyvxyvxyvxy', 'yvxy'), [0, 3, 6, 9, 12, 15, 18, 21, 24])

    def test_min5_overlap_case_434(self):
        self.assertEqual(pattern_match('aaaaaaaaaaaaaaaaa', 'aa'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_min5_overlap_case_435(self):
        self.assertEqual(pattern_match('pspspspspspspspspspspsp', 'psp'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

    def test_min5_overlap_case_436(self):
        self.assertEqual(pattern_match('vfvfvfvfvfvfvfvfvfvfvfvfvfvfvfvfvfv', 'vfv'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32])

    def test_min5_overlap_case_437(self):
        self.assertEqual(pattern_match('iqkiiqkiiqkiiqkiiqkiiqkiiqkiiqkiiqkiiqkii', 'iqkii'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36])

    def test_min5_overlap_case_438(self):
        self.assertEqual(pattern_match('ssssssssssssss', 'ss'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_min5_overlap_case_439(self):
        self.assertEqual(pattern_match('gndegndegndegndegndegndegndegndegndegndegndegndegndegndeg', 'gndeg'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52])

    def test_min5_overlap_case_440(self):
        self.assertEqual(pattern_match('dndndndndndndndndndndndndndndndnd', 'dnd'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])

    def test_min5_overlap_case_441(self):
        self.assertEqual(pattern_match('dzhhidzhhidzhhidzhhidzhhidzhhidzhhidzhhidzhhidzhhidzhhidzhhidzhhidzhhidzhhid', 'dzhhid'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70])

    def test_min5_overlap_case_442(self):
        self.assertEqual(pattern_match('pvaapvaapvaapvaapvaapvaapvaapvaapvaapvaapvaapvaapvaap', 'pvaap'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48])

    def test_min5_overlap_case_443(self):
        self.assertEqual(pattern_match('gggggggggggggg', 'gg'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_min5_overlap_case_444(self):
        self.assertEqual(pattern_match('wwwwwwwwwwwwwwwwwww', 'ww'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])

    def test_min5_overlap_case_445(self):
        self.assertEqual(pattern_match('mrmrmrmrmrmrmrmrmrmrmrmrmrmrmrmrmrmrmrmrm', 'mrm'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38])

    def test_min5_overlap_case_446(self):
        self.assertEqual(pattern_match('ssssssssssssssssss', 'ss'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    def test_min5_overlap_case_447(self):
        self.assertEqual(pattern_match('zvzvzvzvzvzvzvzvzvz', 'zvz'), [0, 2, 4, 6, 8, 10, 12, 14, 16])

    def test_min5_overlap_case_448(self):
        self.assertEqual(pattern_match('wwwwwwwwwwwwwwww', 'ww'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_min5_overlap_case_449(self):
        self.assertEqual(pattern_match('eeeeeeeeeeeeeeeeee', 'ee'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    def test_min5_overlap_case_450(self):
        self.assertEqual(pattern_match('iiiiiiiiiiii', 'ii'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_min5_overlap_case_451(self):
        self.assertEqual(pattern_match('sssssssssssssssssss', 'ss'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])

    def test_min5_overlap_case_452(self):
        self.assertEqual(pattern_match('mcmcmcmcmcmcmcmcmcmcmcmcmcmcmcm', 'mcm'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28])

    def test_min5_overlap_case_453(self):
        self.assertEqual(pattern_match('yjjzyjjzyjjzyjjzyjjzyjjzyjjzyjjzyjjzyjjzyjjzyjjzyjjzyjjzyjjzyjjzyjjzyjjzyjjzyjjzy', 'yjjzy'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76])

    def test_min5_overlap_case_454(self):
        self.assertEqual(pattern_match('kkkkkkkkk', 'kk'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_min5_overlap_case_455(self):
        self.assertEqual(pattern_match('gggggggggggggggggggg', 'gg'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    def test_min5_overlap_case_456(self):
        self.assertEqual(pattern_match('cccccccccccccccccc', 'cc'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    def test_min5_overlap_case_457(self):
        self.assertEqual(pattern_match('uoxspuoxspuoxspuoxspuoxspuoxspuoxspuoxspuoxspuoxspuoxspuoxspuoxspuoxspuoxspu', 'uoxspu'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70])

    def test_min5_overlap_case_458(self):
        self.assertEqual(pattern_match('ieypieypieypieypieypieypieypieypi', 'ieypi'), [0, 4, 8, 12, 16, 20, 24, 28])

    def test_min5_overlap_case_459(self):
        self.assertEqual(pattern_match('lwlwlwlwlwlwlwl', 'lwl'), [0, 2, 4, 6, 8, 10, 12])

    def test_min5_overlap_case_460(self):
        self.assertEqual(pattern_match('uuuuuuuu', 'uu'), [0, 1, 2, 3, 4, 5, 6])

    def test_min5_overlap_case_461(self):
        self.assertEqual(pattern_match('uuuuuuuuuuuuuuuuuuuuu', 'uu'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_min5_overlap_case_462(self):
        self.assertEqual(pattern_match('tkcdvtkcdvtkcdvtkcdvtkcdvtkcdvtkcdvtkcdvtkcdvt', 'tkcdvt'), [0, 5, 10, 15, 20, 25, 30, 35, 40])

    def test_min5_overlap_case_463(self):
        self.assertEqual(pattern_match('hmkuhmkuhmkuhmkuhmkuhmkuhmkuhmkuhmkuhmkuhmkuhmkuhmkuhmkuhmkuhmkuhmkuhmkuh', 'hmkuh'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68])

    def test_min5_overlap_case_464(self):
        self.assertEqual(pattern_match('mdesmdesmdesmdesmdesmdesmdesmdesmdesmdesmdesmdesmdesmdesmdesmdesmdesmdesm', 'mdesm'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68])

    def test_min5_overlap_case_465(self):
        self.assertEqual(pattern_match('wwwwwwwww', 'ww'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_min5_overlap_case_466(self):
        self.assertEqual(pattern_match('sssssssssssssssss', 'ss'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_min5_overlap_case_467(self):
        self.assertEqual(pattern_match('uuuuuuuuuuuuuuu', 'uu'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_min5_overlap_case_468(self):
        self.assertEqual(pattern_match('eeeeeeeeeeeeeeeee', 'ee'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_min5_overlap_case_469(self):
        self.assertEqual(pattern_match('hhhhhhhh', 'hh'), [0, 1, 2, 3, 4, 5, 6])

    def test_min5_overlap_case_470(self):
        self.assertEqual(pattern_match('yxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxy', 'yxy'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])

    def test_min5_overlap_case_471(self):
        self.assertEqual(pattern_match('elelelelelelelelelelelelelele', 'ele'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26])

    def test_min5_overlap_case_472(self):
        self.assertEqual(pattern_match('lpydelpydelpydelpydelpydelpydelpydelpydelpydelpydelpydelpydelpydelpydel', 'lpydel'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65])

    def test_min5_overlap_case_473(self):
        self.assertEqual(pattern_match('xofjxofjxofjxofjxofjxofjxofjxofjxofjxofjxofjxofjxofjx', 'xofjx'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48])

    def test_min5_overlap_case_474(self):
        self.assertEqual(pattern_match('lnlnlnlnlnlnlnlnlnlnlnlnlnlnlnlnlnlnlnl', 'lnl'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36])

    def test_min5_overlap_case_475(self):
        self.assertEqual(pattern_match('iptciptciptciptciptciptciptciptciptciptciptciptciptciptciptciptciptciptciptci', 'iptci'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72])

    def test_min5_overlap_case_476(self):
        self.assertEqual(pattern_match('yyyyyyyyyyyyy', 'yy'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_min5_overlap_case_477(self):
        self.assertEqual(pattern_match('vnwvnwvnwvnwvnwvnwvnwvnwvnwvnwvnwv', 'vnwv'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30])

    def test_min5_overlap_case_478(self):
        self.assertEqual(pattern_match('nnnnnnnnnnn', 'nn'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_min5_overlap_case_479(self):
        self.assertEqual(pattern_match('vvvvvvvvvvvvvvv', 'vv'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_min5_overlap_case_480(self):
        self.assertEqual(pattern_match('ooooooo', 'oo'), [0, 1, 2, 3, 4, 5])

    def test_min5_overlap_case_481(self):
        self.assertEqual(pattern_match('xueyxueyxueyxueyxueyxueyxueyxueyxueyxueyxueyxueyxueyxueyxueyxueyxueyxueyx', 'xueyx'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68])

    def test_min5_overlap_case_482(self):
        self.assertEqual(pattern_match('tctctctctctctctctct', 'tct'), [0, 2, 4, 6, 8, 10, 12, 14, 16])

    def test_min5_overlap_case_483(self):
        self.assertEqual(pattern_match('ugyugyugyugyugyugyu', 'ugyu'), [0, 3, 6, 9, 12, 15])

    def test_min5_overlap_case_484(self):
        self.assertEqual(pattern_match('bdbdbdbdbdbdbdbdbdbdbdbdbdbdbdbdbdbdb', 'bdb'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34])

    def test_min5_overlap_case_485(self):
        self.assertEqual(pattern_match('uouououououououououououououououou', 'uou'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])

    def test_min5_overlap_case_486(self):
        self.assertEqual(pattern_match('aaaaaaaaaaaaa', 'aa'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_min5_overlap_case_487(self):
        self.assertEqual(pattern_match('jsjsjsjsjsjsj', 'jsj'), [0, 2, 4, 6, 8, 10])

    def test_min5_overlap_case_488(self):
        self.assertEqual(pattern_match('vzvzvzvzvzvzvzvzvzvzvzvzvzvzvzvzvzvzv', 'vzv'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34])

    def test_min5_overlap_case_489(self):
        self.assertEqual(pattern_match('zybtzybtzybtzybtzybtzybtzybtzybtzybtzybtzybtzybtzybtzybtzybtzybtzybtzybtz', 'zybtz'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68])

    def test_min5_overlap_case_490(self):
        self.assertEqual(pattern_match('dwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwd', 'dwd'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32])

    def test_min5_overlap_case_491(self):
        self.assertEqual(pattern_match('mmmmmmmm', 'mm'), [0, 1, 2, 3, 4, 5, 6])

    def test_min5_overlap_case_492(self):
        self.assertEqual(pattern_match('frfkefrfkefrfkefrfkefrfkefrfkefrfkefrfkef', 'frfkef'), [0, 5, 10, 15, 20, 25, 30, 35])

    def test_min5_overlap_case_493(self):
        self.assertEqual(pattern_match('qcqcqcqcqcqcqcqcqcqcqcqcqcqcqcqcq', 'qcq'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])

    def test_min5_overlap_case_494(self):
        self.assertEqual(pattern_match('ffffffffffffffff', 'ff'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_min5_overlap_case_495(self):
        self.assertEqual(pattern_match('xxxxxxxxxxxxxxxxxx', 'xx'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    def test_min5_overlap_case_496(self):
        self.assertEqual(pattern_match('yiyiyiyiyiyiyiy', 'yiy'), [0, 2, 4, 6, 8, 10, 12])

    def test_min5_overlap_case_497(self):
        self.assertEqual(pattern_match('exexexexexexexexexexexexexexe', 'exe'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26])

    def test_min5_overlap_case_498(self):
        self.assertEqual(pattern_match('xlfxlfxlfxlfxlfxlfxlfxlfxlfx', 'xlfx'), [0, 3, 6, 9, 12, 15, 18, 21, 24])

    def test_min5_overlap_case_499(self):
        self.assertEqual(pattern_match('evvevvevvevvevvevvevvevvevvevvevvevvevvevvevve', 'evve'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42])

    def test_min5_overlap_case_500(self):
        self.assertEqual(pattern_match('tttttttt', 'tt'), [0, 1, 2, 3, 4, 5, 6])

    def test_min5_overlap_case_501(self):
        self.assertEqual(pattern_match('ccccccccccccc', 'cc'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_min5_overlap_case_502(self):
        self.assertEqual(pattern_match('pjdzkpjdzkpjdzkpjdzkpjdzkpjdzkpjdzkpjdzkpjdzkpjdzkpjdzkpjdzkpjdzkpjdzkpjdzkpjdzkpjdzkpjdzkpjdzkpjdzkp', 'pjdzkp'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95])

    def test_min5_overlap_case_503(self):
        self.assertEqual(pattern_match('nrnrnrnrnrnrn', 'nrn'), [0, 2, 4, 6, 8, 10])

    def test_min5_overlap_case_504(self):
        self.assertEqual(pattern_match('xoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxox', 'xox'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38])

    def test_min5_overlap_case_505(self):
        self.assertEqual(pattern_match('wwwwwww', 'ww'), [0, 1, 2, 3, 4, 5])

    def test_min5_overlap_case_506(self):
        self.assertEqual(pattern_match('zzzzzzzzz', 'zz'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_min5_overlap_case_507(self):
        self.assertEqual(pattern_match('hhhhhhhhhhhhhhhhhh', 'hh'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    def test_min5_overlap_case_508(self):
        self.assertEqual(pattern_match('fififififififififif', 'fif'), [0, 2, 4, 6, 8, 10, 12, 14, 16])

    def test_min5_overlap_case_509(self):
        self.assertEqual(pattern_match('ppppppp', 'pp'), [0, 1, 2, 3, 4, 5])

    def test_min5_overlap_case_510(self):
        self.assertEqual(pattern_match('kkkkkkkkkk', 'kk'), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_min5_overlap_case_511(self):
        self.assertEqual(pattern_match('bhwplbhwplbhwplbhwplbhwplbhwplbhwplbhwplbhwplbhwplbhwplbhwplbhwplbhwplbhwplbhwplbhwplbhwplbhwplbhwplb', 'bhwplb'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95])

    def test_min5_overlap_case_512(self):
        self.assertEqual(pattern_match('qudqudqudqudqudqudqudqudqudqudqudqudq', 'qudq'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33])

    def test_min5_overlap_case_513(self):
        self.assertEqual(pattern_match('kckckckckckckckckck', 'kck'), [0, 2, 4, 6, 8, 10, 12, 14, 16])

    def test_min5_overlap_case_514(self):
        self.assertEqual(pattern_match('jjjjjjjjjjjjjjjjjj', 'jj'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    def test_min5_overlap_case_515(self):
        self.assertEqual(pattern_match('ccccccccccc', 'cc'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_min5_overlap_case_516(self):
        self.assertEqual(pattern_match('aylaylaylaylaylaylayla', 'ayla'), [0, 3, 6, 9, 12, 15, 18])

    def test_min5_overlap_case_517(self):
        self.assertEqual(pattern_match('cccccccccc', 'cc'), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_min5_overlap_case_518(self):
        self.assertEqual(pattern_match('ffffffffffffffffffff', 'ff'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    def test_min5_overlap_case_519(self):
        self.assertEqual(pattern_match('hsacqhsacqhsacqhsacqhsacqhsacqh', 'hsacqh'), [0, 5, 10, 15, 20, 25])

    def test_min5_overlap_case_520(self):
        self.assertEqual(pattern_match('tmurmtmurmtmurmtmurmtmurmtmurmtmurmtmurmt', 'tmurmt'), [0, 5, 10, 15, 20, 25, 30, 35])

    def test_min5_overlap_case_521(self):
        self.assertEqual(pattern_match('giagiagiagiagiagiagiagiagiag', 'giag'), [0, 3, 6, 9, 12, 15, 18, 21, 24])

    def test_min5_overlap_case_522(self):
        self.assertEqual(pattern_match('sfxsfxsfxsfxsfxsfxsfxsfxsfxsfxsfxsfxsfxs', 'sfxs'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36])

    def test_min5_overlap_case_523(self):
        self.assertEqual(pattern_match('mhwmhwmhwmhwmhwmhwmhwmhwmhwmhwmhwmhwmhwmhwmhwmhwmhwmhwm', 'mhwm'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51])

    def test_min5_overlap_case_524(self):
        self.assertEqual(pattern_match('pjpjpjpjpjpjpjpjpjpjpjpjpjpjpjpjpjpjpjpjp', 'pjp'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38])

    def test_min5_overlap_case_525(self):
        self.assertEqual(pattern_match('oeaoeaoeaoeaoeaoeaoeaoeaoeaoeaoeaoeao', 'oeao'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33])

    def test_min5_overlap_case_526(self):
        self.assertEqual(pattern_match('pppppppp', 'pp'), [0, 1, 2, 3, 4, 5, 6])

    def test_min5_overlap_case_527(self):
        self.assertEqual(pattern_match('dddddddddddd', 'dd'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_min5_overlap_case_528(self):
        self.assertEqual(pattern_match('hnwizhnwizhnwizhnwizhnwizhnwizhnwizhnwizhnwizhnwizhnwizhnwizhnwizhnwizhnwizhnwizh', 'hnwizh'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75])

    def test_min5_overlap_case_529(self):
        self.assertEqual(pattern_match('qrkqrkqrkqrkqrkqrkqrkqrkqrkqrkqrkqrkqrkq', 'qrkq'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36])

    def test_min5_overlap_case_530(self):
        self.assertEqual(pattern_match('ccccccccccccccc', 'cc'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_min5_overlap_case_531(self):
        self.assertEqual(pattern_match('yyyyyyyyyy', 'yy'), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_min5_overlap_case_532(self):
        self.assertEqual(pattern_match('rrrrrrrrrrrrrrrrrrr', 'rr'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])

    def test_min5_overlap_case_533(self):
        self.assertEqual(pattern_match('zjzjzjzjzjzjzjz', 'zjz'), [0, 2, 4, 6, 8, 10, 12])

    def test_min5_overlap_case_534(self):
        self.assertEqual(pattern_match('ssssssssssssssssss', 'ss'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    def test_min5_overlap_case_535(self):
        self.assertEqual(pattern_match('pxqpxqpxqpxqpxqpxqpxqpxqpxqp', 'pxqp'), [0, 3, 6, 9, 12, 15, 18, 21, 24])

    def test_min5_overlap_case_536(self):
        self.assertEqual(pattern_match('ttttttttttttttttttt', 'tt'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])

    def test_min5_overlap_case_537(self):
        self.assertEqual(pattern_match('lllllllllllllllllll', 'll'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])

    def test_min5_overlap_case_538(self):
        self.assertEqual(pattern_match('ccccccc', 'cc'), [0, 1, 2, 3, 4, 5])

    def test_min5_overlap_case_539(self):
        self.assertEqual(pattern_match('vxceevxceevxceevxceevxceevxceevxceevxceevxceevxceevxceevxceevxceevxceevxceevxceevxceevxceevxceevxceev', 'vxceev'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95])

    def test_min5_overlap_case_540(self):
        self.assertEqual(pattern_match('dddddddddddddddddddd', 'dd'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    def test_min5_overlap_case_541(self):
        self.assertEqual(pattern_match('ccccccccccccc', 'cc'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_min5_overlap_case_542(self):
        self.assertEqual(pattern_match('bbbbbbbbbbbbbbbbbbbbb', 'bb'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_min5_overlap_case_543(self):
        self.assertEqual(pattern_match('puzpuzpuzpuzpuzpuzpuzp', 'puzp'), [0, 3, 6, 9, 12, 15, 18])

    def test_min5_overlap_case_544(self):
        self.assertEqual(pattern_match('dotfcdotfcdotfcdotfcdotfcdotfcdotfcdotfcdotfcd', 'dotfcd'), [0, 5, 10, 15, 20, 25, 30, 35, 40])

    def test_min5_overlap_case_545(self):
        self.assertEqual(pattern_match('rysjurysjurysjurysjurysjurysjurysjurysjurysjurysjurysjurysjurysjurysjurysjurysjurysjur', 'rysjur'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80])

    def test_min5_overlap_case_546(self):
        self.assertEqual(pattern_match('tttttttttttttt', 'tt'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_min5_overlap_case_547(self):
        self.assertEqual(pattern_match('wopwopwopwopwopwopwopwopwopwopwopwopwopwopwopwopwopw', 'wopw'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48])

    def test_min5_overlap_case_548(self):
        self.assertEqual(pattern_match('vvvvvvvvvvvvvvvv', 'vv'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_min5_overlap_case_549(self):
        self.assertEqual(pattern_match('zodzodzodzodzodzodzodz', 'zodz'), [0, 3, 6, 9, 12, 15, 18])

    def test_min5_overlap_case_550(self):
        self.assertEqual(pattern_match('eeeeeee', 'ee'), [0, 1, 2, 3, 4, 5])

    def test_min5_overlap_case_551(self):
        self.assertEqual(pattern_match('nnnnnnnn', 'nn'), [0, 1, 2, 3, 4, 5, 6])

    def test_min5_overlap_case_552(self):
        self.assertEqual(pattern_match('uuuuuuuuuuuuuuuuuuuuuu', 'uuu'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_min5_overlap_case_553(self):
        self.assertEqual(pattern_match('hrhrhrhrhrhrhrhrhrhrhrh', 'hrh'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

    def test_min5_overlap_case_554(self):
        self.assertEqual(pattern_match('dpdpdpdpdpdpdpdpdpdpdpdpdpd', 'dpd'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])

    def test_min5_overlap_case_555(self):
        self.assertEqual(pattern_match('ltzxltzxltzxltzxltzxltzxltzxltzxl', 'ltzxl'), [0, 4, 8, 12, 16, 20, 24, 28])

    def test_min5_overlap_case_556(self):
        self.assertEqual(pattern_match('apbsapbsapbsapbsapbsapbsapbsapbsapbsapbsapbsapbsapbsapbsapbsa', 'apbsa'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56])

    def test_min5_overlap_case_557(self):
        self.assertEqual(pattern_match('yyyyyyyyyyyyy', 'yy'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_min5_overlap_case_558(self):
        self.assertEqual(pattern_match('ooooooooooooo', 'oo'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_min5_overlap_case_559(self):
        self.assertEqual(pattern_match('lxwulxwulxwulxwulxwulxwulxwulxwulxwulxwulxwulxwulxwulx', 'lxwulx'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48])

    def test_min5_overlap_case_560(self):
        self.assertEqual(pattern_match('pkpkpkpkpkpkpkpkpkpkpkpkpkpkpkpkpkpkpkpkp', 'pkp'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38])

    def test_min5_overlap_case_561(self):
        self.assertEqual(pattern_match('qqqqqqqqqqqqqqqqqqq', 'qq'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])

    def test_min5_overlap_case_562(self):
        self.assertEqual(pattern_match('vbpvbpvbpvbpvbpvbpvbpvbpvbpvbpvbpvbpvbpvbpv', 'vbpv'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39])

    def test_min5_overlap_case_563(self):
        self.assertEqual(pattern_match('nnnnnnnnnnnnnn', 'nn'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_min5_overlap_case_564(self):
        self.assertEqual(pattern_match('dpxzdpxzdpxzdpxzdpxzdpxzdpxzdpxzdpxzdpxzdpxzdpxzdpxzd', 'dpxzd'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48])

    def test_min5_overlap_case_565(self):
        self.assertEqual(pattern_match('ooooooo', 'oo'), [0, 1, 2, 3, 4, 5])

    def test_min5_overlap_case_566(self):
        self.assertEqual(pattern_match('mkmkmkmkmkmkm', 'mkm'), [0, 2, 4, 6, 8, 10])

    def test_min5_overlap_case_567(self):
        self.assertEqual(pattern_match('nnnnnnnn', 'nn'), [0, 1, 2, 3, 4, 5, 6])

    def test_min5_overlap_case_568(self):
        self.assertEqual(pattern_match('bbbbbbbbbb', 'bb'), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_min5_overlap_case_569(self):
        self.assertEqual(pattern_match('cxucxucxucxucxucxucxucxuc', 'cxuc'), [0, 3, 6, 9, 12, 15, 18, 21])

    def test_min5_overlap_case_570(self):
        self.assertEqual(pattern_match('llllllllllllllllllll', 'll'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    def test_min5_overlap_case_571(self):
        self.assertEqual(pattern_match('xxxxxxxxxxxxxxxxxx', 'xx'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    def test_min5_overlap_case_572(self):
        self.assertEqual(pattern_match('lbgsplbgsplbgsplbgsplbgsplbgsplbgsplbgsplbgsplbgsplbgsplbgsplbgsplbgsplbgspl', 'lbgspl'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70])

    def test_min5_overlap_case_573(self):
        self.assertEqual(pattern_match('jwshjwshjwshjwshjwshjwshjwshjwshjwshjwshjwshjwshjwshjwshj', 'jwshj'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52])

    def test_min5_overlap_case_574(self):
        self.assertEqual(pattern_match('njbmnjbmnjbmnjbmnjbmnjbmnjbmnjbmnjbmnjbmnjbmnjbmnjbmnjbmnjbmnjbmnjbmnjbmnjbmnjbmn', 'njbmn'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76])

    def test_min5_overlap_case_575(self):
        self.assertEqual(pattern_match('ssssssssssssss', 'ss'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_min5_overlap_case_576(self):
        self.assertEqual(pattern_match('gggggggggggggggg', 'gg'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_min5_overlap_case_577(self):
        self.assertEqual(pattern_match('qlqlqlqlqlqlqlqlqlqlqlqlqlqlqlq', 'qlq'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28])

    def test_min5_overlap_case_578(self):
        self.assertEqual(pattern_match('vlvlvlvlvlvlvlvlvlv', 'vlv'), [0, 2, 4, 6, 8, 10, 12, 14, 16])

    def test_min5_overlap_case_579(self):
        self.assertEqual(pattern_match('cubdocubdocubdocubdocubdocubdocubdocubdoc', 'cubdoc'), [0, 5, 10, 15, 20, 25, 30, 35])

    def test_min5_overlap_case_580(self):
        self.assertEqual(pattern_match('aaaaaaaaaaaaaaaaaaaa', 'aa'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    def test_min5_overlap_case_581(self):
        self.assertEqual(pattern_match('ffffffffffffffff', 'ff'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_min5_overlap_case_582(self):
        self.assertEqual(pattern_match('ggggggggggggggggg', 'gg'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_min5_overlap_case_583(self):
        self.assertEqual(pattern_match('hzzhzzhzzhzzhzzhzzhzzhzzhzzhzzhzzhzzh', 'hzzh'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33])

    def test_min5_overlap_case_584(self):
        self.assertEqual(pattern_match('vvvvvvvvvvvvvv', 'vv'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_min5_overlap_case_585(self):
        self.assertEqual(pattern_match('zpmzdzpmzdzpmzdzpmzdzpmzdzpmzdzpmzdzpmzdzpmzdzpmzdzpmzdzpmzdz', 'zpmzdz'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55])

    def test_min5_overlap_case_586(self):
        self.assertEqual(pattern_match('xxxxxxxxxx', 'xx'), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_min5_overlap_case_587(self):
        self.assertEqual(pattern_match('ssssssss', 'ss'), [0, 1, 2, 3, 4, 5, 6])

    def test_min5_overlap_case_588(self):
        self.assertEqual(pattern_match('nnnnnnnnnnnnnnnnnnn', 'nn'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])

    def test_min5_overlap_case_589(self):
        self.assertEqual(pattern_match('zpfzizpfzizpfzizpfzizpfzizpfzizpfzizpfzizpfzizpfzizpfzizpfzizpfzizpfzizpfzizpfzizpfzizpfziz', 'zpfziz'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85])

    def test_min5_overlap_case_590(self):
        self.assertEqual(pattern_match('bbbbbbbbbbbbbbbbb', 'bb'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_min5_overlap_case_591(self):
        self.assertEqual(pattern_match('ppppppppppppppppppppp', 'pp'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_min5_overlap_case_592(self):
        self.assertEqual(pattern_match('jfgjfgjfgjfgjfgjfgjfgjfgj', 'jfgj'), [0, 3, 6, 9, 12, 15, 18, 21])

    def test_min5_overlap_case_593(self):
        self.assertEqual(pattern_match('bbbbbbbbbbbbbbbbbb', 'bb'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    def test_min5_overlap_case_594(self):
        self.assertEqual(pattern_match('bbbbbbbbbbbbbb', 'bbb'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_min5_overlap_case_595(self):
        self.assertEqual(pattern_match('qnliyqnliyqnliyqnliyqnliyqnliyqnliyqnliyqnliyqnliyqnliyqnliyq', 'qnliyq'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55])

    def test_min5_overlap_case_596(self):
        self.assertEqual(pattern_match('hhhhhhhh', 'hh'), [0, 1, 2, 3, 4, 5, 6])

    def test_min5_overlap_case_597(self):
        self.assertEqual(pattern_match('ndpndpndpndpndpndpndpndpndpndpn', 'ndpn'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27])

    def test_min5_overlap_case_598(self):
        self.assertEqual(pattern_match('vvvvvvvvvvv', 'vv'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_min5_overlap_case_599(self):
        self.assertEqual(pattern_match('jxvtrjxvtrjxvtrjxvtrjxvtrjxvtrjxvtrjxvtrjxvtrjxvtrjxvtrjxvtrjxvtrjxvtrjxvtrjxvtrjxvtrj', 'jxvtrj'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80])

    def test_min5_overlap_case_600(self):
        self.assertEqual(pattern_match('eveveveveveveveveveve', 'eve'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])

    def test_min5_overlap_case_601(self):
        self.assertEqual(pattern_match('uuuuuuuuuuuuuuuuuuu', 'uu'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])

    def test_min5_overlap_case_602(self):
        self.assertEqual(pattern_match('dmbqdmbqdmbqdmbqdmbqdmbqdmbqdmbqdmbqdmbqdmbqdmbqd', 'dmbqd'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44])

    def test_min5_overlap_case_603(self):
        self.assertEqual(pattern_match('yekyekyekyekyekyekyekyekyekyekyekyekyekyekyeky', 'yeky'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42])

    def test_min5_overlap_case_604(self):
        self.assertEqual(pattern_match('lfklfklfklfklfklfklfklfklfkl', 'lfkl'), [0, 3, 6, 9, 12, 15, 18, 21, 24])

    def test_min5_overlap_case_605(self):
        self.assertEqual(pattern_match('jjjjjjjjjjjjjjjj', 'jj'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_min5_overlap_case_606(self):
        self.assertEqual(pattern_match('kkpzkkpzkkpzkkpzkkpzkkpzkkpzkkpzkkpzkkpzkkpzkkpzkkpzkkpzkkpzkkpzkkpzkkpzkkpzk', 'kkpzk'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72])

    def test_min5_overlap_case_607(self):
        self.assertEqual(pattern_match('gggggggggggggg', 'gg'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_min5_overlap_case_608(self):
        self.assertEqual(pattern_match('lllllll', 'll'), [0, 1, 2, 3, 4, 5])

    def test_min5_overlap_case_609(self):
        self.assertEqual(pattern_match('htyehtyehtyehtyehtyehtyehtyehtyehtyehtyehtyehtyehtyehtyehtyehtyehtyeh', 'htyeh'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64])

    def test_min5_overlap_case_610(self):
        self.assertEqual(pattern_match('vkhvkhvkhvkhvkhvkhv', 'vkhv'), [0, 3, 6, 9, 12, 15])

    def test_min5_overlap_case_611(self):
        self.assertEqual(pattern_match('papapapapapapapapapapapapapapapapap', 'pap'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32])

    def test_min5_overlap_case_612(self):
        self.assertEqual(pattern_match('pgrpgrpgrpgrpgrpgrpgrpgrpgrpgrpgrpgrpgrp', 'pgrp'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36])

    def test_min5_overlap_case_613(self):
        self.assertEqual(pattern_match('vxnvxnvxnvxnvxnvxnvxnvxnvxnvxnvxnv', 'vxnv'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30])

    def test_min5_overlap_case_614(self):
        self.assertEqual(pattern_match('eeeeeeee', 'ee'), [0, 1, 2, 3, 4, 5, 6])

    def test_min5_overlap_case_615(self):
        self.assertEqual(pattern_match('scxscxscxscxscxscxscxscxscxscxscxscxs', 'scxs'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33])

    def test_min5_overlap_case_616(self):
        self.assertEqual(pattern_match('rkrfbrkrfbrkrfbrkrfbrkrfbrkrfbr', 'rkrfbr'), [0, 5, 10, 15, 20, 25])

    def test_min5_overlap_case_617(self):
        self.assertEqual(pattern_match('qmpnqmpnqmpnqmpnqmpnqmpnqmpnqmpnqmpnqmpnqmpnqmpnqmpnq', 'qmpnq'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48])

    def test_min5_overlap_case_618(self):
        self.assertEqual(pattern_match('efefefefefefefe', 'efe'), [0, 2, 4, 6, 8, 10, 12])

    def test_min5_overlap_case_619(self):
        self.assertEqual(pattern_match('uuuuuuuuuuuu', 'uu'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_min5_overlap_case_620(self):
        self.assertEqual(pattern_match('hhhhhhhhhhhhhhhhhhhhh', 'hh'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_min5_overlap_case_621(self):
        self.assertEqual(pattern_match('llllllllllllllllllll', 'll'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    def test_min5_overlap_case_622(self):
        self.assertEqual(pattern_match('jrsxtjrsxtjrsxtjrsxtjrsxtjrsxtjrsxtjrsxtjrsxtjrsxtjrsxtjrsxtjrsxtjrsxtjrsxtj', 'jrsxtj'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70])

    def test_min5_overlap_case_623(self):
        self.assertEqual(pattern_match('nnnnnnnnnnnn', 'nn'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_min5_overlap_case_624(self):
        self.assertEqual(pattern_match('iiiiiiiiiiiiiiiiiiiii', 'ii'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_min5_overlap_case_625(self):
        self.assertEqual(pattern_match('whpwhpwhpwhpwhpwhpwhpwh', 'whpwh'), [0, 3, 6, 9, 12, 15, 18])

    def test_min5_overlap_case_626(self):
        self.assertEqual(pattern_match('mmycmmycmmycmmycmmycmmycmmycmmycmmycmmycmmycmmycmmycmmycmmycmmycmmycmmycmmycm', 'mmycm'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72])

    def test_min5_overlap_case_627(self):
        self.assertEqual(pattern_match('pppppppppppppppppp', 'pp'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    def test_min5_overlap_case_628(self):
        self.assertEqual(pattern_match('oooooooooooooo', 'oo'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_min5_overlap_case_629(self):
        self.assertEqual(pattern_match('uuuuuuuuuuuuuu', 'uu'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_min5_overlap_case_630(self):
        self.assertEqual(pattern_match('sqwssqwssqwssqwssqwssqwssqwssqwssqwssqwssqwssqwssqwssqwssqwss', 'sqwss'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56])

    def test_min5_overlap_case_631(self):
        self.assertEqual(pattern_match('xxxxxxxxxxxxxxxxxxxxx', 'xx'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_min5_overlap_case_632(self):
        self.assertEqual(pattern_match('utututututututututututututu', 'utu'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])

    def test_min5_overlap_case_633(self):
        self.assertEqual(pattern_match('ieieieieieieieieieieieieieieieieieieieiei', 'iei'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38])

    def test_min5_overlap_case_634(self):
        self.assertEqual(pattern_match('yprlqyprlqyprlqyprlqyprlqyprlqyprlqyprlqyprlqyprlqy', 'yprlqy'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45])

    def test_min5_overlap_case_635(self):
        self.assertEqual(pattern_match('iqiqiqiqiqiqiqiqiqiqiqi', 'iqi'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

    def test_min5_overlap_case_636(self):
        self.assertEqual(pattern_match('nqxnnqxnnqxnnqxnnqxnnqxnnqxnnqxnnqxnnqxnnqxnnqxnnqxnnqxnn', 'nqxnn'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52])

    def test_min5_overlap_case_637(self):
        self.assertEqual(pattern_match('lelelelelelelelelelelelelelelelel', 'lel'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])

    def test_min5_overlap_case_638(self):
        self.assertEqual(pattern_match('nmnmnmnmnmnmnmnmnmnmnmnmnmnmnmnmnmnmnmnmn', 'nmn'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38])

    def test_min5_overlap_case_639(self):
        self.assertEqual(pattern_match('okokokokokokokokokokokokokokokokoko', 'oko'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32])

    def test_min5_overlap_case_640(self):
        self.assertEqual(pattern_match('xxvvxxvvxxvvxxvvxxvvxxvvxxvvxxvvxxvvxxvvxxvvxxvvxxvvx', 'xxvvx'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48])

    def test_min5_overlap_case_641(self):
        self.assertEqual(pattern_match('bhbhbhbhbhbhb', 'bhb'), [0, 2, 4, 6, 8, 10])

    def test_min5_overlap_case_642(self):
        self.assertEqual(pattern_match('zzzzzzzzzzzzzzzzz', 'zz'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_min5_overlap_case_643(self):
        self.assertEqual(pattern_match('zcfjgzcfjgzcfjgzcfjgzcfjgzcfjgzcfjgzcfjgzcfjgzcfjgzcfjgzcfjgzcfjgzcfjgzcfjgzcfjgz', 'zcfjgz'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75])

    def test_min5_overlap_case_644(self):
        self.assertEqual(pattern_match('yyyyyyyyyyyyyyyyyy', 'yy'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    def test_min5_overlap_case_645(self):
        self.assertEqual(pattern_match('nnnnnnnnnnnnnnn', 'nn'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_min5_overlap_case_646(self):
        self.assertEqual(pattern_match('hdkshdkshdkshdkshdkshdkshdkshdkshdkshdkshdksh', 'hdksh'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40])

    def test_min5_overlap_case_647(self):
        self.assertEqual(pattern_match('oooooooooooo', 'oo'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_min5_overlap_case_648(self):
        self.assertEqual(pattern_match('xrxrxrxrxrxrxrxrx', 'xrx'), [0, 2, 4, 6, 8, 10, 12, 14])

    def test_min5_overlap_case_649(self):
        self.assertEqual(pattern_match('peylpeylpeylpeylpeylpeylpeylpeylpeylpeylpeylp', 'peylp'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40])

    def test_min5_overlap_case_650(self):
        self.assertEqual(pattern_match('ggdwggdwggdwggdwggdwggdwggdwggdwggdwggdwggdwggdwggdwggdwggdwggdwggdwggdwg', 'ggdwg'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68])

    def test_min5_overlap_case_651(self):
        self.assertEqual(pattern_match('ccccccccccc', 'cc'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_min5_overlap_case_652(self):
        self.assertEqual(pattern_match('medmedmedmedmedmedmedmedmedmedmedmedmedmedmedmedmedm', 'medm'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48])

    def test_min5_overlap_case_653(self):
        self.assertEqual(pattern_match('yqwyqwyqwyqwyqwyqwyqwyqwyqwy', 'yqwy'), [0, 3, 6, 9, 12, 15, 18, 21, 24])

    def test_min5_overlap_case_654(self):
        self.assertEqual(pattern_match('fjvfjvfjvfjvfjvfjvfjvf', 'fjvf'), [0, 3, 6, 9, 12, 15, 18])

    def test_min5_overlap_case_655(self):
        self.assertEqual(pattern_match('mdqmdqmdqmdqmdqmdqmdqmdqmdqmdqm', 'mdqm'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27])

    def test_min5_overlap_case_656(self):
        self.assertEqual(pattern_match('eeoeeoeeoeeoeeoeeoeeoeeoeeoeeoeeoeeoe', 'eeoe'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33])

    def test_min5_overlap_case_657(self):
        self.assertEqual(pattern_match('cccccccccccccccc', 'cc'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_min5_overlap_case_658(self):
        self.assertEqual(pattern_match('yyyyyyyyyyyyyyyyyyyyyy', 'yyy'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_min5_overlap_case_659(self):
        self.assertEqual(pattern_match('wbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbwbw', 'wbw'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32])

    def test_min5_overlap_case_660(self):
        self.assertEqual(pattern_match('qqqqqqqqqqqqqqqq', 'qq'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_min5_overlap_case_661(self):
        self.assertEqual(pattern_match('zzzzzzzzzzzzzzzzzzzzz', 'zz'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_min5_overlap_case_662(self):
        self.assertEqual(pattern_match('abafabafabafabafabafabafabafabafabafabafabafabafabafabafabafabafa', 'abafa'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60])

    def test_min5_overlap_case_663(self):
        self.assertEqual(pattern_match('vqnkvqnkvqnkvqnkvqnkvqnkvqnkvqnkvqnkvqnkvqnkvqnkvqnkvqnkvqnkvqnkvqnkvqnkvqnkv', 'vqnkv'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72])

    def test_min5_overlap_case_664(self):
        self.assertEqual(pattern_match('unununununununununununununu', 'unu'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])

    def test_min5_overlap_case_665(self):
        self.assertEqual(pattern_match('vvvvvvvvvvvvvvvvvvv', 'vv'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])

    def test_min5_overlap_case_666(self):
        self.assertEqual(pattern_match('ucucucucucucucucucucucucucucu', 'ucu'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26])

    def test_min5_overlap_case_667(self):
        self.assertEqual(pattern_match('bbbbbbbbbb', 'bb'), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_min5_overlap_case_668(self):
        self.assertEqual(pattern_match('hhhhhhhh', 'hh'), [0, 1, 2, 3, 4, 5, 6])

    def test_min5_overlap_case_669(self):
        self.assertEqual(pattern_match('ttttttttt', 'tt'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_min5_overlap_case_670(self):
        self.assertEqual(pattern_match('jjjjjjjjjjjjj', 'jj'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_min5_overlap_case_671(self):
        self.assertEqual(pattern_match('yyyyyyyyyyyyyyyyy', 'yy'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_min5_overlap_case_672(self):
        self.assertEqual(pattern_match('ngqngqngqngqngqngqngqn', 'ngqn'), [0, 3, 6, 9, 12, 15, 18])

    def test_min5_overlap_case_673(self):
        self.assertEqual(pattern_match('gtgtgtgtgtgtgtgtgtgtgtgtgtgtgtgtgtgtgtgtg', 'gtg'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38])

    def test_min5_overlap_case_674(self):
        self.assertEqual(pattern_match('jjjjjjjjjjjjjjjjj', 'jj'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_min5_overlap_case_675(self):
        self.assertEqual(pattern_match('fffffffffffffffff', 'ff'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_min5_overlap_case_676(self):
        self.assertEqual(pattern_match('vvvvvvvvvvvvvvvvvv', 'vv'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    def test_min5_overlap_case_677(self):
        self.assertEqual(pattern_match('ctctctctctctctctctctctc', 'ctc'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

    def test_min5_overlap_case_678(self):
        self.assertEqual(pattern_match('qqqqqqqqqq', 'qq'), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_min5_overlap_case_679(self):
        self.assertEqual(pattern_match('gegegegegegegegegegegegegegeg', 'geg'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26])

    def test_min5_overlap_case_680(self):
        self.assertEqual(pattern_match('hyhyhyhyhyhyhyhyhyhyhyhyhyhyhyhyhyhyhyhyh', 'hyh'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38])

    def test_min5_overlap_case_681(self):
        self.assertEqual(pattern_match('qstpqstpqstpqstpqstpqstpqstpqstpqstpqstpqstpqstpqstpq', 'qstpq'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48])

    def test_min5_overlap_case_682(self):
        self.assertEqual(pattern_match('ttttttttttttttttttttt', 'tt'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_min5_overlap_case_683(self):
        self.assertEqual(pattern_match('znznznznznznznznznznznznznz', 'znz'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])

    def test_min5_overlap_case_684(self):
        self.assertEqual(pattern_match('ajajajajajajajajajajajajaja', 'aja'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])

    def test_min5_overlap_case_685(self):
        self.assertEqual(pattern_match('ymiymiymiymiymiymiymiymiymiymiy', 'ymiy'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27])

    def test_min5_overlap_case_686(self):
        self.assertEqual(pattern_match('ozozozozozozozozozozozozozozozozo', 'ozo'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])

    def test_min5_overlap_case_687(self):
        self.assertEqual(pattern_match('ppppppppp', 'ppp'), [0, 1, 2, 3, 4, 5, 6])

    def test_min5_overlap_case_688(self):
        self.assertEqual(pattern_match('adjadjadjadjadjadjadjadjadjadjadjadjadjadjadjadja', 'adja'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45])

    def test_min5_overlap_case_689(self):
        self.assertEqual(pattern_match('ccccccccc', 'cc'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_min5_overlap_case_690(self):
        self.assertEqual(pattern_match('xxxxxxxxxx', 'xx'), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_min5_overlap_case_691(self):
        self.assertEqual(pattern_match('upwupwupwupwupwupwupwupwupwupwupwupwupwupwupwu', 'upwu'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42])

    def test_min5_overlap_case_692(self):
        self.assertEqual(pattern_match('gdtgdtgdtgdtgdtgdtgdtgdtgdtgdtg', 'gdtg'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27])

    def test_min5_overlap_case_693(self):
        self.assertEqual(pattern_match('hhhhhhhhhhhhhh', 'hh'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_min5_overlap_case_694(self):
        self.assertEqual(pattern_match('ckxdckxdckxdckxdckxdckxdckxdc', 'ckxdc'), [0, 4, 8, 12, 16, 20, 24])

    def test_min5_overlap_case_695(self):
        self.assertEqual(pattern_match('wwwwwwwwwwwwwwwww', 'ww'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_min5_overlap_case_696(self):
        self.assertEqual(pattern_match('wxowxowxowxowxowxowxowxowxowxowxowxowxow', 'wxow'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36])

    def test_min5_overlap_case_697(self):
        self.assertEqual(pattern_match('bbbbbbb', 'bb'), [0, 1, 2, 3, 4, 5])

    def test_min5_overlap_case_698(self):
        self.assertEqual(pattern_match('gdegdegdegdegdegdegdegdegdegdeg', 'gdeg'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27])

    def test_min5_overlap_case_699(self):
        self.assertEqual(pattern_match('xxdxxdxxdxxdxxdxxdx', 'xxdx'), [0, 3, 6, 9, 12, 15])

    def test_min5_overlap_case_700(self):
        self.assertEqual(pattern_match('efefefefefefefefefefefefefe', 'efe'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])

    def test_min5_overlap_case_701(self):
        self.assertEqual(pattern_match('nenenenenenenenenenenenenenenenen', 'nen'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])

    def test_min5_overlap_case_702(self):
        self.assertEqual(pattern_match('tokwtokwtokwtokwtokwtokwtokwtokwtokwt', 'tokwt'), [0, 4, 8, 12, 16, 20, 24, 28, 32])

    def test_min5_overlap_case_703(self):
        self.assertEqual(pattern_match('dbwrwdbwrwdbwrwdbwrwdbwrwdbwrwdbwrwdbwrwdbwrwdbwrwdbwrwdbwrwdbwrwdbwrwdbwrwdbwrwdbwrwdbwrwdbwrwd', 'dbwrwd'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90])

    def test_min5_overlap_case_704(self):
        self.assertEqual(pattern_match('orvmorvmorvmorvmorvmorvmo', 'orvmo'), [0, 4, 8, 12, 16, 20])

    def test_min5_overlap_case_705(self):
        self.assertEqual(pattern_match('pppppppppp', 'pp'), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_min5_overlap_case_706(self):
        self.assertEqual(pattern_match('radohradohradohradohradohradohradohradohr', 'radohr'), [0, 5, 10, 15, 20, 25, 30, 35])

    def test_min5_overlap_case_707(self):
        self.assertEqual(pattern_match('udududududududu', 'udu'), [0, 2, 4, 6, 8, 10, 12])

    def test_min5_overlap_case_708(self):
        self.assertEqual(pattern_match('sknsknsknsknsknsknsknsknsknsknskns', 'skns'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30])

    def test_min5_overlap_case_709(self):
        self.assertEqual(pattern_match('jljljljljljljljljljljljlj', 'jlj'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22])

    def test_min5_overlap_case_710(self):
        self.assertEqual(pattern_match('uyuuyuuyuuyuuyuuyuuyuuyuuyuuyuuyuuyuuyuuyuuyuuyuuyuuyuuyuu', 'uyuu'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54])

    def test_min5_overlap_case_711(self):
        self.assertEqual(pattern_match('lyblyblyblyblyblyblyblyblyblyblyblyblyblybl', 'lybl'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39])

    def test_min5_overlap_case_712(self):
        self.assertEqual(pattern_match('aqaqaqaqaqaqaqaqaqaqaqa', 'aqa'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

    def test_min5_overlap_case_713(self):
        self.assertEqual(pattern_match('zzzzzzz', 'zz'), [0, 1, 2, 3, 4, 5])

    def test_min5_overlap_case_714(self):
        self.assertEqual(pattern_match('gggggggggggggg', 'gg'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_min5_overlap_case_715(self):
        self.assertEqual(pattern_match('aaaaaaaa', 'aa'), [0, 1, 2, 3, 4, 5, 6])

    def test_min5_overlap_case_716(self):
        self.assertEqual(pattern_match('ulqwulqwulqwulqwulqwulqwulqwulqwulqwulqwulqwulqwu', 'ulqwu'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44])

    def test_min5_overlap_case_717(self):
        self.assertEqual(pattern_match('ipgipgipgipgipgipgipgipgipgipgipgipgipgipgipgi', 'ipgi'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42])

    def test_min5_overlap_case_718(self):
        self.assertEqual(pattern_match('fffffffffffffffffffff', 'ff'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_min5_overlap_case_719(self):
        self.assertEqual(pattern_match('nfnfnfnfnfnfnfnfn', 'nfn'), [0, 2, 4, 6, 8, 10, 12, 14])

    def test_min5_overlap_case_720(self):
        self.assertEqual(pattern_match('cccccccccccccccccccc', 'cc'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    def test_min5_overlap_case_721(self):
        self.assertEqual(pattern_match('uuuuuuuuu', 'uu'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_min5_overlap_case_722(self):
        self.assertEqual(pattern_match('nnnnnnnnnnnnnnnnnnnnn', 'nn'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_min5_overlap_case_723(self):
        self.assertEqual(pattern_match('mztmztmztmztmztmztmztmztmztmztmztmztmztmztmztmztm', 'mztm'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45])

    def test_min5_overlap_case_724(self):
        self.assertEqual(pattern_match('moknkmoknkmoknkmoknkmoknkmoknkmoknkmoknkmoknkmoknkmoknkmoknkmoknkmoknkmoknkmoknkmoknkmoknkm', 'moknkm'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85])

    def test_min5_overlap_case_725(self):
        self.assertEqual(pattern_match('wwwwwwwwwww', 'ww'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_min5_overlap_case_726(self):
        self.assertEqual(pattern_match('kbkbkbkbkbkbkbkbkbkbkbkbkbkbkbk', 'kbk'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28])

    def test_min5_overlap_case_727(self):
        self.assertEqual(pattern_match('yaiyyaiyyaiyyaiyyaiyyaiyyaiyyaiyyaiyyaiyyaiyy', 'yaiyy'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40])

    def test_min5_overlap_case_728(self):
        self.assertEqual(pattern_match('pppppppppppppppppppp', 'pp'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    def test_min5_overlap_case_729(self):
        self.assertEqual(pattern_match('gigigigigigigigigigigigigigigig', 'gig'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28])

    def test_min5_overlap_case_730(self):
        self.assertEqual(pattern_match('fffffffffffffffffffffffffffffffffff', 'fff'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32])

    def test_min5_overlap_case_731(self):
        self.assertEqual(pattern_match('tttttttttttttttt', 'tt'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_min5_overlap_case_732(self):
        self.assertEqual(pattern_match('wawawawawawawaw', 'waw'), [0, 2, 4, 6, 8, 10, 12])

    def test_min5_overlap_case_733(self):
        self.assertEqual(pattern_match('xxqzxxqzxxqzxxqzxxqzxxqzxxqzxxqzxxqzxxqzxxqzxxqzxxqzxxqzxxqzxxqzxxqzxxqzxxqzx', 'xxqzx'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72])

    def test_min5_overlap_case_734(self):
        self.assertEqual(pattern_match('qgqgqgqgqgqgq', 'qgq'), [0, 2, 4, 6, 8, 10])

    def test_min5_overlap_case_735(self):
        self.assertEqual(pattern_match('aaaaaaa', 'aa'), [0, 1, 2, 3, 4, 5])

    def test_min5_overlap_case_736(self):
        self.assertEqual(pattern_match('lllllllllll', 'll'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_min5_overlap_case_737(self):
        self.assertEqual(pattern_match('ocmbyocmbyocmbyocmbyocmbyocmbyocmbyocmbyocmbyocmbyocmbyocmbyocmbyocmbyocmbyocmbyocmbyocmbyocmbyo', 'ocmbyo'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90])

    def test_min5_overlap_case_738(self):
        self.assertEqual(pattern_match('hrkhrkhrkhrkhrkhrkhrkhrkhrkhrkhrkhrkhrkh', 'hrkh'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36])

    def test_min5_overlap_case_739(self):
        self.assertEqual(pattern_match('wcwwcwwcwwcwwcwwcwwcwwcwwcwwcwwcwwcwwcwwcwwcwwcww', 'wcww'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45])

    def test_min5_overlap_case_740(self):
        self.assertEqual(pattern_match('dddddddddddddd', 'dd'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_min5_overlap_case_741(self):
        self.assertEqual(pattern_match('iiiiiiiiiii', 'ii'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_min5_overlap_case_742(self):
        self.assertEqual(pattern_match('xxxxxxxxxxxxxx', 'xx'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_min5_overlap_case_743(self):
        self.assertEqual(pattern_match('uuuuuuuuuuuuuuuuuuuu', 'uu'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    def test_min5_overlap_case_744(self):
        self.assertEqual(pattern_match('yyyyyyyy', 'yy'), [0, 1, 2, 3, 4, 5, 6])

    def test_min5_overlap_case_745(self):
        self.assertEqual(pattern_match('cqcqcqcqcqcqcqcqcqcqcqcqcqcqcqcqcqc', 'cqc'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32])

    def test_min5_overlap_case_746(self):
        self.assertEqual(pattern_match('kzxkzxkzxkzxkzxkzxkzxkzxkzxkzxkzxkzxkzxkzxkzxkzxkzxkzxk', 'kzxk'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51])

    def test_min5_overlap_case_747(self):
        self.assertEqual(pattern_match('vvvvvvvvv', 'vv'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_min5_overlap_case_748(self):
        self.assertEqual(pattern_match('lplplplplplplpl', 'lpl'), [0, 2, 4, 6, 8, 10, 12])

    def test_min5_overlap_case_749(self):
        self.assertEqual(pattern_match('nnnnnnnnnnnn', 'nn'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_min5_overlap_case_750(self):
        self.assertEqual(pattern_match('kkkkkkkkk', 'kk'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_min5_overlap_case_751(self):
        self.assertEqual(pattern_match('xxkxxkxxkxxkxxkxxkxxkxxkxxkxxkxxkxxkxxkx', 'xxkx'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36])

    def test_min5_overlap_case_752(self):
        self.assertEqual(pattern_match('hcwhcwhcwhcwhcwhcwh', 'hcwh'), [0, 3, 6, 9, 12, 15])

    def test_min5_overlap_case_753(self):
        self.assertEqual(pattern_match('aaaaaaaaaaaa', 'aa'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_min5_overlap_case_754(self):
        self.assertEqual(pattern_match('lyvrmlyvrmlyvrmlyvrmlyvrmlyvrmlyvrmlyvrmlyvrmlyvrmlyvrmlyvrmlyvrmlyvrmlyvrmlyvrmlyvrml', 'lyvrml'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80])

    def test_min5_overlap_case_755(self):
        self.assertEqual(pattern_match('xcxcxcxcxcxcxcxcxcxcxcxcxcxcxcxcxcxcxcxcx', 'xcx'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38])

    def test_min5_overlap_case_756(self):
        self.assertEqual(pattern_match('bsbsbsbsbsbsbsbsbsbsbsbsb', 'bsb'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22])

    def test_min5_overlap_case_757(self):
        self.assertEqual(pattern_match('lgelgelgelgelgelgelgelgelgelgelgelgelgelgel', 'lgel'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39])

    def test_min5_overlap_case_758(self):
        self.assertEqual(pattern_match('iiiiiiiiiiiiiiiiii', 'ii'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    def test_min5_overlap_case_759(self):
        self.assertEqual(pattern_match('lllllllll', 'll'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_min5_overlap_case_760(self):
        self.assertEqual(pattern_match('bibibibibibibibibibibibib', 'bib'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22])

    def test_min5_overlap_case_761(self):
        self.assertEqual(pattern_match('ooooooooooooo', 'oo'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_min5_overlap_case_762(self):
        self.assertEqual(pattern_match('ooooooooo', 'oo'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_min5_overlap_case_763(self):
        self.assertEqual(pattern_match('emhemhemhemhemhemhemhe', 'emhe'), [0, 3, 6, 9, 12, 15, 18])

    def test_min5_overlap_case_764(self):
        self.assertEqual(pattern_match('nnnnnnnnnnnnnnnnnnnnn', 'nn'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_min5_overlap_case_765(self):
        self.assertEqual(pattern_match('iiiiiiiii', 'ii'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_min5_overlap_case_766(self):
        self.assertEqual(pattern_match('wwwwwwwwwwwwwwwwwww', 'ww'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])

    def test_min5_overlap_case_767(self):
        self.assertEqual(pattern_match('aaaaaaaaaaaa', 'aa'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_min5_overlap_case_768(self):
        self.assertEqual(pattern_match('bglovbglovbglovbglovbglovbglovbglovbglovbglovbglovbglovbglovbglovbglovbglovbglovb', 'bglovb'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75])

    def test_min5_overlap_case_769(self):
        self.assertEqual(pattern_match('ttttttttttttttttttttt', 'tt'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_min5_overlap_case_770(self):
        self.assertEqual(pattern_match('lvdslvdslvdslvdslvdslvdslvdslvdslvdslvdslvdslvdsl', 'lvdsl'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44])

    def test_min5_overlap_case_771(self):
        self.assertEqual(pattern_match('iiiiiiiiiiiiii', 'ii'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_min5_overlap_case_772(self):
        self.assertEqual(pattern_match('xdxdxdxdxdxdxdxdxdxdxdx', 'xdx'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

    def test_min5_overlap_case_773(self):
        self.assertEqual(pattern_match('aswaswaswaswaswaswaswaswaswa', 'aswa'), [0, 3, 6, 9, 12, 15, 18, 21, 24])

    def test_min5_overlap_case_774(self):
        self.assertEqual(pattern_match('mmmmmmmmmmmmm', 'mm'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_min5_overlap_case_775(self):
        self.assertEqual(pattern_match('xjwhxjwhxjwhxjwhxjwhxjwhxjwhxjwhxjwhxjwhxjwhxjwhxjwhxjwhxjwhxjwhxjwhxjwhxjwhxj', 'xjwhxj'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72])

    def test_min5_overlap_case_776(self):
        self.assertEqual(pattern_match('dldldldldldldldldldldldldldldld', 'dld'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28])

    def test_min5_overlap_case_777(self):
        self.assertEqual(pattern_match('aoaoaoaoaoaoaoaoaoa', 'aoa'), [0, 2, 4, 6, 8, 10, 12, 14, 16])

    def test_min5_overlap_case_778(self):
        self.assertEqual(pattern_match('blblblblblblblblblblblb', 'blb'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

    def test_min5_overlap_case_779(self):
        self.assertEqual(pattern_match('kpkpkpkpkpkpkpkpkpkpkpkpkpkpkpk', 'kpk'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28])

    def test_min5_overlap_case_780(self):
        self.assertEqual(pattern_match('dhdhdhdhdhdhdhdhdhdhdhdhdhdhdhd', 'dhd'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28])

    def test_min5_overlap_case_781(self):
        self.assertEqual(pattern_match('rdrdrdrdrdrdrdrdr', 'rdr'), [0, 2, 4, 6, 8, 10, 12, 14])

    def test_min5_overlap_case_782(self):
        self.assertEqual(pattern_match('yiersyiersyiersyiersyiersyiersyiersyiersyiersyiersyiersyiersyiersyiersyiersyiersyiersyiersy', 'yiersy'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85])

    def test_min5_overlap_case_783(self):
        self.assertEqual(pattern_match('sssssssssss', 'ss'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_min5_overlap_case_784(self):
        self.assertEqual(pattern_match('jnjnjnjnjnjnjnjnjnjnjnjnjnjnjnjnjnj', 'jnj'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32])

    def test_min5_overlap_case_785(self):
        self.assertEqual(pattern_match('jjjjjjjjjjjjjjjjj', 'jj'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_min5_overlap_case_786(self):
        self.assertEqual(pattern_match('etmetmetmetmetmetmetmetmetmetmetmetmetmetmetmetmetmetmetmetme', 'etme'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57])

    def test_min5_overlap_case_787(self):
        self.assertEqual(pattern_match('mmmmmmmmmmmm', 'mm'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_min5_overlap_case_788(self):
        self.assertEqual(pattern_match('vvvvvvvv', 'vv'), [0, 1, 2, 3, 4, 5, 6])

    def test_min5_overlap_case_789(self):
        self.assertEqual(pattern_match('ffffffffffffff', 'ff'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_min5_overlap_case_790(self):
        self.assertEqual(pattern_match('zzzlzzzlzzzlzzzlzzzlzzzlzzzlzzzlzzzlzzzlzzzlzzzlzzzlzzzlzzzlzzzlzzzlz', 'zzzlz'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64])

    def test_min5_overlap_case_791(self):
        self.assertEqual(pattern_match('bbbbbbbbbbbbb', 'bb'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_min5_overlap_case_792(self):
        self.assertEqual(pattern_match('qlavtqlavtqlavtqlavtqlavtqlavtqlavtqlavtqlavtq', 'qlavtq'), [0, 5, 10, 15, 20, 25, 30, 35, 40])

    def test_min5_overlap_case_793(self):
        self.assertEqual(pattern_match('tttttttttttttttttt', 'tt'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    def test_min5_overlap_case_794(self):
        self.assertEqual(pattern_match('ozfozfozfozfozfozfozfozfozfozfozfozfozfozfozfozfozfo', 'ozfo'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48])

    def test_min5_overlap_case_795(self):
        self.assertEqual(pattern_match('bbbbbbbbbbb', 'bb'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_min5_overlap_case_796(self):
        self.assertEqual(pattern_match('gvgvgvgvgvgvgvgvgv', 'gvgv'), [0, 2, 4, 6, 8, 10, 12, 14])

    def test_min5_overlap_case_797(self):
        self.assertEqual(pattern_match('fofofofofofofofofofofofofofofofofofofof', 'fof'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36])

    def test_min5_overlap_case_798(self):
        self.assertEqual(pattern_match('bbbbbbbbbbbbbb', 'bb'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_min5_overlap_case_799(self):
        self.assertEqual(pattern_match('dwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwd', 'dwd'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36])

    def test_min5_overlap_case_800(self):
        self.assertEqual(pattern_match('uuuuuuuuuuuuuuuuuuu', 'uu'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])

    def test_min5_overlap_case_801(self):
        self.assertEqual(pattern_match('ooooooooooooooooooo', 'oo'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])

    def test_min5_overlap_case_802(self):
        self.assertEqual(pattern_match('kqcwkqcwkqcwkqcwkqcwkqcwkqcwk', 'kqcwk'), [0, 4, 8, 12, 16, 20, 24])

    def test_min5_overlap_case_803(self):
        self.assertEqual(pattern_match('ydydydydydydydydydydydy', 'ydy'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

    def test_min5_overlap_case_804(self):
        self.assertEqual(pattern_match('wwwwwwwwww', 'ww'), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_min5_overlap_case_805(self):
        self.assertEqual(pattern_match('ebaebaebaebaebaebaebaebaebaebaebaebaebaebae', 'ebae'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39])

    def test_min5_overlap_case_806(self):
        self.assertEqual(pattern_match('nkankankankankankankankankankan', 'nkan'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27])

    def test_min5_overlap_case_807(self):
        self.assertEqual(pattern_match('dddddddd', 'dd'), [0, 1, 2, 3, 4, 5, 6])

    def test_min5_overlap_case_808(self):
        self.assertEqual(pattern_match('bwwrybwwrybwwrybwwrybwwrybwwrybwwrybwwrybwwrybwwrybwwrybwwrybwwrybwwrybwwrybwwrybwwryb', 'bwwryb'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80])

    def test_min5_overlap_case_809(self):
        self.assertEqual(pattern_match('sksksksksksksksksksksksksksksksks', 'sks'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])

    def test_min5_overlap_case_810(self):
        self.assertEqual(pattern_match('gxgxgxgxgxgxgxgxgxgxgxg', 'gxg'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

    def test_min5_overlap_case_811(self):
        self.assertEqual(pattern_match('tatatatatatatatatatatatatatatatatatatat', 'tat'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36])

    def test_min5_overlap_case_812(self):
        self.assertEqual(pattern_match('vvvvvvvvvvvvvvvvvvvv', 'vv'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    def test_min5_overlap_case_813(self):
        self.assertEqual(pattern_match('uuuuuuuuu', 'uu'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_min5_overlap_case_814(self):
        self.assertEqual(pattern_match('aaaaaaaaaaaaaaaa', 'aa'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_min5_overlap_case_815(self):
        self.assertEqual(pattern_match('xxxxxxxxxxxxxxx', 'xx'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_min5_overlap_case_816(self):
        self.assertEqual(pattern_match('uuvyouuvyouuvyouuvyouuvyouuvyou', 'uuvyou'), [0, 5, 10, 15, 20, 25])

    def test_min5_overlap_case_817(self):
        self.assertEqual(pattern_match('uuuuuuuuuuuuuu', 'uu'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_min5_overlap_case_818(self):
        self.assertEqual(pattern_match('ssssssssssssss', 'ss'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_min5_overlap_case_819(self):
        self.assertEqual(pattern_match('sssssssssssss', 'ss'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_min5_overlap_case_820(self):
        self.assertEqual(pattern_match('nnnnnnn', 'nn'), [0, 1, 2, 3, 4, 5])

    def test_min5_overlap_case_821(self):
        self.assertEqual(pattern_match('isisisisisisisisisi', 'isi'), [0, 2, 4, 6, 8, 10, 12, 14, 16])

    def test_min5_overlap_case_822(self):
        self.assertEqual(pattern_match('oooooooooooooooo', 'oo'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_min5_overlap_case_823(self):
        self.assertEqual(pattern_match('ebuqebuqebuqebuqebuqebuqebuqebuqebuqebuqebuqebuqebuqebuqebuqebuqebuqebuqebuqebuqe', 'ebuqe'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76])

    def test_min5_overlap_case_824(self):
        self.assertEqual(pattern_match('mmmmmmmmmmm', 'mm'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_min5_overlap_case_825(self):
        self.assertEqual(pattern_match('ououououououououououououououo', 'ouo'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26])

    def test_min5_overlap_case_826(self):
        self.assertEqual(pattern_match('kfkfkfkfkfkfkfkfkfkfkfkfkfkfkfkfkfkfkfkfk', 'kfk'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38])

    def test_min5_overlap_case_827(self):
        self.assertEqual(pattern_match('hhhhhhhhhhhh', 'hh'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_min5_overlap_case_828(self):
        self.assertEqual(pattern_match('jjjjjjjjj', 'jj'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_min5_overlap_case_829(self):
        self.assertEqual(pattern_match('dzizdzizdzizdzizdzizdzizd', 'dzizd'), [0, 4, 8, 12, 16, 20])

    def test_min5_overlap_case_830(self):
        self.assertEqual(pattern_match('umumumumumumumumumumumumumumumumumu', 'umu'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32])

    def test_min5_overlap_case_831(self):
        self.assertEqual(pattern_match('yyyyyyyyyyyyyyyyyyyyy', 'yy'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_min5_overlap_case_832(self):
        self.assertEqual(pattern_match('axaxaxaxaxaxax', 'axax'), [0, 2, 4, 6, 8, 10])

    def test_min5_overlap_case_833(self):
        self.assertEqual(pattern_match('rrrrrrrrrrrrrrrr', 'rr'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_min5_overlap_case_834(self):
        self.assertEqual(pattern_match('nnnnnnnnnnnnnn', 'nn'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_min5_overlap_case_835(self):
        self.assertEqual(pattern_match('wmyswmyswmyswmyswmyswmyswmyswmyswmyswmyswmyswmyswmyswmyswmyswmyswmysw', 'wmysw'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64])

    def test_min5_overlap_case_836(self):
        self.assertEqual(pattern_match('wxwwxwwxwwxwwxwwxwwxwwxww', 'wxww'), [0, 3, 6, 9, 12, 15, 18, 21])

    def test_min5_overlap_case_837(self):
        self.assertEqual(pattern_match('ttttttttttttttt', 'tt'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_min5_overlap_case_838(self):
        self.assertEqual(pattern_match('ffffffffffffff', 'ff'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_min5_overlap_case_839(self):
        self.assertEqual(pattern_match('cgcgcgcgcgcgcgcgcgcgcgcgcgcgc', 'cgc'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26])

    def test_min5_overlap_case_840(self):
        self.assertEqual(pattern_match('fzfzfzfzfzfzfzfzfzfzfzfzf', 'fzf'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22])

    def test_min5_overlap_case_841(self):
        self.assertEqual(pattern_match('kdheykdheykdheykdheykdheykdheykdheykdheykdheykdheykdheykdheykdheykdheykdheykdheykdheykdheykdheykdheyk', 'kdheyk'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95])

    def test_min5_overlap_case_842(self):
        self.assertEqual(pattern_match('tftftftftftftftftftftftftftftftft', 'tft'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])

    def test_min5_overlap_case_843(self):
        self.assertEqual(pattern_match('uuuuuuu', 'uu'), [0, 1, 2, 3, 4, 5])

    def test_min5_overlap_case_844(self):
        self.assertEqual(pattern_match('sssssssssssssss', 'ss'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_min5_overlap_case_845(self):
        self.assertEqual(pattern_match('hhhhhhhhhhhhhhhhhh', 'hh'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    def test_min5_overlap_case_846(self):
        self.assertEqual(pattern_match('tttttttttttt', 'tt'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_min5_overlap_case_847(self):
        self.assertEqual(pattern_match('ccccccccc', 'cc'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_min5_overlap_case_848(self):
        self.assertEqual(pattern_match('asuasuasuasuasuasuasuasuasuasuasuasua', 'asua'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33])

    def test_min5_overlap_case_849(self):
        self.assertEqual(pattern_match('nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn', 'nnn'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34])

    def test_min5_overlap_case_850(self):
        self.assertEqual(pattern_match('ocwocwocwocwocwocwocwo', 'ocwo'), [0, 3, 6, 9, 12, 15, 18])

    def test_min5_overlap_case_851(self):
        self.assertEqual(pattern_match('iiiiiiiiiiiiiiiiii', 'ii'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    def test_min5_overlap_case_852(self):
        self.assertEqual(pattern_match('ebsebsebsebsebsebsebsebsebsebsebsebsebsebsebsebsebsebsebsebse', 'ebse'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57])

    def test_min5_overlap_case_853(self):
        self.assertEqual(pattern_match('mlyvmlyvmlyvmlyvmlyvmlyvmlyvmlyvmlyvmlyvmlyvmlyvmlyvmlyvmlyvmlyvmlyvmlyvmlyvm', 'mlyvm'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72])

    def test_min5_overlap_case_854(self):
        self.assertEqual(pattern_match('vvvvvvvvv', 'vv'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_min5_overlap_case_855(self):
        self.assertEqual(pattern_match('inininininininininini', 'ini'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])

    def test_min5_overlap_case_856(self):
        self.assertEqual(pattern_match('vzbhhvzbhhvzbhhvzbhhvzbhhvzbhhvzbhhvzbhhvzbhhvzbhhvzbhhvzbhhvzbhhvzbhhv', 'vzbhhv'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65])

    def test_min5_overlap_case_857(self):
        self.assertEqual(pattern_match('vhvhvhvhvhvhvhvhvhv', 'vhv'), [0, 2, 4, 6, 8, 10, 12, 14, 16])

    def test_min5_overlap_case_858(self):
        self.assertEqual(pattern_match('jjjjjjjjjjjjjj', 'jj'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_min5_overlap_case_859(self):
        self.assertEqual(pattern_match('rrrrrrrrrrr', 'rr'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_min5_overlap_case_860(self):
        self.assertEqual(pattern_match('xcxcxcxcxcxcxcxcxcx', 'xcx'), [0, 2, 4, 6, 8, 10, 12, 14, 16])

    def test_min5_overlap_case_861(self):
        self.assertEqual(pattern_match('eiekeiekeiekeiekeiekeiekeiekeiekeiekeieke', 'eieke'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36])

    def test_min5_overlap_case_862(self):
        self.assertEqual(pattern_match('vyrvyrvyrvyrvyrvyrvyrvyrvyrvyrvyrv', 'vyrv'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30])

    def test_min5_overlap_case_863(self):
        self.assertEqual(pattern_match('uuuuuuuuuuuuuuuuuuuuu', 'uu'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_min5_overlap_case_864(self):
        self.assertEqual(pattern_match('eaeaeaeaeaeaeaeaeaeaeaeaeae', 'eae'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])

    def test_min5_overlap_case_865(self):
        self.assertEqual(pattern_match('cgcgcgcgcgcgcgcgcgc', 'cgc'), [0, 2, 4, 6, 8, 10, 12, 14, 16])

    def test_min5_overlap_case_866(self):
        self.assertEqual(pattern_match('liygliygliygliygliygliygliygliygl', 'liygl'), [0, 4, 8, 12, 16, 20, 24, 28])

    def test_min5_overlap_case_867(self):
        self.assertEqual(pattern_match('lllllllllllllllll', 'll'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_min5_overlap_case_868(self):
        self.assertEqual(pattern_match('jjctjjctjjctjjctjjctjjctjjctjjctjjctjjctjjctjjctjjctjjctj', 'jjctj'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52])

    def test_min5_overlap_case_869(self):
        self.assertEqual(pattern_match('rxrxrxrxrxrxrxrxrxrxrxrxrxr', 'rxr'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])

    def test_min5_overlap_case_870(self):
        self.assertEqual(pattern_match('iiiiiiiii', 'ii'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_min5_overlap_case_871(self):
        self.assertEqual(pattern_match('cwcqcwcqcwcqcwcqcwcqcwcqcwcqcwcqc', 'cwcqc'), [0, 4, 8, 12, 16, 20, 24, 28])

    def test_min5_overlap_case_872(self):
        self.assertEqual(pattern_match('vqvqvqvqvqvqvqvqvqvqvqvqvqvqvqvqv', 'vqv'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])

    def test_min5_overlap_case_873(self):
        self.assertEqual(pattern_match('rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr', 'rrr'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32])

    def test_min5_overlap_case_874(self):
        self.assertEqual(pattern_match('jjjjjjjjjjjjjj', 'jj'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_min5_overlap_case_875(self):
        self.assertEqual(pattern_match('hhhhhhhhhhhhhhhhhhhh', 'hh'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    def test_min5_overlap_case_876(self):
        self.assertEqual(pattern_match('sssssssssssssssssss', 'ss'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])

    def test_min5_overlap_case_877(self):
        self.assertEqual(pattern_match('nybnybnybnybnybnybnybnybnybnybnybn', 'nybn'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30])

    def test_min5_overlap_case_878(self):
        self.assertEqual(pattern_match('gbsgbsgbsgbsgbsgbsgbsgbsgbsgbsgbsgbsgbsgbsgbsgbsgbsgbsgbsg', 'gbsg'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54])

    def test_min5_overlap_case_879(self):
        self.assertEqual(pattern_match('oooooooooooooooo', 'oo'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_min5_overlap_case_880(self):
        self.assertEqual(pattern_match('urtiurtiurtiurtiurtiurtiurtiurtiurtiurtiurtiu', 'urtiu'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40])

    def test_min5_overlap_case_881(self):
        self.assertEqual(pattern_match('iiiiiiiiiiiii', 'ii'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_min5_overlap_case_882(self):
        self.assertEqual(pattern_match('bbbbbbbbbb', 'bb'), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_min5_overlap_case_883(self):
        self.assertEqual(pattern_match('mbmbmbmbmbmbmbmbmbmbmbmbmbmbmbmbmbmbm', 'mbm'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34])

    def test_min5_overlap_case_884(self):
        self.assertEqual(pattern_match('wwwwwwwww', 'ww'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_min5_overlap_case_885(self):
        self.assertEqual(pattern_match('ffffffffffffffffffff', 'ff'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    def test_min5_overlap_case_886(self):
        self.assertEqual(pattern_match('bibibibibibibibib', 'bib'), [0, 2, 4, 6, 8, 10, 12, 14])

    def test_min5_overlap_case_887(self):
        self.assertEqual(pattern_match('qyfqyfqyfqyfqyfqyfqyfqyfqyfqyfqyfqyfqyfqyfqyfqyfq', 'qyfq'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45])

    def test_min5_overlap_case_888(self):
        self.assertEqual(pattern_match('smsmsmsmsmsmsmsmsms', 'sms'), [0, 2, 4, 6, 8, 10, 12, 14, 16])

    def test_min5_overlap_case_889(self):
        self.assertEqual(pattern_match('bbbbbbbb', 'bb'), [0, 1, 2, 3, 4, 5, 6])

    def test_min5_overlap_case_890(self):
        self.assertEqual(pattern_match('plrzbplrzbplrzbplrzbplrzbplrzbplrzbplrzbplrzbplrzbplrzbp', 'plrzbp'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50])

    def test_min5_overlap_case_891(self):
        self.assertEqual(pattern_match('tptntptntptntptntptntptntptntptntptnt', 'tptnt'), [0, 4, 8, 12, 16, 20, 24, 28, 32])

    def test_min5_overlap_case_892(self):
        self.assertEqual(pattern_match('djqphdjqphdjqphdjqphdjqphdjqphdjqphdjqphd', 'djqphd'), [0, 5, 10, 15, 20, 25, 30, 35])

    def test_min5_overlap_case_893(self):
        self.assertEqual(pattern_match('vtvtvtvtvtvtvtvtvtvtvtv', 'vtv'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

    def test_min5_overlap_case_894(self):
        self.assertEqual(pattern_match('sjxsjxsjxsjxsjxsjxsjxsjxsjxsjxs', 'sjxs'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27])

    def test_min5_overlap_case_895(self):
        self.assertEqual(pattern_match('dadadadadadadadadad', 'dad'), [0, 2, 4, 6, 8, 10, 12, 14, 16])

    def test_min5_overlap_case_896(self):
        self.assertEqual(pattern_match('ddddddddd', 'dd'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_min5_overlap_case_897(self):
        self.assertEqual(pattern_match('tjtiqtjtiqtjtiqtjtiqtjtiqtjtiqtjtiqtjtiqtjtiqtjtiqtjtiqtjtiqtjtiqtjtiqtjtiqt', 'tjtiqt'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70])

    def test_min5_overlap_case_898(self):
        self.assertEqual(pattern_match('jfjfjfjfjfjfjfjfjfjfjfjfjfjfjfjfjfjfjfjfj', 'jfj'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38])

    def test_min5_overlap_case_899(self):
        self.assertEqual(pattern_match('qqqqqqqqqqqqqqqqqqqq', 'qq'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    def test_min5_overlap_case_900(self):
        self.assertEqual(pattern_match('tgsgtgsgtgsgtgsgtgsgtgsgtgsgtgsgtgsgtgsgtgsgtgsgt', 'tgsgt'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44])

    def test_min5_overlap_case_901(self):
        self.assertEqual(pattern_match('ooooooooooooooo', 'oo'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_min5_overlap_case_902(self):
        self.assertEqual(pattern_match('hhhhhhhhhhhhhhh', 'hh'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_min5_overlap_case_903(self):
        self.assertEqual(pattern_match('bmbmbmbmbmbmbmbmbmbmbmbmbmbmbmbmbmbmbmb', 'bmb'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36])

    def test_min5_overlap_case_904(self):
        self.assertEqual(pattern_match('vfezvfezvfezvfezvfezvfezvfezvfezvfezvfezvfezvfezvfezvfezv', 'vfezv'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52])

    def test_min5_overlap_case_905(self):
        self.assertEqual(pattern_match('kkkkkkkkkkk', 'kk'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_min5_overlap_case_906(self):
        self.assertEqual(pattern_match('anuanuanuanuanuanuanuanuanuanuanuanuanuanuanuanuanuanuanuan', 'anuan'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54])

    def test_min5_overlap_case_907(self):
        self.assertEqual(pattern_match('pppppppppppp', 'pp'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_min5_overlap_case_908(self):
        self.assertEqual(pattern_match('nnnnnnnnnnnn', 'nn'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_min5_overlap_case_909(self):
        self.assertEqual(pattern_match('yvzyvzyvzyvzyvzyvzyvzyvzyvzyvzyvzyvzyvzyvzyvzyvzy', 'yvzy'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45])

    def test_min5_overlap_case_910(self):
        self.assertEqual(pattern_match('xxxxxxxxxxxx', 'xx'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_min5_overlap_case_911(self):
        self.assertEqual(pattern_match('ddddddddddddddddd', 'dd'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_min5_overlap_case_912(self):
        self.assertEqual(pattern_match('tgfqatgfqatgfqatgfqatgfqatgfqatgfqatgfqatgfqatgfqatgfqatgfqatgfqatgfqatgfqatgfqat', 'tgfqat'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75])

    def test_min5_overlap_case_913(self):
        self.assertEqual(pattern_match('rrrrrrrrrrr', 'rr'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_min5_overlap_case_914(self):
        self.assertEqual(pattern_match('hhhhhhhhhhhh', 'hh'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_min5_overlap_case_915(self):
        self.assertEqual(pattern_match('hhhhhhhhhhhhhhhhhh', 'hh'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    def test_min5_overlap_case_916(self):
        self.assertEqual(pattern_match('lazmklazmklazmklazmklazmklazmklazmklazmklazmklazmklazmklazmkl', 'lazmkl'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55])

    def test_min5_overlap_case_917(self):
        self.assertEqual(pattern_match('ddteddteddteddteddteddted', 'ddted'), [0, 4, 8, 12, 16, 20])

    def test_min5_overlap_case_918(self):
        self.assertEqual(pattern_match('zzzzzzzzzzzzzzzzz', 'zz'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_min5_overlap_case_919(self):
        self.assertEqual(pattern_match('sqcsqcsqcsqcsqcsqcsqcsqcsqcsqcsqcsqcsqcsqcsqcsqcsqcsqcsq', 'sqcsq'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51])

    def test_min5_overlap_case_920(self):
        self.assertEqual(pattern_match('cqnwrcqnwrcqnwrcqnwrcqnwrcqnwrcqnwrcqnwrc', 'cqnwrc'), [0, 5, 10, 15, 20, 25, 30, 35])

    def test_min5_overlap_case_921(self):
        self.assertEqual(pattern_match('bbbbbbbbbbbbbbbbbbb', 'bb'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])

    def test_min5_overlap_case_922(self):
        self.assertEqual(pattern_match('rrrrrrrrrrrrrrrr', 'rr'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_min5_overlap_case_923(self):
        self.assertEqual(pattern_match('wwwwwwwwwwwwwwwwwwwww', 'ww'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_min5_overlap_case_924(self):
        self.assertEqual(pattern_match('nqnqnqnqnqnqnqnqnqnqnqnqnqnqnqnqnqn', 'nqn'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32])

    def test_min5_overlap_case_925(self):
        self.assertEqual(pattern_match('llllllllllllllll', 'll'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_min5_overlap_case_926(self):
        self.assertEqual(pattern_match('bsbsbsbsbsbsbsbsbsbsbsbsb', 'bsb'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22])

    def test_min5_overlap_case_927(self):
        self.assertEqual(pattern_match('jjjjjjjj', 'jj'), [0, 1, 2, 3, 4, 5, 6])

    def test_min5_overlap_case_928(self):
        self.assertEqual(pattern_match('wwwwwwwwwwwwwwwwwwwww', 'ww'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_min5_overlap_case_929(self):
        self.assertEqual(pattern_match('uuuuuuuuuuuuuuuuu', 'uu'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_min5_overlap_case_930(self):
        self.assertEqual(pattern_match('tttttttttttttttttttt', 'tt'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    def test_min5_overlap_case_931(self):
        self.assertEqual(pattern_match('ppppppppppppppppppppppppppppppp', 'ppp'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28])

    def test_min5_overlap_case_932(self):
        self.assertEqual(pattern_match('tkotkotkotkotkotkotkotkotkotkotkotkotkotkotkotkotkotkot', 'tkot'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51])

    def test_min5_overlap_case_933(self):
        self.assertEqual(pattern_match('kdkdkdkdkdkdkdkdkdkdkdkdkdkdkdkdkdk', 'kdk'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32])

    def test_min5_overlap_case_934(self):
        self.assertEqual(pattern_match('iiiiiiiiiiiiii', 'ii'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_min5_overlap_case_935(self):
        self.assertEqual(pattern_match('fffffffffffffffffffff', 'ff'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_min5_overlap_case_936(self):
        self.assertEqual(pattern_match('wwwwwwwwwwwwww', 'ww'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_min5_overlap_case_937(self):
        self.assertEqual(pattern_match('hhhhhhhhhhhhhh', 'hh'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_min5_overlap_case_938(self):
        self.assertEqual(pattern_match('jfjfjfjfjfjfjfjfjfjfjfjfjfjfjfjfjfjfjfj', 'jfj'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36])

    def test_min5_overlap_case_939(self):
        self.assertEqual(pattern_match('aaaaaaaa', 'aa'), [0, 1, 2, 3, 4, 5, 6])

    def test_min5_overlap_case_940(self):
        self.assertEqual(pattern_match('yimtyimtyimtyimtyimtyimtyimtyimtyimtyimtyimtyimtyimtyimtyimtyimtyimtyimty', 'yimty'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68])

    def test_min5_overlap_case_941(self):
        self.assertEqual(pattern_match('dgtexdgtexdgtexdgtexdgtexdgtexdgtexdgtexdgtexdgtexdgtexdgtexdgtexd', 'dgtexd'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])

    def test_min5_overlap_case_942(self):
        self.assertEqual(pattern_match('ufztufztufztufztufztufztufztufztufztufztufztufztu', 'ufztu'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44])

    def test_min5_overlap_case_943(self):
        self.assertEqual(pattern_match('ofpnofpnofpnofpnofpnofpnofpnofpnofpnofpnofpnofpnofpno', 'ofpno'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48])

    def test_min5_overlap_case_944(self):
        self.assertEqual(pattern_match('yncgyncgyncgyncgyncgyncgyncgyncgyncgyncgyncgyncgy', 'yncgy'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44])

    def test_min5_overlap_case_945(self):
        self.assertEqual(pattern_match('cjfbcjfbcjfbcjfbcjfbcjfbcj', 'cjfbcj'), [0, 4, 8, 12, 16, 20])

    def test_min5_overlap_case_946(self):
        self.assertEqual(pattern_match('eeeeeeeee', 'ee'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_min5_overlap_case_947(self):
        self.assertEqual(pattern_match('ttttttttttt', 'tt'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_min5_overlap_case_948(self):
        self.assertEqual(pattern_match('gggggggggggggg', 'gg'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_min5_overlap_case_949(self):
        self.assertEqual(pattern_match('bfbfbfbfbfbfbfbfbfbfbfbfbfbfbfb', 'bfb'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28])

    def test_min5_overlap_case_950(self):
        self.assertEqual(pattern_match('kkkkkkkk', 'kk'), [0, 1, 2, 3, 4, 5, 6])

    def test_min5_overlap_case_951(self):
        self.assertEqual(pattern_match('vvvvvvvvvvvvvvvv', 'vv'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_min5_overlap_case_952(self):
        self.assertEqual(pattern_match('sssssssssss', 'ss'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_min5_overlap_case_953(self):
        self.assertEqual(pattern_match('fpfpfpfpfpfpfpfpfpfpf', 'fpf'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])

    def test_min5_overlap_case_954(self):
        self.assertEqual(pattern_match('whwhwhwhwhwhwhwhwhwhwhwhwhwhwhwhwhwhwhwhw', 'whw'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38])

    def test_min5_overlap_case_955(self):
        self.assertEqual(pattern_match('onkdtonkdtonkdtonkdtonkdtonkdtonkdtonkdto', 'onkdto'), [0, 5, 10, 15, 20, 25, 30, 35])

    def test_min5_overlap_case_956(self):
        self.assertEqual(pattern_match('cmfbycmfbycmfbycmfbycmfbycmfbycmfbycmfbycmfbycmfbycmfbycmfbycmfbycmfbycmfbycmfbycmfbycmfbycmfbycmfbyc', 'cmfbyc'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95])

    def test_min5_overlap_case_957(self):
        self.assertEqual(pattern_match('ppppppppppppppp', 'pp'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_min5_overlap_case_958(self):
        self.assertEqual(pattern_match('gzgzgzgzgzgzgzgzgzgzgzgzgzgzgzgzgzgzg', 'gzg'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34])

    def test_min5_overlap_case_959(self):
        self.assertEqual(pattern_match('svasdsvasdsvasdsvasdsvasdsvasdsvasdsvasds', 'svasds'), [0, 5, 10, 15, 20, 25, 30, 35])

    def test_min5_overlap_case_960(self):
        self.assertEqual(pattern_match('zzzzzzzzzzz', 'zz'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_min5_overlap_case_961(self):
        self.assertEqual(pattern_match('qqqqqqqqqqq', 'qq'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_min5_overlap_case_962(self):
        self.assertEqual(pattern_match('jjjjjjjjjjjjjjjjjjj', 'jj'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])

    def test_min5_overlap_case_963(self):
        self.assertEqual(pattern_match('dfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfd', 'dfd'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38])

    def test_min5_overlap_case_964(self):
        self.assertEqual(pattern_match('dvdvdvdvdvdvdvdvdvdvdvdvdvdvdvd', 'dvd'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28])

    def test_min5_overlap_case_965(self):
        self.assertEqual(pattern_match('bbbbbbbbbbbbbbbbbbbb', 'bb'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    def test_min5_overlap_case_966(self):
        self.assertEqual(pattern_match('mmmmmmmmmmmmmmm', 'mm'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_min5_overlap_case_967(self):
        self.assertEqual(pattern_match('ititititititi', 'iti'), [0, 2, 4, 6, 8, 10])

    def test_min5_overlap_case_968(self):
        self.assertEqual(pattern_match('dnhdnhdnhdnhdnhdnhdnhdnhdnhdnhdnhdnhdnhd', 'dnhd'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36])

    def test_min5_overlap_case_969(self):
        self.assertEqual(pattern_match('dihdihdihdihdihdihdihdihd', 'dihd'), [0, 3, 6, 9, 12, 15, 18, 21])

    def test_min5_overlap_case_970(self):
        self.assertEqual(pattern_match('fthfthfthfthfthfthfthfthfthfthf', 'fthf'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27])

    def test_min5_overlap_case_971(self):
        self.assertEqual(pattern_match('kakakakakakakakakakak', 'kak'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])

    def test_min5_overlap_case_972(self):
        self.assertEqual(pattern_match('jtmrijtmrijtmrijtmrijtmrijtmrijtmrijtmrijtmrijtmrijtmrijtmrijtmrijtmrijtmrijtmrij', 'jtmrij'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75])

    def test_min5_overlap_case_973(self):
        self.assertEqual(pattern_match('aaaaaaa', 'aa'), [0, 1, 2, 3, 4, 5])

    def test_min5_overlap_case_974(self):
        self.assertEqual(pattern_match('nnnnnnnnn', 'nn'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_min5_overlap_case_975(self):
        self.assertEqual(pattern_match('gfgfgfgfgfgfgfgf', 'gfgf'), [0, 2, 4, 6, 8, 10, 12])

    def test_min5_overlap_case_976(self):
        self.assertEqual(pattern_match('aaaaaaaa', 'aa'), [0, 1, 2, 3, 4, 5, 6])

    def test_min5_overlap_case_977(self):
        self.assertEqual(pattern_match('hgthgthgthgthgthgthgth', 'hgth'), [0, 3, 6, 9, 12, 15, 18])

    def test_min5_overlap_case_978(self):
        self.assertEqual(pattern_match('mnjmnjmnjmnjmnjmnjmnjm', 'mnjm'), [0, 3, 6, 9, 12, 15, 18])

    def test_min5_overlap_case_979(self):
        self.assertEqual(pattern_match('hbehhhbehhhbehhhbehhhbehhhbehhhbehhhbehhhbehhhbehhhbehhhbehhhbehhhbehhhbehhhbehhhbehhh', 'hbehhh'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80])

    def test_min5_overlap_case_980(self):
        self.assertEqual(pattern_match('iiiiiiiiiii', 'ii'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_min5_overlap_case_981(self):
        self.assertEqual(pattern_match('sssssssss', 'ss'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_min5_overlap_case_982(self):
        self.assertEqual(pattern_match('wewewewewewewewewewewewewewewewewewewewe', 'wewe'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36])

    def test_min5_overlap_case_983(self):
        self.assertEqual(pattern_match('wwwwwwwwwwwwwwww', 'www'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_min5_overlap_case_984(self):
        self.assertEqual(pattern_match('qgosrqgosrqgosrqgosrqgosrqgosrqgosrqgosrqgosrqgosrqgosrqgosrqgosrq', 'qgosrq'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])

    def test_min5_overlap_case_985(self):
        self.assertEqual(pattern_match('kqpwtkqpwtkqpwtkqpwtkqpwtkqpwtkqpwtkqpwtkqpwtkqpwtkqpwtkqpwtkqpwtk', 'kqpwtk'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])

    def test_min5_overlap_case_986(self):
        self.assertEqual(pattern_match('xlyxlyxlyxlyxlyxlyxlyxlyxlyxlyxlyxlyxlyxlyxlyx', 'xlyx'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42])

    def test_min5_overlap_case_987(self):
        self.assertEqual(pattern_match('qpqpqpqpqpqpqpqpqpqpq', 'qpq'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])

    def test_min5_overlap_case_988(self):
        self.assertEqual(pattern_match('zbgifzbgifzbgifzbgifzbgifzbgifzbgifzbgifzbgifzbgifzbgifzbgifzbgifzbgifzbgifzbgifzbgifzbgifz', 'zbgifz'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85])

    def test_min5_overlap_case_989(self):
        self.assertEqual(pattern_match('eeeeeeeeeeeeeeeeeee', 'ee'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])

    def test_min5_overlap_case_990(self):
        self.assertEqual(pattern_match('emywwemywwemywwemywwemywwemywwemywwemywwemywwemywwe', 'emywwe'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45])

    def test_min5_overlap_case_991(self):
        self.assertEqual(pattern_match('iiiiiiiii', 'ii'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_min5_overlap_case_992(self):
        self.assertEqual(pattern_match('aaaaaaa', 'aa'), [0, 1, 2, 3, 4, 5])

    def test_min5_overlap_case_993(self):
        self.assertEqual(pattern_match('qqqqqqqqqqqqqqqq', 'qq'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_min5_overlap_case_994(self):
        self.assertEqual(pattern_match('xxmnxxmnxxmnxxmnxxmnxxmnxxmnx', 'xxmnx'), [0, 4, 8, 12, 16, 20, 24])

    def test_min5_overlap_case_995(self):
        self.assertEqual(pattern_match('hhhhhhh', 'hh'), [0, 1, 2, 3, 4, 5])

    def test_min5_overlap_case_996(self):
        self.assertEqual(pattern_match('dgxaadgxaadgxaadgxaadgxaadgxaad', 'dgxaad'), [0, 5, 10, 15, 20, 25])

    def test_min5_overlap_case_997(self):
        self.assertEqual(pattern_match('ssssssssssssssssss', 'ss'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    def test_min5_overlap_case_998(self):
        self.assertEqual(pattern_match('tztztztztztztztztztztztztztztztztzt', 'tzt'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32])

    def test_min5_overlap_case_999(self):
        self.assertEqual(pattern_match('jgpwjgpwjgpwjgpwjgpwjgpwjgpwjgpwj', 'jgpwj'), [0, 4, 8, 12, 16, 20, 24, 28])


if __name__ == '__main__':
    unittest.main()
