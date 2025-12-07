import unittest
from dl_distance import near_exact_pattern_matching as near_exact_pattern_matching
# from naive_dl_algorithm import validated_dl_matches as near_exact_pattern_matching

class TestCorrectedDLMatches(unittest.TestCase):
    def test_case_0(self):
        text = 'hblejflhblejxidryhblejkczwhbleejwyvvhhblqjkkv'
        pattern = 'hblej'
        expected = [1, 2, 7, 8, 9, 17, 18, 19, 27, 38]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_1(self):
        text = 'npwsmsjwfqggpwsmsfhourgpwsmssagpwsmsjgazgpwsmstjygpwsmsqfn'
        pattern = 'gpwsms'
        expected = [1, 2, 11, 12, 13, 22, 23, 24, 30, 31, 32, 40, 41, 42, 49, 50, 51]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_2(self):
        text = 'wcqazgnvbawjcqmzgnsvswmjcqazgnddgwjcwazgnmfcwjcqahzgnuuabawjcqazagnqpga'
        pattern = 'wjcqazgn'
        expected = [1, 11, 22, 23, 24, 34, 45, 59]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_3(self):
        text = 'jrwcakqlkvmjrwcakwlasofjqrwcakwlbiofwjrwcakwiruz'
        pattern = 'jrwcakwl'
        expected = [1, 11, 12, 13, 24, 25, 26, 38]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_4(self):
        text = 'lytxdfrrlytrxdfmayzxlytxdfiflytxdfzsliytxdfldxo'
        pattern = 'lytxdf'
        expected = [1, 2, 9, 20, 21, 22, 28, 29, 30, 37, 38, 39]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_5(self):
        text = 'ovumibzywuovumfibzygfallovumibxyhxbylovusibzyqavovumibzyfphovumibzyvyj'
        pattern = 'ovumibzy'
        expected = [1, 2, 11, 25, 38, 48, 49, 50, 59, 60, 61]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_6(self):
        text = 'apmujxoprszuwapugxoprjubapujxoprzkapuljxoprytly'
        pattern = 'apujxopr'
        expected = [1, 14, 24, 25, 26, 35]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_7(self):
        text = 'oovkhiokoovkhiaijefdoovkhiieoovkhiwggdoovshiwoaoovkhiahyehogovkhiivr'
        pattern = 'oovkhi'
        expected = [1, 2, 8, 9, 10, 20, 21, 22, 28, 29, 30, 39, 47, 48, 49, 59, 60, 61]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_8(self):
        text = 'vssydrjdhvssydsrwycjssydgywevssydtzpavssydncb'
        pattern = 'vssyd'
        expected = [1, 2, 9, 10, 11, 20, 21, 28, 29, 30, 37, 38, 39]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_9(self):
        text = 'yuhqebzqsuhqueebjdysuhqebuytasuhqefbe'
        pattern = 'suhqe'
        expected = [1, 2, 9, 19, 20, 21, 29, 30, 31]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_10(self):
        text = 'eyclssszsxegjyclsssuipehclsssplpehieyclsssltvdeyclmsswvkeyclsqsseo'
        pattern = 'eyclsss'
        expected = [1, 2, 13, 14, 23, 35, 36, 37, 47, 57]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_11(self):
        text = 'oupxdyjbiroupcdypnxfouppdykcczoupddyrkqdoupdynxa'
        pattern = 'oupdy'
        expected = [1, 11, 21, 31, 40, 41, 42]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_12(self):
        text = 'ossnixnarpvossnixwafmhhossnixwnazlnnsssnixnadrdfossnixqnadvybjosksnixnaku'
        pattern = 'ossnixna'
        expected = [1, 2, 12, 24, 37, 38, 49, 63]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_13(self):
        text = 'zsnoulhzjsnoudkaqszrnousvmsnoupddzsnouawjzsnoujuj'
        pattern = 'zsnou'
        expected = [1, 2, 8, 9, 10, 19, 26, 27, 33, 34, 35, 41, 42, 43]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_14(self):
        text = 'fpgcqrnrtfpgzqrnthgfpgcgqrnvzdfpgcqrjzwfpgkqrnojeqfpgcqrnqjhdfpgcqrndmc'
        pattern = 'fpgcqrn'
        expected = [1, 2, 10, 20, 31, 40, 50, 51, 52, 61, 62, 63]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_15(self):
        text = 'wxbgruepwzwxmgrusmsawxmgruqwtwxmgrpozzuaxmgrukbwxmgruhduwxmgruygl'
        pattern = 'wxmgru'
        expected = [1, 10, 11, 12, 20, 21, 22, 30, 40, 41, 47, 48, 49, 56, 57, 58]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_16(self):
        text = 'ccvcgtgidfccvcgdgnuoccvagtgjjgxccvcgtompescjcvcgtgth'
        pattern = 'ccvcgtg'
        expected = [1, 2, 11, 21, 32, 43, 44, 45]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_17(self):
        text = 'unthxquxthjkdqunthvznunthsirt'
        pattern = 'unth'
        expected = [1, 2, 7, 14, 15, 16, 21, 22, 23]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_18(self):
        text = 'phlmbrbrprohlmbrodqphzmbryhxopylmbrjufpulmbrqbphlcbrfb'
        pattern = 'phlmbr'
        expected = [1, 2, 11, 12, 20, 30, 39, 47]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_19(self):
        text = 'bztqmsodqbztqueszbztqmxgtayztqmfgbztqmle'
        pattern = 'bztqm'
        expected = [1, 2, 10, 17, 18, 19, 27, 28, 33, 34, 35]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_20(self):
        text = 'mufqukzibqrubfqukzifuxjzbufqukzicxtbbufqukzixybufqunzizclbufqukzlqbwbnfqukzimur'
        pattern = 'bufqukzi'
        expected = [1, 2, 12, 13, 24, 25, 26, 36, 37, 38, 47, 58, 69]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_21(self):
        text = 'hmimmaglcmimmamghgyjpmiwmagvbnrmimmagoywkdmimmagitfaw'
        pattern = 'mimmag'
        expected = [1, 2, 3, 10, 22, 31, 32, 33, 42, 43, 44]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_22(self):
        text = 'wkqvcxkffgxwkqvpcxkrviwkqvcqxkzyfbwpqvcxkiew'
        pattern = 'wkqvcxk'
        expected = [1, 2, 12, 23, 35]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_23(self):
        text = 'cunznkgzqjufcfnznkgzyycnznkgzffnccnznklzxocnznkgzcfyn'
        pattern = 'cnznkgz'
        expected = [1, 2, 3, 13, 14, 15, 22, 23, 24, 34, 42, 43, 44]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_24(self):
        text = 'wnlpsyixjnpsweblwnprnawnpsxkownvsjuxrgwsnpshousiwnpsutrrk'
        pattern = 'wnps'
        expected = [1, 9, 10, 17, 22, 23, 24, 30, 39, 40, 41, 48, 49, 50]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_25(self):
        text = 'tspotodtvtsyotcdbfetsyotoodqabtftsyotodnraxtsyotodbpqm'
        pattern = 'tsyotod'
        expected = [1, 10, 20, 32, 33, 34, 43, 44, 45]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_26(self):
        text = 'czlgvtyeeczlgvskczlgvjldhhczlgvxtczlgvsaczllvyy'
        pattern = 'czlgv'
        expected = [1, 2, 9, 10, 11, 16, 17, 18, 26, 27, 28, 33, 34, 35, 41]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_27(self):
        text = 'zbiawoqzzpiawrbzpiaemoezpiaiwtuuqzzpoiawocerzpiuawpxkda'
        pattern = 'zpiaw'
        expected = [1, 8, 9, 10, 16, 24, 35, 45]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_28(self):
        text = 'fkocubrriovbfkocuarrrootfkocuarrcjfkocuarrryfkocuargqvdzfkocuarrpgn'
        pattern = 'fkocuarr'
        expected = [1, 12, 13, 14, 24, 25, 26, 34, 35, 36, 45, 56, 57, 58]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_29(self):
        text = 'vvdrikmgvvdijofsyhvvdigervvdixtiavvdiqtvxvdicdavvdiaxh'
        pattern = 'vvdi'
        expected = [1, 8, 9, 10, 18, 19, 20, 25, 26, 27, 33, 34, 35, 40, 41, 42, 47, 48, 49]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_30(self):
        text = 'rkpzsurzrvkpzsutwljdkpzsurtqudbkpzkurawxje'
        pattern = 'kpzsur'
        expected = [1, 2, 3, 11, 20, 21, 22, 32]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_31(self):
        text = 'zudcpaeizfudcvfzudcokbvzudcyozudnciqzudnapage'
        pattern = 'zudc'
        expected = [1, 2, 9, 10, 11, 15, 16, 17, 23, 24, 25, 30, 37]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_32(self):
        text = 'cjhmdpcfzfcxjhmdivlcjhmceascjhmdhkcjhmdelacjhmdre'
        pattern = 'cjhmd'
        expected = [1, 2, 11, 12, 13, 20, 27, 28, 29, 34, 35, 36, 42, 43, 44]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_33(self):
        text = 'rtzqicweixllfrtzicwlyirtzqiswlohfmrtzzicwlxnmh'
        pattern = 'rtzqicwl'
        expected = [1, 14, 23, 35]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_34(self):
        text = 'nhnkvyyknhckvlhphxnhckvgftnhckvspnxckvaygdnhcwvaknrhckvvak'
        pattern = 'nhckv'
        expected = [1, 8, 9, 10, 18, 19, 20, 26, 27, 28, 34, 43, 50, 51, 52]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_35(self):
        text = 'cslpcwuhlhlcslpcwuhgbycslpcwuhckmcslkcwuhom'
        pattern = 'cslpcwuh'
        expected = [1, 2, 11, 12, 13, 22, 23, 24, 34]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_36(self):
        text = 'slaryzeurjufslarazeuhxvleslpryzeurvsslaryzeufjoxslaryzevjp'
        pattern = 'slaryzeu'
        expected = [1, 2, 13, 26, 36, 37, 38, 49]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_37(self):
        text = 'zwqkvhatbvwqkvkbfoxovwqkvhzpvoqkvhglxvwqkvhswrn'
        pattern = 'vwqkvh'
        expected = [1, 2, 10, 20, 21, 22, 29, 37, 38, 39]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_38(self):
        text = 'jckbmdgjckrbdkmtljckpbbwjckbilvajckscbborjckbyglxjckbxtdw'
        pattern = 'jckb'
        expected = [1, 2, 8, 18, 24, 25, 26, 33, 41, 42, 43, 49, 50, 51]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_39(self):
        text = 'hpjacdxwabxahpjacdexehpijacdxlinfhhpljacdxvaihpjacdxtshkhpjacdxfafeahmjacdxvd'
        pattern = 'hpjacdx'
        expected = [1, 2, 13, 22, 35, 45, 46, 47, 56, 57, 58, 69]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_40(self):
        text = 'pmqfrwvftvpmqfrwvilpmqfrwvoobnkpmqfwwvgwjldpmqyrwvid'
        pattern = 'pmqfrwv'
        expected = [1, 2, 10, 11, 12, 19, 20, 21, 32, 44]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_41(self):
        text = 'xfbiynfnzhxfbiqnfnqqlxfzbiqnfnnddxfqbiqnfnfooxoxfbuiqnfnayfdmxfbiqnfnukh'
        pattern = 'xfbiqnfn'
        expected = [1, 10, 11, 12, 22, 34, 48, 61, 62, 63]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_42(self):
        text = 'znsnildytyznsnidydiaulznsnidyupqznsngdyoiznsnidydxnuznsfidymjo'
        pattern = 'znsnidy'
        expected = [1, 10, 11, 12, 22, 23, 24, 33, 41, 42, 43, 53]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_43(self):
        text = 'rdggrdicjrdgslardggvkcrdggijqt'
        pattern = 'rdgg'
        expected = [1, 2, 10, 15, 16, 17, 22, 23, 24]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_44(self):
        text = 'gistwclycisitwcxwistwcadqkistwcccwgistwcdlhjistwcwwujj'
        pattern = 'istwc'
        expected = [1, 2, 3, 10, 11, 12, 17, 18, 19, 26, 27, 28, 35, 36, 37, 44, 45, 46]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_45(self):
        text = 'bqmjptghyreqrmjpcneqmjpsgwemjpuyidbeqmjpsteqmjmhzfyeqyjpfzy'
        pattern = 'eqmjp'
        expected = [1, 2, 11, 18, 19, 20, 27, 35, 36, 37, 43, 52]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_46(self):
        text = 'dxjbotveejdjbotgbdvdjboujhyhdjbocquydjbotywnjfdjbotliwamhdjobotcnfm'
        pattern = 'djbot'
        expected = [1, 2, 3, 10, 11, 12, 20, 29, 36, 37, 38, 46, 47, 48, 58]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_47(self):
        text = 'rtgehrpfrtgelbdqrotgekgowxrrtgecvol'
        pattern = 'rtge'
        expected = [1, 2, 8, 9, 10, 17, 18, 19, 27, 28, 29]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_48(self):
        text = 'mwfmyeqwomwfsmduumwfmiomwfmveutcwfmobmwfmkmcywkdmwfmvjiu'
        pattern = 'mwfm'
        expected = [1, 2, 10, 17, 18, 19, 23, 24, 25, 32, 33, 37, 38, 39, 48, 49, 50]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_49(self):
        text = 'gxusjgmhtegxlsjgeprngxglsjgnfxbgxlscgnhlzgxlasjgqiagxlsjgfey'
        pattern = 'gxlsjg'
        expected = [1, 10, 11, 12, 21, 22, 23, 32, 42, 51, 52, 53]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_50(self):
        text = 'vgtyagbcvsqhfvgtyagbclxmvhtyagbhhvgtyaegbvstvgtyagbvdpagtyagbljglvgtyagbpvm'
        pattern = 'vgtyagb'
        expected = [1, 2, 13, 14, 15, 25, 34, 44, 45, 46, 55, 56, 65, 66, 67]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_51(self):
        text = 'gltdqcoftgltdqzcgltdmjrgltxdqby'
        pattern = 'gltdq'
        expected = [1, 2, 9, 10, 11, 17, 24]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_52(self):
        text = 'chujzgsucachujzqggoechujzgtzrqfchujzkgsytochujygnvwpt'
        pattern = 'chujzg'
        expected = [1, 2, 11, 20, 21, 22, 32, 43]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_53(self):
        text = 'szhhlcmkfvxjnszjhlcmoysmvszjhlcmkonnkszjhlcmlkskszjhlcmkmpnca'
        pattern = 'szjhlcmk'
        expected = [1, 14, 25, 26, 27, 38, 48, 49, 50]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_54(self):
        text = 'bnmnyjazcabnmnyjouumjbnmnyjiqmumbznmnyjcwagbnmnyjopgfabnmnyjnuau'
        pattern = 'bnmnyj'
        expected = [1, 2, 10, 11, 12, 21, 22, 23, 33, 34, 35, 43, 44, 45, 54, 55, 56]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_55(self):
        text = 'hrwfkfpdnhvwfkfpofzwhvwwfkfpplmdsyhvwfkfpvfhvwfkfpauxhvwfkfpmkhvwfkfptpo'
        pattern = 'hvwfkfp'
        expected = [1, 9, 10, 11, 21, 34, 35, 36, 43, 44, 45, 53, 54, 55, 62, 63, 64]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_56(self):
        text = 'ldcqktxvuldckteeldckteovsgldcptokeyldcktuenli'
        pattern = 'ldckt'
        expected = [1, 9, 10, 11, 16, 17, 18, 27, 35, 36, 37]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_57(self):
        text = 'vidqjorsivimqjorxtykzvimqjorhtfjjwvimqjorbkkzx'
        pattern = 'vimqjor'
        expected = [1, 9, 10, 11, 21, 22, 23, 34, 35, 36]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_58(self):
        text = 'mbkftirvmbkftcqiwmbketbwmbkftdsmbktftiecbmbkftbcf'
        pattern = 'mbkft'
        expected = [1, 2, 8, 9, 10, 18, 24, 25, 26, 32, 41, 42, 43]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_59(self):
        text = 'lhdcyfgmgntlhyrcyfgncedlhrcefgjnhuzlhrcyfgcplxhrcyfgdpv'
        pattern = 'lhrcyfg'
        expected = [1, 12, 24, 35, 36, 37, 45, 46, 47]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_60(self):
        text = 'wymnphxhtwzmnmrvkfwymnraawymnfpjjwymnqlsie'
        pattern = 'wymn'
        expected = [1, 2, 10, 18, 19, 20, 25, 26, 27, 33, 34, 35]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_61(self):
        text = 'lxyjqgvnjgnnxyjqgvjgzhlxyjqgnjwjjieylxyjqgvjbugrlxyjqgvjal'
        pattern = 'lxyjqgvj'
        expected = [1, 12, 13, 23, 36, 37, 38, 48, 49, 50]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_62(self):
        text = 'xjtblmexnjtbnhupxjtbbjagxjtbsbpfxjtqnjxfxjtbqg'
        pattern = 'xjtb'
        expected = [1, 2, 8, 9, 10, 16, 17, 18, 24, 25, 26, 33, 40, 41, 42]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_63(self):
        text = 'gzgoqqzgtjgzoqqzidiugzsoqqzjlygzoqqbouzngzoqqzzssagziqqzaxgzoqqvzkpo'
        pattern = 'gzoqqz'
        expected = [1, 2, 3, 10, 11, 12, 21, 31, 40, 41, 42, 51, 59]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_64(self):
        text = 'gfgsxzsqkqvogfgsazsdcgfgsuxzsowgfgsxzqljdhcgfgsxzslwaqngfgsxzstfpxz'
        pattern = 'gfgsxzs'
        expected = [1, 2, 13, 22, 32, 43, 44, 45, 55, 56, 57]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_65(self):
        text = 'mxuanfxzrmxnanplmxnanzvyqhmxnanafimenannmqnfmxfnancmrmnanndbp'
        pattern = 'mxnan'
        expected = [1, 9, 10, 11, 16, 17, 18, 26, 27, 28, 35, 45, 54]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_66(self):
        text = 'jmtpqputcijmtpqputlrehjmtpwqputzsliejmtpqkutgpqpljmtpqputdcfbjmtpqputvefjmipqputihvcr'
        pattern = 'jmtpqput'
        expected = [1, 2, 10, 11, 12, 23, 37, 49, 50, 51, 61, 62, 63, 73]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_67(self):
        text = 'gyvvdvkyvvmnljkkyavvsdgkvyvctxn'
        pattern = 'kyvv'
        expected = [1, 2, 6, 7, 8, 16, 24]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_68(self):
        text = 'yfaalwcgmkqyfaalwcbfwyfaablwwbwmyfaalwahkfydfaalwwo'
        pattern = 'yfaalw'
        expected = [1, 2, 11, 12, 13, 22, 32, 33, 34, 43, 44, 45]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_69(self):
        text = 'nmszbdkzibnmszbkzysnmszbzkkpanmszbkzlycnmszbkmyqkfnmszbikzcpz'
        pattern = 'nmszbkz'
        expected = [1, 10, 11, 12, 20, 29, 30, 31, 40, 51]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_70(self):
        text = 'lpfudamfblpfuonnjlpfguhyfxlpfuaknwalxfuhnv'
        pattern = 'lpfu'
        expected = [1, 2, 9, 10, 11, 18, 26, 27, 28, 36]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_71(self):
        text = 'yncicwkblbmcicnsdbnciczbqbncicwewtbncicxncbncxckmcmbncidchjtcq'
        pattern = 'bncic'
        expected = [1, 2, 10, 17, 18, 19, 25, 26, 27, 34, 35, 36, 43, 52]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_72(self):
        text = 'zptyeyzptyxtokzctyxsyzptyjbwzptygfqayzpetypilmzptyvwlv'
        pattern = 'zpty'
        expected = [1, 2, 6, 7, 8, 15, 21, 22, 23, 28, 29, 30, 38, 46, 47, 48]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_73(self):
        text = 'fzlqzfgoxehhofzlqzggocldfzlqzfgogdfzlqwzfgotgafzlqzfnobpfwr'
        pattern = 'fzlqzfgo'
        expected = [1, 2, 14, 24, 25, 26, 35, 47]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_74(self):
        text = 'pnbekgedepnbznohhypnbekxpnbelrpnwbefsvmepnbljcx'
        pattern = 'pnbe'
        expected = [1, 2, 10, 18, 19, 20, 24, 25, 26, 31, 41]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_75(self):
        text = 'uunwjvuaqcrvdzyunjvuaqvuugcuunjvuaqakubnjvuaqbl'
        pattern = 'uunjvuaq'
        expected = [1, 15, 16, 27, 28, 29, 38]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_76(self):
        text = 'wjwyfcguhnwjwpfcgkgwjwhpfcgsppwjwpfcgxf'
        pattern = 'wjwpfcg'
        expected = [1, 10, 11, 12, 20, 30, 31, 32]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_77(self):
        text = 'mmzkuagoxsvqwmmzkagoxeshmmzkagoxyclmmzkaxgoxfqmmzkeagoxulmmzkafgoxpfo'
        pattern = 'mmzkagox'
        expected = [1, 13, 14, 15, 24, 25, 26, 36, 47, 58]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_78(self):
        text = 'axwlyzkczhbwaxwlzkbnakwlzkvheaaxwlzkvwybaxwlzkgznqaxwlzkruautaxwlzkdwdc'
        pattern = 'axwlzk'
        expected = [1, 12, 13, 14, 21, 30, 31, 32, 40, 41, 42, 50, 51, 52, 61, 62, 63]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_79(self):
        text = 'tgbohaketgbohaydoztfbohazhfftcbohaacvxtgbdohadtv'
        pattern = 'tgboha'
        expected = [1, 2, 8, 9, 10, 19, 29, 39]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_80(self):
        text = 'rxxqzefhxxqphnfxjxqfeubfxxqqitqfxxqeybhxfxxqekjfxxqqqez'
        pattern = 'fxxq'
        expected = [1, 2, 7, 8, 9, 15, 23, 24, 25, 31, 32, 33, 40, 41, 42, 47, 48, 49]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_81(self):
        text = 'uvpwndawgkuvpwndadjihsuvepwndaorfuvpwnjabsxhruvpwncakj'
        pattern = 'uvpwnda'
        expected = [1, 2, 10, 11, 12, 23, 34, 46]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_82(self):
        text = 'fbjaaufbjcakcnfbjayewfbjalusfbjaznlcyfbjakqhqfbjjatju'
        pattern = 'fbja'
        expected = [1, 2, 7, 14, 15, 16, 21, 22, 23, 28, 29, 30, 37, 38, 39, 46]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_83(self):
        text = 'lhfirelgkblmfirelzflhifreldshkrlhfqirellcelhfwirelykrizlhfirelvcn'
        pattern = 'lhfirel'
        expected = [1, 2, 11, 20, 32, 43, 55, 56, 57]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_84(self):
        text = 'xlqsklauuhmxlqsluauvwpokxlqslaujuxlqslajxiyoxlqhlaujlglqslauzlbu'
        pattern = 'xlqslau'
        expected = [1, 12, 24, 25, 26, 34, 45, 54, 55]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_85(self):
        text = 'ockfizywnxxockizdzpfockizubmzorkizimwocxkizmkmoekizqoockizxk'
        pattern = 'ockiz'
        expected = [1, 11, 12, 13, 20, 21, 22, 30, 38, 47, 53, 54, 55]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_86(self):
        text = 'fijvclarfijxsffijveggxhpfijvnhcafrjvjy'
        pattern = 'fijv'
        expected = [1, 2, 9, 14, 15, 16, 24, 25, 26, 33]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_87(self):
        text = 'oonfkwloonwfkqsyooonekmonnhoponfktde'
        pattern = 'oonfk'
        expected = [1, 2, 8, 18, 28, 29, 30]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_88(self):
        text = 'iciplwprpicildnicilxbtyicxilynticildo'
        pattern = 'icil'
        expected = [1, 9, 10, 11, 15, 16, 17, 24, 31, 32, 33]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_89(self):
        text = 'vlkknxflyuvlkknxflshvlkknxfljshtvlkknxflcjyvlkknxfleyvlklnxflshqeu'
        pattern = 'vlkknxfl'
        expected = [1, 2, 10, 11, 12, 20, 21, 22, 32, 33, 34, 43, 44, 45, 54]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_90(self):
        text = 'vowavslxmahvoavslxpmncvoavslxmorvoavsulxmtnedvmavslxmory'
        pattern = 'voavslxm'
        expected = [1, 12, 22, 23, 24, 33, 46]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_91(self):
        text = 'zcxgywngprlzcxgyfsczfcxgyddmzcxgyplqzvxgyzneaaacxgyiqxx'
        pattern = 'zcxgy'
        expected = [1, 2, 11, 12, 13, 20, 21, 22, 28, 29, 30, 37, 47, 48]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_92(self):
        text = 'gvisshvhivikgvissvhiruagvisasvhixcvgvissvhvisrqgvissvhilnfdhgvissvhieyoh'
        pattern = 'gvissvhi'
        expected = [1, 12, 13, 14, 24, 36, 47, 48, 49, 60, 61, 62]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_93(self):
        text = 'vhwgfxnllvowgpxljcfvjwgfxymlqbvowgfxmqsftvowgfxiyylvowgsxadtvowgfzxwa'
        pattern = 'vowgfx'
        expected = [1, 10, 20, 30, 31, 32, 41, 42, 43, 52, 61]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_94(self):
        text = 'mxephdzmxphiswsmxphabmxpkkelf'
        pattern = 'mxph'
        expected = [1, 7, 8, 9, 15, 16, 17, 22]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_95(self):
        text = 'rantdhhrantdmbhcrantdsigferanudxrlvrantdqvx'
        pattern = 'rantd'
        expected = [1, 2, 7, 8, 9, 16, 17, 18, 27, 35, 36, 37]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_96(self):
        text = 'rvaxilcbkgobnrvaxilcbgwjvzrvaxilcbdcrvaxilwcbdshcrvaxiocbjhwrvaxilcbgccqrvaxilcbui'
        pattern = 'rvaxilcb'
        expected = [1, 2, 13, 14, 15, 26, 27, 28, 37, 50, 60, 61, 62, 72, 73, 74]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_97(self):
        text = 'zpesnwtklpzesnavcpznesnafpezpzesnjmbpzesunempzesnxyutnpzesnidh'
        pattern = 'pzesn'
        expected = [1, 2, 9, 10, 11, 18, 28, 29, 30, 37, 44, 45, 46, 54, 55, 56]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_98(self):
        text = 'qoutwviurgatqoutviyznkqoutvivuqoutvilbqoutvigd'
        pattern = 'qoutvi'
        expected = [1, 12, 13, 14, 22, 23, 24, 30, 31, 32, 38, 39, 40]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_99(self):
        text = 'sxdlmewcqxdldbpnpqxdlbhvluqxdlkzdxuqxdlvf'
        pattern = 'qxdl'
        expected = [1, 2, 8, 9, 10, 17, 18, 19, 26, 27, 28, 35, 36, 37]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_100(self):
        text = 'xrqglbndioxrqglbhnuxrtqglbpwsrxrqgnbsciuxrqglbnfeqwxrqglbtqxrqglbza'
        pattern = 'xrqglb'
        expected = [1, 2, 10, 11, 12, 20, 31, 40, 41, 42, 51, 52, 53, 59, 60, 61]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_101(self):
        text = 'ybbozjvhatybbojihftgzybbojtvhpwkybbojvhqjv'
        pattern = 'ybbojvh'
        expected = [1, 11, 22, 32, 33, 34]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_102(self):
        text = 'pjohanrdbpjohtntptpjohanofwjpjohancraompjohandjhdt'
        pattern = 'pjohan'
        expected = [1, 2, 10, 18, 19, 20, 28, 29, 30, 39, 40, 41]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_103(self):
        text = 'eonehqjoynxpueonehojoahvukeonehojbxgeleonefhojoxmamh'
        pattern = 'eonehojo'
        expected = [1, 13, 14, 15, 27, 39]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_104(self):
        text = 'jwaasjqmrajwaasjqlmpdavjwaasjqrmjcyxcjwaasqjqmken'
        pattern = 'jwaasjqm'
        expected = [1, 2, 11, 24, 38]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_105(self):
        text = 'jgtrafbwfqlejtrafbigzwsjtrafbwodyvqjtrafbwsqjtrafbwnjlqjtrafbwnd'
        pattern = 'jtrafbw'
        expected = [1, 2, 3, 13, 23, 24, 25, 35, 36, 37, 44, 45, 46, 55, 56, 57]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_106(self):
        text = 'kujfgkpuluskujgkpuflcjmkukgkpustkujgbpujwguw'
        pattern = 'kujgkpu'
        expected = [1, 11, 12, 13, 24, 33]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_107(self):
        text = 'plfmhwejplamhazpwmhpwfaplmhamtopamhzbozplmhsoxpkqplzmhpenvx'
        pattern = 'plmh'
        expected = [1, 9, 16, 23, 24, 25, 32, 39, 40, 41, 50]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_108(self):
        text = 'zktgjufzkighicczkiggrgzkfgflqvzkiyeaag'
        pattern = 'zkig'
        expected = [1, 7, 8, 9, 15, 16, 17, 23, 31]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_109(self):
        text = 'onguupautongucgmowtoygucpkooingucpabbab'
        pattern = 'ongucp'
        expected = [1, 10, 20, 28, 29, 30]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_110(self):
        text = 'tetneqyzektetnetqyzjhatetnequyzwutetnkqyzwcqntetneqyirivytetnqyzts'
        pattern = 'tetneqyz'
        expected = [1, 2, 11, 23, 34, 46, 58]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_111(self):
        text = 'dcjcxbzykgjdqjdxbzxeusdqjqxbzftjoudqjcxbzzsj'
        pattern = 'dqjcxbz'
        expected = [1, 12, 23, 34, 35, 36]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_112(self):
        text = 'ivuqggvuaihuqgejwtaivuqqgvveaaivoqgtlbgy'
        pattern = 'ivuqg'
        expected = [1, 2, 10, 20, 31]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_113(self):
        text = 'bqlrgkyrbebqlrgkynuelybqlrskysgpzibqlrgkypqobqlrgkyzwpxbqlrgkyykxrbqlrfgkyqzzcf'
        pattern = 'bqlrgky'
        expected = [1, 2, 10, 11, 12, 23, 34, 35, 36, 44, 45, 46, 55, 56, 57, 67]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_114(self):
        text = 'ldpiqivostlpsdiqzezgplpdiqphebpdiqpqhlpdiquhot'
        pattern = 'lpdiq'
        expected = [1, 11, 21, 22, 23, 30, 31, 37, 38, 39]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_115(self):
        text = 'wmgxiqryowjgxfnkcwmgxcqawmgxnxhrr'
        pattern = 'wmgx'
        expected = [1, 2, 10, 17, 18, 19, 24, 25, 26]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_116(self):
        text = 'uxappgotyuxapwixpkfuxapuadguxapib'
        pattern = 'uxap'
        expected = [1, 2, 9, 10, 11, 19, 20, 21, 27, 28, 29]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_117(self):
        text = 'ojbsexraojbsxxgojbstjojbpshoo'
        pattern = 'ojbs'
        expected = [1, 2, 8, 9, 10, 15, 16, 17, 22]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_118(self):
        text = 'ewjnydxvfymaewjydxldobhewjydxpywaewjydxmoewjyaxkpf'
        pattern = 'ewjydx'
        expected = [1, 12, 13, 14, 23, 24, 25, 33, 34, 35, 42]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_119(self):
        text = 'vewveftznvrtvexziiwvryvemzvrwvecxasvrwvekrvrwvefjey'
        pattern = 'vrwve'
        expected = [1, 10, 20, 26, 27, 28, 35, 36, 37, 42, 43, 44]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_120(self):
        text = 'ahoqfhnwssxahofhnizhmiahofhnedpxahofonlydbkahofhnvl'
        pattern = 'ahofhn'
        expected = [1, 11, 12, 13, 22, 23, 24, 33, 43, 44, 45]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_121(self):
        text = 'clegrzjuclygrknkguclegrkeclegraojbclegbbycl'
        pattern = 'clegr'
        expected = [1, 2, 9, 18, 19, 20, 25, 26, 27, 35]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_122(self):
        text = 'mswhzqmcyhmxwhztqsgsumxwhzqgcnoqmxwhzqdumxwhzquatssmkwhzqfvfmxlhzqccrn'
        pattern = 'mxwhzq'
        expected = [1, 11, 21, 22, 23, 32, 33, 34, 40, 41, 42, 52, 61]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_123(self):
        text = 'wjuqvfwjuvqxdwjvuqbdrwjuqgbwjtuqiabs'
        pattern = 'wjuq'
        expected = [1, 2, 7, 14, 21, 22, 23, 28]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_124(self):
        text = 'lxchwojulxghecoojalxghafrtlxghqqpllxghdfzaolxghawthlxghoahq'
        pattern = 'lxgh'
        expected = [1, 8, 9, 10, 18, 19, 20, 26, 27, 28, 34, 35, 36, 43, 44, 45, 51, 52, 53]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_125(self):
        text = 'adhxqyioadhxtkyadhexdsjhyadhwbcffafhxzndmn'
        pattern = 'adhx'
        expected = [1, 2, 8, 9, 10, 16, 26, 34]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_126(self):
        text = 'uepsjsauepsjhryphuepsjjfkqbhuepsjvhpluepsjvtmoruxpsjzatluueysjmx'
        pattern = 'uepsj'
        expected = [1, 2, 7, 8, 9, 17, 18, 19, 28, 29, 30, 37, 38, 39, 48, 58]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_127(self):
        text = 'zicdmpmpaziecdmpmvqzicdvpmnxjzzcdmpmvylxzicdmbpmetm'
        pattern = 'zicdmpm'
        expected = [1, 2, 10, 20, 30, 31, 41]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_128(self):
        text = 'xorkvqplazgrgkxorksvqlakotojxorkvqlapuzijxorkvqlaaecxorkvqlwcvxsrkvqlaesvy'
        pattern = 'xorkvqla'
        expected = [1, 15, 28, 29, 30, 41, 42, 43, 53, 63]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_129(self):
        text = 'jovwvtybnlgjovvtybcbftjokvtybhxpjovtvtybnprhjovvtyhbbzz'
        pattern = 'jovvtyb'
        expected = [1, 11, 12, 13, 23, 33, 45]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_130(self):
        text = 'udfyyenpehuqfyyenprammudfyyenpetdzjdfyyenprbe'
        pattern = 'udfyyenp'
        expected = [1, 2, 11, 22, 23, 24, 35, 36]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_131(self):
        text = 'pwbvnztkmfpywbvnkrpwbvnxzepwbdvnfapwdbvnlppwbvnerpr'
        pattern = 'pwbvn'
        expected = [1, 2, 11, 12, 13, 18, 19, 20, 27, 35, 42, 43, 44]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_132(self):
        text = 'uyfvowpkuyfvwscuyfvkvrzuyfvknjuyfvojhxeuyfvkicbuyfvtdkvd'
        pattern = 'uyfv'
        expected = [1, 2, 8, 9, 10, 15, 16, 17, 23, 24, 25, 30, 31, 32, 39, 40, 41, 47, 48, 49]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_133(self):
        text = 'xwhflhbmxwhqlhbnixqwhqlhgkkldxwhqlhtgdnrxwhqlhoxrkyxwhqlhtdyn'
        pattern = 'xwhqlh'
        expected = [1, 8, 9, 10, 18, 19, 20, 29, 30, 31, 40, 41, 42, 51, 52, 53]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_134(self):
        text = 'mgvppjceabgmgvpjcvwmgvpjctdymgvpyjctxyf'
        pattern = 'mgvpjc'
        expected = [1, 11, 12, 13, 19, 20, 21, 29]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_135(self):
        text = 'rakhdsrilcnrakdsrstpmrakdsrifxmqywrakdsrivgue'
        pattern = 'rakdsri'
        expected = [1, 12, 21, 22, 23, 34, 35, 36]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_136(self):
        text = 'mjvckislqmjvqgvzmkvqdgmjdqcqamjvnezzz'
        pattern = 'mjvq'
        expected = [1, 9, 10, 11, 17, 23, 30]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_137(self):
        text = 'btxurevoqtbthurevowqbtjhurevoimbtaurevomfvbthurevoxcvbthurevoek'
        pattern = 'bthurevo'
        expected = [1, 10, 11, 12, 21, 32, 42, 43, 44, 53, 54, 55]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_138(self):
        text = 'dvkwgceqxjdvkwgctjgdedvkwgncgvdvewgcwjp'
        pattern = 'dvkwgc'
        expected = [1, 2, 10, 11, 12, 22, 31]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_139(self):
        text = 'ephjggnqtsesphjgofjqogphjgigodtephjgoca'
        pattern = 'ephjg'
        expected = [1, 2, 11, 12, 13, 22, 23, 31, 32, 33]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_140(self):
        text = 'czweshjvxphpczwesjvxefebczwesjvxegqczwesjvxhvlmczwesjvxoysi'
        pattern = 'czwesjvx'
        expected = [1, 12, 13, 14, 24, 25, 26, 35, 36, 37, 47, 48, 49]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_141(self):
        text = 'dmfxgtshadmxgtspbdmxgtdsyempdmhxgtssedmugtsluxvn'
        pattern = 'dmxgts'
        expected = [1, 9, 10, 11, 18, 29, 38]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_142(self):
        text = 'ryohkybcagsryohkybgwpqryoyhkybxpryohkybybkryohkybwochjryogkybavswd'
        pattern = 'ryohkyb'
        expected = [1, 2, 11, 12, 13, 23, 32, 33, 34, 42, 43, 44, 55]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_143(self):
        text = 'vfgvoxhrcvflvokocvflvoogvvuflvojynzvzlvoqlvjd'
        pattern = 'vflvo'
        expected = [1, 9, 10, 11, 17, 18, 19, 26, 27, 28, 36]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_144(self):
        text = 'erdunnxhoerdugiterduegerduhha'
        pattern = 'erdu'
        expected = [1, 2, 9, 10, 11, 16, 17, 18, 22, 23, 24]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_145(self):
        text = 'iwnpdwnqsteiwnpzhryiwnywciwnpryyorciwnpswjiwhnpfhrgiwnpvp'
        pattern = 'iwnp'
        expected = [1, 2, 11, 12, 13, 20, 25, 26, 27, 35, 36, 37, 43, 51, 52, 53]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_146(self):
        text = 'cdymwgofncdymwgonncdsymwgoflddymwgordmdcdkmwgornrmcdymwgogb'
        pattern = 'cdymwgo'
        expected = [1, 2, 9, 10, 11, 19, 29, 30, 40, 50, 51, 52]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_147(self):
        text = 'jndutajdaljoduqkksjndulunwjnqduurajndjfx'
        pattern = 'jndu'
        expected = [1, 2, 11, 18, 19, 20, 27, 35]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_148(self):
        text = 'kjabgtvkjabgmhkjabgqikgjabghs'
        pattern = 'kjabg'
        expected = [1, 2, 7, 8, 9, 14, 15, 16, 22, 23, 24]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_149(self):
        text = 'poltnroocuspoldtnfmpnltneoikppoltnkl'
        pattern = 'poltn'
        expected = [1, 2, 12, 20, 29, 30, 31]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_150(self):
        text = 'gdwkrsxgjvgdwkrsfypgmgvdwkrsepgdwkcrsymdgdwkrsambgf'
        pattern = 'gdwkrs'
        expected = [1, 2, 10, 11, 12, 22, 23, 24, 31, 40, 41, 42]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_151(self):
        text = 'fnfaldmfynfnfaldmozvyfnfjaldmkcwtwfnfaldmigaejfnfaldmxxbkfnfaldmxoi'
        pattern = 'fnfaldm'
        expected = [1, 2, 10, 11, 12, 22, 34, 35, 36, 46, 47, 48, 57, 58, 59]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_152(self):
        text = 'fpajjwmdhfpajqirgrafpajnxnbfpcajmaofuajgango'
        pattern = 'fpaj'
        expected = [1, 2, 9, 10, 11, 19, 20, 21, 28, 36]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_153(self):
        text = 'kkpqhqfddtkkpqhqdxekkpqhqfamclkkpqyhqfkmkkpqhqfwb'
        pattern = 'kkpqhqf'
        expected = [1, 2, 11, 19, 20, 21, 31, 40, 41, 42]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_154(self):
        text = 'qjrjlsgaapqjrjlslfazzqjrjlslaekqjrjlwlapyc'
        pattern = 'qjrjlsla'
        expected = [1, 11, 21, 22, 23, 32]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_155(self):
        text = 'jkdkcxfzhtlmjkdkcxffhzzckejdkkcxfhvssjkdkcxfbhokjkdkcxfhmhjkdscxfhwvjkd'
        pattern = 'jkdkcxfh'
        expected = [1, 13, 27, 38, 48, 49, 50, 59]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_156(self):
        text = 'vesfogjkndesvffmtdesfbvrasesfzdbq'
        pattern = 'desf'
        expected = [1, 2, 10, 17, 18, 19, 26, 27]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_157(self):
        text = 'vhprnueesawjjvhprueeshxvvhpzrueeszyvhprukeswjivhprueesjzzuvhprueessvpvhprueesixfek'
        pattern = 'vhpruees'
        expected = [1, 13, 14, 15, 25, 36, 46, 47, 48, 58, 59, 60, 69, 70, 71]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_158(self):
        text = 'jqijoosmoqijooskusqijopswhhqijooshqydqijoostzybfqijoosjfjq'
        pattern = 'qijoos'
        expected = [1, 2, 3, 9, 10, 11, 19, 27, 28, 29, 37, 38, 39, 48, 49, 50]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_159(self):
        text = 'aybmkgoogarwaymkgoyeaymktoxpaymkgoybaymxkgoeznaymkgkopxr'
        pattern = 'aymkgo'
        expected = [1, 12, 13, 14, 21, 28, 29, 30, 37, 47]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_160(self):
        text = 'spjthhaespthffkspbheoaspethpampthqqwspthlvlvexspthkxoy'
        pattern = 'spth'
        expected = [1, 8, 9, 10, 16, 23, 30, 31, 36, 37, 38, 46, 47, 48]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_161(self):
        text = 'yefgoxuvcyefgoizyefgofapyefgoturewyefgoor'
        pattern = 'yefgo'
        expected = [1, 2, 9, 10, 11, 16, 17, 18, 24, 25, 26, 34, 35, 36]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_162(self):
        text = 'jmvntdcdfgujovntdcdkdjmentdcdvgzgjmvdtdcdgdxqejmjvntdcdxfjmvntdcqwfjmvntdcdbq'
        pattern = 'jmvntdcd'
        expected = [1, 2, 12, 22, 34, 47, 48, 49, 58, 67, 68, 69]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_163(self):
        text = 'orlzgghjboblogghjrmcorlogthmdvahorlogghkdcjczorlogghmvorlogghmcc'
        pattern = 'orloggh'
        expected = [1, 10, 21, 32, 33, 34, 45, 46, 47, 54, 55, 56]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_164(self):
        text = 'cxzmnslutcximntufbecximxqcowcximntcgx'
        pattern = 'cximn'
        expected = [1, 9, 10, 11, 20, 28, 29, 30]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_165(self):
        text = 'hclotmhjchclotrmhzghcolotmhmdjmnhclotmhrw'
        pattern = 'hclotmh'
        expected = [1, 2, 10, 20, 32, 33, 34]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_166(self):
        text = 'rhbsthcbrhbthjqwribthdtrbhbthzmwn'
        pattern = 'rhbth'
        expected = [1, 8, 9, 10, 17, 24, 25, 26]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_167(self):
        text = 'tbhxupqtbhxuxzhbjotbfhxuzjgyytbhxuxzitjtbhxnlvdpxptbhxuilq'
        pattern = 'tbhxu'
        expected = [1, 2, 7, 8, 9, 19, 29, 30, 31, 40, 50, 51, 52]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_168(self):
        text = 'jvldrlfstjsldnaejsldeqtajslmdbzjbjsldwiiik'
        pattern = 'jsld'
        expected = [1, 9, 10, 11, 16, 17, 18, 25, 33, 34, 35]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_169(self):
        text = 'hhllptdhznanvuhllptdhdscbhihllptdhuzjpyelhllptdhzjwae'
        pattern = 'hllptdhz'
        expected = [1, 2, 3, 15, 28, 41, 42, 43]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_170(self):
        text = 'mbfkrwjygmvzmbfkrwjypqmbfkrwjytkdmbfkrwjypdrmbfkrajyszombjkrwjyucp'
        pattern = 'mbfkrwjy'
        expected = [1, 2, 12, 13, 14, 22, 23, 24, 33, 34, 35, 45, 56]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_171(self):
        text = 'sfuxaeidglfukxcdduqlfuxxjplfuxrkpdd'
        pattern = 'lfux'
        expected = [1, 2, 10, 19, 20, 21, 26, 27, 28]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_172(self):
        text = 'qksmtthbbwydxqksmtthbgwzwqktmtthbcsrqksmtthblohzqqksmttlhbcnb'
        pattern = 'qksmtthb'
        expected = [1, 2, 13, 14, 15, 26, 36, 37, 38, 50]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_173(self):
        text = 'lkkytymeztnlkkttymeaqqgkkttymeiegflkkttqmekhlykkttymepqa'
        pattern = 'lkkttyme'
        expected = [1, 11, 12, 13, 23, 24, 35, 45, 46, 47]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_174(self):
        text = 'vneulvvkvrnvveulvvkvvbuahveudvvkvhdzdpvkeulvvkvka'
        pattern = 'veulvvkv'
        expected = [1, 2, 3, 12, 13, 14, 26, 39, 40, 41]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_175(self):
        text = 'hjgmfeijhjsmaymhjgmfvbfhagmmtzhjxmjdiehjxgmmwhy'
        pattern = 'hjgm'
        expected = [1, 2, 9, 15, 16, 17, 24, 31, 39]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_176(self):
        text = 'qdqiqbkuxqaiqkwebqqvqvhqqikcaqqiqxlnqqriqqwckqqisswb'
        pattern = 'qqiq'
        expected = [1, 2, 3, 10, 18, 24, 29, 30, 31, 37, 38, 46]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_177(self):
        text = 'qkmpzgenpqkmpmmgemkeqkmpmgebpqkmtmgebjjqkmymgegluqkmpmgecxlqzqbmpmgevh'
        pattern = 'qkmpmge'
        expected = [1, 10, 20, 21, 22, 30, 40, 49, 50, 51, 62]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_178(self):
        text = 'qamumfdujqamumvrofqamumvmipxqamumvfdkhqamumvsudoqamumwxuzjqamumvljfk'
        pattern = 'qamumv'
        expected = [1, 9, 10, 11, 18, 19, 20, 28, 29, 30, 38, 39, 40, 49, 58, 59, 60]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_179(self):
        text = 'klxacgglzclxacggceclxacgwblqlbclxacggazfyclxaclgymlvn'
        pattern = 'clxacgg'
        expected = [1, 2, 9, 10, 11, 19, 30, 31, 32, 42]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_180(self):
        text = 'mksvgjrlgrigmksvgirlabhwksvgirlsvmkswgirlbxtku'
        pattern = 'mksvgirl'
        expected = [1, 12, 13, 14, 24, 25, 34]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_181(self):
        text = 'acjdouhxvzacjdouorjacjdouyobacjdoouowrfnacjdouoognmaejdouofa'
        pattern = 'acjdouo'
        expected = [1, 10, 11, 12, 20, 29, 40, 41, 42, 52]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_182(self):
        text = 'dtemwnkchzdtemwfnkinvadtemmwnkdvraqdtemwnknxpodtrmwnktgzqdtemwnkxqghvdtemfwnkidqul'
        pattern = 'dtemwnk'
        expected = [1, 2, 11, 23, 35, 36, 37, 47, 57, 58, 59, 70]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_183(self):
        text = 'ohbaxwpqpwiohbaxyppkuczhohbaxwppuisiohbaxwpppxdtohbaxwppvj'
        pattern = 'ohbaxwpp'
        expected = [1, 12, 24, 25, 26, 36, 37, 38, 48, 49, 50]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_184(self):
        text = 'ithsrmilthseoqpiitthsbpvithfoqugnithzssesthssvqithsygb'
        pattern = 'iths'
        expected = [1, 2, 7, 8, 9, 17, 18, 19, 25, 34, 41, 42, 47, 48, 49]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_185(self):
        text = 'ruinihcewyeruinihcvutafruinwihcttljruinihccwwruinihchgvrcuinihcxymdtruinihcotn'
        pattern = 'ruinihc'
        expected = [1, 2, 11, 12, 13, 24, 35, 36, 37, 45, 46, 47, 56, 57, 58, 68, 69, 70]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_186(self):
        text = 'frznesmxnfhfrznesmxpmfrznesmxdefrznevmxnabmfrznesmxkksgfrznesmxeeqfrzwnesmxuufc'
        pattern = 'frznesmx'
        expected = [1, 2, 11, 12, 13, 21, 22, 23, 32, 43, 44, 45, 55, 56, 57, 67]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_187(self):
        text = 'idjdxhnfdkmsidjdxhnjqixjdxhnolijfidjdxhnmvdzidjdxhnvcfrwidjdxhncwz'
        pattern = 'idjdxhn'
        expected = [1, 2, 12, 13, 14, 22, 33, 34, 35, 44, 45, 46, 56, 57, 58]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_188(self):
        text = 'nawtezxzdwvnawtezxwzxqnzlbnawtezxzwenawtezxzssjnnbawtezxzrn'
        pattern = 'nawtezxz'
        expected = [1, 2, 12, 26, 27, 28, 36, 37, 38, 49, 50, 51]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_189(self):
        text = 'eekztmtcneekztmgmeevztmqoevlzeekztmexxdeekttmvmeekztmpgeaseekztmnekn'
        pattern = 'eekztm'
        expected = [1, 2, 9, 10, 11, 18, 29, 30, 31, 40, 47, 48, 49, 58, 59, 60]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_190(self):
        text = 'lepebdlusfzepegmdqvlepmeszoaolepezuum'
        pattern = 'lepe'
        expected = [1, 2, 11, 12, 20, 29, 30, 31]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_191(self):
        text = 'ndhyfmxnnhyfihjhnhyfbalbqnnhyfwaumj'
        pattern = 'nnhyf'
        expected = [1, 7, 8, 9, 16, 17, 25, 26, 27]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_192(self):
        text = 'chxwjdcvcphxwmdqguchxtwgdvschxwryldcixwumtacjxwnlpoz'
        pattern = 'chxw'
        expected = [1, 2, 9, 10, 11, 19, 27, 28, 29, 36, 44]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_193(self):
        text = 'qouljjtfabqvqouljjtfnzqouljjtfugyeqouljztfmakiz'
        pattern = 'qouljjtf'
        expected = [1, 2, 12, 13, 14, 22, 23, 24, 35]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_194(self):
        text = 'dqztapbmdqzhwdmddqzhieedqzzhtsimsdqzhwtbkpddqzhwhq'
        pattern = 'dqzh'
        expected = [1, 8, 9, 10, 16, 17, 18, 24, 33, 34, 35, 43, 44, 45]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_195(self):
        text = 'jlgwlpwsejjbgtlpwsgwjbgwlpwstrnijbgwlcpwsvnt'
        pattern = 'jbgwlpws'
        expected = [1, 11, 20, 21, 22, 33]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_196(self):
        text = 'ddytikzddlytqkddyknqcgiddytcjstwbddytkvddytratddwtyw'
        pattern = 'ddyt'
        expected = [1, 2, 8, 9, 15, 23, 24, 25, 33, 34, 35, 39, 40, 41, 47]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_197(self):
        text = 'bmbsifwhlybmbswwqesbmbsrfwmdbmbsftjztuibmgbsfwizlw'
        pattern = 'bmbsfw'
        expected = [1, 11, 20, 29, 40]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_198(self):
        text = 'ebwiawfmobdebwiawfmcpuebwpawfmurmaebwiawfjlxb'
        pattern = 'ebwiawfm'
        expected = [1, 2, 11, 12, 13, 23, 35]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_199(self):
        text = 'zojrqzreqmzojrqzrcoqkojrqzrejanzojrqzmeedbkojrqzreodtuzojrqzreib'
        pattern = 'zojrqzre'
        expected = [1, 2, 11, 21, 22, 32, 43, 44, 54, 55, 56]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_200(self):
        text = 'wloxomksyfimzwloxumkszowloxumkessycwljoxumkspgxwnloxumkstmwloxumksaoum'
        pattern = 'wloxumks'
        expected = [1, 13, 14, 15, 24, 36, 48, 49, 50, 58, 59, 60]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_201(self):
        text = 'fuvomawqiuvomawgfhuvomawhzquvomancdvluvomavwifnuvomawwevuhvomawok'
        pattern = 'uvomaw'
        expected = [1, 2, 3, 9, 10, 11, 18, 19, 20, 28, 38, 47, 48, 49, 57, 58, 59]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_202(self):
        text = 'rzyghawdokrzygawdfrunrzygawdwdtawrzygawdxavrzygawdaotrzygaadmvjdyrzygatdzjit'
        pattern = 'rzygawd'
        expected = [1, 10, 11, 12, 21, 22, 23, 33, 34, 35, 43, 44, 45, 54, 66]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_203(self):
        text = 'eyhyzvaqixzdbeyhyvvaqnokeyhyzvaqwxseyhyzvaqxtrleyhyzvaqdvyefeyhyzvaqxsjedyhyzvaqsn'
        pattern = 'eyhyzvaq'
        expected = [1, 2, 14, 24, 25, 26, 35, 36, 37, 47, 48, 49, 60, 61, 62, 72, 73, 74]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_204(self):
        text = 'yvoxzeyyvsxgxhpmyvoxmtyvoxjzzysryvoxcpztyyvmxkl'
        pattern = 'yvox'
        expected = [1, 2, 8, 16, 17, 18, 22, 23, 24, 32, 33, 34, 42]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_205(self):
        text = 'hpxitpqzwqhpxitpqoehpxitpqfjbhpxitpqdqoix'
        pattern = 'hpxitpq'
        expected = [1, 2, 10, 11, 12, 19, 20, 21, 29, 30, 31]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_206(self):
        text = 'bxlgokbbedrbxlgokbjoscbxlgokqbhzmhbxlggokbyvfqbxzgokbvbetebxlgokbtkbxlgokbnk'
        pattern = 'bxlgokb'
        expected = [1, 2, 11, 12, 13, 23, 35, 47, 58, 59, 60, 67, 68, 69]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_207(self):
        text = 'iymfiahhuiymfikmgriiymfimshxtiymfniyecidmfijvndh'
        pattern = 'iymfi'
        expected = [1, 2, 9, 10, 11, 19, 20, 21, 30, 39]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_208(self):
        text = 'lmygvxyiylmyhmqlvjlmytgqbllwyguphoplmygyalmyggbpb'
        pattern = 'lmyg'
        expected = [1, 2, 10, 19, 27, 35, 36, 37, 41, 42, 43]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_209(self):
        text = 'oowhyaboowhnzoowhjjqoowdkm'
        pattern = 'oowh'
        expected = [1, 2, 7, 8, 9, 13, 14, 15, 21]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_210(self):
        text = 'exgubutidtfxexgubutxcxyexgubdutjqexgubudttmbxgubuthahhj'
        pattern = 'exgubut'
        expected = [1, 2, 12, 13, 14, 24, 34, 44, 45]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_211(self):
        text = 'tldqruptshztldqiuptiyotldqiuptjsovitludqiuptnttldqiuptvtvlbtldqiuptztktldqiuptax'
        pattern = 'tldqiupt'
        expected = [1, 11, 12, 13, 22, 23, 24, 36, 46, 47, 48, 59, 60, 61, 70, 71, 72]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_212(self):
        text = 'bwxpvnobwxpxacgrbwxpzdklbwxpkhubwbpjztrzbwxpkqabwxlrg'
        pattern = 'bwxp'
        expected = [1, 2, 7, 8, 9, 16, 17, 18, 24, 25, 26, 32, 40, 41, 42, 48]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_213(self):
        text = 'mnsnrsfggonsrqzymnsrktdykmnsaxzfmnsrluml'
        pattern = 'mnsr'
        expected = [1, 10, 11, 16, 17, 18, 26, 32, 33, 34]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_214(self):
        text = 'wsrkghcetwrkghcdfvfxwrkghcwllugurkghcme'
        pattern = 'wrkghc'
        expected = [1, 2, 3, 9, 10, 11, 20, 21, 22, 32, 33]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_215(self):
        text = 'fifidfquwpqfifidfquuqaffifidfqsuhmpbpfiofidfquwhbe'
        pattern = 'fifidfqu'
        expected = [1, 2, 11, 12, 13, 24, 38]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_216(self):
        text = 'qkvapwmsyuaaqvapwmdgyrqvapwmwygqvapwmun'
        pattern = 'qvapwm'
        expected = [1, 2, 3, 12, 13, 14, 22, 23, 24, 31, 32, 33]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_217(self):
        text = 'sosiwkszuagssostwkszaussostwkszroqsostdwkszhiaansostwkszaqp'
        pattern = 'sostwksz'
        expected = [1, 12, 13, 14, 23, 24, 25, 35, 48, 49, 50]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_218(self):
        text = 'ckipwjaejfvsclkiwjajeqfockiwxjanbjzcsiwjavrmdgckiwnafomuvckiwjsajlupfckiewjamp'
        pattern = 'ckiwja'
        expected = [1, 13, 14, 15, 25, 36, 47, 58, 70]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_219(self):
        text = 'bzjeqzhjoqkqyezjeqzhjbhvaezjeqhhjzihgwezjeqwzhjgacknezjeqzhmjonyfpezjeqzhjeicub'
        pattern = 'ezjeqzhj'
        expected = [1, 2, 13, 14, 15, 26, 39, 53, 66, 67, 68]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_220(self):
        text = 'kacbzubvkachbrnkwkacbfvakafcbvgcqkacbxufnzkacwolgh'
        pattern = 'kacb'
        expected = [1, 2, 9, 17, 18, 19, 25, 33, 34, 35, 43]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_221(self):
        text = 'vdsnevtevvrvdssevtejlsdsnevtevjrvdsnevtemgvvdsnevteellvdsnevtemhkom'
        pattern = 'vdsnevte'
        expected = [1, 2, 12, 22, 23, 32, 33, 34, 43, 44, 45, 54, 55, 56]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_222(self):
        text = 'bvpfzbnsdlbbfzbnylannvfzbnfuepcbvfzrnhyq'
        pattern = 'bvfzbn'
        expected = [1, 11, 12, 21, 22, 32]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_223(self):
        text = 'jhwuowudbjhwduoptjhwhoburjhwoobfxq'
        pattern = 'jhwuo'
        expected = [1, 2, 10, 18, 26]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_224(self):
        text = 'yefkzehvurykkzehvwvqwvyfkzehvdzdzvyfkzehvbrlyfjkzehvxedfkzehvlfjyfkzehvrbus'
        pattern = 'yfkzehv'
        expected = [1, 2, 3, 11, 22, 23, 24, 34, 35, 36, 45, 55, 56, 64, 65, 66]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_225(self):
        text = 'hrwptyvrweptvqrwpxhnyoarrptjfrwxptvwivxruwptneyte'
        pattern = 'rwpt'
        expected = [1, 2, 3, 8, 15, 24, 25, 30, 40, 41, 42]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_226(self):
        text = 'krvvqcparkrvwvqcaokrvvqqcaqkrvvqvyvddc'
        pattern = 'krvvqc'
        expected = [1, 2, 10, 19, 28]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_227(self):
        text = 'letyybggsejidleqyybgghwbdyletyybggfkasretyybggioivletyybggltq'
        pattern = 'letyybgg'
        expected = [1, 2, 14, 26, 27, 28, 39, 40, 50, 51, 52]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_228(self):
        text = 'xphphoqguiagxxphoqgtjqkaspphoqgctwmhxppthoqgtrxpphoqgzoijxppmoqget'
        pattern = 'xpphoqg'
        expected = [1, 13, 14, 25, 26, 37, 46, 47, 48, 58]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_229(self):
        text = 'sqnqzyuisqsqnqzyuisusqnqzyuizlvsqnqzyuigoffsqnqzyuixuowcsqnqzyuiktph'
        pattern = 'sqnqzyui'
        expected = [1, 2, 10, 11, 12, 20, 21, 22, 31, 32, 33, 43, 44, 45, 56, 57, 58]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_230(self):
        text = 'btsiqwsupgqbtslqwkssrfbkbtslqcwsghbnjbtsplqwsjnbtsiqwskrdbtwlqwspjzie'
        pattern = 'btslqws'
        expected = [1, 12, 25, 38, 48, 58]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_231(self):
        text = 'fnqcccwlufdqccsgfdqccwrbuwfdqccfetfdqlccwfgefdqcctlfdqccynbnl'
        pattern = 'fdqcc'
        expected = [1, 9, 10, 11, 16, 17, 18, 26, 27, 28, 35, 44, 45, 46, 51, 52, 53]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_232(self):
        text = 'zfqiunlstzazqiinlsgqwrgzqiunlseotahzriunlspftw'
        pattern = 'zqiunls'
        expected = [1, 2, 3, 12, 23, 24, 25, 36]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_233(self):
        text = 'omgbamwroknomxbamwutisomxbamwrcqlxooumxbamwraoomxbamwrajmzdomxbamwrginv'
        pattern = 'omxbamwr'
        expected = [1, 12, 22, 23, 24, 36, 37, 38, 46, 47, 48, 59, 60, 61]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_234(self):
        text = 'fwjclsdbaysmqdfjclsdbarmbvqfjclsdbaniawbfjclisdbagbfykfjclsdbajictfjcysdbasmifjclnsdbamglhp'
        pattern = 'fjclsdba'
        expected = [1, 2, 3, 14, 15, 16, 27, 28, 29, 41, 54, 55, 56, 67, 78]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_235(self):
        text = 'zezcmzxawiczezdmzgjzezmlzgbkaxzezmzvszxezmzshzezmzai'
        pattern = 'zezmz'
        expected = [1, 12, 20, 30, 31, 32, 38, 39, 40, 45, 46, 47]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_236(self):
        text = 'ryyhvcljrylkwrrykkgcryykgmtbswyykwxvrmyykplc'
        pattern = 'ryyk'
        expected = [1, 9, 14, 15, 20, 21, 22, 30, 31, 37, 38, 39]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_237(self):
        text = 'utvjlxueuvtjpxcsldmutrvjpxihiydutvhjpxqhtmutvjpkllln'
        pattern = 'utvjpx'
        expected = [1, 9, 20, 32, 43]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_238(self):
        text = 'zdndilthukqlzddiltxastzddiltdbyzddiltnzwby'
        pattern = 'zddilt'
        expected = [1, 12, 13, 14, 22, 23, 24, 31, 32, 33]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_239(self):
        text = 'hvatmbitgxaighvatbidksbyphvatbibzvxthvatbitdy'
        pattern = 'hvatbit'
        expected = [1, 14, 26, 36, 37, 38]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_240(self):
        text = 'wxgubuurlawxgubusqewxpubuyiqwxgubuhnwxgubhukksmwxjgubujyzr'
        pattern = 'wxgubu'
        expected = [1, 2, 10, 11, 12, 20, 28, 29, 30, 37, 48]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_241(self):
        text = 'xpxahiukzxpdahmoxgpxahusbxpxahmxglqxopxahnqkfsxpxahipryr'
        pattern = 'xpxah'
        expected = [1, 2, 10, 17, 18, 19, 25, 26, 27, 36, 37, 38, 46, 47, 48]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_242(self):
        text = 'hlhebpthlhexklqthqhesgihlheedfqhlhece'
        pattern = 'hlhe'
        expected = [1, 2, 7, 8, 9, 17, 23, 24, 25, 31, 32, 33]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_243(self):
        text = 'mpguvxrpyvxpguvxmlamlguvxvywgmpguvxsdsmspguvxnutmpguvxpfjgwh'
        pattern = 'mpguvx'
        expected = [1, 2, 11, 12, 20, 29, 30, 31, 39, 40, 41, 48, 49, 50]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_244(self):
        text = 'hzqdxmneochzqkmxsvthzcmxiyhzqmxubayzqmxcfdm'
        pattern = 'hzqmx'
        expected = [1, 11, 20, 26, 27, 28, 35, 36]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_245(self):
        text = 'cjstsvaxxwbcjstsacswwcjstsayttnfcjstsavqxsr'
        pattern = 'cjstsav'
        expected = [1, 12, 22, 32, 33, 34]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_246(self):
        text = 'jrnqipyjynqylclyjsnqqpjynwporvqjynqztbaynqeoelf'
        pattern = 'jynq'
        expected = [1, 7, 8, 9, 17, 23, 31, 32, 33, 39, 40]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_247(self):
        text = 'uqjtvcfyqsbqjvchnwuqjvcshlksuqjlcgpguqjvcanzwp'
        pattern = 'uqjvc'
        expected = [1, 11, 12, 18, 19, 20, 29, 36, 37, 38]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_248(self):
        text = 'ukgwfmvvunkgwfnbbukgwfmvzukgwfhoibl'
        pattern = 'ukgwf'
        expected = [1, 2, 9, 10, 11, 17, 18, 19, 25, 26, 27]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_249(self):
        text = 'hqwxqkgwcihqwxbgstjhqywxyschqwixwscumqwxltxhqwxrn'
        pattern = 'hqwx'
        expected = [1, 2, 10, 11, 12, 20, 28, 37, 38, 43, 44, 45]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_250(self):
        text = 'jgcrhjoucxynjgcrhjollqhgcrhjoljtejjgcrhjolkfjrjgcrhsjolmvkq'
        pattern = 'jgcrhjol'
        expected = [1, 12, 13, 14, 23, 24, 34, 35, 36, 47]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_251(self):
        text = 'iarvuqvzteoarvuqqzixmiarvuqqzscigrvuqqzpmqln'
        pattern = 'iarvuqqz'
        expected = [1, 11, 12, 21, 22, 23, 32]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_252(self):
        text = 'ogqfhpfhwtogqefipfursqogqfipftjymogffipfmvicyogqfjpfkqs'
        pattern = 'ogqfipf'
        expected = [1, 11, 22, 23, 24, 34, 46]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_253(self):
        text = 'iidmsmjnidmsmgxeubidmsmymrlidmsmjhiyidmsmcpdl'
        pattern = 'idmsm'
        expected = [1, 2, 3, 8, 9, 10, 18, 19, 20, 27, 28, 29, 36, 37, 38]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_254(self):
        text = 'yksombzdyyksimjdgpyksimzyvyksimhzxfyksimnunyksimnvh'
        pattern = 'yksim'
        expected = [1, 9, 10, 11, 18, 19, 20, 26, 27, 28, 35, 36, 37, 43, 44, 45]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_255(self):
        text = 'fhaadppzdfhaadgbjsrfhaadxsbhaadpmoufuaadglz'
        pattern = 'fhaad'
        expected = [1, 2, 9, 10, 11, 19, 20, 21, 27, 28, 36]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_256(self):
        text = 'wktxghaawktxghnxvnwktxghhtpwktxghyawptxghsawktxglhodzhxwktxghlpy'
        pattern = 'wktxgh'
        expected = [1, 2, 8, 9, 10, 18, 19, 20, 27, 28, 29, 36, 44, 55, 56, 57]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_257(self):
        text = 'jtukgjrxytjukgjruiojdjukgjrxrsnbjwukgjrxzifqjukgjrzxtmrnjukgfjrxyztle'
        pattern = 'jukgjrx'
        expected = [1, 2, 3, 11, 21, 22, 23, 33, 34, 35, 45, 57]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_258(self):
        text = 'udqmivsamkuqqminvsjlaluqqmivsnveuuqmivsylszuqqmivsxguqqmqivswhyyuqqmivdspn'
        pattern = 'uqqmivs'
        expected = [1, 11, 22, 23, 24, 33, 34, 43, 44, 45, 53, 65]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_259(self):
        text = 'witzumwydufwitzumwylknwitzumwybbwitzutwyxyszawitzamwywyhwitzumwycwtdq'
        pattern = 'witzumwy'
        expected = [1, 2, 11, 12, 13, 22, 23, 24, 33, 46, 56, 57, 58]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_260(self):
        text = 'khrtgebdyypkhrtgebdmrvkhrtgebdvsskhrtgebdkomqiekhrtgebdokqrnkhrtdgebdmcakhrtgebdhrb'
        pattern = 'khrtgebd'
        expected = [1, 2, 11, 12, 13, 22, 23, 24, 33, 34, 35, 47, 48, 49, 61, 72, 73, 74]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_261(self):
        text = 'pqmjtqmolqvbphqmjtqmolcslepqrmjtqmoxcpqmjtaqmovwstpqmjtqgorfrspqmjtqmoktlpqmjtqmohsdko'
        pattern = 'pqmjtqmo'
        expected = [1, 2, 13, 14, 15, 27, 38, 51, 62, 63, 64, 73, 74, 75]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_262(self):
        text = 'yjgdieqmbyjgdxfqhvlyjgdxtbeqyjgdxdwzz'
        pattern = 'yjgdx'
        expected = [1, 9, 10, 11, 19, 20, 21, 28, 29, 30]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_263(self):
        text = 'mmbwtnjtmwqmmbwtnjtepdximbwtnjtnuambmbwtnjtaxoefmmbwtnjtcychmmbwtnjtzkxmmbwtdjtwuz'
        pattern = 'mmbwtnjt'
        expected = [1, 2, 11, 12, 13, 24, 25, 35, 36, 37, 48, 49, 50, 60, 61, 62, 72]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_264(self):
        text = 'mcnhiiagsjpsizmknhiiashzlhomcnhiiaskhkmcnhiiasgv'
        pattern = 'mcnhiias'
        expected = [1, 15, 27, 28, 29, 38, 39, 40]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_265(self):
        text = 'cjxvbnwmccjxvbnpecjxvobnqymcjxvbntyx'
        pattern = 'cjxvbn'
        expected = [1, 2, 9, 10, 11, 18, 27, 28, 29]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_266(self):
        text = 'ovbtaiwqvobgtaipvobtagkrovodbtazyvobnaelunvobhtajnpkx'
        pattern = 'vobta'
        expected = [1, 2, 9, 16, 17, 18, 26, 34, 43]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_267(self):
        text = 'gggjzsxggjkxucggogjzwngggjntgdggjpefgggjfbd'
        pattern = 'gggj'
        expected = [1, 2, 7, 8, 15, 16, 22, 23, 24, 29, 30, 31, 36, 37, 38]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_268(self):
        text = 'sjdypgyampjdlzwipesjulzwabxsjdlrnsjdlyzp'
        pattern = 'sjdl'
        expected = [1, 10, 11, 19, 27, 28, 29, 33, 34, 35]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_269(self):
        text = 'ycifkgcmycoifyrhkywifmmzycifgcmfu'
        pattern = 'ycif'
        expected = [1, 2, 9, 18, 24, 25, 26]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_270(self):
        text = 'nhckjhqrjcnhcikjhyaozhfhckjhsamnhckjhhznhcdjhyunhckjhhiui'
        pattern = 'nhckjh'
        expected = [1, 2, 11, 23, 24, 31, 32, 33, 40, 47, 48, 49]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_271(self):
        text = 'hiduswrixcashiduswiplhiduswigyrhiduswiggxw'
        pattern = 'hiduswi'
        expected = [1, 12, 13, 14, 21, 22, 23, 31, 32, 33]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_272(self):
        text = 'yjwgajfghvyjwgajfcuksiujwgajfajsyjwgajfuufi'
        pattern = 'yjwgajf'
        expected = [1, 2, 10, 11, 12, 23, 24, 32, 33, 34]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_273(self):
        text = 'czxkwrsivczokfrjelgzokwrbpjgirczokwrwjgdd'
        pattern = 'czokwr'
        expected = [1, 10, 19, 20, 30, 31, 32]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_274(self):
        text = 'elytejrielqtftqlqtyuixeylqtzafelqtkunelqtlgp'
        pattern = 'elqt'
        expected = [1, 8, 9, 10, 15, 16, 23, 24, 25, 30, 31, 32, 37, 38, 39]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_275(self):
        text = 'zbnsuhdrnavzbnsuhjdknqzbnquhdsrzbnsuhdrhlbezbnsuvdqt'
        pattern = 'zbnsuhd'
        expected = [1, 2, 12, 23, 31, 32, 33, 44]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_276(self):
        text = 'rorhrwnoaolrorkrwoadmerorhrwoabpryitorhrwoaancrorhrwoamulxl'
        pattern = 'rorhrwoa'
        expected = [1, 12, 22, 23, 24, 36, 37, 46, 47, 48]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_277(self):
        text = 'piaoeszpifaoeyrvpiaoeeaziaoebzpqaoehxypiaoeqxbapigaoerld'
        pattern = 'piaoe'
        expected = [1, 2, 8, 16, 17, 18, 24, 25, 31, 38, 39, 40, 48]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_278(self):
        text = 'omigroryilygkomigroryzmomigrorythheyomigrozrylmyromuigroryxrroemigroryqwlctomigroryea'
        pattern = 'omigrory'
        expected = [1, 2, 13, 14, 15, 23, 24, 25, 37, 50, 62, 63, 64, 75, 76, 77]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_279(self):
        text = 'roubtpmihylrouctpeqmlroubtphfrouebtpuwroubtpki'
        pattern = 'roubtp'
        expected = [1, 2, 12, 21, 22, 23, 30, 38, 39, 40]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_280(self):
        text = 'bjvjmfcjbjvjuxhmbjvfvnbjvjnppbbjvvjxypezbjvjoxdmh'
        pattern = 'bjvj'
        expected = [1, 2, 8, 9, 10, 17, 22, 23, 24, 31, 40, 41, 42]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_281(self):
        text = 'olkkcexzzapxvlkkcexlhbtaxvlkkcexmtsoqnvlkkcexoacvlkkcexfjyvlkkcnexvyivvlkkcexli'
        pattern = 'vlkkcex'
        expected = [1, 2, 12, 13, 14, 25, 26, 27, 38, 39, 40, 48, 49, 50, 59, 70, 71, 72]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_282(self):
        text = 'tcbsypggzsttcmbsyggsrjptcbsyggjutcbsyggxltcbseggrrox'
        pattern = 'tcbsygg'
        expected = [1, 12, 23, 24, 25, 32, 33, 34, 42]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_283(self):
        text = 'lukmpiprmluapipsdkhlukspipaernlukpipjpbdlukpiphilukxpipgwjt'
        pattern = 'lukpip'
        expected = [1, 10, 20, 30, 31, 32, 40, 41, 42, 49]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_284(self):
        text = 'dqpgofrhkedppgofiszjdqpgofavdqigofvbvar'
        pattern = 'dqpgof'
        expected = [1, 2, 11, 20, 21, 22, 29]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_285(self):
        text = 'etamewfejzqetamewfeametamewfefgabetamewfexzetamewfetsxhk'
        pattern = 'etamewfe'
        expected = [1, 2, 11, 12, 13, 21, 22, 23, 33, 34, 35, 43, 44, 45]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_286(self):
        text = 'maoylrhbaoylrdwoaoylsnxhaoyqrefcmaoylrzggaoyurczaaoylrsx'
        pattern = 'aoylr'
        expected = [1, 2, 3, 8, 9, 10, 17, 25, 33, 34, 35, 42, 49, 50, 51]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_287(self):
        text = 'rxykwvxsrrxykdwvbxwrxykwthvvqrxykwciirxykwvxz'
        pattern = 'rxykwv'
        expected = [1, 2, 10, 20, 30, 37, 38, 39]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_288(self):
        text = 'gehddzggesdtztehdzopzmehdqxgehduujgehdkwesgehdfkl'
        pattern = 'gehd'
        expected = [1, 2, 8, 14, 15, 22, 23, 27, 28, 29, 34, 35, 36, 42, 43, 44]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_289(self):
        text = 'frwlqjkncfewlwqfrwlfepcefrjlpaofrwlpmgqsfrwwlaatpufrwltag'
        pattern = 'frwl'
        expected = [1, 2, 10, 15, 16, 17, 25, 31, 32, 33, 41, 50, 51, 52]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_290(self):
        text = 'jhhavuztdmjhhavrzibrjhhavrzllsjhhavrzgtzjjhhavrzjphfijhhavrzoonw'
        pattern = 'jhhavrz'
        expected = [1, 10, 11, 12, 20, 21, 22, 30, 31, 32, 41, 42, 43, 53, 54, 55]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_291(self):
        text = 'ohmqqszomqqxivzmoomqqseomqgqayomvqqayomqqumxokmqqnnvim'
        pattern = 'omqq'
        expected = [1, 2, 3, 7, 8, 9, 17, 18, 19, 24, 31, 37, 38, 39, 45, 46, 47]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_292(self):
        text = 'mptwqjhbnzqmptwbjhbskukfmptwbjhbccomptwbjhbvj'
        pattern = 'mptwbjhb'
        expected = [1, 11, 12, 13, 24, 25, 26, 35, 36, 37]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_293(self):
        text = 'xsaagbzrwxjaaxdmixsaapnrlqxsbaaczxsuaaarwptxyaaeyxed'
        pattern = 'xsaa'
        expected = [1, 2, 10, 17, 18, 19, 27, 34, 44]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_294(self):
        text = 'soqzffzoaskjskozffzfcmtsozffzvisozffrukvsozffzokpsoczffztdwer'
        pattern = 'sozffz'
        expected = [1, 13, 14, 15, 23, 24, 25, 32, 40, 41, 42, 50]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_295(self):
        text = 'dyvzviwyadyzvigseydyzvicelvdyzvieashdysvipcdzzvicn'
        pattern = 'dyzvi'
        expected = [1, 9, 10, 11, 18, 19, 20, 27, 28, 29, 37, 44]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_296(self):
        text = 'vdfsazbxvjfovdfsazbkvnvdfsazbjvvdfstazbmqvdfsazbylke'
        pattern = 'vdfsazb'
        expected = [1, 2, 12, 13, 14, 22, 23, 24, 32, 41, 42, 43]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_297(self):
        text = 'xyempwysvoglxyempwysqlotzxyempwysztqdxyempwysjpxyempwytsiygpdxyexpwyspty'
        pattern = 'xyempwys'
        expected = [1, 2, 12, 13, 14, 25, 26, 27, 37, 38, 39, 48, 62]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_298(self):
        text = 'bqzrgaaeoqbbqzrmasejfbqzrgaseaiibqzrgasehmril'
        pattern = 'bqzrgase'
        expected = [1, 12, 21, 22, 23, 32, 33, 34]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_299(self):
        text = 'dipxjjlbripxacriopxrbripxdshoteripxarriplazeripxkm'
        pattern = 'ripx'
        expected = [1, 2, 8, 9, 10, 15, 21, 22, 23, 31, 32, 33, 38, 44, 45, 46]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_300(self):
        text = 'jvvscqsehjvsnqshbksnvvsnqslmpkjvvsnqspvmojvvsnqsaaygejvvsnqsrgyajjvvsnqsiklyd'
        pattern = 'jvvsnqs'
        expected = [1, 10, 20, 21, 30, 31, 32, 41, 42, 43, 53, 54, 55, 65, 66, 67]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_301(self):
        text = 'wqbrtmmoktwqbrjautwqbrtxszwqwbrtplo'
        pattern = 'wqbrt'
        expected = [1, 2, 11, 18, 19, 20, 27, 28, 29]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_302(self):
        text = 'ttxuosemwachtwxuolsedwyitwxuoseuztwxuosehhthctwxuoseshombtwxuoselvfutwcxuoselaker'
        pattern = 'twxuose'
        expected = [1, 2, 13, 24, 25, 26, 33, 34, 35, 45, 46, 47, 57, 58, 59, 69]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_303(self):
        text = 'otrswyeqiototrswkwrvvotzrswpwqgotrsvwcweotrswzgj'
        pattern = 'otrsw'
        expected = [1, 2, 11, 12, 13, 22, 32, 40, 41, 42]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_304(self):
        text = 'prgmcntfylhanprgmcntfkubiprgmcntfnabwfoprgmcntfrksprgwcntfjuxk'
        pattern = 'prgmcntf'
        expected = [1, 2, 13, 14, 15, 25, 26, 27, 39, 40, 41, 51]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_305(self):
        text = 'gtfpcqcgtypupbgvfpvogtfpjbgkfpiqgtfphwe'
        pattern = 'gtfp'
        expected = [1, 2, 8, 15, 20, 21, 22, 27, 32, 33, 34]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_306(self):
        text = 'jczapgjkjczapgwujlczapgzbfjcvzapgkru'
        pattern = 'jczapg'
        expected = [1, 2, 8, 9, 10, 17, 18, 19, 27]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_307(self):
        text = 'ngxlpdqmngxlcpddxngulpdonjdhngjxlpdayngsxlpdlgos'
        pattern = 'ngxlpd'
        expected = [1, 2, 9, 18, 29, 38]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_308(self):
        text = 'wglznxmapwdlznxhuwdlznxpccwdlzpxpmfwdlznxbksa'
        pattern = 'wdlznx'
        expected = [1, 9, 10, 11, 17, 18, 19, 27, 35, 36, 37]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_309(self):
        text = 'itjvdemugdyitjvdemujslitjvdemulhitjvdemubj'
        pattern = 'itjvdemu'
        expected = [1, 2, 11, 12, 13, 22, 23, 24, 32, 33, 34]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_310(self):
        text = 'grvmktnirymkzsjirvmkpnofirvmkpyjgvirvmkvgxqj'
        pattern = 'irvmk'
        expected = [1, 2, 8, 15, 16, 17, 24, 25, 26, 34, 35, 36]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_311(self):
        text = 'rsrldfmersrjlwyrsrkacaarsrlsmruwrsrlamhu'
        pattern = 'rsrl'
        expected = [1, 2, 9, 16, 23, 24, 25, 32, 33, 34]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_312(self):
        text = 'coivmsncftdcoivmspmigchivmsdgqchcoivmsjycoivmswtw'
        pattern = 'coivms'
        expected = [1, 2, 11, 12, 13, 22, 32, 33, 34, 40, 41, 42]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_313(self):
        text = 'cogxxwvoqsqvcogxxweoppzpacogxdweoaitzncogxfweofnhkicogxxweoiieicogxxweoddssrcopgxxweopd'
        pattern = 'cogxxweo'
        expected = [1, 12, 13, 14, 26, 39, 51, 52, 53, 63, 64, 65, 77]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_314(self):
        text = 'fkshhbpfdmpfksehbqzfuwfksehbspovfksehbfotfpsehbycfksehabhofksehbrfmf'
        pattern = 'fksehb'
        expected = [1, 11, 12, 13, 22, 23, 24, 32, 33, 34, 42, 50, 58, 59, 60]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_315(self):
        text = 'qpjypicbzzpjypizeulzapjypiqyxhtzpjypigkkzpjyvpiep'
        pattern = 'zpjypi'
        expected = [1, 2, 9, 10, 11, 20, 21, 22, 31, 32, 33, 41]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_316(self):
        text = 'vuygnnqbffviuygnnqbfkxuygnynqbfhqovmuyngnqbfrjulgnnqbfhoek'
        pattern = 'uygnnqbf'
        expected = [1, 2, 3, 12, 13, 14, 23, 37, 47]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_317(self):
        text = 'pyjbzicpjyjniyoypyjnzmpyjncxpyjnomopmjnxudqypyjnsw'
        pattern = 'pyjn'
        expected = [1, 8, 9, 10, 16, 17, 18, 22, 23, 24, 28, 29, 30, 36, 44, 45, 46]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_318(self):
        text = 'frxvuaejkevofrxvuaejycfifrxvuaeilrfbxvuaejhmfrxvuaejcufrxvuaejfskzfrxvuaejqkong'
        pattern = 'frxvuaej'
        expected = [1, 2, 12, 13, 14, 25, 35, 44, 45, 46, 54, 55, 56, 66, 67, 68]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_319(self):
        text = 'yxzkjphqjljayxzkjhhsayxzkjhboyxzkjhvdyhyxzkjhehiswyxzkjhhdiyxzkjhyckdb'
        pattern = 'yxzkjh'
        expected = [1, 12, 13, 14, 21, 22, 23, 29, 30, 31, 39, 40, 41, 50, 51, 52, 59, 60, 61]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_320(self):
        text = 'fapiwrzshfbpiwrzifnlfapiwizpywfapiwrzgrwrfzpiwrzgehwfapcwrzevxa'
        pattern = 'fapiwrz'
        expected = [1, 2, 10, 21, 30, 31, 32, 42, 53]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_321(self):
        text = 'ieovlubxglieolywpasieolbrcieolhubpqeolenrxfieolvlhty'
        pattern = 'ieol'
        expected = [1, 10, 11, 12, 19, 20, 21, 26, 27, 28, 35, 36, 43, 44, 45]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_322(self):
        text = 'cjbjjooyuxgcjbjooyuavcjbjooyubhtitcjfbjooyusccjbjooyumy'
        pattern = 'cjbjooyu'
        expected = [1, 11, 12, 13, 21, 22, 23, 35, 45, 46, 47]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_323(self):
        text = 'gyetrugyerpbojegyeeshogyerguqlgyertaqgyenbjrprgyerumrb'
        pattern = 'gyer'
        expected = [1, 6, 7, 8, 16, 22, 23, 24, 30, 31, 32, 38, 46, 47, 48]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_324(self):
        text = 'korhluvfhsnkorhluvxxqkorhluvdicskozrhluvofaz'
        pattern = 'korhluv'
        expected = [1, 2, 11, 12, 13, 21, 22, 23, 33]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_325(self):
        text = 'omlvyslixomjvyslcqvomlvysljovomlvyslijbxomlvyrlofntj'
        pattern = 'omlvysl'
        expected = [1, 2, 10, 19, 20, 21, 29, 30, 31, 41]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_326(self):
        text = 'abjmeitgxbfabjmeiwqhmabjmetijowbaabjmeivotfy'
        pattern = 'abjmei'
        expected = [1, 2, 11, 12, 13, 22, 33, 34, 35]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_327(self):
        text = 'rpgdgeaahirprdgyhjbrpgdgkdrpgqgzrerpgdguyynsdpgdgzdc'
        pattern = 'rpgdg'
        expected = [1, 2, 11, 19, 20, 21, 27, 34, 35, 36, 45, 46]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_328(self):
        text = 'yrnkyfxjlwrkyfxveyokyfxwzyrkyfxbqayrkyfngiupyrkyfxnzyrkyfxrsoyf'
        pattern = 'yrkyfx'
        expected = [1, 10, 11, 18, 25, 26, 27, 35, 44, 45, 46, 52, 53, 54]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_329(self):
        text = 'maafqjqgbmaaqjsrejcmacaqjkkplmbmaaqjrvmaaqjigqwmapaqjouz'
        pattern = 'maaqj'
        expected = [1, 9, 10, 11, 20, 31, 32, 33, 38, 39, 40, 48]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_330(self):
        text = 'opqtgubfvbpqtgngzbpqtgcfbpqtgywhyl'
        pattern = 'bpqtg'
        expected = [1, 2, 9, 10, 11, 17, 18, 19, 24, 25, 26]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_331(self):
        text = 'wzgwibcasqnfzzzgwibcafxzzgwibcbvbouzzgwibocapnzzgdwibcafizzmgwibcatok'
        pattern = 'zzgwibca'
        expected = [1, 2, 13, 14, 15, 24, 36, 47, 58, 59]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_332(self):
        text = 'rjiddhmikgjidwqrjidprrjidabrjiddcd'
        pattern = 'rjid'
        expected = [1, 2, 10, 11, 15, 16, 17, 21, 22, 23, 27, 28, 29]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_333(self):
        text = 'bmqnopleibmqnopfxloibmqnopljpwrrbmqnoplpccbmqhnoplsxsah'
        pattern = 'bmqnopl'
        expected = [1, 2, 10, 20, 21, 22, 32, 33, 34, 43]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_334(self):
        text = 'fnqgihsobjvfnggihmovxxkfnggihsoodzjfnggihsouzccxfnpgihsoopfi'
        pattern = 'fnggihso'
        expected = [1, 12, 23, 24, 25, 35, 36, 37, 49]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_335(self):
        text = 'lyoyvcxvhlyoyvcuwmlyqyvchhlyoyxvccsmtmlqoyvcdtefwyoyvcjxolyoyvcad'
        pattern = 'lyoyvc'
        expected = [1, 2, 9, 10, 11, 19, 27, 39, 49, 50, 57, 58, 59]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_336(self):
        text = 'jrbzvjyrjrbzvjjtzejrbzvjlhajrjzvjppd'
        pattern = 'jrbzvj'
        expected = [1, 2, 8, 9, 10, 18, 19, 20, 28]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_337(self):
        text = 'iiwwsljjyiiywsljspiiwwwljmeapiliwwsljeokipiwwsljctol'
        pattern = 'iiwwslj'
        expected = [1, 2, 10, 19, 30, 31, 32, 41, 42, 43]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_338(self):
        text = 'gvtfuovaoggvtvupxgvtvuqftgvtvuqusgvtvuukxgvtsvuxdccgvtvupm'
        pattern = 'gvtvu'
        expected = [1, 10, 11, 12, 17, 18, 19, 25, 26, 27, 33, 34, 35, 42, 51, 52, 53]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_339(self):
        text = 'axkpnorxmkaxkptdedauxkpykvdbaxkpepfoxkpqfrvyxkphx'
        pattern = 'axkp'
        expected = [1, 2, 10, 11, 12, 19, 20, 21, 28, 29, 30, 36, 37, 44, 45]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_340(self):
        text = 'rtqfcnnsvxqvrtqffcnoqbzpprtqfcnorwgrtqfcnxpec'
        pattern = 'rtqfcno'
        expected = [1, 13, 25, 26, 27, 36]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_341(self):
        text = 'rnarxbfdrnarkdyyrnxarpuwgrnarao'
        pattern = 'rnar'
        expected = [1, 2, 8, 9, 10, 17, 25, 26, 27]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_342(self):
        text = 'sfqojsaessfqojsgbujdzsfqojsvvssfqovsrsb'
        pattern = 'sfqojs'
        expected = [1, 2, 9, 10, 11, 21, 22, 23, 31]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_343(self):
        text = 'zilkubgtzzilkuimgzilklurmgrzislkuayezilkucgrrdzilkukiz'
        pattern = 'zilku'
        expected = [1, 2, 9, 10, 11, 18, 28, 36, 37, 38, 46, 47, 48]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_344(self):
        text = 'waxozdrebrtaxozdrebrlsaxozdroebqkpgvaxxzdrebrbaxozdrebmpaxozdrqebhhjaxozrebjc'
        pattern = 'axozdreb'
        expected = [1, 2, 3, 11, 12, 13, 23, 37, 46, 47, 48, 57, 69]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_345(self):
        text = 'uvfjrqtdwuvfjfqgbevvfjrqgcafhuvfnjrqggtauvfjrqgiramwuvajrqgccm'
        pattern = 'uvfjrqg'
        expected = [1, 10, 19, 20, 30, 40, 41, 42, 53]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_346(self):
        text = 'mncnyqtiqzmncnyqtincjmrcnyqtipahzhvmncnyqtidpdmemncnycqtizwmmncnyqoicxde'
        pattern = 'mncnyqti'
        expected = [1, 2, 10, 11, 12, 22, 35, 36, 37, 49, 61]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_347(self):
        text = 'zjdrgqoruolzjdrlquvueozjdtlqcozjdrlqokkwzbjdrlqjjrbdzjdrlqpf'
        pattern = 'zjdrlq'
        expected = [1, 11, 12, 13, 23, 30, 31, 32, 41, 42, 43, 52, 53, 54]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_348(self):
        text = 'rbffezidxrtbffesorbffewmqnrbffeowaurbffejzhp'
        pattern = 'rbffe'
        expected = [1, 2, 10, 11, 12, 17, 18, 19, 26, 27, 28, 35, 36, 37]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_349(self):
        text = 'uqibbsnjjsuqipsxtqkduqibsdsrrduqibsokuqibspd'
        pattern = 'uqibs'
        expected = [1, 11, 20, 21, 22, 30, 31, 32, 37, 38, 39]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_350(self):
        text = 'eejokxzbteejovklyvkeejoklnavbeejoklshzeejoklhcsaxeejoklaxejj'
        pattern = 'eejokl'
        expected = [1, 10, 19, 20, 21, 29, 30, 31, 38, 39, 40, 49, 50, 51]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_351(self):
        text = 'bvqwaskbvqwarsgevbmqwalgzbvqwoazpbvqpakua'
        pattern = 'bvqwa'
        expected = [1, 2, 7, 8, 9, 18, 26, 34]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_352(self):
        text = 'ahilzhmmqjarahilzhmteahilzhmtensahilzhmrecg'
        pattern = 'ahilzhm'
        expected = [1, 2, 12, 13, 14, 21, 22, 23, 32, 33, 34]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_353(self):
        text = 'niidibuyuxoniidtbuywriniidtibuyktvniidtbuywbkr'
        pattern = 'niidtbuy'
        expected = [1, 11, 12, 13, 23, 34, 35, 36]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_354(self):
        text = 'rbypcqzdairbypcqozrsypcqzgrrbypcqztcbvrbybcqzrgyvorbeypcqzoowykrbypacqzfyljj'
        pattern = 'rbypcqz'
        expected = [1, 2, 11, 19, 27, 28, 29, 39, 51, 64]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_355(self):
        text = 'rxdfdsjyhgjmrxdfdsjtyukrnrxdfvdstysmrxpfdstyfserxdfdstymgurydfdstykwxqxdfdstytjfb'
        pattern = 'rxdfdsty'
        expected = [1, 13, 26, 37, 47, 48, 49, 59, 70, 71]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_356(self):
        text = 'mpuncktlzmsunykljmhunckrpaohmsbunckqkmsinckqgjp'
        pattern = 'msunck'
        expected = [1, 10, 18, 29, 38]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_357(self):
        text = 'dynehlovdygehgsypsdiynehnojardynehatewdynqhnxdasdynehbzdynehvjk'
        pattern = 'dyneh'
        expected = [1, 2, 9, 19, 20, 21, 29, 30, 31, 39, 48, 49, 50, 55, 56, 57]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_358(self):
        text = 'nxnioiwulnfnioinwpwmoynfnioiwsvnfynioiwyaznfaioiwfyzi'
        pattern = 'nfnioiw'
        expected = [1, 10, 22, 23, 24, 32, 43]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_359(self):
        text = 'rfswoskslooirmswovsksoebrmswosksrermswtsksmrlormswosksmcvkrmswosksaektjrmswosksmnmbg'
        pattern = 'rmswosks'
        expected = [1, 13, 24, 25, 26, 35, 46, 47, 48, 58, 59, 60, 71, 72, 73]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_360(self):
        text = 'ixqbrjokweixqbjozqsloixqbjoulnwfixqbojoaxfiixqbjohi'
        pattern = 'ixqbjo'
        expected = [1, 10, 11, 12, 21, 22, 23, 33, 43, 44, 45]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_361(self):
        text = 'naqxsjjkjkaqxsvqaqmxsafjjaqxsmiqaqfsxxraqxsqwduxaqexseamq'
        pattern = 'aqxs'
        expected = [1, 2, 3, 10, 11, 12, 17, 25, 26, 27, 33, 39, 40, 41, 49]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_362(self):
        text = 'crasppoticraslqpijsmkcraslppokwcraslpupoym'
        pattern = 'craslpp'
        expected = [1, 10, 21, 22, 23, 32]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_363(self):
        text = 'ouxdeibgoouvxdeneaknouxdypszfouxdeabmaouxdeag'
        pattern = 'ouxde'
        expected = [1, 2, 10, 21, 29, 30, 31, 38, 39, 40]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_364(self):
        text = 'ghbfmdihghbmvvnghbmdsthjhbmdqeavf'
        pattern = 'ghbmd'
        expected = [1, 9, 15, 16, 17, 24, 25]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_365(self):
        text = 'zcoeeqsxzcobeogdozzcobemscqkzcobeccsoczcobeirzcobedlzcobefykwm'
        pattern = 'zcobe'
        expected = [1, 8, 9, 10, 18, 19, 20, 28, 29, 30, 38, 39, 40, 45, 46, 47, 52, 53, 54]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_366(self):
        text = 'shvtwnfqtgshvwnfcmshvwnfstyhosdhvwnfskvywshvwnfhscshvwnfqtshvwnfisns'
        pattern = 'shvwnf'
        expected = [1, 10, 11, 12, 18, 19, 20, 30, 31, 32, 41, 42, 43, 50, 51, 52, 58, 59, 60]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_367(self):
        text = 'ptduhfrjpkaptdhfrkzqptduhfrrpbfptduhfrgdptduhfrjfoptduhfriygptduhfrgqtla'
        pattern = 'ptduhfr'
        expected = [1, 2, 12, 20, 21, 22, 31, 32, 33, 40, 41, 42, 50, 51, 52, 60, 61, 62]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_368(self):
        text = 'grevmtaquetmsgrelvmtaugoeigrekvmtauedigrevmtauyazgxgrevmthutgggrovmtaugajktgrevmtaubnbu'
        pattern = 'grevmtau'
        expected = [1, 14, 27, 38, 39, 40, 52, 63, 75, 76, 77]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_369(self):
        text = 'vhxkbfiumvxvhxkbfidtevhxkbfimbvhxkbfidnavhxkffibdg'
        pattern = 'vhxkbfi'
        expected = [1, 2, 11, 12, 13, 21, 22, 23, 30, 31, 32, 41]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_370(self):
        text = 'pxrqgpoozypxrqgpowokkhpxrqgpoumapxrqgpowqht'
        pattern = 'pxrqgpo'
        expected = [1, 2, 10, 11, 12, 22, 23, 24, 32, 33, 34]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_371(self):
        text = 'lieukrqmkleukletleukrlkleujrvojleukjqpcwcleukrcixv'
        pattern = 'leukr'
        expected = [1, 2, 3, 10, 16, 17, 18, 24, 32, 41, 42, 43]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_372(self):
        text = 'ayolklhwaylkefpylkgkyiaylbkqtmcxaylkxcaylwkltu'
        pattern = 'aylk'
        expected = [1, 8, 9, 10, 15, 16, 23, 32, 33, 34, 39]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_373(self):
        text = 'gslkhooykttigsslkhoodsigslkhooerltxgsbkhoomylxgslkhoooidzgslkhoomlh'
        pattern = 'gslkhoo'
        expected = [1, 2, 13, 14, 15, 23, 24, 25, 36, 46, 47, 48, 57, 58, 59]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_374(self):
        text = 'hhdjqqgrhhdjcqaohhdjcqvdrmghhdjbcqvtdmjshdjcqizhzahhdjcxqlwhi'
        pattern = 'hhdjcq'
        expected = [1, 8, 9, 10, 16, 17, 18, 28, 40, 41, 51]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_375(self):
        text = 'pwhrfowfapahrdvpahtfpunppahrryqnpahrfqjahrlfpahrlyf'
        pattern = 'pahr'
        expected = [1, 9, 10, 11, 16, 24, 25, 26, 32, 33, 34, 39, 40, 44, 45, 46]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_376(self):
        text = 'hdhfttwphdhfttnqhvbhdhftztfdfhdhfttrtyghdhfttxedtz'
        pattern = 'hdhftt'
        expected = [1, 2, 8, 9, 10, 20, 29, 30, 31, 39, 40, 41]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_377(self):
        text = 'gvazmoydvugvazmoydrjatgvuzmoydhggvazmoydnerq'
        pattern = 'gvazmoyd'
        expected = [1, 2, 10, 11, 12, 23, 32, 33, 34]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_378(self):
        text = 'degcysonfqdebgcysmtccdebgcysjptdebgcyspuzfdebgcysfej'
        pattern = 'debgcys'
        expected = [1, 10, 11, 12, 21, 22, 23, 31, 32, 33, 42, 43, 44]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_379(self):
        text = 'pttlcyojympttlfluspttlodaqcpttlyiwupttlycdib'
        pattern = 'pttly'
        expected = [1, 11, 19, 27, 28, 29, 35, 36, 37]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_380(self):
        text = 'wcomebnpugwcomemqewcomefefsagwcymezrl'
        pattern = 'wcome'
        expected = [1, 2, 10, 11, 12, 18, 19, 20, 30]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_381(self):
        text = 'jeqwognamonyjnwognamubjqwognaugjqwognamhjqwogniazkl'
        pattern = 'jqwogna'
        expected = [1, 2, 3, 13, 22, 23, 24, 31, 32, 33, 41]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_382(self):
        text = 'tjgovexjsrtjgoovelmtkxtjgovehxgrtjgoveyrhtjgovehudnzhtjmgovemb'
        pattern = 'tjgove'
        expected = [1, 2, 11, 22, 23, 24, 32, 33, 34, 41, 42, 43, 54]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_383(self):
        text = 'rjkilwfttbrikilwwbnyprikilwdiirikilwjejcrihilwxbpyurikilwvjof'
        pattern = 'rikilw'
        expected = [1, 10, 11, 12, 21, 22, 23, 30, 31, 32, 41, 51, 52, 53]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_384(self):
        text = 'ynohltqhfihynoltqhfrnyynoltqhfpvynoltqhjfxkfxkynoltqhfwxkq'
        pattern = 'ynoltqhf'
        expected = [1, 11, 12, 13, 22, 23, 24, 33, 46, 47, 48]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_385(self):
        text = 'slzzvsbonolzzvsxxhjelzzvsspfqqolzzvsnaotlzzvsyiz'
        pattern = 'olzzvs'
        expected = [1, 2, 9, 10, 11, 20, 21, 30, 31, 32, 39, 40, 41]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_386(self):
        text = 'dycnutdaxgycnutabigycautblgycqnutuvtgycnurtnjobqbycnutar'
        pattern = 'gycnut'
        expected = [1, 2, 9, 10, 11, 19, 27, 37, 49, 50]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_387(self):
        text = 'lnfycyeeqkblnfycsqllnfyoqzxrlnfycqfoylnfycqecvlnfycqtcty'
        pattern = 'lnfycq'
        expected = [1, 12, 20, 28, 29, 30, 37, 38, 39, 46, 47, 48]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_388(self):
        text = 'yphnqicvyphnqkaazyyphnqizabbyphnqckpophnqzjdhvyphnoghvmz'
        pattern = 'yphnq'
        expected = [1, 2, 8, 9, 10, 18, 19, 20, 28, 29, 30, 37, 38, 47]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_389(self):
        text = 'utqfztuzqfkoyuzkfnlwuzqfsxpuzqfsedcuzuqfkurgfuqqfvlf'
        pattern = 'uzqf'
        expected = [1, 6, 7, 8, 14, 20, 21, 22, 27, 28, 29, 36, 37, 38, 46]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_390(self):
        text = 'dnnlruafqdwdnnlrafndbnnlrafmsvcdnmnlraflodnnlraftwksldnnlrafiunhdnnlrkafpkgt'
        pattern = 'dnnlraf'
        expected = [1, 11, 12, 13, 20, 21, 22, 32, 41, 42, 43, 53, 54, 55, 65]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_391(self):
        text = 'ptkshivzqysptdshivjgedpptkshifykptbkshivnvptkshicvykptkshivnxhkptkfshivyli'
        pattern = 'ptkshiv'
        expected = [1, 2, 12, 24, 33, 43, 52, 53, 54, 64]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_392(self):
        text = 'dhhzlkvrujmsadhhzlkvrpkdjhzlkvramzkdhhzlkvopxhlydhhzlkvruqpidhhzlkvrrbrhdhhzlkvrmyl'
        pattern = 'dhhzlkvr'
        expected = [1, 2, 13, 14, 15, 24, 36, 48, 49, 50, 60, 61, 62, 72, 73, 74]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_393(self):
        text = 'tshhmylwjcrcshhmylfjgsgcshhmylxcxcshhmyldfncshhmylejwfcshhmrylvdaa'
        pattern = 'cshhmyl'
        expected = [1, 2, 11, 12, 13, 23, 24, 25, 33, 34, 35, 43, 44, 45, 55]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_394(self):
        text = 'vanmivqtjvanvmiqvdyadvanmisqvbzcvanmiqvkzplsjanmiqvaicmvanmjiqvvchxsvanmidvrzp'
        pattern = 'vanmiqv'
        expected = [1, 10, 22, 32, 33, 34, 45, 46, 56, 69]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_395(self):
        text = 'hkaeshwubqmhkmeushwpqhkmesheakekmeshtrgdyhkmesfhvi'
        pattern = 'hkmesh'
        expected = [1, 12, 21, 22, 23, 31, 32, 42]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_396(self):
        text = 'zydzhbnvzqizhbwevzwqdzhbjmzqdzhbhwbtzqdzhbfsuw'
        pattern = 'zqdzhb'
        expected = [1, 9, 18, 19, 20, 26, 27, 28, 36, 37, 38]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_397(self):
        text = 'tmzmsuvtmmxsbpwsvatmmskgtmmsyotmeslbqtmmsfyyt'
        pattern = 'tmms'
        expected = [1, 8, 18, 19, 20, 24, 25, 26, 31, 37, 38, 39]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_398(self):
        text = 'hfymhrbnwrxwhfhymerbnwqwhymhrbanwbmgbhymhrbnwrm'
        pattern = 'hymhrbnw'
        expected = [1, 2, 3, 15, 25, 37, 38, 39]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_399(self):
        text = 'dbupxfmlldvuypxyygrxdvuppxtktfudvupxaindvupxmpdvupxcfdvupxyc'
        pattern = 'dvupx'
        expected = [1, 10, 21, 31, 32, 33, 39, 40, 41, 46, 47, 48, 53, 54, 55]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_400(self):
        text = 'sugfgsyugfgknojtugfgnougfgtjykugfgkuudfugfggyli'
        pattern = 'ugfg'
        expected = [1, 2, 3, 7, 8, 9, 16, 17, 18, 22, 23, 24, 30, 31, 32, 39, 40, 41]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_401(self):
        text = 'kwpcmeayuxqwkdpcmezayknhoykdpcyeaykrrnkdpcmceaygcjsp'
        pattern = 'kdpcmeay'
        expected = [1, 13, 27, 39]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_402(self):
        text = 'cxfaqicixcdcxfadqiciebcxfalqicieizlcxfaqitiyjfedcxfaqiciphccxfaqvciakrqc'
        pattern = 'cxfaqici'
        expected = [1, 2, 12, 23, 36, 48, 49, 50, 60]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_403(self):
        text = 'aqhhpwaqhphrkaqhhodgjyaqhhdwpr'
        pattern = 'aqhh'
        expected = [1, 2, 7, 13, 14, 15, 22, 23, 24]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_404(self):
        text = 'iowasxbxiowasklbeoxasxltsowasbuodowaswsowatsleeowasfufsb'
        pattern = 'owas'
        expected = [1, 2, 3, 9, 10, 11, 18, 25, 26, 27, 33, 34, 35, 40, 47, 48, 49]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_405(self):
        text = 'shhbkkkkshzsbtxsmshzblghshzbbpvshzbrrpshzbfashzbbks'
        pattern = 'shzb'
        expected = [1, 9, 17, 18, 19, 24, 25, 26, 31, 32, 33, 38, 39, 40, 44, 45, 46]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_406(self):
        text = 'lemysebxhsleysesgknlemysesblshxlemysesxzlamysesyvallpmysesomwi'
        pattern = 'lemyses'
        expected = [1, 11, 19, 20, 21, 31, 32, 33, 41, 52]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_407(self):
        text = 'vzdlywktesgvzsdlywfticinyvzdlywyftsjnqvzdlywftqpnvzdeywftqsvzdlywftwtmovzndlywftuq'
        pattern = 'vzdlywft'
        expected = [1, 12, 26, 38, 39, 40, 50, 59, 60, 61, 72]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_408(self):
        text = 'mvtivhmiqemvtirvfvctmvtvixvkcwmdtivfgzpmvtivjg'
        pattern = 'mvtiv'
        expected = [1, 2, 11, 21, 31, 39, 40, 41]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_409(self):
        text = 'pjtbpplnfpjtpbigrrpmtppbtjnpjtlzwwnrpjtjkjtcpjtpnwbi'
        pattern = 'pjtp'
        expected = [1, 9, 10, 11, 19, 28, 37, 44, 45, 46]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_410(self):
        text = 'ktfnmpmvvsqdktfnmmvwoktfnlmmvgbktfnmmvntaktfnmmvaoseo'
        pattern = 'ktfnmmv'
        expected = [1, 12, 13, 14, 22, 31, 32, 33, 41, 42, 43]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_411(self):
        text = 'hwmljkmkgfhwmljkmkoeyuhwmljkmkvmgwwhwmljkmkexshwmljkmkrvmhwmljkmkxpk'
        pattern = 'hwmljkmk'
        expected = [1, 2, 10, 11, 12, 22, 23, 24, 35, 36, 37, 46, 47, 48, 57, 58, 59]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_412(self):
        text = 'zmzznwjumzlmzznofoezmzznimzmoznflrzmzhndkfdlzmzzinrgzmyzznrob'
        pattern = 'zmzzn'
        expected = [1, 2, 10, 11, 12, 19, 20, 21, 27, 35, 45, 53]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_413(self):
        text = 'aztlktbtkltrsoaziktbtkhkdpqazlktbtkoyazlktbtkiuetazlwtbtkaouobazlktbtkqzabazlbtbtkswrk'
        pattern = 'azlktbtk'
        expected = [1, 15, 27, 28, 29, 37, 38, 39, 50, 62, 63, 64, 75]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_414(self):
        text = 'whststjrowhsptstjwcwhjststjlgwwhytstjbssawhrtstjgk'
        pattern = 'whststj'
        expected = [1, 2, 10, 20, 31, 42]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_415(self):
        text = 'csktbdmxccsktbdgxyrdcsktbdgginjvcsktbddqxcskobdhmfcsklbdrzbcsktbdwgle'
        pattern = 'csktbd'
        expected = [1, 2, 9, 10, 11, 20, 21, 22, 32, 33, 34, 42, 51, 59, 60, 61]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_416(self):
        text = 'hgmxhnjkwohgmbhlnjqmvdhgmbgnjgthgmbhndjmzshgmbhnjoacpxhgmbghnjakt'
        pattern = 'hgmbhnj'
        expected = [1, 11, 23, 32, 42, 43, 44, 55]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_417(self):
        text = 'emtsbbkvcetsbbkwfkqqetsbbkmiqxetvbbkdp'
        pattern = 'etsbbk'
        expected = [1, 2, 3, 9, 10, 11, 20, 21, 22, 31]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_418(self):
        text = 'lxzlszlxlzcxtvlxlzkaalxlzyu'
        pattern = 'lxlz'
        expected = [1, 6, 7, 8, 14, 15, 16, 21, 22, 23]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_419(self):
        text = 'ejrmqssxtsbjrmqspytbijrmqsstxvljrmqssylqjrmussxglrmqssdfwrc'
        pattern = 'jrmqss'
        expected = [1, 2, 3, 12, 21, 22, 23, 31, 32, 33, 41, 49, 50]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_420(self):
        text = 'viuhjklpviuhwvdcviuhlivixuhrjf'
        pattern = 'viuh'
        expected = [1, 2, 8, 9, 10, 16, 17, 18, 23]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_421(self):
        text = 'hearrhyahearrhokhearrhljzhearrheohearrhpqvxqheajrhkdiphearrhieyg'
        pattern = 'hearrh'
        expected = [1, 2, 8, 9, 10, 16, 17, 18, 25, 26, 27, 33, 34, 35, 45, 54, 55, 56]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_422(self):
        text = 'grabwoycangrabwoycgpdgrabwoyckvcgrabwoycttiv'
        pattern = 'grabwoyc'
        expected = [1, 2, 10, 11, 12, 21, 22, 23, 32, 33, 34]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_423(self):
        text = 'guwxjzmpgqvmgguwxjzfpgrpwiguwxjzpgrkxnguwxxjzpguozguwxjzpgalybguwxjzpojfviguwxjzpgunf'
        pattern = 'guwxjzpg'
        expected = [1, 14, 26, 27, 28, 39, 50, 51, 52, 63, 74, 75, 76]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_424(self):
        text = 'mkiojrtlmlkiojrwmmkiojrkemkiojaqlrmzmkiojxrtriemkisojryry'
        pattern = 'mkiojr'
        expected = [1, 2, 9, 10, 11, 17, 18, 19, 26, 37, 48]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_425(self):
        text = 'aqvkvzmvgaqvkqvzmslwzqagvkvzmigkkapvkvzmyoggmaqvkvzkmvcpob'
        pattern = 'aqvkvzm'
        expected = [1, 2, 10, 23, 34, 46]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_426(self):
        text = 'nyidpnzbhywvhnyipdnzbfhrtbnyidpnzbfjnyidpnzbehonyidpnzcbnd'
        pattern = 'nyidpnzb'
        expected = [1, 2, 14, 26, 27, 28, 36, 37, 38, 48]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_427(self):
        text = 'eajyhqjfneagleajyhjflkeajyfjfelbdeujyhjffieajchjfgyoeajyyjfsdefjyhjfamj'
        pattern = 'eajyhjf'
        expected = [1, 13, 14, 15, 23, 34, 43, 53, 62]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_428(self):
        text = 'hsnubjrfaphssubjrejssdhssubjrjjhdnhssubjrjdyhssubjrmcb'
        pattern = 'hssubjr'
        expected = [1, 10, 11, 12, 22, 23, 24, 34, 35, 36, 44, 45, 46]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_429(self):
        text = 'ayhvkmiysjayhvwjmcpayhwjmwtuicayhvjmvltpyhvjmaywy'
        pattern = 'ayhvjm'
        expected = [1, 11, 20, 30, 31, 32, 40, 41]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_430(self):
        text = 'mqlncjiicmlnkccogggmlnccsiqlmlncjfmyncjo'
        pattern = 'mlnc'
        expected = [1, 2, 3, 10, 19, 20, 21, 28, 29, 30, 35]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_431(self):
        text = 'plhxxwjxamaxycpuhxwjxavfzplhxwujxapxfpqplhxwjxawnyplhxwjxadwplhuxwjxaqkkrz'
        pattern = 'plhxwjxa'
        expected = [1, 15, 26, 39, 40, 41, 50, 51, 52, 61]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_432(self):
        text = 'optbttsjccoptbbtsjjeacpoptbttsjypoptbttsjtcbjoptvbttsjbdt'
        pattern = 'optbttsj'
        expected = [1, 2, 11, 23, 24, 25, 33, 34, 35, 46]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_433(self):
        text = 'owwnrlkggiowworkpevywwnrkmdzowwnrkxtowwnrkguownwrkux'
        pattern = 'owwnrk'
        expected = [1, 11, 20, 21, 28, 29, 30, 36, 37, 38, 45]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_434(self):
        text = 'piayfpdfcdzpiayfpdhzjwpiayfwpdfzitjpiayfpdgnepiayfpdjc'
        pattern = 'piayfpd'
        expected = [1, 2, 11, 12, 13, 23, 35, 36, 37, 45, 46, 47]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_435(self):
        text = 'gicjtlwlrqrgicjlttvadegicjlutngmvgicjaltbpsgicpltfxgicjltnmdl'
        pattern = 'gicjlt'
        expected = [1, 11, 12, 13, 23, 34, 44, 51, 52, 53]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_436(self):
        text = 'hqyzhseoehkbhyzhnsevuhyzhpevkhyzhsezzhyczhseqjhyzhhseypt'
        pattern = 'hyzhse'
        expected = [1, 2, 3, 13, 22, 29, 30, 31, 38, 47]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_437(self):
        text = 'nssgsbndbvqnsgsbnksrntvnsgbsbndlvrnsgsbnldhsnsgbsndrdensgsbnsbsvsdnsgsbdnefzrs'
        pattern = 'nsgsbnd'
        expected = [1, 2, 3, 12, 24, 35, 45, 55, 67]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_438(self):
        text = 'idplgxaikiplrcwcbiplgeyeiplgbjbugiplgcbiplglbiplyvzxji'
        pattern = 'iplg'
        expected = [1, 2, 3, 10, 17, 18, 19, 24, 25, 26, 33, 34, 35, 39, 40, 41, 46]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_439(self):
        text = 'giohnnnxxgiohnnnpldgiohnnwagbfgiohnnnmbil'
        pattern = 'giohnnn'
        expected = [1, 2, 9, 10, 11, 20, 30, 31, 32]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_440(self):
        text = 'jnbojyatxcecjnqbojyaqjdjnbojyamqyzjnbojyagdfijjnbojlajdujnbojyaxqdcojjnbojyazfcp'
        pattern = 'jnbojya'
        expected = [1, 2, 13, 23, 24, 25, 34, 35, 36, 47, 56, 57, 58, 69, 70, 71]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_441(self):
        text = 'pjqscdvwvpjpqscdvhizpqscdmyjoqscdpt'
        pattern = 'pqscd'
        expected = [1, 2, 3, 11, 12, 13, 20, 21, 22, 29, 30]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_442(self):
        text = 'ofkcawgnwofgkcawgoawafofkcawgnawjfkcawgwigovfkcawgirrpvofkcawgnisexofkctawgucsi'
        pattern = 'ofkcawg'
        expected = [1, 2, 10, 22, 23, 24, 33, 34, 43, 44, 45, 55, 56, 57, 68]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_443(self):
        text = 'fslfoayyrfslfoatdsgnfslfoamaibfmlfoazmnlfslfoaqze'
        pattern = 'fslfoa'
        expected = [1, 2, 9, 10, 11, 20, 21, 22, 31, 40, 41, 42]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_444(self):
        text = 'pbizmpdxjlfpbizmpdqpyzvpzizmpdxnkipbizepdrinlppbizmpdionznpbizmpdzghspoizmpddc'
        pattern = 'pbizmpd'
        expected = [1, 2, 11, 12, 13, 24, 35, 46, 47, 48, 58, 59, 60, 70]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_445(self):
        text = 'csesoinnnwcsesojwqucysesozglcsesoajdyvcsoesosrjd'
        pattern = 'cseso'
        expected = [1, 2, 10, 11, 12, 20, 21, 22, 28, 29, 30, 39]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_446(self):
        text = 'axwfbgiyeaxfbgijvbpynaxfbgiirgaxfbgqanoaxfggibhbnalxfbgiwvm'
        pattern = 'axfbgi'
        expected = [1, 9, 10, 11, 21, 22, 23, 31, 40, 50, 51, 52]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_447(self):
        text = 'qktildxzqkbigpguqkjtipntktidfqktngfksb'
        pattern = 'qkti'
        expected = [1, 2, 9, 17, 24, 25, 30]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_448(self):
        text = 'glqsxgglqpzgjglnqpycglqpplglqapam'
        pattern = 'glqp'
        expected = [1, 6, 7, 8, 14, 20, 21, 22, 27]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_449(self):
        text = 'tkgnyhxhokgnhznkgnzankgnoflbnkgntasnkgnsgyv'
        pattern = 'nkgn'
        expected = [1, 2, 9, 10, 14, 15, 16, 20, 21, 22, 28, 29, 30, 35, 36, 37]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_450(self):
        text = 'brokaquqybnrokaqughrbrokaquvmlwtbhokaqucrkbrokajuqorux'
        pattern = 'brokaqu'
        expected = [1, 2, 10, 11, 12, 20, 21, 22, 33, 43]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_451(self):
        text = 'quziddciypquzidoteknquaziddcxxbquzidewuequzidadtz'
        pattern = 'quzid'
        expected = [1, 2, 10, 11, 12, 21, 31, 32, 33, 40, 41, 42]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_452(self):
        text = 'ryvftyjtnjthryvftyjthuyryvftyjtmtkpnrykvftyjtxhryvftyjtrvaudryvftyjtfywsryvfpyjtollid'
        pattern = 'ryvftyjt'
        expected = [1, 2, 12, 13, 14, 23, 24, 25, 37, 47, 48, 49, 60, 61, 62, 73]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_453(self):
        text = 'izrorbjmbeeygpizrortmbppizrfrbmbzktizrorbmbwaeizgorbmbwfazrorbmbch'
        pattern = 'izrorbmb'
        expected = [1, 15, 25, 35, 36, 37, 47, 57, 58]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_454(self):
        text = 'vbwjoljitvqwnjbiqwevqwyuslovqwjirq'
        pattern = 'vqwj'
        expected = [1, 10, 20, 27, 28, 29]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_455(self):
        text = 'ocjouxjbgocdowznoqhovgvzaochour'
        pattern = 'ocho'
        expected = [1, 10, 17, 25, 26, 27]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_456(self):
        text = 'xizjalfxizcbaxfxizvjjvqkoxizvjgratlxizaammrxhzjxycxizjrko'
        pattern = 'xizj'
        expected = [1, 2, 8, 16, 26, 36, 44, 50, 51, 52]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_457(self):
        text = 'uwfyltcuwtflhlrcauwflfxbuwllgdw'
        pattern = 'uwfl'
        expected = [1, 8, 17, 18, 19, 25]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_458(self):
        text = 'zzihomlszzihqmihvzzihsymzzioguzzzihoraezzihrsh'
        pattern = 'zzih'
        expected = [1, 2, 8, 9, 10, 17, 18, 19, 25, 31, 32, 33, 39, 40, 41]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_459(self):
        text = 'iujrpmhiiujrpmzgciujrpvmpmaiujrpmsaiujrpmdlkfiujrlmamxekiujrfmdy'
        pattern = 'iujrpm'
        expected = [1, 2, 8, 9, 10, 18, 27, 28, 29, 35, 36, 37, 46, 57]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_460(self):
        text = 'wkjegmdewnyfwkjegmdwlyowkjegmdhomwqkjegmdvcnjp'
        pattern = 'wkjegmd'
        expected = [1, 2, 12, 13, 14, 23, 24, 25, 34, 35, 36]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_461(self):
        text = 'dyivvpqbokadyrvvpvqghrdyrxvvpqnhidyrvvpqhzttdyrvveqkudyrvvpqkdcdidyrvvpqlgin'
        pattern = 'dyrvvpq'
        expected = [1, 12, 23, 33, 34, 35, 45, 53, 54, 55, 65, 66, 67]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_462(self):
        text = 'dxjfncgrnyuneduefncgrrrmjsdujfnycgrkkntdujfncgron'
        pattern = 'dujfncgr'
        expected = [1, 14, 27, 39, 40, 41]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_463(self):
        text = 'rdnbdcrjxrirdnbdcmmraurdnbdctslprdncdcmhrfhrunbdcmqcbyordnbdcmguf'
        pattern = 'rdnbdcm'
        expected = [1, 11, 12, 13, 23, 33, 44, 55, 56, 57]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_464(self):
        text = 'azzyrpgxwqkazzmpgsecgazzrpqkbaazzrpgzdazerpgadeta'
        pattern = 'azzrpg'
        expected = [1, 12, 22, 30, 31, 32, 39]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_465(self):
        text = 'ayrmqwlcamqsbarmqmjatrmqqhdarmqxaabmqeynv'
        pattern = 'armq'
        expected = [1, 2, 3, 9, 13, 14, 15, 20, 21, 22, 27, 28, 29, 34]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_466(self):
        text = 'kdvcrfomdlbekdvcreokefexkdvcreootwkdvncreokfktvcreoubhkdvcreojzq'
        pattern = 'kdvcreo'
        expected = [1, 12, 13, 14, 24, 25, 26, 35, 45, 54, 55, 56]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_467(self):
        text = 'rffmhuerdnmonrfnmszzzrfngciudrfnmryrfrmifgrerfnmncu'
        pattern = 'rfnm'
        expected = [1, 8, 13, 14, 15, 22, 29, 30, 31, 36, 44, 45, 46]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_468(self):
        text = 'yssilzdoabnsdyssilzoatgloyssilzoxbuvwiyssilyoapqcqg'
        pattern = 'yssilzoa'
        expected = [1, 13, 14, 15, 26, 39]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_469(self):
        text = 'aenertuaenfwwegaenfcjaenfjjswaeefbevqqenfzfper'
        pattern = 'aenf'
        expected = [1, 7, 8, 9, 15, 16, 17, 21, 22, 23, 30, 38, 39]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_470(self):
        text = 'llgyiypdnilglgyiydcwndllgyiydqcfvllgyiydhhalgyiydstrsrwlgyiydkbnfxilgyiydgdyc'
        pattern = 'llgyiyd'
        expected = [1, 11, 12, 13, 22, 23, 24, 33, 34, 35, 43, 44, 55, 56, 67, 68]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_471(self):
        text = 'elchhnfulselchhlfuamulchhfueezjelchhfuzeexelchhfuuuelchhfjucoutmelchhfubpjj'
        pattern = 'elchhfu'
        expected = [1, 11, 21, 22, 31, 32, 33, 42, 43, 44, 52, 64, 65, 66]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_472(self):
        text = 'heywvxfzaheywvxtssdhedwvxgjceheywuvxyf'
        pattern = 'heywvx'
        expected = [1, 2, 9, 10, 11, 20, 30]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_473(self):
        text = 'xdquciycasxdqmciycsgqdvgdquciyctdzyxdqfciycqvied'
        pattern = 'xdquciyc'
        expected = [1, 2, 11, 24, 25, 36]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_474(self):
        text = 'fbspzpnfwbhpcpdfbhleffbhpawcrcfbhpkp'
        pattern = 'fbhp'
        expected = [1, 8, 9, 10, 16, 21, 22, 23, 30, 31, 32]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_475(self):
        text = 'ilpjbfdsgilpgbfncilpjbfmpilpjbfrrauqilpjbfkrgwp'
        pattern = 'ilpjbf'
        expected = [1, 2, 10, 17, 18, 19, 25, 26, 27, 36, 37, 38]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_476(self):
        text = 'jueafepljueafonrspsxjueaffildjueafztq'
        pattern = 'jueaf'
        expected = [1, 2, 8, 9, 10, 20, 21, 22, 29, 30, 31]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_477(self):
        text = 'yglzwezhiqsfygtlzwezhpyzyglowezhujgyylzwezhpyhyglzweuhcn'
        pattern = 'yglzwezh'
        expected = [1, 2, 13, 25, 36, 37, 47]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_478(self):
        text = 'sjdzjkxdjdrjhsddjdzjredjdzjszdwdjdsjgsdjdfjvkd'
        pattern = 'djdzj'
        expected = [1, 2, 8, 15, 16, 17, 22, 23, 24, 32, 39]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_479(self):
        text = 'ndmtbgqkiqcndmtbgqkhzjvxndmtbgqkfbytndrtbgqkwdlb'
        pattern = 'ndmtbgqk'
        expected = [1, 2, 11, 12, 13, 24, 25, 26, 37]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_480(self):
        text = 'jrnccaincwmjrncaicsdhkjrnccapicodwjrnccaicyoatjrnccaicfqii'
        pattern = 'jrnccaic'
        expected = [1, 12, 23, 34, 35, 36, 46, 47, 48]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_481(self):
        text = 'kwliqtnuvekwlkqndvkwlirtcnltwliqmikwliqjf'
        pattern = 'kwliq'
        expected = [1, 2, 11, 19, 28, 29, 34, 35, 36]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_482(self):
        text = 'nduxvcvmjqxnduxvavmhujlnduxvcvcrfnduuxvcvls'
        pattern = 'nduxvcv'
        expected = [1, 2, 12, 23, 24, 25, 34]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_483(self):
        text = 'ddwjrgcwhloddwjbgovsaddwtbgbqccaddwijbgezl'
        pattern = 'ddwjbg'
        expected = [1, 11, 12, 13, 22, 33]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_484(self):
        text = 'chsqzcugstchtsqjauwchsqvhpuchskxurgpchsqeyq'
        pattern = 'chsq'
        expected = [1, 2, 11, 19, 20, 21, 28, 36, 37, 38]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_485(self):
        text = 'gvlujqqlgvljqmpggvljitfvczgvljqpx'
        pattern = 'gvljq'
        expected = [1, 8, 9, 10, 17, 26, 27, 28]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_486(self):
        text = 'hsllabkfmmkhysllabwkwphsllabiwhsllabuzuzjfsllabghhdsllabatr'
        pattern = 'hsllab'
        expected = [1, 2, 12, 13, 14, 22, 23, 24, 30, 31, 32, 42, 43, 50, 51, 52]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_487(self):
        text = 'digorftdigoyowsdegovjdigooktkvdigovgh'
        pattern = 'digo'
        expected = [1, 2, 7, 8, 9, 16, 21, 22, 23, 30, 31, 32]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_488(self):
        text = 'lsmenozwyzylsnmenouumdvllsmenophncylomenokptghlsmenbmgdkwlsmpnovvfylsmenollgh'
        pattern = 'lsmeno'
        expected = [1, 2, 12, 24, 25, 26, 36, 47, 58, 67, 68, 69]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_489(self):
        text = 'zzmwxqdxqvxmzzwwxqdivwzzawxqdbuejjzzwwvqdftazazwwxqdyl'
        pattern = 'zzwwxqd'
        expected = [1, 12, 13, 14, 23, 35, 45, 46, 47]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_490(self):
        text = 'iagbvfafagbvzgpfagbhvvwgmfagbojynfagfvlfagbuwpyfagplve'
        pattern = 'fagb'
        expected = [1, 2, 7, 8, 9, 15, 16, 17, 25, 26, 27, 34, 39, 40, 41, 48]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_491(self):
        text = 'luvtauupeluvtaueyqluvtpauniujuluvsaukkjshluvytaurbjglsvtauip'
        pattern = 'luvtau'
        expected = [1, 2, 9, 10, 11, 19, 31, 42, 53]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_492(self):
        text = 'akjwxuqnbraktdxuqnhfvwuakjdxuqnjdhzakjdxuqnftiux'
        pattern = 'akjdxuqn'
        expected = [1, 11, 23, 24, 25, 35, 36, 37]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_493(self):
        text = 'oubmcqgkpfoublcgkrbjeloubmcgodbgubmcgkzyobubmcgktcdl'
        pattern = 'oubmcgk'
        expected = [1, 11, 23, 32, 33, 41, 42, 43]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_494(self):
        text = 'nioolnwcnvioolhdcnioollpnijoljqnioowlviniooanir'
        pattern = 'niool'
        expected = [1, 2, 9, 10, 11, 17, 18, 19, 25, 32, 40]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_495(self):
        text = 'ukearwrnsxtciukearwrahramgudearwrhsfzpukearwhhzhzlupearwrhhtv'
        pattern = 'ukearwrh'
        expected = [1, 14, 27, 39, 51]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_496(self):
        text = 'elkqthcounelkqtcoqfpelkqtcoaqelkttcoacnhrelkqtaoowewlkqtcoidpdqelkqtcozf'
        pattern = 'elkqtco'
        expected = [1, 10, 11, 12, 20, 21, 22, 30, 42, 51, 52, 53, 63, 64, 65]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_497(self):
        text = 'jrospglwizyrjzrospglsvpjrospglhebsdjrospglaexjrospglphkq'
        pattern = 'jrospgl'
        expected = [1, 2, 13, 14, 15, 23, 24, 25, 35, 36, 37, 45, 46, 47]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_498(self):
        text = 'jwlxunykyhbjwlxunykyngdbjwlxunykdagdgujwlxuyykhidjwglxunykwf'
        pattern = 'jwlxunyk'
        expected = [1, 2, 11, 12, 13, 24, 25, 26, 39, 50]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_499(self):
        text = 'qeeilixirlhqeeiliyrhgwzqleeilixrwhqeezilixrepqeeilixrfiul'
        pattern = 'qeeilixr'
        expected = [1, 12, 24, 25, 26, 35, 45, 46, 47]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_500(self):
        text = 'dzcxpxssetlczbdzcpxfssesfmztpzcpxsseladzcpxssueukxs'
        pattern = 'dzcpxsse'
        expected = [1, 15, 29, 30, 39]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_501(self):
        text = 'ffitywjimepzffiywheapofgiywavvffiywxtffiyzwqbjc'
        pattern = 'ffiyw'
        expected = [1, 12, 13, 14, 23, 30, 31, 32, 38]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_502(self):
        text = 'hxepfuszshxepfuonuqthxepfuzcpzmhxexfuuvuiihxepfujcqbhxepfufocg'
        pattern = 'hxepfu'
        expected = [1, 2, 9, 10, 11, 20, 21, 22, 32, 42, 43, 44, 52, 53, 54]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_503(self):
        text = 'umoqkvwjzpjdumoqtkvwjhhumoqkvwjqnrrcumoqkvwdhguoumoqkvwjabk'
        pattern = 'umoqkvwj'
        expected = [1, 2, 13, 23, 24, 25, 37, 48, 49, 50]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_504(self):
        text = 'fwpspljwzkffwpsljqynhfwpsljpnfwgsljua'
        pattern = 'fwpslj'
        expected = [1, 11, 12, 13, 21, 22, 23, 30]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_505(self):
        text = 'bmwnebfaitzeubmwnebarpsvhcbmnwebanhngbmwnebaygibjwnebawblbbmwlebarflzbmwnebacsc'
        pattern = 'bmwneba'
        expected = [1, 13, 14, 15, 27, 37, 38, 39, 48, 59, 69, 70, 71]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_506(self):
        text = 'fbzdcrzsptsffzdcrzsofqoqfzdjrzsvwldfzdcrfzsnsbygfzdcrzsdgssj'
        pattern = 'fzdcrzs'
        expected = [1, 2, 3, 12, 13, 14, 25, 36, 48, 49, 50]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_507(self):
        text = 'fijelljyfieetybfiemlloyfieesurhfieesxrxvfiheeeqdg'
        pattern = 'fiee'
        expected = [1, 8, 9, 10, 16, 23, 24, 25, 31, 32, 33, 41]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_508(self):
        text = 'akzpvqnrkakzpvonsrysadkzpvqnlmznkakzpcvqnfnnakzpvqnwdu'
        pattern = 'akzpvqn'
        expected = [1, 2, 10, 21, 22, 23, 34, 44, 45, 46]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_509(self):
        text = 'izejuqrjihenugoiihebjunaihqejuddetzihejualoi'
        pattern = 'iheju'
        expected = [1, 9, 17, 25, 35, 36, 37]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_510(self):
        text = 'lbwlbakmublbwbahzslrbwbardrmlbwpapelbwbaxnw'
        pattern = 'lbwba'
        expected = [1, 10, 11, 12, 19, 20, 21, 29, 35, 36, 37]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_511(self):
        text = 'mzdebyvbemndecamzdeqbxckavzdeaeumvdefx'
        pattern = 'mzde'
        expected = [1, 2, 10, 15, 16, 17, 26, 27, 33]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_512(self):
        text = 'ymgxmkhwlpvfmymgxmkgwerymgxmkhwzkmuymgxqmkhwnfdpaymgsxmkhwfcwpxymgxmkhwak'
        pattern = 'ymgxmkhw'
        expected = [1, 2, 14, 23, 24, 25, 36, 50, 63, 64, 65]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_513(self):
        text = 'zbaafjkrbaafjvenyhbaaqfjouilmbalafjii'
        pattern = 'baafj'
        expected = [1, 2, 3, 8, 9, 10, 19, 30]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_514(self):
        text = 'ohoqmiifxwbwohoqminftkoohoqmisifxkkfsohoqmiiaffvohokqmiifalxjpohoqsiifimiohoqmiiguroqu'
        pattern = 'ohoqmiif'
        expected = [1, 2, 13, 24, 38, 49, 63, 74]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_515(self):
        text = 'nhzebuknhzbkmytnhzboibenhzifnpynhzbqskor'
        pattern = 'nhzb'
        expected = [1, 7, 8, 9, 15, 16, 17, 24, 31, 32, 33]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_516(self):
        text = 'vlmxeonkrzmlmxeonvzvlmxeyonlhvlmmxeonbd'
        pattern = 'vlmxeon'
        expected = [1, 2, 11, 12, 20, 30]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_517(self):
        text = 'qipwzkuhrmqipwzkuhsmkhfqipwizkuhszukipwzkuhikfjqipwzkuhpuk'
        pattern = 'qipwzkuh'
        expected = [1, 2, 10, 11, 12, 24, 36, 37, 47, 48, 49]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_518(self):
        text = 'flnvsvpflnvspiflnvwsqhseflnvscuui'
        pattern = 'flnvs'
        expected = [1, 2, 7, 8, 9, 15, 24, 25, 26]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_519(self):
        text = 'hmpnvfwexhmpnvflyhhmpnvfrghlghmpnvfovsq'
        pattern = 'hmpnvf'
        expected = [1, 2, 9, 10, 11, 18, 19, 20, 29, 30, 31]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_520(self):
        text = 'bzbzgklxnqgbzbrgklbouxlbzwbrgklnekybzbrgkldfgol'
        pattern = 'bzbrgkl'
        expected = [1, 11, 12, 13, 24, 35, 36, 37]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_521(self):
        text = 'twdaysmsetgtwzdasmwifwdasmdfmhvwdasmmtwztwdajmtbtwdasmqmp'
        pattern = 'twdasm'
        expected = [1, 12, 21, 22, 31, 32, 41, 48, 49, 50]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_522(self):
        text = 'ziecbwljbwqziecblsywlxiecbwlyqnmiecbslneqqa'
        pattern = 'iecbwl'
        expected = [1, 2, 3, 13, 22, 23, 24, 33]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_523(self):
        text = 'rtikfxttikfdzfsstikfwkigytikftpeujetikfpuknbtikfbtr'
        pattern = 'tikf'
        expected = [1, 2, 3, 7, 8, 9, 16, 17, 18, 25, 26, 27, 35, 36, 37, 44, 45, 46]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_524(self):
        text = 'ticpgdezjtqccgdyvwqtqcpddlosbzsqcpgdjeuftbcpgdrmkjy'
        pattern = 'tqcpgd'
        expected = [1, 10, 20, 31, 32, 41]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_525(self):
        text = 'fxiitdnaafmlitnbhfzxlitbfgzlfxlgtsndu'
        pattern = 'fxlit'
        expected = [1, 10, 18, 19, 20, 29]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_526(self):
        text = 'dlxiycklvdneiimjjdnaiuuogopdnxixqzldnxibrprunxiwtmf'
        pattern = 'dnxi'
        expected = [1, 10, 18, 27, 28, 29, 35, 36, 37, 44, 45]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_527(self):
        text = 'zxgvnmlzbgvnhcezxgvntszdzxfvnuamnzxgvnwknzxsvnxbnzbgvnll'
        pattern = 'zxgvn'
        expected = [1, 2, 8, 15, 16, 17, 25, 33, 34, 35, 42, 50]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_528(self):
        text = 'dfedegjmsqgtgldededjmstvsmdedegjmscnukjdegegjmskbmdedegjswyp'
        pattern = 'dedegjms'
        expected = [1, 2, 3, 15, 26, 27, 28, 40, 51]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_529(self):
        text = 'ozfvrgpxeamozfvrgprfozfvrgpapuozfvkgpopdozfvrghpxxbsqozfvrghptqw'
        pattern = 'ozfvrgp'
        expected = [1, 2, 11, 12, 13, 20, 21, 22, 31, 41, 54]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_530(self):
        text = 'wldhmyesrwlhmbyegcszvwlcmyexucwlhmyoxkax'
        pattern = 'wlhmye'
        expected = [1, 10, 22, 31]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_531(self):
        text = 'bzwdqjkzzwdqcvohzwaqxszmdqxriazwdqnkzclzwdtfemzwdqzg'
        pattern = 'zwdq'
        expected = [1, 2, 3, 8, 9, 10, 17, 23, 30, 31, 32, 40, 46, 47, 48]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_532(self):
        text = 'xmpzqoaoqixmlpzqyzhkxmhnpzqntlexmnzqcbjxmypzqqpzxmnpzqdjodpxenpzqfoxa'
        pattern = 'xmnpzq'
        expected = [1, 11, 21, 32, 40, 48, 49, 50, 60]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_533(self):
        text = 'gzedgjfmxyoqzedljfzjeqzeidgjahjpgqzedgjzodhfqzedgjgngyiqzedgjukxo'
        pattern = 'qzedgj'
        expected = [1, 2, 12, 22, 33, 34, 35, 44, 45, 46, 55, 56, 57]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_534(self):
        text = 'dqtbnzlmsndqtbnzlxldqtbnzlplwktdqtbnzltoamx'
        pattern = 'dqtbnzl'
        expected = [1, 2, 10, 11, 12, 19, 20, 21, 31, 32, 33]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_535(self):
        text = 'nbnwlxuratvgbnwxxwnbnwxqqbocnvnwxyqyndnwxlxvj'
        pattern = 'nbnwx'
        expected = [1, 12, 13, 18, 19, 20, 29, 37]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_536(self):
        text = 'qarwndnlnqatwttqarwpdqarwbrqharwwfxaq'
        pattern = 'qarw'
        expected = [1, 2, 10, 15, 16, 17, 21, 22, 23, 28, 29, 30]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_537(self):
        text = 'ehjrfjwblzehjrfjhwbfrehjrmfjwblzuyehjrfjwbaclbsehjrgfjwbwpixfehjrfjwbvrpjx'
        pattern = 'ehjrfjwb'
        expected = [1, 2, 11, 22, 34, 35, 36, 48, 61, 62, 63]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_538(self):
        text = 'hcmtbqhmupphumtbqmktzumtbqrmwxahumtubqeyhumtbqzlkhumtoqhxdsh'
        pattern = 'humtbq'
        expected = [1, 11, 12, 13, 21, 22, 32, 40, 41, 42, 50]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_539(self):
        text = 'xkkdjpuvhxkdjqdmgtxkdjbhkvylixkdjmwcv'
        pattern = 'xkdj'
        expected = [1, 2, 3, 9, 10, 11, 18, 19, 20, 29, 30, 31]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_540(self):
        text = 'axixhlyqazaxhmcdloazibxhagnlazixhaw'
        pattern = 'azixh'
        expected = [1, 9, 19, 28, 29, 30]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_541(self):
        text = 'leolzapdogdleolmzapdjucleolzapdmbleolzzapdmyleolzapdecalq'
        pattern = 'leolzapd'
        expected = [1, 2, 12, 23, 24, 25, 34, 44, 45, 46]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_542(self):
        text = 'zlvdqmxcdyezlvdjmxcyfzlvdqmxcjfnfzlvdqxmxcgu'
        pattern = 'zlvdqmxc'
        expected = [1, 2, 12, 21, 22, 23, 34]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_543(self):
        text = 'colwlzsnhlcolwlusdzsrcolwlusclcolwluszewhcolwlusjkjh'
        pattern = 'colwlus'
        expected = [1, 10, 11, 12, 21, 22, 23, 30, 31, 32, 41, 42, 43]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_544(self):
        text = 'ylyednsbeylyednrxpylyedynvtzylyednwcxhykyednbjc'
        pattern = 'ylyedn'
        expected = [1, 2, 9, 10, 11, 19, 28, 29, 30, 39]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_545(self):
        text = 'ltjduilahxdyltynuilatjmpoltyduilafskltyduilawkoxjltyduilaawwxltydeuilaneltyduilljy'
        pattern = 'ltyduila'
        expected = [1, 13, 25, 26, 27, 36, 37, 38, 49, 50, 51, 62, 73]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_546(self):
        text = 'vlfikwhzjrrvlfkehxsjspvlfkwhhrtovlfkwhxdlz'
        pattern = 'vlfkwh'
        expected = [1, 12, 22, 23, 24, 32, 33, 34]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_547(self):
        text = 'qxvxyecfqxvxdipdqxvexypznwdqxvxxnqgvxgqoygqxvxcqpvbcqxvxczqe'
        pattern = 'qxvx'
        expected = [1, 2, 8, 9, 10, 17, 27, 28, 29, 34, 42, 43, 44, 52, 53, 54]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_548(self):
        text = 'hzkemnpyzxpaahzskemnptrnhzkemnppshzkemnpuyhzkemnpfzghzkemnpypkzg'
        pattern = 'hzkemnp'
        expected = [1, 2, 14, 24, 25, 26, 33, 34, 35, 42, 43, 44, 52, 53, 54]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_549(self):
        text = 'hktvhebheulghktvhpebbbbhhktvheblavxhktvhebjldhktvhebmbubzhktvheboghktvihebfmc'
        pattern = 'hktvheb'
        expected = [1, 2, 13, 24, 25, 26, 35, 36, 37, 45, 46, 47, 57, 58, 59, 67]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_550(self):
        text = 'fwivxlkbcztlwfwivlkbcqebtfwlivlkbczxcfwivlkbcorfvwivlkbcrgvii'
        pattern = 'fwivlkbc'
        expected = [1, 13, 14, 15, 26, 37, 38, 39, 48, 49, 50]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_551(self):
        text = 'arcelrmmpsarcelrzybruarcezlrmjcumwarcelrmyv'
        pattern = 'arcelrm'
        expected = [1, 2, 11, 22, 34, 35, 36]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_552(self):
        text = 'udjavsckeeviudjavscxgsudjauvscfkpzudjavscdcewo'
        pattern = 'udjavsc'
        expected = [1, 2, 12, 13, 14, 23, 34, 35, 36]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_553(self):
        text = 'ehvzjbucjzehvzjbucohzehvzjbukqoqniehvqzjbuchvvejvzjbucrwehvzjbucircrd'
        pattern = 'ehvzjbuc'
        expected = [1, 2, 10, 11, 12, 22, 35, 47, 56, 57, 58]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_554(self):
        text = 'gbbfjrhoxgbobfjeygbbfjdsgbbgkbfjqlozsgbbfjsxxfy'
        pattern = 'gbbfj'
        expected = [1, 2, 10, 17, 18, 19, 28, 37, 38, 39]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_555(self):
        text = 'porpdlyewporpdnlsqporpdliwtccporpdlsgcpokrpdlbhusporpdluqfefpcorpdlxwvt'
        pattern = 'porpdl'
        expected = [1, 2, 10, 18, 19, 20, 29, 30, 31, 39, 49, 50, 51, 61, 62, 63]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_556(self):
        text = 'hybfpekyrqqhybifpezjsiybfpbphybfpbt'
        pattern = 'hybfp'
        expected = [1, 2, 12, 22, 23, 28, 29, 30]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_557(self):
        text = 'vkowqmmisvkowqmmcrlqvvkowqqmmntvkowiqmmlxcvkowqmmjfdvkowhqmmefcuvkowqmmoqds'
        pattern = 'vkowqmm'
        expected = [1, 2, 9, 10, 11, 22, 32, 42, 43, 44, 53, 64, 65, 66]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_558(self):
        text = 'lbhldtwlbhldjbwflbhrdfklbbhldjamlbhldpq'
        pattern = 'lbhld'
        expected = [1, 2, 7, 8, 9, 17, 24, 25, 26, 32, 33, 34]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_559(self):
        text = 'qogjaomkspqogzaombcqhlqogzaomklyqogzavomkalve'
        pattern = 'qogzaomk'
        expected = [1, 11, 22, 23, 24, 33]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_560(self):
        text = 'ncntkktremhcntmkmnuhcndtkkpyyhcntkknubyhentkkfghhccntkkarldfecntkkccuwr'
        pattern = 'hcntkk'
        expected = [1, 2, 11, 20, 29, 30, 31, 40, 49, 50, 51, 61, 62]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_561(self):
        text = 'pfwgnkbwnyompugnkbzyutpfgknkbczkupfcnkbympfgcnkbtf'
        pattern = 'pfgnkb'
        expected = [1, 13, 23, 34, 42]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_562(self):
        text = 'yuofpbuviyijyuowpbuvjkkbyuowpbhvlmafyuowpbuvtjyugowpbuvein'
        pattern = 'yuowpbuv'
        expected = [1, 12, 13, 14, 25, 36, 37, 38, 47]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_563(self):
        text = 'kqlwklslfueklwklslflfvklwkljslfdkklwklslfwbyjklwklslfdu'
        pattern = 'klwklslf'
        expected = [1, 2, 3, 11, 12, 13, 23, 33, 34, 35, 45, 46, 47]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_564(self):
        text = 'ibyquhldzpibnquhwtnvmiibnquhquebnquhaqmitbnquhlx'
        pattern = 'ibnquh'
        expected = [1, 10, 11, 12, 22, 23, 24, 31, 32, 40, 41, 42]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_565(self):
        text = 'jmrahebrtmujvmrahebrmrdjmrahebrzqvmrahebrzdmjmrahebirxtjmrahebrsg'
        pattern = 'jmrahebr'
        expected = [1, 2, 12, 13, 14, 23, 24, 25, 34, 35, 45, 55, 56, 57]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_566(self):
        text = 'rxochcaidrfbuxochcawacuxchcaklxuxobhcaywz'
        pattern = 'uxochca'
        expected = [1, 2, 12, 13, 14, 23, 32]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_567(self):
        text = 'kxfmiwaojvtqkxfmiwanvkxfmuwalffxpkxfmiwawekxfmiwabxouz'
        pattern = 'kxfmiwa'
        expected = [1, 2, 12, 13, 14, 22, 33, 34, 35, 42, 43, 44]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_568(self):
        text = 'qwojbmazqwcwjbavlxqwjbavkurqwjbucbbdqwjbfosr'
        pattern = 'qwjb'
        expected = [1, 11, 12, 18, 19, 20, 27, 28, 29, 36, 37, 38]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_569(self):
        text = 'wpkiuuuleptwpkiumpitpwpkiuupqyfopkiuubsjghwpkiuuvkpay'
        pattern = 'wpkiuu'
        expected = [1, 2, 12, 21, 22, 23, 32, 33, 42, 43, 44]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_570(self):
        text = 'jbwnioiyjhbwniovvjbwniwokdijbwnzoveaqbjbwniypgjbwnpioge'
        pattern = 'jbwnio'
        expected = [1, 2, 9, 10, 11, 18, 28, 39, 47]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_571(self):
        text = 'faurmyofaurmmryfaurmhpfaurmaqyfnurmmrkfaurnmle'
        pattern = 'faurm'
        expected = [1, 2, 7, 8, 9, 15, 16, 17, 22, 23, 24, 31, 39]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_572(self):
        text = 'olpcmvvjqolpsmmoagolpcmrwudxnwlpcmgyyomlpcmjo'
        pattern = 'olpcm'
        expected = [1, 2, 10, 18, 19, 20, 30, 31, 38, 39, 40]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_573(self):
        text = 'tyytqjuxtytqkaldmtytqydtytqjfvhoytqokntytqoftz'
        pattern = 'tytq'
        expected = [1, 2, 3, 8, 9, 10, 17, 18, 19, 23, 24, 25, 32, 33, 38, 39, 40]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_574(self):
        text = 'idzotuupdidzozddimidzozmidzfofgvixdzofoodzodvqidzolii'
        pattern = 'idzo'
        expected = [1, 2, 9, 10, 11, 18, 19, 20, 25, 33, 34, 35, 40, 41, 46, 47, 48]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_575(self):
        text = 'ropwcgfpopwosmmxeponpwvzvljporwrpgbupnpwonlumpopjwdhsno'
        pattern = 'popw'
        expected = [1, 2, 7, 8, 9, 18, 28, 37, 46]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_576(self):
        text = 'dukfsejozcdukfsejovzdukfsewoefradukfsejovotzdukfiejotswwh'
        pattern = 'dukfsejo'
        expected = [1, 2, 10, 11, 12, 21, 32, 33, 34, 45]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_577(self):
        text = 'xdxiomakvyjbxjxiomakiqetxjxiomakdncixjxiomakal'
        pattern = 'xjxiomak'
        expected = [1, 12, 13, 14, 24, 25, 26, 36, 37, 38]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_578(self):
        text = 'wkuvyzcwkugtjlwykugyxzvgwkugycphe'
        pattern = 'wkugy'
        expected = [1, 8, 15, 16, 17, 24, 25, 26]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_579(self):
        text = 'vuejfxdzmwwvvuejfldzpwavuejrxdpejyyvuejfxdpahvuejfxdmhmivvuetjfxdqo'
        pattern = 'vuejfxd'
        expected = [1, 2, 13, 24, 35, 36, 37, 45, 46, 47, 58]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_580(self):
        text = 'qgvqyipdydhqgzqyfduqgzqyilmqgzqyiletvzqgzqyiczcwkqgzqkiuesn'
        pattern = 'qgzqyi'
        expected = [1, 12, 19, 20, 21, 27, 28, 29, 38, 39, 40, 50]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_581(self):
        text = 'zjfjasompbzjfjaorgtejfzjfjaorezjfjaopdazjfxaotmusqjfjaoyw'
        pattern = 'zjfjao'
        expected = [1, 10, 11, 12, 22, 23, 24, 30, 31, 32, 40, 50, 51]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_582(self):
        text = 'lhiojqlhirotjjlrhioleqlhioxmuxhlioqr'
        pattern = 'lhio'
        expected = [1, 2, 7, 15, 16, 17, 22, 23, 24, 31, 32]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_583(self):
        text = 'dycnvzikegdycnvziyyzdycnvzigkydycnvzicwtgdycnvziob'
        pattern = 'dycnvzi'
        expected = [1, 2, 10, 11, 12, 20, 21, 22, 30, 31, 32, 41, 42, 43]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_584(self):
        text = 'syqdegdljnsqdegdchpasqdegdjcxwxsqdigdpafsvqdegdonrncsqdegdejho'
        pattern = 'sqdegd'
        expected = [1, 2, 3, 10, 11, 12, 20, 21, 22, 32, 41, 42, 43, 52, 53, 54]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_585(self):
        text = 'heodyythebdhlnhebdwsuiqhebdcnchhtebdpk'
        pattern = 'hebd'
        expected = [1, 7, 8, 9, 14, 15, 16, 23, 24, 25, 32, 33, 34]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_586(self):
        text = 'znnajqeyznnanuzpnauslznnarcsgqznjnassphyzcnnaoouyv'
        pattern = 'znna'
        expected = [1, 2, 8, 9, 10, 15, 21, 22, 23, 31, 41, 42, 43]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_587(self):
        text = 'bsnckhmxbxncksxgwbsntkevbasnckvzpyqbznckzhbsnchgpvpv'
        pattern = 'bsnck'
        expected = [1, 2, 9, 18, 25, 26, 27, 36, 43]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_588(self):
        text = 'zfuhdxrozfcuhuxzfuhhnkkzfuhglbmtzfushrh'
        pattern = 'zfuh'
        expected = [1, 2, 9, 15, 16, 17, 23, 24, 25, 33]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_589(self):
        text = 'ljaipefvuqquljaipezmoindljaipeaykrfljaiperywgljaitemmqinljaiuenufhnljaipzrvu'
        pattern = 'ljaipe'
        expected = [1, 2, 12, 13, 14, 24, 25, 26, 35, 36, 37, 46, 57, 68]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_590(self):
        text = 'kcravwomkcdaalfkrkcdalhzeekcdablkcdalhqslkcdafh'
        pattern = 'kcda'
        expected = [1, 8, 9, 10, 17, 18, 19, 26, 27, 28, 32, 33, 34, 41, 42, 43]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_591(self):
        text = 'eifbfrotwrgefbfrmbwvefbfrtqpvyefbfrrxykyefbfrkntfqefbfrvbgeq'
        pattern = 'efbfr'
        expected = [1, 2, 3, 11, 12, 13, 20, 21, 22, 30, 31, 32, 40, 41, 42, 50, 51, 52]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_592(self):
        text = 'ksbrotxwnksroqpksromnjksroopwjksrohucksroptex'
        pattern = 'ksro'
        expected = [1, 9, 10, 11, 15, 16, 17, 22, 23, 24, 30, 31, 32, 37, 38, 39]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_593(self):
        text = 'coikncnelrzoiknvnfwzoikxcnafzoikncpnnvzoikncnfsif'
        pattern = 'zoikncn'
        expected = [1, 2, 11, 20, 29, 38, 39, 40]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_594(self):
        text = 'uckhohgdlcrfzuckhohgdwquckhjhgdnhuckhoshgddduckhohgdiguckhohgdtf'
        pattern = 'uckhohgd'
        expected = [1, 2, 13, 14, 15, 24, 34, 44, 45, 46, 54, 55, 56]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_595(self):
        text = 'dzbyiwoqqdzbiewonajrdzrbiwotctedxbiwocx'
        pattern = 'dzbiwo'
        expected = [1, 10, 21, 32]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_596(self):
        text = 'onhriorgpxonhriorjnsgkyonhrirakidionhrfrshtfr'
        pattern = 'onhrir'
        expected = [1, 11, 23, 24, 25, 35]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_597(self):
        text = 'edpitpyhcedyioswdpilubodpiwhf'
        pattern = 'edpi'
        expected = [1, 2, 10, 16, 17, 23, 24]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_598(self):
        text = 'enfrpagafeuenfpagaguenfpagwlmenfpaganyjqe'
        pattern = 'enfpaga'
        expected = [1, 11, 12, 13, 21, 29, 30, 31]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_599(self):
        text = 'apvyvgtrdapvyvqcokapvyvvnqpzmapvcyvetzmapvyvnjrladvyvjhw'
        pattern = 'apvyv'
        expected = [1, 2, 9, 10, 11, 18, 19, 20, 30, 39, 40, 41, 49]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_600(self):
        text = 'omnrfxlkkomnrxfxwhkuomnrfxwynjohmnrfxlfomnrfgpdr'
        pattern = 'omnrfx'
        expected = [1, 2, 10, 20, 21, 22, 31, 32, 33, 40]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_601(self):
        text = 'rhkqidyickmhrhkqidyiszzrhkqidymixrhkqidypijxjrhkqidyisvlrhkhidyiihj'
        pattern = 'rhkqidyi'
        expected = [1, 2, 12, 13, 14, 24, 34, 45, 46, 47, 57]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_602(self):
        text = 'gfrwlsydnzcmkgfrwlsyndxgfrwlvsynwrafrwlsynxhoh'
        pattern = 'gfrwlsyn'
        expected = [1, 13, 14, 15, 24, 35, 36]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_603(self):
        text = 'yaqftcayaqyfldpzgyaqxfevuaqyfaglsiaqyfwdsyaqyfdyqyaiyfemir'
        pattern = 'yaqyf'
        expected = [1, 7, 8, 9, 18, 25, 26, 34, 35, 41, 42, 43, 50]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_604(self):
        text = 'wexwvzwwxwvdqvwxwwvnpjwxwvwvliwxwrdzoxtwxxwvuzixi'
        pattern = 'wxwv'
        expected = [1, 2, 3, 7, 8, 9, 15, 16, 17, 22, 23, 24, 25, 31, 40, 41, 42]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_605(self):
        text = 'hdaodupylhlaoxtephlaowfaxnuhlaoqutx'
        pattern = 'hlao'
        expected = [1, 9, 10, 11, 17, 18, 19, 27, 28, 29]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_606(self):
        text = 'gjciywtnfblgvciywanpkndgvuiywtneegvciywtnuogvciqwtnrwpui'
        pattern = 'gvciywtn'
        expected = [1, 12, 24, 33, 34, 35, 44]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_607(self):
        text = 'bucveqyrvbucveqygaobucueqyuoppbucveqaroyabucveqyul'
        pattern = 'bucveqy'
        expected = [1, 2, 9, 10, 11, 20, 31, 41, 42, 43]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_608(self):
        text = 'rflsbtsnrflbstivtyrflbstbqrflbstjuambrflbstmomdo'
        pattern = 'rflbst'
        expected = [1, 8, 9, 10, 18, 19, 20, 26, 27, 28, 37, 38, 39]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_609(self):
        text = 'arqrtxgccpvarqqtxxvzarqqtxpfarqqtxsygarqqtxipouznarqqtxmewg'
        pattern = 'arqqtx'
        expected = [1, 11, 12, 13, 20, 21, 22, 28, 29, 30, 37, 38, 39, 49, 50, 51]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_610(self):
        text = 'jzypqejqbgipndjzypqjqbcuoysjzypqujqbfwfjzypqjqbiphhagjzypqjqobjtzvjzybpqjqbgtjzypqjqbpe'
        pattern = 'jzypqjqb'
        expected = [1, 14, 15, 16, 28, 39, 40, 41, 54, 67, 77, 78, 79]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_611(self):
        text = 'xhcvpbzgfmpextcvgbzbxywxtcvpbzwgxtcvpzsulzrxtcvpbzfn'
        pattern = 'xtcvpbz'
        expected = [1, 13, 23, 24, 25, 33, 43, 44, 45]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_612(self):
        text = 'mengkliqmeznswgmeznzcmezntycmezknrv'
        pattern = 'mezn'
        expected = [1, 8, 9, 10, 15, 16, 17, 21, 22, 23, 29]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_613(self):
        text = 'ncoynstnnwoygognwodfjnnwoyswnuwoyspnwoyampeg'
        pattern = 'nwoy'
        expected = [1, 8, 9, 10, 16, 22, 23, 24, 29, 30, 31, 35, 36, 37]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_614(self):
        text = 'rwmmpjkhkfjrwmmpjkhporwmmpjkhjndrwmmpjkhzprrwrwmmpjkhvgq'
        pattern = 'rwmmpjkh'
        expected = [1, 2, 11, 12, 13, 21, 22, 23, 32, 33, 34, 45, 46, 47]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_615(self):
        text = 'zkbbsxfnugzkbbsxyntpczkbbsxfnfwyzkbbsxfniizkbbsxfnwrzkbbsxfnerfzkbbsxfnen'
        pattern = 'zkbbsxfn'
        expected = [1, 2, 11, 21, 22, 23, 32, 33, 34, 42, 43, 44, 52, 53, 54, 63, 64, 65]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_616(self):
        text = 'rkkkrpyqpxnvrkkkrpbquyibrkklrpyqwprkkkrpyqfdjqrkkkrfyqkjnnrkkkrpyqce'
        pattern = 'rkkkrpyq'
        expected = [1, 2, 13, 25, 34, 35, 36, 47, 58, 59, 60]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_617(self):
        text = 'qrlzrgeeoureqrlmdgeejihyqrlymrgeezpnqrlmrgeeklqremrgeeuslqrlmrgeeypiqrlmrgeezwyo'
        pattern = 'qrlmrgee'
        expected = [1, 13, 25, 36, 37, 38, 47, 57, 58, 59, 68, 69, 70]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_618(self):
        text = 'ixudehrlrfixudehrufwixudehnfpxlixwdehdqixudehmcdixudehifixudeooinb'
        pattern = 'ixudeh'
        expected = [1, 2, 10, 11, 12, 20, 21, 22, 32, 39, 40, 41, 48, 49, 50, 57]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_619(self):
        text = 'boyxlcumboyqmahuhboyqkmkmzbowyqjixoyqqtuxboyqymlbm'
        pattern = 'boyq'
        expected = [1, 8, 9, 10, 17, 18, 19, 27, 34, 35, 41, 42, 43]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_620(self):
        text = 'szhvlqeaeszxvlhdrjszvlsvpgszwvlgbg'
        pattern = 'szvl'
        expected = [1, 10, 18, 19, 20, 27]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_621(self):
        text = 'ygxbbtchxygxqbqctzkxblgxqbtckeygxqbtctwmwygxqbtcuzxbygxqbtchoygxxqbtcjnkr'
        pattern = 'ygxqbtc'
        expected = [1, 10, 22, 23, 30, 31, 32, 41, 42, 43, 52, 53, 54, 62]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_622(self):
        text = 'qsmfmisvqglpsmfmxxxmfjqsmfmxrrhpqsmufmxmraqsmfmxljv'
        pattern = 'qsmfmx'
        expected = [1, 12, 13, 22, 23, 24, 33, 42, 43, 44]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_623(self):
        text = 'qdvdwgkjmplquvdqgoudqdvdmgxdqddvdqgxbdsqdvdqogetma'
        pattern = 'qdvdqg'
        expected = [1, 12, 21, 29, 30, 31, 40]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_624(self):
        text = 'csiwvvkvqsiwynseiccsiwyafevxcsiwyygcsiwyumdfcsiwynhccsiwynv'
        pattern = 'csiwy'
        expected = [1, 9, 10, 18, 19, 20, 28, 29, 30, 35, 36, 37, 44, 45, 46, 52, 53, 54]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_625(self):
        text = 'lcxllpqylvxnldjcllnxlaemhvxlgbjp'
        pattern = 'lvxl'
        expected = [1, 9, 18, 25, 26]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_626(self):
        text = 'klusmqeoklrusrkuwikrlusnystklusilcb'
        pattern = 'klus'
        expected = [1, 2, 9, 19, 20, 21, 27, 28, 29]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_627(self):
        text = 'iaolzfowaogedaolfowabdguiaolfdowaktxiaolaowawpkciaolfowabdkiaolfowaoniauolfowaula'
        pattern = 'iaolfowa'
        expected = [1, 13, 14, 25, 37, 48, 49, 50, 59, 60, 61, 70]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_628(self):
        text = 'qpigcbrgrfxxqpigcbtpdaxqpigcbrxdadqpigcbrypipn'
        pattern = 'xqpigcbr'
        expected = [1, 12, 22, 23, 24, 34, 35]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_629(self):
        text = 'jmibrecqdexmibrwxxmibrrjbxmikbrnhisxmibrjnuxmibrvdykxmibzfozu'
        pattern = 'xmibr'
        expected = [1, 2, 10, 11, 12, 17, 18, 19, 26, 35, 36, 37, 43, 44, 45, 53]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_630(self):
        text = 'txbjjfkdtcxbjqmvxbjysbgztubjfarstxbjpewtxbjimutg'
        pattern = 'txbj'
        expected = [1, 2, 9, 10, 11, 16, 17, 25, 32, 33, 34, 39, 40, 41]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_631(self):
        text = 'dcmaugbbwndegtdmaugbbwujxdmaugxbwaueigdmaugzbbwgopl'
        pattern = 'dmaugbbw'
        expected = [1, 2, 3, 14, 15, 16, 26, 39]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_632(self):
        text = 'jexzaaejvjsjexzaaejnbujeyzaaejhqsjvexzaaejznjexzaaejkaksywjexzaaejnwhywjexzaaejhu'
        pattern = 'jexzaaej'
        expected = [1, 2, 11, 12, 13, 23, 34, 35, 36, 44, 45, 46, 58, 59, 60, 71, 72, 73]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_633(self):
        text = 'nfyelljptnfyelaljovnfayelljsdnfyelljnuwinfyellqya'
        pattern = 'nfyellj'
        expected = [1, 2, 10, 20, 29, 30, 31, 41]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_634(self):
        text = 'asoggjnsegxasoggjnslhasoggjvsnoxasoggjnsyevasoggjnsdkkasoggjnsmia'
        pattern = 'asoggjns'
        expected = [1, 2, 11, 12, 13, 22, 32, 33, 34, 43, 44, 45, 54, 55, 56]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_635(self):
        text = 'fztcafpgwztcawjygztcaanzfdztgcaaiztcawjdbzpcaemdh'
        pattern = 'ztca'
        expected = [1, 2, 3, 9, 10, 11, 17, 18, 19, 27, 33, 34, 35, 42]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_636(self):
        text = 'fkmwjffrkafumwjfrlxgfkmwjfrkdpfkmwjefrlrlycfgmwjfrsux'
        pattern = 'fkmwjfr'
        expected = [1, 11, 20, 21, 22, 31, 44]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_637(self):
        text = 'smiebikahpmiebiluqymiebiphkmiebidqrbmiebilfpmfiebiylg'
        pattern = 'miebi'
        expected = [1, 2, 3, 10, 11, 12, 19, 20, 21, 27, 28, 29, 36, 37, 38, 45, 46, 47]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_638(self):
        text = 'dmnwlwqzdmnilqlxdmnqwleedwidmnwlvx'
        pattern = 'dmnwl'
        expected = [1, 2, 9, 17, 27, 28, 29]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_639(self):
        text = 'kodxhncwxfkomxhmdenokodxhbuxzkodxkhexykkodxhzzplckodxhurfckodtxhtu'
        pattern = 'kodxh'
        expected = [1, 2, 11, 20, 21, 22, 30, 39, 40, 41, 49, 50, 51, 59]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_640(self):
        text = 'hkywvcanodkhywvcavxdzkhywvcamfmihkkhywvcanvndxtkhywvcankhiqm'
        pattern = 'khywvcan'
        expected = [1, 2, 11, 22, 34, 35, 36, 47, 48, 49]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_641(self):
        text = 'tqbtcdiojgqbtcdzwrqnvqztcdlzqbtcplw'
        pattern = 'qbtcd'
        expected = [1, 2, 3, 10, 11, 12, 22, 29]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_642(self):
        text = 'ulhoofezqunfulhoofezajzfmulhoffezcfeulhoofezyjefulhoofeznmiqulhoofqezvxxiulhzoofezcchqe'
        pattern = 'ulhoofez'
        expected = [1, 2, 12, 13, 14, 26, 36, 37, 38, 48, 49, 50, 61, 74]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_643(self):
        text = 'hhjvlaithejvmoxchhjvztehhjvrghhjvralqhjvvhrs'
        pattern = 'hhjv'
        expected = [1, 2, 9, 16, 17, 18, 23, 24, 25, 29, 30, 31, 37, 38]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_644(self):
        text = 'qafhgagqasfhrhaocqafhtkqafhkfqafhhwgof'
        pattern = 'qafh'
        expected = [1, 2, 8, 17, 18, 19, 23, 24, 25, 29, 30, 31]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_645(self):
        text = 'xeaxpopidncxeadpubxeaxpghzoxeaxpfyqaxeaxpbcldlkxeaxpdiq'
        pattern = 'xeaxp'
        expected = [1, 2, 12, 18, 19, 20, 27, 28, 29, 36, 37, 38, 47, 48, 49]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_646(self):
        text = 'mpkfjkamufempkfjzoudagmpkfjhvdxmpdkfjhcw'
        pattern = 'mpkfjh'
        expected = [1, 12, 22, 23, 24, 32]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_647(self):
        text = 'mfdhuihrqacmfdhuiphsgmfdhuiehgfagmfdhuihhyiwmfdhuihjal'
        pattern = 'mfdhuih'
        expected = [1, 2, 12, 22, 33, 34, 35, 44, 45, 46]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_648(self):
        text = 'jnhdjuynojnhdiutqtjnhdxcjnhdcwadjnhxmpbybjknhdvclinjnhdjv'
        pattern = 'jnhd'
        expected = [1, 2, 9, 10, 11, 18, 19, 20, 24, 25, 26, 33, 42, 43, 44, 51, 52, 53]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_649(self):
        text = 'kalbgmbqvrbkalcgmbqaqkalcgmgqwhkjkalhcgmbqzjzzgkalqcgmbqajkalcgmbqpgs'
        pattern = 'kalcgmbq'
        expected = [1, 11, 12, 13, 22, 34, 48, 58, 59, 60]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_650(self):
        text = 'aaybxnevoaaybxnmaaaybxnaqfaxaybxnqfaaybxnwneihkaaybxnltbeaaylxnki'
        pattern = 'aaybxn'
        expected = [1, 2, 9, 10, 11, 17, 18, 19, 27, 28, 29, 35, 36, 37, 47, 48, 49, 58]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_651(self):
        text = 'elxszzbfnhmhcelxszzbwfgpeoxszzbfalelxszfzbfqqelxtszzbffpelsxszzbfjmjzelxszzbftfvj'
        pattern = 'elxszzbf'
        expected = [1, 2, 14, 25, 35, 46, 57, 69, 70, 71]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_652(self):
        text = 'zxrigktwjyzxribktsvtazxxigktevbzxrigkxtjvszxrigktfwz'
        pattern = 'zxrigkt'
        expected = [1, 2, 11, 22, 32, 42, 43, 44]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_653(self):
        text = 'qxiuojpadqfiuoicqxiuwoonxsqxiluokjgkqtxiuoukfgqxiuoryxaeqxiuouj'
        pattern = 'qxiuo'
        expected = [1, 2, 10, 17, 27, 37, 38, 39, 46, 47, 48, 56, 57, 58]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_654(self):
        text = 'fvxmvcltfxxmvpdifxxmvgyfxxmgvbuedfaxxmvmpddfxxmvxflcqbfxxmvkr'
        pattern = 'fxxmv'
        expected = [1, 8, 9, 10, 16, 17, 18, 24, 34, 35, 36, 43, 44, 45, 54, 55, 56]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_655(self):
        text = 'nvrazporgvprauesgdrajbegvraqigvrwazcgxgevrauivtgvrakinp'
        pattern = 'gvra'
        expected = [1, 2, 9, 17, 23, 24, 25, 30, 39, 40, 41, 47, 48, 49]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_656(self):
        text = 'wpfbrdzngjkwpbrdzjhkchwpfbrdzksmpfbrdzpxiwpfbrhdzsjwpfbrdzedvgd'
        pattern = 'wpfbrdz'
        expected = [1, 2, 12, 22, 23, 24, 32, 33, 42, 51, 52, 53]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_657(self):
        text = 'bjjijuaxzebjiijubeocebjiijujcbjiinjuhfghe'
        pattern = 'bjiiju'
        expected = [1, 10, 11, 12, 21, 22, 23, 30]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_658(self):
        text = 'mfzajcwmfzaknygmfzakixmfzaalbdmfzuxgmfzpanlomfzsalpa'
        pattern = 'mfza'
        expected = [1, 2, 7, 8, 9, 15, 16, 17, 22, 23, 24, 31, 37, 45]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_659(self):
        text = 'ytzmlubjytzmcudkubyezmlukuyotzmluxbhytzmluacszytzmluqdsytzmluedl'
        pattern = 'ytzmlu'
        expected = [1, 2, 9, 19, 27, 28, 29, 36, 37, 38, 46, 47, 48, 55, 56, 57]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_660(self):
        text = 'cmmtukvvfxcmmtuskvnhukcmmtukvglbfgdmmtukvhjcmmtckvtpyxpcmmtukvuxrcmmetukvqzrci'
        pattern = 'cmmtukv'
        expected = [1, 2, 11, 22, 23, 24, 35, 36, 44, 55, 56, 57, 66]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_661(self):
        text = 'uqjbbnzacqjbqbpiquqjbwafheuqjbsueot'
        pattern = 'uqjb'
        expected = [1, 2, 9, 10, 17, 18, 19, 26, 27, 28]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_662(self):
        text = 'ilxumelynwdlilxumemigilxumedyhktlxumeyhgnbvilxumsyvmivxumeypjepilzumeymgr'
        pattern = 'ilxumey'
        expected = [1, 13, 22, 32, 33, 44, 53, 64]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_663(self):
        text = 'jqxzooatvihjqxzooaqbgujqxzooaqdmjqxzoogaqgurvjqxzooaqhljqxzooaqbrgjfjqxzoobquiio'
        pattern = 'jqxzooaq'
        expected = [1, 11, 12, 13, 22, 23, 24, 33, 45, 46, 47, 55, 56, 57, 69]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_664(self):
        text = 'lyghwwibqyflyghwibqyhlyghwibzgjtjzlyghwibwsypalyghwibsuclyghfibhrq'
        pattern = 'lyghwib'
        expected = [1, 11, 12, 13, 21, 22, 23, 34, 35, 36, 46, 47, 48, 57]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_665(self):
        text = 'nrrralmgsvnnrralzmgirntrralmgrannrralmgcvnnrrgalmgnnnkbnnrralmgqqnnrralmgdwvle'
        pattern = 'nnrralmg'
        expected = [1, 11, 22, 31, 32, 33, 42, 55, 56, 57, 65, 66, 67]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_666(self):
        text = 'dsxcrndyuaxcrndszeddxcondoyjmgdxccrndsodxcrndyz'
        pattern = 'dxcrnd'
        expected = [1, 2, 3, 10, 11, 20, 31, 39, 40, 41]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_667(self):
        text = 'snqtuhklnztuixpsnztugoxjsnntucubecsnztusz'
        pattern = 'snztu'
        expected = [1, 8, 9, 15, 16, 17, 25, 34, 35, 36]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_668(self):
        text = 'dprdbnitkqdrdritdnrdbjnxdrdbjhoj'
        pattern = 'drdb'
        expected = [1, 2, 3, 11, 17, 18, 19, 24, 25, 26]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_669(self):
        text = 'mmzwmczhiqrmmzwmcvgxmmzwmczhhmmzwmcvuvkmmzwamcbbaq'
        pattern = 'mmzwmc'
        expected = [1, 2, 11, 12, 13, 20, 21, 22, 29, 30, 31, 40]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_670(self):
        text = 'megvmlkeggvmocvgegvmvsvgvmtojufegvmgb'
        pattern = 'egvm'
        expected = [1, 2, 3, 8, 9, 10, 16, 17, 18, 23, 24, 31, 32, 33]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_671(self):
        text = 'ljnukqaqenlznukqaqgnuljnukqaqcjelwjnukqaqnktljnukqaqsr'
        pattern = 'ljnukqaq'
        expected = [1, 2, 11, 21, 22, 23, 33, 34, 35, 44, 45, 46]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_672(self):
        text = 'bgkasvprbgkavasybzgkairkbggafmydbgkavdegkayhibgtkaptgw'
        pattern = 'bgka'
        expected = [1, 2, 8, 9, 10, 17, 18, 19, 25, 32, 33, 34, 39, 40, 46]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_673(self):
        text = 'gclhtgwlxqvmgcmotgwbuhgiclotgwjiigslotgwatgclotfwrfrgclxotgwqyhggclotgywfaa'
        pattern = 'gclotgw'
        expected = [1, 13, 23, 24, 25, 34, 43, 53, 65]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_674(self):
        text = 'pmoowzukepmowwjzmdzpmowyfpmoxxdf'
        pattern = 'pmow'
        expected = [1, 9, 10, 11, 19, 20, 21, 26]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_675(self):
        text = 'xzwzzbkedsztxzzzbkexniqnxzzzbkedtxzzmzbkermixzzzbkexjlq'
        pattern = 'xzzzbke'
        expected = [1, 12, 13, 14, 24, 25, 26, 34, 44, 45, 46]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_676(self):
        text = 'lqrgoxxqglqrgoxxxklqrkoxxlotwglqrgnoxxzilqrgoxxnovrsqrgoxxtzpl'
        pattern = 'lqrgoxx'
        expected = [1, 2, 9, 10, 11, 19, 31, 40, 41, 42, 52, 53]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_677(self):
        text = 'aoujexfysscqaouaqexfyboaouaexfyrhvgouaexfydgfdaouaexvfyeevqlaouaexfyszndaohaexfyynjkl'
        pattern = 'aouaexfy'
        expected = [1, 13, 23, 24, 25, 35, 36, 47, 60, 61, 62, 73]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_678(self):
        text = 'eoevkrzfcmrkeovkrxceovkskeghteorkryuwrg'
        pattern = 'eovkr'
        expected = [1, 2, 3, 12, 13, 14, 20, 30]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_679(self):
        text = 'xnlkanxnlkcxswlxynlkhygxnlknbcgxxnlkazxxnlkcpt'
        pattern = 'xnlk'
        expected = [1, 2, 6, 7, 8, 16, 17, 18, 23, 24, 25, 32, 33, 34, 39, 40, 41]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_680(self):
        text = 'ttxwfgsyttaxwfbcqefttabxwfgzxzagttahwfgzkpgttarxwfgmud'
        pattern = 'ttaxwfg'
        expected = [1, 9, 20, 33, 44]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_681(self):
        text = 'uoipstvlvuoipstroluoipstrhkuoibstrrgu'
        pattern = 'uoipstr'
        expected = [1, 9, 10, 11, 18, 19, 20, 28]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_682(self):
        text = 'mmvaktdjcrvmmvapktkqetbmmvaktkqmmzaktycqmmvxktmlurj'
        pattern = 'mmvakt'
        expected = [1, 2, 12, 23, 24, 25, 32, 41]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_683(self):
        text = 'upavghqyhupaqgwphupaqgmwqxbupaqgxdrupaqgrtcz'
        pattern = 'upaqg'
        expected = [1, 9, 10, 11, 17, 18, 19, 27, 28, 29, 35, 36, 37]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_684(self):
        text = 'ppquamxxxpqummxkbjkpqiuamxwttxpquamxrsl'
        pattern = 'pquamx'
        expected = [1, 2, 3, 10, 20, 30, 31, 32]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_685(self):
        text = 'fowxisnbzgnzfoxisnxcvmxfoxisnvgnkfoxisntafoxisnoozfouxisnyec'
        pattern = 'foxisn'
        expected = [1, 12, 13, 14, 23, 24, 25, 33, 34, 35, 41, 42, 43, 51]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_686(self):
        text = 'hrpfpdthwpffuchwpfnfmrhwpmcuwpfdhvythwpfhlbslhcpfipfye'
        pattern = 'hwpf'
        expected = [1, 7, 8, 9, 14, 15, 16, 23, 28, 29, 36, 37, 38, 46]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_687(self):
        text = 'pvdxgakzdppvdxgakzjpclmpvdxgakbepvqkpvdxgakzxhmhvvdxgakzwpf'
        pattern = 'pvdxgakz'
        expected = [1, 2, 10, 11, 12, 24, 36, 37, 38, 49, 50]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_688(self):
        text = 'hlqzwgjycrhlqztgjswyuhlqyztgjnyhulqztgjxahlqztajoghxu'
        pattern = 'hlqztgj'
        expected = [1, 10, 11, 12, 22, 32, 33, 34, 42]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_689(self):
        text = 'rhhuabuoqlzrrkhuabuojhhxrhhuabuokkhjhhuabuonp'
        pattern = 'rhhuabuo'
        expected = [1, 2, 13, 24, 25, 26, 36, 37]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_690(self):
        text = 'abjlyphwfqkjgycbjyphwfrneabjyphwfxzgnabjyphxfktsdabjyphxfsalvambjyphwflwwabjyphwflvy'
        pattern = 'abjyphwf'
        expected = [1, 15, 16, 25, 26, 27, 38, 50, 62, 63, 64, 73, 74, 75]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_691(self):
        text = 'wcvvjuhwcvmvxrowcvvwwnpjwcvvrbuzwcuvvfsiiwcvvfsvwcvsvnis'
        pattern = 'wcvv'
        expected = [1, 2, 8, 15, 16, 17, 24, 25, 26, 33, 41, 42, 43, 49]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_692(self):
        text = 'nivetfunpnivteujqzdnzvtfuebfnivtfcuiebn'
        pattern = 'nivtfu'
        expected = [1, 10, 20, 29]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_693(self):
        text = 'jxjddpjxjhyawumjjxjhfrjsxjhgahrjxphikesxjxjxhxx'
        pattern = 'jxjh'
        expected = [1, 6, 7, 8, 16, 17, 18, 23, 24, 25, 32, 41, 43]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_694(self):
        text = 'pjqtvasxncepjqtvaxxocddpjitvaxskpgjqtvaxzupnjqtvaxbez'
        pattern = 'pjqtvax'
        expected = [1, 11, 12, 13, 24, 33, 34, 35, 43, 44, 45]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_695(self):
        text = 'bpcwnajfabpcwntjkdlubpecwnajougzobpcwnajmohcbpcwnvjswz'
        pattern = 'bpcwnaj'
        expected = [1, 2, 10, 21, 33, 34, 35, 45]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_696(self):
        text = 'kmheafzkmrevbikzheabkmhesrwkwmhelhqqhkmhjeirqp'
        pattern = 'kmhe'
        expected = [1, 2, 8, 15, 20, 21, 22, 28, 29, 30, 38]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_697(self):
        text = 'wdwtrsqgcfzgdwrsqhiywldwrsqbmwdwrsqtvrudwdwrsqqc'
        pattern = 'wdwrsq'
        expected = [1, 12, 13, 21, 22, 23, 29, 30, 31, 40, 41, 42]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_698(self):
        text = 'bpiolfifbpimlfbpabpiolfwrbppiolfcbrbpiolfeekbpiolfqqpobpiolfey'
        pattern = 'bpiolf'
        expected = [1, 2, 9, 17, 18, 19, 26, 27, 28, 35, 36, 37, 44, 45, 46, 54, 55, 56]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_699(self):
        text = 'hxisnknwbhxisjhhxsaptbhnislihxiupaborhxishzr'
        pattern = 'hxis'
        expected = [1, 2, 9, 10, 11, 16, 23, 29, 37, 38, 39]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_700(self):
        text = 'ehqsmqqwjehqsmqxdgeehpqsmqkvffhehqszmqdj'
        pattern = 'ehqsmq'
        expected = [1, 2, 9, 10, 11, 20, 32]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_701(self):
        text = 'elyylwzkuelixylhgeiheliyloicfuelyiluq'
        pattern = 'eliyl'
        expected = [1, 10, 20, 21, 22, 31]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_702(self):
        text = 'bqhoonyiubqhnoyswbqhoyycfhgbqhoytvhbqhoiyyzxzy'
        pattern = 'bqhoy'
        expected = [1, 10, 17, 18, 19, 27, 28, 29, 36]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_703(self):
        text = 'hqrqddwcahqrqdrchqrqdstozhfqrqdrnyhqrqdttzhqrqdkkaqhqrqdaokg'
        pattern = 'hqrqd'
        expected = [1, 2, 9, 10, 11, 16, 17, 18, 26, 27, 28, 34, 35, 36, 42, 43, 44, 51, 52, 53]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_704(self):
        text = 'icvekjcbujicvekjkbgoicvekjeblrqbicvekjkblgupicekjkbljq'
        pattern = 'icvekjkb'
        expected = [1, 10, 11, 12, 21, 32, 33, 34, 45]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_705(self):
        text = 'jhegsrqvvafajoegsrqbpecpjzegsrqymejoegsrqnhjjoegsrqcrpkd'
        pattern = 'joegsrq'
        expected = [1, 12, 13, 14, 25, 34, 35, 36, 44, 45, 46]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_706(self):
        text = 'hbmipzxcmhbmipgxcgehbmipxwyuijhbmipqprhbmipxdmq'
        pattern = 'hbmipx'
        expected = [1, 10, 19, 20, 21, 31, 38, 39, 40]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_707(self):
        text = 'dkwluztdkwluldumkwluybxydvwlufol'
        pattern = 'dkwlu'
        expected = [1, 2, 7, 8, 9, 16, 17, 25]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_708(self):
        text = 'hguafgtrootehguaftrovuhguqftrowjvchgumftroqoalxhgeaftrojx'
        pattern = 'hguaftro'
        expected = [1, 12, 13, 14, 23, 35, 48]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_709(self):
        text = 'zrmwdmxubuwqfzrmwdtxuvwvezrmwdatxuscdfazrmwdtdugjkzarmwdtxugsxzrmwdtyxujfzzrmwdtxuggkrs'
        pattern = 'zrmwdtxu'
        expected = [1, 13, 14, 15, 26, 40, 51, 52, 53, 63, 74, 75, 76]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_710(self):
        text = 'lxrqumyfcdzulxrpqumfyfjhlxrqumfyzavpilxrqumfymiomlxrqumfyjhmlxrzqumfyaasqy'
        pattern = 'lxrqumfy'
        expected = [1, 13, 24, 25, 26, 37, 38, 39, 49, 50, 51, 61]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_711(self):
        text = 'qunsvjkqtqunsvzvlqunvapnequntvgqkegqunsvwas'
        pattern = 'qunsv'
        expected = [1, 2, 9, 10, 11, 18, 26, 35, 36, 37]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_712(self):
        text = 'vsysxlhgwdvsysxlhgwmuvsysxlhgxagznvsysxlhgcfvsysxlhgkhaz'
        pattern = 'vsysxlhg'
        expected = [1, 2, 10, 11, 12, 21, 22, 23, 34, 35, 36, 44, 45, 46]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_713(self):
        text = 'pdmzwbkzhpdmzwbykpdmzlbvsxgdmzwbubfxhpdmzwbssqirpdmzwbavs'
        pattern = 'pdmzwb'
        expected = [1, 2, 9, 10, 11, 18, 27, 28, 37, 38, 39, 48, 49, 50]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_714(self):
        text = 'ixtxrfaaxixtxruavyuqwixtxrfayrwvixtxrfybrixtwxrfannej'
        pattern = 'ixtxrfa'
        expected = [1, 2, 10, 21, 22, 23, 33, 42]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_715(self):
        text = 'yrcgpwfbayrcggpwgfoodyrcgprhxwhrcgpwutp'
        pattern = 'yrcgpw'
        expected = [1, 2, 10, 22, 31, 32]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_716(self):
        text = 'gxxjcmqjenkgxjcmqdjefwjgxjcmqjwevagxjcmqjeiitgxjycmqjentgynghxjcmqjeuq'
        pattern = 'gxjcmqje'
        expected = [1, 2, 3, 12, 24, 34, 35, 36, 46, 60, 61, 62]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_717(self):
        text = 'gcaxwufptyhgcaxwlvpbgcxwfmhwxgcgaxwfqjuivpgcaxwfcaygcaxwfsinorgcaxufwt'
        pattern = 'gcaxwf'
        expected = [1, 12, 21, 30, 31, 32, 42, 43, 44, 51, 52, 53, 63]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_718(self):
        text = 'rdczsrmsxrdczpiddwrdczzaxrdczntvcgrdczmtbamrdcznunacrduczoz'
        pattern = 'rdcz'
        expected = [1, 2, 9, 10, 11, 18, 19, 20, 25, 26, 27, 34, 35, 36, 43, 44, 45, 53]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_719(self):
        text = 'jbwyspjbwrkbbzmjzbwyatfjbwyswsnjbsyrh'
        pattern = 'jbwy'
        expected = [1, 2, 7, 16, 17, 18, 23, 24, 25, 32]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_720(self):
        text = 'ytqvprpduoytvprpdhdvryatvprpdfmnonytvprvdepm'
        pattern = 'ytvprpd'
        expected = [1, 10, 11, 12, 22, 23, 24, 35]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_721(self):
        text = 'rqwzdtthimrqwfdtthghwwrqwzdtthlecrewzdtthkorqwzdqtthaqrqwozdtthubtiy'
        pattern = 'rqwzdtth'
        expected = [1, 2, 11, 22, 23, 24, 34, 44, 55]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_722(self):
        text = 'ysylhbvebisyslhbvebtiyppnyslhbveboayslhbovebmufyslhbvebsifyslhbvebbvasm'
        pattern = 'yslhbveb'
        expected = [1, 2, 3, 11, 12, 13, 25, 26, 27, 36, 47, 48, 49, 58, 59, 60]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_723(self):
        text = 'boyewauyayyboyewubkcboyewuzmzboyewucgboyewuzgafnboewugfy'
        pattern = 'boyewu'
        expected = [1, 11, 12, 13, 20, 21, 22, 29, 30, 31, 37, 38, 39, 49]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_724(self):
        text = 'pgstveipestvvjpestveaymbpestdvdaiopestvtxpeshtvywi'
        pattern = 'pestv'
        expected = [1, 7, 8, 9, 14, 15, 16, 25, 34, 35, 36, 42]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_725(self):
        text = 'zjrxyszcqdzjruxysrhlqkzjrxysxoqzzjrxysgxnazjrxysutpblzjrxysurzjjrxysbe'
        pattern = 'zjrxys'
        expected = [1, 2, 11, 22, 23, 24, 32, 33, 34, 42, 43, 44, 53, 54, 55, 62, 63, 64]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_726(self):
        text = 'goyuymhpatjgoyuymbgtdgoyuymoworgoyuymmvkwgomuymeugyrgoyujympnngoyuypmyuizf'
        pattern = 'goyuym'
        expected = [1, 2, 11, 12, 13, 21, 22, 23, 31, 32, 33, 42, 53, 63]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_727(self):
        text = 'ichqxfnancichqxfhhlnixchqxfqwzvichqxfsxgicqhxfpzzcichqxflyxc'
        pattern = 'ichqxf'
        expected = [1, 2, 10, 11, 12, 21, 22, 23, 31, 32, 33, 41, 50, 51, 52]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_728(self):
        text = 'tuxxgxlbioydtxxgxlbrwrtxxgxlbgsjqktexgxlbfnzwtxxfxlbfw'
        pattern = 'txxgxlb'
        expected = [1, 2, 3, 12, 13, 14, 22, 23, 24, 35, 46]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_729(self):
        text = 'gvopfffcarwgvnopffflemojgvopfhffpuxngvopfffxewwgvopfffacvcgvotpfffzctngvopfffjlw'
        pattern = 'gvopfff'
        expected = [1, 2, 12, 25, 36, 37, 38, 47, 48, 49, 59, 70, 71, 72]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_730(self):
        text = 'azjjzrflpazojjzmepttmazjjzcrxnvazjtjzvly'
        pattern = 'azjjz'
        expected = [1, 2, 10, 21, 22, 23, 32]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_731(self):
        text = 'mjgebgququmjgefgqupgttbmjegebgquizovmgebgqufsfmjgebgqutdmjgebgqfuvikuo'
        pattern = 'mjgebgqu'
        expected = [1, 2, 11, 24, 37, 46, 47, 48, 57]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_732(self):
        text = 'gmnlhphlmnlhvvpmnlhpvkmnlhpcqiu'
        pattern = 'mnlhp'
        expected = [1, 2, 3, 9, 15, 16, 17, 22, 23, 24]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_733(self):
        text = 'ljnudhikpbjrudhpjjkudhoajnudhggjnudhlb'
        pattern = 'jnudh'
        expected = [1, 2, 3, 11, 18, 24, 25, 26, 31, 32, 33]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_734(self):
        text = 'bjjlakqflkabjjlaknfabutbjjlaknfcbfbjjvaknfairyebjjlaknfokbjjlaknfog'
        pattern = 'bjjlaknf'
        expected = [1, 11, 12, 13, 23, 24, 25, 35, 47, 48, 49, 57, 58, 59]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_735(self):
        text = 'qpfdpbgqpfdehlqpfdghhbzqlpfdydhxcmqpfdvwqpfduy'
        pattern = 'qpfd'
        expected = [1, 2, 7, 8, 9, 14, 15, 16, 24, 25, 26, 34, 35, 36, 40, 41, 42]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_736(self):
        text = 'ozvtvqliwlkozvtvqliahozvtvqcliqbbozvtvqliiqozvtvqibrfwy'
        pattern = 'ozvtvqli'
        expected = [1, 2, 11, 12, 13, 22, 33, 34, 35, 44]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_737(self):
        text = 'edncobysyfkeoncobrhveoncmbegtceonpobvkteoncobcelweoncobvhpirezoncobnthf'
        pattern = 'eoncob'
        expected = [1, 11, 12, 13, 21, 31, 39, 40, 41, 49, 50, 51, 61, 62, 63]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_738(self):
        text = 'eclrfxtnzfoeclrfdxtnanaeclrfxtntheclrufxtnrbhoa'
        pattern = 'eclrfxtn'
        expected = [1, 2, 12, 23, 24, 25, 34]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_739(self):
        text = 'ikmlplvmgrikmlplylsikmlpxbbrikmlpltz'
        pattern = 'ikmlpl'
        expected = [1, 2, 10, 11, 12, 20, 28, 29, 30]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_740(self):
        text = 'xabipcjgsxabipshsjluxabipfnkgvxabibsztlgxabipshwyxabidpsljqoxabipsxsa'
        pattern = 'xabips'
        expected = [1, 9, 10, 11, 21, 31, 40, 41, 42, 50, 60, 61, 62]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_741(self):
        text = 'rtrhmykrwrtrhmbknjncsrtrhmlykzfkrrtrhmykxwycrtremykfnr'
        pattern = 'rtrhmyk'
        expected = [1, 2, 10, 22, 33, 34, 35, 45]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_742(self):
        text = 'cbxeweeumtwrcbxeweeyvcbxeweehucbxebweesofbqcoxeweexdcbxeweeyaelg'
        pattern = 'cbxewee'
        expected = [1, 2, 12, 13, 14, 21, 22, 23, 31, 44, 52, 53, 54]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_743(self):
        text = 'hcgatnrbcgamabwchcgadvxhcgacshcgablzsohcglsbhcgado'
        pattern = 'hcga'
        expected = [1, 2, 8, 9, 16, 17, 18, 23, 24, 25, 29, 30, 31, 39, 44, 45, 46]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_744(self):
        text = 'buvuerbquvupawelbvuvuztxrouvuitybuvgoqujbuvuwvvkfbzvurja'
        pattern = 'buvu'
        expected = [1, 2, 7, 8, 9, 17, 18, 19, 26, 27, 33, 40, 41, 42, 50]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_745(self):
        text = 'rtrivwaxxtrtrivmwklrtrivwijsprtzivwkjlazrtrfivwrqbirtrbvwsgs'
        pattern = 'rtrivw'
        expected = [1, 2, 11, 19, 20, 21, 30, 41, 52]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_746(self):
        text = 'qcqkxdkqcqkxdmuriaqcqkxyfyewqcqkxjziqxcqkxqaygqcqpkxeaqcqxxvmby'
        pattern = 'qcqkx'
        expected = [1, 2, 7, 8, 9, 18, 19, 20, 28, 29, 30, 37, 38, 39, 47, 55]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_747(self):
        text = 'gmxrrvosfkmxrrvshkmxyrvgiukmxrrvaytgd'
        pattern = 'kmxrrv'
        expected = [1, 2, 9, 10, 11, 18, 26, 27, 28]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_748(self):
        text = 'hvjlbubmlhvjlbuzhvjlbohybhvjlbksk'
        pattern = 'hvjlb'
        expected = [1, 2, 9, 10, 11, 16, 17, 18, 25, 26, 27]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_749(self):
        text = 'aqjxlfzkqajqxbeiwgajqxassubajqxxwsajvqxapmdnajqxns'
        pattern = 'ajqx'
        expected = [1, 9, 10, 11, 18, 19, 20, 27, 28, 29, 35, 44, 45, 46]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_750(self):
        text = 'rntujgywerntugkpueprntugberntugxxbbr'
        pattern = 'rntug'
        expected = [1, 9, 10, 11, 19, 20, 21, 26, 27, 28]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_751(self):
        text = 'gpryisgsprdlbiyqgtrdmkxcgpprdml'
        pattern = 'gprd'
        expected = [1, 7, 8, 9, 17, 25, 26, 27]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_752(self):
        text = 'qxlfcalgerqxlftalldqouqxlftalcyqxlfxalbam'
        pattern = 'qxlftal'
        expected = [1, 10, 11, 12, 22, 23, 24, 32]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_753(self):
        text = 'ghkphngaghkpcgjmniaghkpccbffllghkpcoyrpghkzpcjxdfgghkpczvyj'
        pattern = 'ghkpc'
        expected = [1, 8, 9, 10, 19, 20, 21, 30, 31, 32, 40, 50, 51, 52]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_754(self):
        text = 'maatmjasfsmaabmkjaytjepmaabmjakqmaawbmjaxawmaabmjayns'
        pattern = 'maabmja'
        expected = [1, 11, 23, 24, 25, 33, 43, 44, 45]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_755(self):
        text = 'sptfgukzasptfgteksptfgdedqspdtfgczowspcfgiogspstfgnwow'
        pattern = 'sptfg'
        expected = [1, 2, 9, 10, 11, 17, 18, 19, 27, 37, 45, 46, 47]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_756(self):
        text = 'urrqnsqfrjcurnqnsaguvrurrqnszaalurrunsbklfurdrqnsbigaurrsqnsfziurrbqnstmu'
        pattern = 'urrqns'
        expected = [1, 2, 12, 22, 23, 24, 33, 43, 54, 64]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_757(self):
        text = 'nrblqkgiarblqkaesyblqkyxwyfkrblqkdyltfrblqkbicrblqkhobsrblqkrmj'
        pattern = 'rblqk'
        expected = [1, 2, 3, 9, 10, 11, 18, 19, 28, 29, 30, 38, 39, 40, 46, 47, 48, 55, 56, 57]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_758(self):
        text = 'efcvyzzbxknbwefcvzzbqjcnefcvzzbaolydefcvzzbgykqoefdcvzzbgowniefcfzzbygiwx'
        pattern = 'efcvzzb'
        expected = [1, 13, 14, 15, 24, 25, 26, 36, 37, 38, 49, 62]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_759(self):
        text = 'ojtelavkgfhmrojtenapkdohvgojtenavkkrueuojtbnavkcdojtenavkej'
        pattern = 'ojtenavk'
        expected = [1, 14, 26, 27, 28, 40, 49, 50, 51]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_760(self):
        text = 'uioubrfgojobdjiobrfgoktuiobbrfgoxwuiobtrfgevmiobrfgvcv'
        pattern = 'uiobrfg'
        expected = [1, 14, 15, 24, 35, 45, 46]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_761(self):
        text = 'gncmpxhgesgncmpxiagncmpxwzmgncmpwxdusibgnjmpxpmgncmpxnuingncmpxvu'
        pattern = 'gncmpx'
        expected = [1, 2, 10, 11, 12, 18, 19, 20, 28, 40, 47, 48, 49, 57, 58, 59]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_762(self):
        text = 'fdijqbbumlqdijqbbuydendvjqbbuwcqcedijqbbuibdijqhbbuycnepdljqbbuqddijqbbnrfre'
        pattern = 'dijqbbu'
        expected = [1, 2, 3, 11, 12, 13, 23, 34, 35, 36, 44, 57, 66]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_763(self):
        text = 'ubuxuziyxzlubuxuziuwlzubuxuziugwubuxuzijwgntmubuxuziuglksw'
        pattern = 'ubuxuziu'
        expected = [1, 11, 12, 13, 22, 23, 24, 33, 45, 46, 47]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_764(self):
        text = 'daigtjkcqdmhmdaigtjkcejieudaigtjxkctaidaigtjkqaaqbt'
        pattern = 'daigtjkc'
        expected = [1, 2, 13, 14, 15, 27, 39]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_765(self):
        text = 'mttvihkoiuttviymyvzmttvipftywmttviwztqmttvxihyfhtkttvipg'
        pattern = 'mttvi'
        expected = [1, 2, 10, 11, 19, 20, 21, 29, 30, 31, 39, 50, 51]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_766(self):
        text = 'ykfnsypbgsoykfnsyhbvnykfnsypbjptykfnsypbvhylkfnsypbiq'
        pattern = 'ykfnsypb'
        expected = [1, 2, 12, 21, 22, 23, 32, 33, 34, 43, 44, 45]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_767(self):
        text = 'eexschtajeexkcbzgereexkchuggakeexkchupsbf'
        pattern = 'eexkch'
        expected = [1, 10, 19, 20, 21, 30, 31, 32]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_768(self):
        text = 'kjhcsbpeaohjhcsbpxvtkjhcsbpvzkjhcsbperkjhcsbfvrkjhcsbpdajokjhcsbpgt'
        pattern = 'kjhcsbp'
        expected = [1, 2, 11, 12, 20, 21, 22, 29, 30, 31, 39, 47, 48, 49, 58, 59, 60]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_769(self):
        text = 'babrokirbuuvvbabrokirnpxkjbabrokyruexbabrokirzxbabrokirrdnzcbabbokirujtq'
        pattern = 'babrokir'
        expected = [1, 2, 13, 14, 15, 27, 37, 38, 39, 47, 48, 49, 61]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_770(self):
        text = 'namoxikwsgngmoxielpngmoxipwjungymoxisihb'
        pattern = 'ngmoxi'
        expected = [1, 10, 11, 12, 19, 20, 21, 30]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_771(self):
        text = 'lrqobgdvsszclrqoqgdqtbtlrqopgdvllrqopgdbsvlwolrqopsgdrjwhklrqopgdarkgf'
        pattern = 'lrqopgd'
        expected = [1, 13, 23, 24, 25, 32, 33, 34, 46, 58, 59, 60]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_772(self):
        text = 'bwxhdfjaburbwxhldjtwhbwxydjrfbwzhdjhqutbwxhdxsxlbwxhdjrmjxvbhxhdjio'
        pattern = 'bwxhdj'
        expected = [1, 12, 22, 30, 40, 48, 49, 50, 60]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_773(self):
        text = 'nepmgjeabnepmwkwnepmtcpjnelmoaxlnepubhmqonepmvsknepmpwrtu'
        pattern = 'nepm'
        expected = [1, 2, 9, 10, 11, 16, 17, 18, 25, 33, 41, 42, 43, 48, 49, 50]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_774(self):
        text = 'isytaiwibisytbalobqkisytahiskisytajqlehisytaplarwisytafofbt'
        pattern = 'isyta'
        expected = [1, 2, 10, 20, 21, 22, 29, 30, 31, 39, 40, 41, 49, 50, 51]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_775(self):
        text = 'qzhjxuodnqyhjxukopcyqyhjxuolxfyhjxuovkqyhjxuueetgtqyhjxuookes'
        pattern = 'qyhjxuo'
        expected = [1, 10, 20, 21, 22, 30, 31, 39, 50, 51, 52]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_776(self):
        text = 'fvatxxdlmfvaptxxslfveatxxxzfvatxxhybrdfvatxxaqehh'
        pattern = 'fvatxx'
        expected = [1, 2, 10, 19, 27, 28, 29, 38, 39, 40]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_777(self):
        text = 'pqbqqpzelopqbqqpdsxqgapqbqqprzfppqbqqpyfopqbqpqpkl'
        pattern = 'pqbqqp'
        expected = [1, 2, 10, 11, 12, 22, 23, 24, 32, 33, 34, 42]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_778(self):
        text = 'uqjdykkpgiuqjdyusdmluqjdyqauuwujqjdyvuuqjdyxlbpluqjdylnasuqjdyag'
        pattern = 'uqjdy'
        expected = [1, 2, 10, 11, 12, 20, 21, 22, 31, 32, 33, 38, 39, 40, 48, 49, 50, 57, 58, 59]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_779(self):
        text = 'wnngnbavwnnnuomqwnnfncqwnnusbac'
        pattern = 'wnnn'
        expected = [1, 8, 9, 10, 17, 24]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_780(self):
        text = 'kjlregkkjlraiknjlrzssukjprcxkjlrghm'
        pattern = 'kjlr'
        expected = [1, 2, 7, 8, 9, 14, 15, 16, 23, 28, 29, 30]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_781(self):
        text = 'mvoqhetwyfdmvogqhtewzfxmvoqthtewyamvoqztewxczhkmvoqkhtewyxlmovqhtewuzjt'
        pattern = 'mvoqhtew'
        expected = [1, 12, 24, 35, 48, 60]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_782(self):
        text = 'qofvbgmofvraqmoyfvlqqozmofvqjkgl'
        pattern = 'mofv'
        expected = [1, 2, 6, 7, 8, 14, 23, 24, 25]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_783(self):
        text = 'ophkwtdqdphkwuqdphkwrhdphkwbc'
        pattern = 'dphkw'
        expected = [1, 2, 8, 9, 10, 15, 16, 17, 22, 23, 24]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_784(self):
        text = 'tvekjxgygvejxhkztbvejxhultvjjxattvejxcgpe'
        pattern = 'tvejx'
        expected = [1, 9, 10, 17, 18, 19, 26, 32, 33, 34]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_785(self):
        text = 'xjkdkgxylagzyxkdkgxygdxkdkigxypmxzkdkgxycdaxkdkgxyifmxkdbgxyafxkdkgxyawty'
        pattern = 'xkdkgxy'
        expected = [1, 2, 3, 13, 14, 15, 23, 33, 34, 35, 43, 44, 45, 54, 62, 63, 64]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_786(self):
        text = 'cvdytekkcvdyfemjtwcvedyteorxaacvdyterjiyb'
        pattern = 'cvdyte'
        expected = [1, 2, 9, 19, 30, 31, 32]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_787(self):
        text = 'mqytrwumlmcytrqupmcytrpycmcytrefgqmcyotragmcytfyfemdmcytrswx'
        pattern = 'mcytr'
        expected = [1, 9, 10, 11, 17, 18, 19, 25, 26, 27, 35, 43, 52, 53, 54]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_788(self):
        text = 'jltudunnxeltuxsieltuhfkpleltueuweltudskelnudobms'
        pattern = 'eltu'
        expected = [1, 2, 9, 10, 11, 16, 17, 18, 25, 26, 27, 32, 33, 34, 40]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_789(self):
        text = 'ieunduvnieunyubsstieunykuoeblwieutnyuvmkyiaunyuwwxyzieunnyumy'
        pattern = 'ieunyu'
        expected = [1, 8, 9, 10, 19, 31, 42, 53]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_790(self):
        text = 'dxvtbdeuhikxvtbdeorjxzixvtbdehuoxixvtbudetayzi'
        pattern = 'ixvtbde'
        expected = [1, 2, 10, 11, 12, 22, 23, 24, 34]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_791(self):
        text = 'gyqodihjqkgyqoduiffgyqopdivrgyqodhdkjgyeqodiotkgyqoaitez'
        pattern = 'gyqodi'
        expected = [1, 2, 11, 20, 29, 38, 48]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_792(self):
        text = 'tbwyxbeldiqtbwyxubetpunftbwyxbehzbztbwyxbehlxmitbywyxbesairtbwyxbefgdxtbwyxpecz'
        pattern = 'tbwyxbe'
        expected = [1, 2, 12, 24, 25, 26, 35, 36, 37, 48, 59, 60, 61, 71]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_793(self):
        text = 'xeetnmgkipexetnvgkimxzfvxetnmgrkibwexetnmgkkidxfzxetnmgkidufjxestnmgkidlxetnmgkciibn'
        pattern = 'xetnmgki'
        expected = [1, 2, 3, 12, 25, 37, 49, 50, 51, 62, 73]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_794(self):
        text = 'otgeksswivtgeksstrvtgekssxzsrftgekssphsxigekssjf'
        pattern = 'tgekss'
        expected = [1, 2, 3, 10, 11, 12, 19, 20, 21, 30, 31, 32, 41, 42]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_795(self):
        text = 'aaxjvkusrhaaxjvjudvajjaaxjvpkucfzaaxjvkucvfjwaaxjvkuylyauaxjvkuagiaaxjvkuqqp'
        pattern = 'aaxjvku'
        expected = [1, 2, 11, 23, 33, 34, 35, 45, 46, 47, 56, 57, 58, 66, 67, 68]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_796(self):
        text = 'yqxieczcyqxiejgsyqixieixwtlqxieflzyqxiirbtyqxxeoiyqxiepz'
        pattern = 'yqxie'
        expected = [1, 2, 8, 9, 10, 17, 27, 28, 35, 43, 49, 50, 51]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_797(self):
        text = 'dtdwzjtkuvdtdwyjfdgdtdwzjcsidtdwzjbpear'
        pattern = 'dtdwzj'
        expected = [1, 2, 11, 19, 20, 21, 28, 29, 30]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_798(self):
        text = 'ybpttiypilybpttmbybpttbrhybptfjtghybupttukybpttjbybptraller'
        pattern = 'ybptt'
        expected = [1, 2, 10, 11, 12, 17, 18, 19, 26, 35, 42, 43, 44, 50]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_799(self):
        text = 'nrtybuazfofnrtybuazqmnrtybuazrranrtybuazdyu'
        pattern = 'nrtybuaz'
        expected = [1, 2, 11, 12, 13, 21, 22, 23, 32, 33, 34]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_800(self):
        text = 'wcrbkfsulwcrugdojogwcrupgpwgruvq'
        pattern = 'wcru'
        expected = [1, 9, 10, 11, 19, 20, 21, 27]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_801(self):
        text = 'qmfclsumpcuswqmpccbtqmpcvtq'
        pattern = 'qmpc'
        expected = [1, 7, 8, 13, 14, 15, 20, 21, 22]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_802(self):
        text = 'fqgrvzkvqgrbwybqrvqgrnqveukvqgridiavqgrsydpovagrns'
        pattern = 'vqgr'
        expected = [1, 2, 7, 8, 9, 17, 18, 19, 27, 28, 29, 35, 36, 37, 45]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_803(self):
        text = 'wabvzrmlbywabvrmaebhowabxvrmdcrlwabvrrrzm'
        pattern = 'wabvrm'
        expected = [1, 10, 11, 12, 22, 33]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_804(self):
        text = 'ayjmgdwqeuayjmcgdivrvayimgdqnfaaejmgdazdnaayjmgdciuaqyjmgdekhayjmgdkzdq'
        pattern = 'ayjmgd'
        expected = [1, 2, 11, 22, 32, 42, 43, 44, 52, 53, 54, 61, 62, 63]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_805(self):
        text = 'yudeshodydueshobjyudesqcrtyuzeshgedr'
        pattern = 'yudesh'
        expected = [1, 2, 9, 18, 27]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_806(self):
        text = 'josmbvqtzdjosmbazkalfjosmbkthjoambrfzwjonsmbrlarv'
        pattern = 'josmb'
        expected = [1, 2, 10, 11, 12, 21, 22, 23, 30, 39]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_807(self):
        text = 'qinvgodsnmbqinvgodfrqinvgodbleqqinvgodgysqinvgodnppgqinvgodgwmlwqinvgoidmsvce'
        pattern = 'qinvgod'
        expected = [1, 2, 11, 12, 13, 20, 21, 22, 31, 32, 33, 41, 42, 43, 52, 53, 54, 65]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_808(self):
        text = 'egdgusdnzegdgulnaagdgunkrdmegdwgufcmmegdguxngeqegdgultfcegdgusmc'
        pattern = 'egdgu'
        expected = [1, 2, 9, 10, 11, 18, 19, 28, 37, 38, 39, 47, 48, 49, 56, 57, 58]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_809(self):
        text = 'qpnxntyrkonxnotqnxncpxbjqnxnsfwqnxnkxkqnxnzvxsa'
        pattern = 'qnxn'
        expected = [1, 2, 3, 10, 11, 15, 16, 17, 24, 25, 26, 31, 32, 33, 38, 39, 40]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_810(self):
        text = 'vlrjyfbvlbjhvlkqvlbjpvqovlbzbxalvnlbjpyovdbjblhx'
        pattern = 'vlbj'
        expected = [1, 7, 8, 9, 16, 17, 18, 25, 33, 34, 35, 41]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_811(self):
        text = 'ywsolfzdywslrpywyslsegqwslpkywmslsxjxywslcwveg'
        pattern = 'ywsl'
        expected = [1, 8, 9, 10, 15, 16, 17, 23, 24, 29, 37, 38, 39]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_812(self):
        text = 'iwbsvxcuwidbsvxrkegidbsavxccrmidibsvxuk'
        pattern = 'idbsvx'
        expected = [1, 9, 10, 11, 20, 31, 32, 33]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_813(self):
        text = 'ssntywojibqdssntyewsohkssntwysiqxssntywshlmkmskntywszic'
        pattern = 'ssntyws'
        expected = [1, 13, 24, 33, 34, 35, 46]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_814(self):
        text = 'odokejempecndokejemwdododokejelmblboodokejemrqdskodokejemydhdykodokejemyuitb'
        pattern = 'odokejem'
        expected = [1, 2, 12, 13, 24, 36, 37, 38, 49, 50, 51, 63, 64, 65]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_815(self):
        text = 'zmdroldzlefpzmrolddeakpmroldmmhmroldpdmmroldhfizmrolbdxmezmrolmugj'
        pattern = 'zmrold'
        expected = [1, 12, 13, 14, 23, 24, 31, 32, 39, 40, 48, 58]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_816(self):
        text = 'evnqfupkzlvevnqfuppgglevnqfupkifiiuevnqfupkauwkg'
        pattern = 'evnqfupk'
        expected = [1, 2, 12, 22, 23, 24, 35, 36, 37]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_817(self):
        text = 'ugiombougiomujrugiomnabqiugiomlgmugiomgqjgwufiomrodugiamnfkqd'
        pattern = 'ugiom'
        expected = [1, 2, 7, 8, 9, 15, 16, 17, 25, 26, 27, 33, 34, 35, 44, 52]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_818(self):
        text = 'yrjaexdtymaetryjaebjhdlkyjaezxypycaegfdyzyjaelao'
        pattern = 'yjae'
        expected = [1, 2, 3, 9, 14, 15, 16, 24, 25, 26, 33, 41, 42, 43]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_819(self):
        text = 'mlozlywmeqabllzlywmnausmlzlyhwmnezgmlzlywvmumwmlzlywmommlzlywmknsmlzilywmbzujw'
        pattern = 'mlzlywm'
        expected = [1, 13, 14, 24, 36, 46, 47, 48, 55, 56, 57, 66]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_820(self):
        text = 'ntjydiojytgntjsydiomrntjydiobbntmydiobjntjygiogkntjydioxcacx'
        pattern = 'ntjydio'
        expected = [1, 2, 12, 21, 22, 23, 31, 40, 48, 49, 50]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_821(self):
        text = 'wtxcpwwawtxfcqocwtxcvhikwwtxkcfcwtxcilcwtxccqev'
        pattern = 'wtxc'
        expected = [1, 2, 9, 16, 17, 18, 26, 32, 33, 34, 39, 40, 41]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_822(self):
        text = 'qbolbzkogpnsbqbolbzxompnqbolubzxovwckwqbolwbzxokctpqbolbzxoczqnqbulbzxolpdalqbolbzxobfcf'
        pattern = 'qbolbzxo'
        expected = [1, 13, 14, 15, 25, 39, 51, 52, 53, 64, 76, 77, 78]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_823(self):
        text = 'uywqztvawybjuywqztvqvuywqzfvsjkquywqztvbxo'
        pattern = 'uywqztv'
        expected = [1, 2, 12, 13, 14, 22, 32, 33, 34]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_824(self):
        text = 'uqreourcmwuqreoukwhuqgreougguqreouapleuqreounsuqreoudid'
        pattern = 'uqreou'
        expected = [1, 2, 10, 11, 12, 20, 28, 29, 30, 38, 39, 40, 46, 47, 48]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_825(self):
        text = 'irpbhpeajirpbhpjuirpbhpsydrpbhpaiirpbhupupwirpbhperwricirpbhpck'
        pattern = 'irpbhp'
        expected = [1, 2, 9, 10, 11, 17, 18, 19, 26, 27, 34, 43, 44, 45, 55, 56, 57]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_826(self):
        text = 'fjinjirkifjbnjirimfjbnfjiragznfjbnjirfxnfjbnjircfmqrfjbnjiroig'
        pattern = 'fjbnjir'
        expected = [1, 9, 10, 11, 19, 30, 31, 32, 40, 41, 42, 52, 53, 54]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_827(self):
        text = 'hrmilabhrilnchrilrbhorilsycnghriljzzxf'
        pattern = 'hril'
        expected = [1, 7, 8, 9, 13, 14, 15, 20, 21, 22, 29, 30, 31]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_828(self):
        text = 'aqpajpaskhaqpjpajoaqfpjpaagqgaqpjpackppaqpjpaiyuqpjpavhvloaqpjpapv'
        pattern = 'aqpjpa'
        expected = [1, 10, 11, 12, 19, 29, 30, 31, 39, 40, 41, 48, 49, 58, 59, 60]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_829(self):
        text = 'yefmpehulezyefmzehajfyefmzehvfsiqefmzehtiwnyefmkzehvslwx'
        pattern = 'yefmzeh'
        expected = [1, 11, 12, 13, 21, 22, 23, 33, 34, 44]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_830(self):
        text = 'spkrigcblespkrgvespkrgiinhspktgnzspkrgvccjspkrgknhqispklrgrg'
        pattern = 'spkrg'
        expected = [1, 10, 11, 12, 17, 18, 19, 27, 33, 34, 35, 42, 43, 44, 53]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_831(self):
        text = 'rqjrrdbrqmrrtcoqrqjrreqcrqjrrfzwd'
        pattern = 'rqjrr'
        expected = [1, 2, 8, 16, 17, 18, 24, 25, 26]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_832(self):
        text = 'vnyvoholdvzvnyvholtihvnyvholovilhvnyvhglykvnyvtholuqbvvnyvholwrodi'
        pattern = 'vnyvhol'
        expected = [1, 11, 12, 13, 21, 22, 23, 34, 43, 54, 55, 56]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_833(self):
        text = 'qexizcqhjqeizzkqeizbbqeizjiuqehizpmvix'
        pattern = 'qeiz'
        expected = [1, 9, 10, 11, 15, 16, 17, 21, 22, 23, 29]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_834(self):
        text = 'xwojfxbqxwomuzvudxwwojkdxswojezurxwojkebkr'
        pattern = 'xwoj'
        expected = [1, 2, 9, 18, 19, 20, 25, 26, 27, 33, 34, 35]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_835(self):
        text = 'ewpqckrjcmewpqcmkrcwlngewpqckrayewpqckrzlewpqckrqvpgqwewpqckpodvewpqckrtgtb'
        pattern = 'ewpqckr'
        expected = [1, 2, 11, 23, 24, 25, 32, 33, 34, 41, 42, 43, 55, 64, 65, 66]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_836(self):
        text = 'ldygdgtpxhuvdygdgtpomcnldygdgwpnbaoldygdygtparbis'
        pattern = 'ldygdgtp'
        expected = [1, 2, 12, 13, 24, 36]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_837(self):
        text = 'zirpaovnqoszixaoatlvyziragixkaziraojfvhqzuraohxziraqohabozuraolsbpa'
        pattern = 'zirao'
        expected = [1, 12, 22, 30, 31, 32, 41, 48, 58]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_838(self):
        text = 'eichewuzcbvwepicyewuzpnlydeicyewlzmlneicyewwznkko'
        pattern = 'eicyewuz'
        expected = [1, 13, 14, 15, 27, 38]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_839(self):
        text = 'istxewqoistpewjiistpeawradkriscpewnwd'
        pattern = 'istpew'
        expected = [1, 8, 9, 10, 17, 29]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_840(self):
        text = 'rvitidgntikrviidgntfpkrviidgntnlmarrviitgntfanrviidgntqfrviidgfttejjf'
        pattern = 'rviidgnt'
        expected = [1, 11, 12, 13, 22, 23, 24, 36, 46, 47, 48, 57]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_841(self):
        text = 'upxaopocupxahhujzuapxajjuvupxasau'
        pattern = 'upxa'
        expected = [1, 2, 8, 9, 10, 18, 19, 20, 26, 27, 28]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_842(self):
        text = 'yoavgpctgosavgdjhgoapgexusoavgucjiw'
        pattern = 'oavg'
        expected = [1, 2, 3, 10, 11, 12, 19, 26, 27, 28]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_843(self):
        text = 'ttchpjiktzrtchpjwwwtfhpjlytchpwuyixrtchpjajbdo'
        pattern = 'tchpj'
        expected = [1, 2, 3, 11, 12, 13, 20, 27, 36, 37, 38]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_844(self):
        text = 'zhlzagyxkzhlwagczcszhlragofxvoxzhlragpgv'
        pattern = 'zhlrag'
        expected = [1, 10, 19, 20, 21, 31, 32, 33]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_845(self):
        text = 'pwfgzihropwifgrihpwfgopmpwfhmhh'
        pattern = 'pwfg'
        expected = [1, 2, 10, 17, 18, 19, 25]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_846(self):
        text = 'ayzgaxftkbyzgapxfauygzgaxftttwcyzgaxfti'
        pattern = 'yzgaxf'
        expected = [1, 2, 3, 11, 20, 21, 22, 31, 32, 33]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_847(self):
        text = 'asoawdoasooawnuasoakeriasoawlzqasoawvpwcadoawdcvejasoawgp'
        pattern = 'asoaw'
        expected = [1, 2, 8, 16, 23, 24, 25, 31, 32, 33, 41, 50, 51, 52]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_848(self):
        text = 'kzzxhojjnkzzxhpxtmelkzzjhpkdhkuzxhpjxd'
        pattern = 'kzzxhp'
        expected = [1, 9, 10, 11, 21, 30]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_849(self):
        text = 'zdkwcxhbrodkwcxhbnkojdkwcxhabdodcodkwcxhbhdcmudkwccxhbmgdkwcxhblrmu'
        pattern = 'dkwcxhb'
        expected = [1, 2, 3, 10, 11, 12, 22, 34, 35, 36, 47, 56, 57, 58]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_850(self):
        text = 'afexilcnafehxilomiqafexilntfsjafexilsvygbafeyilcwafexilgyyafexiliiq'
        pattern = 'afexil'
        expected = [1, 2, 9, 19, 20, 21, 30, 31, 32, 42, 49, 50, 51, 58, 59, 60]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_851(self):
        text = 'figvfqptnbfivfqpjmgfizfqpwvqdfrivfqpygdfivfqpkgifivfqpjauifiavfqpumfow'
        pattern = 'fivfqp'
        expected = [1, 10, 11, 12, 20, 30, 31, 32, 39, 40, 41, 48, 49, 50, 59]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_852(self):
        text = 'brpzkpbrppziwbrpzxzmborpznknrpzxkbxrpzzu'
        pattern = 'brpz'
        expected = [1, 2, 7, 13, 14, 15, 21, 22, 23, 28, 29, 34, 35, 36]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_853(self):
        text = 'iaklpaukauiaklzaustdwfiaklvzaukwdoiaklzaukgn'
        pattern = 'iaklzauk'
        expected = [1, 11, 23, 34, 35, 36]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_854(self):
        text = 'goggixxuyqngoggitxkgogeixjmgoggixlqzk'
        pattern = 'goggix'
        expected = [1, 2, 12, 20, 27, 28, 29]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_855(self):
        text = 'igkutoigvudpqiukuyevnkigkuzwytxigeuwbdibigkugqlyigkmtyv'
        pattern = 'igku'
        expected = [1, 2, 7, 14, 22, 23, 24, 32, 40, 41, 42, 49]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_856(self):
        text = 'mwraousbcmwraositomwraoeogwraotsbmwraxngmwraozn'
        pattern = 'mwrao'
        expected = [1, 2, 9, 10, 11, 18, 19, 20, 26, 27, 34, 40, 41, 42]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_857(self):
        text = 'xxdgtqttddyxxdgtqtmebnrxxdgtqtecvjpxxdgtqtbedesxxrdgtqtzzxxdgtqtbctxxdgtqtifl'
        pattern = 'xxdgtqt'
        expected = [1, 2, 11, 12, 13, 23, 24, 25, 35, 36, 37, 48, 49, 57, 58, 59, 67, 68, 69]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_858(self):
        text = 'lgpwtblsevqalgpwtblsshxlqpwtblspklgpwtablswokylglpwtblsoklgpwtblseodavlgpwtblssfv'
        pattern = 'lgpwtbls'
        expected = [1, 2, 12, 13, 14, 24, 34, 47, 48, 49, 57, 58, 59, 70, 71, 72]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_859(self):
        text = 'xzzdcpxzzpruloxzzzpffekxzzpyqofxhzpcvxfzzpin'
        pattern = 'xzzp'
        expected = [1, 6, 7, 8, 15, 16, 17, 23, 24, 25, 32, 38, 39, 40]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_860(self):
        text = 'wwpeniyzhaenwwpeniyzcfhwwpenbiyzhegjwupeniyzhmtylwwpensyzgrrmswwpeniyzcrwwpeniyzei'
        pattern = 'wwpeniyz'
        expected = [1, 2, 12, 13, 14, 24, 37, 50, 62, 63, 64, 72, 73, 74]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_861(self):
        text = 'idpsctmqttidpsctkwjfidipscteyvidpstcmmridpscxtnfdzd'
        pattern = 'idpsct'
        expected = [1, 2, 10, 11, 12, 21, 22, 23, 31, 40]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_862(self):
        text = 'kuezelwbczikuezlwmbcemcilkuezlnbckikukezlwbcwuqrxkzezlwbcozund'
        pattern = 'kuezlwbc'
        expected = [1, 12, 26, 36, 37, 38, 50]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_863(self):
        text = 'wlffphmoicdwlffpkmofhwlffimoniumwfffpmovwpewlofpmomrvuiwlffpxmoqewlffpmooyskq'
        pattern = 'wlffpmo'
        expected = [1, 12, 22, 33, 44, 56, 65, 66, 67]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_864(self):
        text = 'ppnsgojqfkppnsojueppnsouovwsppnsojehvurpnsojxfppnsojqajn'
        pattern = 'ppnsoj'
        expected = [1, 10, 11, 12, 19, 28, 29, 30, 39, 40, 46, 47, 48]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_865(self):
        text = 'qwgvltkravqwgyldkpqwgqlqjteqwgvlhrxqwcvlvwqagvlmyxa'
        pattern = 'qwgvl'
        expected = [1, 2, 11, 19, 27, 28, 29, 36, 43]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_866(self):
        text = 'npeqwnzsjlbnpeqxwnzzwbxenpneqwnzdejnpeqwnivbugnpeqwnzhmj'
        pattern = 'npeqwnz'
        expected = [1, 2, 12, 25, 26, 27, 36, 46, 47, 48]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_867(self):
        text = 'vcqqbisyvcqqbipnjgvcqqbmitcaolvoqqbiwoxgtvcqqabitczbzvcqqjivpwuq'
        pattern = 'vcqqbi'
        expected = [1, 2, 8, 9, 10, 19, 31, 42, 54]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_868(self):
        text = 'sbjwhybhqrwsbiwhybhgfgsbjcwhybhfxfcjsbjwhybhtilsbjwhylbhhclysbjwhybhmhsbjmwhybhet'
        pattern = 'sbjwhybh'
        expected = [1, 2, 12, 23, 36, 37, 38, 48, 60, 61, 62, 71]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_869(self):
        text = 'xlgnttlxxkoexlgnttlxwkerhxlgnttlxjoiylxlgnttlxzbtnnxlgntslxalh'
        pattern = 'xlgnttlx'
        expected = [1, 2, 12, 13, 14, 25, 26, 27, 38, 39, 40, 52]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_870(self):
        text = 'tkyjrdethywxremlthyjyqbzfthyjwsethyjcacsqthyjdv'
        pattern = 'thyj'
        expected = [1, 8, 16, 17, 18, 25, 26, 27, 32, 33, 34, 41, 42, 43]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_871(self):
        text = 'obepfqapvvhxxobepfqapngobepfqapryogobepfqrapxikobepfqalhrobepfqapmzehc'
        pattern = 'obepfqap'
        expected = [1, 2, 13, 14, 15, 23, 24, 25, 36, 48, 57, 58, 59]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_872(self):
        text = 'njkllppitnnjkllrwsmbjkllhmloenjklladuo'
        pattern = 'njkll'
        expected = [1, 2, 10, 11, 12, 20, 21, 29, 30, 31]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_873(self):
        text = 'ersnjyjbersnymhkersjnyqcersnsrufersnyqueooersnyjobersnyesfmer'
        pattern = 'ersny'
        expected = [1, 8, 9, 10, 17, 25, 32, 33, 34, 42, 43, 44, 50, 51, 52]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_874(self):
        text = 'afabymecnjauadbyjyqgauabyrqozdaumbybl'
        pattern = 'auaby'
        expected = [1, 11, 20, 21, 22, 31]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_875(self):
        text = 'mlksydzqbbmlvbsydtkalvsydixmlvsymrxmammlvsyydopq'
        pattern = 'mlvsyd'
        expected = [1, 11, 20, 21, 28, 39]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_876(self):
        text = 'llkectpxffllkecxfllkecwjllkvecyfeksllkeockdvedllkecupgq'
        pattern = 'llkec'
        expected = [1, 2, 10, 11, 12, 17, 18, 19, 25, 36, 46, 47, 48]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_877(self):
        text = 'zeisynarwhzwisynwlpwqzeisymroawzeisynisr'
        pattern = 'zeisyn'
        expected = [1, 2, 11, 22, 31, 32, 33]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_878(self):
        text = 'lbehsxjqktxobehsxaaonlbehsxjxlbehsxfuexiolbwhsxcwrwdlbehsxwklbefsxhbhoz'
        pattern = 'lbehsx'
        expected = [1, 2, 12, 13, 21, 22, 23, 29, 30, 31, 42, 52, 53, 54, 61]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_879(self):
        text = 'vtteydmvhqadvtteydmvjnivtjteydmvldcqvttheydmveozpnvtteydmvflmvtteydmvlqxopvtteydmvln'
        pattern = 'vtteydmv'
        expected = [1, 2, 12, 13, 14, 24, 37, 50, 51, 52, 61, 62, 63, 74, 75, 76]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_880(self):
        text = 'ikvnhjelikvinhjmqikvthjyinfmikbvnhjcelikvnhjvpizdiqkvnhjzucwikvnhjhm'
        pattern = 'ikvnhj'
        expected = [1, 2, 9, 18, 29, 38, 39, 40, 50, 51, 52, 60, 61, 62]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_881(self):
        text = 'dmnphrtiydonphsxkmdonphwzdvnphmnhdynphcqf'
        pattern = 'donph'
        expected = [1, 9, 10, 11, 18, 19, 20, 26, 34]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_882(self):
        text = 'jahyitfbtjahyitfxytsjahyitfdoejahyitfnfijahyitfiugaijahyiufpzju'
        pattern = 'jahyitf'
        expected = [1, 2, 9, 10, 11, 20, 21, 22, 30, 31, 32, 40, 41, 42, 53]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_883(self):
        text = 'ftudxboftucxromftudoxsefftudxvptczftudmxthznqbtudxevftudxgxmws'
        pattern = 'ftudx'
        expected = [1, 2, 8, 16, 24, 25, 26, 35, 46, 47, 52, 53, 54]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_884(self):
        text = 'rockjfpdmlrockjjkxbilrockjnsjrxckjujrocujuog'
        pattern = 'rockj'
        expected = [1, 2, 10, 11, 12, 21, 22, 23, 30, 37]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_885(self):
        text = 'ktkftxgnkvkfbulezlktkfbryjktkfbcf'
        pattern = 'ktkfb'
        expected = [1, 9, 18, 19, 20, 26, 27, 28]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_886(self):
        text = 'mmbybjmgmmmbyhrhemmbyzmbjmbyvcglmibyyzjmmbyohvm'
        pattern = 'mmby'
        expected = [1, 2, 9, 10, 11, 17, 18, 19, 25, 26, 33, 39, 40, 41]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_887(self):
        text = 'hmtpxzdphmatpxbmxxhbhmtpxbpsmhmtpxbomcshmztpxbjqhhrmtpxbec'
        pattern = 'hmtpxb'
        expected = [1, 9, 20, 21, 22, 29, 30, 31, 40, 50, 51, 52]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_888(self):
        text = 'znkejmudsznientewznkerapznkefvq'
        pattern = 'znke'
        expected = [1, 2, 10, 17, 18, 19, 24, 25, 26]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_889(self):
        text = 'waewqqeczgzlwawqqezdiawawqqexyxwawwqqeaulapwawlqekkjuj'
        pattern = 'wawqqe'
        expected = [1, 12, 13, 14, 22, 23, 24, 32, 33, 34, 44]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_890(self):
        text = 'ktfsxxcgktusxxzuffgktusxxvgbktusxxpja'
        pattern = 'ktusxx'
        expected = [1, 8, 9, 10, 19, 20, 21, 28, 29, 30]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_891(self):
        text = 'cqoidxccqhoidjpofnpcqoidyuvldcqoireerxcqokdefdabcqomidxkcqoidjfucp'
        pattern = 'cqoid'
        expected = [1, 2, 8, 19, 20, 21, 30, 39, 49, 56, 57, 58]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_892(self):
        text = 'gogabpihgvcgabpnagvhgabpdbpgvgabpmetengvgabpxvtgvgabbprorfy'
        pattern = 'gvgabp'
        expected = [1, 9, 18, 27, 28, 29, 38, 39, 40, 48]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_893(self):
        text = 'hngmdtxqfxphnmdtxygryhnmdtxoxkihnmdtxpxzyhnmdtxuxhnlmdtxpmsoc'
        pattern = 'hnmdtx'
        expected = [1, 11, 12, 13, 21, 22, 23, 31, 32, 33, 41, 42, 43, 50]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_894(self):
        text = 'qegtucgpajoqgtucbomqgtuczldupgqtuclwrrhqgtucxora'
        pattern = 'qgtuc'
        expected = [1, 2, 3, 11, 12, 13, 19, 20, 21, 30, 31, 39, 40, 41]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_895(self):
        text = 'dszxxgkpcdszxxggcndszxxgfolqdszxxgwvodszxxmgsoo'
        pattern = 'dszxxg'
        expected = [1, 2, 9, 10, 11, 18, 19, 20, 28, 29, 30, 38]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_896(self):
        text = 'spxblepncaspxblepqmeypspxblesxlspixblepmdmfspxolepgjhrwspwblepkzspxbiephsw'
        pattern = 'spxblep'
        expected = [1, 2, 10, 11, 12, 23, 32, 44, 56, 65]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_897(self):
        text = 'xsmmpcxakbopexsmmpcbxateibxsmmpcxatvjxsmmpcxauiaurnxsmtmpcxamrzxsmmpcxazlolaxsdmmpcxaos'
        pattern = 'xsmmpcxa'
        expected = [1, 2, 14, 26, 27, 28, 37, 38, 39, 52, 63, 64, 65, 77]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_898(self):
        text = 'eiewcyaftyiewqbyeiewaskrqyiewifqydyipwcuyiewqwlsoyiewojmr'
        pattern = 'yiew'
        expected = [1, 2, 9, 10, 11, 16, 17, 18, 25, 26, 27, 35, 40, 41, 42, 49, 50, 51]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_899(self):
        text = 'ojbtuzxoojbtumnkxaoujbtuglhojbtuetgojbtuzrbgrojbtuomx'
        pattern = 'ojbtu'
        expected = [1, 2, 8, 9, 10, 19, 20, 21, 27, 28, 29, 35, 36, 37, 45, 46, 47]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_900(self):
        text = 'etqbbirfgetlbbijrtrrmqetolbbirryhetlbbirmsyetlbbirsdt'
        pattern = 'etlbbir'
        expected = [1, 10, 23, 33, 34, 35, 43, 44, 45]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_901(self):
        text = 'tskxnovoxftkxnduvtexnqutkxnjckgtkxnfeititkxneltkxnjl'
        pattern = 'tkxn'
        expected = [1, 2, 3, 10, 11, 12, 18, 23, 24, 25, 31, 32, 33, 40, 41, 42, 46, 47, 48]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_902(self):
        text = 'ymeskmlwymjestdrymesnuwlnzmeson'
        pattern = 'ymes'
        expected = [1, 2, 9, 16, 17, 18, 26, 27]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_903(self):
        text = 'gunexbvujfuenephzcfunesjafuneewgxzfuneoefunehxyj'
        pattern = 'fune'
        expected = [1, 2, 10, 18, 19, 20, 25, 26, 27, 34, 35, 36, 40, 41, 42]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_904(self):
        text = 'ksyeekenzapoksyeeknzlkjoqksyeeknzwzodcksyeeknszxerqgksyeeknmzwcpiksjyeeknzwxjsksyeeknzrih'
        pattern = 'ksyeeknz'
        expected = [1, 12, 13, 14, 25, 26, 27, 39, 53, 66, 78, 79, 80]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_905(self):
        text = 'nrrmewflswsjdnrrhewfligdtnrrmewflzkbpnrirmewflnlednrrmewflasyj'
        pattern = 'nrrmewfl'
        expected = [1, 2, 14, 25, 26, 27, 38, 50, 51, 52]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_906(self):
        text = 'dqpkdrzemdqqpkdyfdqpokdwelwkdqpkdnxfdrpkdavvdqpkdvvox'
        pattern = 'dqpkd'
        expected = [1, 2, 10, 11, 12, 18, 28, 29, 30, 37, 44, 45, 46]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_907(self):
        text = 'pvlgianrmwvlgfbnuhvvlgyfkvvligff'
        pattern = 'vvlg'
        expected = [1, 2, 10, 11, 18, 19, 20, 26]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_908(self):
        text = 'ruwitkzhruowirysruwiqjirupwiwrviirudwiifjsr'
        pattern = 'ruwi'
        expected = [1, 2, 9, 16, 17, 18, 24, 34]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_909(self):
        text = 'hjkzbjryibphjkfbjmtfhjkzbjlmwtfhjkzbjkighxkzbjqxhfkzbjtyshjkkbjjnis'
        pattern = 'hjkzbj'
        expected = [1, 2, 12, 20, 21, 22, 31, 32, 33, 41, 49, 58]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_910(self):
        text = 'phkyakozupaizphkyykozbyxhbphkyykoizyqbzephkyykozzparbphkyykozxkeguphkyykozspphkyykozcwduc'
        pattern = 'phkyykoz'
        expected = [1, 13, 14, 15, 27, 40, 41, 42, 53, 54, 55, 66, 67, 68, 76, 77, 78]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_911(self):
        text = 'woggptxmntoggptifbjstoggptxikqtoggpsxznevtoggppxpfmrd'
        pattern = 'toggptx'
        expected = [1, 2, 10, 20, 21, 22, 31, 42]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_912(self):
        text = 'bnrxeiuuvsdwtbnrxeuuvlpbnrxeuuvcwwnbndxeuuvscvfjbnrxeuuxviczzbndxeuuvqfjh'
        pattern = 'bnrxeuuv'
        expected = [1, 13, 14, 15, 23, 24, 25, 36, 49, 62]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_913(self):
        text = 'akdkypovoakdkyclzckdkeyvgkzakdskyylwu'
        pattern = 'kdky'
        expected = [1, 2, 3, 10, 11, 12, 19, 29]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_914(self):
        text = 'odboalzhxxwodbioalzhbtcyjodboalkzhftndodboalzhyapufodeboalzhksqxodboalzhyy'
        pattern = 'odboalzh'
        expected = [1, 2, 12, 26, 38, 39, 40, 52, 64, 65, 66]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_915(self):
        text = 'yszkuzvppzauyszkuzvpfgrgysozkuzvpfirzgyszkuzbpwdzmiysuzkuzvpobysztkuzvpxx'
        pattern = 'yszkuzvp'
        expected = [1, 2, 12, 13, 14, 25, 39, 52, 63]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_916(self):
        text = 'pupqboniupqbohknxcupqbnlemaupqbovr'
        pattern = 'upqbo'
        expected = [1, 2, 3, 8, 9, 10, 19, 27, 28, 29]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_917(self):
        text = 'nxejenzrbbnxejenkrmpzgtnxejienzrookcnxejenzrbcla'
        pattern = 'nxejenzr'
        expected = [1, 2, 11, 24, 36, 37, 38]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_918(self):
        text = 'xbmjtpjoxmnbojtpjetfbmjtpgieynbtjtpbf'
        pattern = 'nbmjtp'
        expected = [1, 2, 11, 20, 21, 30]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_919(self):
        text = 'jougowuxegwjougowssfjougvowblwocjougowrjptbougowhrzjvugowbxtqfjfugowygcw'
        pattern = 'jougow'
        expected = [1, 2, 11, 12, 13, 21, 32, 33, 34, 43, 44, 52, 63]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_920(self):
        text = 'zbhgrzjyibvxzbhvgrzjnmctzbhgrzjavgpfzbhgrzjybzbhgrzrgouzbhggrzjbfnczbxhgrzjsjoul'
        pattern = 'zbhgrzj'
        expected = [1, 2, 13, 24, 25, 26, 36, 37, 38, 46, 56, 68]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_921(self):
        text = 'dntuczwessdntujzulvjtntujzexdjntujzxyydntujzufdntxjzlri'
        pattern = 'dntujz'
        expected = [1, 10, 11, 12, 21, 22, 29, 30, 31, 38, 39, 40, 47]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_922(self):
        text = 'pojkerdubzpojkerdhuprppojkerdusypwjkerdugcqqykpojkerdukhvsipojkerdsbupojkerdujc'
        pattern = 'pojkerdu'
        expected = [1, 2, 11, 22, 23, 24, 33, 46, 47, 48, 60, 69, 70, 71]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_923(self):
        text = 'owdfswufhfzymwdfswufhxcxowdfswufhdeabwudfswufhhiwdfswufhgxwsdfswufhlvjopwdfjwufhfjz'
        pattern = 'wdfswufh'
        expected = [1, 2, 3, 13, 14, 15, 25, 26, 27, 38, 39, 40, 48, 49, 50, 59, 60, 61, 73]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_924(self):
        text = 'hfpdksjffdgghffdnxsnuhffdjnzmcvffdfelrwhfwfdmscg'
        pattern = 'hffd'
        expected = [1, 7, 8, 12, 13, 14, 21, 22, 23, 31, 32, 40]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_925(self):
        text = 'mvthsdzkqcnsvthsydiesvzhsdeysvthsdyzsvthsdqjhgmvthsdiksvthstdqs'
        pattern = 'svthsd'
        expected = [1, 2, 12, 21, 28, 29, 30, 36, 37, 38, 47, 48, 55]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_926(self):
        text = 'hlqlljaiylrqrzzhlgrqiforhylrqvnhlkrqkqhhlrqatsxxhlrmpeeql'
        pattern = 'hlrq'
        expected = [1, 9, 10, 16, 25, 26, 27, 32, 39, 40, 41, 49]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_927(self):
        text = 'cuguoayoovkcuguoayogxulhcnuguoayomemcuguoayopobqcuguoayomq'
        pattern = 'cuguoayo'
        expected = [1, 2, 11, 12, 13, 25, 26, 27, 36, 37, 38, 48, 49, 50]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_928(self):
        text = 'etdnyhiletdnybofetdnywhllpesdnyhsxetdnyheymeetdqnyhkjw'
        pattern = 'etdnyh'
        expected = [1, 2, 9, 17, 27, 34, 35, 36, 45]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_929(self):
        text = 'kcwxbgksdlvahtkcpxbgksvaikcwxbgsksrscwmkcwdbgksryqvkcwxbgksnybm'
        pattern = 'kcwxbgks'
        expected = [1, 2, 15, 26, 40, 51, 52, 53]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_930(self):
        text = 'czsqagicssczsqvalstoczsqaemznczzqajulgczszawtp'
        pattern = 'czsqa'
        expected = [1, 2, 11, 20, 21, 22, 30, 39]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_931(self):
        text = 'mfyvexvwfyvexfkfyvexufbnfyvexqmfyveztpews'
        pattern = 'fyvex'
        expected = [1, 2, 3, 8, 9, 10, 15, 16, 17, 24, 25, 26, 32]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_932(self):
        text = 'apzwdsvsvapzwdsfxrapzwdsvcvdepapzwdsvkcpapzwdsvtlkapzwdsvxporu'
        pattern = 'apzwdsv'
        expected = [1, 2, 10, 18, 19, 20, 30, 31, 32, 40, 41, 42, 50, 51, 52]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_933(self):
        text = 'iyymlqmrmafaiyymlqmahfkyymlqmtoegipymlqmie'
        pattern = 'iyymlqm'
        expected = [1, 2, 12, 13, 14, 23, 24, 34]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_934(self):
        text = 'pmebrpypgmebrqvihypmebrbvxppmdbrmyawapmebrfydpmebjrrmo'
        pattern = 'pmebr'
        expected = [1, 2, 8, 9, 10, 18, 19, 20, 28, 37, 38, 39, 46]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_935(self):
        text = 'gipayuxoagpaykhnugpaygaknigpayuopih'
        pattern = 'gpay'
        expected = [1, 2, 3, 9, 10, 11, 17, 18, 19, 26, 27, 28]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_936(self):
        text = 'lmyitaljblbqlmyitaljfhvlmyitaljzklmyitaljqsfdlmyitalcjjlyjr'
        pattern = 'lmyitalj'
        expected = [1, 2, 12, 13, 14, 23, 24, 25, 33, 34, 35, 46]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_937(self):
        text = 'xkyqeuiennxoxkyqeuinjdhnxkyqeuyioslkxkypqeuiqefdxkyqeuiwtjw'
        pattern = 'xkyqeui'
        expected = [1, 2, 12, 13, 14, 25, 37, 48, 49, 50]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_938(self):
        text = 'nwjvhbqyowjvumarqknwjvudnwjvpqvtnfjvgg'
        pattern = 'nwjv'
        expected = [1, 2, 9, 10, 18, 19, 20, 24, 25, 26, 33]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_939(self):
        text = 'rpqbamiydkrprpqbayibmrpqbayiearpqbbayictrpqbayiar'
        pattern = 'rpqbayi'
        expected = [1, 12, 13, 14, 21, 22, 23, 31, 40, 41, 42]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_940(self):
        text = 'vizbhuvizbgsyoqvizbbfubvidbwzczvizbnlwvizbbvzlbvizbnokbu'
        pattern = 'vizb'
        expected = [1, 2, 6, 7, 8, 15, 16, 17, 24, 31, 32, 33, 38, 39, 40, 47, 48, 49]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_941(self):
        text = 'nfzmhikqnvfzmcknfwmpycsonfzmsinfzmlhcnwzmzjsxynfzqwbxj'
        pattern = 'nfzm'
        expected = [1, 2, 9, 10, 11, 16, 24, 25, 26, 30, 31, 32, 38, 47]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_942(self):
        text = 'rponywtoijkrwonywtljkkrwonywtisfoyrwonywtscxrwohywtvbasgrwonywthv'
        pattern = 'rwonywt'
        expected = [1, 11, 12, 13, 22, 23, 24, 34, 35, 36, 45, 56, 57, 58]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_943(self):
        text = 'aktvrthqvkjaktvrtotwrtaqtvrtbqhaktvrthpmp'
        pattern = 'aktvrt'
        expected = [1, 2, 11, 12, 13, 23, 31, 32, 33]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_944(self):
        text = 'rhwhktpbahwhkegtarhwwkufulrhwhitx'
        pattern = 'rhwhk'
        expected = [1, 2, 9, 10, 18, 27]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_945(self):
        text = 'onwremlyteukonwrmlyawionwremlyuuyqonwrmlyclzonwrmlyef'
        pattern = 'onwrmly'
        expected = [1, 12, 13, 14, 23, 34, 35, 36, 44, 45, 46]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_946(self):
        text = 'gdfzksywpatagvdfzksywdvgdfzksywfdgdfzksywycorv'
        pattern = 'gdfzksyw'
        expected = [1, 2, 13, 14, 15, 23, 24, 25, 33, 34, 35]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_947(self):
        text = 'aspbyxhvvyaspbyxfgospbyxdklraspbynoqdsraspbyhxrnx'
        pattern = 'aspbyx'
        expected = [1, 2, 10, 11, 12, 19, 20, 29, 40]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_948(self):
        text = 'afhcwzphwzafhcwqpcafhcwjeenfhcwkyqvafbhcwklubkafhcwffdkafhcwxh'
        pattern = 'afhcw'
        expected = [1, 2, 10, 11, 12, 18, 19, 20, 27, 28, 36, 46, 47, 48, 55, 56, 57]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_949(self):
        text = 'wauwnwdviewauwlnskwaubwnwjwaauwnahqzwaauwnutyrwaunwdxvwauwnzzm'
        pattern = 'wauwn'
        expected = [1, 2, 11, 19, 27, 28, 29, 37, 38, 39, 47, 54, 55, 56]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_950(self):
        text = 'egqcomegaczuegankqabegacakusegacfaqegadqghy'
        pattern = 'egac'
        expected = [1, 6, 7, 8, 13, 20, 21, 22, 28, 29, 30, 36]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_951(self):
        text = 'tuskiatcuhimtuskiaxzztuskijawkztuskieaytutuskiajatuskjaqlfyituskiatkzvqk'
        pattern = 'tuskia'
        expected = [1, 2, 12, 13, 14, 22, 32, 41, 42, 43, 50, 60, 61, 62]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_952(self):
        text = 'wnahpfwgxmpwnahpihtuoifwnahspipmcwnahpimkuv'
        pattern = 'wnahpi'
        expected = [1, 11, 12, 13, 24, 33, 34, 35]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_953(self):
        text = 'axerqbimwwshaxerqbiwbtfaxerqbiwbhgnpxerqbiwekiulaxerqciwcktaxerqbiwpwbs'
        pattern = 'axerqbiw'
        expected = [1, 12, 13, 14, 23, 24, 25, 36, 37, 49, 59, 60, 61]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_954(self):
        text = 'zcebhaywzcfebzwgdczccebgpddzceblwhzcebdmmqzceoamk'
        pattern = 'zceb'
        expected = [1, 2, 9, 19, 20, 21, 27, 28, 29, 34, 35, 36, 43]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_955(self):
        text = 'zlkjdanhexzllkjdcgdzlkjdjyzlojdntlczlkdgyzlkjdbdzlkbjdcm'
        pattern = 'zlkjd'
        expected = [1, 2, 11, 12, 13, 19, 20, 21, 27, 36, 41, 42, 43, 49]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_956(self):
        text = 'rxcsovdwrxcsvqgajrxcflkrxlcsqubrxcfyjmve'
        pattern = 'rxcs'
        expected = [1, 2, 8, 9, 10, 18, 24, 32]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_957(self):
        text = 'gvebfaltamgvebfapltepgvebfaltjmgvebftltcu'
        pattern = 'gvebfalt'
        expected = [1, 2, 11, 21, 22, 23, 32]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_958(self):
        text = 'spwgoklqspwgsdspwroxnofspwhmcqki'
        pattern = 'spwg'
        expected = [1, 2, 8, 9, 10, 15, 24]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_959(self):
        text = 'yfqrjfkmwqfqrjqckemfqrbkjwzafqrjdtau'
        pattern = 'fqrj'
        expected = [1, 2, 3, 10, 11, 12, 20, 28, 29, 30]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_960(self):
        text = 'lznqpjgpaepznqpjdyrebmpznqspjqudpznqpjyhm'
        pattern = 'pznqpj'
        expected = [1, 2, 10, 11, 12, 23, 32, 33, 34]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_961(self):
        text = 'krxypcpzsisdkrkypcpmprykrkypopzrwkrkyplcpzwjkfkrcypcpzfukrkypcpzfruiankrkypcpzgcoze'
        pattern = 'krkypcpz'
        expected = [1, 13, 24, 34, 47, 56, 57, 58, 70, 71, 72]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_962(self):
        text = 'ucohgaimljhpcohgahbuxzcohgahnqujcohgaxfysucohgaezk'
        pattern = 'ucohga'
        expected = [1, 2, 12, 13, 22, 23, 31, 32, 33, 41, 42, 43]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_963(self):
        text = 'cbgqgqicjppcbggqicoluwcbbggqiclocbggqicdcgow'
        pattern = 'cbggqic'
        expected = [1, 11, 12, 13, 23, 24, 25, 32, 33, 34]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_964(self):
        text = 'rqymdilxqkymjbufoxqypmntxqymytdqxqzymvreg'
        pattern = 'xqym'
        expected = [1, 2, 8, 18, 24, 25, 26, 33]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_965(self):
        text = 'vpcsohtptvvapcsohthjinvpcsohtcfewwvphcsohtvyrruvpcsohtorvvphsohtdhvpcsohyddkc'
        pattern = 'vpcsoht'
        expected = [1, 2, 11, 12, 13, 22, 23, 24, 35, 47, 48, 49, 58, 67]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_966(self):
        text = 'rkxzhildbnkxzhildxnkxzhilcflgnkxuzhilggk'
        pattern = 'nkxzhil'
        expected = [1, 2, 9, 10, 11, 18, 19, 20, 30]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_967(self):
        text = 'ynobbzobynnbbstgynobubsgqynobbsurqvwynobbgozynopbbslnlkzyngbbsdyaiw'
        pattern = 'ynobbs'
        expected = [1, 9, 17, 25, 26, 27, 37, 45, 57]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_968(self):
        text = 'ptdfzwubcnlptfzwukoptfwzudyptfzwuoxifptfpwuuejbwptfzwubotptfzwuooyg'
        pattern = 'ptfzwu'
        expected = [1, 11, 12, 13, 20, 27, 28, 29, 38, 48, 49, 50, 57, 58, 59]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_969(self):
        text = 'lbtqiuxqlbtciznlbtqeowflhlbtqiuxzuz'
        pattern = 'lbtqi'
        expected = [1, 2, 9, 16, 25, 26, 27]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_970(self):
        text = 'igbzvamaeiiigphvafyadlxigbhvafeigbhvamlgh'
        pattern = 'igbhva'
        expected = [1, 12, 23, 24, 25, 31, 32, 33]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_971(self):
        text = 'hmqryekxvmbycthmqryekxrujhmqryekxiiputwhmqryekxmlcyhmqryekxmhcwc'
        pattern = 'hmqryekx'
        expected = [1, 2, 14, 15, 16, 25, 26, 27, 39, 40, 41, 51, 52, 53]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_972(self):
        text = 'rikqhgljdpnerikrhglllfaqrikihglfurcprikihbgltsgrikihglfzrikirhglforikiyglvv'
        pattern = 'rikihgl'
        expected = [1, 13, 24, 25, 26, 37, 47, 48, 49, 57, 67]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_973(self):
        text = 'uqlhmjtgfbuqauqlhmqtgkmybquqlhmjtgyvfuqlhmjtghpp'
        pattern = 'uqlhmjtg'
        expected = [1, 2, 14, 26, 27, 28, 37, 38, 39]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_974(self):
        text = 'nztkjlpnqtkjfxijlnztkjlinztkjmuepnztkjdy'
        pattern = 'nztkj'
        expected = [1, 2, 8, 17, 18, 19, 24, 25, 26, 33, 34, 35]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_975(self):
        text = 'yhvcqwysqwiyhvcqryhvscsccquyhhcvbtyhvcauyyhycsuui'
        pattern = 'yhvc'
        expected = [1, 2, 11, 12, 13, 18, 28, 34, 35, 36, 42]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_976(self):
        text = 'rwjqxrpkfkcvprwjxqrskherwjxqrhpkbdrwjxmqrpknkoo'
        pattern = 'rwjxqrpk'
        expected = [1, 14, 24, 35]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_977(self):
        text = 'prsnlwgarprjnlgvzqxprrsnltrhkvrsnlzkebprsnlwybeoprsnblujv'
        pattern = 'prsnl'
        expected = [1, 2, 10, 20, 21, 22, 30, 31, 38, 39, 40, 49]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_978(self):
        text = 'errrmbscfudyserrrmbsuperrrmbscsdxeerrnmbscvlhierarrmbsctxcobeurrmbscxipbp'
        pattern = 'errrmbsc'
        expected = [1, 2, 14, 22, 23, 24, 35, 47, 61]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_979(self):
        text = 'utkuvcllnyxootkuvclnpsiarutkuclnxgxugtkuvclngvycd'
        pattern = 'utkuvcln'
        expected = [1, 13, 14, 26, 36, 37, 38]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_980(self):
        text = 'oralapxyoyralxbdboyralofjoralqxkporaljqipbs'
        pattern = 'oral'
        expected = [1, 2, 9, 10, 11, 18, 19, 20, 25, 26, 27, 33, 34, 35]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_981(self):
        text = 'qxwhhdkmexdqxwhdkqkolqzxwhddrluqxwehdiaoqxwhdvbhvqxwhdikhmmqxwhdhnsj'
        pattern = 'qxwhd'
        expected = [1, 11, 12, 13, 22, 23, 24, 32, 40, 41, 42, 49, 50, 51, 59, 60, 61]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_982(self):
        text = 'mculnfyhunmhulnfmylimculnfvopmuulnfiitmmculnfxbpvdculnffmwyi'
        pattern = 'mculnf'
        expected = [1, 2, 11, 20, 21, 22, 30, 39, 40, 41, 50, 51]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_983(self):
        text = 'ldrrufixlqdriufmlzldriufleocoqldriufayw'
        pattern = 'ldriuf'
        expected = [1, 9, 10, 11, 18, 19, 20, 30, 31, 32]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_984(self):
        text = 'qlrjinqlrjgduqlurjxchbqlrjjwqlrljwlslv'
        pattern = 'qlrj'
        expected = [1, 2, 6, 7, 8, 14, 22, 23, 24, 29]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_985(self):
        text = 'xvcxpxzmsdhkxzvcxpxzcxxncxpxzifpnxvcxpxzfuuiqxvcxpizgijol'
        pattern = 'xvcxpxz'
        expected = [1, 2, 13, 14, 15, 23, 33, 34, 35, 46]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_986(self):
        text = 'moyhvnqkpzoyhvngxwzkoyhvnxkoyhvnmskhkoyhmvnztixz'
        pattern = 'oyhvn'
        expected = [1, 2, 3, 10, 11, 12, 20, 21, 22, 27, 28, 29, 38]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_987(self):
        text = 'axuuwtloxtafiaxuuwtloeoamcaxuuwtcopyxlhasuuwtlorpryuaxuuwtyloncpraxuuwktloguaaxuuwtloyspy'
        pattern = 'axuuwtlo'
        expected = [1, 2, 13, 14, 15, 27, 40, 53, 66, 77, 78, 79]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_988(self):
        text = 'ulxnxryfvuxnxrjuxnxkdjruxntpnbueuxnxbwdxwuxnxpdiv'
        pattern = 'uxnx'
        expected = [1, 2, 3, 9, 10, 11, 15, 16, 17, 24, 32, 33, 34, 41, 42, 43]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_989(self):
        text = 'rdeytcgserdeytcnesyzrdeytcqordyetcmuw'
        pattern = 'rdeytc'
        expected = [1, 2, 9, 10, 11, 20, 21, 22, 29]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_990(self):
        text = 'mmelfipdxsvgmmelfipdvxcmmelfipdhpqszmmelfipdnu'
        pattern = 'mmelfipd'
        expected = [1, 2, 12, 13, 14, 23, 24, 25, 36, 37, 38]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_991(self):
        text = 'brhkmdojkcfmrhkmdmmnivbrhkmdenbrhkxdqmfbrhkmduxjbb'
        pattern = 'brhkmd'
        expected = [1, 2, 12, 13, 22, 23, 24, 31, 39, 40, 41]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_992(self):
        text = 'najbongqkxgcanjboygqwpnjbongqeqlcnubongqkhnjbonqgqunonjbongqitivknkbongqzx'
        pattern = 'njbongq'
        expected = [1, 2, 3, 14, 22, 23, 24, 34, 43, 53, 54, 55, 66]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_993(self):
        text = 'hctberjlnxeenhctberjlkmhctbwrjlpmwhctborjluwudz'
        pattern = 'hctberjl'
        expected = [1, 2, 13, 14, 15, 24, 35]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_994(self):
        text = 'aydtzshozhbaytzssfaytzsqsgaaytzevmpof'
        pattern = 'aytzs'
        expected = [1, 11, 12, 13, 18, 19, 20, 28]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_995(self):
        text = 'rwqpbxejdfrwqpbxehvbwserwjqpbxejcqhgkrwqpubxejpzrwqpbxejiuztn'
        pattern = 'rwqpbxej'
        expected = [1, 2, 11, 24, 38, 48, 49, 50]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_996(self):
        text = 'uawjviibekuxuawjviibomnxhjuawjviibqcuawjviibdxzuawjvgiblauawjviibhuqjs'
        pattern = 'uawjviib'
        expected = [1, 2, 12, 13, 14, 26, 27, 28, 36, 37, 38, 48, 57, 58, 59]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_997(self):
        text = 'iuiewqyqsuiuiewggcmabiuiewgxzjkoiuiwewgjfniuiewlzwqiuiewgxodkbxwiuiewgxkf'
        pattern = 'iuiewg'
        expected = [1, 10, 11, 12, 21, 22, 23, 33, 43, 51, 52, 53, 64, 65, 66]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_998(self):
        text = 'pxusqpjfcxufqpaikzlpxufqcpigwipbxufqpcifpxufqphpwpxufqpxnqipxufqpbt'
        pattern = 'pxufqp'
        expected = [1, 9, 10, 20, 31, 32, 33, 40, 41, 42, 49, 50, 51, 59, 60, 61]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)

    def test_case_999(self):
        text = 'ksuvwxfgessuvwxlftghssuvwxfsikcssuvwxfkccvssuvwuxfrjgxssuvwxfedk'
        pattern = 'ssuvwxf'
        expected = [1, 2, 10, 20, 21, 22, 31, 32, 33, 43, 54, 55, 56]
        result = near_exact_pattern_matching(text, pattern)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
