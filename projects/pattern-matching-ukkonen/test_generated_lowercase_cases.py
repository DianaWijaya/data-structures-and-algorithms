import unittest
from suffix_tree_matching import SuffixTree

def pattern_match(text, pattern):
    tree = SuffixTree(text)
    return tree.search_exact(pattern)

class TestGeneratedLowercaseCases(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(pattern_match('lmdbajmylaxuo', 'my'), [6])

    def test_case_1(self):
        self.assertEqual(pattern_match('eciyshinhqjcyihiaberyrrqwywetikghomdpctwujegwsmxfwgnbshpqolviqeieivulhtesdzkzbyzmogexl', 'ciy'), [1])

    def test_case_2(self):
        self.assertEqual(pattern_match('hypaoqkiujspjvbkijdqoxljflowvmdrylhnctaiyfipxxinpexmbyoxqjrg', 'xmb'), [50])

    def test_case_3(self):
        self.assertEqual(pattern_match('fqvmrqqsxvqjyhfhdlfdxileicsdpargnmfdvtbnoxtesefhhmrczxurjudtx', 'v'), [2, 9, 36])

    def test_case_4(self):
        self.assertEqual(pattern_match('vxwxuhryrahqfebobgubqatnqqmbcvegtfwxsbkkzscasytfaitqimqerm', 'hryrahqfeb'), [5])

    def test_case_5(self):
        self.assertEqual(pattern_match('khgdxmqlucnszwyuadlwiskizrsofqamslpkqzrubndstbspmejbovokyvgnsqwvqnyrajsniikgschbxaffmvpqnmdygjmbi', 'ii'), [72])

    def test_case_6(self):
        self.assertEqual(pattern_match('khcqtrqtpmsyrueotkeiglbjvpffzxrcslfkdduwhgzk', 'dduwhg'), [36])

    def test_case_7(self):
        self.assertEqual(pattern_match('lbwpmdlnhayaccugadkhifhnozegoafm', 'dlnhayacc'), [5])

    def test_case_8(self):
        self.assertEqual(pattern_match('fwfbjamayqrgqgxxpwnvhwggozpjpfphekofuexhrtvdujmytyeotpelbzkggxqmyoaj', 'lbzkggxq'), [55])

    def test_case_9(self):
        self.assertEqual(pattern_match('budvvrubnmrycixtwjijmibkyoralrhnbklticskhosezjgbitrpj', 'jmibk'), [19])

    def test_case_10(self):
        self.assertEqual(pattern_match('odwdtlyhcnhcuzywqnoqrljxcqgvyglogpybotlvttrfkl', 'ot'), [36])

    def test_case_11(self):
        self.assertEqual(pattern_match('lfidhtgarzmdymrbfxngnmpkfpgkmtthrtuddnwbgonynvodhckjbncfpop', 'dhc'), [47])

    def test_case_12(self):
        self.assertEqual(pattern_match('srpnwtohhadlmcjqnbdsuplauukuozsujvwtqdunmtkybwktofyvkqqwjpcoxmodrtgwurwcjamkjgtln', 'kyb'), [42])

    def test_case_13(self):
        self.assertEqual(pattern_match('qhxxgtemcfhepbrzqbvgomtzsizzusrivprjadeypzskkhalhzauqayhp', 'ayh'), [53])

    def test_case_14(self):
        self.assertEqual(pattern_match('uefsenziechapfgdhbwawbxwyjeonwxjgtiibczhavcpiacehmxblggwjyrcg', 'efsenziech'), [1])

    def test_case_15(self):
        self.assertEqual(pattern_match('qishsiodzqj', 'shs'), [2])

    def test_case_16(self):
        self.assertEqual(pattern_match('czlqypvvbyxpvqmxwdgvfmtjatvicrcrfxqfpylcxxulmfancnfqhvhxejyonvsrekawlsrwcgtr', 'lmfan'), [43])

    def test_case_17(self):
        self.assertEqual(pattern_match('nmhzfbxotdbujzpdxztpq', 'tdbujzpd'), [8])

    def test_case_18(self):
        self.assertEqual(pattern_match('vdktwkhucpdzgzozshhjabfqgelcaztnlcjamiihjiowzdjkxcresravacgxms', 'zgzozshhja'), [11])

    def test_case_19(self):
        self.assertEqual(pattern_match('hfruzkrcthlimfgvs', 'imfg'), [11])

    def test_case_20(self):
        self.assertEqual(pattern_match('npvfbsvmeejiklscsrpeyikqzpcsgbquetlbuyiqjvmkoxjxysxfxldhsfcwngcyambo', 'ysxf'), [48])

    def test_case_21(self):
        self.assertEqual(pattern_match('gqpfyyasyq', 'qpfyyasyq'), [1])

    def test_case_22(self):
        self.assertEqual(pattern_match('akgehlxpjrzccapoeigtidmirlflqrxpthjaihgarykwmuxxxhpvwdotowsbcqtxlgvtinvqtwvtelsfcnvjopwv', 'poeig'), [14])

    def test_case_23(self):
        self.assertEqual(pattern_match('mmxoaumynnagvxlpsscoolvahezvjaiwjqpotybllaoyczambfprvcpawpxvwewnckfr', 'ynnagvxlps'), [7])

    def test_case_24(self):
        self.assertEqual(pattern_match('odhrqxuesdadftvzvkmltfyzphkkqyejhjvphog', 'fyz'), [21])

    def test_case_25(self):
        self.assertEqual(pattern_match('wvkvmqhjxxtxyskiq', 'k'), [2, 14])

    def test_case_26(self):
        self.assertEqual(pattern_match('trgngncmsgootbvgbckszsywvitktdsrshvjbcwqkdldyfvltrsdstfdsjqtfpfledfalkkdbyvqv', 'qtfpfledfa'), [58])

    def test_case_27(self):
        self.assertEqual(pattern_match('glgzomvojjgbrsmhonoalroobgtxlwmk', 'obgtxlwmk'), [23])

    def test_case_28(self):
        self.assertEqual(pattern_match('ltgquxnfwbnwphystzmfuruamqaziztzvayhzgjiiaqtzcqwuzfbswnetrxorjmts', 'tzvayhzg'), [30])

    def test_case_29(self):
        self.assertEqual(pattern_match('bstbeeibqeimoisvumukhurzdmhpcogqoaclhjlrdleyatwakbpxiqvgktzprtmvzbqqyepkqphudjnrzbxzuzin', 'ur'), [21])

    def test_case_30(self):
        self.assertEqual(pattern_match('lnidsrugxklziejr', 'dsr'), [3])

    def test_case_31(self):
        self.assertEqual(pattern_match('zizspwxaqzfmrsepqbzqxnizovpiukhbvzwcuagegsyxokxjidxkzxniyxfexoxbyxdcakyfrcbzzxhxhelnvtwyik', 'xni'), [20, 53])

    def test_case_32(self):
        self.assertEqual(pattern_match('nrxxtemsvvdyosnuzshyorhaahnduk', 'zshyo'), [16])

    def test_case_33(self):
        self.assertEqual(pattern_match('epspmfvztwknyruw', 'ztwknyr'), [7])

    def test_case_34(self):
        self.assertEqual(pattern_match('ernkkhtzciqyydctvkrokwxrizhstvowvaesbhjdxsrpac', 'esb'), [34])

    def test_case_35(self):
        self.assertEqual(pattern_match('npqfradyywwvtsnvbolksptqnubgqqioqxiqrxrvvbhciubswhglqrdcgsemfbzeoiembcznukgfrxp', 'qfradyy'), [2])

    def test_case_36(self):
        self.assertEqual(pattern_match('sytfvgikavogpoangamajuxlo', 'fvgikavog'), [3])

    def test_case_37(self):
        self.assertEqual(pattern_match('mdxoowmvxiwvoozvmvpyhumfowngtneqkklljanbwitmqycyyvsoydeonkncktaltkoinuoisldbjtdazxwwppbpj', 'wvoozvmvpy'), [10])

    def test_case_38(self):
        self.assertEqual(pattern_match('vmdqievugcrodmwihrcanrnguoauyxfswdovrshhosvviziahodalekcmuxcumaaetdmonnbgwfdthyyyvfm', 'dthyyyvfm'), [75])

    def test_case_39(self):
        self.assertEqual(pattern_match('dcqjxtlyscgzioyb', 'oy'), [13])

    def test_case_40(self):
        self.assertEqual(pattern_match('dxffykvaomxnyfkksuxuhcjtasfbdfhauftnjaxfpqmyelebrtzirdyocqcecyxczkrvkmnsvjbolpnohilqn', 'xczkrvkm'), [62])

    def test_case_41(self):
        self.assertEqual(pattern_match('mrmykzwxrawbejvcyzng', 'kzwxrawbej'), [4])

    def test_case_42(self):
        self.assertEqual(pattern_match('edzsnflusdznl', 'dzsnf'), [1])

    def test_case_43(self):
        self.assertEqual(pattern_match('coeexxwwptswrabfuteqvdlsjojzaytfubredirszvahmkginbsizdloxxscpwipgcwar', 'sizdlo'), [50])

    def test_case_44(self):
        self.assertEqual(pattern_match('glitrufscawpinnxyrsmuuisivniqsrnttmnxhrkzgfvuoxojtaskpnmttlrdfjdxcekoeutshkblqkpzxngqb', 'dfj'), [60])

    def test_case_45(self):
        self.assertEqual(pattern_match('vluqexkqlbibqaqcuaehvjqznjuzlvvoppthhdwgafggzspbkvjmlislcqrwgetxn', 'qexkqlbib'), [3])

    def test_case_46(self):
        self.assertEqual(pattern_match('zaqivejgespraepsncvtxqjxrboumkyeomxqva', 'rboumkyeom'), [24])

    def test_case_47(self):
        self.assertEqual(pattern_match('bvciyvopvxkmn', 'yvop'), [4])

    def test_case_48(self):
        self.assertEqual(pattern_match('cmalpqnwakcsepfgnjcyfqbhskvtpnjudzkbeerjoosnjwd', 'erjo'), [37])

    def test_case_49(self):
        self.assertEqual(pattern_match('hyxiyqeuurvdgcrsbaakkcdskytyyxrnushzsgxcwhydasfkfxrghpsmghqiaxmmgewmcuaudvnhjzpipusepfcpnpzdoregja', 'crsbaak'), [13])

    def test_case_50(self):
        self.assertEqual(pattern_match('hbyrsvzavppr', 'svzavpp'), [4])

    def test_case_51(self):
        self.assertEqual(pattern_match('wbolwubyacvajgzqvpzeftkneyslfpibbrqqpejdteawbztuzougkqapsrezyaa', 'ztuzougkqa'), [45])

    def test_case_52(self):
        self.assertEqual(pattern_match('pusyzloxlrrpwmyowrnvoxvnwdfurfwwaiohscwmujliuwsbafenxhuhucgrrid', 'scwmujli'), [36])

    def test_case_53(self):
        self.assertEqual(pattern_match('rdxbkyyxbpabanxfkavfgljxnsgfzcttrbp', 'sg'), [25])

    def test_case_54(self):
        self.assertEqual(pattern_match('rwtjbnpbthiydgearuyfcrxkcyzgccmflqznsnwhoocyahdzqnyfbpkrbjorfgmmvn', 'pbthi'), [6])

    def test_case_55(self):
        self.assertEqual(pattern_match('zlatecgcqgdizyftmpvhewngcnbnyopscimlwunprnjevdnywpugobmrxemhihaiancrfjkjlbsggwrwrvvnwedrbbycrlzdeksj', 'hihaiancr'), [59])

    def test_case_56(self):
        self.assertEqual(pattern_match('zffagmofdodzqqcldjixrvyxxxxcyshmu', 'djix'), [16])

    def test_case_57(self):
        self.assertEqual(pattern_match('hxxgndxnvaxdwbvmezwqnabroibkbmygbwgprarzjpgcmbutr', 'broibkbmyg'), [22])

    def test_case_58(self):
        self.assertEqual(pattern_match('afxatnutljwnvepxpjikdylamqlirqwwwrmzfqdnqrtulmayyvttluahzapvogsz', 'afxatnutlj'), [0])

    def test_case_59(self):
        self.assertEqual(pattern_match('xbpweahmugpaeyvupfoztncnrosyyrulboajxcbooazgtpomzyhk', 'ajx'), [34])

    def test_case_60(self):
        self.assertEqual(pattern_match('bkpovsjdcvklxwgamyxrabvvxlwslernwtydvqjzovrpclfggxlkbljgloteovyg', 'qjzovrpc'), [37])

    def test_case_61(self):
        self.assertEqual(pattern_match('sbiaoimlmqgdtlopxgyopxhiucajnusgjvrfddxtifyychmywhopnu', 'myw'), [46])

    def test_case_62(self):
        self.assertEqual(pattern_match('rbarrzjsafevpkpugvuhf', 'jsafevpkp'), [6])

    def test_case_63(self):
        self.assertEqual(pattern_match('utoncvtcfowqeicmvylkbflrphxdxcrwvassheubmyhiouv', 'yl'), [17])

    def test_case_64(self):
        self.assertEqual(pattern_match('imcccsshdoiwehyfsiromlwpzbpkqcsftcoanffdrqgkgvskfq', 'qgkgvskf'), [41])

    def test_case_65(self):
        self.assertEqual(pattern_match('zuanfxtcihpqbhtvumkkjuzzdjbepllwrqsausjdmenqqfrehxqrpmydtlrtkvwg', 'jb'), [25])

    def test_case_66(self):
        self.assertEqual(pattern_match('zjqzmmbdvwrmjvgmkbvpckpgwfnnamvgvslicu', 'vgm'), [13])

    def test_case_67(self):
        self.assertEqual(pattern_match('vfymzfpeozxskutkfiraxmvqmokfwiegkgzkaaezxkillijjtivnoqavosjdukarnizgmhavoh', 'zxkillij'), [39])

    def test_case_68(self):
        self.assertEqual(pattern_match('afrvwifjebwkmlyumhry', 'u'), [15])

    def test_case_69(self):
        self.assertEqual(pattern_match('pgwnuvtyssahankilltvamouqilxtgwcstuckayekxvnpnclktkvsfffijowympgespq', 'tgwc'), [28])

    def test_case_70(self):
        self.assertEqual(pattern_match('ltzgsinwxwlvxgnpmpvtsbydfbwptbnsqtcgnchlejhoswpdjpnagpgoaydultnhjewefliywciwatmlicebihhqgiu', 'hhq'), [85])

    def test_case_71(self):
        self.assertEqual(pattern_match('ltxvylsyjkvjyfuxhiiwblqnabqifjnrbaclaxdcsdaoul', 'claxd'), [34])

    def test_case_72(self):
        self.assertEqual(pattern_match('gzcfdgtrqwkeemgkkyoludxawvomwvnoowknascmkrasjzjxiolfdaeydpyikurqrybwnpumyngczowevxavvsnmoz', 'yikurq'), [58])

    def test_case_73(self):
        self.assertEqual(pattern_match('ayoxpcfoppqggwvymrzwbyeuuxrbhhk', 'vym'), [14])

    def test_case_74(self):
        self.assertEqual(pattern_match('cttwcbgnwwifrtruhwndruvaopndvbcvlgldscvirawxylemotojqwxapdvhnneuhxazzvtauwrqkxrtqlblkzheojcj', 'kzhe'), [84])

    def test_case_75(self):
        self.assertEqual(pattern_match('tdlnwlendwhnoklhdqqgdsqvkdkquowdvztpmku', 'wd'), [30])

    def test_case_76(self):
        self.assertEqual(pattern_match('navqyqviauyjekyrfndyl', 'yjekyrfnd'), [10])

    def test_case_77(self):
        self.assertEqual(pattern_match('dijucsoslzkyjhejcucqcrkaegkegz', 'yjhejcuc'), [11])

    def test_case_78(self):
        self.assertEqual(pattern_match('jfoffwttvihxqkegwkuphsgmwdakrcohlxkwuypellkpntnbitdyco', 'kegwkuph'), [13])

    def test_case_79(self):
        self.assertEqual(pattern_match('oaohrhehkmsoxohkbydtxsdcntbvxkmblqldgpfbdurorywonxjakzxsuwljtbcdqafajehwqadmsnxlqvon', 'ywo'), [45])

    def test_case_80(self):
        self.assertEqual(pattern_match('pqvrqhsyuiwldpolmvgnazsnhhfmyjwvyyuwvtuhlakijejusnrbbrasrfvmngsxakwijojdtzwqphcumobfwb', 'wldpolmv'), [10])

    def test_case_81(self):
        self.assertEqual(pattern_match('hlpepryhjhcnndfsrhqghcpinkeakthyvfjxbmcbzktchkpusinqktcjvqvdhdexrfsscnaeejrxojoqlffjwtgisrqxcufnxvv', 'cbzk'), [38])

    def test_case_82(self):
        self.assertEqual(pattern_match('xiwceipedofiszkfjymeqfvogpkcanatfwugtgyglqzdjpvqsmolnvqziubhkenvuahnxchpq', 'xiwcei'), [0])

    def test_case_83(self):
        self.assertEqual(pattern_match('mjemycfgebfz', 'mje'), [0])

    def test_case_84(self):
        self.assertEqual(pattern_match('bsgrhxukguwewbhrix', 'grhx'), [2])

    def test_case_85(self):
        self.assertEqual(pattern_match('xrnqpcqrztqkulefbovxkqwaxwgtjhqnnjdtzqqcrzziielrkcfzgvfkcwthpxvonkjebmucyywdm', 'jdtzqqcrz'), [33])

    def test_case_86(self):
        self.assertEqual(pattern_match('nueqcgfhvmjbpwuamlootbyqgfihwokscfospaskoznkwkzxhmeccdmcufsunjodiptvoaohvdhqunztefpss', 'okscfospa'), [29])

    def test_case_87(self):
        self.assertEqual(pattern_match('zvtingsgkqniucwegfzukaynraxtuzwbuyhugmuqmxd', 'uc'), [12])

    def test_case_88(self):
        self.assertEqual(pattern_match('clkxoiuqkmsidvfuyiakikjtagizhjmceoprfmakuocxiqnkxsdvlfgsfxrf', 'hjmceopr'), [28])

    def test_case_89(self):
        self.assertEqual(pattern_match('fbznfcxbiqkxvzibit', 'qkxvzi'), [9])

    def test_case_90(self):
        self.assertEqual(pattern_match('hyuuogpuhptubcqgawjjnzxmshtazmzfllxxlr', 'hyu'), [0])

    def test_case_91(self):
        self.assertEqual(pattern_match('pyyppfgdvpkhyshzjvx', 'j'), [16])

    def test_case_92(self):
        self.assertEqual(pattern_match('sinugpqoqaeikdpqwhoxvxxjjtpxwiislvssmtcgrgeuzpovrmj', 'xw'), [27])

    def test_case_93(self):
        self.assertEqual(pattern_match('ymvscksjlycssmthcvjnpzaaqrzytpokfsdarxofwkbmvmbqobhwa', 'ycssmt'), [9])

    def test_case_94(self):
        self.assertEqual(pattern_match('ofdgriyrjymhpnfqfcqtiquqyngtshcheuixrcidjaepwbaqjghbudeumthwzzjxy', 'thwzzjx'), [57])

    def test_case_95(self):
        self.assertEqual(pattern_match('xmvtbhcttjctjwevoqhqqplzkdces', 't'), [3, 7, 8, 11])

    def test_case_96(self):
        self.assertEqual(pattern_match('oyamnrcwpxlbaofaoczvbcjhrluowvmssfclysfdvxtsxll', 'pxl'), [8])

    def test_case_97(self):
        self.assertEqual(pattern_match('qjdtwyyzhoesbjeffyzmkxuhltnjrjtrobjlgkeertjdabunrcbqrgbonkvptfgfqxrqcbta', 'sbjef'), [11])

    def test_case_98(self):
        self.assertEqual(pattern_match('kvjjfmogpqjkgteowppqxqilwrdnoloziztdbgfktqudcqmocsxwcejoaxtue', 'teowp'), [13])

    def test_case_99(self):
        self.assertEqual(pattern_match('pueofrqvlozcvyabjunpcjfmtnwyxzivzfzlpamsettblqlknfnavtxlxhgmoxzcxbzfzxaovymfchf', 'pams'), [36])

    def test_case_100(self):
        self.assertEqual(pattern_match('cxermekzjscyhsemaagjskgzvadgywmpopersdvmvrmehpudtrunbfcdwdxa', 'scyhsemaa'), [9])

    def test_case_101(self):
        self.assertEqual(pattern_match('ibfagphesemjyewczitodkcwnilphfeosulvxqfwvhyy', 'fagph'), [2])

    def test_case_102(self):
        self.assertEqual(pattern_match('rdsreppzipjidqiwo', 'rdsreppz'), [0])

    def test_case_103(self):
        self.assertEqual(pattern_match('acmcbkxffcbllfwoouvnjmrytubvxovewwtqkahmggghqulvij', 'uvnjmry'), [17])

    def test_case_104(self):
        self.assertEqual(pattern_match('swmumljmnlqnaonxehzujefzxnjhgufqkniljxrtfsmfbxhnyefydoae', 'nyef'), [47])

    def test_case_105(self):
        self.assertEqual(pattern_match('judgdazhbptwlrqcdkywkkgiqqfpsrepyguzflnmcdmrtbuyexngmdbrfhdkttsfqmzlpubbfvhuimlyljungxxmcowxxincy', 'mlyl'), [77])

    def test_case_106(self):
        self.assertEqual(pattern_match('exuxjqhcddpzwseycpeecdjrhrnvhhnarkyjihqgmcopycvvkqmmfzeigivvsqkkgsgb', 'ark'), [31])

    def test_case_107(self):
        self.assertEqual(pattern_match('mrdnlbpshpeeiyprhglnxwbyfdac', 'm'), [0])

    def test_case_108(self):
        self.assertEqual(pattern_match('zyuktgekimkaydlbkaevdbnykerzqfbilggybmnahtw', 'imkaydlbk'), [8])

    def test_case_109(self):
        self.assertEqual(pattern_match('mocjgaowiyomssaoschjhbdxgxneoxlallytndfzkvzzhufgxo', 'zhuf'), [43])

    def test_case_110(self):
        self.assertEqual(pattern_match('dqolfcyvndvsuipqmyqhipjxvweyrcuniknfrsa', 'yqhi'), [17])

    def test_case_111(self):
        self.assertEqual(pattern_match('uuccaqmdobwquuoxrxnssxejamkwujmhbzcmcxhysyhqhehxroloqkdkezctijyceqpbiknsskqkofxvabgokopmrvflhshkl', 'knsskqkofx'), [69])

    def test_case_112(self):
        self.assertEqual(pattern_match('xehqhoacyfueikwtoxoawazw', 'oac'), [5])

    def test_case_113(self):
        self.assertEqual(pattern_match('ynmlpmqndshcwwrjjxlpgxcgdwktcbwxernpccmxtwyucolkdxkwjdopaqweinnkoabxclysgvljrfsqzs', 'dwkt'), [24])

    def test_case_114(self):
        self.assertEqual(pattern_match('wssmqcdtjhlgyzpfoygwdqnjt', 't'), [7, 24])

    def test_case_115(self):
        self.assertEqual(pattern_match('ebkerqnfzcdjqhmkhygibcynzlblzmgrfnlrbnepyryjjzccnwdbnrmhaosrapxaahwbosrugkqkvospojyomliewumdqa', 'rqn'), [4])

    def test_case_116(self):
        self.assertEqual(pattern_match('lzencyqsycgtzbzksioervpvcvgxidugpnxiwqixtviwlqcbmwjemeijpqmisebsgtvtzhmaybclihkpfpskubmuademich', 'lzenc'), [0])

    def test_case_117(self):
        self.assertEqual(pattern_match('hzkkdecbtgoja', 'kkdecbtg'), [2])

    def test_case_118(self):
        self.assertEqual(pattern_match('chbvbcbuiitajuon', 'hbvbc'), [1])

    def test_case_119(self):
        self.assertEqual(pattern_match('lqwtjqksrulkdqwylizawzrkbhilhsrn', 'n'), [31])

    def test_case_120(self):
        self.assertEqual(pattern_match('kqwgmzxeglwkpkiydurvdnsddzkuymkntrzltthclifmofmrylogqdppwarushrpyetcflqbpfajzhphkfaodrqyxtdubtykhex', 'fmofmrylo'), [42])

    def test_case_121(self):
        self.assertEqual(pattern_match('uslepgwpgafmkgqbjdaehdllggeduncufgkdtdqtiysohidombarbdljdgybtyazjoxlqvpixvpczxrrfhxomnlrrzdrxoavqjz', 'yazjoxl'), [61])

    def test_case_122(self):
        self.assertEqual(pattern_match('ygsgklxterzqvmblrikdsolfghfvvqshzeatffl', 'vv'), [27])

    def test_case_123(self):
        self.assertEqual(pattern_match('mbfizoslshrtlsaqcgcbnlhzmxkfgzfvpqmzjxkbsyjxikdluvlirosjchdneefomnglgzwgutfjmflaarlstjrexxxojd', 'rl'), [81])

    def test_case_124(self):
        self.assertEqual(pattern_match('bjuqdihvcqleehv', 'ihvcq'), [5])

    def test_case_125(self):
        self.assertEqual(pattern_match('luskewymplcwerbu', 'mplcw'), [7])

    def test_case_126(self):
        self.assertEqual(pattern_match('wtonrxzsoawmfmjaintecoxoqtjafpdqiklkkcxrazqgmvtjwhmrkghrfhd', 'c'), [20, 37])

    def test_case_127(self):
        self.assertEqual(pattern_match('wdcelenbtgqsoqbpmnimkmcsetznyelz', 'pmnim'), [15])

    def test_case_128(self):
        self.assertEqual(pattern_match('qicxflnfgyyccmibsvyowjecjp', 'fgyyccm'), [7])

    def test_case_129(self):
        self.assertEqual(pattern_match('qoddxocctiruayejuyklrwcihhpekxmwhppwkyomlfkmubpifvzwghonvpwbbejbgidwpreyagcoqhsldxbltvruzgvzplqm', 'mwh'), [30])

    def test_case_130(self):
        self.assertEqual(pattern_match('qlhmkwwzugxjqyopyuawjzv', 'qyopyua'), [12])

    def test_case_131(self):
        self.assertEqual(pattern_match('renicunqweltpaovuxvlcuqbrhafkyfuxkuhtnjccrhvumtjvjpv', 'h'), [25, 35, 42])

    def test_case_132(self):
        self.assertEqual(pattern_match('rkcoylegncyytsferbcupfotcwqdqtgkrkcpsvpntrlwceonqqyediderbnybnbmsdpwyyhkgwbkcgysoqyrlxeazziznuj', 'trlwceo'), [40])

    def test_case_133(self):
        self.assertEqual(pattern_match('ycfzqdvncmcwpquwhndmmaxjscvupbsxvksrbpzjzhftxrtjaatlxksgztqkgcgfnnftmqsrzlxqcqvnecng', 'aatl'), [48])

    def test_case_134(self):
        self.assertEqual(pattern_match('nizlpgyobbfrutuwaeocotolpdvqnybkjaemmbr', 'vqnybkjae'), [26])

    def test_case_135(self):
        self.assertEqual(pattern_match('zffezthxkfkrurdhfibjlceraqdvhukefagkzsbxtcmvadyjsnwydxpknmtyobywshfsjgzpvpcpegxponxykwgvpkdt', 'lceraqd'), [20])

    def test_case_136(self):
        self.assertEqual(pattern_match('pwhfmteluexiqfkfgianakdjwiyyunxxsokmghprhajkddukwbjobcbiprtd', 'hprhajkd'), [37])

    def test_case_137(self):
        self.assertEqual(pattern_match('qpaqtqsshdtcfbpqhrgwvhsrkufkzgsb', 'hdt'), [8])

    def test_case_138(self):
        self.assertEqual(pattern_match('zdurwniuzmxogwpjkkieyowhghrzyaxozrimakswelrliesr', 'uz'), [7])

    def test_case_139(self):
        self.assertEqual(pattern_match('knckufdgwnbuhpbxhytumgpsipaxyvwqypvcsuiughtnlzup', 'ckufdgwn'), [2])

    def test_case_140(self):
        self.assertEqual(pattern_match('uuubtpipfefefptfcfrtzdliatgwlswrpmpghorbkpenrpjkwvdatcsexvbpuwolsvh', 'ubtpipfef'), [2])

    def test_case_141(self):
        self.assertEqual(pattern_match('dxkeamjzlpyxsjwnafteopjbqydgmvszfhpaemrovruyknohmfw', 'o'), [20, 39, 46])

    def test_case_142(self):
        self.assertEqual(pattern_match('lfhfhrdwbocqgajehrdbzvrisejcgmebfysutimbfwawymzoqzasgdwdbqwkcajpfxfjj', 'mzoqzasgdw'), [45])

    def test_case_143(self):
        self.assertEqual(pattern_match('viirvkgdagsakbujitxy', 'irvkgd'), [2])

    def test_case_144(self):
        self.assertEqual(pattern_match('xkzwwgtcikxzjdyhutojexuqjkxeejargvqveszyvfgkxymszpdmwyxlcsuqctlzardunutxn', 'dyhutoj'), [13])

    def test_case_145(self):
        self.assertEqual(pattern_match('yibofrdazalsktdefvnflfuhdwxbxjnvthxbtuncxzygjveldmahptymdblnbvuubprjwpgmhzopqyeawvbrdmxnhoteq', 'vuubp'), [61])

    def test_case_146(self):
        self.assertEqual(pattern_match('qragwneilyxehhshbjatdafgvpsglujkwcrhuiebmjphuerlzirvhf', 'hshb'), [13])

    def test_case_147(self):
        self.assertEqual(pattern_match('sftrpiqaskamavcuassxclcjoddwmuoqbybxokzsrqkgrpdymegee', 'ask'), [7])

    def test_case_148(self):
        self.assertEqual(pattern_match('fbvzpndkhxcevbljkjtnfhfxfzxqmqmyqkmofzabqzlsybnlrzmozabesyeqcrsnttccrkufywkufla', 'lrzmozabes'), [47])

    def test_case_149(self):
        self.assertEqual(pattern_match('smqsrgfdzuddriasvplppiqhsqrsfutocizpiynuvpeycqwfgzqgygdsfphwhnvbcjyoz', 'sfu'), [27])

    def test_case_150(self):
        self.assertEqual(pattern_match('azoslyhsfozfelftqikmumxsgbmcrurnpcjsiaqobetvncuiyoxzmuysyybqeapyrhgqyymejpzzbhf', 'lyh'), [4])

    def test_case_151(self):
        self.assertEqual(pattern_match('eglhmheemodpj', 'eemodpj'), [6])

    def test_case_152(self):
        self.assertEqual(pattern_match('mxochyntfjrkxgftiecldixocxhotmwpxexinol', 'yn'), [5])

    def test_case_153(self):
        self.assertEqual(pattern_match('cefamqftiqphydmvamnoejettbwkabdmypynzbskcgfpzfgmarjnlqtimrvqaefvelqshrjybkegzakgldapxhzkxopnirtvbham', 'lqtimr'), [52])

    def test_case_154(self):
        self.assertEqual(pattern_match('imkxavkujalzaufcjzmdqyckggqwxtbwmhmrsjcvjcjgehswdgdurhzlntqtdgbkrvpqlykbheinokks', 'zaufcj'), [11])

    def test_case_155(self):
        self.assertEqual(pattern_match('snehfprbbvtylhzwrqbee', 'prb'), [5])

    def test_case_156(self):
        self.assertEqual(pattern_match('sxpnufsmgvjctjbmgtttnruomezpblpfpdvxggzgzxvuunctcnldyusrtqvmjtkkbkrqv', 'ldyusrtqvm'), [50])

    def test_case_157(self):
        self.assertEqual(pattern_match('yyqongaooaslzafvghlpynliqpkjixqpoivztxxtdivbhcxyuosymbfytojawdykmptvuiakgpvexzzornbwynnt', 'mbfy'), [52])

    def test_case_158(self):
        self.assertEqual(pattern_match('vnwzzgnfyqqfsrfxtrnsfcegwxualmkoolhjnjcrhsgambzgjjazvuyfaidvkzimzaevyqlabicqnnrdwtrtcbkwaj', 'nnrdwtrt'), [76])

    def test_case_159(self):
        self.assertEqual(pattern_match('lnsdgmlshz', 'dgmlsh'), [3])

    def test_case_160(self):
        self.assertEqual(pattern_match('penbverwrkqpkywxoxdzueahjndasveozpzrylxflrocjcc', 'pkywxo'), [11])

    def test_case_161(self):
        self.assertEqual(pattern_match('wuvsrrvxaylhjmlepqycnjyvbnprrzymo', 'lh'), [10])

    def test_case_162(self):
        self.assertEqual(pattern_match('ibevgsetkjwlvniajviclmlx', 'kjwlvnia'), [8])

    def test_case_163(self):
        self.assertEqual(pattern_match('vdfhilczmsdvzctvbnuyrtfx', 'vzc'), [11])

    def test_case_164(self):
        self.assertEqual(pattern_match('jthqdkrxmuqdpghahnxhsnzpeyueuujumkpcxjwvaxzzyppdqvyfqhssjstoosvengdmivlpc', 'yfqh'), [50])

    def test_case_165(self):
        self.assertEqual(pattern_match('uolqiwhouzbtymlvjohgkdtldxctnfakqnvhyslwsnluftujxqogbldinryiqqnvcinzosshxqibrntxgxdnfoaih', 'qqnvci'), [60])

    def test_case_166(self):
        self.assertEqual(pattern_match('uvgqsmtymynopkuvpbrghuzfkbqawigtbmxnmv', 'w'), [28])

    def test_case_167(self):
        self.assertEqual(pattern_match('cvilkgndrijzofglkbcfjwaogxncyfnprkknvqptzmsli', 'prkkn'), [31])

    def test_case_168(self):
        self.assertEqual(pattern_match('oviztlovwuxpflnpyjdwujifwgalvebeafhbkgy', 'pyjd'), [15])

    def test_case_169(self):
        self.assertEqual(pattern_match('twgqnzjhsb', 'n'), [4])

    def test_case_170(self):
        self.assertEqual(pattern_match('pzgnbhluavkjfjnxzgykmoqr', 'vkjfjnx'), [9])

    def test_case_171(self):
        self.assertEqual(pattern_match('kzkylqyqfjapqrjkrwyckcrrdcnaersllcivozsdjlrqfdbtyognkplsndguaip', 'tyognkp'), [47])

    def test_case_172(self):
        self.assertEqual(pattern_match('xvceulzgoehncpjzypqhvogfrdknzjetrzippttxfboqualcuktqlmuqbgrutibgzs', 't'), [31, 37, 38, 50, 60])

    def test_case_173(self):
        self.assertEqual(pattern_match('xvustyadlxlelw', 'a'), [6])

    def test_case_174(self):
        self.assertEqual(pattern_match('ssksafnhcouvmdekkljcrynaxhnxrozaxmuvemdzgtuspyqtbifbvtzbxwodsweprfkvuvyuzsqxngbnmrmltepetqltaepjpz', 'uzsqxng'), [71])

    def test_case_175(self):
        self.assertEqual(pattern_match('yqoifqkwptgbnnyavzzhjqzdkimufeqtwcexubsyrdtkcldamshudidzqeukhnrgfukktzllyhl', 'qoifqkw'), [1])

    def test_case_176(self):
        self.assertEqual(pattern_match('szwueuzsrjceoylrvmzmpurlwxynntmrtsliizgybwwyrozxhcuiialurbjihtjmfpo', 'm'), [17, 19, 30, 63])

    def test_case_177(self):
        self.assertEqual(pattern_match('wzbamnaasywtygqjdx', 'aasy'), [6])

    def test_case_178(self):
        self.assertEqual(pattern_match('qomdztkzdqbewgknwsaurmtwi', 'be'), [10])

    def test_case_179(self):
        self.assertEqual(pattern_match('tmtpebmgokfobokgpbsmbmzqmjbuuptimgaaupflfeggmzeexpvysmdhettqstgdxxwbtgxnnxlefpnidkhbqkagpfjorn', 'ttqstgdx'), [57])

    def test_case_180(self):
        self.assertEqual(pattern_match('ukglgykjlglcvgv', 'kjlg'), [6])

    def test_case_181(self):
        self.assertEqual(pattern_match('flhakqppgawapdzqslshqipxnkejyizlstvypbwegpplueukitux', 'wapdzqsl'), [10])

    def test_case_182(self):
        self.assertEqual(pattern_match('xufdrtnrzgnikzfadkhxjrgpevwcsscefdtghhzpadicertiobrxszzdouq', 'xufdrtnrz'), [0])

    def test_case_183(self):
        self.assertEqual(pattern_match('nktmamzbzmdyprfrwnvwxuhstjabvsqhzixoxrrxmqxejjsoloznw', 'qhz'), [30])

    def test_case_184(self):
        self.assertEqual(pattern_match('dvsrvdmaofszdtduijaijyialcitsrplhcuo', 'ijaijyialc'), [16])

    def test_case_185(self):
        self.assertEqual(pattern_match('rsypfvmzyjzokyjifg', 'rsypfvmzyj'), [0])

    def test_case_186(self):
        self.assertEqual(pattern_match('apzfakkpbcahxbnmgrglnadybrbrmvlanrpsepseiflmqyozlyezspdrtzfeuqguonlfnuvtrlgjzwvlnaqflgbictfcncpx', 'brbrmv'), [24])

    def test_case_187(self):
        self.assertEqual(pattern_match('tnzgtdjdljjwshbndpsxishvfiehziibqjpfmlvgpevrigozlanlx', 'wshbndps'), [11])

    def test_case_188(self):
        self.assertEqual(pattern_match('pcfxpfovcpemutezaixlqwjxalilqbbjgeolteqdhykxcnqttie', 'i'), [17, 26, 49])

    def test_case_189(self):
        self.assertEqual(pattern_match('fnnrpejynfvjdbfpblcojrzpimvpmwxlvissdyxytnyrubwqansyqrawduqfrzoayjmwssntohjczvochantxtcldrkes', 'uqfrzoayjm'), [57])

    def test_case_190(self):
        self.assertEqual(pattern_match('hlkcrhkjvyqaaknobsdhopqwgiqjwmykbufiibrluygxtywcusmxxbidyldrljcovtbytzhkxonewqcuktyglmx', 'jw'), [27])

    def test_case_191(self):
        self.assertEqual(pattern_match('uekddqfyikscjdnajdzbrqsfixnwvjtjtgsnrbkfdscnnpqkhimivijdonfzqe', 'nwvjtjtg'), [26])

    def test_case_192(self):
        self.assertEqual(pattern_match('hrkslaxgxfjdxromheqbqlxwedkvxseujucnofhjg', 'ucnofh'), [33])

    def test_case_193(self):
        self.assertEqual(pattern_match('yuuvpdagnaducr', 'dag'), [5])

    def test_case_194(self):
        self.assertEqual(pattern_match('fkzwuyyqbuyhapvnyfkczcfkmfrjpxpgggovaxzrwxykurpjlf', 'nyfk'), [15])

    def test_case_195(self):
        self.assertEqual(pattern_match('crdadsjqkawadrsbytdkkpzgxmyeeroaxhtx', 'ro'), [29])

    def test_case_196(self):
        self.assertEqual(pattern_match('vdavbwwzgvzqtbzwjffzhwmtndjtleqpndooyobsxqvtkyczcylwgqgfqyqrolsogbzgelpuuxliwymfk', 'qro'), [58])

    def test_case_197(self):
        self.assertEqual(pattern_match('hxuscxqbnzikifsymon', 'ikifsy'), [10])

    def test_case_198(self):
        self.assertEqual(pattern_match('rdbkmjivugpomclhbjmmicuftkoeheqvzjoanvffawklmaxgpnkyrsofcvhriecopiukmdjwckiaexx', 'cvh'), [56])

    def test_case_199(self):
        self.assertEqual(pattern_match('wilwffwscvqqesglnswfviljvwisqaajdcroqhunxqarlhupfhwotmoazaapbjormbxtgedmrwztqkwh', 'sg'), [13])

    def test_case_200(self):
        self.assertEqual(pattern_match('yvueymdxgcxilwq', 'yv'), [0])

    def test_case_201(self):
        self.assertEqual(pattern_match('evphszunzslvreszpiktopkx', 'iktopkx'), [17])

    def test_case_202(self):
        self.assertEqual(pattern_match('gkubjtvjkzl', 'jtvjkz'), [4])

    def test_case_203(self):
        self.assertEqual(pattern_match('jwgaafawzxgrquoqbxaoeavitmrvjpjxjxqvnfrprkletalvdwotutbcxeoengoergn', 'vitmrv'), [22])

    def test_case_204(self):
        self.assertEqual(pattern_match('yfvupamgnjwkjyyvnqxj', 'y'), [0, 13, 14])

    def test_case_205(self):
        self.assertEqual(pattern_match('waybqpmkwrnkmidiuijbdkbunwvgiesxfsfbugpgpquaxqoolxpuyegsdoreqlgbczxagwyenkeldwmtakbokylqwhtjbmm', 'ui'), [16])

    def test_case_206(self):
        self.assertEqual(pattern_match('vtxoarmmhvlxrqszbudeepljknuqqxktkydjtmrqllmznk', 'n'), [25, 44])

    def test_case_207(self):
        self.assertEqual(pattern_match('mdhpoqfkbqqhpebfegsbkixpdmzhfntgeejaroqievfvoqpjudpakwilhvahswmmksbxbjbwxcyjydwky', 'ie'), [39])

    def test_case_208(self):
        self.assertEqual(pattern_match('jeqhwlbshflavrpanforskxulsblutyvilvknokvedequfftbooyfpxqiftobwqdeqynzngzjeftscbelyzdehs', 'eqynzngzje'), [64])

    def test_case_209(self):
        self.assertEqual(pattern_match('cdhlsjsglmogsjjnmpbvijonlbmganhtzcyxvuakncghyptfyydmzbofcc', 'cghypt'), [41])

    def test_case_210(self):
        self.assertEqual(pattern_match('jpgnvnjwanguwahkhhfowtavhldypnmuuumwuyxixcqrkyevwhosgvkcdrss', 'uuum'), [31])

    def test_case_211(self):
        self.assertEqual(pattern_match('jrisrigirmqhtkipidpyxuzlvgrlweiroxtomyaxbdyoxmesbbepeawlnsltjjamegtdbehlquopxjtpzkvacli', 'igirm'), [5])

    def test_case_212(self):
        self.assertEqual(pattern_match('ndzwcnpfmktiruuunidcnpvkfnqfikwumgysmgonivmgfbneuuzrctibmqpkxxwbvh', 'zwcnpfmkti'), [2])

    def test_case_213(self):
        self.assertEqual(pattern_match('ejqttakohhmvgmnihv', 'jqttako'), [1])

    def test_case_214(self):
        self.assertEqual(pattern_match('blbwnxmvchsunuuuojhm', 'blbwnxmv'), [0])

    def test_case_215(self):
        self.assertEqual(pattern_match('huryjmadoasdzllhinldnttoakntqzyjvsgmlrakdpopjcnpd', 'ntqzyjvs'), [26])

    def test_case_216(self):
        self.assertEqual(pattern_match('ljgkhomeqnsgstvckzqqvgaoqfommbypldizdjkzyugi', 'g'), [2, 11, 21, 42])

    def test_case_217(self):
        self.assertEqual(pattern_match('iwuqqxtzgzqhoiypiyoykbdglxenijpgwrvstlolqrfywfbn', 'kbdglxe'), [20])

    def test_case_218(self):
        self.assertEqual(pattern_match('qjlnpdqyicnwhjczbyxpnmjhjkvjpodyragmtpifmpwpggwnjsodsjhpszagszezhlscfueacgzxpxgvquaiz', 'zhlscfuea'), [63])

    def test_case_219(self):
        self.assertEqual(pattern_match('uiuypfcozegbqwmkqulwvgkt', 'e'), [9])

    def test_case_220(self):
        self.assertEqual(pattern_match('lnueqbdeebkyibtkboumvcnjihfignvxkgilkcpbnwbglzumdasqmksjipzkjqkeqlcsnoutjqnfgrwzzuzsvrrntczkb', 'ueqbde'), [2])

    def test_case_221(self):
        self.assertEqual(pattern_match('reublhsrixkgbbuhzhgfqmsywqowriixbtd', 'gbbuhz'), [11])

    def test_case_222(self):
        self.assertEqual(pattern_match('pzamzcmzrfbewzaafsbhvsbqrskm', 'vsbqrsk'), [20])

    def test_case_223(self):
        self.assertEqual(pattern_match('clpjhovplgrsnqjakmidcrutaqpgcfcumqebdpravprgoxoycaffsbknmojpwlay', 'pgcfcumqe'), [26])

    def test_case_224(self):
        self.assertEqual(pattern_match('udwnntdbsrtcqgxb', 'bsrtcq'), [7])

    def test_case_225(self):
        self.assertEqual(pattern_match('ummuynnrltpljwdyxcpepdkuykfwuwtvtkmvdwpkhedyvjmppvmwdvvinbfeiksemeekdgcnducdkvqkrnxczmc', 'ykfwuwtvtk'), [24])

    def test_case_226(self):
        self.assertEqual(pattern_match('qklhhtgsqvggngzplgdbwzcijqmtxlhkvdvlbm', 'hhtgsqvggn'), [3])

    def test_case_227(self):
        self.assertEqual(pattern_match('cxpazviivizzlsvqqrirjmvjqrvytbcdohxghrgccffyhpwnre', 'cffyhpwnre'), [40])

    def test_case_228(self):
        self.assertEqual(pattern_match('mtabonviytkhs', 'mtabonviyt'), [0])

    def test_case_229(self):
        self.assertEqual(pattern_match('wgbbwsdonkkyqibcfbydhkxzzglletgbhiyvgcsjxhqnfqi', 'donkkyq'), [6])

    def test_case_230(self):
        self.assertEqual(pattern_match('vhxmoudadhbyhfgelogqmfyfxxeaoitkcbvuxckmwlbzyfriyanvtnejfmvxhtmcyuhapyjcylqwztix', 'vuxckmwlbz'), [34])

    def test_case_231(self):
        self.assertEqual(pattern_match('gxqchbfzjzypuzaxddrngstcbaobeyxbyawcwfiiqitusfrrqxlsueytsoybaqqpyydlwglysxqroxdvzntylsylqeiwuhs', 'b'), [5, 24, 27, 31, 59])

    def test_case_232(self):
        self.assertEqual(pattern_match('qwkwhnqkwxobrctwfkycctorqfstaarhmofbzhzcjqpcwhybuvtyjutxsvdoixjacgjutxldhvztrlymcdmfnwxf', 'txldhvztrl'), [68])

    def test_case_233(self):
        self.assertEqual(pattern_match('tojjkttgxrjzzemrxdinyrualrjneukvuujxirekxxirblogyalkgfhjcxhjwlfjjkcgfhmcth', 'jwlfjjk'), [59])

    def test_case_234(self):
        self.assertEqual(pattern_match('syrloepysojgxnywedyaldclfacekuxisrvlekqwotxfnqkuldmwarcpzfniomrmpbgnrudxjrspwjqesgkuiiebzjwok', 'xi'), [30])

    def test_case_235(self):
        self.assertEqual(pattern_match('qqpiprwnblovshejtwhdncshy', 'wh'), [17])

    def test_case_236(self):
        self.assertEqual(pattern_match('bgptpmldbbrwamdlirmedqoufslzhnbapfbjuq', 'oufslzh'), [22])

    def test_case_237(self):
        self.assertEqual(pattern_match('jbqrgeohrybdmxtrfkdtqtwbyypvlamlxyqzgtxlladhdwd', 'tqtwbyyp'), [19])

    def test_case_238(self):
        self.assertEqual(pattern_match('hdydygrqctoebhlygfhgwutynzdcjcwzmtxzflxxgytcfpkxzmydgupmznwqhaibazjqnmd', 'd'), [1, 3, 26, 51, 70])

    def test_case_239(self):
        self.assertEqual(pattern_match('crsyvtqutq', 'crsyv'), [0])

    def test_case_240(self):
        self.assertEqual(pattern_match('benmcajtzikankdttokihyziobwbgh', 'ziobw'), [22])

    def test_case_241(self):
        self.assertEqual(pattern_match('tecjjwwacwwmuqgrfmqgtihqnn', 'ihqn'), [21])

    def test_case_242(self):
        self.assertEqual(pattern_match('ewndbipyfhwkctvmwdnlznaurwrqxrclbsnfayjbqidkagowoucouumkgwknk', 'ayjbqidka'), [36])

    def test_case_243(self):
        self.assertEqual(pattern_match('nwcoqzqjsoszllyvbwkerhalhiwhwozewbjahnyzvlicnostduvdhgwfsczrwdwjwltxfmlyjmi', 'coqzqj'), [2])

    def test_case_244(self):
        self.assertEqual(pattern_match('iuwqybthxhiistovxtlcqgbqjbthpkfbnrlkdlbgtqsjjtyfzobulmijj', 'bnrlkdl'), [31])

    def test_case_245(self):
        self.assertEqual(pattern_match('hydhnziogedrdanwcrgatri', 'ydhnzi'), [1])

    def test_case_246(self):
        self.assertEqual(pattern_match('nrbbxxwpwdfixjglevohoujpiiapahwynnsohyxmlzxjfeotlbfcdhjupuqdayngwmioiwghhpghxyqjcqoedyqqohzujxw', 'dhjupuqday'), [52])

    def test_case_247(self):
        self.assertEqual(pattern_match('yukyesgwuibelwusfsozjpdyjjlcftoultjmbvbfthxyznhgmcxypdvhixwgvhykpqjdntmynzdudubpxryhqltyezm', 'yn'), [71])

    def test_case_248(self):
        self.assertEqual(pattern_match('vjjclbtpfcaycfprlvuhytygdak', 't'), [6, 21])

    def test_case_249(self):
        self.assertEqual(pattern_match('aflhoofhruyputhzqntrmyvzgl', 'flhoo'), [1])

    def test_case_250(self):
        self.assertEqual(pattern_match('aqdofaenoeqnlgtuexrtwnnjmzmzjjgagwaxoisixfr', 'nlgtuex'), [11])

    def test_case_251(self):
        self.assertEqual(pattern_match('slqyzxnisamqbslpocprjxekpfmcqotfafhbnukoripoobiljippsxlktczdplpvxjnxcoarwjazinxeoswcgssm', 'vxjnxcoa'), [63])

    def test_case_252(self):
        self.assertEqual(pattern_match('azvdourocksgswosiiomzjnsczgqwtsfonirxisxipqpxzpvlsocuyzwxridzmhus', 'lso'), [48])

    def test_case_253(self):
        self.assertEqual(pattern_match('jikixzvkpylzaicomlkhuvlwpdytttynoqyhfvzimih', 'ynoqyhfvz'), [30])

    def test_case_254(self):
        self.assertEqual(pattern_match('hwnpuxidyblfdoqwzibcdntaeuseyqomtlrjnblafogsbuyelrysgvrdtzuxlyokulseghgsoybphmzpceq', 'qom'), [29])

    def test_case_255(self):
        self.assertEqual(pattern_match('pmllhmgaeuwajpgujzeinzuegmojry', 'p'), [0, 13])

    def test_case_256(self):
        self.assertEqual(pattern_match('tnwgyfwihglyykcysvznjc', 'y'), [4, 11, 12, 15])

    def test_case_257(self):
        self.assertEqual(pattern_match('ztbhatiiclyhj', 'tiicl'), [5])

    def test_case_258(self):
        self.assertEqual(pattern_match('dlxzjqhfnchytiytbptgjxehaonpidepctppyllgfburhgzwjdasmxcowzatpctfmfldsjgyuurwcojbsojrmzfdkvzxokr', 'depct'), [29])

    def test_case_259(self):
        self.assertEqual(pattern_match('aafxeadkqrcnywwupmjuzcdbbjnbmsosgkmrafqcyhnuspsuaasrmcberuvdziegi', 'bmsosgkmr'), [27])

    def test_case_260(self):
        self.assertEqual(pattern_match('attskzkunxcchgdhyedjtexvuwehnjibkxmxcedddjrsfdfhebf', 'd'), [14, 18, 38, 39, 40, 45])

    def test_case_261(self):
        self.assertEqual(pattern_match('zlexigdzapkhltdwasokmttadnysyhowllkkxkazdkxryvhtvynyhjejxsafdlazozpg', 'jejxsafdl'), [53])

    def test_case_262(self):
        self.assertEqual(pattern_match('qdfxpuurpvsaywqdjntgjqgzjyxrsmkzmuqawmpnebusrpyvzlsvlxcwype', 'saywqdjnt'), [10])

    def test_case_263(self):
        self.assertEqual(pattern_match('sgrtphmxbmjfudwozmckmyflxgdhvreiagba', 'flxgdhv'), [22])

    def test_case_264(self):
        self.assertEqual(pattern_match('rkmuhbfsozi', 'i'), [10])

    def test_case_265(self):
        self.assertEqual(pattern_match('saebzzwnvdoippuurcmfqxkpbwakzyruviefxpxchbbkcmubjaqj', 'wnvdoippuu'), [6])

    def test_case_266(self):
        self.assertEqual(pattern_match('smdlmmpbzvjxwoqcburrwemttzyilyhsfjxekvvzmfgtjeyteexywvohnwiwlyxpmxmybxebif', 'tzyilyhsf'), [24])

    def test_case_267(self):
        self.assertEqual(pattern_match('kvkgxawwnvyisomiwrcszcwayycqtmompyamygqoqobmuoqcvkguwqiuznnhdioalevrap', 'mpyamygqo'), [31])

    def test_case_268(self):
        self.assertEqual(pattern_match('cwxnguzerehyavosztoltsmlbsepwksufcnsbvtnriuvfkuqecbedmrxruntbhnolfncvs', 'nsbv'), [34])

    def test_case_269(self):
        self.assertEqual(pattern_match('fqnxqcudywevetfnbkrrtexkn', 'krrt'), [17])

    def test_case_270(self):
        self.assertEqual(pattern_match('xtdtovkrszhcpbgckiyeyyuhrrn', 'xtd'), [0])

    def test_case_271(self):
        self.assertEqual(pattern_match('pgpecnkuaavdgramxcjlavgqvpxkpijavfcixqfqeyaqonm', 'cixqfqe'), [34])

    def test_case_272(self):
        self.assertEqual(pattern_match('zcmpabicjqsstlstykazh', 'ls'), [13])

    def test_case_273(self):
        self.assertEqual(pattern_match('basamdhtxdlprpxqajdqfiwfvejysuvskvxtqaseldkbuycaqsbhhpymvnxievrbhoavdq', 'wfvej'), [22])

    def test_case_274(self):
        self.assertEqual(pattern_match('fnmgizctwwclvizp', 'ctww'), [6])

    def test_case_275(self):
        self.assertEqual(pattern_match('qtvujhbxgqnylfhkafmqrccdxyskjdspccdthmtcwyuqdyksdnorpeikakdhsbrwlledvwyuwanygjkycqqjyuaxykrstwxfeyy', 'cdth'), [33])

    def test_case_276(self):
        self.assertEqual(pattern_match('azuvvmopocgovcwtmuomfqnczsgbivbyyvtmigrgjuwklvvqmcftokbspelusaomkdedcrtdeqmdnxhaq', 'elu'), [57])

    def test_case_277(self):
        self.assertEqual(pattern_match('zepxzwjktaqjlseqynarhattruumnkiekjkzgcajfvylhphpfxjfmfljmdevbrwoxuh', 'zgcajfvy'), [35])

    def test_case_278(self):
        self.assertEqual(pattern_match('vtkrpetkgllsyivcscbuaklprorqvhz', 'syivcscb'), [11])

    def test_case_279(self):
        self.assertEqual(pattern_match('ljbienluwtgolknrpapjggfzxdmsaujmxuerrydqtgx', 'jbien'), [1])

    def test_case_280(self):
        self.assertEqual(pattern_match('rminpcfgyipeodlfchzjacavxmbinqvqwisjyjqsincq', 'fg'), [6])

    def test_case_281(self):
        self.assertEqual(pattern_match('thoszmkdebbkfgqcrtaoalxarqgrdocxccafnnbxsjajmbhxnncmxoknhibtgzmfkzvdnvmzadrzpqdrioquvfjaffnedcerzq', 'kde'), [6])

    def test_case_282(self):
        self.assertEqual(pattern_match('mvmiwlsozpqbytygctyul', 'zpqbyty'), [8])

    def test_case_283(self):
        self.assertEqual(pattern_match('ccamjzhkfupnlwwyjojnfhoidzjkaosoickfbvlmqqk', 'mjzhkfupnl'), [3])

    def test_case_284(self):
        self.assertEqual(pattern_match('pptuobvzlputttypxhptrmvejbddvqqnpuksqsxupqckzrtkjzro', 'pxh'), [15])

    def test_case_285(self):
        self.assertEqual(pattern_match('zfpkrgcydttulgajjdlojqvbtkhlrvdrnfdkcnkposmumlxokaiqllalkdcujsnaoemdszzvbwidbwybtyqgklc', 'bwybty'), [76])

    def test_case_286(self):
        self.assertEqual(pattern_match('kizpvbtnielvhdutbqfwyksusxxcsrfdbbfnajomzvclxghomvbrusvrfpqfyyryxybjqdzngwx', 'yr'), [61])

    def test_case_287(self):
        self.assertEqual(pattern_match('dejterihysrfcfmtpballflswnkogeqi', 'fls'), [21])

    def test_case_288(self):
        self.assertEqual(pattern_match('bvlcggkvazpdgfnribxkqropuvageatpluzpfwbmqcjldcvdiwcqhmwnbvypyfkbvcygxhyxumngilgkwsbjitoba', 'fkbvc'), [61])

    def test_case_289(self):
        self.assertEqual(pattern_match('wlpxgyvttgqffzhfuzphilckkeoohuiqqgvqawkmbckyvzhrdsnoz', 'z'), [13, 17, 45, 52])

    def test_case_290(self):
        self.assertEqual(pattern_match('rvyvvnvoesyvscofsshrosxcegiaatwyztxqzfoqyl', 'r'), [0, 19])

    def test_case_291(self):
        self.assertEqual(pattern_match('zflozyjjxfmpnfjnlkfpws', 'jnlkfp'), [14])

    def test_case_292(self):
        self.assertEqual(pattern_match('scuxmlqjyshcfpiskrtffieiywrxbjcmlkpfkxqmxbzdjkgfds', 'hcfp'), [10])

    def test_case_293(self):
        self.assertEqual(pattern_match('bkqwhhnpoxr', 'kqwhhnpoxr'), [1])

    def test_case_294(self):
        self.assertEqual(pattern_match('znbtnoqqevznitupixkazablavfoeotzfzhnrdkofefrmwqjckq', 'rdkofefrmw'), [36])

    def test_case_295(self):
        self.assertEqual(pattern_match('tghgfekviqvnsyjiyrjyxjewmhcxdueycjenorctpukhooxv', 'viqvnsyji'), [7])

    def test_case_296(self):
        self.assertEqual(pattern_match('ooygwqunnksiwdnxmjjvphoftjnzvskffeifxptmkwutstwxjhqnywpxdoekdtcyatwdsdsvyawwzvwtaf', 'nywpx'), [51])

    def test_case_297(self):
        self.assertEqual(pattern_match('ebdewuzpmmjyxdedpzkejhbntftppqiwdpjdpqljrotectsyxiyxblavjltwahvlrcynqswjwxluvxcnu', 'avj'), [54])

    def test_case_298(self):
        self.assertEqual(pattern_match('mmohjeghlbazkttkdmc', 'mmohjeghl'), [0])

    def test_case_299(self):
        self.assertEqual(pattern_match('tjocbxrkrqinkyqhmgisfhbamytmelxqewupfkseudjimecnzlqqymjhqsieyrgornugnglqqtgvkthiszbfzovisnsm', 'inkyqh'), [10])

    def test_case_300(self):
        self.assertEqual(pattern_match('emaffgftpuwdhrmoyytvpzsakbufixyvtazaiuiokjikrozbdipw', 'zaiuio'), [34])

    def test_case_301(self):
        self.assertEqual(pattern_match('uglgcspgjcfkabcriiskwruvgfjxnxfqgruqqllieilqpotwfjporkbxxmbsjcezadfaz', 'qgruqql'), [31])

    def test_case_302(self):
        self.assertEqual(pattern_match('qujihsqcbkvubaixntusnmgjxiinknmnxrmrmcefjzqdscssytglpehdipnroouy', 'nmgjxiin'), [20])

    def test_case_303(self):
        self.assertEqual(pattern_match('pvndbyukbbupshcmepsf', 'bbupsh'), [8])

    def test_case_304(self):
        self.assertEqual(pattern_match('isbgotomyoenqybogucxtdqyjzmhjksyjvvaujwdhohssfoplbmyoahmiwjmtskfsuufzzgbi', 'yjvvaujwd'), [31])

    def test_case_305(self):
        self.assertEqual(pattern_match('oriukwdmancmtikcrvxevahklhgvmyluarn', 'wdm'), [5])

    def test_case_306(self):
        self.assertEqual(pattern_match('isrdvtjqlnrwhopwccjqvdpgnoiinqxwkypgphqpkfxtuqnwwwbuwugofspzgospbcdegwzewrxyaimvzwfworu', 'qln'), [7])

    def test_case_307(self):
        self.assertEqual(pattern_match('rcfurrgctobgozeglitzna', 'litzna'), [16])

    def test_case_308(self):
        self.assertEqual(pattern_match('enqscdxtguarvazqmvflwsgovisttsirxhtrvlqzvhmwgolyai', 'gol'), [44])

    def test_case_309(self):
        self.assertEqual(pattern_match('bxrircebjh', 'ri'), [2])

    def test_case_310(self):
        self.assertEqual(pattern_match('dntllwjsudmgsgaeemyeqnikithklwyzoxylkopavpzo', 'ga'), [13])

    def test_case_311(self):
        self.assertEqual(pattern_match('mhpatabtmwdigjsbhykrmxrcndawikezfpgqwlqvbcgdvcmndnkmsfaljtdcndzyzyufboaedxyyjyppi', 'dcndzyzy'), [58])

    def test_case_312(self):
        self.assertEqual(pattern_match('ptlvbngokgswyjflvlezknokaynxghypdgbjousapexhmhthtehay', 'kaynxghy'), [23])

    def test_case_313(self):
        self.assertEqual(pattern_match('glakldgtlgwtfioigxdbpgqppewzioks', 'ioig'), [13])

    def test_case_314(self):
        self.assertEqual(pattern_match('hrukqmubwnuksxkffmtxgiugcc', 'mtxgiugcc'), [17])

    def test_case_315(self):
        self.assertEqual(pattern_match('ngotdahhfquvaapytqiboqxrvvoxutavwtkfsaxmeselnqhygsghwiggjbliyecufzcyoerziztwpbmpcvwcdnkcvefgfbups', 'kcvefgfbup'), [86])

    def test_case_316(self):
        self.assertEqual(pattern_match('zxfyzcnkuxoompakexdpglgyinsvsxenfvyydmymymrmfsiryeqkwsymrpmbslfnytdbtkrj', 'ompakex'), [11])

    def test_case_317(self):
        self.assertEqual(pattern_match('bbdfacociqmmlouzofulxf', 'ciqmmlouzo'), [7])

    def test_case_318(self):
        self.assertEqual(pattern_match('dlyfpilkewdmq', 'yfpilkewdm'), [2])

    def test_case_319(self):
        self.assertEqual(pattern_match('bztbfhyzgafgkl', 'fhyzg'), [4])

    def test_case_320(self):
        self.assertEqual(pattern_match('ceyylcghjmhsheytkmlesxvgzuhiqddosnpc', 'snp'), [32])

    def test_case_321(self):
        self.assertEqual(pattern_match('arqptbbcgbrigpz', 'cgbrig'), [7])

    def test_case_322(self):
        self.assertEqual(pattern_match('uwmqxwvfqxosdtaeaiwsvybpniggwzodhmekiunnuqakorlpjrjjwoaqbfpzsqirzpfgrrqgufdghoekrj', 'hoekr'), [76])

    def test_case_323(self):
        self.assertEqual(pattern_match('creddmucedqxcinxgcklhqqfrbcagevszvjwxdycmr', 'vszvjw'), [30])

    def test_case_324(self):
        self.assertEqual(pattern_match('dzyerdwgkrujujtqoqhahncyaprnqoiromvozcavyggymvbiuqgryvjbydfhvgifj', 'ahn'), [19])

    def test_case_325(self):
        self.assertEqual(pattern_match('qjszxiybenvxrrqgyedofokpoxsftrygelatglyhma', 'd'), [18])

    def test_case_326(self):
        self.assertEqual(pattern_match('pywmccsxyplbjrnfqrtjnbozndjubulokbsivcrjwtgavyxi', 'vcrjw'), [36])

    def test_case_327(self):
        self.assertEqual(pattern_match('juhgguwwtgmyndlojzlqfuihmuyfrtocxjnkkvxkikhgogakwfjstgraogsmynmrumfxmh', 'nmrumf'), [61])

    def test_case_328(self):
        self.assertEqual(pattern_match('cymuyconrnaapdkikjaknelbsjvxjukeeayptfegthdhjwxcrzfdzxctcjcqmrnozvmpyttkilubnakjyhi', 'fe'), [37])

    def test_case_329(self):
        self.assertEqual(pattern_match('uzogrzkexxpfixgmhtmznmyusizcytjedobopmslissjiyfo', 'jedobopms'), [30])

    def test_case_330(self):
        self.assertEqual(pattern_match('vmlgckybhfjkqtimmszlwusbidrfmqzlnstwes', 'wes'), [35])

    def test_case_331(self):
        self.assertEqual(pattern_match('wksnksdoddxuwminaguyloqeiiidbpcqxcnjvgvusayxbpuobcsxwbeddmttagvgqjbutswjewl', 'xwbeddmtt'), [51])

    def test_case_332(self):
        self.assertEqual(pattern_match('heeondgmdsewhmzqqvqzbhnqoxtoeixxawdgjocijdhqdlkrceuzrnojiythioaqqvcfazodjjekkeifvfxcfdru', 'qox'), [23])

    def test_case_333(self):
        self.assertEqual(pattern_match('joefbajlpdvzuxqnniefybablptvcpqqoyjiassmfzwfxalwcqcuapaqbatcmauuirqvlzlzhgtticaxyifhrgqz', 'fzwfxalwcq'), [40])

    def test_case_334(self):
        self.assertEqual(pattern_match('ksynwafieekozxuodrem', 'afiee'), [5])

    def test_case_335(self):
        self.assertEqual(pattern_match('kpesetngqkdoqpnsfjzmtudqpdvspfbbsydhrcutplzhxlfjgn', 'setngqk'), [3])

    def test_case_336(self):
        self.assertEqual(pattern_match('ozfmjehecwb', 'zfmjehec'), [1])

    def test_case_337(self):
        self.assertEqual(pattern_match('ryjbalmxdymbnyfammruxrnhtfgoqhnocfluybzwsldduhttusvmuehetnkyihtixlubmgdgojbg', 'fluybzwsl'), [33])

    def test_case_338(self):
        self.assertEqual(pattern_match('exgiveozifyvqcjblcnrrmiawaemwhrjjxrjgacdhexb', 'c'), [13, 17, 38])

    def test_case_339(self):
        self.assertEqual(pattern_match('tlruebvaftokofdjk', 'oko'), [10])

    def test_case_340(self):
        self.assertEqual(pattern_match('jixdugicplcyurnosxyvxobogv', 'cplcyurn'), [7])

    def test_case_341(self):
        self.assertEqual(pattern_match('xjckzxmmqonchwrjmdlyto', 'jckzxm'), [1])

    def test_case_342(self):
        self.assertEqual(pattern_match('thiltfnzgifmwqsimjavnrwanjtrteclnzxpkgacttgblhbin', 'ttgbl'), [40])

    def test_case_343(self):
        self.assertEqual(pattern_match('pqfejclzanzlizvmoqfwzdfpupaglccztptwxbsbcqwzpetbdtkqorppsqqajzqxnjcnanpbvpyrbijzuqyvnqpvq', 'wz'), [19, 42])

    def test_case_344(self):
        self.assertEqual(pattern_match('lzetwjnwnndyszhbinpaikzhzfvflwgvvcyszfpwxheurxufcsknnpdxvy', 'zhbin'), [13])

    def test_case_345(self):
        self.assertEqual(pattern_match('nfqkmizurmduzhltvbprfdzffxjtwiizlxyobauqglabxclyptgdsollwgxuh', 'nfqkm'), [0])

    def test_case_346(self):
        self.assertEqual(pattern_match('zkqwbjxscyezmgeiqpjijexuoepbqotpjqussb', 'o'), [24, 29])

    def test_case_347(self):
        self.assertEqual(pattern_match('mbrsqiurrjttgyiyoximmmvzdyfpgufnafopiolhtgmkmozrrehjhlvmlgidzbcnjhlqfmvxvrshcvu', 'sqiurr'), [3])

    def test_case_348(self):
        self.assertEqual(pattern_match('tjprtwoaajsnovnwzwgervuvfffqugrvzvzippeypymmomzkpirjlqnrixttzrwxelzgl', 'vnwzwgervu'), [13])

    def test_case_349(self):
        self.assertEqual(pattern_match('tgbfnasjjtnqgvwiwpgevhetbegwp', 'bfnasjjtnq'), [2])

    def test_case_350(self):
        self.assertEqual(pattern_match('spdmpuscyrqdaezcwrgyopxtajvfoajvsefhlcdwoayxmxyiiqnnitrrltbvqwnfailizstrutlijwsewah', 'uscy'), [5])

    def test_case_351(self):
        self.assertEqual(pattern_match('twcbmqhzeyhxvvdgsodesnucyazxnihpagoidwozhsmyyo', 's'), [16, 20, 41])

    def test_case_352(self):
        self.assertEqual(pattern_match('erqemuhgbwnepugouuoxwlpgegpllozfwvfdcawzfblakrjoypnnvuewlrc', 'ewlr'), [54])

    def test_case_353(self):
        self.assertEqual(pattern_match('hxrdzytvuphjbhrmzixyuxhjfqckyhlsbxyukbily', 'zixyuxhj'), [16])

    def test_case_354(self):
        self.assertEqual(pattern_match('ndejubmpfrzjwstiozfhttw', 'wst'), [12])

    def test_case_355(self):
        self.assertEqual(pattern_match('rzndspzugwvcifapdxgfwwcirskuiojignfuncyctanwcqlgmvhbjoswhrwthrydhqrqilddiiwtypyaclyyp', 'ignfuncyc'), [31])

    def test_case_356(self):
        self.assertEqual(pattern_match('lcszzvhtrvuvysbutquyjpuhluiierz', 'butquyjpuh'), [14])

    def test_case_357(self):
        self.assertEqual(pattern_match('wdoiumpfxrqwwwwbvw', 'um'), [4])

    def test_case_358(self):
        self.assertEqual(pattern_match('yykarunzsuxvlihtrpwjnpo', 'runzsux'), [4])

    def test_case_359(self):
        self.assertEqual(pattern_match('jmuacclznciohmmvqibepxtdgubkjvyeuwvgowcgulmyamszfyxvdlumqsy', 'mszfyxv'), [45])

    def test_case_360(self):
        self.assertEqual(pattern_match('rjesnwseewxsaxrmcunqjluvfcyoglfssdsvjdybhxkbadloeewuynkgoqyizstzonigvcxucqgnmlylgbwrecmthuvhf', 'cun'), [16])

    def test_case_361(self):
        self.assertEqual(pattern_match('cncnclqojmjsmixtvogoceecazmjtifdwobxdqttvydvmhkhdstxbfyxlxraliplcecmcpxlwebobsdcthxtkedfeyutyf', 'clqojmjsm'), [4])

    def test_case_362(self):
        self.assertEqual(pattern_match('dwiosvezwqctih', 'iosvezwqc'), [2])

    def test_case_363(self):
        self.assertEqual(pattern_match('rrmeewchklhgjrwfg', 'rrme'), [0])

    def test_case_364(self):
        self.assertEqual(pattern_match('vphhfmeunijmgaogzzurblteedekhzwxrxqgtbwkagytuvohnbkfsgqesgrriqxgrqekhehvxbkrcbduzthgxslqx', 'kag'), [39])

    def test_case_365(self):
        self.assertEqual(pattern_match('oueziphlndxvrxrbicvzgayffvqbdehrnlfinsrjdbmpvazfgyukzxtz', 'eziphlnd'), [2])

    def test_case_366(self):
        self.assertEqual(pattern_match('wmdegdgkupqwlehs', 'wmdegdgku'), [0])

    def test_case_367(self):
        self.assertEqual(pattern_match('zatdvcrgiufzdnjmxamqee', 'njmxam'), [13])

    def test_case_368(self):
        self.assertEqual(pattern_match('hfwepgacnlfilrxnifccsnuaakilxcordaayiuedxylznpccabsaeszbpaqsvxvrszqownbgtccrpgwdtn', 'nbgtccrp'), [69])

    def test_case_369(self):
        self.assertEqual(pattern_match('jehdsopprhgbpyejdukwbz', 'z'), [21])

    def test_case_370(self):
        self.assertEqual(pattern_match('opjagxxgwkkmzzxzpvneuagwwbnzludeiqhlznmykxwsqrainlxqmnmwffxwbrivrifmokbliwqdfzluafvhxjbdtse', 'w'), [8, 23, 24, 42, 55, 59, 73])

    def test_case_371(self):
        self.assertEqual(pattern_match('luqteooetuzazwetqkrnazihqtdvblzmlmknkakfp', 'kf'), [38])

    def test_case_372(self):
        self.assertEqual(pattern_match('yrzrjhegmgflrtpnlurllrqdbliemvrixjywfbydrg', 'byd'), [37])

    def test_case_373(self):
        self.assertEqual(pattern_match('erfnbaktdilvinjekapcjqncfmkjsxsrvnkahiviwfuqzrodtoycn', 'fuq'), [41])

    def test_case_374(self):
        self.assertEqual(pattern_match('ggvtamsqcmrwhvypecvndhehowjrzyuqwyvmfqteerfzlvtgppcphabat', 'ppcphab'), [48])

    def test_case_375(self):
        self.assertEqual(pattern_match('uysuipynvkpxxlozweudfmegdxstkmkjvthzkxystucmoxlkfxtctpwdeq', 'x'), [11, 12, 25, 37, 45, 49])

    def test_case_376(self):
        self.assertEqual(pattern_match('mzpshnagrfgghqghpgeurlroupyytycfni', 'fgghqghpge'), [9])

    def test_case_377(self):
        self.assertEqual(pattern_match('whvosxffyxpjkknddbjlmgvlmldasfyuanjurgtjwlrxxtbvwnluvshqhonvncklgxixmrkk', 'wnluvs'), [48])

    def test_case_378(self):
        self.assertEqual(pattern_match('vteokmanmfwhpccgwssjfkjnnflazunbnonsjkwxolkrsaxveogi', 'anmfwhpc'), [6])

    def test_case_379(self):
        self.assertEqual(pattern_match('vmciqqgisueglozwoikadijknxiqnqzdpzmwbbqkfxupxlkvkobjehdsywjeqmuhntyxtacbuwvymkwgom', 'vymkw'), [74])

    def test_case_380(self):
        self.assertEqual(pattern_match('pzflgauspjauhqtqfnizjyn', 'tqfni'), [14])

    def test_case_381(self):
        self.assertEqual(pattern_match('pcyycjsisbfnzxzhlxvastyytbbujbvljvlvlcacujbvkefrw', 'z'), [12, 14])

    def test_case_382(self):
        self.assertEqual(pattern_match('rgouvucneljvgjndchfikxjvmcynfakesfvijzwmdyrxoevhcuctatpmfzesxjcxnykwzhnvtgpvmrz', 'fv'), [33])

    def test_case_383(self):
        self.assertEqual(pattern_match('jecwviwdcevqulabochlaiqftcdxsaqcopxfbpzevekkjfagijuyiovar', 'viwdcevq'), [4])

    def test_case_384(self):
        self.assertEqual(pattern_match('vhxepewgvxurllexjsyzolony', 'xepewg'), [2])

    def test_case_385(self):
        self.assertEqual(pattern_match('vcqtxggfexaywotfhsjqialhapwucnjeepvtfqubaz', 'ep'), [32])

    def test_case_386(self):
        self.assertEqual(pattern_match('yqcfcfsyotemkgnbvljczqdbhwuglnstgqezddhxflzlxysbhgltvyomlsdelmjlacipinpqlbvsvcdcwtjujqhmjrdnbzbg', 'zqdb'), [20])

    def test_case_387(self):
        self.assertEqual(pattern_match('plvsvaveukkiyomqpbbmvvetbtzwxjijixsurwjyrwjlkwocipktleqaymnuhtieaj', 'yo'), [12])

    def test_case_388(self):
        self.assertEqual(pattern_match('wqwjstoozydktwftjezzfmiifjdlcyngfwocorxrtoksentwybidstjdotjneaxqagwvvwoscnsfqcfb', 'dlc'), [26])

    def test_case_389(self):
        self.assertEqual(pattern_match('wtqbsyegqnht', 'tqbsyegqnh'), [1])

    def test_case_390(self):
        self.assertEqual(pattern_match('frrwfutatzpnazkygnxwnrlwdsjalmylqhbueuberlhojotjrngotffdbhbglwqvwcxdyczcnefghzvfymqcbizxfphyp', 'zxfphy'), [86])

    def test_case_391(self):
        self.assertEqual(pattern_match('varwhphiwdgkjzletkbozvdcxkezsorgrjygowsicphetqddcgmzb', 'jygowsic'), [33])

    def test_case_392(self):
        self.assertEqual(pattern_match('bfemrwkzmvnwmakuyqyovqgujtsprrrwvxs', 'kzmvnwmak'), [6])

    def test_case_393(self):
        self.assertEqual(pattern_match('onwzctzkzcpkaactwlayvznhasbcsd', 'ctzkzcp'), [4])

    def test_case_394(self):
        self.assertEqual(pattern_match('vfvjyullyfqanrnbxdoujzflbpbdbxhgmyssvvmpfqbldnabzvmsufmvrpsxuyktixrvoguhuybfwuehcltsedylrrlzn', 'ullyfqanr'), [5])

    def test_case_395(self):
        self.assertEqual(pattern_match('tgyweindrobwfqbvkuiuqhpeopptjtppiuxnwigigrwshewihgctga', 'wshewihgct'), [42])

    def test_case_396(self):
        self.assertEqual(pattern_match('tgmwfgfcwphdglsxycbtommiwdcqeblvgubotqxpkdge', 'lsxycbtomm'), [13])

    def test_case_397(self):
        self.assertEqual(pattern_match('vxfuoszrvziiwiwmisigaageggnlsaeautkcrgkwmqdisrpuxejwnixantrpppcbkvkphjkblmlztryyxqofaz', 'vxfuoszr'), [0])

    def test_case_398(self):
        self.assertEqual(pattern_match('aamdiroqygpqrurxyxqtmwsuaeqfncudityutyftrukcwklymsueldntcv', 'it'), [32])

    def test_case_399(self):
        self.assertEqual(pattern_match('unqifdepslsdklghbgwdbzwsjbhlyebxugfktuxjxfpprzlnwoshroqpzpybjsvmtvbpgl', 'gwdbzw'), [17])

    def test_case_400(self):
        self.assertEqual(pattern_match('wgpjhaiolydicfbommmrjopb', 'pjhaiolyd'), [2])

    def test_case_401(self):
        self.assertEqual(pattern_match('ssxalnoyyiiovpjizgpxmxzr', 'oyyiio'), [6])

    def test_case_402(self):
        self.assertEqual(pattern_match('uhntguzkykahllenozhtkzftexdfbtjhgzruaplcoauevenkpizgseaiogvv', 'ftexdfbtjh'), [22])

    def test_case_403(self):
        self.assertEqual(pattern_match('gnlurycnbofoawttzgcibkudvyndnhghmoxkjwuulbvypibriewtmucyekqmuburtimxxzrsvvznmdokgzhrvptixwcwxkfhigzp', 'ghmoxkj'), [30])

    def test_case_404(self):
        self.assertEqual(pattern_match('ifamnzbiyj', 'z'), [5])

    def test_case_405(self):
        self.assertEqual(pattern_match('uameudnfqjaodctlwppaycgln', 'lwppayc'), [15])

    def test_case_406(self):
        self.assertEqual(pattern_match('tuelzyyxtardrmahegzukbkeztamanddxovwavfaewwiatqaeydtackavaacivnearumqdaktwzuwtejafgtxnzrkblmlbypkbg', 'ta'), [8, 25, 51])

    def test_case_407(self):
        self.assertEqual(pattern_match('kbxjhwczpinxnc', 'czpin'), [6])

    def test_case_408(self):
        self.assertEqual(pattern_match('betcvncvkchsjfjzicgromsjbxemwgzw', 'zicgroms'), [15])

    def test_case_409(self):
        self.assertEqual(pattern_match('tktwnioifmpeetbxrwewmngfyoldqxegbhhsdjnmovzksahopsjughahvxgeftppro', 'vzksa'), [41])

    def test_case_410(self):
        self.assertEqual(pattern_match('uizfbnwbvbryxflbtobmhavj', 'fb'), [3])

    def test_case_411(self):
        self.assertEqual(pattern_match('iudnjaqclriaynlryqgcsxxnysgndraevrlt', 'udnjaq'), [1])

    def test_case_412(self):
        self.assertEqual(pattern_match('pkyojfqomkazhqwxqjjiqaifnatjngrpfaoiozqdncpoznjtiahjcgetbcwniulheuyiauclugmjavsywgihjovfcbrsciae', 'hq'), [12])

    def test_case_413(self):
        self.assertEqual(pattern_match('xqbmrcpwvbrtvelzdmakbzcbwrcgxjbkfavtdzrydsqs', 'tdz'), [35])

    def test_case_414(self):
        self.assertEqual(pattern_match('qgcwlchghscrtsknbmlqvhjlluvrkadpg', 'ka'), [28])

    def test_case_415(self):
        self.assertEqual(pattern_match('cnrbhsbkbqoxqrjelqnyrytfsohjvqlaziixrjgolrdunsycnwyqimjcozbteyhjwsdlpuozjfbjglwhajypxztqktvlutkzot', 'bqox'), [8])

    def test_case_416(self):
        self.assertEqual(pattern_match('sojeerqyiygxuabechqotrothfsjv', 'bechq'), [14])

    def test_case_417(self):
        self.assertEqual(pattern_match('owvpevrqvtgxrexokmajuxkxumsytuohxeqduerxbcutdzojkpusauriljkredejhfpklvdhuhqm', 'e'), [4, 13, 33, 37, 60, 62])

    def test_case_418(self):
        self.assertEqual(pattern_match('ujwgwrgejgxeyukinvxjdqvjdzbskietwocrqetlgwchautvtpaivegymqnjgdsmylxwaujwafqbszzukhjj', 'k'), [14, 28, 80])

    def test_case_419(self):
        self.assertEqual(pattern_match('fuijmufnbjguducknrtwoqnwnkrx', 'nbjguduck'), [7])

    def test_case_420(self):
        self.assertEqual(pattern_match('mmyzivtgfghmgzksjltrz', 'tgfg'), [6])

    def test_case_421(self):
        self.assertEqual(pattern_match('dklrtscjentqrrjvvrnoqmbhocvlmddechegpwszhpenxckpcaim', 'rno'), [17])

    def test_case_422(self):
        self.assertEqual(pattern_match('xyrgdwhniwverofpbzrwhsfgnawcwcgcekotunjsc', 'gc'), [30])

    def test_case_423(self):
        self.assertEqual(pattern_match('innsoknvwxxnv', 'xnv'), [10])

    def test_case_424(self):
        self.assertEqual(pattern_match('xwfgrbyrqdqfkelktbkiatzayyoshbjbhnuaejoqpgzijihldytxlsqhctiszthbeafirpnhglypvorypmlqc', 'yrqdqfkel'), [6])

    def test_case_425(self):
        self.assertEqual(pattern_match('dzrazrasyudasbhetemczrqqxrfvuqeainamnvffkvrwjjozkwywiphmmutyneczayforqremhy', 'zrasyudasb'), [4])

    def test_case_426(self):
        self.assertEqual(pattern_match('jdxmxygygfjhbzyxewpshtymbodowfwbhzqtoasjqgwapweacqoczreemptqdflsgjxwtznbxtesbtwzahqqgamdrkoqfocu', 'esb'), [74])

    def test_case_427(self):
        self.assertEqual(pattern_match('zxmqwvtwgzjabcgodtomxystvimoxfbscjdkpijwdig', 'dkpijw'), [34])

    def test_case_428(self):
        self.assertEqual(pattern_match('lmvmxzurkzhzohhfdqesyyoakuqumoeejadrnogiffslccjkgpstoibhvpbycxnhzyapttpixrwtfiafajpvwicqqgirkzny', 'hv'), [55])

    def test_case_429(self):
        self.assertEqual(pattern_match('fcnnqtobrmsowvqjriyijuklcjvrqnkmubb', 'cjv'), [24])

    def test_case_430(self):
        self.assertEqual(pattern_match('fatubnoithkayxqnleyowpsxehzdflakycyaoqskwmhvfijyxzgccg', 'vfijy'), [43])

    def test_case_431(self):
        self.assertEqual(pattern_match('jwcvofzwgpqricxzesevhjvavakzamxnnzlpwurgnvhemvuzxtvarrpvxktvzmqydxbl', 'vofzwgpq'), [3])

    def test_case_432(self):
        self.assertEqual(pattern_match('fcdroqneqzlpzvmesdacuszqawhdlhsgjdzpmkg', 'sdacu'), [16])

    def test_case_433(self):
        self.assertEqual(pattern_match('ktaznnezlqadqtdmkfdysknz', 'kt'), [0])

    def test_case_434(self):
        self.assertEqual(pattern_match('ajnaqzqbrkemymuzqofmgjofwaxuwdwwkpfsfsnmwyejohgtyxfjmegchytvlsbzguaxvvucqrsptom', 'wyejohg'), [40])

    def test_case_435(self):
        self.assertEqual(pattern_match('vbmbgsykcuklvyhrwpvaaucihosv', 'vbmb'), [0])

    def test_case_436(self):
        self.assertEqual(pattern_match('lqakpysptiafpdvbeehcputnfvofqwgudmetmoumzudidzdhcmfjkggyrdkgcoldwhclpgaecehzdyzkktqcxdbokj', 'g'), [30, 53, 54, 59, 69])

    def test_case_437(self):
        self.assertEqual(pattern_match('kzvswqxxgtvbnincljfzmbnalkgksmdmoztuioijgprtu', 'xgtvbnincl'), [7])

    def test_case_438(self):
        self.assertEqual(pattern_match('lbfxwpgcelnvloflvgkzsekpfxphyjqi', 'lnv'), [9])

    def test_case_439(self):
        self.assertEqual(pattern_match('nopumbhggdutwxugpuofztcmcfzymokxiycyarmroudxnvnnszkqvnfybmaqqrbeownueoynuneizojwuufhpbkmighgomvt', 'tcm'), [21])

    def test_case_440(self):
        self.assertEqual(pattern_match('cuczijboztx', 'czijbo'), [2])

    def test_case_441(self):
        self.assertEqual(pattern_match('vcpgeoawqpavxjkzmemlyuagukrvre', 'pavx'), [9])

    def test_case_442(self):
        self.assertEqual(pattern_match('yhxdwoxzgtjzvylahayffxsaqkysbarchetdzuxwanmlucuhvijplubmyizfwkehtnufvzofpxptjbkkqsdgxkutz', 'ehtnufvzof'), [62])

    def test_case_443(self):
        self.assertEqual(pattern_match('ndrdogatrvpvrewpncfupvqraizyz', 'trvpvrew'), [7])

    def test_case_444(self):
        self.assertEqual(pattern_match('manaqdkgkhtipzxjopvafywzkbade', 'aqdkgkhtip'), [3])

    def test_case_445(self):
        self.assertEqual(pattern_match('mmkugtwqqbbwgyuyxoodgaaxudhwqmxwdauxpvyreotzkifcvicfmxxmalxwgbgxgqaptocvlvivsoxfjxtmjigehp', 'pt'), [67])

    def test_case_446(self):
        self.assertEqual(pattern_match('atkjtbfrtxdaskoblxwdatf', 'tkjtbfrt'), [1])

    def test_case_447(self):
        self.assertEqual(pattern_match('yhykifotmnjjzrjrwzfxvgwap', 'njjzrjrw'), [9])

    def test_case_448(self):
        self.assertEqual(pattern_match('zqcendvzucsdzprxgqmi', 'csdzprxgq'), [9])

    def test_case_449(self):
        self.assertEqual(pattern_match('azhpoukjrguklwireizgrgkrltwjaumcfxlkjvxrgfmuokwnztjellnnkacdsiiqyqhdcruzmlysxljg', 'rgkrltw'), [20])

    def test_case_450(self):
        self.assertEqual(pattern_match('kthwsrkdbkfbnhkqlhohpmhpljkfuvupiclsclbqbl', 'dbkfbnhkq'), [7])

    def test_case_451(self):
        self.assertEqual(pattern_match('qhhxvrepcmdfzguhlalpnxaqrqapyhhdwynsuewwjgqjdhdaygmrkpjgyicaxsfoyrumavxlv', 'pyhhdwyn'), [27])

    def test_case_452(self):
        self.assertEqual(pattern_match('crrhlkfambfmxgevjaoyje', 'bfmxgev'), [9])

    def test_case_453(self):
        self.assertEqual(pattern_match('ylzhkwukqjtufqxgfnxrpzbakppm', 'r'), [19])

    def test_case_454(self):
        self.assertEqual(pattern_match('qkcjsnqbtekjifjkylcnzmjmxsekmxhciveneapdlaqhii', 'kjifjkyl'), [10])

    def test_case_455(self):
        self.assertEqual(pattern_match('qijhfxntkeoauhgmishhwovqgrvqakgsptzcetfvtn', 'auhgmi'), [11])

    def test_case_456(self):
        self.assertEqual(pattern_match('oulzasnvsfqxvszisgovifrybbqfqawadfygmtfgyvhwawxzilcypgzfkczdktkngrtvkhamcanywliddrahqehuqumbtfyum', 'xvszi'), [11])

    def test_case_457(self):
        self.assertEqual(pattern_match('uyydjwiqxrerjpimrbsieumlpljbtqjcnnsynzydmouhovmhblglnibyotbgetzl', 'lnib'), [51])

    def test_case_458(self):
        self.assertEqual(pattern_match('qudupugnynywahpoinjsdhb', 'yny'), [8])

    def test_case_459(self):
        self.assertEqual(pattern_match('shjxxapzlwofmwdypxgdlzanrcguvepoivjffwlecifggmijvhjtuxchzvierkjbuyvnuigjjowbraezsptrndpuzpmamtshp', 'ggmi'), [43])

    def test_case_460(self):
        self.assertEqual(pattern_match('mvhrqjxraesbtzyvbsstunkkzmzxyfcbciseuuk', 'b'), [11, 16, 31])

    def test_case_461(self):
        self.assertEqual(pattern_match('ikudfeifwlsxhndculxhbanmgyfmctpvyxmgxrmlflj', 'hnd'), [12])

    def test_case_462(self):
        self.assertEqual(pattern_match('mvafgycyzopfljbkn', 'v'), [1])

    def test_case_463(self):
        self.assertEqual(pattern_match('grfukdhzbtccbgguugdroiuddayzrdytguiuwkmuruushuruldcpmrdpxlpajyulpsfcgxw', 'btccbgg'), [8])

    def test_case_464(self):
        self.assertEqual(pattern_match('bxzizbbvxqtsvorueemqaxqoknkunauuvwngxxexcjqhirouumajndoiucejp', 'irouu'), [44])

    def test_case_465(self):
        self.assertEqual(pattern_match('zzwfaprorxqkzugayxleulhcngmozanegdlnczjesvfslrmedbjikpkyxuziytyfwtfnpwup', 'z'), [0, 1, 12, 28, 37, 58])

    def test_case_466(self):
        self.assertEqual(pattern_match('luerpunwzpkzcexieqxtrhzldurkqfmmjvdybgeqqhpqphbibjbemyjvylbkcwpbiqmykidzkgexkimsjqjopletfnlyxx', 'jqjopl'), [80])

    def test_case_467(self):
        self.assertEqual(pattern_match('qdwypbivmkxkejimexjcekkywcybgtojqiofbkpeiurrewmrupkcbebglsojkvkugplck', 'kywcybgto'), [22])

    def test_case_468(self):
        self.assertEqual(pattern_match('rylkjlmhpqhllkurwbfcxuueufpjngqeenjmfblvlfq', 'mhpqhll'), [6])

    def test_case_469(self):
        self.assertEqual(pattern_match('oaezqsqzookwysuggwgnpzz', 's'), [5, 13])

    def test_case_470(self):
        self.assertEqual(pattern_match('otqbejnfebphjlyrfesrlvwmwujxexnsiodaibxgtbkeqntqvvndfykcykpg', 'lvwmw'), [20])

    def test_case_471(self):
        self.assertEqual(pattern_match('nsmjyjiamproofgkylxnisd', 'yjiamproof'), [4])

    def test_case_472(self):
        self.assertEqual(pattern_match('vkmbvqooyo', 'vkmbvqooy'), [0])

    def test_case_473(self):
        self.assertEqual(pattern_match('edleiiqeufgwgjcxgabjjrrtemnqejhuouuvfhcqmclxeztyaghclacaujpxreosyzikcpfkmzsx', 'uvfhcqm'), [34])

    def test_case_474(self):
        self.assertEqual(pattern_match('txszwtdpzieltfmfvursvukvhgmdvimmoblqcomdoakxuiunxdpdteznnsdgjckbeqwpqxvgzyngqxfmjfdjypducwvzjmj', 'qwpqx'), [65])

    def test_case_475(self):
        self.assertEqual(pattern_match('zdikwckfobauxdxajhpejzmkcrgndwonhzhgsjykmpaqulbizafblydmecfvkssjwwybyniw', 'ulbizafbl'), [44])

    def test_case_476(self):
        self.assertEqual(pattern_match('lawervyjcvgxfxoojpemod', 'vgxfxoojp'), [9])

    def test_case_477(self):
        self.assertEqual(pattern_match('lkwniltqpmeumndufitrpyfjtpna', 'lk'), [0])

    def test_case_478(self):
        self.assertEqual(pattern_match('qdlwbdqmhbparxtzqclaalardikalpahfyqmxvhtcizlhrrhenrnhvczsewazjpeenzchtmzsdy', 'dlwb'), [1])

    def test_case_479(self):
        self.assertEqual(pattern_match('dlcssppcbpbsbslzgkgyadgmepumnywnmxpmqqoghgdwvgkhgbsnw', 'hgd'), [40])

    def test_case_480(self):
        self.assertEqual(pattern_match('qvuqkkqhqywptfntloopxowcujleptyrdypqheuojxouhnhd', 'xowcuj'), [20])

    def test_case_481(self):
        self.assertEqual(pattern_match('jdphubuzrtnfzpybhnkqhovvewuyetfouabqpjgosrrcaxxwrvrcmdnwrffbetzpupmyfpamyeibivrlygue', 'phubuz'), [2])

    def test_case_482(self):
        self.assertEqual(pattern_match('szagmkdsywlshfvkplvjkutkhtehzgnstdnjwmcyyhdugkdmbkrnffzunjbtnujxmcxwbbiwcmtvoackwmnlwjwlqiujyhzczlqg', 'vkplvjk'), [14])

    def test_case_483(self):
        self.assertEqual(pattern_match('ksrhahrzluqdrfspojeimrjnrhpmsreixkywqmusjzoqanmtfkzyelkaalkqrywhsjokbauwgrrwfcxmqgpzfprcjtfjefknkq', 'w'), [35, 62, 71, 75])

    def test_case_484(self):
        self.assertEqual(pattern_match('vsqgsyhlleaodnzmwukxfhfhjyggjjfujnvlkjhxejlrrksiedimnnkbvvubbe', 'imnn'), [50])

    def test_case_485(self):
        self.assertEqual(pattern_match('bmzsgrkvmisdguvdeyghdfpgocroruivduthjlmzrjzyirliozeziltmddotpyogynxhdajvulebthisibjbkfpk', 'l'), [37, 46, 53, 73])

    def test_case_486(self):
        self.assertEqual(pattern_match('bsimuevbowmoqfpiiaasialcsdhrgvcfgunmpw', 'piiaasialc'), [14])

    def test_case_487(self):
        self.assertEqual(pattern_match('nxeygrmagqbnhauvywzjbpvlftdnklhrngshvhnbkooqdllasifsctei', 'jb'), [19])

    def test_case_488(self):
        self.assertEqual(pattern_match('dsubqvgztdazrjiudgrmjirfnmetbueleqrxxs', 'dsubqvgz'), [0])

    def test_case_489(self):
        self.assertEqual(pattern_match('izxfvvehtpbnmadskbfjpbfgmliejeqlxecq', 'fjpbfgml'), [18])

    def test_case_490(self):
        self.assertEqual(pattern_match('iedrxpbojixinjtvtmfcmavisksdlhmykna', 'vtmfcma'), [15])

    def test_case_491(self):
        self.assertEqual(pattern_match('dirdrkvhfxfwaypsjitgjtlwskcxnjxrdlpwgyfqjaekwvnbkdbqwaxzmzhxberxmzpbthszbvvhdngnhpohbttzcebyqjamohj', 'it'), [17])

    def test_case_492(self):
        self.assertEqual(pattern_match('ygggitbfywncezrmnwvsyxhfhflwunklttudkkaeddwujo', 'vsyxhfhflw'), [18])

    def test_case_493(self):
        self.assertEqual(pattern_match('ychmnulgtngacvyjfvpbtews', 'nga'), [9])

    def test_case_494(self):
        self.assertEqual(pattern_match('gqbibheafyreenztntan', 'ibheafyree'), [3])

    def test_case_495(self):
        self.assertEqual(pattern_match('yrblkrvhxaeybllleanquarsbfxzqhwzqxinubj', 'a'), [9, 17, 21])

    def test_case_496(self):
        self.assertEqual(pattern_match('ygsyatapawtmndiecspd', 'wtmndiecsp'), [9])

    def test_case_497(self):
        self.assertEqual(pattern_match('befnqsjhkqwbasiixgsmxrwvbsepfdrstdjqplbpwwyarbzomxvqqmrnfquukopnsosyo', 'qqmrnfqu'), [51])

    def test_case_498(self):
        self.assertEqual(pattern_match('qclehexrbuh', 'le'), [2])

    def test_case_499(self):
        self.assertEqual(pattern_match('ccefqfawlallzozbxdtznmnyodgfabfjdcepoeynnycpt', 'yn'), [38])

    def test_case_500(self):
        self.assertEqual(pattern_match('jzeudmnvbgwsgtdmnbjfopxcklzpzgtlyvzcvstkkuphptngfelqibqmplzaaptiisqmhb', 'bg'), [8])

    def test_case_501(self):
        self.assertEqual(pattern_match('djzrapddhcoavxnwkvllhkziieatoyzdakhbybnsybdoawxicbkqethogbmpxfqownuaztyhrgqkizhguipifywnt', 'hbybnsy'), [34])

    def test_case_502(self):
        self.assertEqual(pattern_match('ezhkwertuqf', 'hkwertuq'), [2])

    def test_case_503(self):
        self.assertEqual(pattern_match('qdgcxlpoelxtfjpkxntrmqkowdmkivxxnyljpekjzfptqfqiavqkapgjrpjensoldyjm', 'kivxxnyl'), [27])

    def test_case_504(self):
        self.assertEqual(pattern_match('orssagaqhetrnzuvwfgersliodaugkylzndnwvancfolmpmpwhcwdwmxcrzxgetykchdsopyrlunuaolcoiskwfcutqlq', 'od'), [24])

    def test_case_505(self):
        self.assertEqual(pattern_match('ykgswpepxpgtgyxrrreryziazwkdikhkbhkaan', 'wkdikhk'), [25])

    def test_case_506(self):
        self.assertEqual(pattern_match('niqdvdxoommfidrbrffrnq', 'rbrffrnq'), [14])

    def test_case_507(self):
        self.assertEqual(pattern_match('kmjuykiavdhqhndynenudgcuargifoijbqkdjnxkssdlphypkfjsixwwnnhwoyvyshejaspqpbkin', 'vy'), [62])

    def test_case_508(self):
        self.assertEqual(pattern_match('eouokibwjn', 'eouokibwjn'), [0])

    def test_case_509(self):
        self.assertEqual(pattern_match('uxygfdjcjkywefpqgpkytsvn', 'cjkywefpqg'), [7])

    def test_case_510(self):
        self.assertEqual(pattern_match('iyiiphkruptsemswfa', 'phkruptse'), [4])

    def test_case_511(self):
        self.assertEqual(pattern_match('xfjujbivgpnhzynhftizweijekxtbrybcpwxkekvxdhebwhoqqddrpegxtaxowqjynwkvtridyltwftu', 'vtridyltwf'), [68])

    def test_case_512(self):
        self.assertEqual(pattern_match('qykucjrocexhybtfgazhxnblhdggcnqogeyrgsywrbfmhoxpavafvulunp', 'zhxnbl'), [18])

    def test_case_513(self):
        self.assertEqual(pattern_match('ejwznabgfscnftcuautxylolatzvtgaeyfhetzoqwfsqntnexkrfafoszjxoijzicfnfryhoiug', 'tzvtgae'), [25])

    def test_case_514(self):
        self.assertEqual(pattern_match('svnuxeqwgyxhjcswpvlsjjxxavrcvugto', 'lsjjxx'), [18])

    def test_case_515(self):
        self.assertEqual(pattern_match('suelncwljorpmczyjdfjaudpscbjykcocfunrfwcyxppftvfejvlgpjypmojodzfphrgwulcgnbrchpartphdljg', 'zfph'), [62])

    def test_case_516(self):
        self.assertEqual(pattern_match('hotdljkafcwrlfaekihvkstcekworxxstwfnicjbfybabkqljxdiqmdvyjrtjdkahmyphqltls', 'bfyb'), [39])

    def test_case_517(self):
        self.assertEqual(pattern_match('ieydhjmvpgekktufykwzvhiqwupjfsmtwlcpozsmhlwhmgmmrjoehvsbmmgnakhgrxminjafpzinrdqsfwtt', 'smtw'), [29])

    def test_case_518(self):
        self.assertEqual(pattern_match('dmhlglyomgdepldshkwgifhxkcdpiwjmyw', 'lglyo'), [3])

    def test_case_519(self):
        self.assertEqual(pattern_match('lwgtdtvfeyvkaqbacetjafxprzfpmnuyyhpawtvmdbvyeqwpnvcajqkcslikzw', 'vcajqkcsli'), [49])

    def test_case_520(self):
        self.assertEqual(pattern_match('hdbwkczuoqeiafalqkznxmhrupyhhphdrwpwscziyscvxapomdtubmpyssti', 'hrupyhh'), [22])

    def test_case_521(self):
        self.assertEqual(pattern_match('tbobipytpfpuhyrafwkskrvlieqkoqcbazrllglkfzswwceelavkiwudswfkfegkxbzgpxkwypztwugbkrr', 'qko'), [26])

    def test_case_522(self):
        self.assertEqual(pattern_match('nidmbvmjntysllgedlbjnzdqasvewvrkfvaajqfjcwvrqpd', 'rkfvaajq'), [30])

    def test_case_523(self):
        self.assertEqual(pattern_match('axsnmixcxjwvqthngtodalupapkdnabuxtffqodvwlxo', 'apkdnabux'), [24])

    def test_case_524(self):
        self.assertEqual(pattern_match('nawofigickrgwaz', 'o'), [3])

    def test_case_525(self):
        self.assertEqual(pattern_match('tcxdaaatmiylgdy', 'a'), [4, 5, 6])

    def test_case_526(self):
        self.assertEqual(pattern_match('ibzmqhrpjyzds', 'hrpjyzds'), [5])

    def test_case_527(self):
        self.assertEqual(pattern_match('rabycxhqeepnapvfkyrlwddvgvmfecetswrlvlntyamygfcfn', 'ycxhqeepn'), [3])

    def test_case_528(self):
        self.assertEqual(pattern_match('nypcmxbnubriemggblhcdxtailsdywrseyifpxrmkvtdkrdixmkcczfefwvdaz', 'bnubriemg'), [6])

    def test_case_529(self):
        self.assertEqual(pattern_match('lhigpmdsaqkszklacmfjrpfnbowtwyyqdexniqp', 'gp'), [3])

    def test_case_530(self):
        self.assertEqual(pattern_match('dvnhgmjmugqabtautjbgetrdeczmstmnjswyqjythnemrielpxdqpwgcttdzfyxfndbmxmzqmgvtc', 'bmxmzqm'), [66])

    def test_case_531(self):
        self.assertEqual(pattern_match('ieavcurqhpgzmffsxrgxafyjtf', 'ffsxrg'), [13])

    def test_case_532(self):
        self.assertEqual(pattern_match('zhenawawowkpfzwyedb', 'owkpfzwyed'), [8])

    def test_case_533(self):
        self.assertEqual(pattern_match('otifvwazrqqwolomuhgiwpztldjxjixaxfnjxknddlsyyedoo', 'qqw'), [9])

    def test_case_534(self):
        self.assertEqual(pattern_match('lvhqtlrlnxaaxurakctjmwafcbfdqeavpdblumwbfzgfuxxdnqvlnkesuthhvtrdszqmzquqgpwvdotqjfldkttfdkmmeensht', 'mwbfzg'), [37])

    def test_case_535(self):
        self.assertEqual(pattern_match('utfkujgwnuelmugxvnmdeovnugujkogt', 'eovn'), [20])

    def test_case_536(self):
        self.assertEqual(pattern_match('lwvcsfpiycszjtjrpaykrhxtdyeqjyuqmlbpafodigvdkqxtduinceuycomyewidysmdomswpwqibskkuhthewl', 'yewidysm'), [59])

    def test_case_537(self):
        self.assertEqual(pattern_match('bmzoprvzydotdjvpvobvfvyppawgwyxynxvvjokqqgtkxmjko', 'otdjvpvobv'), [10])

    def test_case_538(self):
        self.assertEqual(pattern_match('cpximzfswofhxzfuzlvmtsszfubnysnuzaluhoqysopzjuitpaqlwowdletnzjdstwmhrfkbbmuzvhwjmeicbhnimefwmpguyznl', 'twmhrfkbbm'), [64])

    def test_case_539(self):
        self.assertEqual(pattern_match('fhfkobovbxhuhhqzqbgjaoricfwssjtijvbpr', 'zqbgjao'), [15])

    def test_case_540(self):
        self.assertEqual(pattern_match('rxorxnqailxlpuijcujxjqnqqgscryxwmnsuztidpnfogzaxhtladbdiikyxbmvlxmfpnlniuszejaiehm', 'pui'), [12])

    def test_case_541(self):
        self.assertEqual(pattern_match('sehacofsklfddfbrrkmgzishidcbpqbquhvdindwkmzpjmk', 'rkmgz'), [16])

    def test_case_542(self):
        self.assertEqual(pattern_match('pluhyemvkjqjjpczlmlijjntnoixkltzeoqnlybxsetaxrlbzet', 'eo'), [32])

    def test_case_543(self):
        self.assertEqual(pattern_match('agpqvlhpcyapiqpvmcjaplrkvnfxrchsurzbtyedipidzeefygkbvkbadhzagrcaspmoxlwch', 'bvkb'), [51])

    def test_case_544(self):
        self.assertEqual(pattern_match('aaxxbxfrkjclzphgjorcucrdfzahataqjivumywplhdiednlcakkfoqrfjlstepxogcwfrotwvgazporvjqa', 'cwfrotw'), [66])

    def test_case_545(self):
        self.assertEqual(pattern_match('lswtkmntelkejifavrrlmopfnxzxzpcijyvlnsb', 'lmopfn'), [19])

    def test_case_546(self):
        self.assertEqual(pattern_match('tyghbtlabucmugmjl', 'abucmu'), [7])

    def test_case_547(self):
        self.assertEqual(pattern_match('glbtlakyvqfrtxljvfgvdnaamxhhoxbgtwerdxurcprhgubplxoxhonhikaefojdzwwzwwdcmkeodthonwuikdxczrqnpl', 'cmkeo'), [71])

    def test_case_548(self):
        self.assertEqual(pattern_match('pekfzgnndydbuynzggx', 'n'), [6, 7, 14])

    def test_case_549(self):
        self.assertEqual(pattern_match('vnrjrgygtvuvmshl', 'nrj'), [1])

    def test_case_550(self):
        self.assertEqual(pattern_match('gziydrhnqbzjuzqzexgpynazmltptiezsmfnlexzcrdtesybtqgboupuyuzrbbuermipqtot', 'ezs'), [30])

    def test_case_551(self):
        self.assertEqual(pattern_match('kaspbmxfnbgninuyzparlokhfyubirokihycndeyhkvfytaiwvxtudrrfptupfwbuyxwxusgb', 'vfytai'), [42])

    def test_case_552(self):
        self.assertEqual(pattern_match('zfqjewnjpvznabweqekilpkefpbndqibxoitokwbtdutbrdbmlcpsadeojrtemzfzglahimsz', 'z'), [0, 10, 62, 64, 72])

    def test_case_553(self):
        self.assertEqual(pattern_match('ileuwqxhddjogsgizfyxgdgzbsyfgjoelkbxbmhklzviqtllomanmczjlriszehjjpxbilssnt', 'lomanm'), [47])

    def test_case_554(self):
        self.assertEqual(pattern_match('zarweidqllavbhinqgufzcwxukdzmqcjty', 'qcjt'), [29])

    def test_case_555(self):
        self.assertEqual(pattern_match('kjamhyqcyyguekhowbrhhyexjyw', 'qcyyg'), [6])

    def test_case_556(self):
        self.assertEqual(pattern_match('zsfjpoopoqpyrlrnmzevjfnttgchsomhrprbenyzgstqczgcafzwtioyqtdregohzbdzyvszlylec', 'ti'), [52])

    def test_case_557(self):
        self.assertEqual(pattern_match('pduxcmpywvmxiixooytkerncouauxaolktgttawjmxfbxetnycncadbabjpoffupbmjhnmcoiwxzhu', 'a'), [26, 29, 37, 52, 55])

    def test_case_558(self):
        self.assertEqual(pattern_match('pftjdbiqzjvjoigjybvzmairkgkxsenjtxtlxveddkiaa', 'jdbiqzjvj'), [3])

    def test_case_559(self):
        self.assertEqual(pattern_match('nhmipmzqyzqsqgewnvvtxyxsvgnjwfmjxfpnnpqefqhl', 'vtxyxsvgnj'), [18])

    def test_case_560(self):
        self.assertEqual(pattern_match('vktehzhtqhwxoygtjdmkznzrdakmwcfjjdqwbebpbpducmeopdphuuwlkouowgjnybvpiizasapbxaamcsvfzbypwojpd', 'meopd'), [45])

    def test_case_561(self):
        self.assertEqual(pattern_match('fasgdotevwfgznbqrdjbiuuhxhape', 'dotevwfgzn'), [4])

    def test_case_562(self):
        self.assertEqual(pattern_match('mszfdekjdbsjdqnifsfozqezhclssaxrxlcqeeqqss', 'bsjdqn'), [9])

    def test_case_563(self):
        self.assertEqual(pattern_match('dtkghchaamvxcyukovocypqzueaalenhvrjzohm', 'chaam'), [5])

    def test_case_564(self):
        self.assertEqual(pattern_match('quvhhxydyz', 'xydy'), [5])

    def test_case_565(self):
        self.assertEqual(pattern_match('ueawiahbgxbscfmmhxovnsfcvvmum', 'iahbgxbsc'), [4])

    def test_case_566(self):
        self.assertEqual(pattern_match('zfhmndeemebgsg', 'deemebgsg'), [5])

    def test_case_567(self):
        self.assertEqual(pattern_match('makzgjzxfnhlvxjkngbpnmrtqqqqnjuqjycljzfvqvbrocuzqahsdeyba', 'jk'), [14])

    def test_case_568(self):
        self.assertEqual(pattern_match('jhdlbubfaljktblnd', 'bfaljktbl'), [6])

    def test_case_569(self):
        self.assertEqual(pattern_match('dincjueaaryqtilhlgekdtjffybqtksxuicqxaiamuxflwniekxsznqcthpmqbxkcvqxdgqnvbnee', 'fyb'), [24])

    def test_case_570(self):
        self.assertEqual(pattern_match('cntwzbifamanblkhevwchgljpouaobdwvdgqpqzqzyefnoypkhpi', 'hevw'), [15])

    def test_case_571(self):
        self.assertEqual(pattern_match('vxwxouhprgjdiqadxdfzbgqykemakkaanhkksqadkkixbdeqnuvlxtilrtzkb', 'aanhkks'), [30])

    def test_case_572(self):
        self.assertEqual(pattern_match('qrlclfovmjqynaovjiruqkzcmsmdbmtwxcfjsafdyntyalpmaamcvspbluzzxwcvcvmrmjrehrtxybkufavfrwxgremxp', 'kuf'), [78])

    def test_case_573(self):
        self.assertEqual(pattern_match('gxkkjrojsyjia', 'j'), [4, 7, 10])

    def test_case_574(self):
        self.assertEqual(pattern_match('natgxdaqdrangageyagajftjogpitybxccsiylunqfheyviiydptjfhla', 'qdr'), [7])

    def test_case_575(self):
        self.assertEqual(pattern_match('dvalpaeuswgvndshgjygacemqlluqpfyfxggweipqejwzgtkasxfrlmcm', 'sx'), [49])

    def test_case_576(self):
        self.assertEqual(pattern_match('mjzmhokfmksfsjtmpafyeeinlsnkbwobaprrvfkmquztlgjkdaqsmuzbzmpzufeinlkohrtsqcozfszutlqheakww', 'k'), [6, 9, 27, 38, 47, 66, 86])

    def test_case_577(self):
        self.assertEqual(pattern_match('nmtjegmujccfruhyh', 'nm'), [0])

    def test_case_578(self):
        self.assertEqual(pattern_match('yuvuoyrvqvoelngtriizfxcbrqdndqkwuwo', 'yuvuoy'), [0])

    def test_case_579(self):
        self.assertEqual(pattern_match('zlyinakexrxgdthssucnmqcqwepkzfflllgsgjqnglojvjsavumq', 'hssucnmqcq'), [14])

    def test_case_580(self):
        self.assertEqual(pattern_match('zexwqnhupckmmyyhrfdbxnnwnqhoglnlzslttyswdrwpobuybaqfmkaseipplsvtqazrbyfabgyd', 'wdrwpob'), [39])

    def test_case_581(self):
        self.assertEqual(pattern_match('ujpmnnpaorwninxlsswhataotpdpqjbommzcrfquyshvbni', 'tp'), [24])

    def test_case_582(self):
        self.assertEqual(pattern_match('dwzvjutwcoxovywzpztonefevgdphxajghwddvabmhrlmfjvdjntlomynklhbxyckduaxeoyglzzvarbhktvctywocvoqwlp', 'h'), [28, 33, 41, 59, 80])

    def test_case_583(self):
        self.assertEqual(pattern_match('qglcqhuiltborfoojmsewmz', 'orfoojms'), [11])

    def test_case_584(self):
        self.assertEqual(pattern_match('kjwoxkmztcjngungzubovhwggrkyazuwqbssjb', 'grkya'), [24])

    def test_case_585(self):
        self.assertEqual(pattern_match('cbhczosqslroajystuwhovjimxvmjgsg', 'jimxvmjgs'), [22])

    def test_case_586(self):
        self.assertEqual(pattern_match('bkrwguygroatghhxqpeihmaetdhryvveq', 'uygroatg'), [5])

    def test_case_587(self):
        self.assertEqual(pattern_match('saecdlytiekmuapmthxvkf', 'apmthx'), [13])

    def test_case_588(self):
        self.assertEqual(pattern_match('jeajjuuztffqhynbwfyqugpitkdtvmthdkyztrpklzhyomogcopiqpohijngqhluspuonvikyvwmkoflszgtst', 'nvi'), [68])

    def test_case_589(self):
        self.assertEqual(pattern_match('mdktfzufuykxh', 'kxh'), [10])

    def test_case_590(self):
        self.assertEqual(pattern_match('toarieqafksdpuhulvpvijngztlsaotlryxczgcsffmxekofeuwzcttpurnikwwlfdobkljiqqqsfnmxnnsxjgwatvqvbcdztf', 'qafk'), [6])

    def test_case_591(self):
        self.assertEqual(pattern_match('czhjxwlmphucvljzxbtijrehbibbaordtwynhufdbqewzqmxj', 'ucv'), [10])

    def test_case_592(self):
        self.assertEqual(pattern_match('mxbkzungolonjhbqmhmzqmjodbqmufmujhhbgpqhtfcsbquadqdwixuftpfdmbnxtylbtovrczv', 'xuftp'), [53])

    def test_case_593(self):
        self.assertEqual(pattern_match('zvjquxqfttrdywugfoqdxbmodbgadtltguudmbimdjpzmaftjdstxlxninpbnqlhkggmuzqecbimbnvpmftxmvt', 'qdxbmodbga'), [18])

    def test_case_594(self):
        self.assertEqual(pattern_match('mkkoupzlzurszihxtnwiupqobyqjwkyzwajsovbxwlzbdkhufxgyba', 'kyzwajsovb'), [29])

    def test_case_595(self):
        self.assertEqual(pattern_match('iqqwegujtwkonxyvgdeq', 'v'), [15])

    def test_case_596(self):
        self.assertEqual(pattern_match('cmdbtyyoapowpztlzivnfbvwlbjcxnlhulkqhmlrecwhklmhjeiljcmajifubysrrlurkdkrcuxlpztnjntjl', 'pztlzivn'), [12])

    def test_case_597(self):
        self.assertEqual(pattern_match('rtiueilyjg', 'y'), [7])

    def test_case_598(self):
        self.assertEqual(pattern_match('ugyofifcxjhqctlxuksunnclsfluwmpkbkdhjxdgtddfkayngcklxfbrqklzphfzjiuntqny', 'brqkl'), [54])

    def test_case_599(self):
        self.assertEqual(pattern_match('scksseeekxpxjvcjfbuhzaizyontpkkbbtfhlmxcflnhutvflatffmjcpctrlmrd', 'hzai'), [19])

    def test_case_600(self):
        self.assertEqual(pattern_match('lqipncsfsals', 'lqipncsfs'), [0])

    def test_case_601(self):
        self.assertEqual(pattern_match('mxrekvbzcwtjqxxzhdpuxwmhgrtwefdmxmhitnzerpebqnwpxuvjdzmfhsthyncmfcfiibzytkmzsiynomgqpavimznpkfjkvtr', 'fhsth'), [55])

    def test_case_602(self):
        self.assertEqual(pattern_match('wpjyrxqwiimazbdkqqzwyksnvaxotooxdhfunkqrmlegcptvrzwvadarkibovv', 'mazb'), [10])

    def test_case_603(self):
        self.assertEqual(pattern_match('vnlfflzdfdkupwcummffzhkzuyqognpasbxkctfkrfjoojnrinvhqblpwtnjugshxsvgbmdxhdxtjsljaceljollegds', 'yqognp'), [25])

    def test_case_604(self):
        self.assertEqual(pattern_match('zvxsiuhughqkpryznndidoicnkmualnonzuhqm', 'ryznnd'), [13])

    def test_case_605(self):
        self.assertEqual(pattern_match('pamwcpumupnsimqrjqesvwsbqbumvplrdwvayvfjbsjapzzpdhwqimlfxkspidcxll', 'idcxll'), [60])

    def test_case_606(self):
        self.assertEqual(pattern_match('wvcnvpozoydkxivwgjom', 'ydkxi'), [9])

    def test_case_607(self):
        self.assertEqual(pattern_match('vliehkxufnhyuskrhxpzkczomvopghdchgdhxsjpfukvdzszxkyiqdzziqygslbkjkgytdnpistbsjhknxeqpv', 'p'), [18, 27, 39, 71, 84])

    def test_case_608(self):
        self.assertEqual(pattern_match('evztnffnjhnrqeeqgctbkhskpzkgaajwolfwse', 'jwolf'), [30])

    def test_case_609(self):
        self.assertEqual(pattern_match('jfgtbtqgngedvodjofkoyhxikseqkqiimxrmuszqgdntgmwkpmaiqxizgyfwwitiadergmwznaqiinzkljpukdugsx', 'gmwznaqii'), [68])

    def test_case_610(self):
        self.assertEqual(pattern_match('oftrxpdpvsnyarrgqetkiusqajxbwu', 'pvsnyarr'), [7])

    def test_case_611(self):
        self.assertEqual(pattern_match('qyrojlueen', 'rojlueen'), [2])

    def test_case_612(self):
        self.assertEqual(pattern_match('olvyxbthkskvbadkkhmqojbptfelrxbvdnkybfjyysywzyvkabhtezrczeiaumyyalbdltwieqzprccneegrqfliqyvziwatehfe', 'rqfliqyv'), [83])

    def test_case_613(self):
        self.assertEqual(pattern_match('rqwfsqvjqgocbkbyfscdphpschlxayaqrhdqqxwdybhacjewjumehxrikruktyniirsiwjqqfbetnr', 'wdybhacj'), [38])

    def test_case_614(self):
        self.assertEqual(pattern_match('nnrzogsgwtghadleiasmmgytmwqauisjarfockdiwdnadcxqpgbsfud', 's'), [6, 18, 30, 51])

    def test_case_615(self):
        self.assertEqual(pattern_match('xncuiiegweiktsmfgwgbmvfftiotoaxhhjpk', 'oaxhhjpk'), [28])

    def test_case_616(self):
        self.assertEqual(pattern_match('sodqbqkacypl', 'odqbqkacyp'), [1])

    def test_case_617(self):
        self.assertEqual(pattern_match('totocekvmzmggraxhhrkqizttobvvmqusxirekrfnvjvkzsykhkcehlslbxgmsunejqwtb', 'kqizttobvv'), [19])

    def test_case_618(self):
        self.assertEqual(pattern_match('xtcbjvyzzeoekvrdfqbnon', 'd'), [15])

    def test_case_619(self):
        self.assertEqual(pattern_match('liutyzowdvrfrimtapwpksrbbzpqsfkhsrkqmvkdximtifzqcodlrgxamcrwlqun', 'wpksrb'), [18])

    def test_case_620(self):
        self.assertEqual(pattern_match('jjcxkukuyvaricgkdxpfftjaqlpkgxpdvxgxrduohmpmdwtz', 'kd'), [15])

    def test_case_621(self):
        self.assertEqual(pattern_match('hhtzqwnzeecnsutwoeezwkvlicwblccxohtqgrrjvzxbdereszqlccpojytzrshdvpmafdnxyxwuusfhhenl', 'gr'), [36])

    def test_case_622(self):
        self.assertEqual(pattern_match('xgtszodzrfthirghrcapgjmmewaaxhsbtwkcajragcelbhdvqdmdimazijgbxdjjpzqppmgrquxlamgwfxn', 'celbhd'), [41])

    def test_case_623(self):
        self.assertEqual(pattern_match('acyvzcfjmmhljojslrsbuwapowdmcqnghdondiryxuknvttdnocpdcpcxhiurgfri', 'pcxhiurg'), [54])

    def test_case_624(self):
        self.assertEqual(pattern_match('sxejvkeeujbgxpybaeygzorcdzgqytafbrnoaiazbinpjesittjjccoxrjnaklgklcxablrstxsbahmdbninc', 'gxpybaey'), [11])

    def test_case_625(self):
        self.assertEqual(pattern_match('svazokngzqlaignpdbmpmsmrwfxcaypknovtbpjacekgp', 'ignpdbm'), [12])

    def test_case_626(self):
        self.assertEqual(pattern_match('hfsbpeywtdwawrbjnxdtsjicnsxuiwstscvumkhpvtagnzuaytsova', 'vumkhpvtag'), [34])

    def test_case_627(self):
        self.assertEqual(pattern_match('aliujpsikbdukofoylo', 'f'), [14])

    def test_case_628(self):
        self.assertEqual(pattern_match('qfmlqazbpgpcgubbeqapdezkdhvmbowucjddeqgjjtfqxrfhgyriizwlwhqqmbvhlnceroodclbtwuutfxcqkkwjydzhdsb', 'gubbeqapd'), [12])

    def test_case_629(self):
        self.assertEqual(pattern_match('dcvnwttxcchzicnilotqvjtfwgqbunadsdqzepxmdbblnrimxzemhbeokbhusjgghxlccfbuwssrcptwdsvt', 'a'), [30])

    def test_case_630(self):
        self.assertEqual(pattern_match('fargmuyvfutaqxprsggbwhcbxevlswjvgttwal', 'jvgttwal'), [30])

    def test_case_631(self):
        self.assertEqual(pattern_match('ajukhzihdertrwdswjojrgxjamnmrprtclcerdolrykeqzjnicjutypqprkxpebbbxzhruvxhcdbymjtczdwiphxgggncoqipu', 't'), [11, 31, 52, 79])

    def test_case_632(self):
        self.assertEqual(pattern_match('sbiujfhxzqwgcnowdmpmsownlykwavfoluqkwdizzshsgkhlaxwremqfzplq', 'x'), [7, 49])

    def test_case_633(self):
        self.assertEqual(pattern_match('gxhzccaqfivbweactkfkanbvxjlostsasnyqgeu', 'bweactk'), [11])

    def test_case_634(self):
        self.assertEqual(pattern_match('melhunraauxbxccdnsyivfnggsd', 'nraauxbxcc'), [5])

    def test_case_635(self):
        self.assertEqual(pattern_match('fhexyyngrwzzslnvzwqhvcdizwnshsixbzqyqktxbtsiplpnvdgdcgfnrmjvreajoounhviiimkh', 'b'), [32, 40])

    def test_case_636(self):
        self.assertEqual(pattern_match('zdfropttblzliumolwcsnyrfrxkggsgenoylxritswttuslfwghpitahpb', 'umolw'), [13])

    def test_case_637(self):
        self.assertEqual(pattern_match('yszufmwodxzhyolcbodigbjnboxeqcmagnuonbx', 'gbjn'), [20])

    def test_case_638(self):
        self.assertEqual(pattern_match('ftxzoplaeduwsvssjevzulaxellbciwqrpubbzbjlgsoryuvygujklgpvbtyftjaflhtfhoqiudtmqjkhbxbhacngwii', 'bbzb'), [35])

    def test_case_639(self):
        self.assertEqual(pattern_match('nbxrkxslmwiknemfldkgi', 'mwik'), [8])

    def test_case_640(self):
        self.assertEqual(pattern_match('wwgdzmbwkmwigltgfllcpdx', 'tgf'), [14])

    def test_case_641(self):
        self.assertEqual(pattern_match('jxefjpoieeagrd', 'xefjpoie'), [1])

    def test_case_642(self):
        self.assertEqual(pattern_match('ehsckmbkyedbiwzonwxojalwwsfhnwlrcfkmasovavbmhudcecepzkpnvlvrwsuslibsaszazlwhuxfikkgymzeubv', 'i'), [12, 65, 79])

    def test_case_643(self):
        self.assertEqual(pattern_match('fezuognxflahrolbafidfykprkqtidjytgbqxjfvccy', 'j'), [30, 37])

    def test_case_644(self):
        self.assertEqual(pattern_match('oxcnuxoqpvgflasoqylbuyeozejifrtzdfegkmlwaunlpsagpfyemamqhxlzykvhfixujrithlzerockyanavkrybmrejediro', 'aun'), [40])

    def test_case_645(self):
        self.assertEqual(pattern_match('smfsbwilydcpwcdwtmgqsrvtfeqbecpbpgsyqpxynjbjpxnbqrvsxxknkogusznfywzcartkkipeq', 'sznfywzc'), [60])

    def test_case_646(self):
        self.assertEqual(pattern_match('vrhiinjujharllphfukwwipxgiydsvgvxqioztmgdqoeyhvuvvbderunlinaaldwkbovxbdrbfjoukrrbkgnrkvinipstqhq', 'bdrbfjouk'), [69])

    def test_case_647(self):
        self.assertEqual(pattern_match('olyobszytgilcmokglvytzhbesvtllviesgrytjbldqm', 'ytzhbes'), [19])

    def test_case_648(self):
        self.assertEqual(pattern_match('ljjqgghmxvtqbsknredoalamvx', 'ghmxvtqb'), [5])

    def test_case_649(self):
        self.assertEqual(pattern_match('difwfwyyahkionyhxwdxgejqrnypqnseueqbtu', 'dxgejqrn'), [18])

    def test_case_650(self):
        self.assertEqual(pattern_match('qszbgnxeuwkhqkakkufqhtpepyjogkfexblyixfhh', 'uwkhqk'), [8])

    def test_case_651(self):
        self.assertEqual(pattern_match('vcnqqqzwax', 'qzw'), [5])

    def test_case_652(self):
        self.assertEqual(pattern_match('vfveegzmuhrllxahiuknfvyzgpxyzibyfashixkffubgnqkuxrwfzodhjvcpliqvlvqmpbkdhgocluhsjdpghsapkqxte', 'llx'), [11])

    def test_case_653(self):
        self.assertEqual(pattern_match('qcqccoqlqfjoyrugzrzbjluvbsncrhdwhcnvblirmz', 'rzbjluvbsn'), [17])

    def test_case_654(self):
        self.assertEqual(pattern_match('vvlflrzsjgsjwitabmfzmgafprkylwxbdkudpoxcft', 'vlflrzs'), [1])

    def test_case_655(self):
        self.assertEqual(pattern_match('axhrdwtjqczzctbjypkyisekrmecqwi', 'zc'), [11])

    def test_case_656(self):
        self.assertEqual(pattern_match('ptopnowcpbnqzhtudgaqwksgbuvfnsronmxdnreaiifilqbstdkbtvzpevydsxffcaliqpapbjukagjz', 'w'), [6, 20])

    def test_case_657(self):
        self.assertEqual(pattern_match('yhmrrejpaulfchbjugutpmfoqrkbczcbyzfuppqushdfrugbjez', 'utpmfoq'), [18])

    def test_case_658(self):
        self.assertEqual(pattern_match('rgdczdeqqwzsellfxrvugnfmgvutpidikndynorrysi', 'nd'), [33])

    def test_case_659(self):
        self.assertEqual(pattern_match('ywybgufpsbuxymkbpwwgdcpkpqousjcavymiovdtoekgvsxfjcitzwqidrezwnlxnrckqkeknejytpc', 'sj'), [28])

    def test_case_660(self):
        self.assertEqual(pattern_match('abvrxohnqxdgdxguirwqkomjbyhywyy', 'yhywy'), [25])

    def test_case_661(self):
        self.assertEqual(pattern_match('kajxepzvnqrezbxlwcqzstapapybahymlbculxydjlnjgtpnanoxastomhpivapyicsvawtqgces', 'awtq'), [68])

    def test_case_662(self):
        self.assertEqual(pattern_match('exkpfwufwzruixcyssnqerbpdutwiaruqgicuhxzjdoznmtjyshdiqlucnjktmpucdqatauhqj', 'nm'), [44])

    def test_case_663(self):
        self.assertEqual(pattern_match('tmbmahhbbrfzvhxdzpckvrkxdkoyutaqkqoucxujlczpwxjkhbswrbwyltsgsqkvpptzjy', 'vhx'), [12])

    def test_case_664(self):
        self.assertEqual(pattern_match('ichteqoojajwxiprojtapzo', 'oojajwxip'), [6])

    def test_case_665(self):
        self.assertEqual(pattern_match('jcskwnyqoqbrepahbnaboafcjmykwzczfzuxfhufdlgicyiyphvstwdbgspbmrkatscceioefxwuixgyql', 'repahbnabo'), [11])

    def test_case_666(self):
        self.assertEqual(pattern_match('xupgcprdupfcagvuftdsylmz', 'vuftdsy'), [14])

    def test_case_667(self):
        self.assertEqual(pattern_match('mlnyqcutwhwbgvffqdnpcspdwvkyjfjgdpsohlcrbipbqucpyvkdguqiuhcfukmx', 'cpy'), [46])

    def test_case_668(self):
        self.assertEqual(pattern_match('ucjrldmjsqlnaguumniygrbonoqpbejojwvteunxogakkrutwknperzb', 'iygrb'), [18])

    def test_case_669(self):
        self.assertEqual(pattern_match('hrpnybkfpshcqnyuccaxtccd', 'bkfpshcqny'), [5])

    def test_case_670(self):
        self.assertEqual(pattern_match('buxsqjxqsnvwwcmwahmststjuy', 'hmstst'), [17])

    def test_case_671(self):
        self.assertEqual(pattern_match('uqqumijwwqn', 'wq'), [8])

    def test_case_672(self):
        self.assertEqual(pattern_match('qxtttjkxvhp', 'qxtttjkxvh'), [0])

    def test_case_673(self):
        self.assertEqual(pattern_match('kyaeayvtfbekhhbqjhmiypqlvbckntifcxbdeljakujqypxxbf', 'qlvbcknti'), [22])

    def test_case_674(self):
        self.assertEqual(pattern_match('xzvzuekvhbcgzdlspazvpnlyccpdxvvdlbzmprtqxtnv', 'pdxvvdlbzm'), [26])

    def test_case_675(self):
        self.assertEqual(pattern_match('stoketwrdmpkotixicntujdmfmihxpozhm', 'icntujdmf'), [16])

    def test_case_676(self):
        self.assertEqual(pattern_match('wmmjkhxspkukncpqdwjodsjvosbmioiciav', 'odsjvo'), [19])

    def test_case_677(self):
        self.assertEqual(pattern_match('kdlaklqgsdh', 'kdlaklqgsd'), [0])

    def test_case_678(self):
        self.assertEqual(pattern_match('ykmrjqadvodyghjyepiljrwmaafnaygiwwltfsxbhqfmwoyugtrqjsxorlbvfqntjozqxsfgjh', 'wltfs'), [33])

    def test_case_679(self):
        self.assertEqual(pattern_match('jzsvdsslbfbnvffnhwoinxcruiywjypusminchfcadcwbumcetfdwjqimphdqrmwvhgyzkqdfmtlohgaqoemcufjwjzpu', 'ruiywjy'), [23])

    def test_case_680(self):
        self.assertEqual(pattern_match('vhyrffhsaufewsudeigchaihvpgshbmhtvxidtarwcirlzycvsbumqoutaflbypqchmslwjyi', 'fh'), [5])

    def test_case_681(self):
        self.assertEqual(pattern_match('usnczyqazlvuisgwjkrusbrbegecoqfpdujhhihuzjx', 'h'), [35, 36, 38])

    def test_case_682(self):
        self.assertEqual(pattern_match('cgrkfcvbbgvmubgdmyhmwljunqgwtkhtxtlqqsmnnjvxyybrafqynabpbjfueqwoofgldddezbzf', 'ynabpbjfu'), [51])

    def test_case_683(self):
        self.assertEqual(pattern_match('jrkxcpuzurgyykjmgtxshihwfjkpygzirhtsuqvxjzqdxknkxftmymgljwvwdjmcdirtikruoptwrlsspmiyiizenx', 'u'), [6, 8, 36, 71])

    def test_case_684(self):
        self.assertEqual(pattern_match('owweeilzgoxdgkhqjfarwsugjsdhnvuyountidjfbgyilgu', 'gkhqjfarws'), [12])

    def test_case_685(self):
        self.assertEqual(pattern_match('axszemssvjsvtstvbsgcdrsldmrufvmk', 'gcdrsldmru'), [18])

    def test_case_686(self):
        self.assertEqual(pattern_match('wxlteltccxdqbptymavsfdnpiqfpxojsdrvtonegaxnafgaqhdvpafzqdooh', 'gaxnafg'), [39])

    def test_case_687(self):
        self.assertEqual(pattern_match('zbqoaytpufzsnemitizaleknhys', 'oaytpufzsn'), [3])

    def test_case_688(self):
        self.assertEqual(pattern_match('dzuayjlpvlggxwnpytlzwrkflmuybgwhcwurgpbdrqddpbvqekzbxqrfe', 'jlpvlggx'), [5])

    def test_case_689(self):
        self.assertEqual(pattern_match('hgayhpmgztaywputlsenkovnplqhwwnfmqnccpbpoexwvfsgrvehfjnpwspmncfeaotyjtgssqgag', 'aywputlse'), [10])

    def test_case_690(self):
        self.assertEqual(pattern_match('jyhibcuxyckrsvkhyrotrhulupkeiqguevtosufhpjlkdnysyjfhnejiapoaldrst', 'hn'), [51])

    def test_case_691(self):
        self.assertEqual(pattern_match('eixfjsbsxxhqkiantnbqgrigctsrnmjy', 's'), [5, 7, 26])

    def test_case_692(self):
        self.assertEqual(pattern_match('abppkumdfqcmighnawyowrtovlhsfxuhfztgdfzovhmqzzmzmgylzhynewkhslqbqaklisoxiuzfdolsqib', 'hmqzzm'), [41])

    def test_case_693(self):
        self.assertEqual(pattern_match('stnzhybnjanflcdutwgfcbgwcxfozovhjzayuqbzclnfojbkpzhpblhhxwiaslcrxj', 'kpzhpblhh'), [47])

    def test_case_694(self):
        self.assertEqual(pattern_match('tycgobektqsjqeyzaodu', 'tycgobek'), [0])

    def test_case_695(self):
        self.assertEqual(pattern_match('gotekobgoqxcltcvgomupkutzellbyfjqgklzruwnuxunxvpfapqp', 'nxvpfapq'), [44])

    def test_case_696(self):
        self.assertEqual(pattern_match('gevxujuiqrjshfymellhqnhmpuadxgxrgbavsvrqkmoxsqzibneqrlwarnslboottfndbrinbfilke', 'ot'), [62])

    def test_case_697(self):
        self.assertEqual(pattern_match('xouxrnogbrdedqjoyvmrsloefcovlrzowgncowdcncadxshdbcyyjemdlvsuadp', 'dlvsuadp'), [55])

    def test_case_698(self):
        self.assertEqual(pattern_match('nggbtcqjfltfgatzmdpnkoqsjtkftobmesbaypjhuhmvegxotxintoqcypynxrnbzmktqyvefqdciv', 'zmdpnkoqsj'), [15])

    def test_case_699(self):
        self.assertEqual(pattern_match('rlmwbtfguwrlacrrndpspuvjxzksustltocxkkdgkgzeetgiapxutrlnvmaqdvpmjyekumityioxdmtrr', 'eetgiapx'), [43])

    def test_case_700(self):
        self.assertEqual(pattern_match('gcoehhrotkmccmvbrgeykizmslkykdjpmmewevulrroijltwrdmzfrjnixnadiintytmtyzvpbnaecfyrbojtfmdkcjxx', 'tyzv'), [68])

    def test_case_701(self):
        self.assertEqual(pattern_match('fxdywmrkhhufoyxfeilblkpnipjardxynkpktjamzhbfbsmenbksyrjtdeexcwgqialipelgmcqvropkmjqcaxcvbajufsxmih', 'xynkpktj'), [30])

    def test_case_702(self):
        self.assertEqual(pattern_match('cufxbermuoshjyrxmgvinqdhzrxsmzxowxargtbcformgkyalhnvvtvwpymqpph', 'pymqp'), [56])

    def test_case_703(self):
        self.assertEqual(pattern_match('deiaftxiqxcsllnhzqtuzagvxclbfzluodqhrolhkkpmmyhgchfzobnrlkewxjouzbfcubovrw', 'zbf'), [64])

    def test_case_704(self):
        self.assertEqual(pattern_match('drxhtnukrelzkuuhpnlidmmbinoffwpjmkxlcidsbjvhhbaqcxiheoccnzygjxspeiesmkwzu', 'kxlcidsbj'), [33])

    def test_case_705(self):
        self.assertEqual(pattern_match('kqfucsymauugiytrjysqmwoorjzlp', 'rjz'), [24])

    def test_case_706(self):
        self.assertEqual(pattern_match('kqfedltkyixzykjjazlbphnaijmtwlhspuhlt', 'uhlt'), [33])

    def test_case_707(self):
        self.assertEqual(pattern_match('jttmertoyjllzfgpnmhklbwkvmoifhyvepsttkcrzat', 'tmertoyjl'), [2])

    def test_case_708(self):
        self.assertEqual(pattern_match('ztfmgjqkyeujytxkowxxhkaqhpwvwipyyczoskyfytpcsqajelm', 'fytpcsqaj'), [39])

    def test_case_709(self):
        self.assertEqual(pattern_match('dotxuawoiegfhgbogl', 'g'), [10, 13, 16])

    def test_case_710(self):
        self.assertEqual(pattern_match('gwctwxwxzubnbgnftitymrfcafyml', 'titymrfcaf'), [16])

    def test_case_711(self):
        self.assertEqual(pattern_match('itxmajbkyxauabudpapvwsfxqogtykbzakrqoypkxnbdrksycnfrkakadalgvulvj', 'vulvj'), [60])

    def test_case_712(self):
        self.assertEqual(pattern_match('msnbeocdppnffufgvwtno', 'ppnffu'), [8])

    def test_case_713(self):
        self.assertEqual(pattern_match('gwwdpjcctbqdhdfkcpcucjukcglzddbvqdnyyvajmrkqcnbi', 'cj'), [20])

    def test_case_714(self):
        self.assertEqual(pattern_match('nouabzoxpwnedhttobrjsxtpvzyipsagg', 'pwnedhttob'), [8])

    def test_case_715(self):
        self.assertEqual(pattern_match('kvtrkofntemuzlqnpejxvdxdwpzzizpbveuqsjzcmtrzabwifebxaocjcavcuxydhtng', 'avcuxyd'), [57])

    def test_case_716(self):
        self.assertEqual(pattern_match('rdsvykhwwemdvkulenguurfessvuoblqdmpplqfccdezqsrqloqpshtbfmcpdeqyltabsipaesjewekvrmxsopfsvfzvakdaehi', 'loqpshtbfm'), [48])

    def test_case_717(self):
        self.assertEqual(pattern_match('qzshhjfjlqjqagwtfeeseddgizejaoqqewlutlasutqzufnwdpzdhkzcpqmzkepoamwxticsuxoysxszfmrtk', 'utl'), [35])

    def test_case_718(self):
        self.assertEqual(pattern_match('fedjshxpsasflqpgaz', 'jshxpsa'), [3])

    def test_case_719(self):
        self.assertEqual(pattern_match('dsfutqxbrdszgiwyhkeza', 'sz'), [10])

    def test_case_720(self):
        self.assertEqual(pattern_match('tpssonthhmzw', 'so'), [3])

    def test_case_721(self):
        self.assertEqual(pattern_match('ctzdhivaxfnymiqnoqoclfxuebvilruxxyxpquvjidxwbweealinksfhpcrirqodmjc', 'ink'), [50])

    def test_case_722(self):
        self.assertEqual(pattern_match('gebgchcooyglqilbsdhwklrbtaiynidmubhaywxndxdeqktrroihjxvfgmfbklstrwugnbbg', 'kt'), [45])

    def test_case_723(self):
        self.assertEqual(pattern_match('gqyluicrduqmbamrgxqwcwjxhbhvdqjendmtvoigorzfbrhjhlvgqivpcuhramibfbmzzeuuizczxmsizttnqchb', 'igorzfbr'), [38])

    def test_case_724(self):
        self.assertEqual(pattern_match('olrjvndhwambjqlqbeforbdhwylccamkoppobpsoeas', 'pobpsoe'), [34])

    def test_case_725(self):
        self.assertEqual(pattern_match('qmzcfqamfogzulgjolahzqzjqdrhbebwhvefaaijajgymdugxlxbzfboobagbbeoicgluzznxirkcqlbdscwpktsmeis', 'fog'), [8])

    def test_case_726(self):
        self.assertEqual(pattern_match('uaegapacanozftl', 'uaegapac'), [0])

    def test_case_727(self):
        self.assertEqual(pattern_match('qzyucolkrpozzvtvwderlwkalnplipwydemgkiszlgdxflqeiyobm', 'plip'), [26])

    def test_case_728(self):
        self.assertEqual(pattern_match('sgbfoamfnmcbhrpyfbcujjeyydppsfhpeqbuyalflgcbhjihnddlzzhavonyweabxeudlo', 'eyydppsfh'), [22])

    def test_case_729(self):
        self.assertEqual(pattern_match('hlugmkosgkdhurb', 'osgkdh'), [6])

    def test_case_730(self):
        self.assertEqual(pattern_match('jvpwxdghlyfdkqkvnfbzmelyfohadrvbygvgnkifkknmtywbikfhobly', 'yg'), [32])

    def test_case_731(self):
        self.assertEqual(pattern_match('wlulpvyrsrxmhngvvepfgyzivyslxtbczmpenmmamxrqbixm', 'mxrq'), [40])

    def test_case_732(self):
        self.assertEqual(pattern_match('sasjdozwxwhicpz', 'z'), [6, 14])

    def test_case_733(self):
        self.assertEqual(pattern_match('mviaxpwheslqonlwyeimzkpumhmlrixzmwjccutsqhwtsguhxfwgnjgougyivyjlbcgii', 'rixz'), [28])

    def test_case_734(self):
        self.assertEqual(pattern_match('zsusthamcsaylekpncixrcbautkptgceawfwecydpvamybfxgmemopqlwagitgoptagu', 'a'), [6, 10, 23, 32, 42, 57, 65])

    def test_case_735(self):
        self.assertEqual(pattern_match('bmxzgimtklabcgvqubdelqxcjhawpngndlswnedimznpyaafktredmqaehkkrmuwbmsc', 'ne'), [36])

    def test_case_736(self):
        self.assertEqual(pattern_match('oknjswppezgovmqmnswuspvnnlxjptzctbbyardbvxvtldptnjbmbwbqh', 'lxjptzctbb'), [25])

    def test_case_737(self):
        self.assertEqual(pattern_match('wzhwymcllwyjfwapbbqqqdocjcanmxckitbeugtvrpcowrrccotxyzgbipvdqouacicxnzli', 'cll'), [6])

    def test_case_738(self):
        self.assertEqual(pattern_match('aclztltqftamtblbxqfdnxnzmfdcechzmrwhiljxphxnjonzjjrbepfudhxgiizyhg', 'xgiizy'), [58])

    def test_case_739(self):
        self.assertEqual(pattern_match('gujnbssiqwqiltuzbqgdfgwvpnqehnfw', 'qwqiltuzbq'), [8])

    def test_case_740(self):
        self.assertEqual(pattern_match('lhnatpmrhaxflclkjqtibmokfahjqvvgkwkegqjkxgwikkpp', 'bmokfa'), [20])

    def test_case_741(self):
        self.assertEqual(pattern_match('qhqcllfengiim', 'qhqcllfen'), [0])

    def test_case_742(self):
        self.assertEqual(pattern_match('oxhgdcayhyokgztkgofxrmxsclfglddogunqwljxtzodcxrkgchxzutikn', 'zodcxrkgc'), [41])

    def test_case_743(self):
        self.assertEqual(pattern_match('nttzugabpcdmotecgzvlxflqtcku', 'ntt'), [0])

    def test_case_744(self):
        self.assertEqual(pattern_match('jwylpqgxlxcjvavrkwdkgfqwkmykctugqihmvmlmdvplvuykbbqfgxqiczhtundmsalcg', 'qihmvmlmdv'), [32])

    def test_case_745(self):
        self.assertEqual(pattern_match('azzqnyxljzyqlcjgfrggehurzmpzjqazmadzqttgfgdemkqpfusngsjvqeipojpiypcygxmfhetdynvwnswelkqmnrx', 'qlcjgf'), [11])

    def test_case_746(self):
        self.assertEqual(pattern_match('wcjrkweaoiexgytqcxecrpblcmwmblvvisamkcqptxwfcnjjlozhgfknlsbcmevtmoajcabddhyqekgik', 'isamkcqpt'), [32])

    def test_case_747(self):
        self.assertEqual(pattern_match('gzowqwoecwwxaioeizxpfeerserkjnhjtmiihvebeioerwjjozgszcdqxnaufwjgezl', 'b'), [39])

    def test_case_748(self):
        self.assertEqual(pattern_match('ehpvnypjhioyjnaqlylcawlqhvo', 'ehpvn'), [0])

    def test_case_749(self):
        self.assertEqual(pattern_match('valseziemauiuvxiwssekwtoukbjqyfllpajgsb', 'ssekwto'), [17])

    def test_case_750(self):
        self.assertEqual(pattern_match('tnzpukclwboqmkfcbkxcjgjgxgxxhjklcgxuqskobajejybtuzwdnledxohdinwuvmjhvkhnealjvykhjaljqw', 'hdinwuv'), [58])

    def test_case_751(self):
        self.assertEqual(pattern_match('ujxyhyvqszcbctleadifvdodektxbkpjykov', 'tleadi'), [13])

    def test_case_752(self):
        self.assertEqual(pattern_match('hbpkgaflcfjnkgfawqvcmviajfmethmzsbwdaosvrbiuipk', 'wdaosvr'), [34])

    def test_case_753(self):
        self.assertEqual(pattern_match('dsvzaaexsvxpuqmzfwucigrikdqgaizcbffylihjekilfohnexbezlbokeqbaaqiqzmhmbgqkjzkvbnlps', 'bgqkjzk'), [69])

    def test_case_754(self):
        self.assertEqual(pattern_match('dnjukpbcqoftljjenyhmaovkc', 'kpbcqoft'), [4])

    def test_case_755(self):
        self.assertEqual(pattern_match('offeaolzmmrtvkgztpyykafhwbqfupdrxoohrebmapyndijfaenokurfsjabaksudfdjnfptystjmhwkugmozoh', 'pyndijf'), [41])

    def test_case_756(self):
        self.assertEqual(pattern_match('jnwphvincoxo', 'hvin'), [4])

    def test_case_757(self):
        self.assertEqual(pattern_match('swwcfoaaohwxaexjxtddykpyj', 'wxaexjxt'), [10])

    def test_case_758(self):
        self.assertEqual(pattern_match('jliaiqlvscmaolqtpeuetebqaopkkulpimktxobpagktsbpxsqcvphvsfqpyagswzropakxl', 'pkkulpimkt'), [26])

    def test_case_759(self):
        self.assertEqual(pattern_match('mcvzlusrjctwqpgykkaikoxuxihpiaqfmvcljedgjmrangoddlbsmqesxldmcildysagyxebzlcy', 'gykkaikox'), [14])

    def test_case_760(self):
        self.assertEqual(pattern_match('ooxbdxvldetshgbfmetwauhtbgrgkpvlhbumebnafwaapbgcaotwpswhragpyfpmwldipxsykxwfkcafqmxlkivegsdjt', 'a'), [20, 39, 42, 43, 48, 57, 78])

    def test_case_761(self):
        self.assertEqual(pattern_match('isprznprxkqeiorwhtkhfnujpberryvnpkotcisjsorzapaqdvrzwwzslfpbpjkebgciufszwvckzngdfvikvqhxqblfogtm', 'gdfvikv'), [78])

    def test_case_762(self):
        self.assertEqual(pattern_match('dsviflckmkqvywgmwnkqnmeofmfngkytioqmefiizbfetsnltvydmtbmarjbjvkxnfunizbltxnanckt', 'ltvydmtb'), [47])

    def test_case_763(self):
        self.assertEqual(pattern_match('imdxirpxpygcerwgcmiopedqrmzrmjnedqtvgbdtofzwjbetitzwynjwjoeoibc', 'mdxirpxpy'), [1])

    def test_case_764(self):
        self.assertEqual(pattern_match('emssbezqozlrgmkujjzfepfvplin', 'gmkujjzfep'), [12])

    def test_case_765(self):
        self.assertEqual(pattern_match('aawjulbeyruaquvfmxtcppucxzsxioqlmlwdczzyxjsiwmsygcjmqzmzbmyzkqzqiudypeirreglmqcdpsgmlavbqndhihkji', 'awjulbey'), [1])

    def test_case_766(self):
        self.assertEqual(pattern_match('tifulmmxoxglzxzwjagahvrosyiwfixdszzsfpnyogvpcjz', 'yiwfi'), [25])

    def test_case_767(self):
        self.assertEqual(pattern_match('fdukpbjwqmsanawcuyhmnxcpvegqmjnynsumacbsmymjbokcvpeowcgxsqycnmupu', 'cg'), [53])

    def test_case_768(self):
        self.assertEqual(pattern_match('yzzwdndttvotti', 'ttvotti'), [7])

    def test_case_769(self):
        self.assertEqual(pattern_match('iylgfnwswbndffwklrfsoczpsymfq', 'lrfsoczps'), [16])

    def test_case_770(self):
        self.assertEqual(pattern_match('qpprowqatmmvbxrxfo', 'xfo'), [15])

    def test_case_771(self):
        self.assertEqual(pattern_match('sibxstahejulstmpatxdmtlxygqufaigkrqojtozeut', 'tahejulst'), [5])

    def test_case_772(self):
        self.assertEqual(pattern_match('jeyadnvaykaghwsatzkbszyujvfllxvywimoyhkjnirkedlovcgsgkjuhhgprglbnyqbe', 'adnvay'), [3])

    def test_case_773(self):
        self.assertEqual(pattern_match('dnzvmapqrlefdrfamvpjvivnzhabixmflqxbwtkqgnlaijoyhabaibxizxoaoyvefryhnpxcphzghqqmezvsfhpxni', 'efdrf'), [10])

    def test_case_774(self):
        self.assertEqual(pattern_match('eugcqxyoiozpxuwzbspnygjnjcbffrpfsdzqsywykrn', 'sdzqsywy'), [32])

    def test_case_775(self):
        self.assertEqual(pattern_match('ccryhahpyaaqwvmrlcoemhxozbynlqpvwiboulmzatcegwbn', 'xozbynlqp'), [22])

    def test_case_776(self):
        self.assertEqual(pattern_match('xpudluekbeyylhoqdiucsq', 'ylhoqdiu'), [11])

    def test_case_777(self):
        self.assertEqual(pattern_match('pksvansdrxgjbggrhaogkzgtrinwpaofdnanymgkibqkxibkgrgepwcfz', 'bggrh'), [12])

    def test_case_778(self):
        self.assertEqual(pattern_match('mlynvmpodzhfeababfufadytpygsucczdbqpf', 'tpygsucczd'), [23])

    def test_case_779(self):
        self.assertEqual(pattern_match('qrtpppxkuudcgrveeujvvwhaqzcxozqqtukbagcrnwzosgpxonckarvcxgjogbbdlil', 'p'), [3, 4, 5, 46])

    def test_case_780(self):
        self.assertEqual(pattern_match('ntkfxrdetajxwdwchyjiamgfqabyvpgrlfmfdbiymkfqjkgytmbfmp', 'tajxwd'), [8])

    def test_case_781(self):
        self.assertEqual(pattern_match('lmwefoakzcvyzihurprwahwefvzgzysidevgcftwgcsrfdngwhnwcevmzpzjoaefpnzledaeprmnsjrdizwtqehz', 'hnwcevmzp'), [49])

    def test_case_782(self):
        self.assertEqual(pattern_match('wvfwwwdzhkzguthmhinxawrghxrgudlsrm', 'lsrm'), [30])

    def test_case_783(self):
        self.assertEqual(pattern_match('kbqgjxolqsygbioeukcuizafalzsvbhawaqeakbwfljwvildmpstaduvruarz', 'a'), [22, 24, 31, 33, 36, 52, 58])

    def test_case_784(self):
        self.assertEqual(pattern_match('kzaltpplbpnyfupybmzowwqenrxq', 'pnyfup'), [9])

    def test_case_785(self):
        self.assertEqual(pattern_match('fpubvlpmiszlmpqwqwfqvlquveztoswosvpaadlpduukcuepmzsaghxfasevtfexfexnayphrsohzbyeswtgdizxbvgfesdw', 'sohzby'), [73])

    def test_case_786(self):
        self.assertEqual(pattern_match('xomqlmzeyhrwjjslscskpksl', 'yhrwjjsls'), [8])

    def test_case_787(self):
        self.assertEqual(pattern_match('umooxnigfrpgqpgnoykofbceioaszavjenfdh', 'ooxni'), [2])

    def test_case_788(self):
        self.assertEqual(pattern_match('duwnxoazvawpwxqycueveqdaeznfufjodriufvzflkhavrmmrbwqdsjywgoixfcvntzwinmrnnxvrh', 'dri'), [32])

    def test_case_789(self):
        self.assertEqual(pattern_match('xfexzldkuppuwqma', 'xzldkup'), [3])

    def test_case_790(self):
        self.assertEqual(pattern_match('fhmxntsevvcrgdomivsjdouitdxvbdyprfbcwnjiwhrb', 'rfbcwnji'), [32])

    def test_case_791(self):
        self.assertEqual(pattern_match('uxqnhstvzultbkkncftoginkesrwbpkhugiaylzlfgdvqzlyezeekfdmdwfhrvdc', 'hugiay'), [31])

    def test_case_792(self):
        self.assertEqual(pattern_match('lezosylhtzidqipad', 'lhtzidqip'), [6])

    def test_case_793(self):
        self.assertEqual(pattern_match('riedjagpmsvuhqiaxjymuvbzwkaw', 'vbzwka'), [21])

    def test_case_794(self):
        self.assertEqual(pattern_match('jujlqvmdcskmvwoedppohcjiwaalwvwgitcswlnyylsblyprlvtwugyvovgvkenzjsdlcumvozvboyqhpq', 'vwoedppo'), [12])

    def test_case_795(self):
        self.assertEqual(pattern_match('afjcrclmjzwdkdcpixcdeyigqafbwwwjkaytpppsseibierweibtxknbuxeybcjrylpaofqxpfxifgjkkjxcaspfcjeecaowl', 'pp'), [36, 37])

    def test_case_796(self):
        self.assertEqual(pattern_match('wkwlgnlllzjuseccteqidwdxbdsxnhxgohqkuwyrrezopiyrcdgdeouivcdfitsnfciibmwhntksglchrpoz', 'ouivcdfi'), [53])

    def test_case_797(self):
        self.assertEqual(pattern_match('aimchmgprjghwutulpawqzwvnrbxjikdibvnzaceyrbjvuymredhgagofgrglicme', 'edhga'), [49])

    def test_case_798(self):
        self.assertEqual(pattern_match('lvvquwspkxxdqmdumhhxdpezro', 'pkxxdqmd'), [7])

    def test_case_799(self):
        self.assertEqual(pattern_match('qqnvrrtirjtuogoklnmncokkody', 'jt'), [9])

    def test_case_800(self):
        self.assertEqual(pattern_match('fakzgufqejphrttxjmzzxykruvvmtqhnucgucsuxexkmuinpkfhgvfurpdnlfwekqdsoekbptzsghxhwa', 'zsghxh'), [73])

    def test_case_801(self):
        self.assertEqual(pattern_match('loqvwnwbbslczyiwhbiojhbtfszgdpnemdxkixeeogsmfjqpngoiovmlmbqlsejjekqsweiigaajhctixjlcuzgxblksvpe', 'jekqswei'), [63])

    def test_case_802(self):
        self.assertEqual(pattern_match('hchsmtdxpnrbuojzmvueiklegfmdhqgolnjizqftrtxkztrpycuqvdpcenavuvpotv', 's'), [3])

    def test_case_803(self):
        self.assertEqual(pattern_match('mcliwtchezjvdyxhbzjczshpiofzwjqqgjgagpikpiwnubxzmajfijjnucncgbsozktfblougoigx', 'liwtchez'), [2])

    def test_case_804(self):
        self.assertEqual(pattern_match('dzbehdrniitzlulosyux', 'eh'), [3])

    def test_case_805(self):
        self.assertEqual(pattern_match('pekdrjoyhzmkwckdqqdullfgjvozoxvmlvutlxoxzudtugptehhpflpqbdkmpxa', 'ozoxv'), [26])

    def test_case_806(self):
        self.assertEqual(pattern_match('rfruzevwjbzsoshljbixqlogulolgoerklxibpowukeg', 'logulolgo'), [21])

    def test_case_807(self):
        self.assertEqual(pattern_match('tjcsumqszrakyctncqdcjtyyqwchaaonqtuybwqgwvnteaixrptysfvpggyd', 'zrakyc'), [8])

    def test_case_808(self):
        self.assertEqual(pattern_match('krorusszecylwfdjmghnfwltlbubcsllmpddeobofadkblplrwgbiaqvnt', 'ofa'), [39])

    def test_case_809(self):
        self.assertEqual(pattern_match('emhsvzxfpmmpcpmiqtmotcrihnlzxmzaafobobgspxyfanbbzkephlo', 'emhsvzxfp'), [0])

    def test_case_810(self):
        self.assertEqual(pattern_match('zanixdlvucusuegztpzcseouascngkpjihtzxizuebgfftko', 'u'), [8, 10, 12, 23, 39])

    def test_case_811(self):
        self.assertEqual(pattern_match('uvxhslzxgqkzjvqbmolclcadggkredaeozhrfgctmwgewrkugrteewwe', 'molc'), [16])

    def test_case_812(self):
        self.assertEqual(pattern_match('idlpjlyrcjqbmccswicnuqfogfimyutlakdbxioswhvoipxcbicoqpcxqjmlsw', 'voipxcbico'), [42])

    def test_case_813(self):
        self.assertEqual(pattern_match('jotfhermrkvteynwuowfynfujnctwgtsrgaieqvithnhccfnexfhgmdhvdlcowja', 'ujnctwgts'), [23])

    def test_case_814(self):
        self.assertEqual(pattern_match('tipzlzezowmfocscycpcmcomnlnfnuytkuagqkpfhqfuviaxccmizpknpvffewwqs', 'zpknpvf'), [52])

    def test_case_815(self):
        self.assertEqual(pattern_match('zwpqtdytbllzcdaimdxigvnduaxmpuhtgagdkcivkjaxodgagukwymndtkzkjrbnmypgymeggkigcjourkkpzycohossxf', 'pzyc'), [83])

    def test_case_816(self):
        self.assertEqual(pattern_match('rjnyszfgmxbojrhmgevbozjfddqvvbknawmlxfgapej', 'qvvbkna'), [26])

    def test_case_817(self):
        self.assertEqual(pattern_match('knekovizjtdqsxxonfzbteodvikawnhluwtlrkhdsixtlxuvvsezhygdhbrrxjilhahhqjcdttfaikrvmgi', 'xuvvsez'), [45])

    def test_case_818(self):
        self.assertEqual(pattern_match('wddyjtpmkjtfljeeigreu', 'i'), [16])

    def test_case_819(self):
        self.assertEqual(pattern_match('lbmtxtsitduornoylrfijmslavyzrblntmeglbvee', 'rfijmsla'), [17])

    def test_case_820(self):
        self.assertEqual(pattern_match('wfdooxfwbahosjswwqgyhiamoyysluicstqirvooalrxnyqegyk', 'y'), [19, 25, 26, 45, 49])

    def test_case_821(self):
        self.assertEqual(pattern_match('ttjcdpnrassygioypqmukpueyeavafpsunyxddivlsxblonvvqlqgmjhfslwvpembdpgu', 'vvqlqgmj'), [47])

    def test_case_822(self):
        self.assertEqual(pattern_match('irocemmfnrncrkwkrgeeunxntbepywudzsfuvcgzcwtcnxctwtemdsaninfcawcqrvehgkcdx', 'gkc'), [68])

    def test_case_823(self):
        self.assertEqual(pattern_match('lovxfhwakluekaet', 'aklueka'), [7])

    def test_case_824(self):
        self.assertEqual(pattern_match('rnyeixgxvihawiqilpanhswlsdsnunihgxiiogfwmfajefqzroufxousxrhgidllbyoxfmubbgytbnyzftvszwxc', 'lbyoxfmub'), [63])

    def test_case_825(self):
        self.assertEqual(pattern_match('kunklygihblwdgpfrltfllghfuqawrdfdiejomlrlwnpiq', 'ghfuqaw'), [22])

    def test_case_826(self):
        self.assertEqual(pattern_match('olxypcbfbldcsjaahfkuemwrawqgnnneukzosanckgzowrdesmujsvpidokyhmloaknxtdzdyxgo', 'fku'), [17])

    def test_case_827(self):
        self.assertEqual(pattern_match('vtxtgaxvkuwzgqmzpfycyutfcefmmbcwtmgzjmrvrmdpkgiuayfjvekkdlsmkxgmuqbuzmwocdqdpxjxuqtgtyzucobskhovthdq', 'vrmdpkgiu'), [39])

    def test_case_828(self):
        self.assertEqual(pattern_match('ekrflevickcireqtmlrcgnppccowfaaurbkhkhndcvvkssoiuuadjijeqcieqgocnhdflfzqq', 'urbkhkh'), [31])

    def test_case_829(self):
        self.assertEqual(pattern_match('ibqqeydaowbfnrkilfvxgfsrepyonmsagkodhtgpdjhgqkfxucvnasdwpfizoszzjqaibowqixbaub', 'a'), [7, 31, 52, 66, 75])

    def test_case_830(self):
        self.assertEqual(pattern_match('qmgbdqmyrdelaeqlhyeadoqbejbjyvztoznqzqpduf', 'b'), [3, 23, 26])

    def test_case_831(self):
        self.assertEqual(pattern_match('dbrrissxjjhnuilttlknsvsbuzvunyavsmeuelczsaogdaqdiacrlpxladbcwozfhgpqiqjmfbprfsamlqqrljw', 'jj'), [8])

    def test_case_832(self):
        self.assertEqual(pattern_match('vvgeynkiurmunxcx', 'kiurmunxcx'), [6])

    def test_case_833(self):
        self.assertEqual(pattern_match('ylsfpcnsdaslfmhotwqdbhvvizwsqraashlvdkzpmqdnudepte', 'cnsdaslfmh'), [5])

    def test_case_834(self):
        self.assertEqual(pattern_match('ooifvzdsevmiobiddxtcil', 'vzdse'), [4])

    def test_case_835(self):
        self.assertEqual(pattern_match('pwrmhhuwlwldadi', 'mh'), [3])

    def test_case_836(self):
        self.assertEqual(pattern_match('lgpwzbforrqkmnxtlyqnmeopzybgwxjyklmqvwsfijfnspbdhpio', 'opzyb'), [22])

    def test_case_837(self):
        self.assertEqual(pattern_match('jdnynzenaqgjulkabibtfaxghsnmlcyvnxluzjjekibfuzeorvqyumuwrdxswwaodwdjfvioniof', 'julka'), [11])

    def test_case_838(self):
        self.assertEqual(pattern_match('cmwfnifykwgdcqkdcabbgoha', 'fnify'), [3])

    def test_case_839(self):
        self.assertEqual(pattern_match('nyrsbrmxkmsotcdkzwtrpfgqnlechudsjcvnfdodqvkdhpdmjkxkvlqvqymvetgnbr', 'trpfgqn'), [18])

    def test_case_840(self):
        self.assertEqual(pattern_match('tbzfqhlyksmkduzdrcbrzxratvjuscosepnhthovfpsengaffxethreomgboxagin', 'xag'), [60])

    def test_case_841(self):
        self.assertEqual(pattern_match('ozwvstzflwcyzohqlsmxbtdaxiuacvhkfasinhfpubgwyzlidjrpregoexvlywgmguantkbsugmlqtgojyvqjleyzqdlud', 'wvstzf'), [2])

    def test_case_842(self):
        self.assertEqual(pattern_match('dklsxryrbntcamtvgy', 'tvg'), [14])

    def test_case_843(self):
        self.assertEqual(pattern_match('qvwfazirbwtfabzyaznnmuqxtagdlekujqvkodlgkiwihl', 'f'), [3, 11])

    def test_case_844(self):
        self.assertEqual(pattern_match('srmpzeqompwjeeilcpahorxlynaniulytjhwuhmpxrelpxxtvjnitqhtrhoqacsax', 'nitqh'), [50])

    def test_case_845(self):
        self.assertEqual(pattern_match('tkpgyxbfykmpcmshpkdqsiwocpcnkxeusyaufcyknmcsxe', 'pkdqs'), [16])

    def test_case_846(self):
        self.assertEqual(pattern_match('wfddpoxxkbyuritixvdjvzahcxthgwxzhaemzpyvjdsbbldsixlzqvckjcyfftwcwahndmdkiaguhneuszazt', 'vzahcxthg'), [20])

    def test_case_847(self):
        self.assertEqual(pattern_match('gehiysubiovq', 'ub'), [6])

    def test_case_848(self):
        self.assertEqual(pattern_match('rphcewmnbubrnxtwwharuvfzoddyhajhxzhhukinqojpkbnyeetikouiyscdpqxnbxfjhsuoxsqsmwxiwrpehej', 'h'), [2, 17, 28, 31, 34, 35, 68, 84])

    def test_case_849(self):
        self.assertEqual(pattern_match('uhukavsyhvftc', 'kavsyhvftc'), [3])

    def test_case_850(self):
        self.assertEqual(pattern_match('wlgwdhyiucvrwgmtokxpuxvkuqtuamrpxitwcyzulnqfdfvsrau', 'puxvkuqtua'), [19])

    def test_case_851(self):
        self.assertEqual(pattern_match('iyqdwhdnzjuvhktafiwirnhiihzyuhiusjpwekraciegmmrneadaobidxcvnxwmyqlywjshdonleurjypxkjowrqxqugyt', 'eurjy'), [75])

    def test_case_852(self):
        self.assertEqual(pattern_match('baauiuuzjjjjndzslzltscsdimdkpcxsy', 'zslz'), [14])

    def test_case_853(self):
        self.assertEqual(pattern_match('vozxiiaeduidivtwsavldzvbnknkczzpvnntngkjjmmyfowqbjdyyhjdxvevssskomgekbddicfayaggmo', 'cfayaggmo'), [73])

    def test_case_854(self):
        self.assertEqual(pattern_match('wjbwvrvzglhwbzwdfgtipluyzo', 'glhwbzwdfg'), [8])

    def test_case_855(self):
        self.assertEqual(pattern_match('ivbyclzyxpvlirktybvpqtmweromxxsunuonhfzbehhoh', 'byclzyxpv'), [2])

    def test_case_856(self):
        self.assertEqual(pattern_match('msgvpaalzkklejpkyrjrmjnyniwwldliezwbjuyvqdvrsshmawquexqoybglkeuvifqtezy', 'yv'), [38])

    def test_case_857(self):
        self.assertEqual(pattern_match('wrqrbrlfcuqlvq', 'q'), [2, 10, 13])

    def test_case_858(self):
        self.assertEqual(pattern_match('jjtsktqeoieabqstbumddtklwzjknlyyqzsvhumgnygffesxkqckwljqrjrbcypa', 'tsk'), [2])

    def test_case_859(self):
        self.assertEqual(pattern_match('olpdhfcxjinomaeunwqbeotzeyuvasqfgtgcezrvewytncwlfhlqtuotywaehywovlsqruzrcpopmnsyoazibnjzgr', 'vewytn'), [39])

    def test_case_860(self):
        self.assertEqual(pattern_match('ckvicdfixfjqsiekshdpalvdfdsyajtoahpteosbuq', 'to'), [30])

    def test_case_861(self):
        self.assertEqual(pattern_match('wvipbxfzuyvzxzeeqfyybwsrubdzpieqhbuhfxlsvfjkzfvjttfgquntv', 'xzeeqfyybw'), [12])

    def test_case_862(self):
        self.assertEqual(pattern_match('osnkwvkcegirmlpjbknhhwptbnvzpwqxbranhwpg', 'knhh'), [17])

    def test_case_863(self):
        self.assertEqual(pattern_match('kmqtsaptbjfupkbesijyagacplydxgrmwfbubjnbsrkflsrapwyjtpxfykvfcn', 'qtsaptbj'), [2])

    def test_case_864(self):
        self.assertEqual(pattern_match('jsuvxqxxzjvsdzfhudqaixxiwmexnkczpjavqpihpdzztchcudofxawnimmaqfqqghazzzkinmz', 'uvx'), [2])

    def test_case_865(self):
        self.assertEqual(pattern_match('gpfnpjwndsfhxojmrtfxcfw', 'j'), [5, 14])

    def test_case_866(self):
        self.assertEqual(pattern_match('tfybfaisfnwzoaikkjxponrwyaiqjskmhtgesdubnhjmxpvsggscncchpvtixlhhgxcl', 'aikkjxpon'), [13])

    def test_case_867(self):
        self.assertEqual(pattern_match('wcpuwnlzfjwpvorlekwxpoesyaspsnehmnwwlffrsgbisvimnnrvgahqozrfjispajstoegveyiuitpoduspik', 'yiuitpodus'), [73])

    def test_case_868(self):
        self.assertEqual(pattern_match('wtptyyslvmvjwupfwtwqbkq', 'ptyys'), [2])

    def test_case_869(self):
        self.assertEqual(pattern_match('jxcjinrxqbyaoaqwwegkekopwguopvpyvpfyoxawvxzxuwavxphhwaojsvxnlrusd', 'yvp'), [31])

    def test_case_870(self):
        self.assertEqual(pattern_match('mzfbvkcjqwzlvwdxpomevvilstjuvcihixsjwviviqvajfukftxfxlqwdjkrkbbkltwrwfmgyuazhtjcjrxdkryly', 'iviq'), [38])

    def test_case_871(self):
        self.assertEqual(pattern_match('wmvuqrlwdnpifmfvyyimfbryvteauotrkjwteisgaeml', 'uqrlw'), [3])

    def test_case_872(self):
        self.assertEqual(pattern_match('zmtyxdlxwbzrcopjllsrbegbgvkfqvnzimaysunhwhvwdtyievylphnlnuemk', 'lphn'), [51])

    def test_case_873(self):
        self.assertEqual(pattern_match('cloypzccgltsubojtesaltbwbhbkuzgbosuugshepgzxvgjqyswdntgizfejaqsqkqbjyvfjjvobjzi', 'ypzc'), [3])

    def test_case_874(self):
        self.assertEqual(pattern_match('cofvlxlxrrspzwkuach', 'spzwkuach'), [10])

    def test_case_875(self):
        self.assertEqual(pattern_match('ekhuuafojycfkldfjhnqsiqqvtbjxdeoncuofrmwhxxeb', 'ycfkldfjhn'), [9])

    def test_case_876(self):
        self.assertEqual(pattern_match('mzlspjyryrcbkdywgsmaywgetdvzvtmnbpudbheaymcxtibssndsbjvicamevmjtcgdsl', 'bheaym'), [36])

    def test_case_877(self):
        self.assertEqual(pattern_match('nawkismomkirucfrkgixqovzcvzcdpiaayjhewkimxmvihuflomjlxygkfibcybheylegctnnjldstusbiigkagntbca', 'xqovzcv'), [19])

    def test_case_878(self):
        self.assertEqual(pattern_match('thtyevmpwwtcebndpbftbqrttdyvdobkcyijfesefnsaqqaifoeosckfobscpaib', 'b'), [13, 17, 20, 30, 57, 63])

    def test_case_879(self):
        self.assertEqual(pattern_match('ggfvevsifwsiiwtgtqxbobnrztmkncqaodfopjaggebe', 'qa'), [30])

    def test_case_880(self):
        self.assertEqual(pattern_match('ygmlspncwylwhbouolezspqgkzexhujeogot', 'qgkzexhuj'), [22])

    def test_case_881(self):
        self.assertEqual(pattern_match('ygrwpwqykqlsmobelzrykcucrajslmcvunrdsicwdvhkzzpbckashzebvqcllifbrtjgdthqutotvhkxmysm', 'vunrds'), [31])

    def test_case_882(self):
        self.assertEqual(pattern_match('yrmmofwjrngvqaceaoowvb', 'jrng'), [7])

    def test_case_883(self):
        self.assertEqual(pattern_match('wcbbncmbchejugqsmyabwoaichlyzho', 'wo'), [20])

    def test_case_884(self):
        self.assertEqual(pattern_match('vdrhxaoushezjxbzqdylnpulzwqhsznbbyulnzenktpfbdtgkcs', 'gkcs'), [47])

    def test_case_885(self):
        self.assertEqual(pattern_match('tcdrwrcxnfimjkggosnslayv', 'drw'), [2])

    def test_case_886(self):
        self.assertEqual(pattern_match('uzbvciqinooxoapukykmpxxhuzjffjmvwexgtknfjvcxzueqwbpeirhoxsdizpjio', 'km'), [18])

    def test_case_887(self):
        self.assertEqual(pattern_match('mgoagtqsotnpamfitnsieznnsoqmgtlfwecbinhyfllsyvjpwwakhfegblumsmjrfuldqwglantqwiqmgrvntrhmxvouimdbehjt', 'mgrv'), [79])

    def test_case_888(self):
        self.assertEqual(pattern_match('rxuxuiufjwfgbfogvdksvydfxxfubgybghpnpdiqqlnljwieniqml', 'wfgb'), [9])

    def test_case_889(self):
        self.assertEqual(pattern_match('tgxbhmltcwpxsellyqzpjsdjfgav', 'xbhmltcwpx'), [2])

    def test_case_890(self):
        self.assertEqual(pattern_match('qatpjomrkqookrddemoxvmygehykssmrgrzzkkaztmsxqomtwtibrwnaqhtteqczqgdlbmbwywxdazauncodylhf', 'qookrd'), [9])

    def test_case_891(self):
        self.assertEqual(pattern_match('ynmrhcrmcjhmz', 'ynmrhcrmcj'), [0])

    def test_case_892(self):
        self.assertEqual(pattern_match('pnrvfkcrlqebkodkgviysgmbsfrodkqwcmqzqpyledmshbhccildwayvrrnfsyqpzopcpnifqtqoqnzfmqxrycutk', 'iys'), [18])

    def test_case_893(self):
        self.assertEqual(pattern_match('vftngiihbdougkqvigfrboaaelsyeieybjwbvbjmsvkdvbpzswmlwjggaupvavty', 'msvkdvbp'), [39])

    def test_case_894(self):
        self.assertEqual(pattern_match('otnrgnjchxzowcsnnpqptzcmphsziilylyalbzzslcojbkzzdplrqsktlsekydkplsshnziafxycvkswstwruaxnqhd', 'ily'), [29])

    def test_case_895(self):
        self.assertEqual(pattern_match('jkndnlvpsfyqlzrkvhedxcsiqhylvdfcvmcswdagmenbfp', 'v'), [6, 16, 28, 32])

    def test_case_896(self):
        self.assertEqual(pattern_match('magpaotsabwqaqqcauznulcaymnpvdafwrvryhvfakymtgqpjfvcblbhnmqyctjoaqzaldemeqjhfnyggiw', 'yhvfaky'), [36])

    def test_case_897(self):
        self.assertEqual(pattern_match('uflsdlzmpypduxjujvofjmpxqlaspyzppoikzrnlniatdapsmw', 'sdlz'), [3])

    def test_case_898(self):
        self.assertEqual(pattern_match('sxdoxnkiesxehwsncdvkbeyhoprsay', 'ay'), [28])

    def test_case_899(self):
        self.assertEqual(pattern_match('xmbitmmkfafmbazarz', 'mbit'), [1])

    def test_case_900(self):
        self.assertEqual(pattern_match('mymhqfudfmbjopfomtjbjiatxtyrevgaweuwkddsibjwyvbcpeukvcqbhixfzhpmmwlmhscuwybvq', 'hi'), [56])

    def test_case_901(self):
        self.assertEqual(pattern_match('vkztdplzyntbljyyutujkr', 'tujk'), [17])

    def test_case_902(self):
        self.assertEqual(pattern_match('vfvehfeepkaeafevkbbtbgjnuhuwnwkegdglbjpxkzeunhzyqrhy', 'gdgl'), [32])

    def test_case_903(self):
        self.assertEqual(pattern_match('uljbnfueexnlzzhiddqblicpgiwfladgqxnqfcarbjugmtjthlfroqxdssnmgdjdehctgeptxbikjynbdjvazdltcrlgs', 'yn'), [77])

    def test_case_904(self):
        self.assertEqual(pattern_match('mfzzivzawscvbydtwtbietyacdfqrxupscydyqgwelxnqhpoflbjacthmnryqcpigoysqjvbuf', 'mnryqcpig'), [56])

    def test_case_905(self):
        self.assertEqual(pattern_match('ukzyiysjeiyklafb', 'je'), [7])

    def test_case_906(self):
        self.assertEqual(pattern_match('cnzsiyucgftlohqexaskwvdnzwbwuygyjffsaqtjypitwcspytodrhbcwmoriclpaonqhkfhjkqxsypxyruzjclcl', 'itwc'), [42])

    def test_case_907(self):
        self.assertEqual(pattern_match('ksgcpulljtpcickzjiqmgytz', 'u'), [5])

    def test_case_908(self):
        self.assertEqual(pattern_match('qddhrcmflmp', 'qddhrcmflm'), [0])

    def test_case_909(self):
        self.assertEqual(pattern_match('hsphlhielcahz', 'hie'), [5])

    def test_case_910(self):
        self.assertEqual(pattern_match('achfbctnoqmakmcczpgli', 'fbctno'), [3])

    def test_case_911(self):
        self.assertEqual(pattern_match('aecdljqgujwssqnmecgfwsahtgcpuhqgyqobzrmibpwxvgxqbrswntrzvvatpjmxvshrbtktlrxkvralxadauuup', 'bzrmi'), [35])

    def test_case_912(self):
        self.assertEqual(pattern_match('esukcaequawvbtidfwtvxvgjhuvxawlxcd', 'bti'), [12])

    def test_case_913(self):
        self.assertEqual(pattern_match('rsgxzjtqjybpxgdkpuzutavzrkeedcsnfwzfigbcsdlpfhlw', 'gxzjt'), [2])

    def test_case_914(self):
        self.assertEqual(pattern_match('yfoyvsougbcqqqwszieowftcakewdqhoespsxgzpstjzkfyidzomwymswahtjuurrnrbp', 'rrnrbp'), [63])

    def test_case_915(self):
        self.assertEqual(pattern_match('bktrvhlbizesxltlcckxgvhmfllepdplrawka', 'zesxlt'), [9])

    def test_case_916(self):
        self.assertEqual(pattern_match('vdgavloqaggkmcnszqlmscnobxqbwoseyyndfqnehgmzpwtztzxwuhcgeddzsz', 'dfqnehgm'), [35])

    def test_case_917(self):
        self.assertEqual(pattern_match('xicdoeuozfebsbqsyjttbrervabguqqpkclafskhiqnlbyykekpyuixotyvpelgjvmu', 'vabguqqpkc'), [24])

    def test_case_918(self):
        self.assertEqual(pattern_match('mrvdwkmhbhytayfbrvipzfngvskpzscbhkbfqnrtvrtctscmeshxadpfuhctjppqznddzolqpzqphgiprainktmbi', 'ipzfngvskp'), [18])

    def test_case_919(self):
        self.assertEqual(pattern_match('agzydifjsdgbemnfyktifgaovjkvvhlocplodfvrrhbaumrkqclujplqpdyvncuabtwemnopwcljqaqbbzcvntrsllmadllr', 'nopwcljqaq'), [69])

    def test_case_920(self):
        self.assertEqual(pattern_match('amvhktlvrsaitxmncyrftbiigvadpedluiojyaxchnzxgjksqxeahklgfziwcul', 'l'), [6, 31, 54, 62])

    def test_case_921(self):
        self.assertEqual(pattern_match('xkdfycxinlujfiicuezh', 'fy'), [3])

    def test_case_922(self):
        self.assertEqual(pattern_match('acdsksqacssqpfofvsndxfhgplhimvncznnuirgjbzaxjxauhsbgdcgqjczpghme', 'auhsbgdcgq'), [46])

    def test_case_923(self):
        self.assertEqual(pattern_match('dgvgzuhrzedardpetcgngcdtluvhxqisqmxhjqeuwfxgptdlhvyjhlryeulkuwyrdjwjpppbwajesgkvz', 'petcgngcd'), [14])

    def test_case_924(self):
        self.assertEqual(pattern_match('ujrvyyecrukqviqslxhgddphberhjrvuljteznvlinuvstjlxctrrhnqehylwqwykqoarrdcrv', 'hberhjrv'), [23])

    def test_case_925(self):
        self.assertEqual(pattern_match('dooqdyjzuidqwdzopvs', 'ui'), [8])

    def test_case_926(self):
        self.assertEqual(pattern_match('hgwefbtimaxdyopuuuyhblayucpyzwnt', 'wefbtim'), [2])

    def test_case_927(self):
        self.assertEqual(pattern_match('esafsburexgzccusekdjrizntiwmizpjkwsxbhuqbfezhvjpmuwlcpcvwhoz', 'uqbfe'), [38])

    def test_case_928(self):
        self.assertEqual(pattern_match('gfggtmjvyjisltepugcjgnwtspzehjkvu', 'tspzehjkvu'), [23])

    def test_case_929(self):
        self.assertEqual(pattern_match('hhuoxlcvfsvwlrdioucvyd', 'rdio'), [13])

    def test_case_930(self):
        self.assertEqual(pattern_match('kuvdyfcgszmqqfwrljqgizyjrsrosavezghadtccjdaoxmzkgbfxjsqxhwytuqndelfediucp', 'xh'), [55])

    def test_case_931(self):
        self.assertEqual(pattern_match('yfkrzaekxkkerrhcbntlnqj', 'kkerrhcbnt'), [9])

    def test_case_932(self):
        self.assertEqual(pattern_match('gcbigvdtpklowwkdpzboszrzirfkluxisceacxlpsctcmcgislokkehvwtfagad', 'cg'), [45])

    def test_case_933(self):
        self.assertEqual(pattern_match('soapcycsboqhsaktnvennizjsxhzojrgwgvrwzb', 'nve'), [16])

    def test_case_934(self):
        self.assertEqual(pattern_match('ynhqiyjrhrgsrbmzsqcamlqmkzbnov', 'mzsqcamlq'), [14])

    def test_case_935(self):
        self.assertEqual(pattern_match('xzltnnnvbvwdxqrjupcutiurbeiahmeqaobnfszvjukahymfnd', 'wdxqrjup'), [10])

    def test_case_936(self):
        self.assertEqual(pattern_match('nszlcvcnvudc', 'nszl'), [0])

    def test_case_937(self):
        self.assertEqual(pattern_match('vguycqimelsyqdobmhszoucrreomjqhyqhvgvnhpqsu', 'melsyqdobm'), [7])

    def test_case_938(self):
        self.assertEqual(pattern_match('xwszxxjpspscaaealefmzvecl', 'psp'), [7])

    def test_case_939(self):
        self.assertEqual(pattern_match('rjrqkktyzcmnqvxrqpsumcjopj', 'qvxrqps'), [12])

    def test_case_940(self):
        self.assertEqual(pattern_match('qiqynbyizdiqwdromwmskxsnjlnqufuzefaqlclnreosbbmqxfbuzvqjtlffqoynr', 'omwmskxsn'), [15])

    def test_case_941(self):
        self.assertEqual(pattern_match('csspngpouemetuxudbymwkbkcpjsdvnpehyekxnqoomgwbwabfikshdfjwqtmdvmq', 'xnqoomgw'), [37])

    def test_case_942(self):
        self.assertEqual(pattern_match('ahfvvodhvdukgdesbxzvnwxortglct', 'hvdukgdesb'), [7])

    def test_case_943(self):
        self.assertEqual(pattern_match('lupyujpfbcvqgagnpdgzswxwjn', 'ujpfbcvq'), [4])

    def test_case_944(self):
        self.assertEqual(pattern_match('aoanfbipbaxcdmybwwfjexlzyghqjpnpsgikna', 'aoanfbi'), [0])

    def test_case_945(self):
        self.assertEqual(pattern_match('xcfyztbfwhfdxjlagqrinrbiimrwemwlwxpbmubupkptphdflquwskpqfkqwdxlmtxba', 'g'), [16])

    def test_case_946(self):
        self.assertEqual(pattern_match('hipmquxzlslfmtxyokjlamkjklssdekokeeyfbvfazkigofjoikfmndtc', 'kls'), [24])

    def test_case_947(self):
        self.assertEqual(pattern_match('nyjczjsvaajocgkjohadooojxnyywtexiehzyxuguuyxjrebcqzblqoy', 'x'), [24, 31, 37, 43])

    def test_case_948(self):
        self.assertEqual(pattern_match('jgqicjosfycsysiqgrjzyxuixeznwkgmrdgzztvon', 'mrd'), [31])

    def test_case_949(self):
        self.assertEqual(pattern_match('ujehbuycfhfaxodcblbfpupyuomvqaffrpcftrrghjrjvairteqfcch', 'ycfh'), [6])

    def test_case_950(self):
        self.assertEqual(pattern_match('krulbfawphfrtavetvky', 'tavetv'), [12])

    def test_case_951(self):
        self.assertEqual(pattern_match('nlvwgmhuhshplgkhprzclceoscdqtbwnlqmwkakejpbljbsipqhqxefptokypcqamw', 'ejp'), [39])

    def test_case_952(self):
        self.assertEqual(pattern_match('udwkqabemqbc', 'dwkqabemq'), [1])

    def test_case_953(self):
        self.assertEqual(pattern_match('kwxhbwjiwjbtzsgxhxgliytqxoguijzwblmtevrtqkhydnsrjidsuotizdngzzqmwljegfrgspumhm', 'ytqxoguij'), [21])

    def test_case_954(self):
        self.assertEqual(pattern_match('blargxxqlabdrhqsotwmiysibstgdzsudafyldglnxmzecymgnsbbzwxfbntwlkvt', 'ysibstg'), [21])

    def test_case_955(self):
        self.assertEqual(pattern_match('knbjhcktqhuxoizgckmkt', 'cktq'), [5])

    def test_case_956(self):
        self.assertEqual(pattern_match('naslnocpzdtdbzjdihqlijeepyypxbmpyvpmrey', 'zjdihql'), [13])

    def test_case_957(self):
        self.assertEqual(pattern_match('mydfrkuqpcoibvhoutyxwwkdmzxjlvsptofpudqibyishzsqbtmlrxiksvxzflxenjwuaufvlwxfqciivncenysrret', 'bvhoutyxww'), [12])

    def test_case_958(self):
        self.assertEqual(pattern_match('qayxpnqxoiuflamvdczuivxfkvmntalrsewrdtehvhijwaccsojejeuezyqojokedn', 'o'), [8, 49, 59, 61])

    def test_case_959(self):
        self.assertEqual(pattern_match('oqxzmmqzrqosqfffxgjinbgncquxglorvaravderrtjbdnokbmltlyzimyxkmvs', 'qux'), [25])

    def test_case_960(self):
        self.assertEqual(pattern_match('wwzcdfcrdblxmtgdxwfrwbihmydnlvukmwxacxwdklmdrxs', 'kmw'), [31])

    def test_case_961(self):
        self.assertEqual(pattern_match('lyenkybhteaqmyhjnjkvthuzwnlcjdrfj', 'jnjkvt'), [15])

    def test_case_962(self):
        self.assertEqual(pattern_match('yufdalfvsliomvvqeovgjhoynbqsaitiq', 'eovgjho'), [16])

    def test_case_963(self):
        self.assertEqual(pattern_match('zfeicniadjshekjahqeetzcdefvyignhsxntfptjcpqkohfjxkrgpqbiecfxwb', 'ntfpt'), [34])

    def test_case_964(self):
        self.assertEqual(pattern_match('cvlomjdwrfuqpvrxaburzliemexvmxrvevtozrdlcjyozmmbmrlhwqgmemydmwcpoimhutjetbfncqk', 'd'), [6, 38, 59])

    def test_case_965(self):
        self.assertEqual(pattern_match('dpsbgfixmlhogqxnejtjxwuejachughlupzinlntboktqvevntzksawflbrwtpnnvtivxqrmkxvk', 'flbrwtpnnv'), [55])

    def test_case_966(self):
        self.assertEqual(pattern_match('kfgtktbhnddsdhudbhqlmpyrnxttgjphypzkhqvbxquwayozrrgdckkbhwe', 'ddsdhud'), [9])

    def test_case_967(self):
        self.assertEqual(pattern_match('rjjkfejbokbkocnnxzetfouggppmjqgrtlybqshgbhiqpzgdzxeeurrcd', 'nxzetfo'), [15])

    def test_case_968(self):
        self.assertEqual(pattern_match('dmtqypwwidtiwstfympafwzdpzlvjxryznaviekxpfdircjahgrtujyrxvnxrzx', 'widtiw'), [7])

    def test_case_969(self):
        self.assertEqual(pattern_match('cvumcsamambwhkcnjulguzdutceodezmrtdddnefopovozoxpumxrttgmdrdtomgezumudueijcfudzaoclmvrcno', 'njulguz'), [15])

    def test_case_970(self):
        self.assertEqual(pattern_match('xzvqxtenacawhbaknrcwhe', 'nacaw'), [7])

    def test_case_971(self):
        self.assertEqual(pattern_match('xgbpqbfzhtfyipmxgkfdpoxdgxurauuwjrgxqkmjrbzaropsifwlzdicnehmolxsbmtciudeepj', 'pj'), [73])

    def test_case_972(self):
        self.assertEqual(pattern_match('erkweboutlprmiplzqwou', 'tl'), [8])

    def test_case_973(self):
        self.assertEqual(pattern_match('kyvonxhmaguboufyjppkadbfrkkv', 'ppkadbfrkk'), [17])

    def test_case_974(self):
        self.assertEqual(pattern_match('tvtfaemywptfsxjsprqqiqxmjfpcxdjuijggslumeeanqpqztcyordemyhbfsuajmotavcrnozwhlgfbeatfmqvqcnbxula', 'a'), [4, 42, 62, 67, 81, 94])

    def test_case_975(self):
        self.assertEqual(pattern_match('qnlxihqdxcbayrlrdugcnioypmvkbxoqcbtcogiksasqxcztugmlkdpvbzqckrjsgmsrsjztoidpjeedbcrayih', 'l'), [2, 14, 51])

    def test_case_976(self):
        self.assertEqual(pattern_match('hiqfexfkprzyxeemtickqrfxfmigdsfmfukdezxncssrrqbyrvnvjsguihthgtkghkfeibntbzkcmqvxzuyegcqtnyuwgvwc', 'gtkg'), [60])

    def test_case_977(self):
        self.assertEqual(pattern_match('qnwuwlzouxtupwmjzrs', 'wlzou'), [4])

    def test_case_978(self):
        self.assertEqual(pattern_match('vwdguprszfvsqzimxtfxrcaalsisfhlnysljijbdjbeltmx', 'hlny'), [29])

    def test_case_979(self):
        self.assertEqual(pattern_match('pwjpbfsjasvkjafurcenpiohqkthbil', 'f'), [5, 14])

    def test_case_980(self):
        self.assertEqual(pattern_match('qynsmdlkojz', 'nsmd'), [2])

    def test_case_981(self):
        self.assertEqual(pattern_match('xxegfuifsklxnrvmovhtt', 'lxnrvmovht'), [10])

    def test_case_982(self):
        self.assertEqual(pattern_match('epeurjreglwqkgxmrgguavlpdcluurpsrdrozfqkmgtqdgdxpdixwrggfxkdukkhbmznarrrbieagmqpc', 'arrrbiea'), [68])

    def test_case_983(self):
        self.assertEqual(pattern_match('bbsfctvhygzbiieuwittqlxrtcstmzxrwlgrtqtdvmormexaadzrdtgvcprqinrklbe', 'rm'), [43])

    def test_case_984(self):
        self.assertEqual(pattern_match('wsclobuyyjbiyzz', 'yyjbiyzz'), [7])

    def test_case_985(self):
        self.assertEqual(pattern_match('gmyfdhsxvppbggvwjvewsriylautmvvugloubgktojecqsmiwnvzsvqqw', 'mvvugloub'), [28])

    def test_case_986(self):
        self.assertEqual(pattern_match('nuzldufnmhlvlqmewoidivrcgfpympobakraisuebupamuloqnpcwjexqksppmbxbncxnoadrhhftgsodofzi', 'idiv'), [18])

    def test_case_987(self):
        self.assertEqual(pattern_match('ieqdcqlfunazptecfjqezkowzudmroojsxuqlmks', 'funa'), [7])

    def test_case_988(self):
        self.assertEqual(pattern_match('pydteuwncyjkaexrrdfaylokljvrz', 'kaexrrdfay'), [11])

    def test_case_989(self):
        self.assertEqual(pattern_match('berzsxfibllbhslrcrjntmbtkextxqxaiux', 'a'), [31])

    def test_case_990(self):
        self.assertEqual(pattern_match('mxoifliagqaajnjv', 'liagqaa'), [5])

    def test_case_991(self):
        self.assertEqual(pattern_match('axcqsegmcvsxivtoabwdxupqg', 'xivto'), [11])

    def test_case_992(self):
        self.assertEqual(pattern_match('clkpyasipshzxejxhgmkmujyetghgcstxpwffvujjifdbodnfphapynbft', 'ujji'), [38])

    def test_case_993(self):
        self.assertEqual(pattern_match('stjezwdafzaqgzotyleqbuachspdoibfphahdmyvywsscdaprdeawksjzpgnxgcfsofpiseaaqhlemddhveq', 'nxgcfsofpi'), [59])

    def test_case_994(self):
        self.assertEqual(pattern_match('gtofebgajfymdu', 'bgajfym'), [5])

    def test_case_995(self):
        self.assertEqual(pattern_match('ttdgnbvptq', 'ttdgnbvptq'), [0])

    def test_case_996(self):
        self.assertEqual(pattern_match('fjixwqkkdqjheqyajacdevksppysebreovwoiolsuiuuejshflkggjunyfvyzlmzkbnqznq', 'woiolsuiuu'), [34])

    def test_case_997(self):
        self.assertEqual(pattern_match('tzkpnuutuegwvcyguzjulqqdcvzktyhdjyszzbolbmbmwctxlwgbggcvjqrpszepjsvjqgdwbqckhfgihuhgqdbgvzt', 'jsvj'), [64])

    def test_case_998(self):
        self.assertEqual(pattern_match('uewdaikevbukvfdykacbkoodzokbynogdkmsgkthlfdrirnkfdbjptmgemghiwlhlrxa', 'oo'), [21])

    def test_case_999(self):
        self.assertEqual(pattern_match('thfxrrrnwaavxxjiivseejyoqzzrmikxsmz', 'eejy'), [19])


if __name__ == '__main__':
    unittest.main()
