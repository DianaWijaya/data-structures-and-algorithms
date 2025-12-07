import unittest
from suffix_tree_matching import SuffixTree

def pattern_match(text, pattern):
    tree = SuffixTree(text)
    return tree.search_exact(pattern)

class TestDenseMatchCases(unittest.TestCase):
    def test_dense_case_0(self):
        self.assertEqual(pattern_match('ayxfyxfyxfyxfyxfyxfyxfyxfyxfyxfyxfyxfyxfyxfyxfyxfyxfyxfyxfyxfyxfyxfyxfyxfyxfyxfyxf', 'ayxf'), [0])

    def test_dense_case_1(self):
        self.assertEqual(pattern_match('ibebebebebebebebebebebebebebebebebebebebebebebebebebebebe', 'ibe'), [0])

    def test_dense_case_2(self):
        self.assertEqual(pattern_match('vvkjrvvkjrvvkjrvvkjrvvkjrvvkjrvvkjrvvkjrvvkjrvvkjrvvkjrvvkjrvvkjrvvkjrvvkjrvvkjrvvkjrvvkjrvvkjrvvkjrvvkjrvvkjrvvkjrvvkjrvvkjrvvkjrvvkjr', 'vvkjr'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130])

    def test_dense_case_3(self):
        self.assertEqual(pattern_match('ahrdahrdahrdahrdahrdahrdahrdahrdahrdahrdahrdahrdahrdahrdahrdahrdahrdahrdahrdahrd', 'ahrd'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76])

    def test_dense_case_4(self):
        self.assertEqual(pattern_match('utqgiutqgiutqgiutqgiutqgiutqgiutqgiutqgiutqgiutqgiutqgiutqgiutqgiutqgiutqgiutqgiutqgiutqgiutqgiutqgi', 'utqgi'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95])

    def test_dense_case_5(self):
        self.assertEqual(pattern_match('wlwlwlwlwlwlwlwlwlwlwlwlwlwlwlwlwlwlwlwl', 'wl'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38])

    def test_dense_case_6(self):
        self.assertEqual(pattern_match('bpeeeee', 'bpe'), [0])

    def test_dense_case_7(self):
        self.assertEqual(pattern_match('fxmtxfxmtxfxmtxfxmtxfxmtxfxmtxfxmtxfxmtxfxmtxfxmtxfxmtxfxmtxfxmtxfxmtxfxmtxfxmtx', 'fxmtx'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75])

    def test_dense_case_8(self):
        self.assertEqual(pattern_match('irplplplplplplplplplplplplplplplplplplplplplplplplplplplplpl', 'irpl'), [0])

    def test_dense_case_9(self):
        self.assertEqual(pattern_match('xzmmmmm', 'xzm'), [0])

    def test_dense_case_10(self):
        self.assertEqual(pattern_match('hthththththththththththththththththththththththththththththt', 'ht'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58])

    def test_dense_case_11(self):
        self.assertEqual(pattern_match('trtrtrtrtrtrtrtrtrtrtrtrtrtrtrtrtrtrtrtrtrtrtr', 'tr'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44])

    def test_dense_case_12(self):
        self.assertEqual(pattern_match('ruuuuuuuuuuu', 'ruu'), [0])

    def test_dense_case_13(self):
        self.assertEqual(pattern_match('vvvvvvvvvvvvv', 'v'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_dense_case_14(self):
        self.assertEqual(pattern_match('jmmmmmmmmmmmmmm', 'jm'), [0])

    def test_dense_case_15(self):
        self.assertEqual(pattern_match('vlpbgpbgpbgpbgpbgpbgpbgpbgpbgpbgpbgpbgpbgpbgpbgpbgpbgpbgpbgpbgpbgpbg', 'vlpbg'), [0])

    def test_dense_case_16(self):
        self.assertEqual(pattern_match('vrggggggggggggggggggggggg', 'vrg'), [0])

    def test_dense_case_17(self):
        self.assertEqual(pattern_match('fmofzzzzzzzzzzzzzzzzzz', 'fmofz'), [0])

    def test_dense_case_18(self):
        self.assertEqual(pattern_match('ihhhhhhhhhhhhhhhhhhhhhhhhhhhhh', 'ih'), [0])

    def test_dense_case_19(self):
        self.assertEqual(pattern_match('avwdeavwdeavwdeavwdeavwdeavwdeavwdeavwdeavwdeavwdeavwdeavwdeavwdeavwdeavwdeavwdeavwdeavwde', 'avwde'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85])

    def test_dense_case_20(self):
        self.assertEqual(pattern_match('jujujujujujujujujujujujujuju', 'ju'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26])

    def test_dense_case_21(self):
        self.assertEqual(pattern_match('ezzzzzzzzzzzzzzzzzzz', 'ez'), [0])

    def test_dense_case_22(self):
        self.assertEqual(pattern_match('jjjjjjjjjjjjjjjjjjjjjjj', 'j'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])

    def test_dense_case_23(self):
        self.assertEqual(pattern_match('hxxxxxxxx', 'hx'), [0])

    def test_dense_case_24(self):
        self.assertEqual(pattern_match('eissssssssssssssssssssssss', 'eis'), [0])

    def test_dense_case_25(self):
        self.assertEqual(pattern_match('wxxxxxxxxxxxxxxxxxxxxxxxxx', 'wx'), [0])

    def test_dense_case_26(self):
        self.assertEqual(pattern_match('wcrfcccccccccccccccccccccccccc', 'wcrfc'), [0])

    def test_dense_case_27(self):
        self.assertEqual(pattern_match('itccccccccccccccccccc', 'itc'), [0])

    def test_dense_case_28(self):
        self.assertEqual(pattern_match('ypkwnkwnkwnkwnkwnkwnkwnkwnkwnkwnkwnkwnkwnkwnkwnkwnkwnkwnkwnkwnkwnkwn', 'ypkwn'), [0])

    def test_dense_case_29(self):
        self.assertEqual(pattern_match('rrrrrrrrrrrrrrrrrrrrrrrrr', 'r'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])

    def test_dense_case_30(self):
        self.assertEqual(pattern_match('zfnnnnnnnn', 'zfn'), [0])

    def test_dense_case_31(self):
        self.assertEqual(pattern_match('iiiiiiiiiiiiiiiiiiiii', 'i'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

    def test_dense_case_32(self):
        self.assertEqual(pattern_match('lllllllllllllll', 'l'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_dense_case_33(self):
        self.assertEqual(pattern_match('huhuhuhuhuhuhuhuhuhuhuhuhuhuhuhuhuhuhuhu', 'hu'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38])

    def test_dense_case_34(self):
        self.assertEqual(pattern_match('ogggggggg', 'og'), [0])

    def test_dense_case_35(self):
        self.assertEqual(pattern_match('bbbbbbbbbbbbbbbb', 'b'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_dense_case_36(self):
        self.assertEqual(pattern_match('akakakakakakakakakakakakakakakakakakakakakak', 'ak'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42])

    def test_dense_case_37(self):
        self.assertEqual(pattern_match('rajgajgajgajgajgajgajgajgajgajgajgajgajgajgajgajgajgajgajgajgajgajgajgajg', 'rajg'), [0])

    def test_dense_case_38(self):
        self.assertEqual(pattern_match('vsvvvvvvvvvvvvvv', 'vsv'), [0])

    def test_dense_case_39(self):
        self.assertEqual(pattern_match('wdgnnnnnnnnnnnnnnnnnnnnnnnnnnnn', 'wdgn'), [0])

    def test_dense_case_40(self):
        self.assertEqual(pattern_match('jzjzjzjzjzjzjzjzjzjzjzjzjzjzjzjzjzjzjzjzjzjzjzjzjzjzjz', 'jz'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52])

    def test_dense_case_41(self):
        self.assertEqual(pattern_match('wgddddddddddddddddddddddddddddd', 'wgd'), [0])

    def test_dense_case_42(self):
        self.assertEqual(pattern_match('hjhjhjhjhjhjhjhjhjhjhjhjhjhjhjhjhjhjhjhjhj', 'hj'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40])

    def test_dense_case_43(self):
        self.assertEqual(pattern_match('pplllllllllllllll', 'ppl'), [0])

    def test_dense_case_44(self):
        self.assertEqual(pattern_match('imzgemzgemzgemzgemzgemzgemzgemzgemzgemzgemzgemzgemzgemzge', 'imzge'), [0])

    def test_dense_case_45(self):
        self.assertEqual(pattern_match('bluhpbluhpbluhpbluhpbluhpbluhpbluhpbluhpbluhpbluhpbluhpbluhpbluhp', 'bluhp'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])

    def test_dense_case_46(self):
        self.assertEqual(pattern_match('pkcccccccccccccccccccccccccccccccccccccccccc', 'pkcc'), [0])

    def test_dense_case_47(self):
        self.assertEqual(pattern_match('ntttttttttttttttttttt', 'nt'), [0])

    def test_dense_case_48(self):
        self.assertEqual(pattern_match('aflflflflflflflflfl', 'afl'), [0])

    def test_dense_case_49(self):
        self.assertEqual(pattern_match('ueitgtgtgtgtgtgtgtgtgtgtgtgtgtgtgtg', 'ueitg'), [0])

    def test_dense_case_50(self):
        self.assertEqual(pattern_match('lgcqgcqgcqgcqgcqgcqgcqgcqgcqgcqgcqgcqgcqgcqgcqgcqgcqgcqgcqgcqgcqgcqgcq', 'lgcq'), [0])

    def test_dense_case_51(self):
        self.assertEqual(pattern_match('kkuckuckuckuckuckuckuckuckuckuckuckuckuckuckuckuckuc', 'kkuc'), [0])

    def test_dense_case_52(self):
        self.assertEqual(pattern_match('akuppuppuppuppuppuppuppuppuppuppupp', 'akupp'), [0])

    def test_dense_case_53(self):
        self.assertEqual(pattern_match('zzzzzzzzzzzzzzzzzzzzzzzzzzzzz', 'z'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28])

    def test_dense_case_54(self):
        self.assertEqual(pattern_match('dddddddddddddddd', 'd'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_dense_case_55(self):
        self.assertEqual(pattern_match('ioioioioioioioioioioioioioioioioio', 'io'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32])

    def test_dense_case_56(self):
        self.assertEqual(pattern_match('duqlllllllllllllllllllllllll', 'duql'), [0])

    def test_dense_case_57(self):
        self.assertEqual(pattern_match('fxafxafxafxafxafxafxafxafxafxafxafxafxafxafxafxafxafxafxafxafxafxafxa', 'fxa'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66])

    def test_dense_case_58(self):
        self.assertEqual(pattern_match('mmmmmmmmmmmmmmmmmmmmmm', 'm'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])

    def test_dense_case_59(self):
        self.assertEqual(pattern_match('dhdhdhdhdhdhdhdhdhdhdhdhdhdhdh', 'dh'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28])

    def test_dense_case_60(self):
        self.assertEqual(pattern_match('uuuuuuuu', 'u'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_dense_case_61(self):
        self.assertEqual(pattern_match('rsctctctctctctctctctct', 'rsct'), [0])

    def test_dense_case_62(self):
        self.assertEqual(pattern_match('swglllll', 'swgl'), [0])

    def test_dense_case_63(self):
        self.assertEqual(pattern_match('rwbftttttttttttttttttttt', 'rwbft'), [0])

    def test_dense_case_64(self):
        self.assertEqual(pattern_match('bbbbbbbbbbbbbbbb', 'b'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_dense_case_65(self):
        self.assertEqual(pattern_match('aaaaaaaaaa', 'a'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_dense_case_66(self):
        self.assertEqual(pattern_match('qlqqlqqlqqlqqlqqlqqlqqlqqlqqlqqlqqlqqlqqlqqlq', 'qlq'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42])

    def test_dense_case_67(self):
        self.assertEqual(pattern_match('vvnyyyyyyyyyyyyyyyyyyyyyyyy', 'vvnyy'), [0])

    def test_dense_case_68(self):
        self.assertEqual(pattern_match('rmxnxnxnxnxnxnxnxnxnxnxnxnxnxnxnxnxnxnxnxn', 'rmxn'), [0])

    def test_dense_case_69(self):
        self.assertEqual(pattern_match('ppppppppppppppppp', 'p'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    def test_dense_case_70(self):
        self.assertEqual(pattern_match('andqndqndqndqndqndqndqndqndqndqndqndqndqndqndqndqndqndqndqndqndqndqndqndq', 'andq'), [0])

    def test_dense_case_71(self):
        self.assertEqual(pattern_match('qoguoguoguoguoguoguoguoguoguoguoguoguoguoguoguoguoguoguoguoguoguoguoguoguoguoguoguogu', 'qogu'), [0])

    def test_dense_case_72(self):
        self.assertEqual(pattern_match('aaaaaaaaaaaaaaaaaaaaaaaa', 'a'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])

    def test_dense_case_73(self):
        self.assertEqual(pattern_match('utztztztztztztztztztztztz', 'utz'), [0])

    def test_dense_case_74(self):
        self.assertEqual(pattern_match('sssssssssssssssssssss', 's'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

    def test_dense_case_75(self):
        self.assertEqual(pattern_match('hcyacyacyacyacyacyacyacyacyacyacyacyacyacyacyacyacyacyacyacyacyacyacyacyacyacyacyacyacyacya', 'hcya'), [0])

    def test_dense_case_76(self):
        self.assertEqual(pattern_match('sddddddddddddddd', 'sd'), [0])

    def test_dense_case_77(self):
        self.assertEqual(pattern_match('dddddddddddddddddddddddd', 'd'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])

    def test_dense_case_78(self):
        self.assertEqual(pattern_match('pxxxxxxxxxxxxxxxxxxxxxxx', 'px'), [0])

    def test_dense_case_79(self):
        self.assertEqual(pattern_match('rwwwwwwww', 'rw'), [0])

    def test_dense_case_80(self):
        self.assertEqual(pattern_match('czczczczczczczczcz', 'cz'), [0, 2, 4, 6, 8, 10, 12, 14, 16])

    def test_dense_case_81(self):
        self.assertEqual(pattern_match('jasiooooooooo', 'jasio'), [0])

    def test_dense_case_82(self):
        self.assertEqual(pattern_match('ririririririririririririririririririririririririri', 'ri'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48])

    def test_dense_case_83(self):
        self.assertEqual(pattern_match('rfdobrfdobrfdobrfdobrfdobrfdobrfdobrfdobrfdobrfdobrfdobrfdobrfdobrfdobrfdobrfdobrfdobrfdobrfdobrfdobrfdobrfdobrfdobrfdobrfdobrfdob', 'rfdob'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125])

    def test_dense_case_84(self):
        self.assertEqual(pattern_match('ztqshztqshztqshztqshztqsh', 'ztqsh'), [0, 5, 10, 15, 20])

    def test_dense_case_85(self):
        self.assertEqual(pattern_match('trfrfrfrfrfrfrfrfrfrfrfrfrfrfrfrfrfrfrfrfrfrf', 'trf'), [0])

    def test_dense_case_86(self):
        self.assertEqual(pattern_match('btscbtscbtscbtscbtscbtscbtscbtscbtsc', 'btsc'), [0, 4, 8, 12, 16, 20, 24, 28, 32])

    def test_dense_case_87(self):
        self.assertEqual(pattern_match('zzzzzzzzzzzzzzzzzz', 'z'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])

    def test_dense_case_88(self):
        self.assertEqual(pattern_match('gaqbpaqbpaqbpaqbpaqbpaqbp', 'gaqbp'), [0])

    def test_dense_case_89(self):
        self.assertEqual(pattern_match('oeszvzvzvzvzvzvzvzvzvzvzvzvzvzvzvzvzvzvzvzvzv', 'oeszv'), [0])

    def test_dense_case_90(self):
        self.assertEqual(pattern_match('jvvvvvvvvvvvvv', 'jv'), [0])

    def test_dense_case_91(self):
        self.assertEqual(pattern_match('wwwwwwwwwwwwwwwwwwwwwwwwwww', 'w'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26])

    def test_dense_case_92(self):
        self.assertEqual(pattern_match('deeeeeeeeeeeeeeeeeeeeeeeeeeeeee', 'de'), [0])

    def test_dense_case_93(self):
        self.assertEqual(pattern_match('fdfdfdfdfdfdfdfdfdfdfdfd', 'fd'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22])

    def test_dense_case_94(self):
        self.assertEqual(pattern_match('remjbbbbbbbbbbbbbbb', 'remjb'), [0])

    def test_dense_case_95(self):
        self.assertEqual(pattern_match('wpspgpspgpspgpspgpspgpspgpspgpspg', 'wpspg'), [0])

    def test_dense_case_96(self):
        self.assertEqual(pattern_match('mabcbcbcbcbcbcbcbcbcbcbc', 'mabc'), [0])

    def test_dense_case_97(self):
        self.assertEqual(pattern_match('ofixoofixoofixoofixoofixoofixoofixoofixoofixoofixoofixoofixoofixoofixoofixoofixoofixoofixoofixoofixoofixoofixoofixoofixoofixoofixoofixoofixoofixoofixo', 'ofixo'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145])

    def test_dense_case_98(self):
        self.assertEqual(pattern_match('rbbbbbb', 'rb'), [0])

    def test_dense_case_99(self):
        self.assertEqual(pattern_match('hbicjicjicjicjicjicjicjicjicjicjicjicj', 'hbicj'), [0])

    def test_dense_case_100(self):
        self.assertEqual(pattern_match('biiiiiiiiiiiiiii', 'bi'), [0])

    def test_dense_case_101(self):
        self.assertEqual(pattern_match('rnsnsnsnsnsnsnsnsnsnsns', 'rns'), [0])

    def test_dense_case_102(self):
        self.assertEqual(pattern_match('cbgbgbgbgbgbgbgbgbgbgbgbgbgbgbgbgbgbgbgbgbgbgbgbgbgbgbgbg', 'cbg'), [0])

    def test_dense_case_103(self):
        self.assertEqual(pattern_match('xdddddddddddddd', 'xd'), [0])

    def test_dense_case_104(self):
        self.assertEqual(pattern_match('lejejejejejejej', 'lej'), [0])

    def test_dense_case_105(self):
        self.assertEqual(pattern_match('jueqoooooooooooooooooo', 'jueqo'), [0])

    def test_dense_case_106(self):
        self.assertEqual(pattern_match('zzzzzzzzzzzzzzz', 'z'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_dense_case_107(self):
        self.assertEqual(pattern_match('cdaabdaabdaabdaabdaabdaabdaabdaabdaabdaabdaabdaabdaabdaabdaabdaabdaabdaabdaabdaabdaabdaabdaabdaabdaab', 'cdaab'), [0])

    def test_dense_case_108(self):
        self.assertEqual(pattern_match('enslllllllllllllll', 'ensl'), [0])

    def test_dense_case_109(self):
        self.assertEqual(pattern_match('aeaeaeaeaeaeaeaeae', 'ae'), [0, 2, 4, 6, 8, 10, 12, 14, 16])

    def test_dense_case_110(self):
        self.assertEqual(pattern_match('amamamamamamamamamamamamamamamamam', 'am'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32])

    def test_dense_case_111(self):
        self.assertEqual(pattern_match('errrrrrrrrrrrrrrrrrrrrrrrrrrr', 'er'), [0])

    def test_dense_case_112(self):
        self.assertEqual(pattern_match('icbiiiiiiiii', 'icbi'), [0])

    def test_dense_case_113(self):
        self.assertEqual(pattern_match('rsurgrgrgrgrgrgrgrgrgrgrgrgrgrgrgrgrgrgrgrgrgrgrgrgrgrgrgrgrg', 'rsurg'), [0])

    def test_dense_case_114(self):
        self.assertEqual(pattern_match('uibibibibibibibibibibibibibibibibib', 'uib'), [0])

    def test_dense_case_115(self):
        self.assertEqual(pattern_match('tehcvhcvhcvhcvhcvhcvhcvhcvhcvhcvhcvhcv', 'tehcv'), [0])

    def test_dense_case_116(self):
        self.assertEqual(pattern_match('iiiiiiiiiiiiii', 'i'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_dense_case_117(self):
        self.assertEqual(pattern_match('dspddddddddddddddd', 'dspd'), [0])

    def test_dense_case_118(self):
        self.assertEqual(pattern_match('aaaaaaaaaaa', 'a'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_dense_case_119(self):
        self.assertEqual(pattern_match('sajfisajfisajfisajfisajfisajfisajfisajfisajfisajfisajfisajfisajfisajfisajfisajfisajfisajfisajfisajfisajfisajfisajfisajfisajfisajfi', 'sajfi'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125])

    def test_dense_case_120(self):
        self.assertEqual(pattern_match('hhhhhhhhh', 'h'), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_dense_case_121(self):
        self.assertEqual(pattern_match('tgnrvrvrvrvrvrvrvrvrvrvrvrvrvrvrvrvrvrvrvrvrvrvrvrv', 'tgnrv'), [0])

    def test_dense_case_122(self):
        self.assertEqual(pattern_match('twrrrrrrrrrrrrrrrrrrr', 'twr'), [0])

    def test_dense_case_123(self):
        self.assertEqual(pattern_match('umqdnnnnnnnnnnnnnnnnnn', 'umqdn'), [0])

    def test_dense_case_124(self):
        self.assertEqual(pattern_match('slyyyyyyyyyyyyyyyyy', 'sly'), [0])

    def test_dense_case_125(self):
        self.assertEqual(pattern_match('zgzgzgzgzgzgzgzgzgz', 'zgz'), [0, 2, 4, 6, 8, 10, 12, 14, 16])

    def test_dense_case_126(self):
        self.assertEqual(pattern_match('cxsvxsvxsvxsvxsvxsvxsvxsvxsvxsvxsvxsvxsvxsvxsvxsv', 'cxsv'), [0])

    def test_dense_case_127(self):
        self.assertEqual(pattern_match('bmdfvfvfvfvfvfvfv', 'bmdfv'), [0])

    def test_dense_case_128(self):
        self.assertEqual(pattern_match('ixixixixixixixixixixixixixixixixixixixixixixixixixixixix', 'ix'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54])

    def test_dense_case_129(self):
        self.assertEqual(pattern_match('uuuuuuuuuuuuuuuuuuuuuuuuuuuu', 'u'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27])

    def test_dense_case_130(self):
        self.assertEqual(pattern_match('okkkkkkk', 'ok'), [0])

    def test_dense_case_131(self):
        self.assertEqual(pattern_match('nnnnnnnnnnnnnnnnnnnnn', 'n'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

    def test_dense_case_132(self):
        self.assertEqual(pattern_match('djtdjtdjtdjtdjtdjtdjtdjtdjtdjtdjtdjtdjt', 'djt'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36])

    def test_dense_case_133(self):
        self.assertEqual(pattern_match('jjjjjjjjj', 'j'), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_dense_case_134(self):
        self.assertEqual(pattern_match('zhhhhhhhhh', 'zh'), [0])

    def test_dense_case_135(self):
        self.assertEqual(pattern_match('kkkkkkkkkkkkkkkkkkk', 'k'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    def test_dense_case_136(self):
        self.assertEqual(pattern_match('gmjomjomjomjomjomjomjomjomjomjomjomjomjomjomjomjomjomjo', 'gmjo'), [0])

    def test_dense_case_137(self):
        self.assertEqual(pattern_match('yxueuuuuuuuuuuuuuuuuuuuu', 'yxueu'), [0])

    def test_dense_case_138(self):
        self.assertEqual(pattern_match('wcowcowcowcowcowcowcowcowcowcowcowcowcowcowcowco', 'wco'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45])

    def test_dense_case_139(self):
        self.assertEqual(pattern_match('gxmyxmyxmyxmyxmyxmyxmyxmyxmyxmyxmyxmyxmyxmyxmyxmyxmyxmyxmyxmyxmyxmyxmyxmyxmy', 'gxmy'), [0])

    def test_dense_case_140(self):
        self.assertEqual(pattern_match('xrvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv', 'xrvv'), [0])

    def test_dense_case_141(self):
        self.assertEqual(pattern_match('pvpvpvpvpvpvpvpvpvpvpvpvpvpvpvpvpvpvpvpvpvpvpvpvpvpvpvpvpvpv', 'pv'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58])

    def test_dense_case_142(self):
        self.assertEqual(pattern_match('zdglelelelelele', 'zdgle'), [0])

    def test_dense_case_143(self):
        self.assertEqual(pattern_match('ccccccc', 'c'), [0, 1, 2, 3, 4, 5, 6])

    def test_dense_case_144(self):
        self.assertEqual(pattern_match('zzzzzzzzzzzzzzzzzzzz', 'z'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_dense_case_145(self):
        self.assertEqual(pattern_match('ggggggggggggg', 'g'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_dense_case_146(self):
        self.assertEqual(pattern_match('hyonyonyonyonyon', 'hyon'), [0])

    def test_dense_case_147(self):
        self.assertEqual(pattern_match('juccccccccccc', 'juc'), [0])

    def test_dense_case_148(self):
        self.assertEqual(pattern_match('jdjjdjjdjjdjjdjjdjjdjjdjjdjjdjjdjjdjjdjjdjjdj', 'jdj'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42])

    def test_dense_case_149(self):
        self.assertEqual(pattern_match('eeeeeeeeeeeeeeeeeeeeeeeeeee', 'e'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26])

    def test_dense_case_150(self):
        self.assertEqual(pattern_match('wqzsqzsqzsqzsqzsqzsqzsqzsqzsqzsqzsqzsqzsqzsqzsqzsqzsqzsqzsqzsqzs', 'wqzs'), [0])

    def test_dense_case_151(self):
        self.assertEqual(pattern_match('vvvvvvvvvvvv', 'v'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_dense_case_152(self):
        self.assertEqual(pattern_match('bexuuuuuuuuuuuuuuuuu', 'bexu'), [0])

    def test_dense_case_153(self):
        self.assertEqual(pattern_match('vmlvmlvmlvmlvmlvmlvmlvml', 'vml'), [0, 3, 6, 9, 12, 15, 18, 21])

    def test_dense_case_154(self):
        self.assertEqual(pattern_match('sffffffffffffffff', 'sf'), [0])

    def test_dense_case_155(self):
        self.assertEqual(pattern_match('upupupupupupupupupupupupupupupupupupupupupup', 'up'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42])

    def test_dense_case_156(self):
        self.assertEqual(pattern_match('geknnnnnnnnnnnnnnnnnnnnnn', 'gekn'), [0])

    def test_dense_case_157(self):
        self.assertEqual(pattern_match('mooooooooooooooooo', 'mo'), [0])

    def test_dense_case_158(self):
        self.assertEqual(pattern_match('wwwwwwwwww', 'w'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_dense_case_159(self):
        self.assertEqual(pattern_match('uwqllllllllllllllllllllll', 'uwql'), [0])

    def test_dense_case_160(self):
        self.assertEqual(pattern_match('joezjoezjoezjoezjoezjoezjoez', 'joez'), [0, 4, 8, 12, 16, 20, 24])

    def test_dense_case_161(self):
        self.assertEqual(pattern_match('mwkxmwkxmwkxmwkxmwkxmwkxmwkxmwkxmwkxmwkxmwkxmwkxmwkxmwkxmwkxmwkxmwkxmwkxmwkxmwkxmwkxmwkxmwkxmwkxmwkxmwkxmwkxmwkxmwkx', 'mwkx'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100, 104, 108, 112])

    def test_dense_case_162(self):
        self.assertEqual(pattern_match('pppppppppppppppppppppppp', 'p'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])

    def test_dense_case_163(self):
        self.assertEqual(pattern_match('zviiiiiiiiiiiiiiiiiiiiiiiiiiii', 'zvi'), [0])

    def test_dense_case_164(self):
        self.assertEqual(pattern_match('qabjabjabjabjabjabj', 'qabj'), [0])

    def test_dense_case_165(self):
        self.assertEqual(pattern_match('jvaddddddddddddddd', 'jvad'), [0])

    def test_dense_case_166(self):
        self.assertEqual(pattern_match('pnbhhnbhhnbhhnbhhnbhhnbhhnbhhnbhhnbhh', 'pnbhh'), [0])

    def test_dense_case_167(self):
        self.assertEqual(pattern_match('uuuuuuuuuuuuuuuuuuuu', 'u'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_dense_case_168(self):
        self.assertEqual(pattern_match('mfmgggggggg', 'mfmg'), [0])

    def test_dense_case_169(self):
        self.assertEqual(pattern_match('mbkmbkmbkmbkmbkmbkmbkmbkmbkmbkmbkmbkmbkmbkmbkmbk', 'mbk'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45])

    def test_dense_case_170(self):
        self.assertEqual(pattern_match('linqaqaqaqaqaqaqaqaqaqa', 'linqa'), [0])

    def test_dense_case_171(self):
        self.assertEqual(pattern_match('nowddddddddddddddddddddddd', 'nowd'), [0])

    def test_dense_case_172(self):
        self.assertEqual(pattern_match('fffffffffffff', 'f'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_dense_case_173(self):
        self.assertEqual(pattern_match('jgwmmmmmmmmmmmmmmmmmmm', 'jgwm'), [0])

    def test_dense_case_174(self):
        self.assertEqual(pattern_match('uzzzzzzzzzzzzzzzzzzzzzzzzzzz', 'uz'), [0])

    def test_dense_case_175(self):
        self.assertEqual(pattern_match('lllllllllllllll', 'l'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_dense_case_176(self):
        self.assertEqual(pattern_match('zwqnwqnwqnwqnwqnwqnwqnwqnwqnwqnwqn', 'zwqn'), [0])

    def test_dense_case_177(self):
        self.assertEqual(pattern_match('rcnrcnrcnrcnrcnrcnrcnrcnrcnrcnrcnrcnrcnrcnrcn', 'rcn'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42])

    def test_dense_case_178(self):
        self.assertEqual(pattern_match('wrrwrrwrrwrrwrrwrrwrrwrrwrrwrrwrrwrrwrrwrrwrrwrrwrrwrrwrrwrrwrrwrrwrrwrrwrrwrrwrr', 'wrr'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78])

    def test_dense_case_179(self):
        self.assertEqual(pattern_match('mmmmmmmmmmmmmmmm', 'mm'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_dense_case_180(self):
        self.assertEqual(pattern_match('rwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrw', 'rw'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32])

    def test_dense_case_181(self):
        self.assertEqual(pattern_match('udfbvudfbvudfbvudfbvudfbvudfbvudfbvudfbvudfbvudfbvudfbvudfbvudfbvudfbvudfbvudfbvudfbvudfbvudfbvudfbvudfbvudfbv', 'udfbv'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105])

    def test_dense_case_182(self):
        self.assertEqual(pattern_match('thjjnnnnnnnnnnnnnnnnnnnnnnn', 'thjjn'), [0])

    def test_dense_case_183(self):
        self.assertEqual(pattern_match('vbfwqbfwqbfwqbfwqbfwqbfwqbfwqbfwqbfwqbfwqbfwqbfwqbfwqbfwqbfwqbfwqbfwqbfwqbfwqbfwqbfwqbfwqbfwqbfwqbfwqbfwqbfwqbfwq', 'vbfwq'), [0])

    def test_dense_case_184(self):
        self.assertEqual(pattern_match('sgoagoagoagoagoagoagoagoagoagoagoagoagoagoagoa', 'sgoa'), [0])

    def test_dense_case_185(self):
        self.assertEqual(pattern_match('ccccccccccccccccc', 'c'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    def test_dense_case_186(self):
        self.assertEqual(pattern_match('nmkimkimkimkimkimkimkimkimkimkimkimkimkimkimkimkimkimkimkimki', 'nmki'), [0])

    def test_dense_case_187(self):
        self.assertEqual(pattern_match('plflflflflflflflflflflf', 'plf'), [0])

    def test_dense_case_188(self):
        self.assertEqual(pattern_match('kwyakwyakwyakwyakwyakwyakwyakwyakwyakwyakwyakwyakwyakwyakwyakwyakwyakwyakwyakwyakwyakwyakwyakwya', 'kwya'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92])

    def test_dense_case_189(self):
        self.assertEqual(pattern_match('cfgtygtygtygtygtygtygtygty', 'cfgty'), [0])

    def test_dense_case_190(self):
        self.assertEqual(pattern_match('evkesevkesevkesevkesevkesevkesevkesevkesevkesevkesevkesevkesevkesevkes', 'evkes'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65])

    def test_dense_case_191(self):
        self.assertEqual(pattern_match('ceeeeeeeeeeeeeeee', 'ce'), [0])

    def test_dense_case_192(self):
        self.assertEqual(pattern_match('qqqqqqqqqqqqqqqqqqqqqqqqqqq', 'q'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26])

    def test_dense_case_193(self):
        self.assertEqual(pattern_match('ajajajajajajajajajaj', 'aj'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])

    def test_dense_case_194(self):
        self.assertEqual(pattern_match('aaaaaaaaaaaaaaaaaaaaaaa', 'a'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])

    def test_dense_case_195(self):
        self.assertEqual(pattern_match('iffxffxffxffxffxffxffxffxffxffxffxffxffxffxffxffxffxffxffxffxffxffxffxffx', 'iffx'), [0])

    def test_dense_case_196(self):
        self.assertEqual(pattern_match('lvvlvvlvvlvvlvvlvvlv', 'lvvlv'), [0, 3, 6, 9, 12, 15])

    def test_dense_case_197(self):
        self.assertEqual(pattern_match('vbvoooooooooooo', 'vbvo'), [0])

    def test_dense_case_198(self):
        self.assertEqual(pattern_match('jjjjjjjjjjjjjjj', 'j'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_dense_case_199(self):
        self.assertEqual(pattern_match('dddddddddddd', 'd'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_dense_case_200(self):
        self.assertEqual(pattern_match('eeeeeeee', 'e'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_dense_case_201(self):
        self.assertEqual(pattern_match('sxuuuuuuuuuuuuu', 'sxu'), [0])

    def test_dense_case_202(self):
        self.assertEqual(pattern_match('rpvpfpfpfpfpfpfpfpfpfpfpfpfpfpfpfpfpfpfpfpfpf', 'rpvpf'), [0])

    def test_dense_case_203(self):
        self.assertEqual(pattern_match('bvvgbvvgbvvgbvvgbvvgbvvgbvvgbvvgbvvgbvvgbvvgbvvgbvvgbvvgbvvgbvvgbvvgbvvgbvvgbvvgbvvgbvvg', 'bvvg'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84])

    def test_dense_case_204(self):
        self.assertEqual(pattern_match('cnoiiiiiiiiiiiiii', 'cnoi'), [0])

    def test_dense_case_205(self):
        self.assertEqual(pattern_match('kirbwkirbwkirbwkirbwkirbwkirbwkirbwkirbwkirbwkirbwkirbw', 'kirbw'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50])

    def test_dense_case_206(self):
        self.assertEqual(pattern_match('llllllll', 'l'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_dense_case_207(self):
        self.assertEqual(pattern_match('aliuvvvvvvvvvvvvvvvvvvvvvv', 'aliuv'), [0])

    def test_dense_case_208(self):
        self.assertEqual(pattern_match('rzpppppppp', 'rzp'), [0])

    def test_dense_case_209(self):
        self.assertEqual(pattern_match('nlurnlurnlurnlurnlurnlurnlurnlurnlurnlurnlurnlurnlurnlurnlurnlurnlurnlurnlurnlurnlur', 'nlur'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80])

    def test_dense_case_210(self):
        self.assertEqual(pattern_match('ihylylylylylylylylylylylylylylyl', 'ihyl'), [0])

    def test_dense_case_211(self):
        self.assertEqual(pattern_match('ctepeepeepeepeepeepeepeepeepeepeepeepeepeepeepeepeepeepeepeepeepe', 'ctepe'), [0])

    def test_dense_case_212(self):
        self.assertEqual(pattern_match('tuhuhuhuhuhuhuhuhuhuhuhuhuhuhuhuhuhuhuhuhuhuhuhuh', 'tuh'), [0])

    def test_dense_case_213(self):
        self.assertEqual(pattern_match('zhzhzhzhzhzhzh', 'zh'), [0, 2, 4, 6, 8, 10, 12])

    def test_dense_case_214(self):
        self.assertEqual(pattern_match('ykkkkkkkk', 'yk'), [0])

    def test_dense_case_215(self):
        self.assertEqual(pattern_match('gggggggggggggggggggggggggggggg', 'gg'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28])

    def test_dense_case_216(self):
        self.assertEqual(pattern_match('rttqoqoqoqoqoqoqoqoqoqoqoqoqoqoqoqoqoqoqoqoqoqo', 'rttqo'), [0])

    def test_dense_case_217(self):
        self.assertEqual(pattern_match('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyy', 'y'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29])

    def test_dense_case_218(self):
        self.assertEqual(pattern_match('yeiyiyiyiyiyiyiyiy', 'yeiy'), [0])

    def test_dense_case_219(self):
        self.assertEqual(pattern_match('anmscnmscnmscnmscnmscnmscnmscnmscnmscnmscnmscnmscnmscnmscnmscnmscnmscnmscnmscnmsc', 'anmsc'), [0])

    def test_dense_case_220(self):
        self.assertEqual(pattern_match('cjjjjjjjj', 'cj'), [0])

    def test_dense_case_221(self):
        self.assertEqual(pattern_match('hhhhhhhhhhhhhhhhhhhhhhhhhhhh', 'h'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27])

    def test_dense_case_222(self):
        self.assertEqual(pattern_match('yflhxhxhxhxhxhxhxhxhxhxhxhxhxhxhxhxhxhxhxhxhxhxhxhxhxhxhxhxhx', 'yflhx'), [0])

    def test_dense_case_223(self):
        self.assertEqual(pattern_match('lnbyxnbyxnbyxnbyxnbyxnbyxnbyxnbyxnbyxnbyxnbyxnbyxnbyxnbyxnbyxnbyxnbyx', 'lnbyx'), [0])

    def test_dense_case_224(self):
        self.assertEqual(pattern_match('tttttttttttttttttttttt', 't'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])

    def test_dense_case_225(self):
        self.assertEqual(pattern_match('acukjukjukjukjukjukjukjukjukjukjukjukjukjukjukjukjukjukjukjukjukjukjukjukjukjukjukjukjukj', 'acukj'), [0])

    def test_dense_case_226(self):
        self.assertEqual(pattern_match('yroiroiroiroiroiroiroiroiroiroiroiroiroiroiroiroiroiroiroiroiroiroiroiroiroiroiroiroiroiroi', 'yroi'), [0])

    def test_dense_case_227(self):
        self.assertEqual(pattern_match('ttttttttttttttttttttttttttttt', 't'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28])

    def test_dense_case_228(self):
        self.assertEqual(pattern_match('dvgrfgrfgrfgrfgrfgrfgrfgrfgrfgrfgrfgrfgrfgrfgrfgrfgrfgrf', 'dvgrf'), [0])

    def test_dense_case_229(self):
        self.assertEqual(pattern_match('leljzjzjzjzjzjzjzjzjzjzjzjz', 'leljz'), [0])

    def test_dense_case_230(self):
        self.assertEqual(pattern_match('dggggggggggggggggggg', 'dg'), [0])

    def test_dense_case_231(self):
        self.assertEqual(pattern_match('pnpnpnpnpnpnpnpnpnpnpnpnpnpnpnpn', 'pn'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])

    def test_dense_case_232(self):
        self.assertEqual(pattern_match('papapapapapapapapapapapapapapapapapapapapapapapa', 'pa'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46])

    def test_dense_case_233(self):
        self.assertEqual(pattern_match('tysysysysysysysysysysysysysysysysysysysysysysysys', 'tys'), [0])

    def test_dense_case_234(self):
        self.assertEqual(pattern_match('vkkkkkkkkkkkkkkkkkkkk', 'vk'), [0])

    def test_dense_case_235(self):
        self.assertEqual(pattern_match('mbjbjbjbjbjbjbj', 'mbj'), [0])

    def test_dense_case_236(self):
        self.assertEqual(pattern_match('sssssssssssssssssss', 's'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    def test_dense_case_237(self):
        self.assertEqual(pattern_match('kshkkkkkkkkkkkkkkk', 'kshk'), [0])

    def test_dense_case_238(self):
        self.assertEqual(pattern_match('tdxdrxdrxdrxdrxdrxdrxdrxdrxdrxdrxdrxdrxdrxdrxdrxdrxdrxdrxdrxdrxdrxdrxdrxdrxdrxdrxdrxdrxdrxdr', 'tdxdr'), [0])

    def test_dense_case_239(self):
        self.assertEqual(pattern_match('aaaaaa', 'a'), [0, 1, 2, 3, 4, 5])

    def test_dense_case_240(self):
        self.assertEqual(pattern_match('lbtlbtlbtlbtlbtlbtlbtlbt', 'lbt'), [0, 3, 6, 9, 12, 15, 18, 21])

    def test_dense_case_241(self):
        self.assertEqual(pattern_match('uiiiiiiiiiiiiiiiiiiii', 'ui'), [0])

    def test_dense_case_242(self):
        self.assertEqual(pattern_match('sypkkkkkkk', 'sypk'), [0])

    def test_dense_case_243(self):
        self.assertEqual(pattern_match('vgezzzzzzzzzzzzzzz', 'vgez'), [0])

    def test_dense_case_244(self):
        self.assertEqual(pattern_match('dqbidqbidqbidqbidqbidqbidqbidqbidqbidqbidqbidqbidqbidqbidqbidqbidqbidqbidqbidqbidqbidqbidqbi', 'dqbi'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88])

    def test_dense_case_245(self):
        self.assertEqual(pattern_match('vkixvkixvkixvkixvkixvkixvkixvkixvkixvkixvkixvkixvkixvkixvkixvkixvkixvkixvkixvkixvkixvkix', 'vkix'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84])

    def test_dense_case_246(self):
        self.assertEqual(pattern_match('djouwjouwjouwjouwjouwjouwjouwjouwjouwjouwjouwjouwjouwjouw', 'djouw'), [0])

    def test_dense_case_247(self):
        self.assertEqual(pattern_match('uuuuuuuuuuuuuuuuuuuuu', 'u'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

    def test_dense_case_248(self):
        self.assertEqual(pattern_match('rprprprprprprprprprprprprprprprprprprprprprprprp', 'rp'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46])

    def test_dense_case_249(self):
        self.assertEqual(pattern_match('yjinononononononononononono', 'yjino'), [0])

    def test_dense_case_250(self):
        self.assertEqual(pattern_match('jxdxdxdxdxdxd', 'jxd'), [0])

    def test_dense_case_251(self):
        self.assertEqual(pattern_match('hhpshhpshhpshhpshhpshhpshhpshhpshhpshhpshhpshhpshhpshhpshhpshhpshhpshhpshhpshhpshhpshhps', 'hhps'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84])

    def test_dense_case_252(self):
        self.assertEqual(pattern_match('hihhihhihhihhih', 'hih'), [0, 3, 6, 9, 12])

    def test_dense_case_253(self):
        self.assertEqual(pattern_match('eigaeigaeigaeigaeigaeigaeigaeigaeigaeigaeigaeigaeigaeigaeigaeigaeigaeigaeigaeigaeigaeigaeigaeigaeigaeigaeigaeigaeiga', 'eiga'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100, 104, 108, 112])

    def test_dense_case_254(self):
        self.assertEqual(pattern_match('hqqhqqhqqhqqhqqhqqhqqhqqhqqhqqhqqhqqhqqhqqhqqhqqhqqhqqhqqhqqhqq', 'hqq'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60])

    def test_dense_case_255(self):
        self.assertEqual(pattern_match('urrrrrrrrrrr', 'ur'), [0])

    def test_dense_case_256(self):
        self.assertEqual(pattern_match('rjvtrrjvtrrjvtrrjvtrrjvtrrjvtrrjvtrrjvtrrjvtrrjvtrrjvtrrjvtrrjvtrrjvtr', 'rjvtr'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65])

    def test_dense_case_257(self):
        self.assertEqual(pattern_match('gjjjjjjjjjjjjjjjjjj', 'gj'), [0])

    def test_dense_case_258(self):
        self.assertEqual(pattern_match('sssssssssssssssssssss', 's'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

    def test_dense_case_259(self):
        self.assertEqual(pattern_match('ggggggggggggggggggggggg', 'g'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])

    def test_dense_case_260(self):
        self.assertEqual(pattern_match('fffff', 'f'), [0, 1, 2, 3, 4])

    def test_dense_case_261(self):
        self.assertEqual(pattern_match('ixoaxoaxoaxoaxoaxoaxoaxoaxoaxoaxoaxoaxoaxoaxoaxoaxoaxoa', 'ixoa'), [0])

    def test_dense_case_262(self):
        self.assertEqual(pattern_match('jkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjkjk', 'jk'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44])

    def test_dense_case_263(self):
        self.assertEqual(pattern_match('kjrckjrckjrckjrckjrckjrckjrckjrckjrckjrckjrckjrckjrckjrckjrckjrc', 'kjrc'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60])

    def test_dense_case_264(self):
        self.assertEqual(pattern_match('yveeeeeeeeeeeeeeee', 'yvee'), [0])

    def test_dense_case_265(self):
        self.assertEqual(pattern_match('lmdwowowowowowo', 'lmdwo'), [0])

    def test_dense_case_266(self):
        self.assertEqual(pattern_match('bfkfkfkfkfkfkfkfkfkfkfkfkfkfkfk', 'bfk'), [0])

    def test_dense_case_267(self):
        self.assertEqual(pattern_match('tttttttttttttttt', 't'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_dense_case_268(self):
        self.assertEqual(pattern_match('ujxtttttttttttttttttttt', 'ujxt'), [0])

    def test_dense_case_269(self):
        self.assertEqual(pattern_match('iffffffffffff', 'if'), [0])

    def test_dense_case_270(self):
        self.assertEqual(pattern_match('rucccccccccccccccc', 'ruc'), [0])

    def test_dense_case_271(self):
        self.assertEqual(pattern_match('bbbbbbbbbbbbbbbbbbbbbbbbbb', 'b'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])

    def test_dense_case_272(self):
        self.assertEqual(pattern_match('hwnhwnhwnhwnhwnhwnhwnhwnhwnhwnhwnhwnhwnhwnhwnhwnhwnhwnhwnhwnhwnhwnhwnhwnhwnhwnhwnhwn', 'hwn'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81])

    def test_dense_case_273(self):
        self.assertEqual(pattern_match('fvfvfvfvfvfvfvfvfvfvfvfvfvfvfvfvfvfvfvfvfvfvfvfvfvfvfvfvfvfv', 'fv'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58])

    def test_dense_case_274(self):
        self.assertEqual(pattern_match('tpfbdfbdfbdfbdfbdfbdfbdfbdfbdfbdfbdfbdfbdfbdfbdfbd', 'tpfbd'), [0])

    def test_dense_case_275(self):
        self.assertEqual(pattern_match('llllllllllllllllllllllllll', 'l'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])

    def test_dense_case_276(self):
        self.assertEqual(pattern_match('qrsjpqrsjpqrsjpqrsjpqrsjpqrsjpqrsjpqrsjpqrsjpqrsjpqrsjpqrsjpqrsjpqrsjpqrsjpqrsjpqrsjpqrsjpqrsjpqrsjpqrsjpqrsjpqrsjpqrsjpqrsjpqrsjpqrsjpqrsjp', 'qrsjp'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135])

    def test_dense_case_277(self):
        self.assertEqual(pattern_match('zlyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy', 'zlyy'), [0])

    def test_dense_case_278(self):
        self.assertEqual(pattern_match('ftvvvvvvvvvvvvvvvvvvvvvvvvvvv', 'ftv'), [0])

    def test_dense_case_279(self):
        self.assertEqual(pattern_match('gejqjqjqjqjqjqjqjqjqjqjqjqjqjqjqjqjqjqjq', 'gejq'), [0])

    def test_dense_case_280(self):
        self.assertEqual(pattern_match('moiumoiumoiumoiumoiumoiumoiumoiumoiumoiumoiumoiu', 'moiu'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44])

    def test_dense_case_281(self):
        self.assertEqual(pattern_match('viiiiiiiiiiiiiiiiiiii', 'vi'), [0])

    def test_dense_case_282(self):
        self.assertEqual(pattern_match('pspspspspspspspspspspspsps', 'ps'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])

    def test_dense_case_283(self):
        self.assertEqual(pattern_match('gvvvvvvvvvvvvvvvvvvvvvvv', 'gv'), [0])

    def test_dense_case_284(self):
        self.assertEqual(pattern_match('loettttttttttt', 'loet'), [0])

    def test_dense_case_285(self):
        self.assertEqual(pattern_match('uququququququququququququququququququququququququququ', 'uqu'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50])

    def test_dense_case_286(self):
        self.assertEqual(pattern_match('uuuuuuuuuuuuuuuuuuuuuu', 'u'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])

    def test_dense_case_287(self):
        self.assertEqual(pattern_match('znnnnn', 'zn'), [0])

    def test_dense_case_288(self):
        self.assertEqual(pattern_match('bdvrlvrlvrlvrlvrlvrlvrlvrlvrlvrlvrlvrlvrlvrlvrlvrlvrlvrlvrlvrlvrl', 'bdvrl'), [0])

    def test_dense_case_289(self):
        self.assertEqual(pattern_match('urmrmrmrmrmrmrmrmrmrmrmrmrmrm', 'urm'), [0])

    def test_dense_case_290(self):
        self.assertEqual(pattern_match('yejjjjj', 'yej'), [0])

    def test_dense_case_291(self):
        self.assertEqual(pattern_match('axpxpxpxpxpxpxpxpxpxpxpxpxpxp', 'axp'), [0])

    def test_dense_case_292(self):
        self.assertEqual(pattern_match('emszzzzzzzzzzzzzzzzzzzzzzzzzz', 'emsz'), [0])

    def test_dense_case_293(self):
        self.assertEqual(pattern_match('rrteaeaeaeaeaeaeaeaeaeaeaeaeaea', 'rrtea'), [0])

    def test_dense_case_294(self):
        self.assertEqual(pattern_match('ewewewewewewewewewewewewewewewewewewewewewew', 'ew'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42])

    def test_dense_case_295(self):
        self.assertEqual(pattern_match('gqqqqqqqqqqqqqqqqqqqqqqqqqqqqq', 'gq'), [0])

    def test_dense_case_296(self):
        self.assertEqual(pattern_match('ncyyyyyyyyyyyyyyyyyyyyyyyyyyyy', 'ncy'), [0])

    def test_dense_case_297(self):
        self.assertEqual(pattern_match('wdffffff', 'wdf'), [0])

    def test_dense_case_298(self):
        self.assertEqual(pattern_match('dudududududududududududududududududududududududududu', 'du'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50])

    def test_dense_case_299(self):
        self.assertEqual(pattern_match('jskzzzzzzzzzzzzzzzzzzzzzzzzzzzzz', 'jskz'), [0])

    def test_dense_case_300(self):
        self.assertEqual(pattern_match('lllllllllllll', 'l'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_dense_case_301(self):
        self.assertEqual(pattern_match('rydcppppppppppppppppp', 'rydcp'), [0])

    def test_dense_case_302(self):
        self.assertEqual(pattern_match('hsbahsbahsbahsbahsbahsbahsbahsbahsbahsbahsba', 'hsba'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40])

    def test_dense_case_303(self):
        self.assertEqual(pattern_match('vcevcevcevcevcevcevcevce', 'vce'), [0, 3, 6, 9, 12, 15, 18, 21])

    def test_dense_case_304(self):
        self.assertEqual(pattern_match('pzzzzzzzzzzzzzzzzzzz', 'pz'), [0])

    def test_dense_case_305(self):
        self.assertEqual(pattern_match('rumnrumnrumnrumnrumnrumnrumnrumnrumn', 'rumn'), [0, 4, 8, 12, 16, 20, 24, 28, 32])

    def test_dense_case_306(self):
        self.assertEqual(pattern_match('sssssssssssssss', 's'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_dense_case_307(self):
        self.assertEqual(pattern_match('dcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdc', 'dc'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36])

    def test_dense_case_308(self):
        self.assertEqual(pattern_match('vhhhhhh', 'vh'), [0])

    def test_dense_case_309(self):
        self.assertEqual(pattern_match('wwwww', 'w'), [0, 1, 2, 3, 4])

    def test_dense_case_310(self):
        self.assertEqual(pattern_match('tttttttt', 't'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_dense_case_311(self):
        self.assertEqual(pattern_match('uwuwuwuwuwuwuwuwuwuwuwuwuwuwuwuwuw', 'uw'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32])

    def test_dense_case_312(self):
        self.assertEqual(pattern_match('ypprtprtprtprtprtprtprtprtprtprtprtprtprtprtprtprtprtprtprtprtprtprtprtprtprtprtprt', 'ypprt'), [0])

    def test_dense_case_313(self):
        self.assertEqual(pattern_match('zozozozozozozozozozozozozozozozozozozozozozozo', 'zo'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44])

    def test_dense_case_314(self):
        self.assertEqual(pattern_match('pqhwghwghwghwghwghwghwghwghwg', 'pqhwg'), [0])

    def test_dense_case_315(self):
        self.assertEqual(pattern_match('ewdwdwdwdwdwdwdwdwdwdwdwdwd', 'ewd'), [0])

    def test_dense_case_316(self):
        self.assertEqual(pattern_match('wudqwudqwudqwudqwudqwudqwudqwudqwudq', 'wudq'), [0, 4, 8, 12, 16, 20, 24, 28, 32])

    def test_dense_case_317(self):
        self.assertEqual(pattern_match('wwwwwwwwwwwwwwwwwww', 'w'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    def test_dense_case_318(self):
        self.assertEqual(pattern_match('yelyelyelyelyelyelyelyelyelyelyelyelyelyelyelyelyelyelyelyelyelyelyelyelyelyelyelyelyel', 'yel'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84])

    def test_dense_case_319(self):
        self.assertEqual(pattern_match('dndndndndndndndndndndndn', 'dn'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22])

    def test_dense_case_320(self):
        self.assertEqual(pattern_match('ccccccccccccccccc', 'c'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    def test_dense_case_321(self):
        self.assertEqual(pattern_match('hxshxshxshxshxshxshxshxshxshxshxshxshxshxshxshxshxshxshxshxshxshxshxshxshxshxshxshxshxs', 'hxs'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84])

    def test_dense_case_322(self):
        self.assertEqual(pattern_match('mmmmmmmmmmmmmmmmmmmmmmmmmmmmmm', 'm'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29])

    def test_dense_case_323(self):
        self.assertEqual(pattern_match('epbepbepbepbepbepbepbepbepbepbepbepbepbepbepbepb', 'epb'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45])

    def test_dense_case_324(self):
        self.assertEqual(pattern_match('eeeeeeeeeeeeeeeeeeee', 'e'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_dense_case_325(self):
        self.assertEqual(pattern_match('xdxdxdxdxdxdxdxdxdxdxdxdxdxdxdxdxdxdxd', 'xd'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36])

    def test_dense_case_326(self):
        self.assertEqual(pattern_match('knqyyknqyyknqyyknqyyknqyyknqyyknqyyknqyyknqyyknqyyknqyyknqyyknqyyknqyyknqyyknqyyknqyyknqyy', 'knqyy'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85])

    def test_dense_case_327(self):
        self.assertEqual(pattern_match('yyurzrzrzrzrzrzrzrzrzrzrzrzrzrzrzrz', 'yyurz'), [0])

    def test_dense_case_328(self):
        self.assertEqual(pattern_match('kjjiqjjiqjjiqjjiqjjiqjjiqjjiqjjiqjjiqjjiqjjiqjjiqjjiqjjiqjjiqjjiqjjiqjjiqjjiqjjiqjjiqjjiqjjiqjjiqjjiqjjiqjjiq', 'kjjiq'), [0])

    def test_dense_case_329(self):
        self.assertEqual(pattern_match('ujofmmmmmmmmmmmmmmmmmmmmmmm', 'ujofm'), [0])

    def test_dense_case_330(self):
        self.assertEqual(pattern_match('sjxjxjxjxjxjxjxjxjxjxjxjxjxjxjxjxjx', 'sjx'), [0])

    def test_dense_case_331(self):
        self.assertEqual(pattern_match('jbbbbbbb', 'jb'), [0])

    def test_dense_case_332(self):
        self.assertEqual(pattern_match('tambambambambamb', 'tamb'), [0])

    def test_dense_case_333(self):
        self.assertEqual(pattern_match('jerererererererererererererererererererererererer', 'jer'), [0])

    def test_dense_case_334(self):
        self.assertEqual(pattern_match('rqbscccccc', 'rqbsc'), [0])

    def test_dense_case_335(self):
        self.assertEqual(pattern_match('bbbbbbbbbbbbbbbbbbbbbbb', 'b'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])

    def test_dense_case_336(self):
        self.assertEqual(pattern_match('neeeeeeeeeeeeeeeeeeeee', 'ne'), [0])

    def test_dense_case_337(self):
        self.assertEqual(pattern_match('hccccccc', 'hc'), [0])

    def test_dense_case_338(self):
        self.assertEqual(pattern_match('objbjbjbjbj', 'obj'), [0])

    def test_dense_case_339(self):
        self.assertEqual(pattern_match('gpapugpapugpapugpapugpapugpapugpapugpapugpapugpapugpapu', 'gpapu'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50])

    def test_dense_case_340(self):
        self.assertEqual(pattern_match('rlrrrrrrrrrrrrrrrrrrrrrrr', 'rlr'), [0])

    def test_dense_case_341(self):
        self.assertEqual(pattern_match('pftvjvjvjvjvjvjvjvj', 'pftvj'), [0])

    def test_dense_case_342(self):
        self.assertEqual(pattern_match('yismsmsmsmsmsmsmsm', 'yism'), [0])

    def test_dense_case_343(self):
        self.assertEqual(pattern_match('cqroqroqroqroqroqroqroqroqroqroqroqro', 'cqro'), [0])

    def test_dense_case_344(self):
        self.assertEqual(pattern_match('pvpvpvpvpv', 'pv'), [0, 2, 4, 6, 8])

    def test_dense_case_345(self):
        self.assertEqual(pattern_match('ifibsifibsifibsifibsifibsifibsifibsifibsifibsifibsifibsifibsifibs', 'ifibs'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])

    def test_dense_case_346(self):
        self.assertEqual(pattern_match('kdddddddddddddddddddddddddddd', 'kd'), [0])

    def test_dense_case_347(self):
        self.assertEqual(pattern_match('ftftftftftftftftftftftftftftftftftftft', 'ft'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36])

    def test_dense_case_348(self):
        self.assertEqual(pattern_match('uuuuuuuuu', 'u'), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_dense_case_349(self):
        self.assertEqual(pattern_match('vvvvvvvvvv', 'v'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_dense_case_350(self):
        self.assertEqual(pattern_match('ooooooooo', 'o'), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_dense_case_351(self):
        self.assertEqual(pattern_match('rrrrrrrr', 'r'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_dense_case_352(self):
        self.assertEqual(pattern_match('gfvbpppppppppppppppppp', 'gfvbp'), [0])

    def test_dense_case_353(self):
        self.assertEqual(pattern_match('fdnymdnymdnymdnymdnymdnymdnymdnymdnymdnymdnymdnymdnymdnymdnymdnymdnymdnymdnymdnymdnymdnymdnymdnymdnymdnymdnymdnymdnym', 'fdnym'), [0])

    def test_dense_case_354(self):
        self.assertEqual(pattern_match('hgvgvgvgvgvgvgvgvgvgvgvgvgvgvgvgv', 'hgv'), [0])

    def test_dense_case_355(self):
        self.assertEqual(pattern_match('gejejejejejejejejejejejejejejejejej', 'gej'), [0])

    def test_dense_case_356(self):
        self.assertEqual(pattern_match('uxeeeeeeeeeeeeeeeeeeeeeeeeeee', 'uxe'), [0])

    def test_dense_case_357(self):
        self.assertEqual(pattern_match('ysjlsjlsjlsjlsjlsjlsjlsjlsjlsjlsjlsjlsjlsjlsjlsjlsjlsjlsjlsjlsjlsjlsjlsjl', 'ysjl'), [0])

    def test_dense_case_358(self):
        self.assertEqual(pattern_match('wwwwwwwwwwwwwwwwwwwwww', 'w'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])

    def test_dense_case_359(self):
        self.assertEqual(pattern_match('sssssssssssssssssssssssssssss', 's'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28])

    def test_dense_case_360(self):
        self.assertEqual(pattern_match('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz', 'z'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29])

    def test_dense_case_361(self):
        self.assertEqual(pattern_match('rururururururururururururururururururururu', 'ru'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40])

    def test_dense_case_362(self):
        self.assertEqual(pattern_match('fdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfd', 'fd'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50])

    def test_dense_case_363(self):
        self.assertEqual(pattern_match('edwooooooooooo', 'edwo'), [0])

    def test_dense_case_364(self):
        self.assertEqual(pattern_match('yxhztyxhztyxhztyxhztyxhztyxhztyxhztyxhztyxhztyxhztyxhztyxhztyxhztyxhztyxhztyxhztyxhztyxhztyxhztyxhztyxhztyxhzt', 'yxhzt'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105])

    def test_dense_case_365(self):
        self.assertEqual(pattern_match('swcjwwcjwwcjwwcjwwcjwwcjwwcjwwcjwwcjwwcjwwcjwwcjwwcjwwcjwwcjwwcjwwcjwwcjwwcjwwcjwwcjwwcjwwcjwwcjwwcjw', 'swcjw'), [0])

    def test_dense_case_366(self):
        self.assertEqual(pattern_match('ttttt', 't'), [0, 1, 2, 3, 4])

    def test_dense_case_367(self):
        self.assertEqual(pattern_match('nmzmzmzmzmzmzmzmz', 'nmz'), [0])

    def test_dense_case_368(self):
        self.assertEqual(pattern_match('ttttttttttttttt', 't'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_dense_case_369(self):
        self.assertEqual(pattern_match('juuuuuuuuuuuuuuuuuuuuuuuuuuu', 'juu'), [0])

    def test_dense_case_370(self):
        self.assertEqual(pattern_match('qustiustiustiustiustiustiustiustiustiustiustiustiustiustiustiustiustiusti', 'qusti'), [0])

    def test_dense_case_371(self):
        self.assertEqual(pattern_match('xnpkpkpkpkpkpkpkpkpkpkpkpkpkpkpkpkpk', 'xnpk'), [0])

    def test_dense_case_372(self):
        self.assertEqual(pattern_match('vnyyyyyyyyyyyyyyyyyyyyyyyyy', 'vny'), [0])

    def test_dense_case_373(self):
        self.assertEqual(pattern_match('kkkkkkkkkkkkk', 'k'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_dense_case_374(self):
        self.assertEqual(pattern_match('vvvvvvvvvvvvvv', 'v'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_dense_case_375(self):
        self.assertEqual(pattern_match('zxzxzxzxzxzxzxzxzxzxzxzxzxzxzxzxzxzxzxzx', 'zx'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38])

    def test_dense_case_376(self):
        self.assertEqual(pattern_match('zdofofofofofofofofofofofofofofofofofofofof', 'zdof'), [0])

    def test_dense_case_377(self):
        self.assertEqual(pattern_match('hhhhhhhhhhhhhhhhhhhhhhhhhhhhh', 'h'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28])

    def test_dense_case_378(self):
        self.assertEqual(pattern_match('rkmprkmprkmprkmprkmprkmprkmprkmprkmprkmprkmprkmprkmprkmprkmp', 'rkmp'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56])

    def test_dense_case_379(self):
        self.assertEqual(pattern_match('nnnnnnn', 'n'), [0, 1, 2, 3, 4, 5, 6])

    def test_dense_case_380(self):
        self.assertEqual(pattern_match('bfefefefefefefefefefefefefefefefefefefefefefefefe', 'bfe'), [0])

    def test_dense_case_381(self):
        self.assertEqual(pattern_match('ufsfsfsfsfsfsfsfsfsfsfsfsfsfsfsfsfs', 'ufs'), [0])

    def test_dense_case_382(self):
        self.assertEqual(pattern_match('mapmapmapmapmapmap', 'map'), [0, 3, 6, 9, 12, 15])

    def test_dense_case_383(self):
        self.assertEqual(pattern_match('mamamamamamamamamamamamamamamamamamamamamamama', 'ma'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44])

    def test_dense_case_384(self):
        self.assertEqual(pattern_match('rxwwwwwwwwwwwwwwwwwwwwwwwwww', 'rxw'), [0])

    def test_dense_case_385(self):
        self.assertEqual(pattern_match('krererererererererererererererererere', 'kre'), [0])

    def test_dense_case_386(self):
        self.assertEqual(pattern_match('bwlwwwwwwwwwwwwww', 'bwlw'), [0])

    def test_dense_case_387(self):
        self.assertEqual(pattern_match('desybybybybybybybybybybybybybybybybybybybybyb', 'desyb'), [0])

    def test_dense_case_388(self):
        self.assertEqual(pattern_match('nnnnnnnnnnnnnn', 'n'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_dense_case_389(self):
        self.assertEqual(pattern_match('auuuuuuuuuuuu', 'au'), [0])

    def test_dense_case_390(self):
        self.assertEqual(pattern_match('ezzzzzz', 'ez'), [0])

    def test_dense_case_391(self):
        self.assertEqual(pattern_match('qqqqqqqqqqqqqqqqqqqqqqqqqqq', 'qq'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])

    def test_dense_case_392(self):
        self.assertEqual(pattern_match('pppppppp', 'p'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_dense_case_393(self):
        self.assertEqual(pattern_match('rpgggggg', 'rpg'), [0])

    def test_dense_case_394(self):
        self.assertEqual(pattern_match('jojojojojojojojojojojojojojojojojojojojojojojojojo', 'jo'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48])

    def test_dense_case_395(self):
        self.assertEqual(pattern_match('ykcyykcyykcyykcyykcyykcyykcyykcyykcyykcyykcyykcyykcyykcy', 'ykcy'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52])

    def test_dense_case_396(self):
        self.assertEqual(pattern_match('zvolvolvolvolvolvolvolvol', 'zvol'), [0])

    def test_dense_case_397(self):
        self.assertEqual(pattern_match('cvddyddyddyddyddyddyddyddyddyddyddyddyddyddyddyddyddyddyddyddyddyddyddyddyddyddyddy', 'cvddy'), [0])

    def test_dense_case_398(self):
        self.assertEqual(pattern_match('nyyyyyyyyyyy', 'ny'), [0])

    def test_dense_case_399(self):
        self.assertEqual(pattern_match('llllllllllllllllllllllllllll', 'l'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27])

    def test_dense_case_400(self):
        self.assertEqual(pattern_match('lxuoduoduoduoduoduoduoduod', 'lxuod'), [0])

    def test_dense_case_401(self):
        self.assertEqual(pattern_match('zwtoooooooooooooooooooooooooooooo', 'zwto'), [0])

    def test_dense_case_402(self):
        self.assertEqual(pattern_match('nnnnn', 'n'), [0, 1, 2, 3, 4])

    def test_dense_case_403(self):
        self.assertEqual(pattern_match('zvqgzvqgzvqgzvqgzvqgzvqgzvqgzvqgzvqg', 'zvqg'), [0, 4, 8, 12, 16, 20, 24, 28, 32])

    def test_dense_case_404(self):
        self.assertEqual(pattern_match('whuwhuwhuwhuwhuwhu', 'whu'), [0, 3, 6, 9, 12, 15])

    def test_dense_case_405(self):
        self.assertEqual(pattern_match('uoncrrrrrrrrrr', 'uoncr'), [0])

    def test_dense_case_406(self):
        self.assertEqual(pattern_match('szzzzzzzzzzzzzzzzzzzzz', 'sz'), [0])

    def test_dense_case_407(self):
        self.assertEqual(pattern_match('dadadadadadadadadadadadadadadadadadadadada', 'da'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40])

    def test_dense_case_408(self):
        self.assertEqual(pattern_match('olayrayrayrayrayrayrayrayrayrayrayrayrayrayrayrayrayrayrayrayrayrayrayrayrayrayrayrayrayrayr', 'olayr'), [0])

    def test_dense_case_409(self):
        self.assertEqual(pattern_match('rjjjjjjjjj', 'rj'), [0])

    def test_dense_case_410(self):
        self.assertEqual(pattern_match('uxuxuxuxuxuxux', 'ux'), [0, 2, 4, 6, 8, 10, 12])

    def test_dense_case_411(self):
        self.assertEqual(pattern_match('ajmmmmmmmmmmmmmmmmmmmmmmmmmmmm', 'ajm'), [0])

    def test_dense_case_412(self):
        self.assertEqual(pattern_match('oioioioioioioioioioioioioioioioioioioioioioioioioioioioioioi', 'oi'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58])

    def test_dense_case_413(self):
        self.assertEqual(pattern_match('lllll', 'l'), [0, 1, 2, 3, 4])

    def test_dense_case_414(self):
        self.assertEqual(pattern_match('wtwmzzzzzzzzzzzzzzzzzzzzzzz', 'wtwmz'), [0])

    def test_dense_case_415(self):
        self.assertEqual(pattern_match('blgggggggggggggggggggggggggggg', 'blg'), [0])

    def test_dense_case_416(self):
        self.assertEqual(pattern_match('nnnnn', 'n'), [0, 1, 2, 3, 4])

    def test_dense_case_417(self):
        self.assertEqual(pattern_match('hjcjcjcjcjcjcjcjcjcjcjcjcjcjcjcjcjcjcjcjcjcjc', 'hjc'), [0])

    def test_dense_case_418(self):
        self.assertEqual(pattern_match('mtzezezezezeze', 'mtze'), [0])

    def test_dense_case_419(self):
        self.assertEqual(pattern_match('uuuuuuuuuuuuuuuuuuu', 'u'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    def test_dense_case_420(self):
        self.assertEqual(pattern_match('wtozbtozbtozbtozbtozbtozbtozbtozbtozbtozb', 'wtozb'), [0])

    def test_dense_case_421(self):
        self.assertEqual(pattern_match('rbrbrbrbrbrb', 'rb'), [0, 2, 4, 6, 8, 10])

    def test_dense_case_422(self):
        self.assertEqual(pattern_match('roooooooooooooooooooooooooo', 'ro'), [0])

    def test_dense_case_423(self):
        self.assertEqual(pattern_match('xyqqggggggggggggggggggggggggggg', 'xyqqg'), [0])

    def test_dense_case_424(self):
        self.assertEqual(pattern_match('ylililililililililililililililililililililililililililililili', 'yli'), [0])

    def test_dense_case_425(self):
        self.assertEqual(pattern_match('wfmfmfmfmfmfmfmfmfmfmfmfmfmfmfmfmfmfmfm', 'wfm'), [0])

    def test_dense_case_426(self):
        self.assertEqual(pattern_match('wzzzzzzzzzzzzzzzzz', 'wz'), [0])

    def test_dense_case_427(self):
        self.assertEqual(pattern_match('adekmmmmmmmmmmmmmmmmmmmmmm', 'adekm'), [0])

    def test_dense_case_428(self):
        self.assertEqual(pattern_match('iknfnnnnnnnnnnnnnnnnnnnnnnnnnnnn', 'iknfn'), [0])

    def test_dense_case_429(self):
        self.assertEqual(pattern_match('qsvbkqsvbkqsvbkqsvbkqsvbkqsvbkqsvbkqsvbkqsvbkqsvbkqsvbkqsvbkqsvbkqsvbk', 'qsvbk'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65])

    def test_dense_case_430(self):
        self.assertEqual(pattern_match('csxcsxcsxcsxcsxcsxcsxcsxcsxcsxcsxcsxcsxcsxcsxcsxcsxcsxcsxcsx', 'csx'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57])

    def test_dense_case_431(self):
        self.assertEqual(pattern_match('plfruplfruplfruplfruplfruplfruplfruplfru', 'plfru'), [0, 5, 10, 15, 20, 25, 30, 35])

    def test_dense_case_432(self):
        self.assertEqual(pattern_match('iqibrrrrrrrr', 'iqibr'), [0])

    def test_dense_case_433(self):
        self.assertEqual(pattern_match('eplxjjjjjjjjjjjjj', 'eplxj'), [0])

    def test_dense_case_434(self):
        self.assertEqual(pattern_match('zlzlzlzlzlzlzlzlzlzlzlzlzlzlzlzlzlzlzl', 'zl'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36])

    def test_dense_case_435(self):
        self.assertEqual(pattern_match('ndndndndndndndndndndndndndndndndndndndndndndndndndnd', 'nd'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50])

    def test_dense_case_436(self):
        self.assertEqual(pattern_match('zzzzzzzzzzzzzzzzzzzzzzzzzz', 'z'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])

    def test_dense_case_437(self):
        self.assertEqual(pattern_match('enhqnhqnhqnhqnhqnhqnhqnhqnhqnhqnhqnhqnhqnhqnhqnhqnhqnhqnhq', 'enhq'), [0])

    def test_dense_case_438(self):
        self.assertEqual(pattern_match('pafffffffffffffffffffffffffff', 'paf'), [0])

    def test_dense_case_439(self):
        self.assertEqual(pattern_match('fnfanfanfanfanfanfanfanfanfanfanfanfanfanfanfanfanfanfanfanfanfanfanfanfa', 'fnfa'), [0])

    def test_dense_case_440(self):
        self.assertEqual(pattern_match('ezqknezqknezqknezqknezqknezqknezqknezqkn', 'ezqkn'), [0, 5, 10, 15, 20, 25, 30, 35])

    def test_dense_case_441(self):
        self.assertEqual(pattern_match('egyhegyhegyhegyhegyhegyhegyhegyhegyhegyhegyhegyhegyhegyhegyhegyhegyhegyhegyhegyhegyhegyhegyhegyhegyhegyhegyhegyhegyhegyh', 'egyh'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100, 104, 108, 112, 116])

    def test_dense_case_442(self):
        self.assertEqual(pattern_match('ffffffffffffffff', 'f'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_dense_case_443(self):
        self.assertEqual(pattern_match('zbbbbbbbbbbbbbbbbbbbb', 'zb'), [0])

    def test_dense_case_444(self):
        self.assertEqual(pattern_match('zqvqzqvqzqvqzqvqzqvqzqvqzqvqzqvqzqvqzqvqzqvqzqvqzqvqzqvqzqvqzqvqzqvqzqvqzqvqzqvqzqvqzqvqzqvqzqvqzqvqzqvqzqvqzqvqz', 'zqvqz'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100, 104, 108])

    def test_dense_case_445(self):
        self.assertEqual(pattern_match('vtvtvtvtvtvt', 'vt'), [0, 2, 4, 6, 8, 10])

    def test_dense_case_446(self):
        self.assertEqual(pattern_match('lbblbblbblbblbblbblbblbblbblbblbblbblbblbblbblbblbblbblbb', 'lbb'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54])

    def test_dense_case_447(self):
        self.assertEqual(pattern_match('ihhhhhhhhhhhhhhhhhhhhhhh', 'ih'), [0])

    def test_dense_case_448(self):
        self.assertEqual(pattern_match('nnnnnnnnnnnnnnnnnnnnnnnnnn', 'n'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])

    def test_dense_case_449(self):
        self.assertEqual(pattern_match('nxodgggggggggggg', 'nxodg'), [0])

    def test_dense_case_450(self):
        self.assertEqual(pattern_match('rmmomomomomomomo', 'rmmo'), [0])

    def test_dense_case_451(self):
        self.assertEqual(pattern_match('krqqqqqqqqq', 'krq'), [0])

    def test_dense_case_452(self):
        self.assertEqual(pattern_match('jjjjjjjjj', 'j'), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_dense_case_453(self):
        self.assertEqual(pattern_match('njjjjjjjjjjjjjjj', 'nj'), [0])

    def test_dense_case_454(self):
        self.assertEqual(pattern_match('hhhhhhhhhhhhhhhhhhhhhhhhh', 'hh'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])

    def test_dense_case_455(self):
        self.assertEqual(pattern_match('hofzufzufzufzufzu', 'hofzu'), [0])

    def test_dense_case_456(self):
        self.assertEqual(pattern_match('zzssezzssezzssezzssezzssezzssezzssezzssezzssezzssezzssezzssezzssezzssezzssezzssezzssezzssezzssezzssezzssezzssezzssezzssezzssezzssezzssezzsse', 'zzsse'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135])

    def test_dense_case_457(self):
        self.assertEqual(pattern_match('mnqbqbqbqbqbqbqbqbqbqbqbqbqbqb', 'mnqb'), [0])

    def test_dense_case_458(self):
        self.assertEqual(pattern_match('aaaaaaaaaaaaaaaaaaaaaaaaaaa', 'a'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26])

    def test_dense_case_459(self):
        self.assertEqual(pattern_match('vwvwvwvwvwvwvwvwvwvwvwvwvwvwvwvwvwvwvwvwvwvwvwvwvw', 'vw'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48])

    def test_dense_case_460(self):
        self.assertEqual(pattern_match('lvyzyzyzyzyz', 'lvyz'), [0])

    def test_dense_case_461(self):
        self.assertEqual(pattern_match('mlaaaaaaaaaaaaaaa', 'mla'), [0])

    def test_dense_case_462(self):
        self.assertEqual(pattern_match('jdixxxxxxxxxxxx', 'jdix'), [0])

    def test_dense_case_463(self):
        self.assertEqual(pattern_match('iuwwwwww', 'iuw'), [0])

    def test_dense_case_464(self):
        self.assertEqual(pattern_match('ttttttttt', 't'), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_dense_case_465(self):
        self.assertEqual(pattern_match('yoooooooooooooooooooooooooooooo', 'yo'), [0])

    def test_dense_case_466(self):
        self.assertEqual(pattern_match('mmmmmmmmmmmmmmmmmmm', 'm'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    def test_dense_case_467(self):
        self.assertEqual(pattern_match('labbbbbbbbbbbbbb', 'lab'), [0])

    def test_dense_case_468(self):
        self.assertEqual(pattern_match('zefefefefefefefefefefefefefefefef', 'zef'), [0])

    def test_dense_case_469(self):
        self.assertEqual(pattern_match('culzculzculzculzculzculzculzculzculzculzculz', 'culz'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40])

    def test_dense_case_470(self):
        self.assertEqual(pattern_match('yvnnnnnnnnnnn', 'yvn'), [0])

    def test_dense_case_471(self):
        self.assertEqual(pattern_match('ttttttttt', 't'), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_dense_case_472(self):
        self.assertEqual(pattern_match('ttttttttttttttt', 't'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_dense_case_473(self):
        self.assertEqual(pattern_match('wvrwvrwvrwvrwvrwvrwvrwvrwvrwvrwvrwvrwvrwvrwvrwvrwvrwvrwvrwvrwvr', 'wvr'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60])

    def test_dense_case_474(self):
        self.assertEqual(pattern_match('ggggggggggggggggggg', 'g'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    def test_dense_case_475(self):
        self.assertEqual(pattern_match('mwmdmdmdmdmdmdmdmdmdmdmdmdmdmdmdmdmdmdmdmdmdmdmdmd', 'mwmd'), [0])

    def test_dense_case_476(self):
        self.assertEqual(pattern_match('fwywkwywkwywkwywkwywkwywkwywkwywkwywkwywkwywkwywkwywkwywkwywkwywkwywkwywkwywkwywkwywkwywkwywkwywkwywkwywkwywk', 'fwywk'), [0])

    def test_dense_case_477(self):
        self.assertEqual(pattern_match('swmmmmmmmmmmmmmmmm', 'swm'), [0])

    def test_dense_case_478(self):
        self.assertEqual(pattern_match('ijijijijijijijijijijijijijijijijijijijijij', 'ij'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40])

    def test_dense_case_479(self):
        self.assertEqual(pattern_match('jlwhjlwhjlwhjlwhjlwhjlwhjlwhjlwhjlwhjlwhjlwhjlwhjlwhjlwhjlwhjlwhjlwhjlwhjlwhjlwhjlwhjlwhjlwhjlwhjlwhjlwh', 'jlwh'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100])

    def test_dense_case_480(self):
        self.assertEqual(pattern_match('ayrayrayrayrayrayrayr', 'ayr'), [0, 3, 6, 9, 12, 15, 18])

    def test_dense_case_481(self):
        self.assertEqual(pattern_match('pjmxpjmxpjmxpjmxpjmxpjmxpjmxpjmxpjmxpjmxpjmxpjmxpjmxpjmxpjmxpjmxpjmxpjmxpjmxpjmxpjmxpjmxpjmx', 'pjmx'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88])

    def test_dense_case_482(self):
        self.assertEqual(pattern_match('qzgzgzgzgzg', 'qzg'), [0])

    def test_dense_case_483(self):
        self.assertEqual(pattern_match('lbdvlbdvlbdvlbdvlbdvlbdvlbdvlbdvlbdvlbdvlbdvlbdvlbdvlbdvlbdvlbdvlbdvlbdvlbdvlbdvlbdvlbdvlbdv', 'lbdv'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88])

    def test_dense_case_484(self):
        self.assertEqual(pattern_match('amsmsmsmsmsmsmsms', 'ams'), [0])

    def test_dense_case_485(self):
        self.assertEqual(pattern_match('aekgggggggggggggggggggggggggg', 'aekg'), [0])

    def test_dense_case_486(self):
        self.assertEqual(pattern_match('yespyespyespyespyesp', 'yesp'), [0, 4, 8, 12, 16])

    def test_dense_case_487(self):
        self.assertEqual(pattern_match('tytsssssssssssssss', 'tyts'), [0])

    def test_dense_case_488(self):
        self.assertEqual(pattern_match('gotpotpotpotpotpotpotpotpotpotpotpotpotpotpotpotp', 'gotp'), [0])

    def test_dense_case_489(self):
        self.assertEqual(pattern_match('qjkepepepepepepepepepepepepep', 'qjkep'), [0])

    def test_dense_case_490(self):
        self.assertEqual(pattern_match('tmcwcwcwcwcw', 'tmcw'), [0])

    def test_dense_case_491(self):
        self.assertEqual(pattern_match('qvaaaaaaaaaaa', 'qva'), [0])

    def test_dense_case_492(self):
        self.assertEqual(pattern_match('zdrppppppppppp', 'zdrp'), [0])

    def test_dense_case_493(self):
        self.assertEqual(pattern_match('wwwwwwwwwwwwwwwwwwwww', 'w'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

    def test_dense_case_494(self):
        self.assertEqual(pattern_match('javrrrrrrrrrrrrrrrrrrrrrrrrrrr', 'javr'), [0])

    def test_dense_case_495(self):
        self.assertEqual(pattern_match('dalmmmmmmmmmmmmm', 'dalm'), [0])

    def test_dense_case_496(self):
        self.assertEqual(pattern_match('mdvmcvmcvmcvmcvmcvmcvmcvmcvmc', 'mdvmc'), [0])

    def test_dense_case_497(self):
        self.assertEqual(pattern_match('pixxxxxxxxx', 'pix'), [0])

    def test_dense_case_498(self):
        self.assertEqual(pattern_match('bobobobobobobobobobobobobobo', 'bo'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26])

    def test_dense_case_499(self):
        self.assertEqual(pattern_match('barevevevevevevevevevevevevevevevev', 'barev'), [0])

    def test_dense_case_500(self):
        self.assertEqual(pattern_match('riqriqriqriqriqriq', 'riq'), [0, 3, 6, 9, 12, 15])

    def test_dense_case_501(self):
        self.assertEqual(pattern_match('njdsuuuuuuuuuuuuuuuuu', 'njdsu'), [0])

    def test_dense_case_502(self):
        self.assertEqual(pattern_match('zbpoeeeeeeeeeeeeeeeeeeeeeeeeeee', 'zbpoe'), [0])

    def test_dense_case_503(self):
        self.assertEqual(pattern_match('wvyyyyyyyyy', 'wvy'), [0])

    def test_dense_case_504(self):
        self.assertEqual(pattern_match('nwcwcwcwcwcwcwcwc', 'nwc'), [0])

    def test_dense_case_505(self):
        self.assertEqual(pattern_match('rwwwwwww', 'rw'), [0])

    def test_dense_case_506(self):
        self.assertEqual(pattern_match('nvrggggggggggggggggg', 'nvrg'), [0])

    def test_dense_case_507(self):
        self.assertEqual(pattern_match('zomxzomxzomxzomxzomxzomxzomxzomxzomxz', 'zomxz'), [0, 4, 8, 12, 16, 20, 24, 28, 32])

    def test_dense_case_508(self):
        self.assertEqual(pattern_match('nnqsnnqsnnqsnnqsnnqsnnqsnnqsnnqsnnqsnnqs', 'nnqs'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36])

    def test_dense_case_509(self):
        self.assertEqual(pattern_match('uuuuuuuuuuu', 'u'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_dense_case_510(self):
        self.assertEqual(pattern_match('vdvdvdvdvdvdvdvdvdvdvdvdvdvdvdvdvdvdvdvdvdvd', 'vd'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42])

    def test_dense_case_511(self):
        self.assertEqual(pattern_match('nccsyccsyccsyccsyccsyccsyccsyccsyccsyccsyccsyccsyccsyccsyccsyccsy', 'nccsy'), [0])

    def test_dense_case_512(self):
        self.assertEqual(pattern_match('lxvrdxvrdxvrdxvrdxvrdxvrdxvrdxvrdxvrdxvrdxvrdxvrdxvrdxvrdxvrdxvrdxvrdxvrdxvrdxvrdxvrdxvrdxvrd', 'lxvrd'), [0])

    def test_dense_case_513(self):
        self.assertEqual(pattern_match('tkrkrkrkrkr', 'tkr'), [0])

    def test_dense_case_514(self):
        self.assertEqual(pattern_match('fifccccc', 'fifc'), [0])

    def test_dense_case_515(self):
        self.assertEqual(pattern_match('ashhhhhhhhhhhhhhhhhhhhhhhh', 'ash'), [0])

    def test_dense_case_516(self):
        self.assertEqual(pattern_match('gcvtststststststststststststststststststststststststs', 'gcvts'), [0])

    def test_dense_case_517(self):
        self.assertEqual(pattern_match('dttttttttttttt', 'dt'), [0])

    def test_dense_case_518(self):
        self.assertEqual(pattern_match('fmsfmsfmsfmsfmsfmsfmsfmsfmsfmsfmsfmsfmsfmsfmsfmsfmsfmsfmsfmsfmsfmsfmsfmsfmsfms', 'fms'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75])

    def test_dense_case_519(self):
        self.assertEqual(pattern_match('eeeeeeeeeeeeeeeeeeeeeeeeeeeee', 'e'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28])

    def test_dense_case_520(self):
        self.assertEqual(pattern_match('vlnbzbzbzbzbzbzbzbzbzbzbzbzbzbzbzbzbzbzbzbzbzbzbzbzbzbzbzbz', 'vlnbz'), [0])

    def test_dense_case_521(self):
        self.assertEqual(pattern_match('kbxvuuuuuuuuu', 'kbxvu'), [0])

    def test_dense_case_522(self):
        self.assertEqual(pattern_match('rkptptptptptptptptptptptptptptptptpt', 'rkpt'), [0])

    def test_dense_case_523(self):
        self.assertEqual(pattern_match('hfqqqqqqqqqqqqqqqqqqqqqqq', 'hfq'), [0])

    def test_dense_case_524(self):
        self.assertEqual(pattern_match('fhfddfddfddfddfddfddfddfddfddfddfddfddfddfddfddfddfddfddfddfddfddfdd', 'fhfdd'), [0])

    def test_dense_case_525(self):
        self.assertEqual(pattern_match('uiuiuiuiuiuiuiuiuiuiuiuiuiuiuiuiuiuiuiuiuiuiuiu', 'uiu'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44])

    def test_dense_case_526(self):
        self.assertEqual(pattern_match('apapapapapapapapapapapapap', 'ap'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])

    def test_dense_case_527(self):
        self.assertEqual(pattern_match('skpugkpugkpugkpugkpugkpugkpugkpugkpugkpugkpug', 'skpug'), [0])

    def test_dense_case_528(self):
        self.assertEqual(pattern_match('cdvvvvvvvvvvvvvvvvvvvv', 'cdv'), [0])

    def test_dense_case_529(self):
        self.assertEqual(pattern_match('vrgifffff', 'vrgif'), [0])

    def test_dense_case_530(self):
        self.assertEqual(pattern_match('xdrxdrxdrxdrxdrxdrxdrxdrxdrxdrxdrxdrxdrxdrxdrxdrxdrxdrxdrxdr', 'xdr'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57])

    def test_dense_case_531(self):
        self.assertEqual(pattern_match('kwkwkwkwkwkwkwkwkwkwkwkwkwkwkw', 'kw'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28])

    def test_dense_case_532(self):
        self.assertEqual(pattern_match('ffffffffffffffff', 'f'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_dense_case_533(self):
        self.assertEqual(pattern_match('awmogawmogawmogawmogawmogawmogawmogawmogawmogawmogawmogawmogawmogawmogawmogawmogawmogawmogawmogawmogawmogawmogawmogawmogawmogawmogawmogawmog', 'awmog'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135])

    def test_dense_case_534(self):
        self.assertEqual(pattern_match('xcohmxcohmxcohmxcohmxcohmxcohmxcohmxcohmxcohmxcohmxcohmxcohmxcohmxcohmxcohm', 'xcohm'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70])

    def test_dense_case_535(self):
        self.assertEqual(pattern_match('qqqqqqqqqqqqqqqqq', 'q'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    def test_dense_case_536(self):
        self.assertEqual(pattern_match('ewgegegegegegegegegegegegegegegegegegegegegege', 'ewge'), [0])

    def test_dense_case_537(self):
        self.assertEqual(pattern_match('klnclnclnclnclnclnclnclnclnc', 'klnc'), [0])

    def test_dense_case_538(self):
        self.assertEqual(pattern_match('makvzkvzkvzkvzkvzkvzkvzkvz', 'makvz'), [0])

    def test_dense_case_539(self):
        self.assertEqual(pattern_match('povpovpovpovpovpovpovpovpovpovpovpovpovpovpovpovpovpovpovpovpovpov', 'pov'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63])

    def test_dense_case_540(self):
        self.assertEqual(pattern_match('ahbahbahbahbahbahbahbahbahb', 'ahb'), [0, 3, 6, 9, 12, 15, 18, 21, 24])

    def test_dense_case_541(self):
        self.assertEqual(pattern_match('pppppppppppppppppppppppppppppppppppppppppppppppppppppppppp', 'pp'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56])

    def test_dense_case_542(self):
        self.assertEqual(pattern_match('nhnhnhnhnhnhnh', 'nh'), [0, 2, 4, 6, 8, 10, 12])

    def test_dense_case_543(self):
        self.assertEqual(pattern_match('hhhhhhhhhhhhhhhhhhhhhhhhhh', 'h'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])

    def test_dense_case_544(self):
        self.assertEqual(pattern_match('hoiiiiiiiiiiiiiii', 'hoi'), [0])

    def test_dense_case_545(self):
        self.assertEqual(pattern_match('elvelvelvelvelvelvelvelvelvelvelvelvelvelvelvelvelvelv', 'elv'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51])

    def test_dense_case_546(self):
        self.assertEqual(pattern_match('jvbkxbkxbkxbkxbkxbkxbkxbkxbkxbkxbkxbkxbkxbkxbkxbkxbkxbkxbkxbkxbkxbkx', 'jvbkx'), [0])

    def test_dense_case_547(self):
        self.assertEqual(pattern_match('ocococococococococococococ', 'oc'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])

    def test_dense_case_548(self):
        self.assertEqual(pattern_match('fgggggggggggggggggggggggggg', 'fg'), [0])

    def test_dense_case_549(self):
        self.assertEqual(pattern_match('wfhojfhojfhojfhojfhojfhojfhojfhojfhojfhojfhojfhojfhojfhojfhojfhojfhojfhojfhojfhojfhojfhojfhoj', 'wfhoj'), [0])

    def test_dense_case_550(self):
        self.assertEqual(pattern_match('hucgucgucgucgucgucgucgucgucgucgucg', 'hucg'), [0])

    def test_dense_case_551(self):
        self.assertEqual(pattern_match('mmmmmmmmmmm', 'm'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_dense_case_552(self):
        self.assertEqual(pattern_match('mimimimimimimimimimimimimimimimimimimimimimi', 'mi'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42])

    def test_dense_case_553(self):
        self.assertEqual(pattern_match('mimimimimi', 'mi'), [0, 2, 4, 6, 8])

    def test_dense_case_554(self):
        self.assertEqual(pattern_match('rskrskrskrskrskrskrskrskrskrskrskrskrskrskrskrskrskrskrskrskrskrskrskrskrskrskrskrsk', 'rsk'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81])

    def test_dense_case_555(self):
        self.assertEqual(pattern_match('ouououououououououououououououououououou', 'ou'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38])

    def test_dense_case_556(self):
        self.assertEqual(pattern_match('iqmiqmiqmiqmiqmiqmiqmiqmiqmiqmiqmiqmiqmiqm', 'iqm'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39])

    def test_dense_case_557(self):
        self.assertEqual(pattern_match('wwwwwwwwwwwwwwwwww', 'w'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])

    def test_dense_case_558(self):
        self.assertEqual(pattern_match('fmnlnlnlnlnlnl', 'fmnl'), [0])

    def test_dense_case_559(self):
        self.assertEqual(pattern_match('zwrrrrrrrrrrrrrrrrrr', 'zwr'), [0])

    def test_dense_case_560(self):
        self.assertEqual(pattern_match('noesoesoesoesoesoesoesoesoesoesoesoesoesoesoesoesoesoesoesoesoesoesoesoesoesoesoesoesoesoes', 'noes'), [0])

    def test_dense_case_561(self):
        self.assertEqual(pattern_match('owowowowowowowowowowow', 'ow'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

    def test_dense_case_562(self):
        self.assertEqual(pattern_match('mmmmmmmmmmm', 'm'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_dense_case_563(self):
        self.assertEqual(pattern_match('fbjlmjlmjlmjlmjlmjlmjlmjlmjlmjlmjlmjlmjlmjlmjlmjlm', 'fbjlm'), [0])

    def test_dense_case_564(self):
        self.assertEqual(pattern_match('znpznpznpznpznpznpznpznpznpznpznpznpznpznpznpznpznpznpznpznpznpznpznpznpznpznpznpznp', 'znp'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81])

    def test_dense_case_565(self):
        self.assertEqual(pattern_match('qqaqqaqqaqqaqqaqqaqqaqqaqqaqqaqqaqqaqqaqqaqqaqqaqqaqqaqqaqqa', 'qqa'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57])

    def test_dense_case_566(self):
        self.assertEqual(pattern_match('pppppppppppppppppppppp', 'p'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])

    def test_dense_case_567(self):
        self.assertEqual(pattern_match('llbjfjfjfjfjfjfjfjfjfjfjfjf', 'llbjf'), [0])

    def test_dense_case_568(self):
        self.assertEqual(pattern_match('slllllllllllll', 'sl'), [0])

    def test_dense_case_569(self):
        self.assertEqual(pattern_match('lasvsvsvsvsvsvsvsvsvsvsvsvsvsvsvsvsvsvsvsvsvsvsvsvsvsvsvsvsvsvs', 'lasvs'), [0])

    def test_dense_case_570(self):
        self.assertEqual(pattern_match('ppppp', 'p'), [0, 1, 2, 3, 4])

    def test_dense_case_571(self):
        self.assertEqual(pattern_match('pppppppppppppppppppp', 'p'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_dense_case_572(self):
        self.assertEqual(pattern_match('ffffffffffffffff', 'f'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_dense_case_573(self):
        self.assertEqual(pattern_match('kaazzzzzzzzz', 'kaaz'), [0])

    def test_dense_case_574(self):
        self.assertEqual(pattern_match('cqxqxqxqxqxqxqxqxqxqxqxqxqxqxqxqxqxqxqxqxqxqxqxqxqxqxqxqxqxqx', 'cqx'), [0])

    def test_dense_case_575(self):
        self.assertEqual(pattern_match('zmnyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy', 'zmnyy'), [0])

    def test_dense_case_576(self):
        self.assertEqual(pattern_match('zcewzzzzzzzzzzzzzzzzz', 'zcewz'), [0])

    def test_dense_case_577(self):
        self.assertEqual(pattern_match('ublblblblblblblbl', 'ubl'), [0])

    def test_dense_case_578(self):
        self.assertEqual(pattern_match('aaaaaaaaaaaaaaaaaaaa', 'a'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_dense_case_579(self):
        self.assertEqual(pattern_match('ffqffqffqffqffqffqffqffqffqffqffqffqffqffqffqffqffq', 'ffq'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48])

    def test_dense_case_580(self):
        self.assertEqual(pattern_match('kkkkkkkkkkk', 'k'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_dense_case_581(self):
        self.assertEqual(pattern_match('biiwiwiwiwiwiwiwiwiwiwiwiwiwiwiwiwiwiwiwiwiwiwiw', 'biiw'), [0])

    def test_dense_case_582(self):
        self.assertEqual(pattern_match('aksksksksksksksksksksksksksksksksksksk', 'aksk'), [0])

    def test_dense_case_583(self):
        self.assertEqual(pattern_match('nwanwanwanwanwanwanwanwanwanwanwanwanwanwanwanwanwanwanwanwanwa', 'nwa'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60])

    def test_dense_case_584(self):
        self.assertEqual(pattern_match('xxxxxxxxxxxxxxxxxxx', 'x'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    def test_dense_case_585(self):
        self.assertEqual(pattern_match('akakakakakakakakakakakakakakakakakakakakakak', 'ak'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42])

    def test_dense_case_586(self):
        self.assertEqual(pattern_match('cusycusycusycusycusycusycusycusycusycusycusycusycusycusycusycusycusycusycusy', 'cusy'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72])

    def test_dense_case_587(self):
        self.assertEqual(pattern_match('wcscscscscscscscscs', 'wcs'), [0])

    def test_dense_case_588(self):
        self.assertEqual(pattern_match('czbczbczbczbczbczbczbczbczbczbczbczbczbczbczbczbczbczbczbczbczbczbczb', 'czb'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66])

    def test_dense_case_589(self):
        self.assertEqual(pattern_match('nfcvfcvfcvfcvfcvfcvfcvfcvfcvfcvfcvfcvfcvfcvfcvfcvfcvfcvfcvfcvfcvfcvfcvfcvfcvfcvfcvfcvfcvfcv', 'nfcv'), [0])

    def test_dense_case_590(self):
        self.assertEqual(pattern_match('zsrzsrzsrzsrzsrzsrzsrzsrzsrzsrzsrzsrzsrzsrzsrzsrzsrzsrzsrzsrzsrzsrzsr', 'zsr'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66])

    def test_dense_case_591(self):
        self.assertEqual(pattern_match('nxnxnxnxnxnx', 'nx'), [0, 2, 4, 6, 8, 10])

    def test_dense_case_592(self):
        self.assertEqual(pattern_match('zggggggggggggggggggggg', 'zg'), [0])

    def test_dense_case_593(self):
        self.assertEqual(pattern_match('uvvtkvtkvtkvtkvtkvtkvtkvtkvtkvtkvtkvtkvtkvtkvtkvtk', 'uvvtk'), [0])

    def test_dense_case_594(self):
        self.assertEqual(pattern_match('ndvvvvvvvvvvvvvvvvvvvvvvv', 'ndv'), [0])

    def test_dense_case_595(self):
        self.assertEqual(pattern_match('thhhhhhhhhhh', 'th'), [0])

    def test_dense_case_596(self):
        self.assertEqual(pattern_match('ufffffffffffffffffffffff', 'uf'), [0])

    def test_dense_case_597(self):
        self.assertEqual(pattern_match('mlelelelelelelelelelelelelelelelelelelele', 'mle'), [0])

    def test_dense_case_598(self):
        self.assertEqual(pattern_match('evbvbvbvbvbvbvbvbvbvbvbvbvbvbvbvbvbvb', 'evb'), [0])

    def test_dense_case_599(self):
        self.assertEqual(pattern_match('nnnnnnnnn', 'n'), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_dense_case_600(self):
        self.assertEqual(pattern_match('cjmwzwzwzwzwzwzwzwzwzwzwzwzwzwzwzwzwzwzwzwzwzwz', 'cjmwz'), [0])

    def test_dense_case_601(self):
        self.assertEqual(pattern_match('izhknhknhknhknhknhknhknhknhknhknhknhknhknhknhkn', 'izhkn'), [0])

    def test_dense_case_602(self):
        self.assertEqual(pattern_match('zjzjzjzjzjzjzjzjzjzjzjzjzjzjzjzjzjzjzjzj', 'zj'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38])

    def test_dense_case_603(self):
        self.assertEqual(pattern_match('zsssss', 'zs'), [0])

    def test_dense_case_604(self):
        self.assertEqual(pattern_match('uuuuuuuuuuuuu', 'u'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_dense_case_605(self):
        self.assertEqual(pattern_match('ukqqqqqqqqqqqqqqqqqqqqqqqqqqqq', 'ukq'), [0])

    def test_dense_case_606(self):
        self.assertEqual(pattern_match('oodddddddddddddddddddd', 'ood'), [0])

    def test_dense_case_607(self):
        self.assertEqual(pattern_match('ibdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdw', 'ibdw'), [0])

    def test_dense_case_608(self):
        self.assertEqual(pattern_match('lbbbbbbbbbbbbbbbbb', 'lb'), [0])

    def test_dense_case_609(self):
        self.assertEqual(pattern_match('iyffffff', 'iyf'), [0])

    def test_dense_case_610(self):
        self.assertEqual(pattern_match('cccccccccccccccccccccccc', 'c'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])

    def test_dense_case_611(self):
        self.assertEqual(pattern_match('pjypjypjypjypjypjypjypjypjypjypjypjypjypjypjypjypjypjypjypjypjypjypjypjypjypjypjy', 'pjy'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78])

    def test_dense_case_612(self):
        self.assertEqual(pattern_match('ppppppppppppppppppp', 'p'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

    def test_dense_case_613(self):
        self.assertEqual(pattern_match('tcntcntcntcntcntcntcntcntcntcntcntcntcntcntcntcntcntcntcntcn', 'tcn'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57])

    def test_dense_case_614(self):
        self.assertEqual(pattern_match('vjigjigjigjigjigjigjigjigjigjigjigjigjigjigjigjigjigjigjigjigjigjigjig', 'vjig'), [0])

    def test_dense_case_615(self):
        self.assertEqual(pattern_match('fdrpfdrpfdrpfdrpfdrpfdrpfdrpfdrpfdrpfdrpfdrpfdrpfdrpfdrpfdrp', 'fdrp'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56])

    def test_dense_case_616(self):
        self.assertEqual(pattern_match('nzskzskzskzskzskzskzskzsk', 'nzsk'), [0])

    def test_dense_case_617(self):
        self.assertEqual(pattern_match('joooooooooooooo', 'jo'), [0])

    def test_dense_case_618(self):
        self.assertEqual(pattern_match('stgnjtgnjtgnjtgnjtgnjtgnjtgnjtgnj', 'stgnj'), [0])

    def test_dense_case_619(self):
        self.assertEqual(pattern_match('wqdddddddddddddd', 'wqd'), [0])

    def test_dense_case_620(self):
        self.assertEqual(pattern_match('nxnxnxnxnxnxnxnxnxnxnxnxnxnxnxnxnxnxnxnxnxnxnxnxnxnxnxnx', 'nx'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54])

    def test_dense_case_621(self):
        self.assertEqual(pattern_match('ofofofofofofofofofofofofofof', 'of'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26])

    def test_dense_case_622(self):
        self.assertEqual(pattern_match('uqcicicicicicicici', 'uqci'), [0])

    def test_dense_case_623(self):
        self.assertEqual(pattern_match('jxpnbjxpnbjxpnbjxpnbjxpnbjxpnbjxpnbjxpnbjxpnbjxpnbjxpnbjxpnbjxpnbjxpnbjxpnbjxpnbjxpnbjxpnbjxpnbjxpnbjxpnbjxpnbjxpnbjxpnbjxpnbjxpnbjxpnbjxpnbjxpnbjxpnb', 'jxpnb'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145])

    def test_dense_case_624(self):
        self.assertEqual(pattern_match('icycycycycycycycycycycycycycycycy', 'icy'), [0])

    def test_dense_case_625(self):
        self.assertEqual(pattern_match('wskpqskpqskpqskpqskpqskpqskpqskpqskpqskpqskpqskpqskpq', 'wskpq'), [0])

    def test_dense_case_626(self):
        self.assertEqual(pattern_match('benkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk', 'benk'), [0])

    def test_dense_case_627(self):
        self.assertEqual(pattern_match('egggggggggggggg', 'eg'), [0])

    def test_dense_case_628(self):
        self.assertEqual(pattern_match('gdeogdeogdeogdeogdeogdeogdeogdeogdeogdeogdeogdeogdeogdeogdeogdeogdeogdeogdeogdeogdeogdeogdeogdeogdeogdeogdeogdeo', 'gdeo'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100, 104, 108])

    def test_dense_case_629(self):
        self.assertEqual(pattern_match('ffqfqfqfqfqfqfqfqfqfqfqfqfqfqfqfqfqfqfq', 'ffq'), [0])

    def test_dense_case_630(self):
        self.assertEqual(pattern_match('qzzhjzhjzhjzhjzhjzhjzhjzhjzhjzhjzhjzhjzhj', 'qzzhj'), [0])

    def test_dense_case_631(self):
        self.assertEqual(pattern_match('xtkpytkpytkpytkpytkpytkpytkpytkpytkpy', 'xtkpy'), [0])

    def test_dense_case_632(self):
        self.assertEqual(pattern_match('bbbbbbbbbbbbbbbb', 'b'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_dense_case_633(self):
        self.assertEqual(pattern_match('muuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu', 'muu'), [0])

    def test_dense_case_634(self):
        self.assertEqual(pattern_match('wgpgpgpgpgpgpgpgpgpgpgpgpgpgpgpgpgpgpgpgpgpgpgpgp', 'wgp'), [0])

    def test_dense_case_635(self):
        self.assertEqual(pattern_match('wsnfwsnfwsnfwsnfwsnfwsnfwsnfwsnfwsnfwsnfwsnfwsnfwsnfwsnfwsnfwsnfwsnfwsnfwsnfwsnfwsnf', 'wsnf'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80])

    def test_dense_case_636(self):
        self.assertEqual(pattern_match('oooooooooooooooooooooooooooo', 'o'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27])

    def test_dense_case_637(self):
        self.assertEqual(pattern_match('rkmmmmmm', 'rkm'), [0])

    def test_dense_case_638(self):
        self.assertEqual(pattern_match('anbfffffff', 'anbf'), [0])

    def test_dense_case_639(self):
        self.assertEqual(pattern_match('jrjrjrjrjrjrjrjrjrjrjrjrjrjrjrjrjrjrjrjrjrjrjrjrjr', 'jr'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48])

    def test_dense_case_640(self):
        self.assertEqual(pattern_match('wcgggggggggggggggggggggggggggg', 'wcg'), [0])

    def test_dense_case_641(self):
        self.assertEqual(pattern_match('yzhvivivivivivivivivivivivivivivivivi', 'yzhvi'), [0])

    def test_dense_case_642(self):
        self.assertEqual(pattern_match('whaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'wha'), [0])

    def test_dense_case_643(self):
        self.assertEqual(pattern_match('hoooooooooooooooooooooooooooooo', 'ho'), [0])

    def test_dense_case_644(self):
        self.assertEqual(pattern_match('ppppppppppppppp', 'p'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_dense_case_645(self):
        self.assertEqual(pattern_match('pbtttttttttttttttttttttttt', 'pbt'), [0])

    def test_dense_case_646(self):
        self.assertEqual(pattern_match('zzzzzzzzzzzzzzzzzz', 'z'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])

    def test_dense_case_647(self):
        self.assertEqual(pattern_match('eeeeeeeeeeeeeeeeeeeeeeeeeeeee', 'e'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28])

    def test_dense_case_648(self):
        self.assertEqual(pattern_match('hhhhhhhhhhhhhhhhhhhhhhhhhhh', 'h'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26])

    def test_dense_case_649(self):
        self.assertEqual(pattern_match('enjenjenjenjenjenjenjenjenjenjenjenjenjenjenjenjenjenjenjenjenjenjenjenjenjenj', 'enj'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75])

    def test_dense_case_650(self):
        self.assertEqual(pattern_match('oxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxox', 'ox'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34])

    def test_dense_case_651(self):
        self.assertEqual(pattern_match('iiiiiiiiiiiiiiiiiiiiiii', 'i'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])

    def test_dense_case_652(self):
        self.assertEqual(pattern_match('ksnksnksnksnksnksnksnksnksnksnksnksnksnksnksnksn', 'ksn'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45])

    def test_dense_case_653(self):
        self.assertEqual(pattern_match('tgccccccccccccccccccccccccccccc', 'tgc'), [0])

    def test_dense_case_654(self):
        self.assertEqual(pattern_match('eeeeeeeeeeee', 'e'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_dense_case_655(self):
        self.assertEqual(pattern_match('phaetaetaetaetaetaetaetaetaetaetaetaetaetaetaetaet', 'phaet'), [0])

    def test_dense_case_656(self):
        self.assertEqual(pattern_match('vrrrrrrr', 'vr'), [0])

    def test_dense_case_657(self):
        self.assertEqual(pattern_match('tbzydbzydbzydbzydbzydbzydbzydbzydbzydbzydbzydbzydbzydbzydbzydbzydbzydbzydbzydbzydbzydbzydbzydbzydbzydbzydbzydbzydbzyd', 'tbzyd'), [0])

    def test_dense_case_658(self):
        self.assertEqual(pattern_match('twwwwwwwwwww', 'tw'), [0])

    def test_dense_case_659(self):
        self.assertEqual(pattern_match('gggggggggggggggggggg', 'g'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_dense_case_660(self):
        self.assertEqual(pattern_match('yyyyyyyyyyyyyyyyyyyyyyyy', 'y'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])

    def test_dense_case_661(self):
        self.assertEqual(pattern_match('ffffffffffffffffffffffffffff', 'f'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27])

    def test_dense_case_662(self):
        self.assertEqual(pattern_match('nnnnnnnnnnnnnnnnnnnnnnnnnnn', 'n'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26])

    def test_dense_case_663(self):
        self.assertEqual(pattern_match('cehhhhhhhhhhhhhhhhhhhhhhhhhh', 'ceh'), [0])

    def test_dense_case_664(self):
        self.assertEqual(pattern_match('aoaoaoaoaoaoaoaoaoaoaoaoaoaoaoaoaoaoaoaoaoaoaoaoaoaoaoaoaoao', 'ao'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58])

    def test_dense_case_665(self):
        self.assertEqual(pattern_match('wtwtwtwtwtwtwtwtwtwtwt', 'wt'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

    def test_dense_case_666(self):
        self.assertEqual(pattern_match('sssssssssssssss', 's'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_dense_case_667(self):
        self.assertEqual(pattern_match('ocircircircircircircircircircircircircircircircircircircircircircircircircircircircir', 'ocir'), [0])

    def test_dense_case_668(self):
        self.assertEqual(pattern_match('fecnnnnnnnnnnnnnnnnnnnnnnnnnnnn', 'fecn'), [0])

    def test_dense_case_669(self):
        self.assertEqual(pattern_match('mhwhwhwhwhwhwhwhwhwhwhwhwhwhwhwhwhwhwhwhw', 'mhw'), [0])

    def test_dense_case_670(self):
        self.assertEqual(pattern_match('yturrurrurrurrurrurr', 'yturr'), [0])

    def test_dense_case_671(self):
        self.assertEqual(pattern_match('uuuuuuuuuuuuuuu', 'u'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_dense_case_672(self):
        self.assertEqual(pattern_match('dcfdcfdcfdcfdcfdcfdcfdcfdcfdcfdcfdcfdcfdcfdcfdcf', 'dcf'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45])

    def test_dense_case_673(self):
        self.assertEqual(pattern_match('gclvtclvtclvtclvtclvtclvtclvtclvtclvtclvtclvtclvtclvtclvtclvtclvtclvtclvtclvtclvtclvtclvtclvtclvt', 'gclvt'), [0])

    def test_dense_case_674(self):
        self.assertEqual(pattern_match('zttttttt', 'zt'), [0])

    def test_dense_case_675(self):
        self.assertEqual(pattern_match('biiiiiiiiiiiiiiiiiiiiiiiii', 'bi'), [0])

    def test_dense_case_676(self):
        self.assertEqual(pattern_match('jxmuuuuuuuuuuuuuuuuuuuuuuu', 'jxmu'), [0])

    def test_dense_case_677(self):
        self.assertEqual(pattern_match('aqbgggggggggggggggggggggggggggg', 'aqbg'), [0])

    def test_dense_case_678(self):
        self.assertEqual(pattern_match('iydxnxnxnxnxnxn', 'iydxn'), [0])

    def test_dense_case_679(self):
        self.assertEqual(pattern_match('irairairairairairairairairairairairairairairairairairaira', 'ira'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54])

    def test_dense_case_680(self):
        self.assertEqual(pattern_match('ihgihgihgihgihgihgihg', 'ihg'), [0, 3, 6, 9, 12, 15, 18])

    def test_dense_case_681(self):
        self.assertEqual(pattern_match('pfapfapfapfapfapfapfapfapfapfapfapfapfapfa', 'pfa'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39])

    def test_dense_case_682(self):
        self.assertEqual(pattern_match('cnopnopnopnopnopnopnopnop', 'cnop'), [0])

    def test_dense_case_683(self):
        self.assertEqual(pattern_match('nzbnzbnzbnzbnzbnzbnzbnzbnzb', 'nzb'), [0, 3, 6, 9, 12, 15, 18, 21, 24])

    def test_dense_case_684(self):
        self.assertEqual(pattern_match('hlhlhlhlhlhlhlhlhlhlhlhlhlhlhlhlhlhlhlhlhlhlhlhlhl', 'hl'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48])

    def test_dense_case_685(self):
        self.assertEqual(pattern_match('tocoltocoltocoltocoltocol', 'tocol'), [0, 5, 10, 15, 20])

    def test_dense_case_686(self):
        self.assertEqual(pattern_match('hivvvvvvvvvvvvvvvvvvvv', 'hiv'), [0])

    def test_dense_case_687(self):
        self.assertEqual(pattern_match('rvhvhvhvhvhvhvhvhvhvhvhvhvhvhvhvhvhvh', 'rvh'), [0])

    def test_dense_case_688(self):
        self.assertEqual(pattern_match('abszbszbszbszbszbszbszbszbszbszbszbszbszbszbszbszbszbszbszbszbszbsz', 'absz'), [0])

    def test_dense_case_689(self):
        self.assertEqual(pattern_match('gggggggggggggg', 'g'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_dense_case_690(self):
        self.assertEqual(pattern_match('skkkkk', 'sk'), [0])

    def test_dense_case_691(self):
        self.assertEqual(pattern_match('vvvvvvvvv', 'v'), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_dense_case_692(self):
        self.assertEqual(pattern_match('aeraeraeraeraeraeraeraeraeraeraeraeraeraeraeraeraeraeraeraeraeraeraeraeraeraeraeraer', 'aer'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81])

    def test_dense_case_693(self):
        self.assertEqual(pattern_match('dfxyfxyfxyfxyfxyfxyfxyfxyfxyfxyfxyfxy', 'dfxy'), [0])

    def test_dense_case_694(self):
        self.assertEqual(pattern_match('sqfqisqfqisqfqisqfqisqfqisqfqisqfqisqfqisqfqisqfqisqfqisqfqisqfqi', 'sqfqi'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])

    def test_dense_case_695(self):
        self.assertEqual(pattern_match('tttttttttt', 't'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_dense_case_696(self):
        self.assertEqual(pattern_match('uuuuuuuuuuuuuuuuuuuu', 'u'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_dense_case_697(self):
        self.assertEqual(pattern_match('kbntententententente', 'kbnte'), [0])

    def test_dense_case_698(self):
        self.assertEqual(pattern_match('kgkgkgkgkgkgkgkgkgkgkgkgkgkgkgkgkgkgkgkgkgkgkgkgkgkgkgkgkgkg', 'kg'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58])

    def test_dense_case_699(self):
        self.assertEqual(pattern_match('jhcmhcmhcmhcmhcmhcm', 'jhcm'), [0])

    def test_dense_case_700(self):
        self.assertEqual(pattern_match('eklekleklekleklekleklekleklekleklekleklekl', 'ekl'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39])

    def test_dense_case_701(self):
        self.assertEqual(pattern_match('nnnnnnnnnnn', 'n'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_dense_case_702(self):
        self.assertEqual(pattern_match('neiypppppppp', 'neiyp'), [0])

    def test_dense_case_703(self):
        self.assertEqual(pattern_match('wpqfsfsfsfsfsfsfsfsfsfsfsfsfsfs', 'wpqfs'), [0])

    def test_dense_case_704(self):
        self.assertEqual(pattern_match('xvquuuuuuuuuuuuuuuuuuuuuuuuuuu', 'xvqu'), [0])

    def test_dense_case_705(self):
        self.assertEqual(pattern_match('tdqnrtdqnrtdqnrtdqnrtdqnrtdqnrtdqnrtdqnrtdqnrtdqnrtdqnrtdqnrtdqnrtdqnrtdqnrtdqnrtdqnrtdqnr', 'tdqnr'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85])

    def test_dense_case_706(self):
        self.assertEqual(pattern_match('ffkcbffkcbffkcbffkcbffkcbffkcbffkcbffkcbffkcbffkcbffkcbffkcbffkcbffkcbffkcbffkcbffkcbffkcbffkcbffkcb', 'ffkcb'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95])

    def test_dense_case_707(self):
        self.assertEqual(pattern_match('wanmnmnmnmnmnmnmnmnmnmnmnmnmnmnmnmnmnmnmnmnm', 'wanm'), [0])

    def test_dense_case_708(self):
        self.assertEqual(pattern_match('tmviiviiviiviiviiviiviiviiviiviiviiviiviiviiviiviiviiviiviiviiviiviiviiviiviiviiviiviiviivii', 'tmvii'), [0])

    def test_dense_case_709(self):
        self.assertEqual(pattern_match('llnlnlnlnlnlnlnlnlnlnlnlnlnlnlnlnlnlnlnlnlnlnln', 'lln'), [0])

    def test_dense_case_710(self):
        self.assertEqual(pattern_match('asfysfysfysfysfysfysfysfysfysfysfysfysfysfysfysfysfysfysfysfysfysfysfysfysfy', 'asfy'), [0])

    def test_dense_case_711(self):
        self.assertEqual(pattern_match('qmqooooooooooooooooooooooooooo', 'qmqo'), [0])

    def test_dense_case_712(self):
        self.assertEqual(pattern_match('tmgvmgvmgvmgvmgvmgvmgvmgvmgvmgvmgvmgvmgvmgvmgvmgvmgvmgvmgvmgvmgvmgvmgvmgvmgvmgvmgvmgv', 'tmgv'), [0])

    def test_dense_case_713(self):
        self.assertEqual(pattern_match('kaeaeaeaeaeaeaeaeaeaeaeaeaeaeaeaeaeaeaeaeaeaeaeaeaeaeae', 'kae'), [0])

    def test_dense_case_714(self):
        self.assertEqual(pattern_match('qlllllllllllllllllllllll', 'ql'), [0])

    def test_dense_case_715(self):
        self.assertEqual(pattern_match('pmpmpmpmpmpmpmpmpmpmpmpmpmpmpmpmpmpmpmpmpmpmpmpmpmpmpmpmpmpm', 'pm'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58])

    def test_dense_case_716(self):
        self.assertEqual(pattern_match('nvcnvcnvcnvcnvcnvcnvcnvcnvcnvcnvcnvcnvcnvcnvcnvcnvcnvcnvcnvcnvcnvc', 'nvc'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63])

    def test_dense_case_717(self):
        self.assertEqual(pattern_match('tbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbt', 'tbt'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52])

    def test_dense_case_718(self):
        self.assertEqual(pattern_match('sovpsovpsovpsovpsovpsovpsovpsovpsovpsovpsovpsovpsovpsovpsovpsovpsovpsovp', 'sovp'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68])

    def test_dense_case_719(self):
        self.assertEqual(pattern_match('fffffff', 'f'), [0, 1, 2, 3, 4, 5, 6])

    def test_dense_case_720(self):
        self.assertEqual(pattern_match('mmmmmmmmmmmmmmmmmmmmmmmm', 'm'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])

    def test_dense_case_721(self):
        self.assertEqual(pattern_match('ypoypoypoypoypoypoypoypoypoypoypoypoypoypoypoypoypoypoypoypoypoypoypoypoypo', 'ypo'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72])

    def test_dense_case_722(self):
        self.assertEqual(pattern_match('fxiiiiiiiii', 'fxi'), [0])

    def test_dense_case_723(self):
        self.assertEqual(pattern_match('hhhhhhhh', 'h'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_dense_case_724(self):
        self.assertEqual(pattern_match('pnvkdnvkdnvkdnvkdnvkdnvkd', 'pnvkd'), [0])

    def test_dense_case_725(self):
        self.assertEqual(pattern_match('aaymaymaymaymaymaymaymaymaymaymaymaymaymaymaymaymaymaymaymaymaymaym', 'aaym'), [0])

    def test_dense_case_726(self):
        self.assertEqual(pattern_match('uuuuuuuuuuuuu', 'uu'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_dense_case_727(self):
        self.assertEqual(pattern_match('kkkkkkkkkkkkkkkkk', 'k'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    def test_dense_case_728(self):
        self.assertEqual(pattern_match('evevevevevevevevevevevevevevevevevevevevevevevev', 'ev'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46])

    def test_dense_case_729(self):
        self.assertEqual(pattern_match('looooooooooooooooo', 'lo'), [0])

    def test_dense_case_730(self):
        self.assertEqual(pattern_match('uwpppppppppppppppppppppppppppppp', 'uwpp'), [0])

    def test_dense_case_731(self):
        self.assertEqual(pattern_match('qdadadadadadadadadadadadadadadadadadadadadadadadadadadada', 'qda'), [0])

    def test_dense_case_732(self):
        self.assertEqual(pattern_match('ajxkfkfkfkfkfkfkfkfkfkfkfkfkfkfkfkfkf', 'ajxkf'), [0])

    def test_dense_case_733(self):
        self.assertEqual(pattern_match('eokokokokokokokokokokokokokokok', 'eok'), [0])

    def test_dense_case_734(self):
        self.assertEqual(pattern_match('nqsssssss', 'nqs'), [0])

    def test_dense_case_735(self):
        self.assertEqual(pattern_match('gobgobgobgobgobgobgobgobgobgobgobgobgobgobgobgobgobgobgobgobgobgobgobgobgobgobgob', 'gob'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78])

    def test_dense_case_736(self):
        self.assertEqual(pattern_match('andmcccccccccccccc', 'andmc'), [0])

    def test_dense_case_737(self):
        self.assertEqual(pattern_match('jjjjjjjjjjjjjjjjjjjjjjjjjj', 'j'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])

    def test_dense_case_738(self):
        self.assertEqual(pattern_match('vybgbbbbbbbbbbbbbbbbbb', 'vybgb'), [0])

    def test_dense_case_739(self):
        self.assertEqual(pattern_match('jbjjjjjjjjjjjjjjjjjjjjjjjjjjj', 'jbj'), [0])

    def test_dense_case_740(self):
        self.assertEqual(pattern_match('ulplplplplplplplplplp', 'ulp'), [0])

    def test_dense_case_741(self):
        self.assertEqual(pattern_match('ooooooooooooooooooooooooooo', 'o'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26])

    def test_dense_case_742(self):
        self.assertEqual(pattern_match('grgrgrgrgrgrgrgrgrgrgrgrgr', 'gr'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])

    def test_dense_case_743(self):
        self.assertEqual(pattern_match('gwqqqqqqqqq', 'gwq'), [0])

    def test_dense_case_744(self):
        self.assertEqual(pattern_match('rjjjjjjjjjj', 'rj'), [0])

    def test_dense_case_745(self):
        self.assertEqual(pattern_match('vyyyyyyyyyyyyyyyyyyy', 'vy'), [0])

    def test_dense_case_746(self):
        self.assertEqual(pattern_match('aaaaaaaaaaaaaaaa', 'a'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_dense_case_747(self):
        self.assertEqual(pattern_match('dypdypdypdypdypdypdypdypdypdypdypdypdypdypdyp', 'dyp'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42])

    def test_dense_case_748(self):
        self.assertEqual(pattern_match('blqwblqwblqwblqwblqw', 'blqw'), [0, 4, 8, 12, 16])

    def test_dense_case_749(self):
        self.assertEqual(pattern_match('hbhbhbhbhbhbhbhbhbhbhbhbhbhbhb', 'hb'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28])

    def test_dense_case_750(self):
        self.assertEqual(pattern_match('lyeazeazeazeazeazeazeazeazeazeazeazeazeazeazeazeazeaz', 'lyeaz'), [0])

    def test_dense_case_751(self):
        self.assertEqual(pattern_match('hbxxxxxxxxxxxxxxxxxxxxxx', 'hbx'), [0])

    def test_dense_case_752(self):
        self.assertEqual(pattern_match('yucyucyucyucyucyucyucyucyucyucyucyucyucyuc', 'yuc'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39])

    def test_dense_case_753(self):
        self.assertEqual(pattern_match('zzzzzzzzzzzzzzzzzz', 'z'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])

    def test_dense_case_754(self):
        self.assertEqual(pattern_match('arjrjrjrjrjrjrjrjrjrjrjrjrjrjrjrjrjrjrjrjrj', 'arj'), [0])

    def test_dense_case_755(self):
        self.assertEqual(pattern_match('hjidmmmmmmmmm', 'hjidm'), [0])

    def test_dense_case_756(self):
        self.assertEqual(pattern_match('eeeeeeeeeeeeeeeeeeeeeeeeeee', 'e'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26])

    def test_dense_case_757(self):
        self.assertEqual(pattern_match('nrexnrexnrexnrexnrexnrexnrexnrexnrexnrexnrexnrexnrexnrexnrexnrexnrexnrexnrexnrexnrexnrexnrexnrexnrexnrexnrexnrex', 'nrex'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100, 104, 108])

    def test_dense_case_758(self):
        self.assertEqual(pattern_match('lekixlekixlekixlekixlekixlekixlekixlekixlekixlekixlekixlekixlekixlekixlekix', 'lekix'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70])

    def test_dense_case_759(self):
        self.assertEqual(pattern_match('wwwwwwwwwww', 'w'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_dense_case_760(self):
        self.assertEqual(pattern_match('inlplplplplplplplplplplplplplplplplplplplp', 'inlp'), [0])

    def test_dense_case_761(self):
        self.assertEqual(pattern_match('yzpttttttttttt', 'yzpt'), [0])

    def test_dense_case_762(self):
        self.assertEqual(pattern_match('ivvvvvvvvv', 'iv'), [0])

    def test_dense_case_763(self):
        self.assertEqual(pattern_match('uiiiiiiiiiiiiiiiiiiiiiii', 'ui'), [0])

    def test_dense_case_764(self):
        self.assertEqual(pattern_match('ooooooooooooooooooooooooooooo', 'o'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28])

    def test_dense_case_765(self):
        self.assertEqual(pattern_match('pppppppp', 'p'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_dense_case_766(self):
        self.assertEqual(pattern_match('wmddmddmddmddmddmdd', 'wmdd'), [0])

    def test_dense_case_767(self):
        self.assertEqual(pattern_match('jjfffffffffffff', 'jjf'), [0])

    def test_dense_case_768(self):
        self.assertEqual(pattern_match('nvehvvvvvvvvvvvvvvvvvvv', 'nvehv'), [0])

    def test_dense_case_769(self):
        self.assertEqual(pattern_match('tpppppppppppppp', 'tp'), [0])

    def test_dense_case_770(self):
        self.assertEqual(pattern_match('xbsbsbsbsbsbsbsbsbsbsbsbsbsbsbsbsbsbsbsbsbsbsbsbsbsbsbsbsbsbs', 'xbs'), [0])

    def test_dense_case_771(self):
        self.assertEqual(pattern_match('javfvfvfvfvfvfvfvfvfvf', 'javf'), [0])

    def test_dense_case_772(self):
        self.assertEqual(pattern_match('bpcapcapcapcapcapcapcapcapcapcapcapcapcapcapcapca', 'bpca'), [0])

    def test_dense_case_773(self):
        self.assertEqual(pattern_match('ollqqqqqqqqqqqqqqqqqq', 'ollq'), [0])

    def test_dense_case_774(self):
        self.assertEqual(pattern_match('tsmtsmtsmtsmtsmtsm', 'tsm'), [0, 3, 6, 9, 12, 15])

    def test_dense_case_775(self):
        self.assertEqual(pattern_match('rbwzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz', 'rbwzz'), [0])

    def test_dense_case_776(self):
        self.assertEqual(pattern_match('bykdyykdyykdyykdyykdyykdyykdyykdyykdy', 'bykdy'), [0])

    def test_dense_case_777(self):
        self.assertEqual(pattern_match('zgozfzgozfzgozfzgozfzgozfzgozf', 'zgozf'), [0, 5, 10, 15, 20, 25])

    def test_dense_case_778(self):
        self.assertEqual(pattern_match('irggsirggsirggsirggsirggsirggsirggsirggsirggsirggsirggsirggsirggsirggsirggsirggsirggsirggsirggsirggsirggsirggsirggsirggsirggsirggsirggsirggsirggsirggs', 'irggs'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145])

    def test_dense_case_779(self):
        self.assertEqual(pattern_match('lzqahlzqahlzqahlzqahlzqahlzqahlzqahlzqahlzqahlzqahlzqahlzqahlzqahlzqahlzqah', 'lzqah'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70])

    def test_dense_case_780(self):
        self.assertEqual(pattern_match('sikbppppppppppppp', 'sikbp'), [0])

    def test_dense_case_781(self):
        self.assertEqual(pattern_match('sfaaaaa', 'sfa'), [0])

    def test_dense_case_782(self):
        self.assertEqual(pattern_match('qoooooooooooooooooooooooo', 'qo'), [0])

    def test_dense_case_783(self):
        self.assertEqual(pattern_match('zsqsqsqsqsqsqsqsqsqsqsqsqsqsqsqsq', 'zsq'), [0])

    def test_dense_case_784(self):
        self.assertEqual(pattern_match('mccccccccc', 'mc'), [0])

    def test_dense_case_785(self):
        self.assertEqual(pattern_match('orivlivlivlivlivlivlivlivlivlivlivlivlivlivlivlivlivlivlivl', 'orivl'), [0])

    def test_dense_case_786(self):
        self.assertEqual(pattern_match('ejejejejejej', 'ej'), [0, 2, 4, 6, 8, 10])

    def test_dense_case_787(self):
        self.assertEqual(pattern_match('wwwwwwwwwwwwwwwwwwwww', 'w'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

    def test_dense_case_788(self):
        self.assertEqual(pattern_match('aqufaqufaqufaqufaqufaqufaqufaqufaqufaqufaqufaqufaqufaquf', 'aquf'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52])

    def test_dense_case_789(self):
        self.assertEqual(pattern_match('thjxvvvvvvvvvvvvvvvv', 'thjxv'), [0])

    def test_dense_case_790(self):
        self.assertEqual(pattern_match('eybqcqcqcqcqcqcqcqcqcqcqcqcqcqcqcqcqcqcqcqcqc', 'eybqc'), [0])

    def test_dense_case_791(self):
        self.assertEqual(pattern_match('kdfkdfkdfkdfkdfkdfkdfkdfkdfkdfkdfkdfkdfkdf', 'kdf'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39])

    def test_dense_case_792(self):
        self.assertEqual(pattern_match('bwwwwwwwwwwwwwwwwwwwwwwwwwwwww', 'bw'), [0])

    def test_dense_case_793(self):
        self.assertEqual(pattern_match('plpqxlpqxlpqxlpqxlpqxlpqxlpqxlpqxlpqxlpqx', 'plpqx'), [0])

    def test_dense_case_794(self):
        self.assertEqual(pattern_match('mmmmmmmmm', 'm'), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_dense_case_795(self):
        self.assertEqual(pattern_match('agjgjgjgjgjgjgjgjgjgjgjgjgjgjgjgjgjgjgjgjgjgjg', 'agjg'), [0])

    def test_dense_case_796(self):
        self.assertEqual(pattern_match('fsdjcccccccc', 'fsdjc'), [0])

    def test_dense_case_797(self):
        self.assertEqual(pattern_match('kwkwkwkwkwkwkwkwkwkwkwkwkwkwkwkwkwkw', 'kw'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34])

    def test_dense_case_798(self):
        self.assertEqual(pattern_match('uwwwwwwwwwwwwwwwwwwwwwwwww', 'uw'), [0])

    def test_dense_case_799(self):
        self.assertEqual(pattern_match('lfeeeeeeeeeeeeeeeeeeeeeeeeeee', 'lfe'), [0])

    def test_dense_case_800(self):
        self.assertEqual(pattern_match('fyststststststststststststst', 'fyst'), [0])

    def test_dense_case_801(self):
        self.assertEqual(pattern_match('bgtqbgtqbgtqbgtqbgtqbgtqbgtqbgtqbgtqbgtqbgtqbgtqbgtqbgtqbgtqbgtqbgtqbgtqbgtqbgtqbgtqbgtqbgtqbgtqbgtq', 'bgtq'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96])

    def test_dense_case_802(self):
        self.assertEqual(pattern_match('yyyyyyyyyyyyyyyyyyyyyyyyyyyy', 'y'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27])

    def test_dense_case_803(self):
        self.assertEqual(pattern_match('hsotxhsotxhsotxhsotxhsotxhsotxhsotxhsotxhsotxhsotxhsotxhsotxhsotxhsotxhsotxhsotxhsotxhsotxhsotxhsotxhsotxhsotxhsotxhsotxhsotxhsotxhsotx', 'hsotx'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130])

    def test_dense_case_804(self):
        self.assertEqual(pattern_match('fnnnnnnnnnnnnnnnnnnnnnnnn', 'fn'), [0])

    def test_dense_case_805(self):
        self.assertEqual(pattern_match('kotlllllllllll', 'kotl'), [0])

    def test_dense_case_806(self):
        self.assertEqual(pattern_match('bbbbbbbbbb', 'b'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_dense_case_807(self):
        self.assertEqual(pattern_match('hydghydghydghydghydghydghydghydghydghydghydghydghydghydghydghydghydghydghydghydghydghydghydghydg', 'hydg'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92])

    def test_dense_case_808(self):
        self.assertEqual(pattern_match('yyyyyyyyyyyyyyyyyyyy', 'y'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_dense_case_809(self):
        self.assertEqual(pattern_match('rvgcjjjjjjjjj', 'rvgcj'), [0])

    def test_dense_case_810(self):
        self.assertEqual(pattern_match('xytuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu', 'xytuu'), [0])

    def test_dense_case_811(self):
        self.assertEqual(pattern_match('qipipipipipipipipipipipipipipipipipipipip', 'qip'), [0])

    def test_dense_case_812(self):
        self.assertEqual(pattern_match('ilbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb', 'ilbb'), [0])

    def test_dense_case_813(self):
        self.assertEqual(pattern_match('qtkbqtkbqtkbqtkbqtkbqtkbqtkbqtkbqtkbqtkbqtkbqtkbqtkbqtkbqtkbqtkbqtkbqtkbqtkbqtkbqtkbqtkbqtkbqtkbqtkbqtkbqtkbqtkb', 'qtkb'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100, 104, 108])

    def test_dense_case_814(self):
        self.assertEqual(pattern_match('mhhocococococococococococococococococococococococococococococ', 'mhhoc'), [0])

    def test_dense_case_815(self):
        self.assertEqual(pattern_match('jjjjjjjjjjjjjjjjjjjjjjjjjjj', 'j'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26])

    def test_dense_case_816(self):
        self.assertEqual(pattern_match('qqqqqqqqqqqqqqqqq', 'q'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    def test_dense_case_817(self):
        self.assertEqual(pattern_match('dbdbdbdbdbdbdbdbdbdbdbdbdbdb', 'db'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26])

    def test_dense_case_818(self):
        self.assertEqual(pattern_match('gqdbccccccccccccccccccc', 'gqdbc'), [0])

    def test_dense_case_819(self):
        self.assertEqual(pattern_match('jlwllllllll', 'jlwl'), [0])

    def test_dense_case_820(self):
        self.assertEqual(pattern_match('xxxxxxxxxxxxxxxxxxxxxxxxx', 'x'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])

    def test_dense_case_821(self):
        self.assertEqual(pattern_match('ojcjoojcjoojcjoojcjoojcjoojcjoojcjoojcjoojcjoojcjoojcjoojcjoojcjoojcjoojcjoojcjoojcjo', 'ojcjo'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80])

    def test_dense_case_822(self):
        self.assertEqual(pattern_match('noooooooooooooooooooooooo', 'no'), [0])

    def test_dense_case_823(self):
        self.assertEqual(pattern_match('uquququququququququququququq', 'uq'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26])

    def test_dense_case_824(self):
        self.assertEqual(pattern_match('xxxxxxxxxxxxxxxxx', 'xx'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_dense_case_825(self):
        self.assertEqual(pattern_match('uuuuuuuuuuuuuuu', 'u'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_dense_case_826(self):
        self.assertEqual(pattern_match('llllllllllll', 'l'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_dense_case_827(self):
        self.assertEqual(pattern_match('ttttttttttttttttt', 't'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    def test_dense_case_828(self):
        self.assertEqual(pattern_match('eooooooooooooooooooooooo', 'eo'), [0])

    def test_dense_case_829(self):
        self.assertEqual(pattern_match('dpwpwpwpwpwpwpwpwpwpwpwpwpwpwpwpwpwpwpwpwpwpw', 'dpw'), [0])

    def test_dense_case_830(self):
        self.assertEqual(pattern_match('dcdcdcdcdcdcdcdcdcdcdcdcdc', 'dc'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])

    def test_dense_case_831(self):
        self.assertEqual(pattern_match('halhhalhhalhhalhhalhhalhhalhhalhhalh', 'halh'), [0, 4, 8, 12, 16, 20, 24, 28, 32])

    def test_dense_case_832(self):
        self.assertEqual(pattern_match('ibbxbbbxbbbxbbbxbbbxbbbxbbbxbbbxbbbxb', 'ibbxb'), [0])

    def test_dense_case_833(self):
        self.assertEqual(pattern_match('kctxddddddddddddddddddddd', 'kctxd'), [0])

    def test_dense_case_834(self):
        self.assertEqual(pattern_match('ddttttttttttt', 'ddt'), [0])

    def test_dense_case_835(self):
        self.assertEqual(pattern_match('rrrrrrrrrrrrrrrrrrrr', 'r'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_dense_case_836(self):
        self.assertEqual(pattern_match('nrrrrrrrrrrrrrrrrrr', 'nr'), [0])

    def test_dense_case_837(self):
        self.assertEqual(pattern_match('ikukeukeukeukeukeukeukeukeukeukeukeuke', 'ikuke'), [0])

    def test_dense_case_838(self):
        self.assertEqual(pattern_match('anpanpanpanpanpanpanpanpanp', 'anp'), [0, 3, 6, 9, 12, 15, 18, 21, 24])

    def test_dense_case_839(self):
        self.assertEqual(pattern_match('gjygjygjygjygjygjygjygjygjygjygjygjygjygjygjygjygjygjygjygjygjygjygjy', 'gjy'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66])

    def test_dense_case_840(self):
        self.assertEqual(pattern_match('hnuhnuhnuhnuhnuhnuhnuhnu', 'hnu'), [0, 3, 6, 9, 12, 15, 18, 21])

    def test_dense_case_841(self):
        self.assertEqual(pattern_match('ejjjjjjjjjjjjjjjjjjjjjjjjjj', 'ej'), [0])

    def test_dense_case_842(self):
        self.assertEqual(pattern_match('jscscscscscscscscscscscscscscsc', 'jsc'), [0])

    def test_dense_case_843(self):
        self.assertEqual(pattern_match('qpcroqpcroqpcroqpcroqpcroqpcroqpcroqpcroqpcroqpcroqpcroqpcroqpcroqpcroqpcroqpcroqpcroqpcroqpcroqpcroqpcroqpcro', 'qpcro'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105])

    def test_dense_case_844(self):
        self.assertEqual(pattern_match('vivxvxvxvxvxvxvxvxvxvxvxvxvxvxvxvxvxvxvxvxvx', 'vivx'), [0])

    def test_dense_case_845(self):
        self.assertEqual(pattern_match('mdneldneldneldneldneldneldneldneldneldneldneldneldneldneldneldneldneldneldnel', 'mdnel'), [0])

    def test_dense_case_846(self):
        self.assertEqual(pattern_match('xxxxxxxxxxxxxxxxxxxxxxx', 'x'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])

    def test_dense_case_847(self):
        self.assertEqual(pattern_match('aaaaaaaaaaaaaaaaaaaaaaaa', 'a'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])

    def test_dense_case_848(self):
        self.assertEqual(pattern_match('iupuoupuoupuoupuoupuoupuoupuoupuoupuoupuoupuoupuoupuoupuoupuoupuoupuoupuoupuoupuo', 'iupuo'), [0])

    def test_dense_case_849(self):
        self.assertEqual(pattern_match('gkdgkdgkdgkdgkdgkdgkdgkdgkdgkdgkdgkdgkdgkdgkd', 'gkd'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42])

    def test_dense_case_850(self):
        self.assertEqual(pattern_match('nvavavavavava', 'nva'), [0])

    def test_dense_case_851(self):
        self.assertEqual(pattern_match('lwzmwzmwzmwzmwzmwzmwzmwzmwzmwzmwzmwzmwzmwzmwzmwzmwzmwzmwzmwzmwzmwzmwzm', 'lwzm'), [0])

    def test_dense_case_852(self):
        self.assertEqual(pattern_match('pwwwwwwwwwwwww', 'pw'), [0])

    def test_dense_case_853(self):
        self.assertEqual(pattern_match('oilhllhllhllhllhllhllhllhllhllhllhllhllhllhllhllhllhllhllhllhllhl', 'oilhl'), [0])

    def test_dense_case_854(self):
        self.assertEqual(pattern_match('gynenenenenenenenenenenenenenenenenene', 'gyne'), [0])

    def test_dense_case_855(self):
        self.assertEqual(pattern_match('ytytytytytytytytytytytytytytytytytytytytytytytytytyt', 'yt'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50])

    def test_dense_case_856(self):
        self.assertEqual(pattern_match('tdvnnnnnnnnnnnnnnnnnnnn', 'tdvn'), [0])

    def test_dense_case_857(self):
        self.assertEqual(pattern_match('tmvvvvvvvvvvvv', 'tmv'), [0])

    def test_dense_case_858(self):
        self.assertEqual(pattern_match('vvvvvvvvvvvvvvvvvvvv', 'v'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test_dense_case_859(self):
        self.assertEqual(pattern_match('prrrrrrr', 'pr'), [0])

    def test_dense_case_860(self):
        self.assertEqual(pattern_match('xvnhxvnhxvnhxvnhxvnhxvnhxvnhxvnh', 'xvnh'), [0, 4, 8, 12, 16, 20, 24, 28])

    def test_dense_case_861(self):
        self.assertEqual(pattern_match('obbbbbbbbbb', 'ob'), [0])

    def test_dense_case_862(self):
        self.assertEqual(pattern_match('thhhhhhhhhhh', 'th'), [0])

    def test_dense_case_863(self):
        self.assertEqual(pattern_match('fmmmmmmmmmmmmmmmmmmmmmmmmmmmmm', 'fm'), [0])

    def test_dense_case_864(self):
        self.assertEqual(pattern_match('knxnxnxnxnxnxnxnxnx', 'knx'), [0])

    def test_dense_case_865(self):
        self.assertEqual(pattern_match('thhhhhhhhhhhhhhhhhhhhhhh', 'th'), [0])

    def test_dense_case_866(self):
        self.assertEqual(pattern_match('chchchchchchchchchchchchchchchchchchchchchchch', 'ch'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44])

    def test_dense_case_867(self):
        self.assertEqual(pattern_match('mmmmmmmm', 'm'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_dense_case_868(self):
        self.assertEqual(pattern_match('xfmccccccccccccccccccccccccc', 'xfmc'), [0])

    def test_dense_case_869(self):
        self.assertEqual(pattern_match('cwcwcwcwcwcwcwcwcwcwcwcwcwcwcwcwcwcwcwcwcwcwcwcwcwcwcw', 'cw'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52])

    def test_dense_case_870(self):
        self.assertEqual(pattern_match('aaaaa', 'a'), [0, 1, 2, 3, 4])

    def test_dense_case_871(self):
        self.assertEqual(pattern_match('pweeeeeeeeeeee', 'pwe'), [0])

    def test_dense_case_872(self):
        self.assertEqual(pattern_match('hqqqqqqqqqqqqqqqqqqq', 'hq'), [0])

    def test_dense_case_873(self):
        self.assertEqual(pattern_match('pppppppppppppppppppppppppppppp', 'pp'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28])

    def test_dense_case_874(self):
        self.assertEqual(pattern_match('amamamamamam', 'am'), [0, 2, 4, 6, 8, 10])

    def test_dense_case_875(self):
        self.assertEqual(pattern_match('nevevevevevevevevev', 'nev'), [0])

    def test_dense_case_876(self):
        self.assertEqual(pattern_match('ozwozwozwozwozwozwozwozwozwozwozwozwozwozwozwozwozwozw', 'ozw'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51])

    def test_dense_case_877(self):
        self.assertEqual(pattern_match('bbbbbbbbbbbbbbbbbbbbbbbbb', 'b'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])

    def test_dense_case_878(self):
        self.assertEqual(pattern_match('qgccccccccccc', 'qgc'), [0])

    def test_dense_case_879(self):
        self.assertEqual(pattern_match('kkkkkkkk', 'k'), [0, 1, 2, 3, 4, 5, 6, 7])

    def test_dense_case_880(self):
        self.assertEqual(pattern_match('ekgggggggggggggggggggggggggggg', 'ekg'), [0])

    def test_dense_case_881(self):
        self.assertEqual(pattern_match('kgnggnggnggnggnggnggnggnggnggnggnggnggnggnggnggnggnggnggng', 'kgng'), [0])

    def test_dense_case_882(self):
        self.assertEqual(pattern_match('mmmmm', 'm'), [0, 1, 2, 3, 4])

    def test_dense_case_883(self):
        self.assertEqual(pattern_match('oxnxpxpxpxpxpxpxpxpxpxpxpxpxpxpxpxp', 'oxnxp'), [0])

    def test_dense_case_884(self):
        self.assertEqual(pattern_match('czzzzzzzzzzzzzzzzzzzzzzzzzzzzz', 'cz'), [0])

    def test_dense_case_885(self):
        self.assertEqual(pattern_match('irycuirycuirycuirycuirycuirycuirycuirycuirycuirycuirycuirycuirycuirycuirycuirycuirycuirycuirycuirycuirycu', 'irycu'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])

    def test_dense_case_886(self):
        self.assertEqual(pattern_match('uiahwahwahwahwahwahwahwahwahwahwahwahwahwahwahwahwahwahwahwahwahwahwahwahwahw', 'uiahw'), [0])

    def test_dense_case_887(self):
        self.assertEqual(pattern_match('qgfmqgfmqgfmqgfmqgfmqgfmqgfmqgfmqgfmqgfmqgfmqgfmqgfmqgfmqgfmqgfmqgfmqgfmqgfm', 'qgfm'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72])

    def test_dense_case_888(self):
        self.assertEqual(pattern_match('zzyzzyzzyzzyzzyzzyzzyzzyzzyzzyzzyzzyzzyzzyzzyzzyzzyzzyzzyzzyzzyzzyzzyzzyzzyzzyzzyzzyzzy', 'zzy'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84])

    def test_dense_case_889(self):
        self.assertEqual(pattern_match('qkqkqkqkqkqkqkqkqkqkqkqkqkqkqkqkqkqkqkqkqkqkqkqkqkqkqkqkqkqk', 'qk'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58])

    def test_dense_case_890(self):
        self.assertEqual(pattern_match('hrrhrrhrrhrrhrrhrrhrrhrrhrrhrrhrrhrrhrrhrrhrrhrrhrrhrrhrrhrrhrrhrrhrrhrrhrrhrrhrrhrrhrr', 'hrr'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84])

    def test_dense_case_891(self):
        self.assertEqual(pattern_match('hnonononononononononononononononononononono', 'hno'), [0])

    def test_dense_case_892(self):
        self.assertEqual(pattern_match('sssssssssssssssssssssssss', 's'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])

    def test_dense_case_893(self):
        self.assertEqual(pattern_match('hhhhhhhhhhhhhhhhhhhhhhhhhhhh', 'h'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27])

    def test_dense_case_894(self):
        self.assertEqual(pattern_match('nnnnnnnnnnnnn', 'n'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_dense_case_895(self):
        self.assertEqual(pattern_match('jssssssssssssssssssssssssss', 'js'), [0])

    def test_dense_case_896(self):
        self.assertEqual(pattern_match('bwouuuuuuuuuuuuuu', 'bwouu'), [0])

    def test_dense_case_897(self):
        self.assertEqual(pattern_match('tejhjjjjjjjjjjjjjjjjjjjjjjjj', 'tejhj'), [0])

    def test_dense_case_898(self):
        self.assertEqual(pattern_match('eeeeeeeeeeeeeeee', 'e'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_dense_case_899(self):
        self.assertEqual(pattern_match('limlimlimlimlimlimlimlimlimlimlimlimlimlimlimlimlimlim', 'lim'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51])

    def test_dense_case_900(self):
        self.assertEqual(pattern_match('bpnnbpnnbpnnbpnnbpnnbpnnbpnnbpnnbpnnbpnnbpnnbpnnbpnnbpnnbpnnbpnnbpnnbpnnbpnnbpnnbpnnbpnnbpnnbpnnbpnnbpnn', 'bpnn'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100])

    def test_dense_case_901(self):
        self.assertEqual(pattern_match('hrrrrrrrr', 'hr'), [0])

    def test_dense_case_902(self):
        self.assertEqual(pattern_match('fwwwwwwwwwwwwwwwww', 'fw'), [0])

    def test_dense_case_903(self):
        self.assertEqual(pattern_match('cjcjcjcjcjcjcjcjcjcjcjcjcjcjcjcj', 'cj'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])

    def test_dense_case_904(self):
        self.assertEqual(pattern_match('ovvjxvjxvjxvjxvjxvjxvjxvjxvjxvjx', 'ovvjx'), [0])

    def test_dense_case_905(self):
        self.assertEqual(pattern_match('pppppppppppppppp', 'p'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_dense_case_906(self):
        self.assertEqual(pattern_match('wzwzwzwzwzwzwzwzwzwzwzwzwzwzwzwzwzwzwzwzwzwzwzwzwzwz', 'wz'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50])

    def test_dense_case_907(self):
        self.assertEqual(pattern_match('ryjkijkijkijkijkijkijkijkijkijkijkijkijkijkijkijkijkijkijki', 'ryjki'), [0])

    def test_dense_case_908(self):
        self.assertEqual(pattern_match('npgbqqqqqqqqqqqqqqqqq', 'npgbq'), [0])

    def test_dense_case_909(self):
        self.assertEqual(pattern_match('tmipopopopopopopopopopopopopopopopopopopopopopopopo', 'tmipo'), [0])

    def test_dense_case_910(self):
        self.assertEqual(pattern_match('qyyyyyyyyyyyyyyyyyyyyyyyyyyy', 'qy'), [0])

    def test_dense_case_911(self):
        self.assertEqual(pattern_match('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz', 'zzz'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48])

    def test_dense_case_912(self):
        self.assertEqual(pattern_match('bwlmmmmmmmmmmmmmmmmmmmmmmm', 'bwlm'), [0])

    def test_dense_case_913(self):
        self.assertEqual(pattern_match('pcttttttttttttttttttt', 'pct'), [0])

    def test_dense_case_914(self):
        self.assertEqual(pattern_match('qxpvvvvvvvvvvvvvvvvvvvvvvvvv', 'qxpv'), [0])

    def test_dense_case_915(self):
        self.assertEqual(pattern_match('rrrrrrrrrrrrrrrrrrrrrrrrrrrr', 'r'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27])

    def test_dense_case_916(self):
        self.assertEqual(pattern_match('eeeeeeeeeeeeee', 'e'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_dense_case_917(self):
        self.assertEqual(pattern_match('obooooooooooooooooo', 'obo'), [0])

    def test_dense_case_918(self):
        self.assertEqual(pattern_match('kuynekuynekuynekuynekuynekuynekuynekuynekuynekuynekuynekuynekuynekuynekuynekuynekuynekuynekuynekuynekuynekuynekuynekuynekuynekuynekuynekuyne', 'kuyne'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135])

    def test_dense_case_919(self):
        self.assertEqual(pattern_match('iiiiiiiiiiiiii', 'i'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_dense_case_920(self):
        self.assertEqual(pattern_match('hosiiiiiiiiii', 'hosi'), [0])

    def test_dense_case_921(self):
        self.assertEqual(pattern_match('exexexexexexexexexexex', 'ex'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

    def test_dense_case_922(self):
        self.assertEqual(pattern_match('goiqqqqqqqqqqqqqqqqqqqqqqq', 'goiq'), [0])

    def test_dense_case_923(self):
        self.assertEqual(pattern_match('hxhxhxhxhx', 'hx'), [0, 2, 4, 6, 8])

    def test_dense_case_924(self):
        self.assertEqual(pattern_match('iiiiiiiiiiiiiiiiiiiiiiiiiiii', 'i'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27])

    def test_dense_case_925(self):
        self.assertEqual(pattern_match('rjlrhhhhhhhhhhhhhhhhhhhhhhhhhhhh', 'rjlrh'), [0])

    def test_dense_case_926(self):
        self.assertEqual(pattern_match('znxxxxxxxxxx', 'znx'), [0])

    def test_dense_case_927(self):
        self.assertEqual(pattern_match('dhscoscoscoscoscoscoscoscosco', 'dhsco'), [0])

    def test_dense_case_928(self):
        self.assertEqual(pattern_match('zuigzuigzuigzuigzuigzuigz', 'zuigz'), [0, 4, 8, 12, 16, 20])

    def test_dense_case_929(self):
        self.assertEqual(pattern_match('txswswswswswswswswswswswswswswswswswswswswswswswswswswswswsw', 'txsw'), [0])

    def test_dense_case_930(self):
        self.assertEqual(pattern_match('ppnkrppnkrppnkrppnkrppnkrppnkrppnkrppnkrppnkrppnkrppnkrppnkrppnkrppnkrppnkrppnkrppnkrppnkrppnkrppnkrppnkrppnkrppnkrppnkr', 'ppnkr'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115])

    def test_dense_case_931(self):
        self.assertEqual(pattern_match('eimcimcimcimcimcimcimcimcimcimcimcimc', 'eimc'), [0])

    def test_dense_case_932(self):
        self.assertEqual(pattern_match('wfyyyyyyyyyyyy', 'wfy'), [0])

    def test_dense_case_933(self):
        self.assertEqual(pattern_match('ffgfgfgfgfgfgfgfgfgfgfgfgfgfgfgfgfgfgfgfgfgfgfgfgfgfgfgfg', 'ffg'), [0])

    def test_dense_case_934(self):
        self.assertEqual(pattern_match('sisisisisisisisisisisisisisi', 'si'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26])

    def test_dense_case_935(self):
        self.assertEqual(pattern_match('bkjabkjabkjabkjabkjabkjabkjabkjabkjabkjabkjabkja', 'bkja'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44])

    def test_dense_case_936(self):
        self.assertEqual(pattern_match('vvvvvvvvvvvvvvvvvvvvvvvvvv', 'v'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])

    def test_dense_case_937(self):
        self.assertEqual(pattern_match('zdvtqqqqq', 'zdvtq'), [0])

    def test_dense_case_938(self):
        self.assertEqual(pattern_match('jhsahsahsahsahsahsahsahsahsahsahsahsahsahsahsahsahsahsahsahsahsahsahsahsahsahsahsahsahsahsa', 'jhsa'), [0])

    def test_dense_case_939(self):
        self.assertEqual(pattern_match('knnnnnnnnnnnnnnnnnn', 'kn'), [0])

    def test_dense_case_940(self):
        self.assertEqual(pattern_match('nurqurqurqurqurqurqurqurqurqurqurqurqurqurqurqurqurqurqurqurqurqurqurqurqurqurq', 'nurq'), [0])

    def test_dense_case_941(self):
        self.assertEqual(pattern_match('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 'xx'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54])

    def test_dense_case_942(self):
        self.assertEqual(pattern_match('nvbvbvbvbvbvbvbvbvbvbvbvbvbvbvbvbvbvbvbvbvbvbvb', 'nvb'), [0])

    def test_dense_case_943(self):
        self.assertEqual(pattern_match('adaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaadaada', 'ada'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78])

    def test_dense_case_944(self):
        self.assertEqual(pattern_match('bzzzzzzzzzzzzzzzzzzzz', 'bz'), [0])

    def test_dense_case_945(self):
        self.assertEqual(pattern_match('lkvlkvlkvlkvlkvlkvlkvlkvlkvlkvlkvlkvlkvlkvlkv', 'lkv'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42])

    def test_dense_case_946(self):
        self.assertEqual(pattern_match('kpkpkpkpkpkpkpkpkpkp', 'kp'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])

    def test_dense_case_947(self):
        self.assertEqual(pattern_match('mtnnnnnnnnnnnnnnnnnnnnn', 'mtn'), [0])

    def test_dense_case_948(self):
        self.assertEqual(pattern_match('qxxxxxxxxxxxxxxxxxxxx', 'qx'), [0])

    def test_dense_case_949(self):
        self.assertEqual(pattern_match('bnbnbnbnbnbnbnbnbnbnbnbnbnbnbnbnbn', 'bn'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32])

    def test_dense_case_950(self):
        self.assertEqual(pattern_match('oooooooooooooooooooooo', 'o'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])

    def test_dense_case_951(self):
        self.assertEqual(pattern_match('qzqzqzqzqzqzqzqzqzqzqzqzqzqzqzqzqzqzqzqz', 'qz'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38])

    def test_dense_case_952(self):
        self.assertEqual(pattern_match('ccccccccccccccccccccccc', 'c'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])

    def test_dense_case_953(self):
        self.assertEqual(pattern_match('wwwwwwwwwwwwwwwwwwwwwwwww', 'w'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])

    def test_dense_case_954(self):
        self.assertEqual(pattern_match('mhyyyyyyyyyyyyyyyyyyyyyy', 'mhy'), [0])

    def test_dense_case_955(self):
        self.assertEqual(pattern_match('lavlavlavlavlavlavlavlav', 'lav'), [0, 3, 6, 9, 12, 15, 18, 21])

    def test_dense_case_956(self):
        self.assertEqual(pattern_match('llllllllllllllllllllll', 'l'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])

    def test_dense_case_957(self):
        self.assertEqual(pattern_match('aaaaaaaaaa', 'a'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_dense_case_958(self):
        self.assertEqual(pattern_match('tttttttttttttttttttttttttttt', 't'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27])

    def test_dense_case_959(self):
        self.assertEqual(pattern_match('klzjzjzjzjzjzjzjzjzjzjzjzjzjzj', 'klzj'), [0])

    def test_dense_case_960(self):
        self.assertEqual(pattern_match('xyybyybyybyybyybyybyybyybyybyybyybyybyybyybyybyybyybyybyybyybyybyybyybyybyybyybyybyybyyb', 'xyyb'), [0])

    def test_dense_case_961(self):
        self.assertEqual(pattern_match('diddddddddddddddddddddddd', 'did'), [0])

    def test_dense_case_962(self):
        self.assertEqual(pattern_match('txtxtxtxtxtxtxtxtx', 'tx'), [0, 2, 4, 6, 8, 10, 12, 14, 16])

    def test_dense_case_963(self):
        self.assertEqual(pattern_match('lllllllllllll', 'l'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    def test_dense_case_964(self):
        self.assertEqual(pattern_match('nisnisnisnisnisnisnisnisnisnis', 'nis'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27])

    def test_dense_case_965(self):
        self.assertEqual(pattern_match('nczmqqqqqqqqqqqqqqqqqqqqqq', 'nczmq'), [0])

    def test_dense_case_966(self):
        self.assertEqual(pattern_match('orrururururururururururururururururu', 'orru'), [0])

    def test_dense_case_967(self):
        self.assertEqual(pattern_match('lydqssssssssssssssssssssssss', 'lydqs'), [0])

    def test_dense_case_968(self):
        self.assertEqual(pattern_match('yyyyyyyyyyyyyyy', 'y'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_dense_case_969(self):
        self.assertEqual(pattern_match('tgtgtgtgtgtgtgtgtgtgtgtgtgtgtgtgtgtg', 'tg'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34])

    def test_dense_case_970(self):
        self.assertEqual(pattern_match('enqrnqrnqrnqrnqrnqrnqrnqrnqrnqrnqrnqrnqrnqrnqrnqrnqrnqrnqrnqrnqrnqrnqrnqrnqrnqrnqr', 'enqr'), [0])

    def test_dense_case_971(self):
        self.assertEqual(pattern_match('jldsldsldsldsldslds', 'jlds'), [0])

    def test_dense_case_972(self):
        self.assertEqual(pattern_match('tzwbtzwbtzwbtzwbtzwbtzwbtzwbtzwbtzwbtzwbtzwbtzwbtzwbtzwbtzwbtzwbtzwb', 'tzwb'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64])

    def test_dense_case_973(self):
        self.assertEqual(pattern_match('znznznznznznznznznznznznznznznznznznznznznznznznznznznznzn', 'zn'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56])

    def test_dense_case_974(self):
        self.assertEqual(pattern_match('pdhhhhhhhhhhhhhh', 'pdhh'), [0])

    def test_dense_case_975(self):
        self.assertEqual(pattern_match('rnclvrnclvrnclvrnclvrnclvrnclvrnclvrnclvrnclvrnclvrnclvrnclvrnclvrnclvrnclvrnclvrnclvrnclvrnclvrnclv', 'rnclv'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95])

    def test_dense_case_976(self):
        self.assertEqual(pattern_match('qnqnqnqnqnqnqnqnqnqnqnqnqnqnqnqnqnqnqnqnqnqnqnqn', 'qn'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46])

    def test_dense_case_977(self):
        self.assertEqual(pattern_match('ixtatatatatatatatatatatatatatatatatatatatata', 'ixta'), [0])

    def test_dense_case_978(self):
        self.assertEqual(pattern_match('fryryryryryryryryryryryryryryryryryryryryryryryryryryryryryry', 'fry'), [0])

    def test_dense_case_979(self):
        self.assertEqual(pattern_match('awglllll', 'awgl'), [0])

    def test_dense_case_980(self):
        self.assertEqual(pattern_match('scccccccccccccccccccccc', 'sc'), [0])

    def test_dense_case_981(self):
        self.assertEqual(pattern_match('tsssssssssssssss', 'ts'), [0])

    def test_dense_case_982(self):
        self.assertEqual(pattern_match('nacipipipipipipipipipipipipipipipipipipipipipipipipipipipipip', 'nacip'), [0])

    def test_dense_case_983(self):
        self.assertEqual(pattern_match('bhfeyfeyfeyfeyfeyfeyfeyfeyfeyfeyfeyfeyfeyfeyfeyfeyfeyfey', 'bhfey'), [0])

    def test_dense_case_984(self):
        self.assertEqual(pattern_match('xwjwlwlwlwlwlwlwlwlwlwlwlwlwlwlwlwlwlwlwlwlwlwlwlwl', 'xwjwl'), [0])

    def test_dense_case_985(self):
        self.assertEqual(pattern_match('gqwkkkkkkkkkkkkkkkkkkkkkkkkkkkkk', 'gqwk'), [0])

    def test_dense_case_986(self):
        self.assertEqual(pattern_match('rqqqqqqqqqqqqqqqq', 'rq'), [0])

    def test_dense_case_987(self):
        self.assertEqual(pattern_match('ewwewwewwewwewwewwewwewwewwewweww', 'eww'), [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30])

    def test_dense_case_988(self):
        self.assertEqual(pattern_match('fffffffffffffffffffffffffffff', 'f'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28])

    def test_dense_case_989(self):
        self.assertEqual(pattern_match('ksssssss', 'ks'), [0])

    def test_dense_case_990(self):
        self.assertEqual(pattern_match('ciiiiiiiiiiiiiiiii', 'ci'), [0])

    def test_dense_case_991(self):
        self.assertEqual(pattern_match('cnunnunnunnunnunnunnunnunnunnunnunnunnunnunnunnunnunnun', 'cnun'), [0])

    def test_dense_case_992(self):
        self.assertEqual(pattern_match('pejlfpejlfpejlfpejlfpejlfpejlfpejlfpejlfpejlfpejlfpejlfpejlfpejlf', 'pejlf'), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])

    def test_dense_case_993(self):
        self.assertEqual(pattern_match('zesbzesbzesbzesbzesbzesbzesbzesbzesbzesbzesbzesb', 'zesb'), [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44])

    def test_dense_case_994(self):
        self.assertEqual(pattern_match('kyktzzzzzzzzzzzzzzzzzz', 'kyktz'), [0])

    def test_dense_case_995(self):
        self.assertEqual(pattern_match('sssssssssssssssssssssssssss', 's'), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26])

    def test_dense_case_996(self):
        self.assertEqual(pattern_match('slslslslslslslslslslslslsl', 'sl'), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])

    def test_dense_case_997(self):
        self.assertEqual(pattern_match('hzhzhzhzhzhz', 'hz'), [0, 2, 4, 6, 8, 10])

    def test_dense_case_998(self):
        self.assertEqual(pattern_match('ewkwkwkwkwkwkwkwkwkwkwkwkwkwkwkwk', 'ewk'), [0])

    def test_dense_case_999(self):
        self.assertEqual(pattern_match('axofffffff', 'axof'), [0])


if __name__ == '__main__':
    unittest.main()
