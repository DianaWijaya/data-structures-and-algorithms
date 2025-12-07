import unittest
from suffix_tree_matching import SuffixTree

def pattern_match(text, pattern):
    tree = SuffixTree(text)
    return tree.search_exact(pattern)

class TestASCIICtrlHeavyMixed(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(pattern_match('gKawfq.3tB9F|=p\x0c%H-kqu\x0cf\x0cy)Yh)\x0cpDS7u"PJ\x0c\x08:kjN+,r!\x0b\x0c;Q-aU\t:{mK-e4x~[\r\x0ci\x0cl[A)%[kprRf(:iZp\x0b\x0b2e\'@-A:{2R\x08J\r\n\n\x08[\ntx{a<', 'Q-'), [52])
    def test_case_1(self):
        self.assertEqual(pattern_match('\x0c)#\x08Xw\x0b%\tNdJ|\t)\x0cf\x0ckfg~\r9blt\x0bq!\x08F\x08B1t\x0bVV\tfj8vVmI\x0c\\4C\t1h<%4\\(#A[3\n(0W[*\x08\rUKx5Znov\r\x08g5js|!a\x0c-\t3\x089;C]{}9<\x0b@Tg\n:.{gh!\\1!', '\tNd'), [8])
    def test_case_2(self):
        self.assertEqual(pattern_match('`b\x08+u\x08LJ5"wx\x0bhI=kk\x0cbd9,)5XP`,-\n!7{cK\n9\x08o6d+>hqo=JSJ\n{JZ.X\x08Y]?#sp\x08V\x0bSV\x0b+l\x0cQLT9.&\t1\x0b-ue(p3\x08Y[R>c/G\t\x08k', 'SJ'), [49])
    def test_case_3(self):
        self.assertEqual(pattern_match('%p6\rC>J;[\t\x0b1x\x0cAgFiZM2tww0a-Q\t\tWx\x08,\n/F2}fD_+\x0c\t\x08\nrzC\x0c/6N\x0c52lo\naH@b\nSACZ\n!Bdp"4m;<\' NIh\t@5S~Hv\t\x08:d{3\x0cuOy^\x08C\x0c334L<VZ5[\nLU~', '/F2}fD'), [35])
    def test_case_4(self):
        self.assertEqual(pattern_match('+\n[=oc!W7/}\x08\rMz"h-!f0woJf\x08\t\x0cHK7thq\r\x0clh;l|R[\x08+DfHI=0be~W\nZ0\x08Q7fy!\x08\x0b9\x0c\x0b\x0b#dN\'vj\r<+H:@)2KNl', '7/}'), [8])
    def test_case_5(self):
        self.assertEqual(pattern_match('M\x08FZ"/rO\x0cf<39\\V%g\twb&PO\x0c>`\x087BM,,|Z-%E\r\nY\r|\rnw[>O\x08PFeo\x0bf\n\x0b\r;j@</iBNhUh\n6I5 +pCBE~\x0c\x0b\'*\td7\x08W\x0cl1N2Tb@\x0bj^', '</'), [61])
    def test_case_6(self):
        self.assertEqual(pattern_match('\t~&\x0c}\rBn"`"EP\x08wXe\n[>6,\'2%U`a-6/\\;*\n7hmU{L\x0c\r#_8No\nz9\tJ\r\nSA6B+dg\x08%6y{[YY\t\nYk:Yt\x08\x08\\O8N\nk`\tcfzwTNKW\'\r>7g%Z\x0bB`V}\x0b@wV', '"`'), [8])
    def test_case_7(self):
        self.assertEqual(pattern_match('S,2tm015mqout.~\x08\n*\nm\t#%x+V[?\x0c0t\n\x0b-hA!~h&\n9\x0c,Q\rw[0+\x0b\t\x0cj}\n9\x0c2?4CV\x0cI\x0c\r\tP``\x0bYgb6RR4\x0c6\x0cJ8 \x0b)g`4XqDt\x08?GArR\r', '8 '), [83])
    def test_case_8(self):
        self.assertEqual(pattern_match('\n\rv`\x0b@s7|XD8@Zg)>B"9V^\nOEx\n\n=X\\\x0by^n\x0cdG#L7\x08H\tB72zJO7*\rBD\x08\x0bB\r\x0cNbl5\\\r\r R[)wD\x0bD\n\x0c/<^th\x0c', 'y^n\x0cd'), [32])
    def test_case_9(self):
        self.assertEqual(pattern_match('KT`3\'oL*0^\x08fg.OO"j\\xa\r4_5y+UnF(Rlz\x0c\nXb%Ra>\\\n[{\x0b\t.MP)P<dTN?1M8Im)P!0IH}8\tF\x08w\'=\x0barB0\n!?V?}FcK\x0b\x0b\x0c(5E\x0c\x08o&\\d\nk^oJ6\x08li\x0cM7\n', 'lz'), [32])
    def test_case_10(self):
        self.assertEqual(pattern_match(' ;\rz\r\x0bF:>;\na]\n\r"j\tcuOROlK\t_[c\r\t\'=*~QNEQ*0c\x08L\r4{r>+\r\r=\x08,gT08`@\n*D9\t\x08t9RW~Z\n]#XmLOE\x0ch\r{La0r\\>z)*u 1TrVK', 'a]\n'), [11])
    def test_case_11(self):
        self.assertEqual(pattern_match(';J!\x08\x0bQzZo(,v>O\tB0]hgCE\t\'\x0c^)Yf{Q<2Cb\tB\nB\x0cK\nph3\t)7r\r,a^F\rx9(!\x08!52S\n2X"V-rs\x08x,LzP\x08%O6d\x0b"Ya)\n/U\nk( \t)vx\x0bC+', '\x08x,'), [72])
    def test_case_12(self):
        self.assertEqual(pattern_match('H@1:Qj_\x08wuQUSU\x0c\x0chSaE=Lv26\x0cl\x0c<o4Q4!El/%kIm1\n\rj!=.U[3k2S)a\x08\x0bP)I\x0bw<lV.\x0br`60JbmZCyQ\t+5DgO9Us\rIHj7;D\x0c\nV\nS`~\x08YJ8A:\x08<<,', '!=.U[3'), [45])
    def test_case_13(self):
        self.assertEqual(pattern_match('_\nQ\x0c\x0bO.rpc8X/vih47D Mii"VC_\x0cmA\x0b\x0c47\x0b3\thubo?\\4*1}%\x0c\x0c-%6Nn)\riH[Dn1N:\'Jp\rbDN\x0b8fY>T[_\nf`t\x08:MH*-2\'iF\x0c\x0cn\x08vQ\x08>S3\\\x0b&2P\r15\nu\x08"6', 'vQ\x08'), [98])
    def test_case_14(self):
        self.assertEqual(pattern_match('1!r`OQB\\ \rz;oD:\x0b\x0bd\x08q;pa\x0c\x0b#\n\x0ct]\x0btf7\x0bK\nb7!Dl"Qu>*\t\x0b #N\t\nC\tI\\m1Y\\,-?wsh\rXd&4612osI1C`', 'd\x08'), [17])
    def test_case_15(self):
        self.assertEqual(pattern_match('\nGU=(\x0cYrXn(Eb\x0bq<DdW @S[mmy\rGaV*2;bV\\z|2\n QcyD:\x0b\x08\r!O;+kl+o@!@\x0cnat)[Z1\tYt2CI11B7sV\x0b\x08Q\nW35J\nniWQf\x0b0', '\nW35'), [83])
    def test_case_16(self):
        self.assertEqual(pattern_match('jE4vyMG\t\x08A\n\x0c]_1)E+!\rpUA\x0cq\x0cTza)\t\x0c5:7b\r!z8&Yp=E\r\x0c")b\x0b(%\x0b\x0c(cWr\njgyK\nQv},FDo\x0bR`v\t_naQ&xo/\tHzT2\temb^\x08U2)zUt\x0b6vg\nr\x08&#r87)h/)h', 'a)'), [28])
    def test_case_17(self):
        self.assertEqual(pattern_match("\teb^VoBJ' D?+U3-Ch12\x0c`\x0c9k5t@p*:\x0b:16;h\r??c=M_<=^y8F\x0c@Fwu\x08-\rjLb\x0c^`-\nBBo\x0c),L\x08!\x0bb\x0cW\r2", '_<'), [43])
    def test_case_18(self):
        self.assertEqual(pattern_match('(9\tP_7 m\t\n\n\r?\x08\tk%[\n)P`qt\x082h\r#y\\9F7\x0c7~u\tqA\x0bj)C`\x08\x0cYyA5Ykt\x0by2u%\x0c\x0cVR[_r@X;+aV"-)>N\'j8X4\x0b\x08*\x08\x0bEW ?MGK]PY\x0c<~c}\n\x0b!Ff7\n2L#%s3.`/', '+a'), [70])
    def test_case_19(self):
        self.assertEqual(pattern_match('id~h\r_.\x0b4>@>vzY^qPX\x0bc\x0c\x0bep}Y?%\x0cfHTs\t\x0bW8\nipwX\x0b2~;d5B*\x0cqN!P/\x0b>2w\te<=2I)s\x089xh8_jb\x0cRW\rNy\x087\x0bu\x0c', '\x0cfH'), [29])
    def test_case_20(self):
        self.assertEqual(pattern_match("~(|\x0cW\t.3\x08yo*%-lUdFFBdE/.u\rH@\x0b\tYWlL\r6dsA;T(w!\x0cCX\x08~\r}\x08L6(n\x0c90[g\x0cUm94a>\n+\nXOiy2VE/Q&/[F\nF43YX%Y\x081f'zB1b=jBI", '4a>\n'), [65])
    def test_case_21(self):
        self.assertEqual(pattern_match('\rD5]wq\t1K\x0cD,S?a;GvWya\'Mq@e"ltJN*6Sr6Otm:|n\x0b5qJ}Wi\rL8s:%\x0bq \x0bVH\x0c.SNV\x0cK"siR:::\t\nsJY', 'K"siR'), [67])
    def test_case_22(self):
        self.assertEqual(pattern_match('QV9VbMC~zyMXn2\x08Fo5\x0b11>Bw-\t\tsMxW`Y^U\x0bvzw0\tY}5cx1F\n\x08\t\t"6\x08\x0cypBp^\r\r7;v6&^jabfH+d\r4#\x0c\t^Eek\x0cUK/>m\x0b7G\\', '\x0cUK'), [85])
    def test_case_23(self):
        self.assertEqual(pattern_match("vH\x08Y.sZO\nyT p>g*k\r`p'o\n3++\x0b\x0b*wO86VNV\nK\naYG>g\x0cUn\nY?]Z0\nn2Ch=U1a8\x0b[[Re\tt+\x0bpItR?L&\x0cEU\x0c~g20\tosA8}Rn-t\x08,[5)\x0cz={p&#n_Y'O\t\t\r\tb\x0b", '0\to'), [86])
    def test_case_24(self):
        self.assertEqual(pattern_match('{l*!rxXr\n o\x0c.W"y\x0b"&\r\'\t\rP8Q.D8Jv ;BLttNH`OrI\x0c%q`woj^2r(dZ\n\rr~rjt\x08j&b\x08\x08ew,8Z/Jlg\x0b\x0co*8}c_*Fb\x0ccT-[N9\t"T9,EI\x0b1', 'dZ\n\r'), [54])
    def test_case_25(self):
        self.assertEqual(pattern_match("\r/9_osIUvA\x0b4P!_nz\tAG\n\r>S\r\x0b\n0 \x08#}yE\x08uRR&\\n6{v'x=G\r6ct\rJa#W2a8\t\\a]J@va%\x0c^Q6\t7dZhM5P3\r \x0cyd\x0c5nAYo33][mkm\x0c\x08\rot\tg(vd\n/\x0bLS:%i\nQ", 'AY'), [90])
    def test_case_26(self):
        self.assertEqual(pattern_match("\x0byk~MfE\\*W{\t?}c{8!\x080n=,\x0c\n\t\na5|\x0c\n\tSW>\nr2\x0c^x8\x0891\x0c7{7S}QqQB0\x0c\nu]35'wf", 'u]'), [59])
    def test_case_27(self):
        self.assertEqual(pattern_match('+kn\x0b@\x0b"\x0cz^5c\x0b\t\x0cY3H!K\nMe1a`U8noo\x08N\x0b\x08}pH\r!i\x08*Q\x08/\x0c@1q\x0b8w).(VBJ@\txpW}\tOE\t84"i?!\x08kox0"x{\r%#D\tJ^" iE\ti{H&\x0cwX#\t^Nr\x0b0', '%#D\t'), [84])
    def test_case_28(self):
        self.assertEqual(pattern_match('ViT\t|O7hA*z\x08\'v{\x08\r%\tq]\\n&GyeSmhOpj/?\x08\rvK"rA\x0b\x08B;f\r\\\nf`oT4YJ~c#u\n&\x0cv7\r~] gsM1u\x0c\r\x0c\x08!S3\x0b,7\x0c(', 'n&Gye'), [22])
    def test_case_29(self):
        self.assertEqual(pattern_match('[;lo0m2Iuc-a*:(IG9\n&\x0b@y %cITl\x0cv%\t\x0cg%tSF<edX?\tg\nXwVx)HwN{/x#yu0,\'"\x08(7}w\x088|=ZPw"Om+A\x089Jc.\nC\x0b\nH !\rLjM\x08J?8JF^\ni0`<', '*:(IG'), [12])
    def test_case_30(self):
        self.assertEqual(pattern_match('vW<>\x08g\x0bk\rFBFDc,\rQG\x08u{^F;QjPP%.+,AR\x08+7#>#\x0b\x0b\x0c\t"Y@e\x0c\t@}\rC\x0ce\x0b/\x0b@\t7\x0bM@#TY\t\x0cA\\39[+uF\x0b^pS+\r7T#y+\x0c#!!/\x0c.-;\x0bT<Oq@3cyw', '<Oq'), [100])
    def test_case_31(self):
        self.assertEqual(pattern_match("=(\x0b\x0c)\r0H7[/Ci.\r%w\x0b%J6\tEmF#\nP.'s{Qj:\n\x08i\x08%\x08.\x0cz|{\x08\ts;\n4hRt\n\x0b\x08\n\x08V\t~uQ\x0c", '.\r%w\x0b%'), [13])
    def test_case_32(self):
        self.assertEqual(pattern_match('55%e\taP\\S_P\r4`r]\tktoyu7\rnx\x0b7 \r[{|\'\n\t9il\nH\r?\x08(\rT\naweG"| <f?QLx\x0c\rvvO\x0c1\t/#?\x08)7A\x0biB=\n!\\\x0c\x08`\x0b', 'P\r4`'), [10])
    def test_case_33(self):
        self.assertEqual(pattern_match("IJv\x0be!0\r^f^JeO1y!,m\t:2\t6\x0b\x0bJib{D'jCcR\x0b\x0c\r[FNn\x0c*m8qnOXeqp[&u *{JpKGQJ1)sDwIqd-zP3\x0b\x0c0\x08@9y", '^JeO1y'), [10])
    def test_case_34(self):
        self.assertEqual(pattern_match("TnpDq\r>1rqc>\t\x0c[r7\n%cFH\t{\x0bygrce]f\tq1r\n\tZLf!Y\tZHF?;,:}Yl(\rVS?ep^I'\x0c>s\x0c^6F", '\rVS?e'), [55])
    def test_case_35(self):
        self.assertEqual(pattern_match("F&k\r)@`=R[,!OuPb_!TQ^3Ul(\x0b%'q0&\x0bU*>et[\x08Q\r>'P\x0c{Zd+6^\txS_B\n\x0b#nw3!Y2R%Nd/Sy\x08mg\x0b\x0c(re\nO\x0cdA\t\x0c", '\r)@`=R'), [3])
    def test_case_36(self):
        self.assertEqual(pattern_match('y\rj\x0bl!x\x0bOaT\x0c\x0bO:K~]Owm\x0bk(X51IoC2{~"Glx\x0c]^R"16P\nP\'Q7,_\x0bH82Z=\x0bEqJF.\ru/\x0bE\x0cVa\n2T`\x0czzt`.|0J\n\x0b*;\x08{V\n?r', 'qJF.'), [60])
    def test_case_37(self):
        self.assertEqual(pattern_match('\r_\x0c-SZ`J\x08jsL\n~`\t\nTy=j\x08\x08K]i][ed.4h\x08&\rNC\x08W\np"]:SkJ!Eg}\n\x0ch\x0cK"FE](_]dwm\x0cEk;[c\x0b xhFR\x0cD^\x0b+\\S', '!Eg}\n'), [48])
    def test_case_38(self):
        self.assertEqual(pattern_match("5MI!{.\r[>9e\ns\t0\x0bXb5![`:+\n3{MP\rl<0a[NG/\nr\nwoy\nw2;\x0c\x0bu\r{*Gow=.3('t\n\x0cRKG).NF}^zl\x08J,", '\nwoy\n'), [40])
    def test_case_39(self):
        self.assertEqual(pattern_match('fT]sA+\x08s#Eu7\x08R\x0c2\re/\x0cd6\x0b\r\r8okc-s\r]\'@N}U3E\x0bSC+\rTb\x0bU\n\rEok\r2c\r*bdWI_"xD!\'k-<^P5f\t', 'bd'), [59])
    def test_case_40(self):
        self.assertEqual(pattern_match('\t;D`RMl\rQ#_\n\trqdTZ\x0bENS85\t7kq}4!\x0c\x0b2^RHcto\x0cB:p?}@\r\n;Yj\x0cVn\n\tYW5\r', '`RMl'), [3])
    def test_case_41(self):
        self.assertEqual(pattern_match('L\x08\ne 4DO\x08"\rw|FW9Tx \x0bAe\n\n]m|sJ*}\\-J\nL"#\rr+EfJn&\x08x3^~I}f5\x08^bi\'w\x0c\x0b\x0cL9"%"Q\t\x08\x0b-c\r3uuK3?hW:gzU`umc\'/PAwNjW', '-c\r3u'), [73])
    def test_case_42(self):
        self.assertEqual(pattern_match("K]c!Z\x0c\x0c\r]'9S_5.7H\x0cn\tz#|{OA/pT+V|KBv>{g6%^u\x087|h}7LJk,v*M`\x082\x0czY\x08\n&VfU)!s^[Rab}\ryz\r`\t8!\n\tn\t|%!Y8_\x0b|vX4e\no\t5\x0c", '!Y8_\x0b'), [90])
    def test_case_43(self):
        self.assertEqual(pattern_match('\x0cLm-EIQWk>Ny,\n=\rU>3=.:jA\r\x0c\x0bY%/s(#&\r(\n6ZqxBRCwq(>~\x0c\x0c/gX:R]@D3H\t>zak\'?3":V\x08\\673\x0c!gyw}', 'D3H\t'), [58])
    def test_case_44(self):
        self.assertEqual(pattern_match("Uz`'r@w'@Tz.-1\x0bFQLgYw\x08\rGW2We\n\rH:\x0bT=sw>'\t^Ie1\rL!~N\n'\x0b [c7x~cwn<\tA?7\x08\x08\tX[\ry,*b\n|\n\x0c{gB/lb#\t,Q~\tc=UtA9DF]v%\ntgN\x0c)y\\E\n0E'\r", 'y,*b\n|'), [72])
    def test_case_45(self):
        self.assertEqual(pattern_match('^9Ep1%>aalO#]0dfB\x0b7\td"\x0b\n,6c*m\tI9ty 7\x08|Fp<l\x08A\x0bsS[Nm^o\x0b<}iJdAUm/hnI', 'm^'), [49])
    def test_case_46(self):
        self.assertEqual(pattern_match('fus\x0bs\r7\x0c\rx\rp\x08}KVfsy\tpMA*VEesxnzMO){evvl\x08\x0bKM\rA<\r{<ExQF\r\x08x06>=Y,bHndKs6\t~oo', '\x0bK'), [40])
    def test_case_47(self):
        self.assertEqual(pattern_match('\t\x0ba\n\nsQp(N],)1_Xd\x0b@\x0b}}\x0cQ2yZT19.\\i"\rbf\x0by\tC91=qje\x0bS\r\\\x0c!S\rY\x0b\n?5M][\x0c,3T<s\r\n\t"KT%3C5\x08J\r\x0buAj;\x0cij\x0bO}\t;l{\x08k\n(3<\r\x088oD', '\n\nsQ'), [3])
    def test_case_48(self):
        self.assertEqual(pattern_match("\x08y %./\rC' \\N+%5\rTN^\x0c\x08X\x086\rWN-xVd\x0b7D\x0c(sULLe2t\r\nv,\x08\r|hC.1&jDo[G\x0bfn]6\x08Kg", "' \\N+%"), [8])
    def test_case_49(self):
        self.assertEqual(pattern_match("L5*P\na\r\rf!Kx(+= Lp%@WuX\\r\ru?\x0cai3I'j\x0bL\x08J+|{r*w\ti \x0c}\x0cV/W9@O;\x08v%qJJ\x0b;\x08)?\x08.\x0bud\x0cw'F '00O(;h\tzM\x0bbcJ9oKq^`hvc@*ej\t\x08", 'WuX\\r\r'), [20])
    def test_case_50(self):
        self.assertEqual(pattern_match('iO[>:}jN`\nY\rs>w\x0cz\x0bb4\rH*G\x0c{N\\\\V\x0c5\nr| \nJQ.1uyS%bGKGd1wB\rz\x0bd)eI106T#\'b\nZ\x0bU]k\r\x0byH!\x0c?3P&\'^_\x08X"!q/\rc^~\nM\x0bg7u4/\t3=_oZ', '^~\n'), [94])
    def test_case_51(self):
        self.assertEqual(pattern_match('Rj\nNl?O}e-{;L \r\t-\rQ\r6s\'UyPQGh\ri3\\!05I\r+D&"!URWPA\x08]"4\x0b\nY\x08\x0b!K+ap5uP\n;pXA\n8\x0b\x0b\x0b{ak\x0bTQ!n=\x0c\nR;Cz\'6P\x08Lh\x082Dv\t\n', '!05I\r'), [33])
    def test_case_52(self):
        self.assertEqual(pattern_match('\r\t\x08B&!\x0b+e|NDsXGb\n\r&PjW^\x0b\x0b\r#8\x0cX[H(\te\x0b+4@Q9}`0^\x0bU\x0c&\r`[[r\'c9GH]ns\x0c6wD53Y\tSKbi\x0cV\\69!?"SG<cbNM<k\x08X\r\tMSoY4`q6=k\rA,J@w|@mw', '^\x0b\x0b\r#'), [22])
    def test_case_53(self):
        self.assertEqual(pattern_match('t\x0c\nVF?aw\x08+=1%z?*\t\x0cinEM@\x0c)fhq2/`>;*t64\x0c4 NPDb[/8kOA\x0bO";6\x0coU@a+#0]&RY&?q@bT5\rl"', '@bT5\r'), [70])
    def test_case_54(self):
        self.assertEqual(pattern_match('#>=?cWxqDzx8\x0bO^\n]GAfIk{y2Hy[VRJ\r8 oEC75F>Hd`\x0bZd*[T,{([w"QZS\r\r\r5\x0c?yOv>m-"]r:\n]:/w\t2#\r)a9%^0', '#\r'), [82])
    def test_case_55(self):
        self.assertEqual(pattern_match("\tU+v\nKj\x0c?RUQ .\x0cD.}+PLB\n\tC^\rzio{\t\nf3-N'EG(@kHe{k6EI,>\nik\r\x0c\r^V\t\\eth", '\nK'), [4])
    def test_case_56(self):
        self.assertEqual(pattern_match("D\n:&'r@\raa?P\r{L\n\rMkR1\t\r^8dt^[|`-Y&\t\x08\x08fr\x085]'\rxN:M`;\x08\n'F&S>'4\r`\nV:\r\x0c-4!sOU(\n\\wl", '1\t\r^8'), [20])
    def test_case_57(self):
        self.assertEqual(pattern_match('(\x0cd7)7\x08 \rxV|/j)kn-,=\tAKA#>.\\8f\x0c#wP\x0cc\x0cY\x0b]\r#u\x0cs\n*Tm\x0cj:aU>c\x0b\n#:\x0b0%}\x0b\x08E\x08\x0bFUW{\n', 'd7)7\x08 '), [2])
    def test_case_58(self):
        self.assertEqual(pattern_match('<1xN@4.l,\rV>\nn<f]qp%a&W(SHv%h.XS}G.L\x0b"L=<s~a\rF~\x0bA{E9\x0c0*v\x0b(3=N\x0csTq\nM.qT\x08\x0bhZJ\x08\x0bEUqJ+L_.{qj\x0bmbh\rZ+\x08@Wlj(b\x0c(', '.XS}G'), [29])
    def test_case_59(self):
        self.assertEqual(pattern_match('-8#!&}!\x0c!I\x0c\x0cj\x08pK\x0b\\dT%\nnK@H8@H+d\x0bo\x0b."5w\x0by.#4\x0c`?\rz\x0cO~rG\x0bS\nxZ qBaW\x08oX\t((Lun\'S;H3IHzZ\tLw\ta\x08`kcBp}9\x089\x08\\/rMo*%+).%V\n.K\nL#\x0c\x08\x0b\n\x08', '+).%'), [104])
    def test_case_60(self):
        self.assertEqual(pattern_match('\rP\x08k39Nz\r;fa\r,1S.FtV\t\n3viE_yo8@J\n\x0b\x0c \x0b1\n\x0b,"vr\rtN\nO\x08A}?|\x0ce#UO3<c\rKx', '1\n\x0b,"v'), [37])
    def test_case_61(self):
        self.assertEqual(pattern_match('\r\tR}\rjI\x0bv#!7fE,D6[\t_gWR\x0c\x0cg\x08i~\tk:PW\np\x0cG\x0b!7FWn>ys\\\x0c7XV\rHk\x08\x08|bR:ax\x0b4', '|bR'), [57])
    def test_case_62(self):
        self.assertEqual(pattern_match('%+N1"i@\r=gG\x0cCC\t\x08&Ni;OK!|2qw`i\x0cj\r\x0ba8Cn:_Uf&*1<F`W\n\rh\x0c\t\x0c=yr^fBc\n3.\x0b0S{0jWq:|uF3<Y@%c_1\x0b:|/*N-', '\x0b0S{0j'), [64])
    def test_case_63(self):
        self.assertEqual(pattern_match('-`H\rQw+A0C?\x08\nCR92/sc4\tp~W""/S7A_I;]\ra\x08(\t\'\r\t\rb\rH"\x0b)\\-\r|9~Lqao:\x0cW5uN0n%y"3/!\r.\x0bS`@C\\s+]aoZD|2Gc[i\x0bqQ\n7\\E', '\t\r'), [42])
    def test_case_64(self):
        self.assertEqual(pattern_match('M\x08\x08\n\rm>~>@R<n;vDs\x0c\n%A6:\n\rpN_\tK Nc>+\nH0\x0b1v(WI\r+B TACh:1t\t`\r\x08 ^e@]uA!LQ\r\x088pfzHN:<\t', 'I\r+B '), [43])
    def test_case_65(self):
        self.assertEqual(pattern_match("6<\x0bUNisi?\x0c0Ps+!\\\x0bO2x%foB\x0bAi\rc(9s;\t\t'\x0cf(\x0b\r/i8.Tv%.MCmhy)whA\rl[\t\x0b", '\\\x0bO2x%'), [15])
    def test_case_66(self):
        self.assertEqual(pattern_match("h;<\t;EdL5\x0cFLS'\x08I\\<C|ln&%\x080\n[YG\x08E17+Wh\x0b\x0b7\x0b7{>0\n&y\rB-,\x0b\n\rbD\rM\x08Fls2FFm\tD\r3{_\\\nW=\x0bC~f}|ai\r@", '7+Wh\x0b\x0b'), [33])
    def test_case_67(self):
        self.assertEqual(pattern_match('KD\x0b\x0b\x0b\x0b_S\r{poRuU\x0bY>ax)\x08Q1%\r/]\rsdWt\r\x08X&CJl^z2\x08||\\D8(bVs\x0cD.g&h/oR0', 'S\r{p'), [7])
    def test_case_68(self):
        self.assertEqual(pattern_match('./i\t9\r/=\x0bjeZ\x0bo\x0bERakhz:?sx.l`\tGU6e%\x08)3XP-q\x0c\x0c8W0n\r*%_\x0cVi:2F*5|S\rT(\x08\x0b:&B\x0cm[V!\nWvbgE\x0c\tst"wmj4>iFdzi\t!\x08\x0b\n', '/i\t'), [1])
    def test_case_69(self):
        self.assertEqual(pattern_match('[C,A\t}d#:?\n@I\tuOG}*\n)gK\x0bbD:\teh\x0cJ*W>LNU&3sEtioolQtUfP\tI3b \x08{%\x0b"dP?yT42enW5[0f\n\r\tISTDU:pPbQTo- 0;)#', '&3sEt'), [38])
    def test_case_70(self):
        self.assertEqual(pattern_match('\t! +L\\i\\\x08Xb?dl\tvE\x0b*,LYd}6\n?/c\r0n#Rk]\t=(U0fi-"}:(1<0kT"B\r;&\x08g\x08\x0b', 'i\\\x08Xb?'), [6])
    def test_case_71(self):
        self.assertEqual(pattern_match('QplZE7z\x0b\x08iVTux!\x0cFH1i\x0cK>W@\x0b<S;1\x0b>ZEM\x08"Z<SDrO\rj"\x0c\'i\nG\x08T\x0bx-OY\t7~<])H\r4giQQ\x0b\x0csXRFH~A', 'SDrO\r'), [39])
    def test_case_72(self):
        self.assertEqual(pattern_match('K\x0bM<u9uC|Jbn_6wICR\x0b!/>Y%UvVZ%\'\\K|JcCt>  U\r\x0b4=St5\x08H;a\rRc%\r\nlm\x0c\'2LXh9}^K\x085q[T60CGV\\mAW%kB#Y&C\t{rt>GPf0}AC{  \n4"m\x0cZ', '|J'), [8, 32])
    def test_case_73(self):
        self.assertEqual(pattern_match('4\x0c5\n\n`_~Yl\t_c0y0+=\x0bOXBUk-ic+\nhK.A#\t\txg\te-EA^#D\r/QkNa%:\t!Eu8\x0b?a*\x08+F(c:[,@c\'K@\nk6k!"6!1m!\x0c\t{;f\x0c', "'K@\nk6"), [73])
    def test_case_74(self):
        self.assertEqual(pattern_match('Vx%\x08X\x083mnE\r\x0b_t+v?joyP~-\x0b ]d^kqaY?VP>\x08,\x08+b\t6\\5<T%Wv\x0c =UQTrk~8\x08~;', '-\x0b ]d^'), [22])
    def test_case_75(self):
        self.assertEqual(pattern_match('23hM6yRL\\TjH/s0Jj#\rT1#\x0cwf2__ObqlGXtXL\rn\rAo\r\t>g3f}T#G\x0b)\rz|M\n\n[y\npdD\x08\tT|x\x0b><\x0c\x0b6', '\tT|x'), [67])
    def test_case_76(self):
        self.assertEqual(pattern_match("\ti<1z\r4\rPFzr1U'bNpNzwr[fBq@\n\x08.\x0c/Kin2k3G;L+\x0b\\Wu\x08SFl\x08?/~I~2}_\t\x0cr'A\x08l", 'Fl\x08?/'), [48])
    def test_case_77(self):
        self.assertEqual(pattern_match("H;\n!aw*r5.\t\x08jo\x08bROs`<li;%kwb\x0b-jy\t8b9)Dmc`bi\x0b\t*8g;FFi\x082?+0E<\x08CF}\t%b3\tinS5UcA+w_Nb\x0c\\ShaO\x0bLzajAV\x08\n\r'\x0c:wiWG&\x0cj-2", '<\x08CF'), [58])
    def test_case_78(self):
        self.assertEqual(pattern_match("Q@aeg9\tV\x0b\tpspz\x0c&L{&{<.rs#SrQ+e\x083J\x08\x0cQVP\r}.\rW\x0b\x0b0d\r\x0b&t'[+64F\x0b{\n,u,9#mrrldKPaP}t\n_\x08qab[\t1g[+`fr;\r'%u\n04\r>1OA{\r(", 't\n_\x08q'), [75])
    def test_case_79(self):
        self.assertEqual(pattern_match('J!k\n]%:\x0c\x08lK{tc\x0beE\x0b}P1[>3-z\ns0zR#\x084Vg\t;>\x0c`*\x0b\x08)\r*4tO 3d#\x08~\x0b&U9\x0ck}\n\x08oD>@l\nd\n9pvKGfs\x0c\n\x08N-1ny\x08t~Bs\x08\rV+x`Q\x0b\tA', '\x08N-1'), [82])
    def test_case_80(self):
        self.assertEqual(pattern_match("4U\x08uw04i&O'/1Oz\nmo\n\x0b1I!ug\r|qZtYGeE\tRP\x0b<({\\Hdo\x0b\r2(Is\t\tA}QmsX5\n\x0b<ihY`\x0c<J\x0b[\r<tyT94Ldf/\x0c\t\x0bW%\\\x0c*", 'U\x08'), [1])
    def test_case_81(self):
        self.assertEqual(pattern_match('\tn;\\h\n/\x08\x0b]\x0bz\rccdR=P"al"L"\nXMm0p\x08Dx|ApC9vkfyH!(`:~A8e9w9\td/D\na^AOi"(?f]\x0csC\x08Vc9:yFd\x0c&Y))Z\x0c\x08', 'p\x08D'), [30])
    def test_case_82(self):
        self.assertEqual(pattern_match('?{h\x0b;8h\x0bf4\nj`@\nKW`WV^n=7R\x0b+N+\x0b\x08=8M&XU8{Si\x0bg:Z\n8\r\r)JmPb\x08^Yv\n\x08~sm56a\x08\\H,E\x08z`M\x08\x0bI\x08\x0cH\r|--Q\x0bT\x0c*n\r_OD/3dG^ 8`aiI', '\r\r)Jm'), [47])
    def test_case_83(self):
        self.assertEqual(pattern_match("4\x0c\n@C}8\n(fzHL\x0b\\\r>\x0bz]ho\x0c%t W\tf?\r\tNPNUR\rB2jEVS};yom]\x0b_\t'8/<\nEMq|%,\x08\x0c#7R#c9}G\x08\x0b\x0bU0|%\x0c\n-\x0c\\H\r\n6\\]U\tdc+''I@1\r[<6", '\rB'), [37])
    def test_case_84(self):
        self.assertEqual(pattern_match('b=kYx/ktkK,V\x0b\tUP\tp\rf8aj_(.\x08STk2lI.L+g=6X1\rP\tiv\x08}\r\r*`X\nz"XLUytj\x08\x0cwy_,', 'ytj'), [59])
    def test_case_85(self):
        self.assertEqual(pattern_match('^`(6\r\nym7cqx#rR^[3`Pv8\n`^2:\x08n&06\njFe\tD>0\'a["LH|Nm\x08Q vQ{37F`lR\\jfv(\x0bB\x0b1hA5|\ta,XVH\nB\x0b_h\x0c\tZ# 2qA5F\\`A,+\t\r<', 'XVH\n'), [77])
    def test_case_86(self):
        self.assertEqual(pattern_match('n}L\x08ur\x0c9\r\rXDc>z*W-b-\x08\x0cFG?-#3"y\x0bqQk!F3 (2\x08\r6n}/=mh)mF(Q?;ni\r@TMMo= {A\x08|7t\x0b&=rA\n\x08Q\r\n\x0c3-8\x0cbU0\'\n\x0cU\x0bR\x08\x08ZY\x0c-/\x0bj.y', '(Q?;ni'), [52])
    def test_case_87(self):
        self.assertEqual(pattern_match("[}\\dxxh!\x0b(+N{8'{\x0c%_J>+I\t\tUhzlzfoy\x0c\x0c@d%\tYX!ET/y&Iw)\nX\nc]JxaX\t D=#[", 'lzfoy\x0c'), [28])
    def test_case_88(self):
        self.assertEqual(pattern_match('ie9y\t\r:+#]\tWj-~y\x0b*\x0cf^a%Ql!@Dx>\r*k]1LeZ%Qoj]K6\x0b\t\x08TvG3\r. gJ"\x08y>\x08\x0b3&|,6\x08ERyex657Jn2G\x0b\th\nn:T\\zI\nHs\x08>S\x08%9_\\', 'Jn2G'), [77])
    def test_case_89(self):
        self.assertEqual(pattern_match('h6e\x0bC\x0c#GikX\t)TU^C\x0c\\\tX/Mjw5\x0cD\t!v\x0bINk//\x0cGFk\x0b^:\x0c.\tFt|`M\x0bp}qXW(\x0cF\x0bu[b}"\r_F/W?WFqY%<rk\x0crQcvb<\\@Ra0R^@9x3/iz{iI\x0bc\x08s)]3{ zk\r~D\x0b', 'W(\x0cF\x0bu'), [57])
    def test_case_90(self):
        self.assertEqual(pattern_match("K43(t\n[Qx\x0c\n!\n5\n2(i5o\x081'ptGsUV*Z;`K':r\n@\x0bUz8\x0bxh.6\x0c%!a\\f_uld\x0cWg+ki9\x0ch#\rT'XeS4{\r\n\x08G\\\x0c\tgq\rRV\nk\x083~U.\x0bs/mq@,&\t=#pcYa7S", 'RV'), [86])
    def test_case_91(self):
        self.assertEqual(pattern_match('0 \x0co\x0bcoqF{dnZ8"\n>&Gtkdi1y\n\t(\rKl[-\x08U)y\x0cQc9qJ\r_?P-w::9\x08bUz>;\x0b\tf^\x08ucl<sH_cr.+CM6}8<b%<EZm\\0\n\t+suS92J!', '?P-w::'), [45])
    def test_case_92(self):
        self.assertEqual(pattern_match('\n^\ta"X4l\nX3)\x0cxBlf\x0ctRct-1\r\rG.\t}M-\x0b\r\tP6(a\x0cMmqZ\r"9%x@\r[@EJ!c\t@#F@9~q\x08KA]\'\x0b_s \x0c#`[Q]y0', '\r[@E'), [50])
    def test_case_93(self):
        self.assertEqual(pattern_match('XN\x0c|[oRgPaClp\x0cM3\x08\nK<Ho|\x08sFLv#J3\t\r1Q^Y*Ft*{"r\x08\x0c\t\t)1xBEbBbJ[Ovc3[TY\x0cBEvEbZ', ')1xBEb'), [48])
    def test_case_94(self):
        self.assertEqual(pattern_match('\x08~<+#e9Am7\r\x0c6%QB"0\x0889Hw\x0bJ,\n~3B|3\nH\\K2v\n\x0c\rMDf?H\'.imKzbx\x0bhZ\x0b`w\nzS%6:', 'QB"0\x088'), [14])
    def test_case_95(self):
        self.assertEqual(pattern_match('cODW\x0clX])K`&u-HvGu1\x0cSv\x0cn*xoIe\x08\x0cr\n</ww\x0cUlSpgu-85hQb{ Vn\x0b~5k\x0b\x08%*>;Wiv!\r\rcE!l%N%', '%*>;'), [60])
    def test_case_96(self):
        self.assertEqual(pattern_match(',qO*\tk{\t\'E43{\x0c\r6L.\x0b\tsp\ni M} {)|\\S)KO"y~<v\t0&c3\x0cG \n\x08>M\x0bD\\K&6W7Rb7r\tM\r\n\'[~]\x08\x085', "M\r\n'[~"), [66])
    def test_case_97(self):
        self.assertEqual(pattern_match('\x0b&M=\t\rC?\\L\n%p~)z,a"\x0bFZN-S3rNW:0M%3\x0bMH\x084i\t^\nss#\r\nE}l\x0c\n\x0cFpc:VH-)\x0c\x08)@<c~)&\r0\x0cHAs!\x08g\'<O\x0cy;\x0cSn"`~:\nF\'_\x08"7M\x0bz\tQ\rN"\x08#%Ne', '-)\x0c\x08)'), [60])
    def test_case_98(self):
        self.assertEqual(pattern_match('\x0cY7Q;w3\rACYsh~\teg#>\t{\n}I l[El5L{hDhH\t:\x0bKX\x0cWZei\t+3\n\rowi\x0cZc84b`\nc}E+5M\nP6ltSSD\tpZ\t\t\x0bA3#i\n2\x08@.u=_zDW%\x0cBg', 'DW%'), [95])
    def test_case_99(self):
        self.assertEqual(pattern_match('\t*[Vy\t^p\x0c6g\rfX*\x0c~\n~:\x0b@6s*Aiq\n\tTu&!\n%Ki\rpH_:J\ry\t%P4H*Sa~_M\x0cm5k%0\t4@\r\x0by\x0b3l;F1-uSh=(', '&!\n%K'), [32])
    def test_case_100(self):
        self.assertEqual(pattern_match('S#EDq=nb\tcH/\x08`\x0c\ngk\rE\x0b Y\rSQy~\x0cNR\x0c[C]<FX\r2\r&&6(L\x0bUM~@9,i[jvh\nqrc[Y;Ys\x0b@el#8KhB\ti"7\nK{\'\tcN_~LgH', 'KhB'), [73])
    def test_case_101(self):
        self.assertEqual(pattern_match('\tr/C=\x0c\r-d~oR>\x0b"8Q&xG[S.qdD|\t\x0b\x08*\\oR*\x0bo8-%r\n5F]*1\x0c\r"^(}!<1x\x0b\'6:\t\')Xfhil}2,L.`\x0cY\x08)#bEe,|\\_KD\x0czy&\rU\x08)BXv\'{%Gb\x0b2Z\rgw', "')"), [62])
    def test_case_102(self):
        self.assertEqual(pattern_match('k|e%"\rl1\tQo(Y4x\x0b|@\x0bY\x0b-Z[x:pN"P>\rv\tS\x0bi\r\t_wP\\\t+]\t)[\x086n\x0b9mtb|NQ{6SJb]\x08%{g+Y\x08yL%|JFm]+IE', 'pN'), [26])
    def test_case_103(self):
        self.assertEqual(pattern_match('1\x0bk|n^uv Mp^V))\x08;Y\\B^H[ @uLw/#9\r\x0bs{m\r_\x0b\nD^uWjPNV1U>\twCw0#\rtz\rln52)eg0=\rgkX4\rZyLJV.\n"\x0b)\tpa5)', '.\n"\x0b'), [81])
    def test_case_104(self):
        self.assertEqual(pattern_match('\x0bi-"CV\r\x0b\x08\nPC vJ<\x0b!e\\=]2?5\t]D\x08\tO387uhog\x08AL;+,s\r\\+]cH~U|ej\t\n\nQ*S>\x08g}Mqj\n3~r!\'g|mQ\x0bl\r\x08x*', 'e\\=]'), [18])
    def test_case_105(self):
        self.assertEqual(pattern_match('.8\\^=\x08REjNOeR\x0805L5kN\tiz\x08l\x0b\x08Sy6;v:o\nNTOh%XIF\ngs5S\x0b\tG\x0bL`\r,Lila ]#\t\x0c', ':o\nN'), [32])
    def test_case_106(self):
        self.assertEqual(pattern_match("d\x08o&\nf\x0cf fFkhJs[~`\x0bI; (#\nr\x08e\n0\t\r+T\tN\x08\x0c\x08\x08d'\x0b\t^?BM`-X!N2xZhKT\r0zp\tO\x0c.'8P&/|i\\5/gNydEY/5N-D\x08", '\nf\x0cf '), [4])
    def test_case_107(self):
        self.assertEqual(pattern_match('/\x0b\x0c:CCw!?LY40{\x0ckNx\x0b\x08\t?@\r\x0bLm*/_B~5WjQ(\x08xgm\t\x08GlSoQ=@3l!30eg \r^\t57>s\r&dtd\x0b4!]4&YnI\n%_w\nah+*=/\ty', '/\x0b\x0c'), [0])
    def test_case_108(self):
        self.assertEqual(pattern_match('?\thxlO\tU\x0c9[\x0b*U\n?d^]&2\n\t\r7eC44i`\t_S-vv\x0bg;T\no\x08+tAB//\x08@2p;\x0c4Q&h"r%W"x', '?\thxlO'), [0])
    def test_case_109(self):
        self.assertEqual(pattern_match('#n5QS?U_LAtiDi?_5%7bDe1_;E4<\r\nu\x0b)4?J4JkT*\tM{I\r?<4\n\x08~^\\:ka"qKm\x08/id>On;\x0bdpo]pJgR_0\\%\r,\x0cVW;WNkny&+(j~3`\x08m?\nr\r-g+V\x0bLs\rR', ';\x0bdpo'), [68])
    def test_case_110(self):
        self.assertEqual(pattern_match('\nn\x0bG {\r\nTOm-z9>@|\t&P\t\rf\tae\x0cx1V\n"\x08\x08i\x0brA}?J}6\tp\')^SF\x0cw0\tsm\x0c\ra>Q#j:Ky9\x08,c\ne5i\\sL*\naS\x0b0Pi', 'e5i\\s'), [71])
    def test_case_111(self):
        self.assertEqual(pattern_match('Q\rsLDkw&)O\n\x08\n\x08i\x0b\t \x0clS{hmu\n@\n+yd"R8/\r-~\x0bs4Rmo(kXU l_\t\x0cZ>\to\x0bb&\x0b8>Gb#\r\nDKI\r,WLvhn>7cv o', '\n+'), [27])
    def test_case_112(self):
        self.assertEqual(pattern_match('\x0b"c`\x0blu\x0cof&C]\t6~\x0bQT\x08 57xh\\FWN-vZ\'D9g\t\nM\'zW|[Y\nIMhfg(bR=5jiU%e6|)PV`G}^]]&7I(YX~Dt4G>QL_d\x0cS\x0c\x0boL+0Cd1zw|+22p0F\'OCo/\nZY', '\x0bQT'), [16])
    def test_case_113(self):
        self.assertEqual(pattern_match("\x0b\rA.h}9Y\x0ccW]Y\x0cfu\x0c\t\r0Hd#81i\x08]l\x0b\rN;o\x0cG. v?[~Lm\x08y \x0cK\t,o\n\n~)OjM7q`\x081\x0c\t\rn2~A-\x08eE\x08t\\<\nS_F,\x0c4s\x0bm>-xy\t#(Tt\x0bSEWkFC\n\t9|\rUN[MDT='m", 'WkFC\n'), [101])
    def test_case_114(self):
        self.assertEqual(pattern_match('nF8Z\t=:\x0c]zh\r#T@\nc\rwW|6oz`\')+uhgm\x0c\nr\rg\x0c|mJ&"\tc\x0cYU{:!T\x08\x0bS\ncC(!\x08^} EVD1eG]ou8K]yo\\)OA3Q_|F%(X6?p1@7q\x0clVH\n^-\r*bk\n\t\x08V9Q', 'q\x0clVH'), [96])
    def test_case_115(self):
        self.assertEqual(pattern_match("+kgd'x/H)KW\rqHPM\tQ\x08?W\t&\nLI30^q/352F?\tRYTg>9!-Za\t\x0b\x08\x0bT?kdkIbc\x08Hz\x08\x0c18\x0bm\\f\r?X(\n=^Aw7F\x0c,gOzz\r3Sl", 'LI30'), [24])
    def test_case_116(self):
        self.assertEqual(pattern_match("U6{:\t88d'\r<!9\njDpW\x0c6\r0eS\nE->E\x0b=\x0b.H\x08aCa=}d/ip0\rv@6~\\KX=hH[`FA{sF\x08\n9DL\r;3QF\tYq&1:T~\x08PI@\t", '.H'), [32])
    def test_case_117(self):
        self.assertEqual(pattern_match('\t\rYOzH92B#f?`\x08*\x0b\nru&ag-=q\ru!keKM}wzf#\x08DIcOCS\ts\nD:c#i\t<^\x0b%O\tE\r(h\x08-m\x0b', 'cOCS'), [40])
    def test_case_118(self):
        self.assertEqual(pattern_match('\t(Z5g0&\x08q\r(\r.VEk\r\x0bo\ryc\t4\nOtynu*P8pk6S\n+\x0cqXWLASVXt\x0cv\rf\tP \nPP\x0c\x08G\n%-\r*o(h`Q/kW\x0c\nDl\x0b%l~Y-;\x083\x0cOha:\x0cp^<\x08kP*_\t', '~Y-;\x08'), [82])
    def test_case_119(self):
        self.assertEqual(pattern_match('`JRbkSgnH tzlJej:O{OEJb7\ncQ\x0cI}}s\tSIwC3\x0c\\\x0c)ZR9\r\x0b\x08\n+aqi\x0b~E%\x08\x0cU\t1\r\rWcA\x08\r:\nM\x0bSb\x0b\nO\nZM>', '\x08\r'), [67])
    def test_case_120(self):
        self.assertEqual(pattern_match("C(auSW;q(]U\t\\\t,.~m>\r\n\x0cWO~P\trc.siA\rVyYObad\x08\x0c*&:\x0c/}oGXV\x0bTu'':(5kmm\x0b&U\x08\r?wK\x08L#@P0n#&\n\x0b!\x08W,\rBT\r#-S.\x0b\x08\tlfYR9\t:Z", 'P\trc.s'), [25])
    def test_case_121(self):
        self.assertEqual(pattern_match('\x0b.oO,g\npv\rcr \x08T9ZZ-hu.{de%Mat\ryS_\x0b\n-Qw;G\\e\x0c\t=\t42D<isUYU/\rxr[\x0bl\nt;\x08;\x08vngP/z\x08\nG\t', 'G\\e'), [39])
    def test_case_122(self):
        self.assertEqual(pattern_match('\t\\6l@Y@XFIg^kE_Q[0A\n7_GZ,\\8Ul\x08J,]%Ve\r\nD,%\x0b`.\x088K[\x08{\x0b0FOm \x08\\F?\x0b\r\to\nkE]dO+Xp\n/\x0819DG65gzY0LvW)\td?>8~', '0FOm'), [51])
    def test_case_123(self):
        self.assertEqual(pattern_match('p{Rx89CW_-Yz{B-!J\\m&#Gxzf#I\n\x0bn\x08aqN]V\x0cvCP\x08\nS|T\\?\\||j/~\npvjvh\rT;PeD.\tc\x0b`jH__p#Z/2!~i``h]0\x08XubZfA)mf\\bW3:N7q;zle_5,u\x0c|\tLH5', '\rT;P'), [59])
    def test_case_124(self):
        self.assertEqual(pattern_match('t&e\x0cBLOA\x0cf(\n{Bb&F`\roXt/\x08~!&s3\t[\rJe7/MX#H+0\t\nV\x0c\x0cR\t\rLU.\r\nq-\n\n{.@wbr\n3', 'V\x0c\x0c'), [44])
    def test_case_125(self):
        self.assertEqual(pattern_match('\r|5*(}\x0ce#Kp#ms.\r\x0c[5\n5@O"\n\x0b7si Tg\x0cO_L!D^\rVj\x0c\t\rWl<\x08^+gWol}gjYSIMLU<eW\nW\x0cr<AGo\x08', 'Wol}gj'), [52])
    def test_case_126(self):
        self.assertEqual(pattern_match('Tj#;Th>b\x0bH\n\x08Fx4g\rsYJqJ/4bR\t)`G|(\x0c\n\x0cY\r\x0c\t^Rl?<cwA1kwRF5\x08m"W"\r\r(L\nUCFV_7V?K_;\t\ns4\x08Ee:~3U:\'IW', 'g\rsYJq'), [15])
    def test_case_127(self):
        self.assertEqual(pattern_match(".\x0cre'\n\nhG!]VU\tC6GC{%\rw\t\nIn:eKo\tc1agj&&yUxRd#K?GO\x0c(G\x08P}@{\n\x0b|0)}t}+5\n", '?GO\x0c('), [45])
    def test_case_128(self):
        self.assertEqual(pattern_match('0\t%H\rXtz4pb=ER\nv\x08B8yNgyJ1*#i\rmU\r`yJ k{o=\x08\ro\n/(\nS\nVI\x0cs\x0b\tYZl6t\rGrG ~c', 'k{o=\x08\r'), [36])
    def test_case_129(self):
        self.assertEqual(pattern_match("\r{Z-kjH}}Jn!\x0c/Ny:f0n-\rL7\r30\n\n\nJrb\nXXh=T\r=L??',?*t|\x0c 9^zg4P~)!b.eQ\x0cY{v7'em3kycuP;_39&'\txzP\rwoH?", '\nJ'), [29])
    def test_case_130(self):
        self.assertEqual(pattern_match('Xo,s\tL<;XdQ2;?.bj\x08C\x0bm7\x0b2+?4pjQ9\r\r]J-\rtl\x0b:-3N%N\x0bEcR\x0c(1_\x0cn%saMN\nNn\rkBq\\/TiO\x0cY#~-n\rDR/jK7{3L0j\n,<-+y#tG23+Pv', 'L<;XdQ'), [5])
    def test_case_131(self):
        self.assertEqual(pattern_match("s\rOh\x08<\t)1M6OT2u+B\nRp\rL\\\t4ko/zk\x0bY(sRVAxo_v.g\r\t\t\x08owz0\nWj%S+} LK9#<\tW\x08I`m\x08X\x0cYq\x0ch0\t\x088P\x0c5_\x0c(U&\nzj4d#r;RLKA\t\x0bNy~gn'a\x08J>E{\r)", '\t\t\x08owz'), [44])
    def test_case_132(self):
        self.assertEqual(pattern_match("inQ\x0c{sC)~-Qj+~w@>um{25-\rSmbD\t[5;&]ij\nI0Jrx\t~Z\x08_ X}(No/}|c*\x0c3\\?,#+(-MC:W\x0b&ie:8RaKz&F\x0b'5M5FAMJ", '/}|c*'), [53])
    def test_case_133(self):
        self.assertEqual(pattern_match('qQ*\nF+5*LAb\t.CkY|]&\x0b9P.\t\nh,\taw4\x08T=y,\t?\x0c!\x089";f]"~*;\\WP\n\rI\\jd\t\rNMhjCg\x0b<\'i@;9\n@[NW2GbqG\\\ro{_&MdpxW\r\x0b', '|]&\x0b'), [16])
    def test_case_134(self):
        self.assertEqual(pattern_match('I/M\x0c-Wlj\rK\n\x0c\x0bi\\B>+!qa-y3;L\t \x08{\x0c!J;h/B\x0bRB\r\n\x0ba\x0b~@yz7\n_W}O}_!hQ\x0bXa}', ';L'), [24])
    def test_case_135(self):
        self.assertEqual(pattern_match(' K8G|\x0b\rIeH+A4pnt5\\A\x0cn^v/[Wp]SGx5\rL%is2\n\n=x\x08 \r F&\rO(48=)9\x0cJ~Q*8[Q%?1^  \x0b\r\tpSK-\tk?"#<Z\rj9zfB]i]\rG\t0{i', 'SK'), [74])
    def test_case_136(self):
        self.assertEqual(pattern_match("rk-GN!95YvT\x08;%n(LW%6v#8@';s|\x083Zc\rH\x08neXaE!\x0cM\x08qB\t\tK\x08D\t\tYLT]MuhdRM\nuKXQ\\", '!\x0c'), [40])
    def test_case_137(self):
        self.assertEqual(pattern_match("|)u'%[r<|XQ^pv\x0b:i\x08#CM*\nfBd?h\nL`yIbT\x0c|-7\\K\x0c1R^Dy'@:QF]f('f\\\x0bV\\RC=\x08;\r\tjY?\x0c\tfE\r1^Ne2^vz<", '1^Ne'), [76])
    def test_case_138(self):
        self.assertEqual(pattern_match("g3R\n!!m/b]\x0c?-:P\x0c*\x0c%\nzG\\~A\x0b+@\t'\n\x0brT]:\\I,\x0b\\\t\t\tB\x0c)8\x0cY\x0b`G69=)\r\r\t[/HcHap~\\", "+@\t'"), [26])
    def test_case_139(self):
        self.assertEqual(pattern_match('.\x087H]F\x0bL#R\x0c\r\x08exW\nz/\nN_U\x0caM[`6Zbe\x0c\\/M3>cnf!x\x0b3,\ntG\n"wG9\x0bGz\rZwR,\x08}5]KVF:', '\x087H]'), [1])
    def test_case_140(self):
        self.assertEqual(pattern_match("\r\r[&+\x0bC\x0cPtZ5\niGg%\x08\x0c\x0b`#K/Y\x0b\x08/stW\x0cTiL~]U b\x0cT_XMs|4&bccL \x0b6\x0cqfewCiXJ-B'0yB&^%8Ss\nV\n@(3&&\\\r\x0b`c6b0%[\x0b6jsNkI", '\x0bC\x0cPt'), [5])
    def test_case_141(self):
        self.assertEqual(pattern_match('R*\x0bq~\x0b\n+\x08+\rDl\\r9g{\x0c\r0\\OTXl\x08e5v\x0b1\x0bROc\x0c\t*I\r6\nSC~6nZ8;%>\x08_Is\x08M,!ctTz-M\x0b\x0cHJ0EE.FF7\x0cRFqJ(#\x0cZ-\x0c\x0cj1\x0c3M\r\x0b\\N', '\\OTX'), [21])
    def test_case_142(self):
        self.assertEqual(pattern_match('<n\rxm\x0c:\tR\t)Y\x0clE\x08\x08s\x0c5L}i#~1\tf\x08\x0c!C<U\x0b8d\r=(\x08YrV\r2VL\x0cD\'HJlu502F{\rU\n<?\x0crn%Y\x0cj\rb6\x0bVk<\tD\x0bk\x0b}:j"2M\x0cvMsux:hoW9\t\r9Z\t\rz\'OZ0\x08y\x0b\t', '50'), [55])
    def test_case_143(self):
        self.assertEqual(pattern_match('*:w~P\n\rc8\n\x0cWybSwls\x0b\r\t\nE\x0b0:5j(~\x08fv mk\tt&,e][U>#[jr<if+f%\x0b/Tm7E?28\x08nZn7MU^\nPnK+\t{o*#\t\x0b^5g=bBK0k0S\t#V\nne\tjZ\x0bSj-x\nm2@\tewR6', 'e\tj'), [100])
    def test_case_144(self):
        self.assertEqual(pattern_match(")\rm3\n\n\x08\r8\x0c\t\x08bO\x0c5/}U.o+P\r]cF82K8h\x08M\x0c^_Gn!}d_vzkEW\nQ`4_q\rP=+6y*\x08_&4G}Bd\tAZ)k2FamwYL'\\>J\nd6t\r?{nRQ&)p\x0cPIl^yCwnco\x0b\x08)a(dm:n", '\x0cPI'), [98])
    def test_case_145(self):
        self.assertEqual(pattern_match('\n{7g?d\x0cDu 4-cid}x[ld.A\x0bn\x0b=\x0b9v81D\x0b\x0c%4N?\'\x08sm!2O\t\nG|;}w_\tXEoY^-\x0b\tzA\x0c\t\x0b?\x08@S`H=Wk;m\nac<3[t\r\\\r#S-Y3j\x08B"VP\ti*\r\x0caH\tAW\x08yvw7*\t9,', "'\x08sm!2"), [38])
    def test_case_146(self):
        self.assertEqual(pattern_match('{074G\tpH/IEfo4p\nd2D\t\x08\x0b\ra\x0b\tMy.\x08\n@\x08Qoqb*f"F,#y\nC\x0cw_~k\t:_iP\\o\x0b23@\rC&n\t\tr\x08{jOjHQ7\x0c|\x0c1~lg,\r<jt+3pT^`>6', '3pT^`>'), [90])
    def test_case_147(self):
        self.assertEqual(pattern_match('K5T!wwY^"|=K1(@_\t&hdQQ@cgTY*8_lLY\rnN\'l@@P^AAb\n\rX\x08\x083\x0c\x0bS!UZ\x0csN8\n/Q\t9rP-\x0c;rw\n\rx\'!^,', '@@'), [38])
    def test_case_148(self):
        self.assertEqual(pattern_match('dGgM_\n\rhI,\\tqw=\n\t4)KP\x08Oe|u-99\n\x0bh3@0n\r]N\r@{qwv\t}]`)%v~\x08Z\x0b7b :M9K+go&B{+)+iN:^9\x0b\ncY]kW\x08Cde', '9K+'), [61])
    def test_case_149(self):
        self.assertEqual(pattern_match(')K4P\r\r\x0cKkuR]\\1g&s81lC=^3>lX8zqfZ3qX8+G@"l6QQ\x0c\rYx-R~Xr\n?\x0cJ\x0c~\t \nhm\tN1V}Z@\t2&{\n0(\\q7\x08C!\x0c;', '~\t'), [58])
    def test_case_150(self):
        self.assertEqual(pattern_match('7x3"Y_*\x08,y4J%S\n\x08\x08exl@\x0c91&^VBd\tS@vMYs=u&:)2]\x08l\t(d{7Grq\\}MHU\x08I1Fkz\x0b\x0b#\r(', 'vMYs'), [32])
    def test_case_151(self):
        self.assertEqual(pattern_match('=);#\tu!?Xt<_g\x0b)NP<bssI\t}\x08&E,V0k\nh-L\r:j0?qk<++ c+\rS\x0b(\x08\x0cN{EvQu26m{\n-g\nI}6/42OQbD/\x0cY7v5nCV5!\nF{g\n\r\nQIx)', '-L\r:j'), [33])
    def test_case_152(self):
        self.assertEqual(pattern_match('/ =\x0b]\n\x0bax\t\x0bP5d\nxK]"KNYQ\tzsS7\nmRIv\n{w}o\x0c_2h?,Y4G\x0bu\x0c7\x0cxe(@=9\x0c\x08dGv\x0befa/!=v\n\ra\x08\r\x0cG99GUj+2\x0b-\r:vn,x\x0b38zlM\tz"y[O#\t2SH4nhb\r%', 'G9'), [77])
    def test_case_153(self):
        self.assertEqual(pattern_match('\t1lii7\\+%\t`\x08Km@2\r~\x0c-H.%#X\t]\\n5\x08c2EH~XHwaY\x0b%N\x0b\t(Em\x0c9x(\nr\'_\r|#sX;L5\t9&3;~\x086\x0b/\x0c"tv.1\x082\x0b8n1wO&#h\\HN\x080f*w;\r:7', '\x0b%N\x0b\t'), [41])
    def test_case_154(self):
        self.assertEqual(pattern_match('r/*W&&5\t\tj3m(N\n\x0bB\x0b)\tn5F}&\t*}%f\nrGj77B{D`+L\t"j;Q\x08V* BN\x0b*\x0c4C\nC"<\rb\x08)y\r5H\x0cc`:nAR>^6?U/>\x0cV\t,&b{bt\t', 'V* '), [48])
    def test_case_155(self):
        self.assertEqual(pattern_match('i\n\x0c\t;N (+}r3G\x08.]B\x0b\x0b/a\x0c-Fe`=\x0bf\x0c\x0bhDmtZ~C\rZ\tbX\n3n;N\x0c;(7i98\x0cF6kK5h\x0cl0o}\x08cH\x08k-/ut#;N\x0cJ%dX\x0bRj]t?.gI', '-/u'), [72])
    def test_case_156(self):
        self.assertEqual(pattern_match('~"LFzqtrdB:m.xBVx\x0cjp\x0bpYQPp\rIzmVh3 \x0bz\\UBo*!\nDb\x0b\x0bc/G}[_H\rcIy<\x0cR\x0bb[};WL=S_A\neN\rQem{tw1\n:', '\rIz'), [26])
    def test_case_157(self):
        self.assertEqual(pattern_match('\t\r\r~\n*w#\t^0\nVu1\x0cHhM\x0bV~Z"RR\x08\t\x0cEsvHFr 1b"J\rAp\t\t%D;\x08F6\r  o\tG]::?o1\r+\rv ?\t4\x0b1G', ']::?'), [57])
    def test_case_158(self):
        self.assertEqual(pattern_match('\n\x08A\tw #le\t\rox;M*\tL).iEegQN=l4QqNW@\x0b\n\x0c|Qopp0qm\t.C@)zG:gq](\t2\rgc3[\n7w"k=5c&A]Eq', 'pp0qm\t'), [40])
    def test_case_159(self):
        self.assertEqual(pattern_match('\tje\nv.LI)vJ\n\n)K_u\x08*A\t-C\x08\rT68r\x08A+\'\x0b\nSRB~*"S\x0c\\\x0c(\r\\;1^J\tK{\r\n2e\n-/Chi\x0bBzY_D', '\x08*A\t-'), [17])
    def test_case_160(self):
        self.assertEqual(pattern_match('\x0cK\tm^F_rM\x08RD\tE\t|"\x0b>]\x0c|/>HL#6\x0c=?5O9\r84\t\\|BXSxvC7\nN}K>\x0c0z\x08\t>6w!D\tMzq\'}\x0b"RV-:KAcjb\x0c\n2yCMWg\ng%\rCRh\t\txyL\x0bdom\t:\x0b<h?\n1', 'BXSxv'), [40])
    def test_case_161(self):
        self.assertEqual(pattern_match('Bg/F{\n\x0cic\x0ce&v\\\x0cxlxL`\x0bnqif4\nf0\x0b\t\x0b\x08"O\x0cJw47`\x0cL\x08\rRln0Ub\tPGg&\x08\n2]jCv\x0b>#K\n+KMZ)=\x0b+d\x0bxS3LCVP~Nad"\t|\x0cu"\x0b=o QCD;KH?X\n\x0cuseEz\x08@VJf', 'b\tPGg&'), [50])
    def test_case_162(self):
        self.assertEqual(pattern_match('w9&{Yh\x0clC\r\tg3)x"\x0cuq%l,\nu|\x0c\x0bJ\nLP}uKs\x0bQdpHZ~\x0c{^d+RSz\n\x0c,j9_DR"B.)c\x0cyt2nl;~*c}n)]0}9\n%\x08Wd=\x08sol5k"QF\x0b\x0cg=pAtZW\\,>\'\'DX\x0cT\x0bRV', 'pHZ~\x0c{'), [38])
    def test_case_163(self):
        self.assertEqual(pattern_match('<y&&czz=\n]\r3i\tzH7F\x0c\rvmZ*\x0bi\x08\n\x0c\x08f\x08T1\rd\r78J\x0b\t5+On\t\x0cdpw?!!z.B\\,a\x08S"\x0c Ga\x0cc3EX\x0bh', '\x08f\x08T'), [29])
    def test_case_164(self):
        self.assertEqual(pattern_match('\x08\x0c\tl!I\x08iny\n\x0cmw,\x08rF}4l\x0crs.)ra+sGWo\r-`XxP"n/vO-{\t\x0cO:To\x0cM%t8\x0bDK\nC\tu\t\r]m\x0c/kZ\x08\x08[-', 'GWo\r-'), [30])
    def test_case_165(self):
        self.assertEqual(pattern_match("9'9\x08?\n\x08\x0bO}\x0b\\P/`B!Ge\to\x0cE@)4G|yqjv\rRR5\to]\n\x0cP\tw\x08;1\r/`kt!8P<cs-@m'%\tbj\x08b\r'hE\n&\rMuhW\x0c\t\x0c}q@e\nSW4e~\x08h)5=f!^\x08F\x08", 'E@)4G'), [22])
    def test_case_166(self):
        self.assertEqual(pattern_match('[6<\x0bNH-/\\E\neW^n%\x0c\x0c}~,x!8!D.:\r\rq6c34/q7|Ep;jh#\x0bZF\t0\x0b\t\x08\x0b6zq!\nv\n\'\\e\rY/\t\r1"\x08Z\x0cfS\x083r\t\r<~\x0bk\x0bJ\x0bnd9x\rT>\nd\x08\ru\':d;jVe(]\ru\x0b\r\t[@Idw\x08', 'S\x083r\t\r'), [75])
    def test_case_167(self):
        self.assertEqual(pattern_match('9\x08GEy7w\x0c{!3f(JbQX\x0bS"~og!F7\r\nW&fH.:\na<BqJ\x0cp.VgFG8< [z\x08|aw^P\x0bm3*p\x0c_]Ep_JW_T\t>X?wR\'+:\tmlK\x0b\rg0\r-J{Hj\x0b [\x0b\\:Mu\nv*,5oP;mdG9', 'f(J'), [11])
    def test_case_168(self):
        self.assertEqual(pattern_match('\x08dk\ti\x0b\n,P}Q68QG\n}{Mo6+F?p[U6\r\x0bVqJ\x0bQyGwm[-4\x08\t\x08\x08\x0ct4ySinN\x0bKSmS\x0bTW\x0bIzebB~Ywt\r,9#6G\n45', '\x0bQyG'), [33])
    def test_case_169(self):
        self.assertEqual(pattern_match('l\t;\x08\x0bH5\x0cIN9lr7`\x0c{jx]fO=4\x08_E\r8\n\x0c5\x08U-\n.i7v.guJz:;R@:gmE\n\x0cN<Espj`74RC>NjG\tJo}B\x08]>\x0bi\rc\rs\x08]u^;alU5\rz W\tS\x08c\\\x0bk\x08Ch\x08{~,;daK[\rZ9', '\tJo}B\x08'), [70])
    def test_case_170(self):
        self.assertEqual(pattern_match('nDw6Y\r;\nvnB}1b6N|\t\x0brX#(,>HK\r\x0cP05nT\t<\np\x0b:]9*1\t\x0cg8S5\reo\n^;\x0coWD#*<;\x08YT', '(,>HK'), [22])
    def test_case_171(self):
        self.assertEqual(pattern_match('m~1W@1Hq/L=Rc\r\nW\\g?\t\n[R,\n\x0cD\tw{"\x08B;6S\t1."i.EktcQn\x081lJ7TC}\r\'?n7\x08A\'u\x08TU.wE\n\r+R&x_c=d\x08/_j5x\x0beB!\n?\x08\tDnn\nbXx)(vp\x0c+0`B;', '\x0be'), [87])
    def test_case_172(self):
        self.assertEqual(pattern_match("\x0c-%7wof9(R\x0c\x08\nJ\x0c3KbN^ne64a)y\tw?xU\n9OVkd\r\\Yts\x0c\x0b\r\n>So,<<\rp9\x08BS_\x0b\x0c\x0cy !9&o'r\ru\x08B{JBc\n 6a\r\t\x0c84W)j26ed7'Wj\x0cZJe+=", 'c\n '), [78])
    def test_case_173(self):
        self.assertEqual(pattern_match("ZO84\x0bo\x0c_\t\rEi\x08B[7sd5}\x0cL0R(q>Pyp2zD7F_55y'M)O\t,V7^\nz8zAT\r13WIM\x0c\x0c\t_||q\tj8\t]hgDlyJ\ry3MP6\r=\r\x0b,E]!/^z5d\x08+;2gdLQH%\x08\x0b+Wq", '0R(q>P'), [22])
    def test_case_174(self):
        self.assertEqual(pattern_match('!6\\a!aXt  etq*\rd\x08TFjR<\n\r\n\x0ci%R~Jbh\n\r4"@W\rH\x0bi<?\n4|\x08k\x0b>\x087#(l\x0c@yIX^otH`(0el^E|#\tzr-xP@2U*w6\x08hxA:8Pa2\x0b\r\r\n\tC,n[!', '\x0c@yIX'), [57])
    def test_case_175(self):
        self.assertEqual(pattern_match('3?VtA?tm\\_aX\x0c\'\x0b-J\'WE!\r\r]P;R<\x0b\x0b\th\rQ\x0c\x0b@7a<\n"\x0b3\x08\n1^\t[Q<s\\d .l<;h!OEB\tI\tl\x0b X\x0cv(b#\x0c3\x0c\n_)!#t\x0cg^,W6k\n\x0bX|m|3iC\x08\n\x08F3px\x0c_', '#t\x0cg^'), [84])
    def test_case_176(self):
        self.assertEqual(pattern_match('m?9<8&`c\tja\x0cb]u|DqiwLqp|csIXR&\x0c?\x0b\t@G+GGi_>\x08\x08)kTxL24|`,c9V3>\t\x08gU\x0c\x0c==_@""-9\x0c/hA-\x0b\nL/m\n\nOH)~', '9V3>'), [55])
    def test_case_177(self):
        self.assertEqual(pattern_match('\rH\x08*f9!\x08<\x0b\x0bl?"i1;k\'7;\tG4T\x08}ssbPUr-@t,+\n0REw?o\nQ~\\u"]\x0cNsD|\x0c:\t7^M(\r(dO\t>G?\neNCMr}oBu2\nUNYRv/\tx\x08R[s?\x08bHnaU\rTeI,\x0bjH\x0b.^5[', "'7"), [18])
    def test_case_178(self):
        self.assertEqual(pattern_match("J\rC}*A\x08/{aM7\r\x0bFz!uvsSF\nq=?13w7/ Z\x08'C1e\nq.hdm\r\x08Z\x0bJ\r!hxdYbJn\rc^\n#e0J#=qRa43:W1\x08", '\x08Z\x0bJ'), [45])
    def test_case_179(self):
        self.assertEqual(pattern_match("/xv,\x0c,0YY\x0cGb\x0b9O;+D2&\n3pSU)DI9_nI]!/y\nA#F'!s__h8\t7^vu\x08o!J\x0c\n*PQ\na\t\nD\x0c!Z\x08", '\n*P'), [57])
    def test_case_180(self):
        self.assertEqual(pattern_match('\t^Hr~?Yt\x0c\nf(\x08\x0cyO`Rq\x08J)W\x0c~cQ,=\r@\x0b\'M#\x08@e?f<fc&L\r\\P6P\x0b\n\t~xvA\x08R"\r\t+r\x0c\t<*1v\tcb;\x0c\nfw=-nfX+GCIukzAt@', 'c&L\r\\'), [42])
    def test_case_181(self):
        self.assertEqual(pattern_match('ycj~e2\x08Z0QCn_>\x08S \'OnhI\rvmn9RV.\n "pbfR{\tAV\x08J\x0bH8\tf^\x08\x0bf}rX7\x0cpZ6\tf0pUv\x0c_\x08)\x0bxdnpc\x0cT"4\x0c;\x08kqs!*`#)PeC"\x0c^#\x0c\x0b\x08\r', 'n_>\x08'), [11])
    def test_case_182(self):
        self.assertEqual(pattern_match(" b9>hB[`Ky1v'Be\x0c'\x0cMq\x08X/#A`\x0b4<b3sS`_\tADa\n6/&\x0b\x0b<`\x08Y-h@al[StL\t==Q9SM\rf|\x0c9\t6p:'\x08\x0bZ\x0b<\t!b\nF0%P8b\nN\rS\n", 'StL\t='), [55])
    def test_case_183(self):
        self.assertEqual(pattern_match('\x08\r\x0b4I6\x0c/:\rkk\x08|=\t\x0bYJ3_x\nu\rk\n@zlp \nN%\tA6OM0z\x0c+A0C26blPqH\t,[AmrvRW\x0cy\r5s\r\rK9pNo\r\n!h~p\nwT', '\x0bYJ'), [16])
    def test_case_184(self):
        self.assertEqual(pattern_match("w\n62FL\r4zHR.GR4nvna:Llv\x0ctxxq/<rHv,'nxl+q?\t]Q\x0b,\x0bS\x0c\rP\x08k\r*(h@S.vpJXW!5fu)\rN\n\rdf=x\nk-\x08U4E~wbRBUJL^J\x0c\n\x08", 'u)'), [68])
    def test_case_185(self):
        self.assertEqual(pattern_match('M9v\x0cpS\nCGV^eISF{yS<\x0bk\ri#]\x08l"\n|8F3\x0cD{L@D\t+7E,9&Wz&nH\tL\n\x0b_\x0cS\n-,\n\x08\x0b\x08\x0c0\x08MlHV\rV=XKZB\nHA*R@;)Y`qSl/s|Vbtm', 'V=X'), [73])
    def test_case_186(self):
        self.assertEqual(pattern_match('*`\x0bD ;5p\n\nI1\n s[N\r=w4UZ?bA8aT\x08\n&81M\tI\x08Ho[\n\ny/\x0bn\t\n+v~">lt}5\rZ9~@S\njZ[zoIpTI', '4UZ?b'), [20])
    def test_case_187(self):
        self.assertEqual(pattern_match("O<?`v\n\x08^.0XT\x0bgi':[l\x0bUwRL PoGltbF\x08hzIbTi\t\x08\r%p\x08+OeO\rz %`\n^@&M3Kf+\\C\x0c", 'Kf+\\'), [60])
    def test_case_188(self):
        self.assertEqual(pattern_match('\nC&\ru>8\\\n_Z|\nEZd=t\'*\\9\x0bAYS)`|1\x0c;\x0bki6`57\r\x0c\x0cPYcQCKi9cW|\nSl]e"\tYx\n\t]aiW+\x0cY"\x08\x0c4.Ow-]\x0bSgu<RY\x08#1', '-]\x0b'), [78])
    def test_case_189(self):
        self.assertEqual(pattern_match("\tFMq'd_\x0bJ=rH~zViHfD\x0b\x0b&&LCV\x08\\b\ta\t\x08o0SJFdF\x0b`pXcA;\n\x0b\n\ral m\nh]C\x08U2u@|r7],", '\ral m'), [50])
    def test_case_190(self):
        self.assertEqual(pattern_match('SkT2N6P\x0b1u\rfvN\n7sG\x08=q\x0bd\nIRl\x08\x08l&b{BE\x08V\n\\z?\t6h39I\x0b \\O^8+CQgDh ,SbV\x08dK3M`\x0cQ\tR\r}0d\x0c', 'd\nIRl'), [22])
    def test_case_191(self):
        self.assertEqual(pattern_match('\r/tK\x0cl|mNQ*CHU\x0c:\x0b7q\x0bgKh7sKYh(E\r\x08\tF(C&0N@!O\x0c_\tw+7\r\x08j\x0csY/Sh\n\\d+Q\x08', 'Kh'), [21])
    def test_case_192(self):
        self.assertEqual(pattern_match('\x0bM5#>#/S\x08\x087]\r\x08?QW#\rfp2}O(\n?2 Yk5gz\x0bjFc\x0b>#eF<G2\tkN,@u\x08:n{:J\nrP{\x08y\x0c8\n_\rO\x0baDa(pHS\x08VLNpo0K6\rw\n(vlV]z\r\tNZ\rdF `?\x0byR', ']z'), [94])
    def test_case_193(self):
        self.assertEqual(pattern_match('6\nv!(_f\x0b>\t5S4=\rnb,BjM\x0cY(\x084\tBmcP)O4\t\r4,q\x08H~#=\x081\x08N"mpyv\r \x0b!\x08HFF(6\r\x0bK\'iehTp\x0bk`fPC`\to\x0ct\x0ca|e.Ni;|Z\'m\r\x08dKDd<<q3./\nJ', 'mc'), [28])
    def test_case_194(self):
        self.assertEqual(pattern_match('lU}UCAahF\n\tV\'9d8oVKL\x0c8T\x0b\nT\tq1\n\n*\x0b\niC=_t1q|}{\x0cv5\x0b\x08v`"gbEG!lu\x08v2sPZcBGMBuU_uHTm4\rL\nZ8ny\x089A.\rW\x08f<dkn\\', 'q|}{'), [40])
    def test_case_195(self):
        self.assertEqual(pattern_match('{\x08 }>\to>;jn7\x0c\rh\tB`\'+?=q6s\x0c\n8"^T9\t56oOKoon;<%iA\x0b\\E+J@*\t\ntvbqj\r\nJ(3\x08s:\rT\x08&.\t|8gju\\IX!\x0b\x0c"Mu\x0b\n\x08^ZWQLt?\r\tc9-6f>c`\r@\x08 2>\r\rS\x0c=Z', '\to>;'), [5])
    def test_case_196(self):
        self.assertEqual(pattern_match("?90Uaz\x08\\w&n\n\x08`6\x0bYmeh6c(5a=\rV(1 \x0ch(phKoE s=\x0cY4\t<1\t\x0b\x0b5:1\x0c4,iw}D*vNDxA%znZ\x0bl\tjoEPl\r=;3,.2'7:PN4\x08\rO|Lb2lVQY\tm>\t8\x08|%\x0c@LkV", '90Uaz'), [1])
    def test_case_197(self):
        self.assertEqual(pattern_match('4nC}\tK3UfEh7\n P?\t\t>r\x0c*zNWe]w``~Nx^X"\'\x0b,\x0cc55rrLVc\x08+\'Ndtw\r \x0b\x0cWE\nN\n|', 'tw\r '), [53])
    def test_case_198(self):
        self.assertEqual(pattern_match('\tmaM!ftQ\r~[M{+\ro9\n\nI\x08O\tA!n\x0b\x0b!q`\x08%.[A4g-Se|m0\x0b\'"!Zj)+\x0b*\x08{\r&\nH+\rRh6\t%JXj1gVH-cX.', '9\n\nI\x08'), [16])
    def test_case_199(self):
        self.assertEqual(pattern_match('G\nB_hnvBX<~\tYs-TVX {R62/\tJ~#_\tIPgA\x0b]9i\x0b\nf&D\n\n.\\\x0b\r*huo-=-3\r7\t <\r-\x08f\x0cg|@I>mQ\t(<\x0bB\x0bk=sCa5\x08/&Ey}5\x08J,H\r?{ ==\x0b-\\O2K\x0c:g\n\x08>\r#\x0c\x080', '-3\r7'), [55])
    def test_case_200(self):
        self.assertEqual(pattern_match(":#3O,S0#]!=n\tt G&q#@dkkH{\n\r(\rVdEb]PqG\t^^<\x0c0mf>Hpn/T8AN 1?-*)^P\x0b,hN'f\nHv\n1\n4.\x0bsD,_HLN\r", 'mf>H'), [43])
    def test_case_201(self):
        self.assertEqual(pattern_match(':*7\nOD|Qn{&\x0cw\x08prJb\x0bSn5)(VP\x0c(QTblY\x08q^2aA\'\r/\x08\n\x08\x0b.;:`\n6ew%\ni-\'\x0b=\\y!qlo"*Srn\np\t\rXW\t2A%6\t\\\x08LV+#y0q\x0c{]P\x0cuBNx\x0cm2.\r&h\nau=\x08', '\x0cw\x08pr'), [11])
    def test_case_202(self):
        self.assertEqual(pattern_match('JA\x0bm^p\t\nAGCg\x0cfg8 o1:=\x0brV|\x0c\x08-2E77 sBsH\n(t\x0b\r^Qj\x0cC\x0c?W\r{\x0c\x0bq&\x0c\x0cL|M{E\r\t\t\t\x0b\x0c+j\r>B\t\x0cODCn\x0brMRh\x08*o\r2\x0cv\tO\x0c*\x0b\\\n02:F0', '\n02:'), [98])
    def test_case_203(self):
        self.assertEqual(pattern_match('O\x0c\x0cIE)\r=ys| q1S~\x0cXEo_w/\x08*-m,-B^\x08%\t\rA`h%~]p\nEGm\r\nX\x0b:"d+LB\x0b\rKF\r]}w\x0bX[I\x0baG\x0c]1<8Dl?5#A\r})3k}"\ttfte\x08F\x08!,mZ2#zfbb', '-B^\x08'), [28])
    def test_case_204(self):
        self.assertEqual(pattern_match('NvkrB\x08}(\toLQ8\'\x0bUg\nO\x0bU,~rF\x0bX^JM\x0clDh&IR\t\r%e\x08S{ta\x08^%\rxjy\x0c\n\r\riD6;yVo\r8?Zm\t?KM\tRg"R\r\x0b0lt', '\tRg"'), [73])
    def test_case_205(self):
        self.assertEqual(pattern_match('O\n*\x08(lvAM%>\rN]q`7"\'\x08qJ1Uo_c\x08\x0b\x0b \x08XCTX!(,AS_MN#h4aq_JA\x08\x0c~:\t}B\r\r}1\n<O%+,}Y\rT"\nBa=P', '%>'), [9])
    def test_case_206(self):
        self.assertEqual(pattern_match('."\tT[\r3jNP\r\nt^z//\x08^-26/\nSyaR}LpaE\x08%\x08]~t_\x0cG>NduK(U]bSmZ5N%1\rLbV\x0bX.-H+r-\x0cwip))\r6\r]\x08AJyJ\x0b*\nQS:\x0bD?\x0bwxI_q\x0b.\t', 'G>Nd'), [41])
    def test_case_207(self):
        self.assertEqual(pattern_match("3C1Oq\x0c\x08cG=X\x08<J+\n\t~(j\x08r\x0bcr\tD@cOk% FA:\nC)hG\x0c4-!W\tNBGyQ'u2D.RT\x0cfI\nD\tRa*", '\x0cf'), [59])
    def test_case_208(self):
        self.assertEqual(pattern_match('~\r\t=SV*_NA\x0b\n\r)\x0bT\r3pUR=:ch\x0baX]sB4b2{1k\x0bG}YmhO(\x08?~\n,\t\\l5Yt;\nr\x0c{P+yUuC\\i V\n\nk.X%f]RCS\x0chlY\n\t^[F\r\\*,4?\x0b\n7i;Hi0f\x0b\n-', ' V\n\nk.'), [69])
    def test_case_209(self):
        self.assertEqual(pattern_match("p\x0cB%\n<vIpEA6\r\t5}iD;!\x0b~\n~\x0c +q\x0c\x0byBY:%h`'\x08/ji M\x0b\x0b7\x0cY\x08x\x08!_,m5g\r\x0c\x08\x0b?x", ' +q\x0c\x0b'), [25])
    def test_case_210(self):
        self.assertEqual(pattern_match('y\n,-pm+iV(\x0c\x08gq\x0bI7}\tyX\'4H\x0c{mi`~ 5aT[;\x0b/[\nLSY7?\x0bIV;cwr\nEv<Ys,=Sl\nL&YL\x08aq<O\x0c2\x084)Hv\ribRsbp-\x0c\r\nh\n \rVu\t"nuT`\tA\x0c3;\x08j4\r\x0b\nz1z8l\x0b*', '<O\x0c2'), [70])
    def test_case_211(self):
        self.assertEqual(pattern_match('dV\x0c=/".\'PjP1\x0cA,.\r\x08\'t\x0b1wh{ddQ{7],\nEJP1&(+;>SQVc[\tOr~\x0c*h\x0bG<\x08*\\^F\n9\x0cduN\\Y@Q+96\r<s(\x0c!\x0c<-u3x\t\tYiE\\~', '6\r<'), [74])
    def test_case_212(self):
        self.assertEqual(pattern_match('t|H\x0b\x0b3\x0b\rC~~\\T\n6s|K\'\tIo4o\nV]\x08\rPb\x0cD?L\x08 5Q%)Fz\\*]9G>bA\x08j:d>\nr\x0bTvb#\x0c?\x08%&q/\n@f\'\nf\r"\x0b\'=\x0cfT=k~Jgp{\rGjfs\tb\x08\x0bo.\x0c&Z\\\r@\t#\'6\x08 oYxkm', 'T\n6s'), [12])
    def test_case_213(self):
        self.assertEqual(pattern_match('+Xj=gd\tYB\x0b,NdGJT,ZY*\nS*{\rW67Wjc=:\x0c+;M\x0c\x0bO\x0c|cK)F>B\x08@S[A,g\x08I\t\x0b\x0c', '\x0c|'), [40])
    def test_case_214(self):
        self.assertEqual(pattern_match('@\x08]e/]SaCP;\x08\tVVrv5`qAHS_v\nr\x08,hfw\x0cc\\L}\x0b4-MdX/f7ZL8\r<vD\t\x0c@ \nzD*\nexQPb\tW\rA[BOe<Ca\x08\x0cr;W~\x0c\x08ICt]1cNDl ', '\tVVr'), [12])
    def test_case_215(self):
        self.assertEqual(pattern_match(':L=iG(6\nF@*`&\neD\x0b|\x08u\t\tlk\x0b=kv*N;\t7/6,A88I\x0bs\tG~Nx9\r\tJbFzd\x0b%\\\tiBravo{p\r\nN\x0bb\\\x08\t;X+\x0bT\\]#&I\x08i@J(\n~qe"\x0c\r\\u>\rdaC9^\x0b8\n(5C', '@J(\n'), [87])
    def test_case_216(self):
        self.assertEqual(pattern_match('4x"k?x{lacgY\tB T=&Cx~VA\r7\r{)v?l\t\'h|\n*q\t4UA"TrT\x0b=vQq0SpB\'\r\n\x0c]\nSkovQKoH5x.\t\rp\x0bd\x08\x08P\n,!B7\rMl\rQn4a1Hf4!VLJ\x08`A\r8>\x0b<xi\\"pW', 'q\t4UA"'), [37])
    def test_case_217(self):
        self.assertEqual(pattern_match("_l|\\\x0c,ze0\x08\x0b:eaViO\x0c'|CJ\rP\x0cMA{10m;5w8 CKQ7`3\n/W!96m7}5_Lj#`V[_0IL\nn\x0b4NtB%\x08DxDa", '\x0c,ze0'), [4])
    def test_case_218(self):
        self.assertEqual(pattern_match("Z&K,6yZl7m\t'{4j\r\x0b\x0cG\rV:q`9<#O\x0b>\n\tR)-7-f~FYtM6\x0cb`G\x0c)*(B(#\\>g\nnF\t\twe\r*?h}G_C\x0b\x0b%ApmbmR\r\x08dx\x0cOAB=\x08\tp<5", 'B('), [52])
    def test_case_219(self):
        self.assertEqual(pattern_match("'g^Gd\njFm1\tt\x0b\x08Yp-G\x0c'Kg\x0cV%\x0b8qpv-)F|\x0b\x0b5pzG'l(\x0caIt\rO\tp\x08~U:(y]lBv]\r\t]v/\x0cz,e\riqq\n`;LVdT\x0ce@&zPP\x0c\n?pEJK'{I\x0cx_", 'PP\x0c\n?p'), [87])
    def test_case_220(self):
        self.assertEqual(pattern_match("OL\x0b\\`#fYC2K^qCB|6eyy8])YH\x0b~\rF;l'k\x0cpBx2,}(\n(\x084NF\rE\x0bT(8}\x08^\t7DG&gqUiT[Y:?m\x08;u\tQ\r\rJ 9w\x08uN\x08A_\tQF!ul ,", 'T(8}'), [50])
    def test_case_221(self):
        self.assertEqual(pattern_match('\n\x08k\t\x0c\x0bt_W_4}\x0bG\r_@o7r\t?S`;,X\x0bPp`hL\n3{}L[d0%{b1kNc\rf#1i3?|6()/NYetG-.\x0c;\x08N6D2Ib%x~>L\t\x0cabE=}EIYK#F_\x0b\x08\x0b*D\x0cYZXL:fS\x08Wg&\x082W', '_4}\x0bG'), [9])
    def test_case_222(self):
        self.assertEqual(pattern_match('ZPZ%gN;\tc5mdv;*\nWn\t\x08g5^<mo!%\reL\r2^\nu^fg\t^Xr9\x0b:J\x0c\n-,PO!|F\x0c\x08BL[g\x0c\x08g17', 'PZ%'), [1])
    def test_case_223(self):
        self.assertEqual(pattern_match("AiT_[Vxg\x0c\x0b23\rCyc]_l0j\x0bN>\x0b(HP&fX\n3jdYqE'\x0b\tS?\rn\rv\x08N.;KK!\t\n^C/\r4&r\nmUC\x0c\x0b[sEzn\tj\tmeO5\t2o<\x08=#5f[,\x0cWf\nH;[I%;", '&fX\n3j'), [28])
    def test_case_224(self):
        self.assertEqual(pattern_match("t0\x0c'*[>cY.\rUP\n9wZ\x08|j:\x0b\x0c{<\x08#'z{.\tBjh,#V\t\x0b\x0b\rzn)\tf17}:i_y}c]\x080b9(S/8wp\rM\t|:E\x0c61R\x0b\r=C\x08}\\o", '61R\x0b'), [74])
    def test_case_225(self):
        self.assertEqual(pattern_match('s7zsd%2\r`mF\tc\x0c+\x0b(}zP\x08v?((HAHak94\tF2bfP\n%2n\x08\x08,r\nh% &t|pg0Qtn*(,{/\x08J!Xai\x0cr\x08', 'g0Qt'), [54])
    def test_case_226(self):
        self.assertEqual(pattern_match('\tXaP2va\x08\n\x0c<k*\nEq;\n\x08:/h\'p<Hq\tf9{GD;ZJLUE5z5\x0b\x0be\nB72\\\teKO\x081m\'\t\x0b7??\\..LLF6O\r_XzY. "Ao1E\x0b\x08(5\x0bWd8\x0bPwz\rXJS', '*\nEq;\n'), [12])
    def test_case_227(self):
        self.assertEqual(pattern_match('un\x0c-kW+k[16b\rfqx,Z\x0bc>9\x0bZ<tQ\tJ@&Hr/HFJ:F>pqD\x0bdi\x0b[/(<\x0c\x0bcF^j\t7\x08L~\tnm]L=\ra%l=d+_#a9e0\x08/~^\nH:h(,Si-n=\x0cZpV_\x0cw9(wbQ\x08=*', 'nm]L=\r'), [63])
    def test_case_228(self):
        self.assertEqual(pattern_match('\x08U%pn\r14mXoE2Qg*p)q7\x0c+v!sY\r,\'FP\tBVeef<u";OR,G"\t\x0cdmY,\nMN(\x08vt"S\x0b(y5q!?wIFk^Fl\x08^u-{', '!?w'), [66])
    def test_case_229(self):
        self.assertEqual(pattern_match("G\r\n\x0bK_\t\x0b\rr\rGQQhK\x0c7E+(\\+\x08`xhi\n\x0b<Q*Z\x0bh\r0\tZ\x0cJ\r^P\\.\nnvCb]2\x0b\r\x0bGAK'\x0bKj6N}K1wOK\rj'<3>\x0b~a=w`=E^[}B\x0b=eiijpdUF4C@\t\t,6\x08Y\x0cp,W\\\x08\rU", '6\x08Y\x0cp,'), [106])
    def test_case_230(self):
        self.assertEqual(pattern_match('rHHw\tp",3Vfl\t}.\r]xU\taUX\r\tow\td\'\t\x0cn\x0c;NQI\x0b_]4yFV(\tP\nh\x0c\x08N|Ye {-:\x08\x0cgB:\x08\x08]j= 7<DM;?U\ns_\x0cKWA>\x0cG\ngy\tc\x08y~u*J<Gu_', '*J'), [97])
    def test_case_231(self):
        self.assertEqual(pattern_match(']\x08\n9_}e\tZ\x0c9Tw"\x0bp-\x08L\x0bnV\n\x0c0E_\t\nPR&O%\tK3T\x0ceJ%\x0cq<aJe^Y\t|*z@CE)\tA\rOH40lo\t&88yzz I[\x083', 'E_\t'), [25])
    def test_case_232(self):
        self.assertEqual(pattern_match('%np!|?~\x08q--.C\x08m%1\x0cI!A\x081\t2&/QbjwE\r\x089\x08Hp\x08\x0bt+! f\x0bA7\x0b*uFsnK8hfo9>cR(Av', '9\x08Hp'), [34])
    def test_case_233(self):
        self.assertEqual(pattern_match('DzD\x0br`\x08\\9PRRH??%\x08\x08XuHJa<\t^uvrUD\x0b g\t3F;!M0\nogE;\tDKeI\tDq][\x08\x0c\n3q\rJAy?fdkcx`C\tZhDtB\tFH\x0c9q%I~&l?%fB\rp', 'PRR'), [9])
    def test_case_234(self):
        self.assertEqual(pattern_match("fE\x08k\r\\oP\x0bK\x08f\x0bxN\x0ct'N+\n\r\\OK\x088QJzy2R\x0c;Rk.)~G\rLqvnX\x08/LE4:m\x0c\t|\t9ww9\nN\n4P\rjv>~R\tXf+gM\r\x08\x08Sm\t'E'bie\r\x0b\x080[:ph\n:M\x0cRC\x08\n`&{%.5IwVX\x08\x0b", 'Sm'), [82])
    def test_case_235(self):
        self.assertEqual(pattern_match("X]+5\x0c\x08\\,y\n<kEpIDktfZ^;(\x08s(Rbi?-w\nD\tASGXc}\x0c3}@n\n~(#J1\x08\t7f6\x0c7=\t+(}qg\x08jc_'\x0b,eNGnnfwg&Z:O\rn?j\tNIR", 'c}\x0c'), [39])
    def test_case_236(self):
        self.assertEqual(pattern_match('YI6\tw!(hF47z{jc(Fe1oU<{}X}y?\n6\x08fCZ&\t1mhMD!HKWV^[!JI\rzK.\tD\\4w', '1mh'), [36])
    def test_case_237(self):
        self.assertEqual(pattern_match('\r\nQ\ruH^\n__l9.\rH0orPcQe=to17\n7K\txg73=x*\x08\t{0F{R\t.W(\x0cBoYfJfJR{0X#EUHN{OcYT&9U"D(_2/w\x08m"\\_b\r9So|\x0bca/\\\x08L\n8YSE[2', 'to'), [23])
    def test_case_238(self):
        self.assertEqual(pattern_match('@][m6\x0b:\rE\x0b**!\x0b\t-ht`;f)\x08\tD%@3J\x08NtHHG}7/(n~\rKv\nY\tKA_ er51SP7zx\x0b4N-|tAz\r;Ifz\x0c\nUiub\n)^&5x|Hzt.\ndw&})\rV\x0bY\x08Te4h', 'V\x0bY\x08T'), [97])
    def test_case_239(self):
        self.assertEqual(pattern_match('E27\t\x08YE\\YaO"m:\x08C5]/,rR8U1\\FIc\x08RMH\'|\x0b\x0c\x08\r8D\nL^%\x0cceZa2|Oik`"]\nM', ']/,'), [17])
    def test_case_240(self):
        self.assertEqual(pattern_match('\x0c\x0cc,2\x0cC\x0bxHtDw>;59\nWZ\n+#OB3I*K\x0b?\r#Yv\rVTH0\x08dZ0eL\x0b~*\n_\x0bt\x0b<9;}mi\t\t!a :E:[Gdc3v\n9#IxG\x08"ID y\r_\r9U\x08YiX\tI% |y}N\nmuUg[Eun', '#IxG\x08'), [76])
    def test_case_241(self):
        self.assertEqual(pattern_match('}M\ng\rF\x0bo8Pu\r*;9\x08yh#^X3"bZFn6\t\x0bli~;\tmtS\r%yn1a#GjN}[BQJX\rj\x0br:M\tp)[a&\np\\cdpj``^?\x0b3\x08foz.\\C', 'foz.\\C'), [80])
    def test_case_242(self):
        self.assertEqual(pattern_match('9HE Yk/@2~\t4`j{VV9S]4d]iC^iZJe\x0b\r\t"wu\tdh`z8m2K\'M{\x0c.K:itCWO:I\x0b;?"G\x0b&6qx"H\x0cwt.lP qx)\x087,1[w|iZM,<s`K\r.l1W\x086sT4cH', 'x"H\x0cwt'), [68])
    def test_case_243(self):
        self.assertEqual(pattern_match('\x08,G\rw\t\tr^\t_\x08~7TJ8jseSPX`^<L\x0c//h\x08\x0c/\x08c2\x0cHuU\n1"\x0b\x0c7e{S[k\x08\x0b\x084\rgRLD%LV\t\x0b\x0bn+x]\x0c1\x0cS\t9\x0cG03\n>\r\t\x0c)4\r\x08w?rVy\n\x0cG6*En;H\nm', 'PX`'), [21])
    def test_case_244(self):
        self.assertEqual(pattern_match('I]+\x08~Z(YWj\t\r\x08x*n\x0bG*_C!\r"c0\x0c\x08R!JIu}<o.-\n\x0clbX+a16\tJ@I L\n\\\x08Il<\n\x08}"ul|\t \x0b*ob\x0c\x08o`,\x0b?VRZ\t\tRl\':\'S\tw<\x0b7%Yzmj[c6P\\&\x0c4H-\x08\\O', '|\t'), [65])
    def test_case_245(self):
        self.assertEqual(pattern_match(',\x0bP4\x08\t?",E"UO!\r,oI\x08JoXz }-FpZ&dHFj?Y.\x0b\'9a/\'ts4m[\t\n"Vjv!\x0c\x0cOnr"\\"do%f-]\x0b', 'Vjv'), [51])
    def test_case_246(self):
        self.assertEqual(pattern_match('4Bkyd-ch"\x0c\x08">Zt!\x08WJ]Q\x08s1\rv5\ru}DBw~Rl\x0b)8a\tH8>\nR\tu|_["7n\'\x0c\n|\x08A7>e~\x0cXN\tDHYT\x0b\to\t5\x08\x0ctHWI', 'Q\x08s1\r'), [20])
    def test_case_247(self):
        self.assertEqual(pattern_match("&/7Bp}p\x08F>x%\x0b\t\x0c2\t\n7JG=\\\x0bJ\n5\x0c)h\x0c\n<>^<fY\t;\x0ctt:up\x0cd,Tl:f\t@i\rl}'|?J\x0c+9tJ4P;q0kd'F/L~DJ\no}]P\r\nL\rOvYm,5>U*'", '&/'), [0])
    def test_case_248(self):
        self.assertEqual(pattern_match('n7j\x08!C;y6\x08\x0ciZ*(&\x08Ai?Fq:kfW;e!|71R7%L\r5%lA3Jg9"r\r7y\nL=)S\nB;Ps\t\x0b`:X\tvnQ\tr}bS_?.l\ty+<-\x08|\\SW\x08e=,yFEL q3S0\x08k\x0b=\\sx)1\n\toe\x0bY', ',yFE'), [91])
    def test_case_249(self):
        self.assertEqual(pattern_match('Cp5z<\t\x0bazg5"APZGE^X\x08#-)\x0c\x0b2U\x0cv\n\nH\x0c&hC`m02:\x08>\t+\tH;\tqSMte+\x0b?%4\x0c!\x0bhDC\x0cx"E b\x0cLDh1Rr\x0c\x0c&w&:o(h\t]zAC\x082{\x0c0_B\r\x0cl4!T', '(h'), [85])
    def test_case_250(self):
        self.assertEqual(pattern_match('-@n,@2SGL\x0b@\rK\x0c[@\x0bC9{d\n\x08\x0cW\x0bld\nTR`!\n\x0c("\x0b+P!]c#\x0bB!&C^Eg rP\x08LMo4\rj~aq2\x0cQ.p\x0cV>ZCGi2\'oo\nNS*\\Y\nK=\x08<5r\x0c\x0cKzh\tpi\n-l{@,[\x0baly&yv7\t\'', 'pi\n-'), [100])
    def test_case_251(self):
        self.assertEqual(pattern_match('LVF\x08o%\r\tb\x0bAn\x0bxldi\'\x08#\x08J8\t\x08em#k\x08&\x0c\\W!\x0bH\x0c(iXfC P\tdY ~Mu}\tie/a&XM!a{3gb\t<p)b\x08X"n?\t`Be&}N\x08\x08[[N\n', 'J8\t\x08'), [21])
    def test_case_252(self):
        self.assertEqual(pattern_match('5Zkf*\x0c^D@G\n&\x0cuPfW{LXDn\tx0bOb&\r\r\x0c\r8\t.FCz|t}k\r\x0c\\tw\ne8Z:n0K&LTg\tH\x08BUKC}L}h\x0c[{# qDF>\x0b\x0cJ\x08-EVw\t)\t\rps\\EG\rT\r@F\x08\t6,\tvZ|DW*oT{k', '>\x0b'), [79])
    def test_case_253(self):
        self.assertEqual(pattern_match('Gqht\t.\t\tt\x08SjN\x0c/&U\x0c<=\nD,Ptc)\tI2\n\t^j=W1:F\t#-\x08&A5+<@}\x0bxYv\x0bDe],;H<hX\x0c.\x0c-Ct&WNibC\x0bo\x0cS\nGY\x0b\rN7\nY\np\n6dKF+Kyl', 'S\nGY\x0b'), [79])
    def test_case_254(self):
        self.assertEqual(pattern_match("k5<<kl\nPRD(\tCRx\r&\x0b\x08sU7y0K?\x0cb(\nd%Lk|-'\x0b/EZMSfsrx8Rc!\n.g]EKbQlq+e-\x0bANe\x08m\t'\x0b-", 'y0K?\x0cb'), [22])
    def test_case_255(self):
        self.assertEqual(pattern_match('(f)i\t9H\tpBqKkD\t2U<i\tf+Y\r\t;Ax\tYFF-,r\tHT*r\x0bw\n\t +~i;G,Yk&<4ROq852U8:h\x0bh{XXZ%\x0c:Xkk\x0bJ=\r{ClWS%\x08;sa\x0b\\#&Ed-', 'YFF-,r'), [29])
    def test_case_256(self):
        self.assertEqual(pattern_match("O9R_uCwTpe\r!'^C\rGx\x08\tZ\t\tpUb4xRgU6-1EgZ=,?{8L\t};^Z\tW4%\x0b!M3C#:\x0c\x08", '!M3C#:'), [53])
    def test_case_257(self):
        self.assertEqual(pattern_match('zO0dCe\naA({=|xq[v%2u,( &rr[C\x08:_*0\\z\x0c\x08\\\x08\nuX282\n"\x087w&GB{0SB\x08Ty=nQp\x0cEeY#duk_3yg\x08yye?\t', '=n'), [60])
    def test_case_258(self):
        self.assertEqual(pattern_match('n;.A[v\tSkjP[dB3O%Z1\x0bS\x0b\x0b}\\RB\r~\r{\'4Sz,\x08f7Bx|=Gp\x08(\r\n\x0bVT\rkF%#Q/}B\x0b"!q\r\x08\n\x0b9\tG9@1\x0cdC?;f\r\x0cYzg', ',\x08f7Bx'), [35])
    def test_case_259(self):
        self.assertEqual(pattern_match("S\r7kCL5MDZbZ2oiS`v\nF'CyD^\tL3\x0b\n\tg?RUt79,\\CWnV\nK}M\x08kgl\x0b/=~qU*;:[\rfAs\r\x0cJe/\\}@\x0bO \x0bE@|d\x0bu\x0b`\n0q\t;\tm", 'Ut'), [34])
    def test_case_260(self):
        self.assertEqual(pattern_match('i8GMkn;vM0]#hB9\x0c-5\x0b#@SJ3\t4o9\rW.](N\t/i"v\x08^T)\x0cf\n7\rI[Fr.^\x08a\r=T7.L*\rY!m', '#@SJ'), [19])
    def test_case_261(self):
        self.assertEqual(pattern_match("e&\x0b4Y\x08Jpa+@\x08*\x0cdfDWM2^Morvo QO\td+gXe_Ll\x0c:BK1juD\t&b+oS=wzkN\x08U Gd?1OSAR\x0b+*\x0cU\r%1K^<\x0b\x08yN B>[\x08ZN\x0bAL'00VA\x0coP\x0bSZnYl", '^<\x0b'), [77])
    def test_case_262(self):
        self.assertEqual(pattern_match('\x0c[Xsf\n6l\n\x08b6\\ -v\tM\x0bN9XU8K,\njBJ~|8 %\x08\rekv_n|\x08%(=7\tm#He\x0c\x0b\ro%W\x0856\r\nnKI\x0b\t}\r\x0c7-@rB\rG\t\n2L\tcWL{*\nfL\x0b\x0cD/6\r\x0bC_2)xp8p\\T:<X]\n,_\n', '\tM\x0bN9'), [16])
    def test_case_263(self):
        self.assertEqual(pattern_match('Fsl\x0c\t"{n\x088P`\re@86b1E\')_6,-XSJ"\\?4cW*\x0b2m\x0clVWLPtTa{=eUa1qI\'Cwp\x0bM"t<E\rKMd\x089\']Y\x0c\rqYCt7De6La30.*\x0c\x0bQ\n\r\r:\x0cf\x0bn2\rh1&8`:\x08\r (\n@H[u', '\x0c\x0b'), [91])
    def test_case_264(self):
        self.assertEqual(pattern_match("u#\x0bO Xa\tr\t\x0ck.cU[5c\t\x08]5dy7-\t?d4>0aI!\x0cPN\x08_b\tJkCjbQe7bLY\r':\r\t8D\x08\x0ci8Oe4\t`I4H'4'Ky\\'K_~e3\r+\nzC@=<\x0c[3T,y}im!Tw", '\r\t8'), [56])
    def test_case_265(self):
        self.assertEqual(pattern_match("0_j!S\x08\t\r7\rD5y+\x08\x0bH2ej\x08lt\x08U'\n\t4^\r/[\t`\n9(\x08\x08TeK\th\t^n\nxT\x08kH&2}[u`'1@2X\rb\x0bSk<\n`+Ahnypj\x0cBjp\\bH", 'eK\th\t^'), [41])
    def test_case_266(self):
        self.assertEqual(pattern_match('{VmF37#:jC?O))v,GP[\ri@BeFfWOHSXZ=A|\n\t34EfAcTQ@\x0b2\rZZ)5J\r|%LgXn\trO0eA#z\nw \r', 'OHSXZ='), [27])
    def test_case_267(self):
        self.assertEqual(pattern_match('0\rZ\x0c#\x0c%rgQ4g4&\x0c"8P/h3|DJ\x0bI\r\t%4\tg4kp<(#m: De8&]21uTW>&\x0c\x0b\nL/O}h}\x0c4R|\r\x08/', '\r\t%'), [26])
    def test_case_268(self):
        self.assertEqual(pattern_match('Ei6\r\tFXE-\x08}:X\t\x0b\n41_}!<\r\t{C\t*M\tx\n@\x0cvG\'D\x0c^>O6\x08\x0bA\x0c&\tFA:QX\r\txQyeN"neS`\x08s!\\?-c\x0b', 'XE-\x08'), [6])
    def test_case_269(self):
        self.assertEqual(pattern_match('i!\tGy\ra\x0bUUeE<r\x0c\x08\nH\x0c\r[gAK[ZD%Y};w/\t@S?"\x0c~\x0c%I_:B;\'y@k\nC:[\np"\nt-rH|5X\tBl.C\n">Bbdz)!y', '\nC'), [51])
    def test_case_270(self):
        self.assertEqual(pattern_match('9\x08M__|lTTM,\r#0%zH\tt\x0b+X}1\x08Z)-kfV2H\t7-\tjn|%fR!\r\x08SeN5\x0c\re\\+\x081w}G7\rabI@aS|?j09D(Th"\x0bi\t0\'j\x0c"\x0b)', '2H\t'), [31])
    def test_case_271(self):
        self.assertEqual(pattern_match('Y\\&LK~"%_D43\x0c")z]N!A5\x0cUf\x08D%\t\x0br0*\x0c~g>d\x0b\t#?k\x08~D\r \r7tx_\x0b1e"\td<x\x08\nEh\x08pBn\nnH;P[`L8<)\nQ>!bd\n\rq\x0cm\x0b', '\x0br0*'), [28])
    def test_case_272(self):
        self.assertEqual(pattern_match('\trW\t\x08zT\x08m\t-Dwc][T{A[W#\x0c\tCH%~`p|N:\tV]}\t\x0c%tn\x0ck%U1h^[,\x0b(\x0b`i6\n\rHQ\x0bcgHo\rPH\r9', '\x0bcg'), [61])
    def test_case_273(self):
        self.assertEqual(pattern_match('>lX\r1CL*\rs.9\x0b<B\t\x0cj3{7j`c9\r5\x08=w<\x08cpnX\x0cdx]^k\nN\n; _V{Dp\t^UrusW i`M\x0br!u":\x0bgFv\t\x08~" f(xhP\n,"\r\r\r*a.s515CB|;w', '\x0b<B'), [12])
    def test_case_274(self):
        self.assertEqual(pattern_match('=L-qF#pb\x0c{u50u:]DMp\\\tiB4Y;rcrj\tND8rAT=3OcBb\nyp_<g\x0b"EVBh+>b`zJp>+o\x08\n\nZ\',G`p9v\x08/\x0b3&WCt\rJ]5.GG\t\r9a|IA4w^\x08]"vl]\x08{\\DC85;"O\x08', 'G\t'), [90])
    def test_case_275(self):
        self.assertEqual(pattern_match("\x08pb:F^r\x08)\n;\t\x0bxQ~V&O7?qTA<J<\x08:op\\\n,\x08\x0bt.PvP,jpD\tX282)\t8&@=I\r<u<5\x088l')a", '28'), [47])
    def test_case_276(self):
        self.assertEqual(pattern_match('7MlKX;^\x08  Sl\x08\x08*ln3!3-i\n&H#\rv`\x0b%A[\x08E.Xn>+N[Hw[e7Xpj\x0c\x0brOT\t>sxJ<S\x0cMa]DVO', '\x08  Sl\x08'), [7])
    def test_case_277(self):
        self.assertEqual(pattern_match('#Ec=p\ni\x0cAQ\r!Nq\x08AhW}AI"\x0bB\x0b{M0z!@\np\x08\x0c%\tY7l_IO%%)\r\tH059xwe(:\x0b?7\t_B9G?L6vw>\x0b\n{h*\t\n7K\r\x08v\n\x0cu\x0c{x[%]7.<\x0cD\r[', '@\np\x08\x0c'), [30])
    def test_case_278(self):
        self.assertEqual(pattern_match('{lr7_n@\x0c_r\x0cC\x08O9\x0c\tm\tor&\x0bSK&Mne\x08Ihh(bKuh\n8\x0c\x0b\t?duop:\t\'7\t\'B"7w(<x6!Q:Y(2\n\'.', 'SK&Mn'), [23])
    def test_case_279(self):
        self.assertEqual(pattern_match('\t6\rSI7#HnIp\x0c\x0c-%\rR%}FV\x08 \n2J\x0cP\'\tY?Z\\\x0cy]5Q%Ut"5uX\x0c-VM\x0bm\x0bFWQp\x08?aHk\t\\51kM\r>\r\r}\x0b\x0b#q@mJ8u{gh%\to\tgFMc\rDQOpE2Ur', '1kM\r>\r'), [65])
    def test_case_280(self):
        self.assertEqual(pattern_match('\tTd{q)\t A\x0baN:st\x08ebh+Q}&W%m\\x/Hy9YT\x08nF\rt|d\n\x0b|5I?\x08\x08\x0be7ko\t3Wvjd\x08)', '\t3'), [54])
    def test_case_281(self):
        self.assertEqual(pattern_match('{\rv@.("[]qO5(Z>\x08:y~x\t;^]&3\t0yS5P\x08zyqkoV6M9O1I&\tx\r+"\rI:g/Et(=\x0cR|7\x0c\n{\\Tl\x0bGN}k~\x08\x08c!n\tC=Qt\nQpUH\x0c-r]GP/bo+as\n', '\x0c-r]G'), [91])
    def test_case_282(self):
        self.assertEqual(pattern_match(';oc?a=\r\t[8Q=guZKyM9r]\nxBk\x0c3@vzhS(p\x0b:QG#a_TfBb\r*Ae\x08"B-\t0\tbg-~(fv9oS|&\x0b \te7\x0b1;\x08Z`*I\n;0X\tGb\x0b\x0cu\x0b|4\trpLU\ntV%IF\tT0EHFi5l', '=g'), [11])
    def test_case_283(self):
        self.assertEqual(pattern_match('\ry\n\tt@\x0b\x08H)@tk1(\x0c;Ei-\x08"A\ruJRrS{]\x0c.{dT*=PnX6hZ7\x0cT\rWG\r+;] U{e-\n?83uY\x0c^1\r\nY>l"', '@\x0b\x08H)@'), [5])
    def test_case_284(self):
        self.assertEqual(pattern_match('s#BLUu3X\t\t4y\'7%]YT\n&#q\nB;(b2\t\x0b7SoUJ2L_\rn]N"x6flg4H-\tP?\x0b\r\nR\r\x0c?r\' O\n`p<1*7K\tbpY\x08\x0b9', 'lg4H-'), [46])
    def test_case_285(self):
        self.assertEqual(pattern_match('+gdI@3T&XMrx%wO8(j\x0clDUOr6A&n\x0cC1CdOu9w\x0bK"Sas*tHT}*PFbCw`[iDN&RRx', 'gdI@3'), [1])
    def test_case_286(self):
        self.assertEqual(pattern_match('F`:"P@uM\t:9B~g\x08X\tw0\tz=\x0b\x086|\nq,mA0UH\\Qk&:mD.f_Uw\n,-c\x08X\x08H\n/p\x08-*IMdNXNZ5Om[w)\r\nFvcR \x08=/y!qO]', ' \x08=/'), [79])
    def test_case_287(self):
        self.assertEqual(pattern_match('\t\'}b.}Zy&\t~kR-6\nGqvuZUMb{ hm{}"\\U\x0bc\t\'Ua0=vB3BR<\rU\x0cV\x0bsNv\x084\nT\x0c^&\x0cu.7J#WF(S|=\ta\\U"\x0b\x08\nJ\x0c,n\x08S#<', 'y&\t~kR'), [7])
    def test_case_288(self):
        self.assertEqual(pattern_match('Y8PTY/8yZ%[5(s})YJ!\x0b\x0c\n_1~xa`7>_\x0cP1:Qk.s&`A9\tJA\x0c\r=H-1;#\tV*_\x0c\tYD~_9+5=\x08?`\n.E\x0c0F9!8\r{Lb4LHV|aKGT\nJ', 'a`'), [26])
    def test_case_289(self):
        self.assertEqual(pattern_match('QP\t+\\r*Zj!W U9"^8e1;\x083<3j\txTCPm 6mC[:m)R=O+TVwI1h?iqP\x0cy,KwFa\'Pc(Sk<NA\x0cjQ)EI?8G\x0c9q@P\rVuzu', '8e1'), [16])
    def test_case_290(self):
        self.assertEqual(pattern_match('Xx1\x0c59k[kC|}.1\t& Nlyx\x0cfWB{zF\tb\x08K&YY<C1OseM+f"3\x0bH\\#\x0cL\x0bS.\x0c\x0c3\t"N#p.\x0cF', 'x\x0cfW'), [20])
    def test_case_291(self):
        self.assertEqual(pattern_match('wUNmN=OX7-s\':bD^V\x08nfRcc07J9\t\x08z]!\t\x0czp8,\tk.\nQo\x0b;6uE:+D1"\x08`B(RC\r8ndA\\d`wG2', 'p8,\tk.'), [35])
    def test_case_292(self):
        self.assertEqual(pattern_match('\']l\\^x\x08{lt102uK/cs-Z&c\x08k\'\x0bA?At3s^y"H\t\r\x086Ft*GP!\x08R#\x0b`AOJ\x0bkp`C\r|`N)KQa', '`C\r|`'), [57])
    def test_case_293(self):
        self.assertEqual(pattern_match('|yYbg{*+Z\x0c-8A@W\tEb/\tp[C\x08\x08[5jXe Z6zD\r7BO[\x08 2uQ`\x0c!\x08\tg0=|<[Qv^\tuZVG\x08SZJ\t=?#"D\r"\tDNsU\x0b:8t6o\x08', '*+Z\x0c-'), [6])
    def test_case_294(self):
        self.assertEqual(pattern_match('-C~fC\r]bj7\r\x08k:\r]@TnG\t6BcE\t\t=3R\t!^D}D"u\tzW*Q\x0b\x08rxozg\x08|Lk.\rm\x0bo\x08esu%/8XEs\tN\x0bx\rjM1YY|3!nb&a\t\rqpL0"7J4ydu', 'g\x08|L'), [49])
    def test_case_295(self):
        self.assertEqual(pattern_match('yiz\nIMQ`1"k\x0b\x0blt\nn\x0cQ\x083s&N0q\taNr:dWZk-hc\x08B\rsTD.\'.:>[\nY;\r<;L\n\ns:~!\r!k\nH!5b^x;4wW', 'Y;\r<;'), [51])
    def test_case_296(self):
        self.assertEqual(pattern_match(',\t\tT,Ro{p\x08tBu"5t1\x0cK9B:\nW3poDb\n\t*t\n|i?lVc\x08a ^\x08M/^\x0c\x08c&{T\x08w0\tFIDT1\x0c?AY\tn+\tcE\t<mug\x0b\x08\x08\n\x0cDf\n)opN', 'T1'), [61])
    def test_case_297(self):
        self.assertEqual(pattern_match(':Ex(~zzX7.\n?F@),gYt\x0b#Xtz<\\\t_\x0b*9*R\x08;G>m\n\x0b\x08\x08\x0b\x0c\x0b/YI=3 o:P67\x0b9\tTb[Nr6N]x', 'z<\\'), [23])
    def test_case_298(self):
        self.assertEqual(pattern_match('S~!J4m<e\x08\x080x!g[](x]!|uk%\x0c"F\tgN\t\t~(#\n\\i&Zc!"A?`(8tI8DZJ!HpRx3TP3^\x0b\t0..PJw', '\n\\i&'), [35])
    def test_case_299(self):
        self.assertEqual(pattern_match("\x0c\n\x0bby\x0c}KcJ\x08'\n-N\t,7lB-a~X\n:6Ww/4\x0c\t\t\x08T\nSr(\x08iR\x08k4h;\x08.\x0biN[\nj:Edh&\t4\x08`C.(P/\n]O'W7s\r\t |mR0\rGfuj0\t4\rJdLrO-f }~", 'Edh&'), [57])
    def test_case_300(self):
        self.assertEqual(pattern_match('!\x0cR3D`\r xfz^\nGT\x08q}0t78o:}c\x0bNS)-\x0ce{(R;^_8[\\GPiggJCk58/MP8VZ~:ce_m*EaR[K)?\r\tT?\n', 'R;'), [35])
    def test_case_301(self):
        self.assertEqual(pattern_match("\ni\nz\r7\x0bqFO\n':bH'\x08[{nFLN\x080I<\x0c\x0bF\n\rpIz+kf'O0x\r\\E1)U\x08\rF]&f\x08F_99Pi\x0bE8\n\x08H", '\r\\E1)U'), [42])
    def test_case_302(self):
        self.assertEqual(pattern_match('xgu\nK\x0cl,9UGM\tv;<,\\d\r\nehG\\1Ep9- Sks,lqiO\rXAbhA4\\X\t|u\'\rpsY~S{r^"~v^C=\x0b|q#\x0b\x0c5d\x08u8>\x0b@WoVrDxe\\.Y\ruN3\x0c|5:B?w`UYE8\rKH\\\nZ(Pe+\t\x0cn', '\nehG\\'), [20])
    def test_case_303(self):
        self.assertEqual(pattern_match("vfI\rF\x08jS&]\rz~w8UkN'\n\x08&!Q_c\tu#:C8wEx\x0b`\x08)\x08UjlKK\x0b0bFpi\tP45\n#b}\x0bjeR\x0ce?>Qm*\r\x0bKb`?h\x0buZV<\x08/:`T\nknYV-N", 'jS&]\rz'), [6])
    def test_case_304(self):
        self.assertEqual(pattern_match('z;wS\n2xLORW1JkQd;{[!)J  <6,+G\x0bOf"UNJLLVs\t/Aig&|d\x08xR\r\x0b3iP*wH\x0c/]j8lCF\x0b4>O<E\'L\'\x0c!FZ"5IWl/\x0b\x0bjzOX3P&;bM:%"*', 'd;{['), [15])
    def test_case_305(self):
        self.assertEqual(pattern_match('0&Y4E\x0c8"n\t}-\x0c3\r&"Zi:B\x0bRitc}=@\no\r39IkMZ1|<b\x08\x08>\t<c\'1\x0bvAy\n+T:P[Yi9\rE\\2f\n9z\x0b+Ect|R\t\ncX_o\x08\rT:-&\x0cPsmq', "'1\x0b"), [48])
    def test_case_306(self):
        self.assertEqual(pattern_match("arS\x08`nW#L|MN]Lh|kg}.\x08KNITA^*\n\x0br6'[1{' jZ\t\rf\x08j!\n\x0c)^k qX;`]qe[a\r&", "r6'[1{"), [30])
    def test_case_307(self):
        self.assertEqual(pattern_match('~aH\rp=M>^]"\r\x0crm\n\x0b\x0c\r"\x0c8j%C\\QD1,p\x0b\\XvjleMkN\\\r\n@v.<>\n\t;X\r2b:"\\Y\rm8{S,n\\L\x0bxX\x0c9{(Hzz#us>r8a^I\r\x0b:e', 'us'), [80])
    def test_case_308(self):
        self.assertEqual(pattern_match('@E\rt_k1\nk;[~x\rJ0ZkMATPd\x0buOTx\r:\x0c=\x08 \x08jyz8]Q}*G4V}1Lk\x0byf[\x08\r\t=\rx<XaQ\r<\r\n\x0c', 'ZkMATP'), [16])
    def test_case_309(self):
        self.assertEqual(pattern_match('\x0b\x08Ku)ABN_!Wj*.]aXNGZi\tks:!-<kA\n\n;LrO|)}2d,f+VRU)\tr\x08?YuF6nsMZYE', 'A\n'), [29])
    def test_case_310(self):
        self.assertEqual(pattern_match('`hj}ya\t\n5s746my\x0b\tt\x0bK[6o7G=a(T\rGBb2j\tC r\x0b\r+8?`Ov\t<JL\x0b(bY\n74zZ|jl\\\tZ(3j\t"w=\'\x0c\rH~_\x0cE5l\\nR@1:b\r81"\x0b;^2>?A\x0cI!', 'j\t'), [34, 68])
    def test_case_311(self):
        self.assertEqual(pattern_match('uLM%"i"f}.:yCk@7=h\n\x0b\x08gNE\tf!(f\x0c%`Eu)|?t\x0b9MAo+I>i=\x0b~36o-/4Mkd9%O\x0cp\nBRf/P\x0bv\x0c.[<(!U!W4<f@\tmM=-<{S\'WUEv\t|', 'Mk'), [56])
    def test_case_312(self):
        self.assertEqual(pattern_match('u)P3j[2HT\x0c|NbE.}~ lGb\txFYy\x0bd4*#]UM\x0c\x0cXY]d>\rL\\(\x08\n(\x08N\\4OtxU~\rhM', '4Otx'), [51])
    def test_case_313(self):
        self.assertEqual(pattern_match("ZIpB\x0b>#C~Tg#r\t\r(X\x0b\x0c>6<]@\tc\nR\r+k=xHxez{AaQ\x0bQGh[\tW\x0bl{FTu\x0cD*j|n\n;2IN'\nrE/h-_9jT%!^+]v@\x0cwjW62/JR:|ZL{\x0cc\r}i\\{VI`\x0c3k4u4z\tYM%", '+]'), [79])
    def test_case_314(self):
        self.assertEqual(pattern_match('xfg1NG3MOR`h\t]gG~\x08=|#{L8>cuR?+\nt-7rO\r?\x08Hl{. V22\x08)m(r#y\nF\x08-CBjxT\n-[T>9%O\t\t\x0b!W\n>YFi9PhjI\x0c 1[x|!}^\x08~uh37H# )(^\x0b1vH=q=g\x0b^_N', '2\x08)'), [46])
    def test_case_315(self):
        self.assertEqual(pattern_match("-\tcobc`7e;m~\rEWb%!!\x0b}\x0cXr8([[v\x0b\t\x08C\n\x0cZ\rEN?6Fj54y3=^`Qq}Cd\tBXjY\x0bV\x088k\tZ]\n>B6=50K.\t8V\x0cg[i4pYBW*y7\x08{\n`S,V \x08q'A/ 4l~(/Y|L1\t", 'm~'), [10])
    def test_case_316(self):
        self.assertEqual(pattern_match("z*0P'x\nS4\nE\x08s\x0b\t&`0\t\ne\nNbPD8\x08{\x0c\t\t;kBooeBnZl\tYsk8rO\\;@#i\n[#`X\t>gtu*@S\x0bD\x0c3Xa\x08y>\\Cq\x08\x0biYG*uKCK13#_e\x0cy\tf\tg%9OQ", '\\;@#i\n'), [49])
    def test_case_317(self):
        self.assertEqual(pattern_match("WC\r\\o\rPgWN8~gMp:B\x0c]CEb~\x0bi&D\tBa@BL=>D>\x0b4Bd+0oLK`.k\x0bq2=><rH\rD'#\x0c[De*8\r{A&\tOav\x0b!62,UI\\xJ", "\rD'"), [57])
    def test_case_318(self):
        self.assertEqual(pattern_match("al\rW'v\t\\Q}`,`sm-hG3TT9uO\t\rC/r0VD%S3;\x0c\t7\x08\x08)\x08A'\x0b`%I6\n4OQLl;q\x0b\x0c|ig\t+(\x08,oliRr0~8!\nGzoCnw", '\n4OQLl'), [50])
    def test_case_319(self):
        self.assertEqual(pattern_match('\n\nRu*^J%\x0be6Nh.:l/A&#z\n48{ jM\x0bCn)\nf\n5rb^HzMx\x0bLJ5Hk\nU\x0ctU\'8FI}4PR\r"\r##\x0bU}-Bz\t&\x08?&\nB\n/ji:p<En\x0cK\'Z;\\', '5r'), [35])
    def test_case_320(self):
        self.assertEqual(pattern_match('8U0g`\'n4jWs=\nYsZ|;;\nY\t?}j\t>sE^oOuy aW{NU?0|IVD\nUXnoG]ZjO\x0b\x0c7"0_l\x0bj+AXP\\Ef\t\x08\t', 'G]Z'), [51])
    def test_case_321(self):
        self.assertEqual(pattern_match('?>SScReZme27,RQv=\x0cu;K-SB\\\n3R!T-&\x08%?A\x08N)~\x0bIg 9f\x0bHG;O\t,Q\n16yNY1B\r/A^', 'me27,R'), [8])
    def test_case_322(self):
        self.assertEqual(pattern_match('E\x08\rp%F^\x0cH\\=\tu;\x0cBn^K{>KIO>^\tW\tH(w\x0b\x0c\x0c\x08jC0W\r}y\x0b#w% JIc=FAE]3\x08BxP6Wk\x08~c^K\x08>C9\rB%uD}', '\tW\tH('), [26])
    def test_case_323(self):
        self.assertEqual(pattern_match(':V_W\x08-\r\ne9X<\n!Fy\x0bJ\nI!B(R\x08o/qScq_k%{!"Gb6;KJM\rGc\na%YLVEg:\nI{\x0c8\x0b`\nihQ~s]L\t75\npjv|5M\rjLqFE7oi\x0c', '~s]L\t7'), [67])
    def test_case_324(self):
        self.assertEqual(pattern_match("\x0c~\x0cl\x0c@DfA%\x0c\x0ch\x0cVhWN6;v,I;{\x0bAY\x08Lf\n\t. eh&s,.W\x08jt'\nx_~\r\x0b\x0cfu!d0t;(7\x0bukqJ2r5DN%/9A!i6%/\x08\ne\tr\tD[e", '.W\x08jt'), [40])
    def test_case_325(self):
        self.assertEqual(pattern_match(".d[\\F_*[\nlbli`j=S.)\n\r~&\x08+k]1{ef\nNK\x0c'{*0UFP\x0cyY<JWEM \tF|m\x0cGH}\tg\x08_", 'K\x0c'), [33])
    def test_case_326(self):
        self.assertEqual(pattern_match('@E\nl\rM\x0bE\x0cm\x08#:N\x0bsr/Lx>x94u@*-3`\\L\rV2cbXN{6\n\r\x0c9YwA\r\'\raP\r_YYD\t1\n!\x0c6\x0b5NR1]gPwU\rI+[OGSD,e:0Y4nq|Ra5"Q\nq\x08\n \x0bvNp:vzK<B \naH', 'R1]g'), [67])
    def test_case_327(self):
        self.assertEqual(pattern_match("\x0b\x0cPrf\t5W*l R30l<b0kPFVs\x0c\n\tQ\x08~\tK5\t'\n\x0ccVPW^Afp%mcT&xq\n>hkV/\x0cK\x0c,-{{VPJR'b;\x0b=Y0'u(\r4\x08?C9\n\rG\tY", ';\x0b='), [70])
    def test_case_328(self):
        self.assertEqual(pattern_match('In+T*^3"e\x0c_,.L+|\x08*]taM\r3)\x0b\x08:hU\ruIZ<\r@*NeUR+!+\rvt]\x08cVchU"z\x0c2,87\x0b^V<\x0b\x08\t\n[\x08\tSMjq:k\tPj\t\x0cu }Z{:%0/!P3\x0b}m\x08*{KD1e\tR;)\x08X@t4dr{', ',8'), [59])
    def test_case_329(self):
        self.assertEqual(pattern_match('k\x0c\x08\x0cIah\rF%sw}&f@)\x08\x0cqfn\t<h\r[W= gZc\re8\n\x0byNAPfTYD/Ken[(>>\nK<nD:\r~\x0cv', 'k\x0c\x08\x0c'), [0])
    def test_case_330(self):
        self.assertEqual(pattern_match("Ydy%ySez`9l\x0b.\x0b\x08.lA~\t\x08A\t\\\tj1'}\x0c\tThob.q-\tZS\tBh\t/\x0cLv\x0cVU7t[e\r=I\tdHo~,^M\x08(+b\x0bU)\n^\t-]", 'Ho'), [61])
    def test_case_331(self):
        self.assertEqual(pattern_match('\x0cj\x08\n\t )\rvf 5\x08ba\x08Mf;pjY\x0bw&)12\rumHo@rLI*j u{TU{\x08x\x0b?M4mIWm,#(g6|\r\r\x08ccc&sN\n\rGhBO(\x08%fj\rzxs@ dCU[\x0c\r@Sm', '\x08%f'), [77])
    def test_case_332(self):
        self.assertEqual(pattern_match("*\x0cb1=@(\x08\x0bF`WTQR.|gvnH\n#\rd\x0c\t\x0c\nT?XGn+\x0cj?Km\riIw~\x0cB<\tg\ta\x08\x0b~-#\x0c-'U\x0cC6", '\rd\x0c\t\x0c\n'), [23])
    def test_case_333(self):
        self.assertEqual(pattern_match('G"\r\x08&pGxW0\r\\O\rPE\n>b\x0c\'Vn@?sOA\x0bUXmW}\t|JK9\x08f\x0c}\rEydVX\nB\nE\r?y\r606\x08Y:9U\r\x0b\t41zC.WYcJfS02 e/s\x088\r.\\\x0b', '|JK9\x08f'), [35])
    def test_case_334(self):
        self.assertEqual(pattern_match("KX/W\t1p/s\n\x08_\x0841(~Z\nLs0>`(iCX'XtKOBwk\nN=BR>/\x0c5\\'*4wc!iMynsf\n1|D35\x0c\r-V<rrSeTw\x0c\th6=\t\x0b\x0c\x0c,)=F", "\x0c5\\'*"), [43])
    def test_case_335(self):
        self.assertEqual(pattern_match('=O\tC^yeIm\x0csK 3#\x0c,f\rb\x0bJF)VX\rqBT8!`\t7cF#xJqH0s\tP\x0b5@OIUBM\n\x08pT\nR\rzN\x08s \x08@RI\r\n@a\np-z^@q"=~Pn\r_h\x08bb?-!n\r8_Y\t', '\tC^ye'), [2])
    def test_case_336(self):
        self.assertEqual(pattern_match('d~52\\6<i#v@A"\\U69aiM`\x0bus\n5Dcob\nNsi[>*?N5B2.GlL\x08{\x08ykDR9U]).W)6%iX\t !}I\n\x0bRiq*\x08S3^s\x0cJZ4Q\n*B},\tf', 'd~52\\6'), [0])
    def test_case_337(self):
        self.assertEqual(pattern_match('vV{\x0b_O 0iy\tmIc\tll,e%\x0c\rKX7}E"%J\x08)~9\x08n\n^6\x0c_}Ev!\\\rbrxUDis9Tp\t#ZV\x08\r]\t\x0b~\x0b2;J8\x08i<bX\x08N.A\rA\x0c7\nl<a4dW(\n\x08{0\r|\x0b\x0bRA)Rg\x0b', 'X\x08'), [76])
    def test_case_338(self):
        self.assertEqual(pattern_match('{pkr\nnax8IT@7"\nv2o8I\rIHxF\x0c\n0\riGD2yK\r#?L+\ne\n\x0b>X-qqc`\x0c.\x08*g-\r\x08X/%6v\x0b?{gy+^t\'B.)X\\', '"\n'), [13])
    def test_case_339(self):
        self.assertEqual(pattern_match('`d}ov\t?])U\x0c\x08h\rr\x089\x08a+VSY0\x08p=#D;0+Ckdd`q;\\p w2t:k\x0cD\nM@NhGO8X \n+~ \x08;\nH04tta\x0cwc4:,+\n=\n\x0b0\tqWv\\+\x082sJ*9Z8s\t>t<"+\n6/!J\\|d', 'SY0\x08'), [21])
    def test_case_340(self):
        self.assertEqual(pattern_match('kd>\x0b\ri 3t]"!*W@~\x0cz"8\x0c\n-\rCaL\r8ZEK]\tp`c44y\ra\x08jy6):w\tn\\}\n_gJNr\'\x08u\x0bTvE*s]wk~rwN{K*%}\nWS8\x08XMsa/4J\x0ct\t)\x0c1c\x0cYhC\x089ca\n.\r"6=jy\x0c#', '\r"6'), [109])
    def test_case_341(self):
        self.assertEqual(pattern_match('bz|}\x0c\x08s\'\t{JaD>\\|rLd75#J@1XC?UwE5uA\nvKfD[GK\r%_Cf_y*gvG(>v\tA\tk2SJ=Q\t\nI"5."\x0b1&mLd!-"A1I`Sa[n|^', '1I`S'), [82])
    def test_case_342(self):
        self.assertEqual(pattern_match('\n\x0c>\x0c^S\x0c\x0b\x08]SL3QL\x0b\r\rN\t6`o\x0bc\x0b `H;/bO\rPRw,\tWy\tP\x08u.U!=[[E\toF\tYM|hs\x08!i\x0b]5\rO\x0b##t\x0bIov_G44Z4Z', '\n\x0c>\x0c^'), [0])
    def test_case_343(self):
        self.assertEqual(pattern_match('(.:\x08~8QC"\n{A]:pbuTy"h1NQ\x08+"KsQ#X#Y+\x0c@0L8DZ43uq\x0cv\t\\9(k+p~t)\x0b0^E|6q\r\x0c\r\rqq\x08\r\x08uLRr', '+p~t)'), [53])
    def test_case_344(self):
        self.assertEqual(pattern_match("L%F]:_z\x0c\x08>7R[\t:Fj\te~XiWc]\\GF@W9)\txH|3L-`n?7,!g{Jb\x0b<\nd'~ -{P/@u?yjRf\nZ{: qh)\x0bm\x08u6b.gVid<`cB\\~\t\x0c\x08\t\t5N\\G@\nx\tzk9", '\t:Fj\t'), [13])
    def test_case_345(self):
        self.assertEqual(pattern_match('N)\tc6i`577\x08\x0bb+Wx`TJ\x08\x08qV*\x08\t0r@m+\x08\x0b6\x08\r/\x0c,7\tuGCp(RqFJ\n}DLs"\x082=\x08?Q\n1["oaa\t\x0b[@8\x0b\rLb#zJ ,/\x0cC"z%\x0cB\\iW\x0b|lW', '7\tuGCp'), [39])
    def test_case_346(self):
        self.assertEqual(pattern_match('\x08_FD%p\r`>n~t\x08Jg?9Bw)]*u<[uhX\nG!i,u:3#:X\x0c4\x08g\tK_LF&/EaHyt\r\x0b(b6j\rb\x08w\x08;\r7\x0bF\n~x{Uvp\x08mR\n]\r\niG1,lb15\x08\x08#\r*?lzRXRw', 'K_LF'), [44])
    def test_case_347(self):
        self.assertEqual(pattern_match('\\\x08)ps\x0bz \t,1p;%\x0b\t\n~rpmEAVJ5\r\x0baSzDWs])lK.R%{hmw0\x08LjyA(\x080R:gGlGZR)\t-\x08\x0b\n\rU5rvBN)MM}00b\ra;36]&N\tGmrNgk*Z', '0R:gGl'), [53])
    def test_case_348(self):
        self.assertEqual(pattern_match('NH*[E0Y8\x08Q\\\x0c\x08C)1E.x\rm|%o8B\x08_"`/R\x0bG3kq)rI*WFlVZ`\nSg)ESC8\x0c\'S<acIL=D9tK(N\x0cl\x08\nXRbB\nrY+\x0c\rBu\x0c1\t', 'E.x\r'), [16])
    def test_case_349(self):
        self.assertEqual(pattern_match("OUB^wPU<\x0cql\ri/:ySq5r2je\n`C]}_*\x0c_aBG8TrB\rG\x0b|\nUJ\x0b_d\t\rO\x0by[|i\x0bO#Y{g?Y\rwX\x0cn\x080Ur\x0bl\x0b\rfko(\x0bghd-@E}0]OL.\tzm,Kz\x0c'\x0c\nRI\t\x0b`\x0b;+\t\td5", '\x0b_d'), [46])
    def test_case_350(self):
        self.assertEqual(pattern_match(':Y\x08GI\rBG\x08\t\x0b\t(\t^50Y;L\rIO=\\\r;1u\x0c\x0cN:J\x089+F\n9\nJ_^|d\n\x0bV\x0b^\x08T])\x0c\x0cDS~=\x0bBr6g@x', '\x08T])\x0c\x0c'), [51])
    def test_case_351(self):
        self.assertEqual(pattern_match("B;;HBy3n9_HS_b^CZG,3\rnZ-v\t%2!CF<DG*cM\x08Hw\n<h6>3\tdRT\tUoB1/NliJ+o:)\r.6\\_7P\x08\tcl=au;C_'", '3\r'), [19])
    def test_case_352(self):
        self.assertEqual(pattern_match('fT)PX\x08\rCkbofn.\t6Y^\n\rs7R)\x0c_7=j\x0c(IU!Dxy"3\n\n.<_#V:\x0b;P\tWG8w\x08|:.\n2\x0c\t-9"e)bAd\tv\x08\r\x0cEx\x0bet,!0A0 \x0b\x0bE=-Bl:t&1\x0b\rc', '\x0b\x0bE=-B'), [87])
    def test_case_353(self):
        self.assertEqual(pattern_match('k\\5w]1\t\t6\t\x08\tOtyk\x0c"\x0c\x08Y,2EekJ&,\x0cZ\nN\x08AYdH\x0b\x0c\tBimAQ{tC*;\x08,Q.ZGXwpB-s-8p\x08S|<z%', '8p\x08'), [64])
    def test_case_354(self):
        self.assertEqual(pattern_match('b{\x0cgH[5R2\x0cs7%XR\tf)\t\x0b7\x0b{8Om\n\tK*i\x08:o\t>Iv|?pnk \x0beV6\r\r\x0bOhss3~|m]\x0c3\tEau7*o|bb', 'Ohss'), [51])
    def test_case_355(self):
        self.assertEqual(pattern_match("/\rpsLjH}\x0bmQxv\t]5\txF1\n:bnnh\r>G\nD^\nw4T^M/\t-+t\rT.{`wH\n\tZ1\x0b'DSLakz\n\x0br)", 'M/\t-+'), [37])
    def test_case_356(self):
        self.assertEqual(pattern_match('\t}>\t,_\x0ceBGRLpv\x08&Wi&75t.\rKnL\x08\x0ci@m\rA\x0b8]#2]L\x08j\ny"u.&;=C~oR7~]W/\'?j3~\x0cN\x08kbkOt:h,w@05f.\r}Z#O&`-', '&Wi&'), [15])
    def test_case_357(self):
        self.assertEqual(pattern_match("=vX*\tA\x0b\nBR-:@*'vVH\x0b\x0b!\tE1da\\F Gk4\x0bZ\x08bGJZ\ryV>_J]\x08Cu\ry(:?Z-64\x0bU\n\roz6Xz/P_UkZR_\n \t6S~wH", 'X*\tA\x0b\n'), [2])
    def test_case_358(self):
        self.assertEqual(pattern_match('1@\tA^m\t\r"\x08`sB\rbqr\r&sW\x08@#\x0c\nT3\x0c/jP#Qnqaf&,Ln\x0b:"#0Ca>.Lcz2OLr*`\x0b&FhJ`\t"#\n[S\t\t8T:`VV|^\rmy:y\nY%\\wm(Gk:d@', '\x08`sB\r'), [9])
    def test_case_359(self):
        self.assertEqual(pattern_match('T\x08d\x0cI~\x08\x0830\x0bbg7`CwDQ_R46\x0c?m\x0b\x0b\tK\t~\x0c\tjJ>5L\x08\\}[+h\r8_}#a[\r#43\nQP]u90Or\rU\x0c6ORI%\x0cYhZ0YGkWPyCR', '\nQP'), [56])
    def test_case_360(self):
        self.assertEqual(pattern_match('D\rw/b`^tO\x0c\x08:`<\rF\x0b}6\x08Cs,b<_\t\t\x08DxUaP /B[\n9t/\x0cgFY\nvWeAyTHATV0\x0c{o_\r[jI:q3M8Ga~R\r?+j#\x0c\tt\x0b\x0b\rP31K\n\x0bPZK0*\x0c\\\rA\n(\t\x0bsY4IH', '\rF\x0b}'), [14])
    def test_case_361(self):
        self.assertEqual(pattern_match('cpVHd\x0b)6vb\x0cf7s5C\r?\x08]\t*\n Vr5l.\\{qk+C+PE|YLF\x08jE/A\tz91"-6\t%~p!&_K.!\x0bI\tN|U}\rC^6^@\\*4y;x1m"&WHm', '%~'), [55])
    def test_case_362(self):
        self.assertEqual(pattern_match('\x0c\t?=@\r5yPr\x0cy\r#1`Zq_Wd3\tF\x0bCN5#yi\n-\\1`E36\t6Y<E\x0b\x0c:2tnG\x08W\r\tq&e:o@\x0b2+2@+~j~()B5UJ,a|\x0cpHgn\x08k4G_\nW`u\n\n\x0cW\\\'["4[s\x08', 'k4G_\n'), [85])
    def test_case_363(self):
        self.assertEqual(pattern_match('\nYABOJw\x0bsv\\\x0bF\rbi).zpx\\t|=\'"~X\n,Xu\x08\n\t]cU.\n\x0b"&djr\tt)@D!?I!\x0cV=3<\x083^oh5 \'[hUCg', '.\n\x0b"&d'), [39])
    def test_case_364(self):
        self.assertEqual(pattern_match('{\nk\x08=\r\ny\x0cx%\nB\x0bSUiAT\x0c-fe`i;Je\n(\x08;J9?iIIxglbO46;\x08R\x0b\rqrq*,}T>h7Gw@w<a3lQ|a\x0b]&s8\nr\t`)vB\r{Q#VJd?#%\x08ln\r[0\x0bPh\r|QE0n', '\x0bSUiAT'), [13])
    def test_case_365(self):
        self.assertEqual(pattern_match('YN,C};\x08X):eU\x08*ycf1IX6+wU~Fdr_y92]`\rhR\x08<=X\x08D]YHyaBXqP\noJMy1\x0b\tx\x08|.', 'YN,C'), [0])
    def test_case_366(self):
        self.assertEqual(pattern_match('\t\x08\n?V0\x0cDH\x0cv%(#\x0cY,\t`JpkX8\x0bk>WM!#-`=\nbdr?V07\tXA(HV\\-\x0c[".,;QPm\n,HkFsdlI\x0c\x08#R7u(3q|k_g^#`Z(NFqD', 'pkX8\x0b'), [20])
    def test_case_367(self):
        self.assertEqual(pattern_match("]N^-pc'\x0b.%z_ekNo>qh8|ca<V22\x0b0]\n\x0b\rk\x0cW2lL\tI<FV <\\\r\ne\x0b\n:v'S(gY_CA|hg'\x0bEw\t\rW,4\nR\\@1\nD3B\r}viXABu*v\n\n\x0b!\x0by\rpS@^;\n'\x0cfs!\x0b", '\rpS@'), [99])
    def test_case_368(self):
        self.assertEqual(pattern_match('4P[m\tK\t\r:wdQ\x0c\rI2\\Rc9c0@`\'aSb\tM2<nlp31AA\ng\t\x08\x0cfE!\ry\n4\nX6|0u\x08\x0b,6;16a\x0clZdC\'MQywx\tD,*#z]pd^JR93"qP0YL\x08\x0c\'Sn\x08?\x0b?8W', 'AA\ng\t'), [37])
    def test_case_369(self):
        self.assertEqual(pattern_match('(X\rjk\n\n`d\x08, !rTE[\\SWis*@e\nBt;S_\rD8\\ lGe|Yv=nMZZ\x08_%l\x08U\x0bIbU>}\x08V', '*@e\nBt'), [22])
    def test_case_370(self):
        self.assertEqual(pattern_match('=\nt{?bZg{@xA\'!|\rFD/,\ndW*\x0bsuI?*7\x0c&:\\\x0bf-=&u\x0bsB\rgp\x08z\x08 y\rTdSX@5\'M\x0cj#\ri\r*g.\rhUtwz`7U"\x08y\'\t e\ti2-7', 'sB\rgp\x08'), [42])
    def test_case_371(self):
        self.assertEqual(pattern_match("'H,6\ta<'zX%G^M\rc-1\x08#\nN)up|o\x0b6?\x0cgu]HH\x08;J\rSf\t\x0b\x08\x0b+#:5>kE32T\x08a#f*\n}3FzBs'I2\x0br\x0c7Ij\x0c@qH\t", ':5>'), [48])
    def test_case_372(self):
        self.assertEqual(pattern_match('4&\t5s\rh*g4&.Mm3/"5%@Hk~-\x0c%,p(H9>KQF\x0c5`eHWKM|l/]\tjuYNDw-=[*A yY\x0b \'3iC\'a\t\x08W\x0b8sO!\x0cdtN\t[o', 'H9'), [29])
    def test_case_373(self):
        self.assertEqual(pattern_match("w[F\n;\nVrM-4-^{\nFbJG1<rb\x0c\x08\x08hO'QLv\x0c7\x08ZE5M\n\x0c\x0bF\rahWZ\x0cK]!*\t\x08\x08&g\r}cDd^|k4LA )", 'bJ'), [16])
    def test_case_374(self):
        self.assertEqual(pattern_match("C\x0cot\n7\x0co\r\rO`R\x0c=?'NM_Qjs3m\x0cl.hW1\x08w{uq0\x08\x08PfQg@syU|E>%[/\n\x0b\\xe\r6\t\r", '0\x08\x08PfQ'), [36])
    def test_case_375(self):
        self.assertEqual(pattern_match('X^K.uyC5Nfmz{k-M k,-;C(:;Eo\x08i\r\r\tr?\\XW\nwa\x0b\r~e{zb\x0b.P\x08\x0bs|df\x0c"uLMIyL]\rb\t%Qp?\tgi4\x08U\r^\t', 'W\nwa\x0b\r'), [36])
    def test_case_376(self):
        self.assertEqual(pattern_match("og\x08297\x0cYA&hDAMV<r-<DoWpxE\nXuO\nc*\t%\x0c(f\r\\<Z<g<@QIk\x0c\rqK1u4\tg.[j+\r\t\rke\r\x08})9n}<q\r\x0bsJ>&CjF'q(<Csyl3t\x0bU\tm'\nz,0\x0b]\n4\t=x", '\nXuO'), [25])
    def test_case_377(self):
        self.assertEqual(pattern_match('\rx9d\n4\x08;ZCn\rAb>]^h\tZ rJ\r{67\x08ChVh\x0c9i+_\'=y(BFj"K=D\x0c;9e ;\x08hy\tW\x08\rDa \tU\\~)xA\x0c\r\nm v1YPDi<.A64l\r%r\x0b/Pi%u\r\x08KU', 'j"'), [43])
    def test_case_378(self):
        self.assertEqual(pattern_match(']\x08\x0cR{!ZVAS\r0HY"s=wq9\t\tY} \t<S66GhI\rIFS2\x08A}/V\x0bh?M(<\n1T^~L\x0c\',(h\x0cR{\x08\t&\r`.)?wg_R{\x0cE\t*yAEol', '{!ZVAS'), [4])
    def test_case_379(self):
        self.assertEqual(pattern_match(" Y\x08~\x08\x0c,c*F'a\x0c~\t.;e?4[sC\t9%g\t))F>#a6wu9k}@j@a|Bd\x0c\t+C66({h'^\x08\x0bQ\nh,{y^v\t", '?4'), [18])
    def test_case_380(self):
        self.assertEqual(pattern_match('T\x0bg\'"vl6ywr \t1_dU{0j-\n\x0b?q \x0c\nZLJ\n3.}P[X{byKr%\x0csT\x08+rd,VrmI\n:A,T\x08\n6D\r4U>\n{>`>46b?\t~r9', '1_'), [13])
    def test_case_381(self):
        self.assertEqual(pattern_match('CR4\'F\td\rcvFWa:g\t0IOKsxfyrm"i":\x0cSjF+\x0bO\t:R\x0b#F\t;cC_eB\npl.lAm2\t\x08\ttwa\r\r\x0c=p\n-K.yVf[\x08=,Ru(4e\x0baJX~', ';cC_'), [44])
    def test_case_382(self):
        self.assertEqual(pattern_match('\x0cP6v82@fGd3_gO\x0b\rzQS"QP\r\x08l`\x08!7+0R3\t\x08\x0bkf8K\x0b*\n]Tj,#"@C\\2S/.S\x08^4\n\t', '@C\\'), [49])
    def test_case_383(self):
        self.assertEqual(pattern_match('%\'z\x086\x0cno\x08\x0c\r%+t8\x0cMg4voe\x0c\x0b&[FJ\r#\x0br\x0bv,?\x0bw\t&~5.S\x0cs\x0c\x08.U<HG;Ub\rJV?13Qa*\n,|\n7kKu\rV;(K8WN\x0c?w_@":Od(3p/JG\nW\rS=/:nSk\nL"8+\'<', '\r%'), [10])
    def test_case_384(self):
        self.assertEqual(pattern_match('a\nL\t\x0c&.i\nHB8\x0cEJ~lpUtY*3\t|1\x0c\x0cD){"l^u\x0c\x0cMHxz\tTlyL\x0c\x0820OV.\x0c7Ft9P\nZt]|qDq.zS\x0bF', '8\x0cE'), [11])
    def test_case_385(self):
        self.assertEqual(pattern_match("\t:\t6OteO\x0bwl\r\tK^sKU\x0bxv\x0b55hEFO3\x08KO6'cbZ0\x0c9hWb}'e+#y>\x08\t/ES\x0c\x08\x0bO~%\niN+>DpLho\n\x0ca\x0cB^pSAc2TPH+p\rv\n@5!LgL2i9\x08#~\x08mY~K\\P~g(:?\x0c\x0cv", '\r\tK'), [11])
    def test_case_386(self):
        self.assertEqual(pattern_match('\x0b*`hd9E0\r6\t\x0bM\nkLt\x0cM=!,90\ry-\t7aic@)\n#1>.w0\x0b.\n_v!=&\t\t\x0cLU\ngf/WWDq\\qH;\x0c\'}t\x08en!:"Ge|1\x08Jki\r\n\r', '=!'), [19])
    def test_case_387(self):
        self.assertEqual(pattern_match('q1d4}X?:]II]IwjpB=,WcX=Mlj\n\x08\x08,(yC7v(A"-g]Cb^,Gs\tiW!\x0b\n?KFPGe\x0c.Kk^g\x0bqX7\tEUf\t\t\x0c[zC\reDA', '\tEUf\t'), [69])
    def test_case_388(self):
        self.assertEqual(pattern_match('2J\x0c\nw7\x08(`\rG7CR)G]L8q(iuEbNmr\x0c\te1;p_\x08iQBPb{\tYa 5"_I\x0b\x0bn\x0bAqwb3FG3W^N\n6[%\x0c\x08<Rb\x0bJO]\t\x0cJQLov2T\x0bPf,f>(\x08\t4V]I\x0bs35@q', 'CR'), [12])
    def test_case_389(self):
        self.assertEqual(pattern_match('x\t2p8pk\x08\rioeX\x0b}^\n2\x0c/z)p\taH\rD\n\t\t;ld_\t\x08/E\n\t\x08rdEf%}dK,jEily\x0bZ`%r\t\n\x08D_\nL>j-~\x08{4-\rHhJ\t\to+\r\rXE. \naoOoGB\x088_s{d[P1B5W`V))>6%E\x0bl', '\rXE. \n'), [85])
    def test_case_390(self):
        self.assertEqual(pattern_match("|_b,dP\n{p\r\tO\rV\t\rU\x08(amml0\x08mC2\rNzhj|L:\x0bxr;l\x08a'A\x0b/J4A,;LBcgZR+1eZ", ';L'), [51])
    def test_case_391(self):
        self.assertEqual(pattern_match('yP=l\\tZ\t\t\nS\nX+5\r.=^."(Wae"9{\x0b7\x08?*VbW&te8<&jx=\rC\x0cMc=\x085bi9\x0c\x08`p&T\r\x08P\n\x0cS&j]|A:\x0b', '\x085bi9'), [51])
    def test_case_392(self):
        self.assertEqual(pattern_match("edE^_p2Gt.mI .>R?pY\x0cFe!'#^,d#Y4#ccn\x0c&\x08\x08`_FGO8i\\B2)=;L-R:AR\taj\x0c4\rqP'gY\x0cDkZdU{P78I=\rH#=yDFIU,2D-\x0c\x0by7(\nk:V*E\rWmK4s0\x0bNU", '&\x08'), [36])
    def test_case_393(self):
        self.assertEqual(pattern_match('c^N\'>fZ"%of\x0cZET+mB`\t.u&SSD`=WjzUD.\x0bH0e\x0c\n\t8]\x0cxF#R"tq|`%\'}{\x0c?{', 'e\x0c\n\t8]'), [37])
    def test_case_394(self):
        self.assertEqual(pattern_match('i\x08R]4ed\t\x0cW,sO+\x0b_qH\n\t\r%|\n64\r\\y\r\x0cfY|z"\r#Q\x08M=\x0bB}BfwGq\x085&#T!\tcPB!`\t \n`Yu\rB6\x08_E\x08~h\x0c\x0bg\nEn)z', '5&'), [51])
    def test_case_395(self):
        self.assertEqual(pattern_match('p\x080:VKy%z3\x0c\t9~bzbr\x08=JD\r\x0c@k\x08H#\ri ]A\n=T|Pp\x0bra\t\n\tO-"&")2"TMr*Z0\x0c*4y0r=>uQ|y@P\x0c#RKc>g\tmD|\x08s&\\', 'A\n=T|P'), [33])
    def test_case_396(self):
        self.assertEqual(pattern_match('VR;\x0c4m\n3#QD%\n\n\x08K"YKbd%HoK6/vI\r\rQ\'SD]|f\nh.N\'\t#\r\x08iWv.xqg"gK66\x0b!;k`-KV0\x0cE\x08(?\rc|8qp>\x08\tyLqU]UO/6a8grG~\x0c8g\x08r-8\r-%', '3#Q'), [7])
    def test_case_397(self):
        self.assertEqual(pattern_match("5 'pf\rM)\rT\x0b\r\x0cR\x0bv5F^=\t~4wt:riE+G\tm\rDUO>%=U>M7 \x0cW\tmd\\T[!\tZc\x08E[sL+\tl=u[pazuy\noi?p\x0cy%EUk\r:PeW!\x08Vt_", '\t~4'), [20])
    def test_case_398(self):
        self.assertEqual(pattern_match('f\n<cD9h5G>4\x08}F\r0e44&\x08!*bb=EWwULpQE.(@\r^]&v\x08K\ti\r}+&Q\t Ja(E\x08\'g"&s9^8\\a4\tzt\x08fj\x08JakvHUOyoPAG\x0c\r6\r}c', 'UL'), [29])
    def test_case_399(self):
        self.assertEqual(pattern_match('? v*U71Z&MV\x08\t~6\\b"A4=\r9\nks0s\x0b\\55yn#bs\t\'p\x084S\t.mWk4Un{Lp+Fl8S~<', '~6\\'), [13])
    def test_case_400(self):
        self.assertEqual(pattern_match('\n>d\rX*)\x0c9^\x08]A\'\x0c8ir\x08\nxGpDc\x0ca\x08\x08Ej\r)\teWcmk;Z4@\x08\x0bW\t/\n\x08<\x08\n\t=u3<1t:\n5\nY\x08%\x0c-\x0b]"\x0cIKtu}Z\x0bi|<x\x08', '-\x0b'), [68])
    def test_case_401(self):
        self.assertEqual(pattern_match("\x0b\x0bF1ia(\\-pt\x0cO\x0clsan\t0d,W!f\n\x0c(tjK\n!]\x0bt5\t\n\x082?\t|Ltulc\nT\x086c\tm&rPa}\x08(v15r\n#w2=\tCHwg\x0b!jI'N\x08cK\x08]e'O#\ra|ov/:itJQ}+#D\x08\r/*y5v+?c", '?\t|'), [41])
    def test_case_402(self):
        self.assertEqual(pattern_match('J7\x0cDI-U\x08B[(<H9k[i[\x0bHFSOL\r8S3\tUr\x0c{a6zl J&zyHe[01-?*JT\rfb/\tu|F\\?', '\rf'), [52])
    def test_case_403(self):
        self.assertEqual(pattern_match('\'m\rf\n\r7_\t::M.*.=yv?4\tg)\th<Z)y84V d&guG>I\'>6\rsT\n\x0bo{UsMshyZ"K\x08sq\t]\x0cQ2M\x082\r#>l^3(\'0\x0cd?\x0c/G0F+4T\x08Y\'`', "guG>I'"), [35])
    def test_case_404(self):
        self.assertEqual(pattern_match("I?\rvnd)ot\tzmkZas6c0Kww\tq#XD\x08aj/D-P%j\to>:vU\x0c5?R.'b#1\r^e]m5{rgK)cy 8y\r=?9", 'vU\x0c5'), [40])
    def test_case_405(self):
        self.assertEqual(pattern_match('[\x0c\x0c\n_m\x081f\tOu\nb%\'D}\x087[\n7cOq>63\r08}J\x08l_{|BJL% Br\npBO3\x08l|_!\x0c^\t]Qy"', '\npBO3'), [46])
    def test_case_406(self):
        self.assertEqual(pattern_match('6"s!.6;^/a*Di7wc<<2GE[aiW[Y%K\x0c{.FK\t.ZC8TF:fc;\nb>=\x08Y <#P;T=\rQc(3~kLmn\rbL\x08', 'kLmn\rb'), [64])
    def test_case_407(self):
        self.assertEqual(pattern_match('GOJa^vN\\-\'|\r\r\rG?8I,:\t\x0c\x08\t8W\x0c\nXjBum"!ur!<\r#Z\t\n\x08E\'M\x08mZ&fX,YXGN\tvLt5k%Imq~\x0bvKwI,DL\x0bNU4ra\x0br\t~\x0b57e', 'q~\x0b'), [68])
    def test_case_408(self):
        self.assertEqual(pattern_match('<i&<\r]\nL-t#wU\t}`Qn3D_g\x08RA;\t#T/U=Zh~#A<fM\x08S\tg\x0bx?\tx"\x0bgVb\x0cKXuc\rE+Jw(o:\x0b\nh,RDE1\r/\x0b~z%K~"y\x0b\'P\x0b<v5dlbVo)\n\rVqa-S"]\x0cCBC!', 'S"]'), [104])
    def test_case_409(self):
        self.assertEqual(pattern_match('\x08L"J1#=Dx2(\x0b\x0bC\'2Q\r\\#\r8,Uk? ^6#W]=p\\i\'+I\tyz\x0bZ)\\3va\x0c)U\x0c\x0bq-x\x0c\x08t:+A\x0c', "\\i'"), [34])
    def test_case_410(self):
        self.assertEqual(pattern_match('\\!~\r\x08\t];}\nQ\t\nd~l\x0b4T\t_\t\r\t"!iPtA _O@"}\rM5[;\r5++`r\x0bQX<yK\x0b\x0bsX\x08\rjX8\x08,\t\nfRT-y4Kod\x0cG{[?RM\n/\nZ\x0c}\n\tl^jJSD~U\t{P\t\x0c[A\x0c\x0b#\n\x08>+v&2o^', '<yK\x0b\x0bs'), [50])
    def test_case_411(self):
        self.assertEqual(pattern_match('qoci/%39\r<\x0buBf0?F_%t)T=ca>c\tulDe:\tD\t"C~2Ho\x0b)-^s"H=h>!%sM#o\\0A\x0b/m(AVqA:p4y\x0bSUPS\r"y4lY\t\x0c8,#\rY^7[,y]2^\x0ccV?hNW\x0c\x0b\x0c\n\x0ctY', 'e:\t'), [31])
    def test_case_412(self):
        self.assertEqual(pattern_match('\tCbK"G8\r3U\'\x0cx\r{/^\nQDZ\x08fF99]9m\nZ{\x0c?\x08~-\x08H\\\x08\t\\\\pK\x0b!e3\x0bV,*\n\x0b7\x0b\tD\nbs\x0cm\x0cs46\t6?t7\x08n|]yXI0\tg\x0b[v\x08O', '\x0b!e'), [46])
    def test_case_413(self):
        self.assertEqual(pattern_match('w=#(3D`ea6KI\tJG\t9S\x0b\\{5E\t-o"y\rS#S":79De"c\r\'qUn\n!dZ^MuF"?# m;^\tq8(3Kx\x0c@gu!\rWU99', 'u!\rWU'), [70])
    def test_case_414(self):
        self.assertEqual(pattern_match('>Y\x0c+5z^d\x0b\n^R|\x0b7|;d "P#O\x083+p\x08&r,GFzkNNh3C1lz=j\x08[Qu1\t*j!\x0b8RohB(CzZZfzx\x0c#*W8;I43x\x0b', '|;d'), [15])
    def test_case_415(self):
        self.assertEqual(pattern_match("\nV\x0c\r{EpqBLNkp`~&c@&\x0b\r\x08pxMR9idg4cju\n#J\t\nFx\r#z}whltY\t\x0c^UurR\x08+F9\rzXG7=Fg\t'ZK3aa\x08vO@E\rJ|\x08ei!:I-Ij\x0c99U\tT\\tQf*ubY, 68S<SUX<o", 'E\rJ|\x08'), [80])
    def test_case_416(self):
        self.assertEqual(pattern_match('-\x08\r#O:Q3:\nAgt`0jE\r+*\rq5|n;\tj("Fqm\ts\x08Wn/5p!A\nzE4<d;5;qZ\rJa\x0b!7\x08r>)utdl7vb\nsnj\n46', 'Z\rJa\x0b'), [53])
    def test_case_417(self):
        self.assertEqual(pattern_match('-\x0bWK.\t\x08v#UNa\x08\nz\n7G-\x08q\rZ]9\r<U\x0c\x08nIl\tyf};&\rW>DkL6o\\3\nbK1tqX\r,\n\n&,XR7^F\\|\x0czNd4?', 'Na\x08'), [10])
    def test_case_418(self):
        self.assertEqual(pattern_match('.\x0816Ak>\x0b=:W\x0b\x08+\r*Tm\x0bIbbRZ7"e*\x08d`7Y\x0ct5?\t!Z\x0bFOf49QFFOar \x08\x08;\ni.W\x08N_p4\x0bZr\n^\no#:0zrQ\rFi\r\x0cfXS\x0b#&u2]\x0b_-T\x08XwJBS7c\rxX\x0bU\x0c', 'Tm\x0bIb'), [16])
    def test_case_419(self):
        self.assertEqual(pattern_match('NO\x0cYFsU+E]\tt\nH=\x0bJ\x0cN\nQ\x0b`L*H}\x0cjC@>9UGS6^\x0bo=yO\x0c\n_b,1O>j/i>:t,LJ\t\t@kw\t\n\x0b O\t\t Q%i@@i\t\r\r Jj|2\x0cs\x0cZ"f', 'w\t\n\x0b'), [64])
    def test_case_420(self):
        self.assertEqual(pattern_match("\t=\x0b.;N+\tP\x0c\x0cw\x08ru\r,\tvTeObQ\x08T\rZ->#>!`\x0c.eE(\x08l0\r33Pt\x08]e4z/3\x0bXqV,\r Us'#b`\n3\x0c+\n", "Us'#"), [61])
    def test_case_421(self):
        self.assertEqual(pattern_match('\x0c>pr\x0c0b&j:\x0cP\x0c\x0b&\nFc:F+vVeos/)C\'\nX\n\'\x0cvEm_"fHD\'[@D}>DETVifE\x0c56@#6@r\x0b\nt\t\x0cS9O\x0bn\taKp\\*j<X#C69rgB\nm 3\r<bTV\t~]KK4J>6S\x0b', "\n'\x0cvE"), [32])
    def test_case_422(self):
        self.assertEqual(pattern_match('Gp\x0cI`KGQt3<\x089\x0b!}vNt5<p"n5DRJ\rroGI;X\x086H&YR!\x0b\'\x08,, |ZFVjLe_j,-&\t\nM+lY<Ur\r-asiwA<dq\x0cP\t', ';X'), [33])
    def test_case_423(self):
        self.assertEqual(pattern_match('\x0c4H6.a-\r{\tvF\rkz\t|NQ\'d++3alr0\t|ewVIQ\tJ\r Z`?2a]#B\x0c\nIm!z\tT"nTi\x08Y\x0c~Kh=G2P(He\r\r\t1=l\x0b G[RAE1N9<w\x080\x0c?i\t#;[X\\Cp', "|NQ'd"), [16])
    def test_case_424(self):
        self.assertEqual(pattern_match('\n\tR%,s\x08\x0b2js*\x08.c^\x08Bw/`n\x08qhAvbO8\n/b:Oz<4}zThuQ{\rc\\B9\n~}^D\x0byi? dc\x08', '\x0b2js'), [7])
    def test_case_425(self):
        self.assertEqual(pattern_match('_|j)\x0bJw`Y\x0cRKf!9T\rj2:\r[\t WS%k[|bxD?4/\\6Lm<7WFw^x\x0bIx\x0b[\x08UAfbg9oQ+V}1\x08JK', 'Ix\x0b'), [48])
    def test_case_426(self):
        self.assertEqual(pattern_match('1>bQNtPz`XJ\t\x0c"5Y\x08\x08~\\PV\\%6\x08WKeXiC~\t|[W:\t;r+N]eB1sm*+u]C?Yer85XYA:\x0c]z{=\ny\n~MAq5*\rk\x0c\rG)"U{fdJ7+"3\x085|@V=_soY\x0b|~fbXC"\x0c', '\x0c"5Y\x08'), [12])
    def test_case_427(self):
        self.assertEqual(pattern_match('1\x08\x08aS+5\n8rqqR<Z\r?107Lm.zPV\n"\'~\r\n4\\*"\t~L"6{\x0b|\n-!3\t]D\x0cBy\r5\'Y>J6lV2Lzw3Jy9h\'C{t,2dj\nLm\t#1kCH3', '6{\x0b|'), [40])
    def test_case_428(self):
        self.assertEqual(pattern_match('\x0cG\x086|{Pu.Py!oiIPPR9C\nM>PVLz/1cS\x0c\nC;_B*D`lXUj<\'n\x0b\x0c\r:K#d}Z(*a,\x0cF\r"e!(', 'K#d'), [51])
    def test_case_429(self):
        self.assertEqual(pattern_match('z\t0\t)\rHLk\x08:D\t\x0b~Wn)\n\x0c\x0b\x0c3l50q\x0c?1PXXa?X\tG\x08F\n!N.l\t[f\n3\\w-lDYtq1Jf\n5gNs~\tV\tGBoC\x0b3F(WrLyI', '50q\x0c'), [24])
    def test_case_430(self):
        self.assertEqual(pattern_match('\\#\x0b@|a5\tG,<+)">K*|Z_\r1Fp#Tl\x08eef3\x08\x08Sq+3\x0c0\tJad\tU]<\x0bh[&\r+Q7:>\x0cQc\x0cX\x08P]=Q1o] \x0c!cJ{\x0cT\n,/lkhQ7p\x08Bo]S', '_\r1Fp'), [19])
    def test_case_431(self):
        self.assertEqual(pattern_match('L\x08V7Syki{-_>75|g\tHFe{\x0cj/\x08BRa\tU\r,\r,p]BhD_!vu[7SP\th"1\rz8Ec\'u\x08P2uf6n\'\\8C t\x0cx\nyYD"H:Q\x08(*\x0b||\x08\t\r\t:\x0cNC\n{\x0cANwk\x0b', '\tU\r'), [28])
    def test_case_432(self):
        self.assertEqual(pattern_match("A\x0bxun^\x08p';\x0c,@[`2JW6kSb-56\r\n\n\tG|IwGl?\x08/k31\n\x0c6\x0cJdv?V\tVG1?@6t^:\nf:+\nC!\x08y`>6'Tg\x0c!HQ(\t{\x0cjc)4;\x0bl\x0cvV(U\x0b\x08qjjH\x0c.", '!HQ('), [76])
    def test_case_433(self):
        self.assertEqual(pattern_match('@F@4rv\tv!O"a\x0bBOHO\rYut\x0bV\x0c\x0cHfyH6\x0b3\x0c4*]R{66\rC{\nS3kAP\x0cSlO63\rA\t4Zvo#B0\r\x08>f\x0b|E+', '\x0bV'), [21])
    def test_case_434(self):
        self.assertEqual(pattern_match("NP'lT1kW\tr\tH#>|10ut&N`~R{-6\x08lr]\nt!f}-Y//\x08H2m,j@.\tkC\x0bm4I(^8z<\r\x0b\x0bfaK\x0cBMpBZn", ']\n'), [30])
    def test_case_435(self):
        self.assertEqual(pattern_match('\x0bC#g|g8\nU=@V\x08STDh|Nu\ro8_G\tA"w?Yws\ncYW\n@R=SqM?at\x0c~@mc1H\x0biCwV45rL^4\\=o\tr\x085E=\r"UVgF\x0bh\t-\t6\\,\n]g+SPt\ns\x0b\x08]+"', '@V\x08STD'), [10])
    def test_case_436(self):
        self.assertEqual(pattern_match('\tB4_1SlsF}4\x0ciOIa\x08t|\tRe&\nd\x0bl&q5\x0bEm8^:z\x0b\n <A1nG\x0c3;cPz\t\n\x0b~a(\x0bdH?#\r:\x0cz{\x08\x0b>uUI>Bn dM\tJa`3[z\\c\x0bT\x08CR=;Nq|KMoGX\x0c(-x"m', 'nG\x0c3;c'), [43])
    def test_case_437(self):
        self.assertEqual(pattern_match('\r\r\\b2S\'"s\x0brt~Tx~1\x0b#Is"\t\nSjv\r\t*{6uh\'IW\\"8\rC]\x0b\r@vC<\x0c)}<KwRGr\x08y\r@Dv\x0c>*Oc\rO\x0cb>1X', '\r\t*{6u'), [27])
    def test_case_438(self):
        self.assertEqual(pattern_match('W\x0c2Pnv ,\x0b\t\t>IjzV}?\x08K\'o!M+q!\rmV!|GK#V?Y<+\\{3\r.\nJ:24^H\x0c\r\tqh^FAH^d+s}\t2M;6E~cAG?hN?y-\rh"\\', '^FA'), [57])
    def test_case_439(self):
        self.assertEqual(pattern_match('q+VtD\x080uD<!,\\I?Ap\x0b\x08\x08\ndpPCK7RQI+\x0cT@Q_\x08xZ 2KEQBedx2i][*\rE/@\t\t!c7.[C?K\ncIp<B?*t\x0buv@"N3/)\t\r<6p\x0c"3\x0c"~U"pH"s`E)k#', '\x080uD'), [5])
    def test_case_440(self):
        self.assertEqual(pattern_match('\rAp\r\tg\nB@)eT\tIK7Sv\x0c\n\tRmJ\x0c\x0bR=\nc2NC\x0cz*{+v\x0cm\x0c,x:&\rw!8yJ3HJ \x0cD^gLtg\x0c\rOHOidVZx\r\x0bi~=T^!XYM\x0c~`7e/\x0b\x08\x0bzJ}O', '7e'), [87])
    def test_case_441(self):
        self.assertEqual(pattern_match('=wl\x0ce|rb#\rZr6ed\x08\x0b\x08tQD\rS\n\x08%b\'#=8nc>\r|\x0c3\rwWT9Q>;7\rVL\x08m7T:MeEG[\x0c\x0c\r\n\x08D_[V*Ipp;fmy=L{"UV73#9g\nqy}h\rxpd.M2D77\n\x0be?Z!\x0bP)a\x0bB', 'y=L{"'), [76])
    def test_case_442(self):
        self.assertEqual(pattern_match('=\nV}\x0bh\x0cw\n3Umup\x08%\x0cu|Y{T5VP`i*\x08|6W"rSo:}!v\r8a]Z\x0c[y\x08RA4\t(\n4,F\x08\x0ck\x0ciI~Rz,m>*Se<`\rPBe\x0c1\x0b%J\nytbid\x0cmA\x0cp', '\x0c1\x0b%J\n'), [79])
    def test_case_443(self):
        self.assertEqual(pattern_match("\r<\r\\?\x08A,phKw#l{U\x08T\r>uM!\r75mE3x\tXk4\x08\nZde%3hk\n~4XO,c@{0cy25R\r\x08\x08\\23qo5\n6\r\t6huHCt)\x0boVw\x0col\x08u' lqk;X6)(UlH\r\n~(hc(\r0\nV#", '\x08\\23'), [60])
    def test_case_444(self):
        self.assertEqual(pattern_match("w{Nt&+_d~\x08:9\x0bl9+RT/4exJ2?#y\x0b!\x0b\tF7RLc|\x0cq'0)<f\r=t\rZ1!1hN\x0cfPS{r6\n{L#\x0cl\nkRf\x0b{\x0b#\x08\n\x08!\r\x0c", '~\x08:9'), [8])
    def test_case_445(self):
        self.assertEqual(pattern_match('K=BEb,\tr0p\r#M]us3Q\x0c\tT\x080\x08>aWn\n\r6V\riYIH\x0b\rZ\x08"\r<d\t\n\r^2 }p.;o\x0cH]2D\x0bg\rwEI6n\'rhdi\x0b\x0c\rM\x0b+)\n[\x0b1a\nvG', '0\x08'), [22])
    def test_case_446(self):
        self.assertEqual(pattern_match('PZkr6 /!5q5%,@\\<.W^ewXzG\x08\tUm!*g\\@\n\x08*mXZ\tOyU/:\x08}\r*ZkZ_S4\x08s\x08ZcqC \rb\n ', 'G\x08\tU'), [23])
    def test_case_447(self):
        self.assertEqual(pattern_match("2T\x08AVWMnq_o\x0b>P\nb\r4~c61c~Tz%U5Y5lI\x08L\x08VET/TbErbVTU&r'B\rY-+G)ZTBz9\r@\rI\nX\n,U\n_^\nmz9*S", 'VTU&r'), [45])
    def test_case_448(self):
        self.assertEqual(pattern_match(':F.& (A\x08\t\x0cC@I?jv~"\r%\x0baR,z6V\nXh\x0c7d\r@8L_16m(\n[\x0cS^T3z\x08U\x0b,\rq),\x0c\x0b9dGd}j\x0cR\x08yhy-%;aex\x0c(+\x0co>!^', '8L_1'), [35])
    def test_case_449(self):
        self.assertEqual(pattern_match("rK3zbjMX>'u)\x08KYm:\tLDe#u8A<XEm \tk*5\x0b\x08OcI>C&^n[\x0b\x08_e\n\x08\x0b|5>KunzDUGJafm.e|<:s\x0b", '\tk'), [30])
    def test_case_450(self):
        self.assertEqual(pattern_match('rm\x0baSjNq\n7\rR\x0c,O[+x 7z\rT\'\x0ccq\x0b\r0\x0c\x08iExS^rr\t+(U+u8>\n~zcW?j!">d8u', 'm\x0baSj'), [1])
    def test_case_451(self):
        self.assertEqual(pattern_match('~^"\x0co#cY7xk*UFF5\'Z]%y\x0c91\thdGc*KQ\x08%zZ})k[I*py3\x0c6\tWm@xr1G\r\r|}UH,r92A\r@}=\n*\t+qL\tnKC\x0b', '"\x0co'), [2])
    def test_case_452(self):
        self.assertEqual(pattern_match('3|A+HZ7F&j|4\t5z0Vwr<\'\x08g4\x0c3#n&6\x0cA \nh@A\x0c"|VX\x0cWEh\t"{d\x0c\x0b\nr9>\x08\\\x0b~1\x08~Gq\r#\x0b-%N}>j0OI]6~\x08J:nH:rbi#1K\x0b_Z.DLA]\r\t', 'VX'), [40])
    def test_case_453(self):
        self.assertEqual(pattern_match('/>^5^;48r\x0cm9h\x0b\x0cUF&\nQl\n\x0c\n\t\tGM9\x0c\r-\x0bTf\rz\x0bd?Vtup\x0c7\nMtP2b1~"PLwP2,\x0cc|F wv\\\x08\x0b\x0bE/X@\tLM8\t\n\nIRt?6x', ' wv'), [65])
    def test_case_454(self):
        self.assertEqual(pattern_match('dn<rCw\x08\nJzR\x0bsn\x08]@jaTe7\x0bZ*`5"(N\tQC\x0bY}"e.`=\x08P/fFS/=M\n\tf\t\x0b\x08Y\tq\x082\x0bR\x08fq%\n_%Wo\x0b\x083ZMTw#y\x08_\rjVK;Q{Ne:?GC\tsd', 'aTe7\x0b'), [18])
    def test_case_455(self):
        self.assertEqual(pattern_match('DTBE\rT}ihC3\x0c.K?L4x] H9ePy\t*H\x08lw\x0bk?\nvwCS~U3/{;\x08x\t\n[B3l#I\'Mz|<KOs0m\t+"NxZj.KJ;+8Wh_\t\x0b3m\x0b.9*5_5a\t^j[&/z\x0cUKt8X\t?mN\ryV;', 'z|<K'), [57])
    def test_case_456(self):
        self.assertEqual(pattern_match('mF0m5=6#Fk \nE\nog(eB*-\n\'c ^\'.s\n\x0b-u\\*\\\t\x0bi\x0b]t\x0cEy\x0c4\x08\tpCI2Q \r53)|a4Q^q\t\x0b6E\n,T<1d;C\x0b\x0cN\t\x08l;gj?\x0b"\x0bFY\nMPN]\r\r!OO1', 'g(eB*'), [15])
    def test_case_457(self):
        self.assertEqual(pattern_match('u>\rb>\x085BW\tjDf-\x08\\a>qn~1\x0c5^b5\x0c\nH?E=J#\x0bS*l\x08@<(A\nHo\x0c7I\x0bX7=lXfH)6\r84\r=8Y:t\x0b?6\x0cZ\x08\x0890', 'n~1'), [19])
    def test_case_458(self):
        self.assertEqual(pattern_match('CcsG;l_G/3[jw]:PxJ\ntj\\\rx20E>#b\x08mK:\x0cW[\x0c{P-nqA-7\\^`]r\r6|\t\x08|\x0b8pl,q39\n3mxmk\x0b1^*(', 'jw'), [11])
    def test_case_459(self):
        self.assertEqual(pattern_match('m\trV>V36x\n\x0b1\x0c*EIZA\x0bj^\r=.\x0bGt\x0bz\x0c6pcQU 0o\rtXQ\x0cW&xuN\n+;a\\uakv\tXa\rp\x0bguHbl(mYJ%9mQ\r"Jn\n\x08mVF\nc^W~jTV\x0b>`Ps', '\tX'), [57])
    def test_case_460(self):
        self.assertEqual(pattern_match(":V`~Xl9\nQx\n\rEeX\nff) 2v'Y D;n\x0b#mME\n~/\x0cEZp<'KnY~!\x0c7c!Q,VvK\niU2*ry\tL})4\nK\t\x08kp\rz[29O0&(8@ \r\x0co\t(/<\nL&VX#,\n||90", 'EeX\nff'), [12])
    def test_case_461(self):
        self.assertEqual(pattern_match('(wSvT\x0c[q!\x0cwVdO\x0c"|wuv]~z\x08flE^C\x08\ryTlzjd\x0c<3{:[\tac^g-lf\r!\x08Is\n\x0c\x0b|\x0c&JrhPe\x08*gCIV&8H>', '-lf\r!\x08'), [48])
    def test_case_462(self):
        self.assertEqual(pattern_match('6@OqUVK\r\x0b,\x0c8;x0\n\nGVn6f%]\n\n\rP9n1L"_"1^!ZpBI"\n9]X[}>=K\x08+%\x0cD<Mm6OcnfK2[\t:?>KBq\tRER\nJ)\x08z^AB:\ts3qJoaaC3F`X\'\n=q?gsfw,\x0b\rS{%', 'I"\n9]X'), [41])
    def test_case_463(self):
        self.assertEqual(pattern_match('tY\t\x0be[`!]\r#\x0b< ;\rG\nyze\x08E\n\x0c\n&k=U\x0btK\rWv0NZov7VkqZrKM2(\t~cjX\x0b\x0bQEU', '\rG'), [15])
    def test_case_464(self):
        self.assertEqual(pattern_match('On<Xo|\n\x0btDp?\x08b\x0ce^T\t)vWNwom\x0cNvE\r\n\x08HD\x0cU\x0cuJhediroN.LUFhh>{.kQ*j acR\x08\t!%?\'l[N^\tq=<4\'=\tX#nOiH/T"i', '\x08b\x0ce^T'), [12])
    def test_case_465(self):
        self.assertEqual(pattern_match('\r\x0c?\r\n@J8m:Rn>\t\r\r43JPFM]BeOp~.8Fh/Y\x0cj%%*n<lF#R^UzI\x08H>&V`G\x08\t)HRu@a7u=7', 'u@a'), [61])
    def test_case_466(self):
        self.assertEqual(pattern_match("U\r\x0b)<FS-U9IVJZp\x08_eD]9hn&\t1\\1P@\t!X@\n\x0cZ#bQ\r|\x0c_\x0cBV<>6OvsZ_{,6Hx-Pa8\n\tZm{YV{\x08d|N'I6@bU=]\rrR?GOp%N\n&\x083P\rM\n,R \x0c@", 'V<>'), [46])
    def test_case_467(self):
        self.assertEqual(pattern_match('Y\x0cu\x08BbSrZ0\x0b\r*\n{9Mxu\x0bf1],\t\r`\rty:VWaV9!lUf;ve\t\x0cspK;ywuX"Cc\npY4ts]dPA\t\n\ts', 's]dP'), [61])
    def test_case_468(self):
        self.assertEqual(pattern_match('l,a\x0cXIxYDg\x0b\x0cr4 !>=\x08vz,Z0[\x08V7Y%\x0c3xG\\?:T6s\rPPbF_\r\x0c&a?jf\\~\\:VS\x0c\x08e<\x0cV\n\x08,JuIuiQcaz)cFt\x08&4c@+', '7Y%\x0c3x'), [27])
    def test_case_469(self):
        self.assertEqual(pattern_match('e~j3\rcD35Z\nn~uZ`\tE+M>\x08~5h0\'yPB8\n\tfHiU(y!-;t\r+:d4GxoEEh\ns]>iF.d\'M0h|40ydk7"<nChG3i8^M^\tfl/%h\x0b{\x0b\n\x08#\x0b_%iq2(/\x0b\\4M\x08z{\nNNZ=Zy', '~5h0'), [22])
    def test_case_470(self):
        self.assertEqual(pattern_match('kaY)9<\nH9\x0bsC\x08;=\n0@DY0^r{\r\x08\x0cV\tN^m miHBc;C\x0b\x0b/2]\x0b2N;88\t\n\ndu\n\x08\x08~IDd,B\x0b/\n\tFixk', '\t\n'), [51])
    def test_case_471(self):
        self.assertEqual(pattern_match('(C\n\'\n5&Gw4O(;pF!\t\rCS6,\t:d.\x0cW\x087wDo\nt*8\x08o iof_6Kn^\r#"#N:q1Lim%JpvX0@q\x08<^-\x0b\ro9J\nkB:E<XGM4|dz\x0c7OF,\rD2&g', 'q\x08'), [66])
    def test_case_472(self):
        self.assertEqual(pattern_match('3i=xCX*f.;U`"j"Jd+@ky6f)`nD}\rp{.;>=z253Z\rB\tp:o;g%NlqiH\x0cK7\rW:\n9<-u;L-alZn\x0b\x0bd \r%dM\x08{L8lRY=#D\t5!', '=#D\t'), [87])
    def test_case_473(self):
        self.assertEqual(pattern_match('2\x0c,Lyxe+/\r\'//nM\t&,\r\n}B\x0cln\x0c\nvM?^"y\n|_/\x088\t+Y\n\r/\x08\nyYm^@\x0b/V\x08UlHY=MBX#%\x0b\x0c\rt}GMU_yJ\r&\t\r\r\x0c1`\t\x0cp\x082)\x0bE4|5l6FR3{v\x0b\x0bzDK\x08yyk\t', 'ln\x0c'), [23])
    def test_case_474(self):
        self.assertEqual(pattern_match("\nLjaAmT\tMW%l{G\t\x08Tr8=\x08\x0cxN\x08\n,':z\rf:.6[\nCK\x08*M4qk\x0bgA>\r\x0cA\r-\n\tE^\nWB\nD\x08'EE)YC\r|/Wnm|\x08.\\[\x0b\x0cI(*VGE\\VZ:Q+/\x0c\x08Ke:/H\\\nr\x0b", 'gA>\r'), [46])
    def test_case_475(self):
        self.assertEqual(pattern_match("j<z\x08e.]/9,.\x08Oc*t\x08\\lo=bJ\x08cv|w\x08\\]'\x0bE`Y:\t}+%IKi\x0c2W\\|S%c_V+U4\nqoj\x08\r\x0c\ru \nh/7U!n\no~\tz&Zzd^5-S\t\x08,NEc", '\no~\tz'), [74])
    def test_case_476(self):
        self.assertEqual(pattern_match('as(!a)h\\14 \\Tjk8\x0b\x0bWIT\tR\x0c\r\nS?K\n4QE9Imog 5\n|\x0bAv\x0bY?71\x0b!W ?\r!C@\rmY\x0c\tlcsvQ4\x0b{I1ep+\nv', '9I'), [33])
    def test_case_477(self):
        self.assertEqual(pattern_match('yd;N\r\x08\r_v-=4;\x08(u\nIz\x0b\t5\r\x0bz)gISiRe\'xRiZ=\rY1\x0cKsl^/N=mp?zJ_\rC\x0c#\x0c#7sEMP\x0c \n(w_\nY-+8RgQ\n\n"K\tKFs;\naX{#2fOXBj9\x0cZ\rMd\'\rR', 'd;N'), [1])
    def test_case_478(self):
        self.assertEqual(pattern_match('u\x08\t^\x0c\rx\x0c\x0c7m\nx+&\rp\\C\x08zk\t.m\nP\nzf\x08\x08~-\x0b/:.o\rzU420_ZY*TIHB*\x0chCuZe\n/:8\t,\x0c1A', '\x08\x08~-'), [30])
    def test_case_479(self):
        self.assertEqual(pattern_match('Z5[{-\t@"k\x08m\x08_"4\x0c\x0cIqb{[4gs\nho2n\x0bI\x0b,0l[\t6H=iDw\x0bfG\nqG3J\'\\]g\r=v*\t\x0bi\r!\rdlxN)Y]\t\tF>n+yP@f\r*U_vb\x08H', '\x0c\x0cIqb{'), [15])
    def test_case_480(self):
        self.assertEqual(pattern_match("YpVc^)7iIHuf\rDx\x0bxs\x08\x0b*?I)}N_nImZMM[+\x08Qwl\x0cnx\te\n:;a8}X\\H]\x08\\!\t~\x0bKUo7H3\x08Wxk6s~aNQ\rO?bf+%7M6@\rY4]m\r\rD'\x0b73\x0bJ\x0bH", '}N_nI'), [24])
    def test_case_481(self):
        self.assertEqual(pattern_match('B,W\x08BCS\rO%ST7WW \tD\x08\x08VDzO\rp\x0b\x0btj4T\t7TZq\nL%EGL!)m0{W\x08\nHL.K\r\\dQJ^\x0bMQT~zpH', 'J^\x0bM'), [59])
    def test_case_482(self):
        self.assertEqual(pattern_match('{^_\x08\t]\t\x0c-\t\'rsz\r\t\x08\'\x0bh=\t\x08,\x089F(b\x08R&\x0b#&J\\8xM ].\nsHvr\r\ndg6\r(_\r]r:{_\ntRwhm8\x0c,tsY7\x0cRL9d\x0b4\x0c2sW!%b /6"GH.>\x0by\x08\rS2\rL\'G^3', 'S2\rL'), [101])
    def test_case_483(self):
        self.assertEqual(pattern_match('A+\t /}q\rvBa\'\x0cr\x08mf\n\x0c\r2L}Hy\rm\x08J?0 q`c~\x08!;b2\x08)P\x0cn\x0b\n\x0bp F #.!Dd]\x08?YSdhBl\x0c"rE\x08(^`tiy*B_-3xU9S~', '\n\x0c\r'), [17])
    def test_case_484(self):
        self.assertEqual(pattern_match('\x0baXmBW}7\t^\t=*u,VZohJ5l.S\x0c5s\x0cCK2\n@P.h.H=\x08q<=\tjeqIccA@h,l4n"d\x0b4\tF\t\n{\x0c\x0b\x0cBQ\x0bp/ydZ*\x0c&.!\rc\x0cx@u_\x0c\n1\x0bt', '^\t'), [9])
    def test_case_485(self):
        self.assertEqual(pattern_match('\x0c;dZ%8uf&ao~\tWW(\\\n|T\x08@K+P4}(*fWD\n{=\n@\tb^.\t?es>\tA~\t,@L1e{/8<K_LZ@eQ\x0clF*Qj\tq\re\r<f', '\x0clF'), [66])
    def test_case_486(self):
        self.assertEqual(pattern_match('S\x0c"\x08YIK\r>9\\\r{w\x08gk^\x087\r>\n<r%2HeC\r\x0c2oxYE`Kv\r|sm\x0b\x0b\nF\x0c>G\r\x0bOecm\x0c\x0b\r\x0b\rH~', '\x08YIK'), [3])
    def test_case_487(self):
        self.assertEqual(pattern_match('Rm}Pe\x0b%M\x0b5I\tcT}aQ\x08o \t\t\t^\n!\t.\n \tN\x0c*0@QBy8oZAH-H\ro\n,l\t-pCfs:4E[9K<\x0b \x0c\x08*3_[UbPG9-lRGbdQ\nm', '-H'), [44])
    def test_case_488(self):
        self.assertEqual(pattern_match('7\x0c/\ttHZagWSFq\nB|\x0b}Ta=8l<U3a\tiO,(dkt\x0b>~y6.\x0b\n\n]\n\x0bk_bJz4f5eU\n\rnbtG5]6vHF\x0b\rKtiU<]\n0.', 'a='), [19])
    def test_case_489(self):
        self.assertEqual(pattern_match("&,\x08UQFpt7\ti+dMY`\t[5~\x0b2<'f#&%hp0DKjgE/F;`'};@I-n>\tk@RUC\n~:\x0b6\r_?ubWH%S\nAu\tm", 'E/'), [35])
    def test_case_490(self):
        self.assertEqual(pattern_match('h^)@Ui`SL4nn\x0c*!+E\x0c8p\'!{]~I\x0bjt"\x08\tN3?\n\x0b)B\x08nzb\n`\x08tTI:!X&1Bf\nBIf,7q\nfb\x0bI{S\x0bQ{\t\rwH,\nt[\\,', 'h^)@U'), [0])
    def test_case_491(self):
        self.assertEqual(pattern_match('JC`u\x0b5\rF*6\x0cF^(0w^q\x0c\x08f\x0c\x08\nGbV>rC\x0b`1(Vu\x0c!^ilf@W\rCwu j1%\rj!_4.3.:m\rGvLv)#!/0A][C', 'u\x0b5\rF'), [3])
    def test_case_492(self):
        self.assertEqual(pattern_match('[t~ba!\t</w3_)z4\nak-Lz\x0cQpjW\x08Dl].bL%e\x0b\n%!\x08Y*\x08E\tIc\x0cG+YQZ}C/~;WQ,T[>\nT\nL6\niWkgm', 'T\n'), [65])
    def test_case_493(self):
        self.assertEqual(pattern_match('4)^zs1e\x08Fxoa\x0bz\nA`,\x08A:wH5q\\+\no\n!,@\x0c7_\x0b\t:\x0cbyG6rC8o=|T|*k\\kQugBe\x08rt\x082d\t\n|bI', '+\n'), [26])
    def test_case_494(self):
        self.assertEqual(pattern_match('0M=2F)5q;u^\x0ct%Tg!Y* \x08\x0b@T\t(b\x0b\x0b1k\x0c\x08d\x0c\re2Z>~qm\ri%%E::\x0c|MR)\x0bKEE5HeaLLFW9U^[X}o\rE@O.#:\\X|}]/3#G\t2iJrP:"', '\x0b\x0b'), [27])
    def test_case_495(self):
        self.assertEqual(pattern_match("\x0bHM;@\r,\t,UzF 1:u'e\x0c:Ed\x0cU3O.@I\x0cr|\rY<+k\x08Z\rCG\tx^W+EK*?\rAn;2:c\\d>", '*?'), [49])
    def test_case_496(self):
        self.assertEqual(pattern_match("L\x0bh)\x0bHYSV\t\rd\x08Y\x0bKlgY(\t\r0+6j\x08KR/fvDWykb)\x0b\t52b,\r\rWW2K\n Z4\x08\r5zf('/)J7\n'\ny eWkf\t0-;*;#)*=0(f7K", ';#)'), [79])
    def test_case_497(self):
        self.assertEqual(pattern_match('FMH0~85W\tB\r\r\t1\r (mTg\x0c\r#+6`k&y5g\x080\\S 6><fb9x\t<\x0bF1\n%\t }oS3^\tuW(bGqt\x0cTH7UYcI4c2?:', '&y'), [27])
    def test_case_498(self):
        self.assertEqual(pattern_match("l&\x0bE6ycHJU+a\rCfM;\x0b7'<\n>\x0b\x08==W_<k[,\x0bv\r\nG\x0c20:B\x0cR>Y[Q\x0cvr-iO#pMsh.\x0bq3\x0b.\t\x0ciOfq\t0.sX\x08[\x0cQz}pl*@v7B\x08VrIyxf2%s<", 'a\r'), [11])
    def test_case_499(self):
        self.assertEqual(pattern_match(':4d7G\r\x08CLD\rpuWx\rq@\x0b_\x08XQ1O~\x0cl\nZw"\x0c\tb><]d\t\tCIA*Own\n{\x08\x087U}<c\'\r\tGqJE\x0c82VZ\'F\rR-R7~\x0b@Vbav9l*\n\x0ca\x0b\t+B\tLY;|/\teoe9z\x0c', 'n\n{\x08'), [47])
    def test_case_500(self):
        self.assertEqual(pattern_match("i{c8@INwqC7+xd\tS0Ch|\x08d~Go{s\n\n^:6*>\nB1T_z>\x0cB\r'&\t\x0bh\t'\n~=-C`x\x0bcU\\)R17a{1I\rgJ`[ SDW\\Dq'3H\x085qDz AjoX\x0bAAe\nq~n\tGA5]v", '[ '), [74])
    def test_case_501(self):
        self.assertEqual(pattern_match('\' *e^kY*6v_x\x08f?n2L/(],9\tc\x0b\x0bw2D\x0cB\x0chbv7g\\T\x0c <NU \t +As+~t>\x0cVe:3n\t?\td"&\tx5`.uf%9B (<r', 'uf%9B '), [72])
    def test_case_502(self):
        self.assertEqual(pattern_match('%NJ@Hx(Y\x08Oa]qKCtD\\sxc13\x08xHQ]ai\r!;16Z\r\n;l\x08x/\r D\x0c*&kX|0Kw\x08`/\x0b\x0b\x0c^\n>\tg(\n2n\x08b]\nWr?\x0c|I\x0c%n\x08E}>2vH7^@pLj})q:\rq^.MlJ\n;\x0b#t=Q\x0b8T', ';\x0b#t'), [108])
    def test_case_503(self):
        self.assertEqual(pattern_match('d@\x0b{\r\x0cNOxtuAyk1HG\rR*\n,f!00=>\nR\n5/G\x08\nX+R1k))\n\x0byRC6\nM\x0b\x080Qv\x086N`ee\x088Vz7c', 'R*\n,f!'), [18])
    def test_case_504(self):
        self.assertEqual(pattern_match('?\x0c(8\r\x0bi\n\x0bCaFs}\ndgjA\\`\x0ca\x0b;-D0 \x0cf?Zq\x0c\n@\n`tfly\n Kon@62~9%\n\x0b)"`"),0+!8+\n\tu\x0b*R7qT_\r', '62~9%\n'), [49])
    def test_case_505(self):
        self.assertEqual(pattern_match('y6\x0b/\x0caD}`\tw\x0bLsn@ Xox=,\x0c\x08^6\x0b\tS&fE#\x0cg3EB\rgW)rZ\t\rJhuzN\r_JEO1"7\n\rD#wV\n', 'w\x0bLs'), [10])
    def test_case_506(self):
        self.assertEqual(pattern_match('E?\x0c\n)*\t\rh]]To.2qfOY.a]s\tW#mM]\x0b\x0bjkKbb=U}\\\x0b6K:f.EH\x0bQ\n50hSY\t\tq+*de\nyE.\x08_?x', ']To'), [10])
    def test_case_507(self):
        self.assertEqual(pattern_match('\x0cB\'\x0b\nI\ttB(";E?(_U*f:p&(\x08_v\x0cY\r:@dM<Yj\x0c~%\rwUSfW>D&\r`tKP^wm\tZj*}0+\nJ5OI\x0br]\x0cV\x0b?q\x08\n\r^*\x0bDU\x0buybKw&v\x0bKqo^iuBz\x08', '(\x08_v\x0c'), [22])
    def test_case_508(self):
        self.assertEqual(pattern_match('Aj3:\x0bq\x0c\twSB\x0c:#<ke[\x08?\x08[pw6s|2E|a1\x0cH\x08|DZp\x0b!Qe\x0c^Owc\x0b/(p+]6^eS}Bb.u.haKq@Iui);ucg\nH]6VuhEo#pFEqc', '\x0c:#<k'), [11])
    def test_case_509(self):
        self.assertEqual(pattern_match('13r4V{)St]`u;\r:PSq38_)s6(F3Je\n*KkS=yF*\x080pT<\n5fb\x08iJ\'\'\x0c@j:qk`\n`mq\tsV\tsfn?\\hRTnh\rO/)\x0cW\x08Q\x0c"\t\t%x8=Evdv\x0bpLN\nE~_76W\x0c', 'x8'), [90])
    def test_case_510(self):
        self.assertEqual(pattern_match("eSA\rR<-tD\x08dB+\n#eSh}\rk\tZ\x0cv+~}xh\tM#'8.\tx;\tM%+*6[3\x0b0ei<h|M9qo\x0cib4 H", 'i<h|M9'), [50])
    def test_case_511(self):
        self.assertEqual(pattern_match('<\t\x0ct6=@_<#mP\rQq?_kj\rw\x0bBt"\r1KKDhX7^\\D\\hHP\x08TRB\ni_NF\\\x0c\x08u@J#9k0b+?m\tn \rQJjo^Ae\x08^6\x0cH\rrJb\n\rw:}5\n\x08|0/-n\r\tOt,T6p{k\x0cGM', '\x0c\x08u@'), [50])
    def test_case_512(self):
        self.assertEqual(pattern_match('oE3n\x0c\x0c\tld\\\r]d</\x0b\x0bkC\x08<q"\x08\x0cvZ"Y\x0br5WP<Sh]{\\d\x0bD."?h}rd0{H\x0clRt{?OKc[\t\'Ngz.,x@CBa9z2k\\82gLl[__/Wyq2g=q\x080', 'Z"'), [26])
    def test_case_513(self):
        self.assertEqual(pattern_match('3;_5\x08`,e)rgJ(?9<DG2%A\x0cIT/N@-WC\x0cGO)p&`kh\x0c\x0bK\n/zh\x08U7\x0bwT\x08h7^Y\x08"a f]\x0c:\'kd(^#,2x\n\x0bQ\x086\n?\x0c\r{:@Bjc%sx1/<3\x0cjF!\tY\x0cjeQ\tOeP+bP\x0b\t-*\n', 'rgJ(?'), [9])
    def test_case_514(self):
        self.assertEqual(pattern_match('P]-wA,L*#5YCeg\r&NKOH\t/skM\x0c}=HHjEpT\'A37Xzad&)ic\x0c[nE\t2}Z\nZ\tV#3cV/\\\t\rvJ|\n%\nO},]\x0c`q:qs-,\x0ch\r{"[W3s\x08/FQ7>\x0crP/x<?u.&TL\t^u]C', 'YCeg\r&'), [10])
    def test_case_515(self):
        self.assertEqual(pattern_match("'it\\1kb]Pg}k[lR-a\x08\x08X\x0bF'\ne77I2syo\tDeX\x0b~\x0cF*\x0c?Z:P~3%XAG-=k\r-\ri\n\x0b", '\\1kb]'), [3])
    def test_case_516(self):
        self.assertEqual(pattern_match('6%\x0c\ri1\x0c|tSUb^\rOcnTy\x0cF_Xrfs\n}\'WZw\x0cdGkfP2\x08Qs2-\nVmX@^5o"<|]\x0b.#cM\x0cEtJtiYOqQSHQ=Dzb\n\x08', '-\nVmX@'), [43])
    def test_case_517(self):
        self.assertEqual(pattern_match('K\'QH\tgTTF.I{Q\x0c(5k\t%#i{Cto*\x0bD>o\x0ca,}W\'L\nq\'pQ(s|]pLx\r\r!\x08{d"\x0b\nExj\x08TpE\'\n5,TT_\n6fd g4j;5;>W\r=^H,Jx-\x08', 's|]pLx'), [43])
    def test_case_518(self):
        self.assertEqual(pattern_match('!0U\r\rE\x0bfm\rnKXM\x08ad.W)eX7\x08QqcO!x\tePDq%!\tsCojq\r0+:6e\r9|\r\x08cec}\rJP4|"\x0bVcn!}ahGt\r\'QCsMYMye5,9h\n\x08^!m;hkG\x0bN}', '"\x0b'), [63])
    def test_case_519(self):
        self.assertEqual(pattern_match('v\x08f\x08\r!\n!7\n;\nBdvBoGs\t/dpipHKi\tdmE|\t7JnG&+4]\t\tD\x08*hvm\x0c{Cw=Zsw\x08\x08!\x08;\x0c\x08n2Wr}sF"k|Y[^dh\r;y\n4\x0bznle\x0c\r|\r`\t\nu\x08zV\t;Yac\t', '!7\n'), [7])
    def test_case_520(self):
        self.assertEqual(pattern_match('hl.\tB#@VVg]id:#N\x0c!1V%1~/x\x08-pK\x0c2Rz\x0b &Y8!p}+I+c\x08#7k\rD#\x0b\x08wC\nVIx\ng_^f18f', '\rD#\x0b\x08w'), [49])
    def test_case_521(self):
        self.assertEqual(pattern_match(' )NV H&"8:?+J2h~LN0\x0b/w@U8\x0b\'{&L \r4jWw\t{wb{~S\tc\x08E?U,[r?ax5t^+p\x0bH\x08mN6\r,/B\x0b<Ty', 't^+'), [56])
    def test_case_522(self):
        self.assertEqual(pattern_match('\t,wMrDRV\x0blp{(YPI3DdGO\nSnpk#t\n46frjtY\x0bw\r*yprB|\n\t6zl9@4\x0c%dZHqnW\x0c\n\t i\x0bbWb,\'\'ou^g9<fpQ!ZI-}c\x0cji"I\'i~o/<P\x082M', ',wMrDR'), [1])
    def test_case_523(self):
        self.assertEqual(pattern_match('ML2k(R1@\x0c\n:\x08\x0c4aC\x0c^^\n=\x0b\r,APxEqEn\rc}W+?\x0c\t\x0c\n6<5#rK3V?mWHXtN7.r/}]G\t~\tk&\x0bR\x0bZl@h\x08_{r\x0b\rWv5E)f[F\r', '6<5#rK'), [41])
    def test_case_524(self):
        self.assertEqual(pattern_match('lU\\\x0b2>x`\t\x0cs\x0b"D\x08Q\x0cbY[9v\'\nH{=:+3\x0c{_/3\x0c\x0bjT5TQLSr\rn&\x08\tnw\rX`^6"K.\r +:l\x0c:Eud\x08D7.gSZ\t\t\t%\x0bdi%9(\x0c^)9n_(nrI\\SQwbu#hnzuhj%]Hhz8', 'w\r'), [51])
    def test_case_525(self):
        self.assertEqual(pattern_match('\x08(}mC<\n*Z{z^!|\x0b\r6(q>K6dJ\nbW\x0cw-PA[\x08\x0bT\x0bA\r\t\x0c0U+^X\n\tGV[pMl\n^<-\ro\r3.\x08<V"2\t=rDY&L\tgr=\x0bI\x0cF\n\'\tiY."E\x0c\t|\tZo\nt.CN(#gbt\rpo7\tC\x0b8W)D\t', 'dJ\nb'), [22])
    def test_case_526(self):
        self.assertEqual(pattern_match('h&*u/\nsKD`0w\x0c;CF,t\x0c\t\r\n]NK\r:c<\t17N}\ng\x0c%/\rZNEr5\r0q\r6=P,\t\x08~hNb;XT]yU\x0cdRt00%FmU@o}K![zE0', '\x08~hN'), [54])
    def test_case_527(self):
        self.assertEqual(pattern_match('40\x0bf4,+eM\rk\x08Wt&na6\t3\t\x0bh@y/#|c\nab\r>\rU|hO\rq\x0bnO\x0cNlb^\t\x0c=\x08W\r_/m\\s~=ez\t\x0c\x0bk=P:\n\nq\t:\n[;=8\rZ]B', '#|c\n'), [26])
    def test_case_528(self):
        self.assertEqual(pattern_match("\x0b\x0b-]kKF%m~*\x0c)e_,%MTn5eGQ_W\x0b<:\t/BzK#-9&s1\x0c6\x0b\x08 _\x0cVF&\t#@~;k+S4?P\r*\x0cr}\x0chrHBfeSX\x0b?\x0cwj5T-FzSyH-\rY\x0cn''~*0Vr\x08 m8\tNU.L\x0b\x08+OYf@", '-9&s1'), [35])
    def test_case_529(self):
        self.assertEqual(pattern_match('\n2|,p@k#,#Cw4\x0b\r\te8]~i aV6.uL\tY\x0cPd\x0b9lHMD\r}\nC8/bO)b5\x08> f5m/#\teYR>Us\x08+E\nG\nRY/d*yNq>@\x0bkhj', 'q>@'), [78])
    def test_case_530(self):
        self.assertEqual(pattern_match("B74>4lW\r2H9m\x0cG'Z\r\x0b m/|9Ih\x0c))\nGa\x0bro8\x0b\x08\x0c\r +_\x08DCvl%T\tP\rH@\r(@w\n'Y!+\x0c~{,19o\rApz!Ys'y;\x08q_\x0cv#9=g5\x0b\x0cKH", '+_\x08DC'), [40])
    def test_case_531(self):
        self.assertEqual(pattern_match('5yBQ[nn/\nH\r,yF3j\n\t>\n\x08p46;\x0b\\hh\rv8\x0cek;zTxDPCDW?py~y\rn\x0cN\x0bbFH\rJ\r"(\n_j\x08d`vy~\r\x08(\tV8!-MWWzn\tTVo]R:cE38\t<La[phE\t^\x0c%"\t', 'y~\r\x08'), [69])
    def test_case_532(self):
        self.assertEqual(pattern_match('\x0bD[\x0ci`:VX\\V>-#|H~^85cuA\n-l\x0cgD}D\to^SHH\r,Z\x0br2\t\x0c`O\x0ct8[b\x08-&\x0c;Y\r;\x08T\nbf\tX=A3RWMs"#\x08\x0b)d\x08.r\x0b@{lC', '-l\x0cgD'), [24])
    def test_case_533(self):
        self.assertEqual(pattern_match('\x0b%3Bw[wr,4W#lazxF\x08,z6pSIS+R\x0b(<v\t1B\rI5nwp UD52r.n\t+\x084biR\x0b",\x0c>Ew(s-yB\x08Z^@k\t!w&\nLc#L#5\tk&1|\x0b\x0c/\x08-E*Hv9M', 'c#L'), [78])
    def test_case_534(self):
        self.assertEqual(pattern_match('/x0p3\x0b\nLZ\t\\P\x0c\n?\x08/g"@\'m"eve\'\x0b\nvAP\njdn/i\n\x0b\x08b8M=R&A\tb0/QB\x08"fx\r\x08,\x0c74-a|\r07Lg.|\nd!|\x08bW{h<Ij({\rk\rr7\nS-E\x0cN7G9', '\t\\P\x0c\n'), [9])
    def test_case_535(self):
        self.assertEqual(pattern_match('PH!\nZ\tf)Rg\x0c\x0cd\r(9K\rK>:|C\rj3\x08\x08j\x084R\ryFcXtY\x0ctq`~/\r\t072:\n\n`hzV*o>6\x0cJyXSYslg4jeD>Gy>\n(>\x0b\\\t\rN\n', '\ry'), [32])
    def test_case_536(self):
        self.assertEqual(pattern_match('=\x0b\t\nBD\rbs_+rDa\r(S+\x0c%\r@"z2\x0c\'Hvwt\'\n[7#O]x-\'\x0cI-dA\t 2kV\\iN\nA6Ck1o6T3[H!^\r\rQhXh\nD`]]o;', "'Hvwt'"), [26])
    def test_case_537(self):
        self.assertEqual(pattern_match('Es}m\nkb7_rM!sc~\x0b0\x08!B<:\\hW-\x0bu?\rysRc\x0bg\t&VZ.P-\nXPv#M\r^\'\x0b\nM}i.A\x0c;3MHS}>\x0b.-a|X"\x0c*q_\nR~h\t*M0|Me', "M\r^'\x0b"), [48])
    def test_case_538(self):
        self.assertEqual(pattern_match('\x0bS5nM{N2Rul14]0\x08Sboj1L\x0c|{\n,\r\x082BRK`9M\n_9Z`NnuAIxYz:e8c8O_EF%)Q*\'\t6\rq\n\t\x08nol/c(.8{~&H@\x0b!\x0bAEvekrUY{M0bH\x08"9', 'Evek'), [87])
    def test_case_539(self):
        self.assertEqual(pattern_match('i\t|3rtE\x0ci\n\x0cCP@vQbFe`^`CIelO&k<xg\x084\ro&p\n&E>Ft6?`\\ktuy%\tF5_\x0bb;lh{\r\x0cRX*\x0cC>;h\x08F\x0b\rk[Z\x08-b]\x0b\r8a\x08Ck5\n\x0b^[}@4x\x08dZ\x0cT3\n\x0bV\x0b9hz', 'k<x'), [28])
    def test_case_540(self):
        self.assertEqual(pattern_match('yg(GhI+q{pX{a|x8s&^\')x=[o7REXW8YYM\nM\nB8Md\tL&\x0c.o,b>-\nf2OhUY\n\n?]*\tu0e\ng\t(->"XA\t8 )O\rY\x0b3W;=4PU\x0c#Wf', '(->"'), [70])
    def test_case_541(self):
        self.assertEqual(pattern_match('vWC\x08d9K99 6{O\x0b_\tfK`7F\r/m\t&B\x0bzhj\rxM\tF\x0bW,v\x0b_\x08z=]F\n+MB]\t|*g\nQT%ymYNc{MB\x0c>rY( M4v', 'xM'), [32])
    def test_case_542(self):
        self.assertEqual(pattern_match(':\r\x0bk\x08[Xq\n-0=xNx.W_\x0b_}\r^!9\n #cb<D\x08/}1LxXBu\x08Iv%}\x08D<Zhi>*FGj+\n-', '\x0b_'), [18])
    def test_case_543(self):
        self.assertEqual(pattern_match('5\x08q`jZ:p\'}b6^ta+\rT{=1\rK^\n:O\t-,S\x0b\n\r{MXA J\x0bk\x08B\x08NW&}@zlj|@>\teL\x08\x0c^7 RoV<*gH~\x08wB22u4Q/HKp%|oADoNme";LFlu\tbf`\tu', '|@>'), [53])
    def test_case_544(self):
        self.assertEqual(pattern_match('{f0gE]\nZL\r^L/\rxh\x0b\x0c/\nW(yh_\n\')x?UJ(!J\rO\tf5N%Y&Xxz"\x0co\\L8yK:i>l\x0bgm[[HGF7\x0b}zwt\x0c%\t\x0b', 'W(yh'), [20])
    def test_case_545(self):
        self.assertEqual(pattern_match('ii>jGPCQ=H,Q\n\r^0\x0bPn`m\x0c\t3#|\nx!=wn\x08\nDE\x08?.\r%#\x08k=\x0bN\x0c|\x0bHl\r&V!|Y!EK3%\x0b', '\x0bPn`'), [16])
    def test_case_546(self):
        self.assertEqual(pattern_match('\r}-.S*=3nbq^vG\niRQrLY \x08Je\r3_8\nh"4693[/Tr:4Z\x08m.5^2\x0b=)e\x0cG"20i\x0c[f/Tf4f\nf#`n\tL?K\rq\t\x083~a\x0c7\nz\nAQ)FX\x0bod\tfuj{Ivm&?8\ta.HJHx<G6"l\x0c', 'f4'), [64])
    def test_case_547(self):
        self.assertEqual(pattern_match('s0D\tRV\x0c.K\n_54\x08YXW(x*FED=\x0bYpo\nD\x08\x0c;`;&mW=Y9m\tBv\x08a{#:\x0b4\r\t&=\rb\x083.F\t-46r@\\0?*|A:Lw\nN?8\nfEU:4l-o+', '\\0?*|A'), [68])
    def test_case_548(self):
        self.assertEqual(pattern_match('~Ph]M\tQ:Z[;^YTVq_NX:%\x0b\x0cBEDbbj?\\T<xLddby\\oX\x0c\x08X\x08Z4P\r\rg7v@BxYL)\x08<@j', 'Vq_NX'), [14])
    def test_case_549(self):
        self.assertEqual(pattern_match('\x0b-2%8N\x08\x0czg~Pq\rrlF7fS\\iN/nS\n@!:#oJ1zhj\x0b\x08W/)}*b?Kj.\x082R&N4 <\x0b\nh[.-\x0b\x0c7Qf\\!7\t \x08x\x08\nK#\x08,!', '\nK'), [76])
    def test_case_550(self):
        self.assertEqual(pattern_match('H\n9/T*o44\x0832\nL\x0b\x0b\x08Z\x0cCMu\'Vrb%=w_\x0b\x08u \tPvf\\&OW\r/\x0b\x08!=>H"xa%d#\x08#\x08\x0bir\x0bb&.N\x0c\x0c"w\n<=.&WyLH?', "\x0cCMu'V"), [18])
    def test_case_551(self):
        self.assertEqual(pattern_match(">|m@\\\x08t_sd]b=a\nNe\rU0LaC|\x08[*lFV\rm+&\n`yzk\n:zq\n(v)RPIQBF]'?{\t ky", '\n(v'), [43])
    def test_case_552(self):
        self.assertEqual(pattern_match('m<x(W<\x0c\r0T\x0b\nlLk\rMHD#\x0b5Z\'%Hg\t4Q/\n,+K\t\tvT2lX<||d#\')>\x0c7%1u=>\r\x0c\x083p"\rt MB\x0b?\x0c\nsDxNB-?0UI(JrI\\\x0c\n0\rUg%9', 'vT'), [37])
    def test_case_553(self):
        self.assertEqual(pattern_match('\x0b6%(,1\ne/\r5@dk*/Qx\nGrO`M\rsN}?nH"*\x0bfk\rwAPpEoG[N\'r]%Vc\x08Bh+t^\nS^Si)\rm@="AO\x0c8i^\x08\x0c6j"5F\x0c<X9Q}WKT"', '\rsN}?n'), [24])
    def test_case_554(self):
        self.assertEqual(pattern_match('|B\r~e"+\x08\x0c\x08<u[HHSPTD#&\x0c0\rRaoz\r\r!sL]lwfn\nH/S4ul44bYJ\x0c@5\x0c#p\t\x0c\tx/lTqk\x0bP\x0c\n8\x0cO~ Zw\'vH\nnP0Io/Ow\x08q\x0b\'7u\x08v)\t\x08B\rVjyB^\x0b\x08-\x08', 'HSPT'), [14])
    def test_case_555(self):
        self.assertEqual(pattern_match('r<YA\tCv\x0b\t]!\x08xK\rT\tt*MArD\x0b]9_Fw_`z\x0c\x08x&.l\r<<U9Bv);-*|\\&\tQpL:\t1i\nL3aw \x08g`+\nFRM', '&.l\r<<'), [35])
    def test_case_556(self):
        self.assertEqual(pattern_match('v`Je\x0bAhh-\x08cF#\\\x08p\x0c\x0c\x0bG3T6wL\x0cOT.@DiyrSVIoH\x08\\u\r\x08U!\x0b\t1`1aQ]KF2\n\rLiroOrV<JWxwqq!\x0b\r9{y\t\x0cQHh\x0cjN!6w,M<!Wjta0X1\t:L3`?sqx^', '\x0bAhh-\x08'), [4])
    def test_case_557(self):
        self.assertEqual(pattern_match('%j"1\x0c \r<nlfM[p@02>SL\x0bB~G2\rwJ\x0bu\r\x08r+;\x0b}@f*]-x w|C\x08\\%[w*uBKwB%\r_WF\rHfyd\'(\t\\%\x0bQ?z_AFFwOxt\tVPv7J\x0b\x0bxRs', '\rHfyd'), [63])
    def test_case_558(self):
        self.assertEqual(pattern_match("a\x0cv7u+Ry0@\x0cm2?WpJ-\x0cTE\r})sg\nDtSR_!-@/\x0b\x08{L'`3.[ DeRU>\r}o\x0baNr\r]c`tOjZ", "{L'"), [38])
    def test_case_559(self):
        self.assertEqual(pattern_match('Shj1u\t9g%M\t+Q|A\x0bwg]]|I\'E|j\x0c02&4\x08d;eHnde\tH\x0c+\x08\x0b\x0c\x0b .RaO\rPWI\r!N\rv/\x08HR*\x0b\x0c^\rMK(c\x0bs"s\x084sK]F)kMy9K&6nbR', ']F)kMy'), [82])
    def test_case_560(self):
        self.assertEqual(pattern_match('\x0b\x08>7[:xo5)\x08Za\t4{e\t]u5@&2hzl\x08e}\x0bF\x0b{!Mw\x0c\t\x0b\n+\x08Fl\x08F\x08~/S+|Igb\x0b\t\\\n4\x08@3\n\x0b#@Z]=\tu3aDRi^ O^', '~/S+|'), [48])
    def test_case_561(self):
        self.assertEqual(pattern_match('*\rQC)"}#\nt~kb\\\x08\nt\x0b\'5g?r"M%_\x0c\x0cv\x082.=E1M^~\x0c5\t&;=N}U2\x0c\x08=_mF\tBZ\n\x0bU\n\tU\x080EsHbFm\tT\x0b\tW]\x0b\x0bC', '*\rQ'), [0])
    def test_case_562(self):
        self.assertEqual(pattern_match('b\x0boW=\rCC9-2kF*kGV[kFg}8\x08<p{#\x08I7w#q>CD\x08-uO6\rip[5\r0U34pLG\n~\x0b*?', 'CD\x08-'), [35])
    def test_case_563(self):
        self.assertEqual(pattern_match('5RNi\n!\x0cCy8yrBL7R\tx9@B\x0cp\x0cmSfBLCM\t^["KVJmp\x0be\x0czn\nvjf\n}t=\x08+5=ir!U\tX7\';F4ZoR?Li{=J\x0citu?R7Y^:q*\tX=x0\tWh\x0b\r\x08gpb}t\x08\x0chTI8r5bLJig', '!\x0cC'), [5])
    def test_case_564(self):
        self.assertEqual(pattern_match("Hi7%G\\zL\x0b\x0b\rH{l\n'<dEuW|\\\tlNle,X9=uqag}&:<4oDOC\r\x0bv\n\r\x088oPUyp\t)\x0b6+\\09ds`*NL4-I\x0c`|\r", 'uqag}&'), [32])
    def test_case_565(self):
        self.assertEqual(pattern_match(",'6_5Z\n\r%\x08KcR\x0c2,!\x08Rf/\nk\x08\\q\t5S(@5*H }c{'GTS;,O}n;8w\x0c0!\r^[|\x0cZne(k?\x0b", ",'"), [0])
    def test_case_566(self):
        self.assertEqual(pattern_match("v(Ru9'u.,~[R\x0c\\W3+22EFQ6SbQkI+7\tZc6Ah]fU\rZ\x0c\t\x08tj\r\x08+.\t0\\=L[\tZ\x0bqo\r:Ph:Eb.N+y9/q4l\x0cRE\x0c\rz(\x08N7\x08", '\x0c\rz('), [80])
    def test_case_567(self):
        self.assertEqual(pattern_match("\x0cq9^IK%xW\r\n\t\x0bm\n@o6\x0clr\x0c&bpBD\x0b\r\x08)Y\tOw{oe'C\x0bv\t4\x08\x0bD2U+@&QvI\x0b@xU\x08vX=\x08f\r", '\r\x08)Y\tO'), [28])
    def test_case_568(self):
        self.assertEqual(pattern_match("[\x0b4\tF2\x08[\x08(=i\x0cF/\x0bw0^^1:}kXjeu<\nP\rjQP)1p|\x0cbf\tXK\rAG'#)zS\r_@\x086\n1]\x0b3#h\x08\x08!h\x0b>[t J'v\x0b5v5\x0b)J\x0b}8t+2(", 'v\x0b5v5'), [76])
    def test_case_569(self):
        self.assertEqual(pattern_match('6UU#?Y?>Fc*0T\x08\x0b>|dW>7`+X\x08\tt=7!Z^<i2^d{P3HZojz\r\tR4\thC\rK\x08y&Adq\x0c\x08\x0bX\tf6:p"kA\x0b=\'0/\x0b@', '\x08\x0bX'), [61])
    def test_case_570(self):
        self.assertEqual(pattern_match('T|\'OZh\n_cVC_\x0blP37w4s\x0bL\tw`db"\x0ci>m6J3^7sL\x0c6)P\n0yfV\ni^H#%<_;Ekk\x08\rW\n~S', '_;Ek'), [55])
    def test_case_571(self):
        self.assertEqual(pattern_match('\x0b:ka\x08t3I(9`Z7}\x0c6\r\tcY`92Y9F7N_\x08]>z^\x08q07|/\x0b4}JWNZ\\DkR"4|\x0bz9H\x08_5/@#R0_e7B==S\x08`\x0bw. \x0c} yV&,<%&', '0_'), [65])
    def test_case_572(self):
        self.assertEqual(pattern_match('\\\nOZb\n\x0c\rg\nYWXx0@z-boVE\x08/l4ee\x08XX=h28:#+y\t\x08 Ts1NVJws3\r]q`NY\n=i\n@U\t@\rFSSWUM,V\x08lVsI3', 'ee'), [26])
    def test_case_573(self):
        self.assertEqual(pattern_match('0#Z.f/QL\x08g\n\x08j\x0c#Pb2\x08/v\x0bkOr&W~mkFb,a5umIp(\teT\n?xd\x0c?U\x0byHVTG#p;uN\x08sq=>0x\x08/\x083\x0c\x0c:\x08Q\x08Ysl5~pnl\x08,#_Re2\t', '=>0x\x08'), [64])
    def test_case_574(self):
        self.assertEqual(pattern_match('D\x0b\r}E[s\tS^PdCpAN/k\tZGaHEe\\se"Fr3,F\x08K~y4|6-bR\'|\rrh{0MjG-[\x0b~%\x0b~\x0cVr', 'dCpAN'), [11])
    def test_case_575(self):
        self.assertEqual(pattern_match(')F"\'CH!^W^Yk\x0bu&/Z?H\x0b`(V\x0bM/k%\x08_=L{B*9Fr\rm\t\tQU-Q%Xj+<3\r|\n{5PTf5+\x0c9\raM;H"\rB_V34X\x0c\t6\nWI;[,\t\x0bfb\x0cT>=}B5S,_pln`Z', '\rm\t\tQU'), [38])
    def test_case_576(self):
        self.assertEqual(pattern_match(":9-\x0bLSLo9v^>U\\@@+.r\x0bB,l0qGD0E|0BBAhA\\0^\nI\x083_uod\x0b \x0bW@'CEl\x08Z!\rOt6MJz", 'od\x0b \x0bW'), [45])
    def test_case_577(self):
        self.assertEqual(pattern_match('5)g:*\x0cQ\n\t~7\t2\tk\x0ci\x0c\te\x0b5k>-qE^bnM\x0c`VRra\x0c(b~A.{lCF?um9\x08Vb\\y_sJS\x08^2m\x0c\t!zeTO:^)/bG^_7wz\x0bO', '\n\t~7'), [7])
    def test_case_578(self):
        self.assertEqual(pattern_match(' >LA8Lw\n&pyJ`0?\x0cc%QME5\x0cd\x08F.grB\x08Diozn[d-\x08H%]fj\x0b?v+]6i\n\rf**l4>\t^8\t?Q~\rK\nY]u\rqv*3Hrz-U%\x08\r5\x0c\r\x0c', '>LA8'), [1])
    def test_case_579(self):
        self.assertEqual(pattern_match('Ij*{nL\x0cv\x0c5\x0c\rD).O\x0c\rnBI#\n:cy\x0b\x08C*/*c,|J7Tes2L~,+/&P>kDj\rM\t\\A4T/k;-Y,G|FU9rW\x08.]XHD:r`PA\r\x0cq~UdjF]S\x0b', ',+'), [43])
    def test_case_580(self):
        self.assertEqual(pattern_match('9"u;{z#\\&:glg5OEu\x0c\r\nOMe\x08JH1\x08/wm\x0c4Fj7\x0bxS T;\x08zD?1wV\nba\x08"saJ]\\\x08j=Z\x0cAD\rM,Csg\x0b\r#O \x0bZb,rR-v&lf!e+}G=\r\t5Bi\nILr[P\trI[u5kTy', 'gl'), [10])
    def test_case_581(self):
        self.assertEqual(pattern_match("[x\t52\rP\x08\x0cSO\rB\x08TS4F\n\x08\x08qt}c0g/]c\n^'r\rD\nr?L6l\x0c'tB\\Q\x08??E!\r(3Q\n\t\n[\nV,N;*@F\x0bUr=cj5V&xJIfGh\rVwJ|zLkXv`l9\x0c:D3Cf}+&\r", '\x0cSO'), [8])
    def test_case_582(self):
        self.assertEqual(pattern_match("w.t>\n\t#|k\x0bX\tbxVpYp\x0bJ!{TYc'a=;Q:\\)s_~h\r5#m\x0c(\n@\rRoT\n]\x08pG\no}\x080.R\r!\x08,gX,,HWF\\b7*\x0cr!ER}\rf\tP(w[;\rfn)z~Zt_aj))F'd\x08?", 'T\n]\x08p'), [48])
    def test_case_583(self):
        self.assertEqual(pattern_match('B6\tZ3i9ZV\x08sT:2z/9"\'`SAPm#Qa]]6m3jc\x0bbz@I\x08T\x0cA.\t")\x0cR;Qn3ggH<=6A\'\x08 T\r`\x08kFN)\x08[\r/T\r\risMtyH\x0b!=>0XaKGh0)\n\\Z\rz1b @g8', '#Qa]]6'), [24])
    def test_case_584(self):
        self.assertEqual(pattern_match('\x0b\nk_l\r6\rb9NNS\x0c\x0b) r)\x08f&k\x08&=_Aca\x08,^gjPQ\t@H\x0b\x0b3}l\n6eL\x0c\x08xs]o&&`Z%]e\nflD\nK=q9\x0c\x0cF\x0c\x08/F', 'D\nK='), [65])
    def test_case_585(self):
        self.assertEqual(pattern_match('\x0cERN^45=nEHoAeF1} @Oe\x0b\nM>&jr0M/U\tl\x0bM\tZ \x0ca\\\x08\tf)_ Ozz\t00*1\x0cG TZY\x08\x08R[\r/mbIk?.b_W~\tMdxv+n%7/zL\x08_4=51RBd', '\x0bM\t'), [34])
    def test_case_586(self):
        self.assertEqual(pattern_match('<-nTRyCbJ\x0ck\t_\r(\x0c0_qd41#qf ;@\tk]:C*\rmV:\x0b:o\x0cy&5!R\r&U)JW4A\t)?}"0/)W]s86', 'C*'), [32])
    def test_case_587(self):
        self.assertEqual(pattern_match('Mv\r\x08\x08.M@_\n2"W\n jH[r[\t\x08\n?Yr\x0b\x0c:Gc\x0c\r\tsbu\x08\t*xs@_s@@%Pmxx\x0bPj\x08S>\x0cRT+EZ\r7EhKG\x0cfjqdz\n3IO]RL?\x0bN\t4wt', ':Gc\x0c'), [28])
    def test_case_588(self):
        self.assertEqual(pattern_match('E{X\r\x0b\x08Y>YV! 1BtG\x0c@V`7QB|`\r}E:\t\r%Vg\x0c~Pm\rJA\n_}\x0btAi\x0b\nX#\x0cPD-&b\n?pA\t)A/v\x08aNW7\ts\x08,?\\\r/<PXa\r=\x0b\n`\tKg]\n\x08j\rp5r n\n8M`', '{X\r\x0b\x08Y'), [1])
    def test_case_589(self):
        self.assertEqual(pattern_match("\x0cV\x0b=\rAU\x08q\r[Zf't\x0b\nrf\n+5J}rkI\x0cB9)SsAO7LM|eXA\x08snvtlr|\x0b\\\rf^n2\x08qm7t|Q\tXf_bq]\nCL.\t\x0b*U\r\x08n]~A:zV_nuA5\np\x086\r9\\-zrr[!", '|eXA\x08s'), [38])
    def test_case_590(self):
        self.assertEqual(pattern_match('Fsgt\x08\t_"\r\rR\n\t#))Ap\nW zS\tU\tYw\x0b\x0b[|\r+<Z\t)dIt\x0b]Rwru\x08\nc&oO:9 \n1s{c\x0bWn\rs-\nyD\x0c0)\x0ctXZ+pXu(Q)', 'oO:'), [51])
    def test_case_591(self):
        self.assertEqual(pattern_match("\x08\r=\x08^Liw\t*r\tVs=\nD`2Ag\ta&\x0b\r|0]X\x0c\x0b@qV35;ubWhhc\\wSpn4Yi\rA \ndjwk\x0c\x0b'OrB~@3)\n\tWl&E\n\tC=\x0b}L-fB~]o\n)tNB*`r%=", 'X\x0c\x0b@'), [29])
    def test_case_592(self):
        self.assertEqual(pattern_match('Q}/ep>h `\nddWE~"\t\x0bXIS\t@\x0c^A!\\C\'SFL\\\tj\noy+/75jrp/\x08\x08\x0b:d]X8mz%*v&`\x0c/\n\x0b\nbraZ\x0cN_ynjC4i[=!', 'aZ\x0cN_y'), [69])
    def test_case_593(self):
        self.assertEqual(pattern_match('jlB`d)e,TN\x0b~\ts;02gJr!y(2@\x08U)41#\x0bN\nh."S*j9LJzR}yGtGHqewE#\x0cTu\x0c+vW\ri\n\r\x0b\tI\x0b\x0bI_s\x0c\x08\rEBg]', 'y(2@\x08'), [21])
    def test_case_594(self):
        self.assertEqual(pattern_match('H\x0b\r\'\r&yy+wy"Wz\x08.MBA8:`^S{\x08#V\tfpn|t^{dtWry2KR\x08MG?q0Js\rl&b\nhm\x0c3bPY@-\nRz\x0bL\rjhfCW@C', 'BA'), [17])
    def test_case_595(self):
        self.assertEqual(pattern_match('| H\x0bNg,dS-\\Ld\t-C01\t-#`d9`@3F9d;M1,h7DjG\x08rs\x0b=D-eY\n2;\t>S\\{R/A0e\x087roU-NXVtal\x08\nBp2\x0b|a', 'Ld\t'), [11])
    def test_case_596(self):
        self.assertEqual(pattern_match('"Z\tX\t\x0c+UyWf@dpT^v\r\x0b`\t\n\tInv\t.\t>\tC2?m`v/By<BRb4\r\tOzP"3t\rs|p(Xv#\x0c,)2`F]\x08\x0cV\n9s', 'p(Xv'), [56])
    def test_case_597(self):
        self.assertEqual(pattern_match('"smH;oor;;2\x0cq&@f6|F\nH;uz\x0b%-1\x0b4?\tj7%47GmJR4\tGi(dj.|q\rw"|L\x0b3!M&!3;G\t\rh31\n"-D7c17#\x087\x08"!', 'H;oor'), [3])
    def test_case_598(self):
        self.assertEqual(pattern_match("\x08\x0b^\tLb\nY\n\rI&e'K0SX1U}{\t\x0c94`!Uo7 w\x08.\nv\tS\x08yE'- sAEt}4`nW79\r%o\x0cEVM\tHP2q#B \x0bb82JG0", ' w\x08.'), [31])
    def test_case_599(self):
        self.assertEqual(pattern_match('\x0bq0Iz3ZdG#DE9yd5X\x08q\x0c\rk\nIZ\\J\x0bU\t}t\x08|V\x0b33s-;@\x08<b\n.J<.\x08&x.\\TKU3DU%/\n!fe6VeX2\rx\x0cFb2,<\x0b\\dlNV\n\x08b\x0bf', '\t}t'), [29])
    def test_case_600(self):
        self.assertEqual(pattern_match('pY_"\x0bgf{`3;.b%4V\r3\x0b\x0bJ[\nU=Y;\x0cFk(Ta;.)\rn4\x0b\r\rHt7\n]UcO\x082\x0c\r\r&^tKM`]-', '\x0bgf{`3'), [4])
    def test_case_601(self):
        self.assertEqual(pattern_match("6IGa9DqX\\nw@RV! d<q\nso\n6^/Q3\x0caXS(DtLrz8'1O<\n\x0b0JerMH<p\tjyT.huaZ&\x0cU\x0c9l0\nm-T;tV\rsBPD\t>\x0cr)\x0b7o<U\rO|=M{w!0_8Pz\\\tfu\n\t\x0bY2.!\x0bL", '&\x0cU\x0c9'), [62])
    def test_case_602(self):
        self.assertEqual(pattern_match('CJ \nc~J\x08j%x2%6\x08)wwADM\x0cfN*\rAj\rB5uX\x0b;n\x087+Y"b\x0c-^jn\tGu4[\x0cb3:G^\x0c`h7GLEAi~8`+\x0b+dbtq5fh>nqjW+i4X\x0c<@v\r\x0c\'}5NMET8a', '5NME'), [97])
    def test_case_603(self):
        self.assertEqual(pattern_match("rP=F&O`^\r\nXF\tF\x0bY\x0bQQ\\s9o&DDOF\x08\nA7SY}@Np*/_tm'\x08.}\x0cy\tEY\rwn\x0b\rn!gYV]4\rM>\r`NR}\x0b\x0bV", 'n\x0b\rn!g'), [54])
    def test_case_604(self):
        self.assertEqual(pattern_match(':+R84\ts\x08RW<2[\\BE8\x0c1YfxG-)5\r\x0b\x0cI%r:\x0bJI7L\\=`\r\n\x0b8J>n,0f6Wd=Y!R9 \x0c5\rNf\nZE', '`\r\n'), [40])
    def test_case_605(self):
        self.assertEqual(pattern_match("NR]e~t4fD8J\x08\rd\x08(0KnZTC\x0cdN{xY~4C'AmGs\x0b\x08#h\x08\x0cLo3g:~E)C\x0b(\t=2n`2[B_r", '\x0cdN{x'), [22])
    def test_case_606(self):
        self.assertEqual(pattern_match('\n&jRx\x0c\truP\x085V\r\tKP|UaHN\x0b|b?R\x0c]\x08\r=+\x0b<\x0c\r{y\x0c(F%eZmfn+g#"uE+:\x08#D\x0cmXxlU{\'~WK0a\r2c{Re@-', 'HN\x0b'), [20])
    def test_case_607(self):
        self.assertEqual(pattern_match('WJY3DKRj\tk^oAUTIo\r\x0bfx7D^V>\nw\x08~6!G\x0cA.rh\'>\x08~;%\t!\tt{t^b>V\r7d[b53=?Q\tM\x0b\nJ\x0b5B@\x08"\rcM\x0c-\r\nBA\nCp\n+\nz;\x0b+\x08toSS&', '\x0b\nJ\x0b5B'), [66])
    def test_case_608(self):
        self.assertEqual(pattern_match('\x0b)#t IvOF!\naY?!`&\'t\x08"\t~iS\x08kT\r:\r,\n\n8 FnPe!oGaC\nGdUlVB\r\x0bC:gj}v*Jw\x0b!;\x0c\n\x0bVgh[Dz8tv4SM\r5/&vq\x081\x0c\x08#\t%V\tMI[H\nx\r\x0b;{8', 'M\r5/&'), [80])
    def test_case_609(self):
        self.assertEqual(pattern_match("\t2dKI+\r muHuAe\n\x08\\}*NW\x0b\t\nb\n(&YEy\nxC[\x08=\x0c_7TI\tS\x0bb\nm\tRi`)f\x08B\rrz3^m\x0b7r:%0\x08'%\x0bScU+4i ", 'NW'), [19])
    def test_case_610(self):
        self.assertEqual(pattern_match(';2d\n\x08}\x0bdk>{{cyThR\x08\tPtCQ.FszBkh1b\x0c5\x0c]\x0b#Q\\t]?&k\x08^qB\'\rav}.@VN\r.1J+\nSz\tgl\nGm\x0bkX?"arf{/`=:ys6B\x0cxV&q\nNtx0ZNY\nzHA)T\x0c\x0b', '.F'), [23])
    def test_case_611(self):
        self.assertEqual(pattern_match('\x0c\x0b9e]I+30_X\tB( *\x08%q6\nGQ\r\x0c\n|,uGu\r\x0bqo\x08X\x0c8\r\x0bA9/Pr\t3@D-\tRNcrJd2!g5-\r\r8,\r\r[\tI.\x0b_\r 9s2[\t/{\x0c\n\x0b>iD[jEjMg95u\x0bC', 'jMg95u'), [93])
    def test_case_612(self):
        self.assertEqual(pattern_match('+35\x0894,g/Z6*_HuBb\x0bU:\nzG%4P.`T!\x08b\x08\x0c0%e=e[\r5\t+6u#r\x0b\x0b[@_i.ZrE(\\A', '!\x08'), [29])
    def test_case_613(self):
        self.assertEqual(pattern_match(';\\i /\x08=o^\x08v\r)%kjvE!k}\nTs~\r\x08V\\O\r*4UPFr`\x0ca\x08Pw\x08 \x0b7\rGp\ny\x08)\nbm9"Mn\x08,(G>ekv\x0b;\n0olm\x0bY\x0c|', '\\O\r'), [28])
    def test_case_614(self):
        self.assertEqual(pattern_match('!G)\r@\x08ivE"{6\x0bF{|gofa2\x0c|wsja\x0c"ckOI\t\x0b`FdK)o\x089:p#r|\x08\x0ci=+1K\x08\tEu6\n\x08|}\\2\t\t+uD\rz\rK~\nx\x0bqwl=(', '\x08ivE"'), [5])
    def test_case_615(self):
        self.assertEqual(pattern_match('C[n[M9*\x08F=QOx=++9r45\\z\x0cr!u\n9\\%[6ZtZwis&\r!\\+e"dGA7jSVuo/PP\x0b"TR-[mr0y;(K!pceI1aa\x0b\x0b4p:rs!\tq\x0cr`\t\'4&\x0b\x08\n?\nb', '\x08F=QO'), [7])
    def test_case_616(self):
        self.assertEqual(pattern_match("Lx5w;]:\r@T=ok[bj@;0\x084\r8\n@T \x0b\x0b1bxw\\HVIBgM7\t,s\x0c<b\nm`\x0b`WD.,1k+\r{ze\nEt|a\r})fx0V^x]>'4\nM2N\x0bw/\x0cK8R", 'ze\n'), [61])
    def test_case_617(self):
        self.assertEqual(pattern_match('DRZ:F\t(D5#!Sh"%g_0w&meqD;V\x0c|X\x08sT\x0bMIKtOp\ndl\tkw/=D_bXq\t]:\r\x0c]\x084T.D[&{\nCBxcT,vX/sPE/\x0cZEA}\x0c\x08\x0bF+', '\tkw/=D'), [42])
    def test_case_618(self):
        self.assertEqual(pattern_match('T~^\x0c\x08\rW~Y?={V\x0b#nd~t\t\t4<q"tQB5~\x0c:H(8K-eC#\'\\5hQ4yL\x08)\x0bG,GR^:jp\r-Nx<\x0cfZ!4?]M\nf6\x0cg[h', '\t4<q"'), [20])
    def test_case_619(self):
        self.assertEqual(pattern_match('Wy{JXZ\x0chg {0y@.\n]\r5Ao\x0b\x08H\x0cN7T?q>Z`Fw;"f^\x0b0H6dXO5\x08\x08|s\x0c\npXizIRJ![/\x0cTxDIvW\t-\t\t/\x08#OX\x08F.e>=693\n]FCYb`n!\'fK\x08R\x0c^:j5N\r\x08', '#OX'), [76])
    def test_case_620(self):
        self.assertEqual(pattern_match("2OtsPgy?d0|j\x08y\x0c~\t\tN4p1;N-TC%\rH&QBQ\r<@N?}\rRy1g>s>'\nC\tA6UaC_4Q#\thSJ\x08v[\r:XM\r\r3=&{w LhN#\t\rwz", 'H&Q'), [29])
    def test_case_621(self):
        self.assertEqual(pattern_match("7f6\n{\rt\r6u}\rmv8<t\x0b=ycC&_)\t3A~Wq}B*M~9ftXFi\x0b2\tiN\t\x0b>);B\t?'+\nji\nIM+K0(={M\\7\t\ty\x0c", 't\x0b=y'), [16])
    def test_case_622(self):
        self.assertEqual(pattern_match(">6\t\x0b(?s\rJ~\x0b~9\x0b\nx\nO?\x088&\x0cs&h4hZ)+Els\n.3\t\x0c\x08\n_~Hp'\t`_LnDK\x0b\x08D_&|\x0b\x0b(f<g|*k&_\tydjl\x08+h)F\x08\x0cC*d*?|\t\x0c<#4'\x08r:` \x0c\n%#\t/", 'F\x08\x0c'), [79])
    def test_case_623(self):
        self.assertEqual(pattern_match('k#3h\ncM<c>0[&D\n;QKc"JCf/\nZbLAp\x08jjt\rY\t\tP]\x0bsHo^X)r\'th\t3:bX;(\x08G\x08', "'t"), [48])
    def test_case_624(self):
        self.assertEqual(pattern_match('\x0bFKj%uaG\r%\x0cQ=\x0b\njz&]f_0V\ndzb\x0cuZ2CaiLyP#\r\x08xvb%MueJKRnJA\x0b3O=2j_0li~:gPn\x0cux(\x0b\x08=k\x0cL;Qg', 'A\x0b3O=2'), [52])
    def test_case_625(self):
        self.assertEqual(pattern_match('Q+\\\x08Bf#\x08fQz*D\r~_\ng\tS3HA\tRU]\x08-cpbui?1%ObA%\nKqPTLnI@%YjSc}+zQ26zsgDzD_{]|\rC8n`', 'U]\x08-cp'), [25])
    def test_case_626(self):
        self.assertEqual(pattern_match('gn\tJ/J%\rj\n\nn\x0b8l\x08,\x0boJ^Q@\'4S _0P;f5\n"(}.QZbj\x086Y\x0b\tSHP(k\x0crQJ0\x0c0)\t\t/_%q \x08\n%`"PqTbu)VpH41{\x0c@5J\tjR\x08\x0b\n3\n\nc7\x0c\tg\tQA\re\nQ', 'f5\n"(}'), [31])
    def test_case_627(self):
        self.assertEqual(pattern_match("\nZj\x0cn]d=,{mEM7\x0b^n\twt:0)4G\x0b\x0b\t\r_oo`X!ZP\x0b\tuFGew\x0bR*%@O\tY\x0br|l44\to\x0c\tO)K\r\t+''APH?Tke[WCHfN9g9U}5\x08b0|eq>\t0{\ty=\x0b\tHRh", '|l'), [54])
    def test_case_628(self):
        self.assertEqual(pattern_match('8-\x0cc^\rgM(W^Wrk\x0bA\t9Chh]\t\x0c\tu8"]-;vZ\x086=\n@}EpB=\\82\x0c\x08|Z\tP:]y\x0b4b?1B\r', '8-\x0cc^'), [0])
    def test_case_629(self):
        self.assertEqual(pattern_match('a\n&ar\n<\x0c]\r\tpV8[\x0b\\\x08~o"\'(%\x0cAs\r\x08a\njDh)rq=%*\rQNANQz2q}"," 6ASb]HOf0\t17\x0br\x08\t)`mdc1i\x0bj7\tFV08\x08U+\x0bQ`\t\x08pRz)f\x0bPq\x08\x0b6N90#\x0bN', '\x08pRz)f'), [92])
    def test_case_630(self):
        self.assertEqual(pattern_match("N?,~gBhw\n\ty\r%dPj~\x0b\tl\r\x08U@]\r'K\rrftAu\rinDzA\r\x0cC#y)1\x08O\t\t;z1X\x0c{R?cSF", 'U@]\r'), [22])
    def test_case_631(self):
        self.assertEqual(pattern_match('6\t_~kXlOK\r=%\t8\n5K^H\x0b18dLM\re\n\r}h-\x0cu0\r)\n(D|QAzv*R@iR7\x0b\x081\n-U28t|\x08\x08\\G@X\x0c0\r,W,oBFX\x0bM#\x0b#\x08\x0b/i|!fbU4Tvn\x08F@\tu~W\x08Na;\\36ehcC@u', 'K\r=%'), [8])
    def test_case_632(self):
        self.assertEqual(pattern_match(']\x08X+\x0b\td*9]1i\rC\x08;{xEzqF90HJ\r"%\n?bL\t6\t< "q\r\x08sFI\tZ0\r`\x0bj\'\t\r\x08@\x08mE\x08\rgB*\t4(qoP?V(d\n 9XH\ru\tR\\0+P7(s\r`\rL\'|\tC6-.H\x0b?', 'X+'), [2])
    def test_case_633(self):
        self.assertEqual(pattern_match("N%\rt\r]k(p`/xe\n\x0be\x0b(\rM9.3\x08\x08\t,KZ'\x08\x08\n*{\ty\t\x0c\x0cWk\x0ccPn\x0b\t43\x08,\nbKtHXp<\x0b~\x08.V/\t5\tYX\x0bqI&70\x0b>?\x08UOWKu!~7&wa\r:|5\n", "Z'\x08\x08\n"), [28])
    def test_case_634(self):
        self.assertEqual(pattern_match('D6Nw&\x08!\rT\x0b]pB>"D%\t\r\nkha<!r<\x0b-f[?Rp\t6]\'UxEzG,o\r"XGiR\x0cot\tO\x0bK\x0cvC=\x0b\ti@sJ<TBG=5BN&/x!\nwD\r\t(Vquw\r)2#6hQ\r/!HM?4AI-G4^ha\n@J\x0c', 'XG'), [47])
    def test_case_635(self):
        self.assertEqual(pattern_match('#KU8\tI^\r3\x0b@C2+\rw7-};xAHb5|G\t.z?Z\nc\x08\x0cD~mN~\x08v\\=e=H;\x0c`yx[;P/}7/~ve(', 'H;\x0c'), [47])
    def test_case_636(self):
        self.assertEqual(pattern_match("|F\n\ndV;\tW\n`*\\br1tu\x0cpHo3\x08\nt&-yB5sw7\x08\x0b&O\nDBf-}'JcZkp\x0bth\x0c>|a_4\x0c%jLfoIY\n\x08zG,Zc:!\x0c>*GVK", "'JcZkp"), [44])
    def test_case_637(self):
        self.assertEqual(pattern_match('^P\x08s\nSv\x0bQyz\r1@f\t_!dPp\r~H\x08d5y1\t<\x08GW |tEfOk!Z](i)7\x08nByA(ln!]2_\t2qPztpOLs ~\x0c\\0tRo:\x08', '<\x08GW |'), [30])
    def test_case_638(self):
        self.assertEqual(pattern_match('>)xE(\x0c\r4tSr\t\to\r H}\n43\n#p?\x08m\x0c66R?\r2>\x0cF\x0bok*\x08\x08\t\x0b\tnWz*~1k-\tM|5wniR\x0b\r\x08\nw\x0c}4~3\r`Z', '\x0b\tnWz'), [44])
    def test_case_639(self):
        self.assertEqual(pattern_match('\x0b<G\\Jao/S{]\x0c~\n\x0b5QK\rN@i^=s{(\\7F\n\x08\x0c\x08Sak`c\rCk(o~E<\x0c|mEW+/0k?:Y\x08-\x0b%HK u', '7F\n'), [28])
    def test_case_640(self):
        self.assertEqual(pattern_match("K2%\r5_ScdNL<|\x08k{\x0bZ\x0b!%v\x0b\tT>\t\t:\x0c}n]4=?S3\nHL)\nr<n6SqNZA\nBYu'`DHlW0sYy|1C\tB+O.\x0c5&r", '!%v\x0b\t'), [19])
    def test_case_641(self):
        self.assertEqual(pattern_match('?!1^HgAuGc8\r\x08/73N*9vYB~>v0UM\x08Nm\t^Z?\x0bdnl\x0b%G`ZXjf\x0cJy\rxLc\n\n\x0b60E/,6;o1', 'B~>'), [21])
    def test_case_642(self):
        self.assertEqual(pattern_match('K.f^)\t\x0b}"P()#\tl:"<O\r}`:w3\r|gxQ\x08_BKnJBW/ft 0{sB6{\x0cBx7XBK:\n,PA5oiQO\x08,\'T7', '`:'), [21])
    def test_case_643(self):
        self.assertEqual(pattern_match('G2:,?M*(L<Y\x08E.E-eP\x0cBd}GKOw\t&J9-\x08`P.\x08R;+AR,F>E]Gxl\rtg+]=i@-K\x0b7\nt-?\x08oP\x0b\x0c', ':,?M'), [2])
    def test_case_644(self):
        self.assertEqual(pattern_match('Wvu:Y[>DGb}B?(9\n\t%\r\rba)\rZ\nUFh-;P3HN\n<*\rl8\x0b[:Hmgy\x08\x0c\tC\rnGBYX\n0=ja)uG}\r\x08\x0b2,}U\x0c1/ymtaJ-)\nh2', 'ymtaJ'), [77])
    def test_case_645(self):
        self.assertEqual(pattern_match('Gs"\nB~kH\n~pS2\x080p2|q!B\r\x08.3f!Qy0`2t\x08\x0cB\x083>58\x08\x0bNEIbUbyhqRu@Q(\x08`-p1D~\t8\n47n,Saf0\n[?c', '3f!Q'), [24])
    def test_case_646(self):
        self.assertEqual(pattern_match('tg~\r#\x0b#toi[\x0bfFtJ\x0c\rv\x0b\\c\x0c6w\n\x0cTx0m1\tOU)\rHu(lKWl?3qI,r1\x0b\t"u|1\tVrWr:>_q\\_0ZX:QhqqPFS\rky\njc^SRyo.\nSXQ\n4Ta0-\x0c\x0b\nt\r%y6XX(\';rO\x08\x083D', '\x0b\t"'), [51])
    def test_case_647(self):
        self.assertEqual(pattern_match('5\x08\x0c\nKIk?D\x0c{\r8d^nX\\/\x08gmaa/N\tqRxPW-\x0bwT\nPq[o0\r8@2J6\n<bb\x0cH\t7:plr!N\x08u\x0ctv\n{6UpD\ns;lm\tOF_}b!b\x0bGH', '^n'), [14])
    def test_case_648(self):
        self.assertEqual(pattern_match('&n,aaR\n3.\x0bPa&|)<;Vox)6c3u=HblEE=\x08b6\x0b\n5aMAWL\x0c\x08\x0c\rM\t\r\x0bStg&>AF/q\r7l0\x08FI~_"};t&B=jiUe5Qz/;%TEJd\x08Yq\r_\x0cXv[52z', 'AWL\x0c'), [40])
    def test_case_649(self):
        self.assertEqual(pattern_match('pv\t<Rb\t\x08G`^xa\x08k\x0cVo^ZDiO!Aq\x08\x08C\t~B\x08v\x0b\x0b=qjo<nxV\r\rBh)im[bGs2&#sMUuC\t>{\x0bs\n\x08iUJ+O\x0cI%x/G^m:Ar\x08pz!\x08w.TZ#oTyc^4+F\x0cZ\x08n2<.', 's\n'), [67])
    def test_case_650(self):
        self.assertEqual(pattern_match('\x0b\nK4z\x0c}I\r4>/{eyL!d\\CAvHc\'qj4[\x08\t<\x08B!0\t\x0ct%B51LFR1&3\x0b+1\t|"67\x0c;\to#g]\\x', '\x0c}I\r'), [5])
    def test_case_651(self):
        self.assertEqual(pattern_match('7P\x0b\t7^1"2dTcaypCDM8\x0cM\n~\\D^C5tG]\x0c%\x0cRZ\x08@  JR\tACV>Yy\t#1\x0chV\x08w\x0b[NI\x0c`\x0b)3\x0bQ\x08ySyf/(O', 'ACV>Y'), [43])
    def test_case_652(self):
        self.assertEqual(pattern_match('G?G,_\t\tnj/L\r+BL\rm\t>\t#\\jJm\x08.%`;]=XlGc HYE01?"vb\x08\x08\x0bWi65+[Ui+\n"hXr\x0c\r>lm8\rW>CD\x0b\x08#W7,e\r\x08!4/K1`7{S\x0b', '65'), [51])
    def test_case_653(self):
        self.assertEqual(pattern_match('~&[*QA\r\tF\nO\x08\t7cj\x0cnBQ\x08\tQ\nZ"XHQ\t[IId\r(r@%\tt-_G~*Y-g\n;OT\t\\\rNl?\x08Ev%FQ^X', '*Y-'), [45])
    def test_case_654(self):
        self.assertEqual(pattern_match('Pv263B8E|7\r8qERXplqQVZWuYoS*FV\x0bA\x08@\x08g=\x0b"~uI8\n^\rPG=H}]AS\\2g\r`TFCP\tag|>tfsBNA', 'ERXp'), [13])
    def test_case_655(self):
        self.assertEqual(pattern_match("\t'\x08\rT\\<S\nD`\nD#R<AC+}Q\r\x08Am.,5\x08S?14\x0b\x08!9Q\x0b\x0bG\x0c0gp\n^\x0b\x0cZK{NBk{\rmOy&j\n\rA;2z:aWpf{\to6,YPKq*C\x0c\x0cjZ\x0c,\x0b@\tG4", '\x0b\x08!9'), [33])
    def test_case_656(self):
        self.assertEqual(pattern_match("; w:k\\V\x0cu-8\x0888C?IwC\t\tx\t\x0cUXpjxE)i\nM?\x0c8\r}\r|\x0c/1?t?1\\?,)&7\r\x0cvV\\-\x0b!\x0c#!'k#VAby\x0c?r\n\x08mjy22&b\x08\x0c\x0c&{pff\r\tQ", ')&'), [51])
    def test_case_657(self):
        self.assertEqual(pattern_match('\x0b^\r|#e/\rq!5%\ne\x0br\x08V;b=z>Y\x0b\rpT>\rTZ9\t\x0c1V7\x0bDFw2UU\n)s\x0be\x0c\x0c|n( u\x0cH\x0b\\\x0bLpa0T\x0cNn\nt', 'TZ9\t\x0c1'), [30])
    def test_case_658(self):
        self.assertEqual(pattern_match('\ts1\tl"Hyv480\x0bfT\x0c\x0c_b&\nzX{=Gh-9\x0b\n\rRh9\\+S@IiZaUO\x08}eL\t\x0b9xl@2:\r+\x0cfdNbOp>vFq\n\x08O\nIi [8h\n\rm@(:\t;>\t\x0bY2Q*\x084;I.\x087#:rVSbW-\t\x0b', '7#:rVS'), [101])
    def test_case_659(self):
        self.assertEqual(pattern_match("+WH3\r<\ru\ru:cp\x08N.VN\x0b[vS(7s\ry HYJ#?jn6X}5MS\x08v:wow(B9n\\Us}vR.\x08g0Q'V\x0bX&(,H\tzsxr#\n\x0c%m7LUgZ(}\x08:pR\x08\x086z7\ryo^c!L~Y[L\x0c", '\x086z7'), [92])
    def test_case_660(self):
        self.assertEqual(pattern_match('p\x08#\x0c\t\r\x0c& wDL\x0c%qw1\x0cJ*\x0c8WPj\nvl\x0c\nVS\x08aLhp\nx Xz3mz~\x0b\x08\nDE=&>j"#(s4q\x0b', 'aL'), [33])
    def test_case_661(self):
        self.assertEqual(pattern_match('y9\n\x0c\x0b\rz\x0c(v\x0c\x0cs"ZjX[\x0bO\'<e\txad*@B\x0cG(HE|:MK\r@GSI\roh5@~}u\r\n\x0c#d\x0cG}~f5q<=\t4s6\x0cxgAa<blj\rm*h)\x08?Y\tQ,D4H<', '\x0cG(HE|'), [30])
    def test_case_662(self):
        self.assertEqual(pattern_match('d^t4F\nNM0F@..\x088A\x0b.e*\x08|\x0bp+W\t"x\nSo\x0c0FB\t\ra>*)\x0c/mjP\n\x0bnuyC\r\x08!,\nv5/\n#]uTXJjpW1^rI);8Q\np}FruryTk\\\x08q\x08m){P\x0bodTe6a0', '0FB\t\ra'), [33])
    def test_case_663(self):
        self.assertEqual(pattern_match('`r\x0c>\x0c%<6t7wP;P[E\r-)\n%{\x08@_0G\x08O9SgL}\n~v/\x08\tg\x08g~o\'L~%"#k{=0D=q1kg', '-)'), [17])
    def test_case_664(self):
        self.assertEqual(pattern_match(':H\r\n.&\x0ch4\t`QS~r\n:?\rIITVm"+6\tg#\nz\x08)K\x0bx\n.F\n\t{bsnU\r\x0beP\x0b638~xeZh\x0cP+`,T\r:', '#\n'), [29])
    def test_case_665(self):
        self.assertEqual(pattern_match("Yhaqo(\x08oX9QZv\tB;LUjt@/J@'+Pt\x0b59ESs\x08W\n>A\x0865\nE\x0bm6NB\x0cKf\n@P!\x0c?.W.\x088G}Kmy1>O~WUx+X\r:G~", 'Yhaqo'), [0])
    def test_case_666(self):
        self.assertEqual(pattern_match('_`WogO\nw\rt`>-Cul[\nEWf%cX8hG\n\\ q&av\nO-z\x0cSCg\x08\n\tx\x08&L#uYZ \\\x0c|pjW\r;\x08p>yZk:Ch>%@\x0c(a::m^V{fM\rF', 'Cg'), [40])
    def test_case_667(self):
        self.assertEqual(pattern_match('-\r.\x0bQ\'#x1-\r;?\x08Yc\x0c.\\[y#NUlR#..Nc8s\r@NJYl),\x0b*U7a+}L."GY\x0c\n-Dr+c\tS<A|4-(UZ1\x0btP%#\x0b^pW\r!\tn\r#', 'pW'), [78])
    def test_case_668(self):
        self.assertEqual(pattern_match('jPsV\tjs\x08\x0bn(phI\x084%ju^^\\57\rP&L\r\x0b K%\x0b:k\tTiq*\x08S<\x08\x08\x0c9fy`P=93;r\t\r7\x08pl=\x0cz\x08=!n"\r2Uyufy\x08\x0c`pU*_CNn%\x0c', '\x0b K'), [29])
    def test_case_669(self):
        self.assertEqual(pattern_match("X`Xp64&\t8|XUdtJ\nK}>`<CgD\x0b_[PV@RZ\x0b)J_Fi\x0bPa!F.\x0c!'jHF\n[\x0bQ>\x0cdA9\r1zSCsZt{\r\x08i[n*h\\|J8\r~1\x08w>#+o3", '&\t8|X'), [6])
    def test_case_670(self):
        self.assertEqual(pattern_match('O|sub2q\x08\x0c6n_7Yn@6Kg!|\'!]\r\x08WBS"M:d%Y#\x0bcR*-*\\-Y\x0c\t%MDT\'\n["[TqVr\x0bJK\t\x0c\tim\x0c[p5>W<\x08\x0cd9\tig.\n\x0b\r\x08AW\x0b5s%J*\t%h', '@6'), [15])
    def test_case_671(self):
        self.assertEqual(pattern_match('hb\t\x08\r\x0cCKu!N\n\\~KxC2m\x0b7xM2iCAl{(DRle""m\nZJl\r\x08EPI"sP1\x08t]5s\n8aa*GiE\x0b^b\x0c23R5[gtSi \x0c]\x0chP\x0b#a\tKq\nTNgVA+<-@:uk#\t', '\nTNgVA'), [88])
    def test_case_672(self):
        self.assertEqual(pattern_match('T\r*\x0b+w9e4>*Q1Rn.!\tA:\x08R:\x0b{*9Q+\r\x0b@:\x0cr\\ik4/ (\x0c7I8734aoA\n\x08\x0b* h\tf@9]/&:', 'e4>'), [7])
    def test_case_673(self):
        self.assertEqual(pattern_match('\n\x0c\t%.\x0b[25J\x0b2\nXif\t6!5QD\t3(A*uD\n#|`\nHT\nxT\np!_",\tc}o2\'\x0bO}\x0cz)ToraE5?Yj=is \x0b<EC', '3(A*u'), [23])
    def test_case_674(self):
        self.assertEqual(pattern_match('T%a\x08\x08P\x0bm\\~QB_?\x0cvFb\t!^\x0bO[8YI\txvK\\i;&\x0cN{\t(\n7,#\\o\ni-Vh\x0b\r\nu:;n\x0bA\x0b^\x0bD}.8@pz!1O_>6\n~?|\x08\n?J5[3n0J', '{\t(\n7,'), [37])
    def test_case_675(self):
        self.assertEqual(pattern_match('Yu\rV-\tT^\x0c\r5N41XnuUtntL\t\x0bXo\x0b~\tGL?\r<|8\x08M.AwLhFH\t\rW,PL\x0c7M5Kg6\x0bpy.\x08& \x0cK*nUN];)5\x0bWX\x0bdb,L4ji\x0bhi"D\x0c\n[vc2', '\x0bdb,L'), [78])
    def test_case_676(self):
        self.assertEqual(pattern_match('\x0cP2F7\ro@GV>\n5s\n}rM,*>9}6|yMIakq:wpZ\x0cPGPU}q@X RXBOSQZ\x08*"\x0b:x3W`:Uy', 'P2'), [1])
    def test_case_677(self):
        self.assertEqual(pattern_match('\\QhD\na>_5Mu\rTf?Snr\n%Zr%IQIB\x0c\t`/\x0bL%^[hrjbM\x0c6~@b]e\\b>\rNN8r2;QWV\rSps.oK>B.\x0b\x08b\nEIM7OePzoKU2+HdqJb\n\x0b[P\n\r#37QmX\r\\^*auQ', '>_5M'), [6])
    def test_case_678(self):
        self.assertEqual(pattern_match("\r\nZ)!^\t\r%vv\x08z2\x0bZO1\tm1r'\x0bz\n@A vBo\r-JgR\x08t \tLx\x0bz=Nbc]`}\t\t3mz*Hly", 'O1\tm1r'), [16])
    def test_case_679(self):
        self.assertEqual(pattern_match('.\rW<>hMbW7y\x08\tP\x0bn=\x0c]OqOvBAp />\x08\nO(\n)UR5}\rCtBwFw\x08\n*\x0cZ[\t9iJY\x08(&\x0b\n4K::\r\x0bB\nT\']bXp\x080`d\n4g%{G`N\n\nPDH\x0b\t\x0btOPe=mR*\n}9:"]@\x08J\x0bB', '\x080`d\n'), [76])
    def test_case_680(self):
        self.assertEqual(pattern_match('\x0c#\tETn\x0c\x0b\nm4\nXd,sJ9B}\x0bjW;Sw\x0b`\nGv)HQ&\x083W~rZHg\x08\x0c\x0cO\rmW~`Nu\r:\rXpDba\x0b=*-\n`\x0b9\tnl=#j<&-\r\x0bcH&\\G0\nY', 'g\x08\x0c\x0cO'), [42])
    def test_case_681(self):
        self.assertEqual(pattern_match('\rlZ\x0b\r")-X),jlp\x0b-DMg,I\nx\x08\x08f\rdqu]az\x0bYi|:4P\rL,\'#+\x0b\tj5Io\t@x+\x0c:dCD\r%\x0bUcg\t1Zx\x0cO\r\r\n\tB\rgn;*qb#yMa4 \x0c\tQ\tl}j\x08\rqB[\n(a', 'qB[\n(a'), [100])
    def test_case_682(self):
        self.assertEqual(pattern_match('{\x0b\x0c\x0bV=`\tX\n\t3K\x0b\r\x0bjp]R\x0c>6/|\x0c<%_).\x0c9\x0cC[+Ph\nA;f"hFLkGA|iz\t}L\rhGb\n\r\'\x08\t\nxYwf<x[Z|IX8)H\'cD\t\x0b_\nbM8BiF\r', '{\x0b\x0c\x0bV'), [0])
    def test_case_683(self):
        self.assertEqual(pattern_match('CGiI7:\tKN\x0cJhY7mL-:w(uw`}\x08a15:A:ITOn\t`Q#~B\r9k\x0cy*\x0ce\tV!~\x08\x08GY\x0bK"\x0b\\b\n?O^,p;j`\n\x0cxDj\r4J0\rRT(d^e\x0b\x0b-[&.<\n\x0c\x0ch2\x0cq%', 'GY\x0bK"\x0b'), [55])
    def test_case_684(self):
        self.assertEqual(pattern_match('CLrq@n[\x08\x084"?.%\x0b@\x0cGHpyYxH,.B\tW\x08hIYz~UYUW#\'&U?:)d\t5P>vvS\x0bU\nn>~\r\tgf;A\r-aF\\TIM}\tT\x0b:80z', '\tT\x0b'), [75])
    def test_case_685(self):
        self.assertEqual(pattern_match('O*6BmjoK\x0c"\x08s|kP:/h"(]kk;fhC\x0bR:7kRa7,C|>i\x0c\rMR!?<i<E>3-LiA4Eo8J', 'O*6Bm'), [0])
    def test_case_686(self):
        self.assertEqual(pattern_match('<~V<t\x0bE^r\t\rp[<R9p\n!PE9\\d8>"/\ree\rLC~\\89-Eu\'Q@AQu\r\r\'T3\nrM\t|;1\x0c43wr\t&sdVB\x0c\x0bM!m\x0b<R7E^\x0c\x0bKl\\AdC\x08\n^Uy\x0c|\tjz\x08V\n`5<Us\x0cCBs&#F.KA\x0c\n%', '[<R'), [12])
    def test_case_687(self):
        self.assertEqual(pattern_match('0"I%\x0c\tOpzNrx\x08V;w\x0c13g]\x0c\x0bicC5sR2.hIatb7W=sB\rHI\x08\x0bup\ntFXBFH8\\F<>\tvxe#br`c\x08Q3cgn00U\n#@\r^)Dt\n>3\r1}[e`\t93\r""^@}', 'at'), [33])
    def test_case_688(self):
        self.assertEqual(pattern_match("K0w'x 5Q(L\x0b|V#\r\\\r+.4;K\x0b'9uo<K4e\x0b^5Q\t\r`,Yu5\toa\n,\x0ce\tq+8}-Vri/>\x0cT|4 U\rn2A\x0b\x0csLT\n\t\\&|3/T&\x0b\\3h5)R\x0b<\t\x0bW\r&An\r", "'x"), [3])
    def test_case_689(self):
        self.assertEqual(pattern_match('\x08hgTnb\x08\x0cZM~Uv\rD|\x08\x0b\t) \x08wQ?*[>]K6j*UtA\n5za]\x0cZ|D^R\tyn{}&\x0cw\x0br)\rfO\\9Ywl\x0bf\x0cll?\nsJ\x0cY]l\t\\DgX\t^f!\x0b\t]\x08', 'wl\x0bf\x0cl'), [64])
    def test_case_690(self):
        self.assertEqual(pattern_match('p)OR\r&Vq\tZ>o\x0b20#WbA&\x0b=I&\x0c6Q*Cb|9G&Bo>GHo\x0b^b\t\x0cg\x0c`\x0b\r\tHDi\n\tB=}Lq3 >/\x0b!\r0jIvv\ru\x0c', 'b\t\x0c'), [42])
    def test_case_691(self):
        self.assertEqual(pattern_match("w9-~}5Dfv:8]{\t6tw\r3da*k(k<\t\nf5x^\r}V?|qrYjL'\x08AvW%[\x0b}=K@qOjbIx\x0b\tDe\x0bx", 'vW%'), [45])
    def test_case_692(self):
        self.assertEqual(pattern_match("pC,c\x0cj}M\t\x0c^`+\x0bh'ts\x085`e8Ji0]\neO .>\nD\x0b3\tx\n\x0cmEMS\nX)A\r\r%\t3|\x0c H@a}W`2s->ry+%`',O^%f`svo\x0cS", ',c\x0cj}'), [2])
    def test_case_693(self):
        self.assertEqual(pattern_match("8TW\n\x08W}gY#\\(mG:JoKI+b<':cRCpg;,m\x08\ndS\x0b&%ph>7ip'bGFc5\n!'\x08 *\rJ\x0bX`*\r\x0c:hM\r\x0b\n\x0b}I=\x08z", "!'\x08 *"), [52])
    def test_case_694(self):
        self.assertEqual(pattern_match('\r\t\x0b_^\x0b\';s\x0b+/\r33\x08]%D/f]nt\t:\x0b?a`uC=Nq\r8Gdxi"7s\niOW1#_|ds9}z\x08kT\r\n=8V>S=&\nB', 'xi"7s'), [39])
    def test_case_695(self):
        self.assertEqual(pattern_match('\'T0XOl\x08td0Q-\\&BLSzeN\rs]_\x08\x08\t]R\x0b_\r;s=%PT\x0b\r%pA\x0cr" #5}=\x08_\t5\n dZ\r\x0b,UXI\r:', '\r;s=%P'), [31])
    def test_case_696(self):
        self.assertEqual(pattern_match('PG1OB{!:iZlN?F\x0ck`]o(/!9y\taH\n\r3#\x0b_p\x08?\x0c7r6V\x087x\r"x=\x0cICZ+X&&u;cS2\x0b\x08bm\r\r`gRtn\rm-|\\fnR()Mc?l\tq(1\x08\t<@', 'gRtn'), [68])
    def test_case_697(self):
        self.assertEqual(pattern_match('~{\n(\t5\r)@g|\x0b#Ag8^qJ8.ya.9\\N3.\x0cG]8I\x08{3V%au{0w6%HrFA} \ncs\\xrL\ra\x08d\x0cE#\x0c(Ss\x0c#]|ka#*BM^cr;%:x1F[H\n<bY4a|`Z', ')@g'), [7])
    def test_case_698(self):
        self.assertEqual(pattern_match("2+;o3am`hR]\t\r\ni\\z\tn Dv,J|^>@M%pK<&SW\x08!3grk\rx!'@~M`*v\re-&fgCb#Di_>7axx\x0bp;8?8dO\x0b\x0b)-(9\tW^\t-\\E*\x0bi\x0c]\x08tf;=Hc", 'i_>'), [62])
    def test_case_699(self):
        self.assertEqual(pattern_match('\x0cQc.,MEq@sG\x08\x08ds06MC\x08`@^[[i)J]oV}ua}Ie|AS)\x0b8(4"+Z\r\x0bdpD5atkw^~z4!%p}9m\t(\ny\nKo', 'e|AS)'), [36])
    def test_case_700(self):
        self.assertEqual(pattern_match('\x0be4{\rry\x0b\nJ-o\x0bS-\r6f\rM<(ZlMX4t?}|\rLvHQ\x08O9\t+Uos`x\x08\n&\x0c62=4Z4d\x0b9"\x0bRp\x0c/\t}PMX3w\nMS\x0bFw+B\t ?y7', '?}|\rLv'), [28])
    def test_case_701(self):
        self.assertEqual(pattern_match('\rZc!ksIQBUFCsyE\x0b]mJ\t2`C,1\x0b^XD\n\t,0p!S;3\x0b|x:uK/\n[h\nx\x0cuPn\rn:\tz\x08M', 'D\n\t,0p'), [28])
    def test_case_702(self):
        self.assertEqual(pattern_match('\x0be:8\x08\x08\x0c\x0b^\x0bb^^\rvz\x0b#d5I)Oyi\n<C\x08v\t.4\n1^V\t\n=Z-3,.}u!\nA\n/-gFzI\\R)Jd\x08Y,akx>Wnq*C\t\x08Y|WL\n[1\x0c\nk', '\x08Y,ak'), [62])
    def test_case_703(self):
        self.assertEqual(pattern_match("\te*,']\tTBK])\x08N\t\nf2U)1+oE\r}uq.eny\x0bfRQvtXbj}P94\x08Cc!;0.}\x0bjNpb\x080n~}\t\x0be#E1", '])\x08'), [10])
    def test_case_704(self):
        self.assertEqual(pattern_match('O(\t\r%a\x0bQ]r@\x0c\x0cCHs^\t\x0b\r>3q&&\rYH\tnQ1[\t9L%f\x0ca\x0b"YG/?\t(q\x0b\tz\x0bB\\&x+\teIn\r!\x0b\x08be6P\x08p\ngj\'f&X\t\\#i!F\rHu\r,bV*{85Dz|4\x08-\x0b1q\nz', '5Dz|4\x08'), [95])
    def test_case_705(self):
        self.assertEqual(pattern_match('E\x0c6,%4{Ef:#aV\t>\x0c)*\tzOGDWg&\r{\taM*N}&B.Ghm^\tw\tS5\x0c\nyrYTz\tx4McSB22\r"\\5a\x0bL0*\nmfMLVE\x08\x08I(Jb\x0b\x08\nK\tiK/i!/hBzD', '#aV\t>\x0c'), [10])
    def test_case_706(self):
        self.assertEqual(pattern_match('.5yt":\x0c;EMxr&+\rb5@(\x0cfEcX\t0?>C1|UWm-]6\n13E"aeO\rUX/G\'P{[\rB\n\x0b7;1*\\9J7\twk', 'yt":'), [2])
    def test_case_707(self):
        self.assertEqual(pattern_match('D=="|\n0\x08*2\x0cW\x0bk\x08}9~>fo.\rx\x0c[;C|Lx\tlQ^UhqOy{\rFl\x0bK\x0c#\n{}\tUv\x08iH.u0o8HU\x0cw0o\n&-7;\'z\x0c(\tP\rxx\x0bE\t/l\x0b\r0f;.\n@#', '[;'), [25])
    def test_case_708(self):
        self.assertEqual(pattern_match('\x0cM\r\tUm{"`>5}ehZ`tVd/b\nY\tRjfW\x0cyia2FcBGOa*\n\'UnOu%%e\t\x0bU\x0b\r9n{B\x0b\t?6v=cW:}1c Zw09\t[@ai\x081>Bz:2\nC|T.AE\x08Sx&ue*2o', 'W:}1c'), [65])
    def test_case_709(self):
        self.assertEqual(pattern_match('#3+,=9{W}YGPAey4\x0cQ\tb\x08d.~\x08r1\nMMotKf*V*@GcW\r|pj\rH6;M,s"%.B\t:@eL\x08#\n\x0cCSr\x0bbBMJnw!\x0bkO&\x0c6_+C\n\x0bCx7"Mq\x08Us0Wgs\tDEkY:)', '\n\x0bCx'), [85])
    def test_case_710(self):
        self.assertEqual(pattern_match('-dI\x0c:eqJR pb\x0c=\n.r!F\n\r""\x08\nE/\n8c\x08{a\n\t\x08x\x0bdAE#3S.\n\x0cI\n\n38AG&F\x0b9\'|\x0c&JC:m\x0boM0N}\r+\t\ntgpG\t`\x0cS\t\r"\x0bW8p"OP\n`|Or4%1g\'M3', '{a'), [31])
    def test_case_711(self):
        self.assertEqual(pattern_match('3\r{#lFh!|\r?\t\n\x0c:\x0c]\x0cpu_\x08\nD\t\x0c/\x08\t7>L\x08*FE\t3uJ\r\tZbG{\x0c\x08@\x08ts\t\x08Y\x08jI.m\rSW\x08TxX', '\t3uJ'), [36])
    def test_case_712(self):
        self.assertEqual(pattern_match('.4M\r>z=)=\teK:R"l.B"\nU#U!\x0bk*]qXoh7{G7:b\rxl\rK#\n\n|F)=\x0cW\x0c^\x0b*\rdA"zPTo(FVza=V\r/17r\x0b#\'', 'h7'), [31])
    def test_case_713(self):
        self.assertEqual(pattern_match('`B]\x0bti*/upYP\r\x0b=4P?1\n\rm\x0bT\x0c-m\x0b5\n~#]a\tgZd;"Y~\tC\x08\x08"W:.\x0cC}"\x0c\x0bJ e_Br]8A#y\tL;SI9\ta\t}j(d\x08Wv\\X[>\x0b\r]\x0c\x0b!<(BXa', '"Y~\t'), [39])
    def test_case_714(self):
        self.assertEqual(pattern_match("+#\x0crvv\nsYWT}x3i?D%+'XA23NVn}Q*bG?\n\t\r~\tlf2\r.^\r{THh)zCDHx~'l:9aT\x0bC\nC\ry08", '*b'), [29])
    def test_case_715(self):
        self.assertEqual(pattern_match('o\x0cOZTY{\t.Q=\x0c"\x0c\r\\e\r_9jlIKgxC:#R\r}Lx:\r\rwJQ\rZmW|C5Pb-\n#]qs>^Y~oI\'\n%{\nP \x0cd9\x0bFEv0\x0c5\x0b{WJ7*IU\x0c\r\x0b/o', '%{\nP \x0c'), [63])
    def test_case_716(self):
        self.assertEqual(pattern_match("( \x08'Y%0\x0c\x0cKxKI|-aw7<{?\nxkOI2\x0bT<@4f\n{sI:![\x0cF\x0bS\nifMZhS0vv>qEvE:}ZB\r\x08w\nC\t:\x0beo1I\x0cZJ(:z<\tl^*3r`p<\rZ\x0bB?\x08Kp!\taBGzY", '\x08w\nC\t:'), [64])
    def test_case_717(self):
        self.assertEqual(pattern_match("6w:y#?\x080L|nT#Q\nRds\r4),Oa*Xy{e\x0b\n!=p2s\x0c<\x0cPSc^'\ti\x08\tV@Nc*Ns`\r\n2Xu9kK\nB\x08\x0bo]_&Cxe^EhH[%", '\x0cPSc'), [38])
    def test_case_718(self):
        self.assertEqual(pattern_match('[\t>#1^\r\tYagp=\n2?ye0\x0c4 \rbrSe%c/RK1;ZIpM\twNh\n4BQSLN\r(O{Zb^\x08}Tz?D\x0b', '\n4'), [42])
    def test_case_719(self):
        self.assertEqual(pattern_match('\rU\x08K\nT3aER\x0c%T~l^"/.}\x08,:7\x0b7@*7OiBVlL\t*M7}wuX`@3Ts|4\tY*D\x0b5OpKg6D\x08b&Bn)sW9t\x0cF\'\tvu%\tP4m\\\x0ce\n:N\x0cYn', '\tvu%'), [75])
    def test_case_720(self):
        self.assertEqual(pattern_match('#\x0cXm\t\rt\x08[E(n\x0cL\x0bk@\twLgq\r#\nK\x0b1"(n%e)\x0cu\r\' pX\x0cJ!)\x0b\n\t]RvuR6\x0bEushYjq\x0c\r\\k-,^F', 'K\x0b1'), [25])
    def test_case_721(self):
        self.assertEqual(pattern_match("'\r1~-WI\ne\rP,/}\n`dI\n|Ne#\t0I\tHN[:q\x0bS-(@IKgD\rSYrhlY=r\x0ct\t\x08M1[\ne@4_s\x0b\x0b0\t\tn\t\x0c/&oZHFR/", '\n`dI\n'), [14])
    def test_case_722(self):
        self.assertEqual(pattern_match('\x0ctF\n{D!5\x0cN7`D+r1W5\x0bJS\\[>StJysv\nyh1o"SON\nOL@=&:,\r{gK\rm\'w\rvCdUeC/g\tY;n`H\nXqH/[\r7Ng6G]o\nT[,&qIS\rj\x08fcYD%YzVO\r\x08', 'C/g\t'), [61])
    def test_case_723(self):
        self.assertEqual(pattern_match("\x0bg<3<u15G.h51\n9B}\x0c c?,06\x08:o'^utv2L+\x0c\x0cz\nZ\x08.bHj\x0cfj47\x08*6\x08\x0bnDl`h|BxC2SlG,\x0csJt\r\nCz\x0c\x0c", 'z\nZ\x08.'), [37])
    def test_case_724(self):
        self.assertEqual(pattern_match('kK*\'|\t\x0c\x08=\x0bs3\x0bFim\x0c.Ey{\x082.\ncBMtw\n?  \rh~\ru0Vjh"!]nhKcIv3\n!wQ0\x08\rfU4\x0bSNJbRH5/\x0b', 'Fim\x0c.E'), [13])
    def test_case_725(self):
        self.assertEqual(pattern_match('p4m?Fq\n`\x08M\x08A&\t}g\nPCK_GlD<%G8k(z\nO\x0c~Q\r",R\x0b\n\x0b^/ zr\x0cX&xG9\r( ZKYlHT\r\t\x0c^m5 E\nQMH[OaxA7a#(auXZnUMEi', 'ZKY'), [57])
    def test_case_726(self):
        self.assertEqual(pattern_match('m_RI\x0b\t[oJ\nJE!Y40SX\x0cK^>UO:mZ\x08z1m*v.C\\L3R`\rls\rv/mh zf`,m^t+nd\x08>\x0c]F6T\x0b%}S\x0c\rP\\HopOtY\x0c(\n0\x0bT2@QSx;pTu\t\\wb{p=\t>2\x0c03\x0b', '+nd'), [56])
    def test_case_727(self):
        self.assertEqual(pattern_match('1\x08F7H2\x0bF\x0crl &}\t\r\\A20{M%7\x0cT\rMQn,\x0b\x08\x0bXi\x0b#\x0c!78d9j4~L\t6\x088[f_#Dk4w|3d-\t=r&KoRz( `{p\x0cA7I< >zeX}f@\x0ch\txD G"', 'f_#Dk4'), [53])
    def test_case_728(self):
        self.assertEqual(pattern_match('db+^%\r\tPfDCv\t/.c`sxV|HnobKbVtCWc\x0cugBUL\x08]FYMKSOl2w#LT\tcuA\x0cl4OL>QQk*^hx6jfB\tT)o%\rk37txM/O/:MF"7\r\x0c+1Upzq%Hm\x0cq\x084@4K,1', 'MK'), [42])
    def test_case_729(self):
        self.assertEqual(pattern_match("mI\x0bms=/SG'YcVH~&K\x0b\x08\x0c\r.\rwHN-\x08O\rN@F\\Bx\nQ&l!\x0cWl[~`e@yv*iL\r:87XD%~&xf5<#~{p8J+^o9y?bQ\x0cHh\n8\tg\x08CeHQ1y*urAu\x0b?W(KG}\t\x0bk\rD\x08SP", 'o9y?b'), [75])
    def test_case_730(self):
        self.assertEqual(pattern_match('\x0cNs\x0bz\n[\x08\x0c}9o_\rs~oLD\x08&P\x08>`\r*Ko=o9l6,ZY":|\x0c"n1GOo\x0c}bE\tK:6\r,\x08S)z\x0b*!&N^hw', '"n1G'), [41])
    def test_case_731(self):
        self.assertEqual(pattern_match('\rmCG\x0c6\n\x0c&*S\tFlw\x0b.g4<_,= &%!Ot3\x0b)J\ru3\x08\nBy\r/|\x08"\r!K\x08b\x0b\t5W+_?B\n|\x083~\r\r{c~oY]u\to1LB+\t`#`.}\r?', 'J\ru'), [32])
    def test_case_732(self):
        self.assertEqual(pattern_match('F\x0b],6IX&!F8\x08}V?w\x0cHu\ri\t9/\n-v\x0cta~yK>g\x08,mI,,\t\x08:\x08\x0c\tzBy^z\t)SE\x0b\\L<\r\x0b9hw\x0b\x0c?{e1IFlQ~*T\tP\x0cU[\x0b!N\x0b\x0b\r\r3.{lG5`<eE\\6\x0c', '~yK>g'), [30])
    def test_case_733(self):
        self.assertEqual(pattern_match("kth*\x0c\t 5}K\x0cs\t/\nQ\x0b\x0c`z~\nU X=Xf.<_B\x0b6-9jtr\t/\na\\w5%LHZx\x0c]\rn'KcnL\r|d:\n\x08J\n}~2,Iq>*|luBKe\n/yQ\nds^'^7\n", '%LHZx\x0c'), [46])
    def test_case_734(self):
        self.assertEqual(pattern_match('n\rW\x0c\x089D#!QfUVvJL2}\t+QW\x08/#e*\x0bqJ~3\t_@\\09dyFE\n?|#B\x0bHIWd\x0c5[0"Z4byM4\x0bu\r&Nvg~n/^36W/u*\x088ej', 'd\x0c5'), [51])
    def test_case_735(self):
        self.assertEqual(pattern_match("\x0c4Udo68VjWHA\x0b(I:\ng`[r^@\x08d<D\x0bKK*8\r'2g&6bA\x0bJj\x0c\x08T:_^aC\x0bdu\x08ct\rW~I\x0b0rO{\tklODRDrB K:\x0c?#j\n&bG7<os\tN/\x0b}\nGd.\r'k /Q", '4U'), [1])
    def test_case_736(self):
        self.assertEqual(pattern_match("b ,%k{Y*%[\x0c\rW\rPe\x0cu\x08Q\rWmBc=Hg[J2qaNs\x0c\tHj\n\x082\\?Vm5\x0b\nAP=\x0c7xV?vw{p\n\rc\x0bO\x0biVD\x083u\t?\ry0!@'D`\x0b\nvw9j5+P9+>\nW\x08C*\x0b``DdEB", '`\x0b\nvw'), [82])
    def test_case_737(self):
        self.assertEqual(pattern_match('y\x08w\x08mvWZ@tn&}n<FF|PGMM\x08_6@|Je\x08p\t<;PB`;]3XCgB2\x08\\@:\x08y@@Ri{&\x0bgN2ZG*ZE|>bB2\r>\x0b\x0bH{2\x08*d\n:`VkN0f,', 'VkN0'), [84])
    def test_case_738(self):
        self.assertEqual(pattern_match("%xlu\x08\r0S#P(\x08ZKYY3'\x0b<rVc\tPW^Uzs|s\x0c\x08\x0btoDn5y3d3:%OVTsH\x0cW\x0cb\t\\3,\ne\t\t\nPZ]\n%;'C&\x0b\x0cK5\nD/", '\x08\x0btoDn'), [33])
    def test_case_739(self):
        self.assertEqual(pattern_match('*{\r[[kc\x0b<^EBHLv\r;\t9@|N\x0c1Us\tG-qQ,\x0ck9X.N5n\x08\tYXJqrz|2%A:GT{\n\x08&^FX#uwM0XY\x0bC03/\r)D\n@', ';\t'), [16])
    def test_case_740(self):
        self.assertEqual(pattern_match('kF\x0c\x0bXW~Q8[mS/UYy`o8~BYD\tTn\x0c\x0b?l\x0cH&;liM\x0b\x0cj"*+\n_>(z6*6SCv+Au08,o~\x0c>oqL"K[v"pmfDF\n\x0chc*u\x0cF9O PR\r%Q9rLZ\\t\x0c|Tu\rDpX1b', '&;liM\x0b'), [32])
    def test_case_741(self):
        self.assertEqual(pattern_match('\nc\x0bqW^ES3>p*v<Lldtjb4a\x0b\x08<8EAmZ0K\r\\F\rkz1\t.N<dj\x08[v"{QrU^@U\ts\tKA\r\x0b\x0cBZ', '\\F\rkz'), [33])
    def test_case_742(self):
        self.assertEqual(pattern_match('i[t\n+g\x082Jf\n!G3U\x08@,iA,6H.PGtlu~@A\n\tVT\x0b\t8I-t\n}]R}\no\nu(\ta=C6vq&9\r.\\PvC\x0c', '\n+g\x082J'), [3])
    def test_case_743(self):
        self.assertEqual(pattern_match('P\t@f:\t\t\n/J\nB/Fyp\\P;\n&\x0b-vlhou}>"-D:TfkrXLu*6Iw 0Yg<V7\x0cKReZQ\tU1|p\x0cJ|1\tbP?<fH\r-l6}P\t', '-l'), [75])
    def test_case_744(self):
        self.assertEqual(pattern_match('N|~5\x08\nk%@\tC\x0ci\x0bxp\t&zJm)/v]+:(r\n:)LINw!rka5R/OT:\x0c1\x08DU\x0cCT{TW=bV4L\n4\r5a;B3\n bmj<2M^x[D\rf\n\x0crvCFF\x08\x0b', 'p\t&z'), [15])
    def test_case_745(self):
        self.assertEqual(pattern_match('%R>4x#1..|Rb\rfO^XCY{\x08\t|\x08`>]wkp\x0c\rCfje"<-->\x08S">X=)\tL{8\x0b(\tO(\x0b=]u!`lflh=t5[?}).\'c\\n6yGf\x08\x084to+\x08\n\r4\n=\n50#:Ra\x0c', 'lh=t5'), [65])
    def test_case_746(self):
        self.assertEqual(pattern_match('U}vL65K>H:\r7#\t|+2zFcJCa\x08v~\x08;%\\0zff\x08l\nZrw\x0c\rUwNr/8;4xY\x08z5Z@\x0bX@fIjK\rhV)/==|.\x0br+\x0b\t\n%GH\x08N]*5S\r\t{5kQ\x08+2@#QWAR\tbyuq&w\npqMw!T,`k', '==|'), [69])
    def test_case_747(self):
        self.assertEqual(pattern_match("d\x08A\x0b\rA'~ p\rI\x0cP;* 8\n\x08\x08r:,fp~:\rV)!\tI\x0ber\x0b:d@7\x08.}H^UPqJMi9T\rS\x08;\\s\x0c\x08xP)%FY<ID..O-SS\t k&\\gu\x0cmQ#z5M\n\n\nhx\nu2\r+W,{UATRKCr^\x0c~", 'ID..'), [70])
    def test_case_748(self):
        self.assertEqual(pattern_match('poD\x0c\td,*qU"\',WES\nV5\taQ/1q\x08\x0b~y\x0c?4b\tP{z\t\r;+?UNdMDVn{STZd\r\x0crnpj^\r~FS>>\x0b[x/o9HF\x0c\tZ2\x0b\r!bH', '4b\tP{z'), [31])
    def test_case_749(self):
        self.assertEqual(pattern_match(']2\r%%\x0b,\tr#*nCl\t~w3y-3u:\t_}\t)sx-IHwsQwsgs\r\n{eg\nagO\x08?_\t\x08\x08\x0c\x0c7|\n', '_}\t)'), [24])
    def test_case_750(self):
        self.assertEqual(pattern_match('fAPD,w\x0c|\r\\"c(M-oD\x0c\nmMst?(XBw:9\t|l\rY>2\x0cyS_:?\x0b3O}U\t5\n\x0bBYgg"x,\rE\x0b\x0bp/\r\x0b\nk3o^/\x08Qr=\x0be', '\x0b3O'), [43])
    def test_case_751(self):
        self.assertEqual(pattern_match('v=Z!VU=Dfe\x08LJW\t-z90.>P{MQAxb\'vl\rV\x0c5@}OCW<9NQ\n`1dI~X|D\rH\x08\n\x0cSp\r"%2\t\n\tSJP\nVR}\x0boOpSzX{\x0cg]!FoZ\t#PBV\n\x08?t{*H>9E\x08aPb4{*|Y', '\x0cSp'), [57])
    def test_case_752(self):
        self.assertEqual(pattern_match("8BgF\n=m|2%\r89>\x0bd\t&72pk\tKd?D4PnC?25N_fY1HV\x08'<S8h3C`rax(Zh?3`I}\x0bS@\n2a,s8\x0c;VbMI{T!cUNej\n\t;Z5WT{\rPa%?i\nJH5(:f7)\x08w%", 'i\nJH5('), [97])
    def test_case_753(self):
        self.assertEqual(pattern_match('tHJw+\x0b7P"\x0b~z\n\x0bPGjUHb5t0`0F@Ad\t;Ju%v=BwE~kV3v\r,<#>2"Ry<ctW`_3g\x0cDLFn=ihu,9\x08Xn4\tuf\x0c\'n\x08PRQj\'\x08N\n-F\'2,r\n\tZ\n@|\t>\rX\r?', 't0`0'), [21])
    def test_case_754(self):
        self.assertEqual(pattern_match('pz\rUp0DmS-i\x0b@+0hO>:"^\tiV{sZgx[E&l-Iyyz!l4\x08i{2\t~tV\x08+cg!hA\x0c6s\r\x0bsy9\ncd]\t\tx7:%F57u0OWa\r\t}W1;q7f:\nt12>jNu\td5j^\nq 8?,J2', 'u\td5'), [99])
    def test_case_755(self):
        self.assertEqual(pattern_match('krO}NyrJ(T\r/Z9bPH\rt\x08Q\t4y\x0c\t\rDHe#j{0\'DP_D3%T>i\x0c\x08x/dO]vbj?\x088\r\x0co\rI,\x08\rdz|\n!hL\t#~LUM\x08BAY8"H \tSm7@R/\x0b2)\x08^rC\x08Qi"\\L_', 'PH\rt\x08'), [15])
    def test_case_756(self):
        self.assertEqual(pattern_match("fJSgBI<_px\x0cJnHnu-\\!\x08zG\n\x0crK<h\x08\x0cG\x0b\x0cPN^\t)O%\x0c\ng\x08;'Zscq88~\x08S\n*Nl,{ q_", '%\x0c\n'), [39])
    def test_case_757(self):
        self.assertEqual(pattern_match('\n\rAG\tmn#r4(\x08o2}78/Lne.\x08h\r]fR*\r7uj\nHh7\x08R0\x08v\x0bc5Ugn\nl\x08B\x08m\r(`/>`Y\rNB!\x0cLP@TR? *b^HZ\x0ch\x0bjmQ,\r7]\x0c^r\x080d\x0b\x0b/YIj5\x0bD\r%X~', 'mn#'), [5])
    def test_case_758(self):
        self.assertEqual(pattern_match("\x08\tyAp\x0bp%\x0b3OwXW\tU9\nt_#F#a0(3p{@[\rjNS\x08\tgJi*\nIO\x0cku}t\rj:\x0c+MKHN{|*HuB74y/_BfE\n#SsR\x0b\r]'K\x0b\n\x0bR", 'E\n#SsR'), [71])
    def test_case_759(self):
        self.assertEqual(pattern_match('\nNW|A.h:O\rzJ`:\x08oPb\t#e\x0cfC2\x0c\x0cDx]\nl)<GH\'z\x08b&\x08\tcW-\x0b1w\x0c]Vtv+\r`\x0c\'\r\x080h%P/~V>A|HbAb?t}f\nDds3i%@z+}\\Q]\nlW"P&\'{\x0c9', "`\x0c'\r\x08"), [56])
    def test_case_760(self):
        self.assertEqual(pattern_match('az{\x0c_+)\x0cLQ":\n\x0bxA\x08%}qh@^*U\tXG99}z9{N\x0bU3y1I*\x0b^f\x0c`j\x0c\x08!\n#P*j_oQ)SY\'V*M/)x\r\tud]4l%[56{ ', 'A\x08%}qh'), [15])
    def test_case_761(self):
        self.assertEqual(pattern_match('Yvs\x08{7\x08|/\x08\n\x0bmr\x08]A\'-8;KC[\x0b,\'"E\r"*@Api2@D0H\x08\t6\'X%07\rjK{^\r\x0b5L5\x0b\n/\x0b!>=!YIO\x08}ReYa-z\t\r~=\t;*w', '*@'), [31])
    def test_case_762(self):
        self.assertEqual(pattern_match('\x0cjp8f6xcw\x082HEZ\t+\r\r\\{\'\n\x08"\x0b}\tnLD+|favw~m\x0bUxMf7\x0c?}dfY{tfm8K\rHo=Q Q{\n;P\x0b\x08iq\nUb;', '\n;P\x0b\x08'), [64])
    def test_case_763(self):
        self.assertEqual(pattern_match("#G|5aT\\\tr/k.L8K\x0bk\x0cgfB>){\x08%=F*.]D\n\\}-G_Y\rw\tn\x08IuJ0{K/`*A\x0bdu-Pb\x08'kD", '\\\tr/k'), [6])
    def test_case_764(self):
        self.assertEqual(pattern_match('\x0c|cw#D{nq\\\x0b]R.\nm\\u\r#O&+l\rGo:2_\tQ\x08N-\x0b6HGu\taM\r~Sas\n\x0c\n;k\\L\tN\rOzk1UCK&\tA!gI\x0cCe}^\t\t\rd', 'k1UC'), [60])
    def test_case_765(self):
        self.assertEqual(pattern_match('\tk\nh\x08\x0b8&\x0b\n4w\tv\x0c%muF(XRR8x8mjHF-\x08o\x0c5hl^\rcg\n\x0c>0BXp!OJ_KD4\n)+*\x08u\rX2%l(.2t|@', '!OJ'), [48])
    def test_case_766(self):
        self.assertEqual(pattern_match('80\r{u}l:/\x08\nDFh%(Coe8Rv0Gq[\x08G"m!\x0bq/V=7\r\x0c!\x08w~[1r8.24]BGM0N\x08\t\t^\t!qNr\r\x08N^sF*\x08g<\r\x08i\na9J\x08\'gq|Hyy@GG"lXf)J\x0c1', "'g"), [83])
    def test_case_767(self):
        self.assertEqual(pattern_match('|a;Ce%kv\x08i?"==wP\n\n+\'.\nu\t]\n5Rfj5:lb\n4VDi\nc1h&|\tmA_4u:Us90&+G _/f>kv\\7u(2WEDR\r(A\r]Ich', 'EDR\r'), [72])
    def test_case_768(self):
        self.assertEqual(pattern_match('S\n5d\n\x08Q_YW\x0c.\tt\x0cp\n!\n\r5BMI9.\th\x086WJphXN!\x0c~)R3vdz(@.@L\x0cr7\x08QE\r!S8`OTP//i>\r>HW}*p9l=gl/^\na\x0b*\nU\r;O\t', '/i>\r>H'), [65])
    def test_case_769(self):
        self.assertEqual(pattern_match('\x0c-8\n\x0c yW4Tl)1llt\t\r\t\racGS;W+2\no\x08J9Dd!g(v\x08f~\x0b4H/\x08ea\x08\t\x0c_\r\x0bxD\x08N4m#vgO>5?<\tO\x0c64@\t q5^J6\r\x0bXVo\x0cL\n', '4m#vgO'), [59])
    def test_case_770(self):
        self.assertEqual(pattern_match("]AG\n05#&H!7D\rGfZi\\3|5*n\t;Xf#-1Vrr\ri\\SA\x0b*CRR\ngC \x0bGV0FS9lR9y>)'1T@\x0c\x0bN\\\x0cT\x0898QD XZ\x08x!J;Z\x08d )w\n\\;t`NA.7b\x0cqo0.}F O4m2\rW \x08", "y>)'1T"), [57])
    def test_case_771(self):
        self.assertEqual(pattern_match('s:/2)q#8EM\r\r,w\x0c\x0c\tQ1b\tw\t&v&w\x0c-!c[N~n&\x0cOtVVb\tN!!)P|Ve|\r\x08^Hl<4/\x0b\n\x08 )T2\nkiWK/9\t}Fh9\x08PO*\x0cb\n?bo}x\tN}BL ^@7l_', 'VVb\tN'), [39])
    def test_case_772(self):
        self.assertEqual(pattern_match('S\n\rev(\x0cRKgz_\r\t.\x0c=,\n:IcTH\x08\x0b5[4P[8:v\x0bP9\t[MHYE*o\r.\n*\tD@\rDmoIX\t\tKM \x0cgK~w^@[e', '[4'), [27])
    def test_case_773(self):
        self.assertEqual(pattern_match('a)\x0b,\rb[\tO@h\x0c:eXil @Z\\)>c\r\rSb\x08`@\x0b>{w\x08Yc/P9=G+\'w\x0c\x08.\x0b+lxT:4\x0c\x082;\x0b?8\n\x08"\x08\\@jPEI\r&>R(]U*T`\r\nyc\r\x08%k[_mB#u\rq\x0b\x0b[uv-;C_\t_r', ' @Z\\'), [17])
    def test_case_774(self):
        self.assertEqual(pattern_match('\\R7bI\x0b*{/#,\r<\t\x0c J\\~Wm3DuoWk4v08iY]>!FHnp{pQun{.\r)B+l!sG%\x08!eX#;6I<Q=?SGj\x086\n3\x0cy\x0b\\\x0cz6\ry\ngu!r7h\r8S.', '#,\r<\t'), [9])
    def test_case_775(self):
        self.assertEqual(pattern_match('SNlA\\\x08\x0cdk"\x0b8t;UMy\t8\x0b\r&Sy\x0cO4\x08Yg\rD-V`\rw\r\n\x0b0\nX\tzXP=\r&472]DE@1\x08C\n{eiN\x0bD9/HYs.g;HtA;Gdi?NIDj\x08+gH', 'XP='), [45])
    def test_case_776(self):
        self.assertEqual(pattern_match('SQvRoUH\x08\x0b:zK\x0c>N\nQp?6\nv\\Vtc\x0b\n\x0b8"{(m\t]I/W0Si\x08\n--f`M|^\x0c\'\n?1,lK\x0bpWl9\n', '6\nv\\'), [19])
    def test_case_777(self):
        self.assertEqual(pattern_match("\r7dG5e\x08n'S\ngH\x0cc 9o&F;J\nNN\x0cC\x0b\x0b]c;\r\x0bMEi\r&D_2\x0b NK^0g[*j\\I\x08wbho\x0b;\n[lB<&vssA#*u\tMdo%l[XisB/", 'B<&v'), [64])
    def test_case_778(self):
        self.assertEqual(pattern_match('n\x0b_0\r_COyVw))3I)T\t\r?[H`C>{L`IX5Jq"\t/<-\x08@2%\rs r~F\t[\x08S@eCtvEM\x08`?Ud2u', '\t[\x08'), [48])
    def test_case_779(self):
        self.assertEqual(pattern_match('uy<1N4-\'S: HQDuPj3+Dg \n-e\\=i&"?J\r\rsVJZA\x0cb%=-\x0c3lhnItK4dv4\x0c7\r|a@!\r\tQ>e\x0cf\x0c):Zu++cG\nA\x0cR6w"\r\r\n\x0cY', "'S"), [7])
    def test_case_780(self):
        self.assertEqual(pattern_match(';hKpW6%\x0cs\r\x08|qY\x08\x0brG ;\x08^\r \ne*"*\t\x08M\nEg\x0bo hO~OHhD(1AnGX\x0b:"J\t(1\rW)mUVFuVy7|~>.\x08o-F\\ou\nm\n', ';\x08'), [19])
    def test_case_781(self):
        self.assertEqual(pattern_match('m6Qff}\t\x08\tYZ 4q\raw\tVQN[4\t?DG\r;0Pj!I~"A\\a6W\rCx\n\x0b={~q-]\x0b\n\r75\r1j@Qz]BU\x0bt\\\ra\t\x0b\x0c\r8\nyyTOT-NLcR&Y(\'}fQT#v,ytKP^]yVR7h\x08M', '\n\r7'), [53])
    def test_case_782(self):
        self.assertEqual(pattern_match('Y7=Wf\x0cx\n!P&\nRq_\x08r"z7B\x08Gfo=.c`h\'lo\rZ)0o3FW+u)p\t\x0cb:z*aY\x0c\r5]Z+_(\x08\tY X%S\x0b\x0c\x08v\rnVNLqSKw`L*f<V\rx', 'NLqSK'), [75])
    def test_case_783(self):
        self.assertEqual(pattern_match('XgXf\\\'\n\x08\x0bxw9pJZ4\n\tcj)8qe8O*0\x08\n\x08"1!\n*\x0ceh~zb4(N5x\rfL\x0b\nf3\x08nY5\reWe\x0bGT\tT:\x0cp\rq\r\r9ObA%\x08.*\x0c@>icC2g\nIkA1`dFKNU\tP<T9} \x0c \tUS;Nl', '3\x08'), [53])
    def test_case_784(self):
        self.assertEqual(pattern_match("N\x08P\x0bv\n\x08j\rW\np\r6\t+\t+WjU /GX\x0c:G\x0b'YI)%'c8\x0b\r%(:\nyNc[3Mkky%j\x0b(>\x0c>\r8H{OT\rJGUU\rwHriQ", "%'"), [33])
    def test_case_785(self):
        self.assertEqual(pattern_match(']]S\nkNR\x0b`\t_h3Ps\x0b:ND3\x0cX?FMQ7ZdqI@k%(X1\x0b2bT]zjCAI^_d>Q_U\n\x0c3\rymER]\x08C', '\x0cX?'), [20])
    def test_case_786(self):
        self.assertEqual(pattern_match('*X()l"MD]IP\r\\\th)F\x08\tI?h8Ws<+m\x0c8\x0cj\nG3}x,Qw%0~ZbIX-<H\x0cJ33fi(Z5iYM&k4H8p}vpz\t?u~\'i\rh[s*0x\x0b`VN\x0c\x0b)\x0c\x0c', 'J33f'), [51])
    def test_case_787(self):
        self.assertEqual(pattern_match('\x087)W+.\n\x0b}\x08l_p<i"\x0b\x0c\r6\x0c\tJ}]X~__\x0c54v\nHdo\x0bU4L7Mo_\x0c\\P3dp\x0c},~#S/e\x0cM\nnQ>YtU3[gx/lP;/\x08oW\t<Biv@\'\nsAK\x08E<\t.`#_)g5;t', '\x0bU4'), [37])
    def test_case_788(self):
        self.assertEqual(pattern_match('<un8\x08"\nUf^\x0c\x0bI\x0c\n\x08Q~x~r;gh94g[\x0c @.#\x0c\'\rqKEo,\x0c\\\rnUuY\\\t\x08hS5b-u]48\x08|\r=7W\x0cFaLMg-6;#c\x0c>^', '6;#c'), [73])
    def test_case_789(self):
        self.assertEqual(pattern_match("Nom&f y\rh\\v*\x0ci&r#nxuH'r*\x08\\WAUcm\r\r\x0b#kn,\x08b\x08\rh{RV_M2N#^%\x080fCXNp@~1\n*L.s<\r6TbgK|\r", '2N#'), [48])
    def test_case_790(self):
        self.assertEqual(pattern_match(';-}G7\r*\x08gFaE\nlQwumoT=Gj2\rJW%~BF>B \rA\n_^]]7<}{KL1+w%>yLo=\rr4\x0bEu-Y9\x0b/6ke.\n<0Ll8\tf->3(o<B', 'T=Gj'), [19])
    def test_case_791(self):
        self.assertEqual(pattern_match('|!]S1r.9U\t4h5XF7hdh[+c9vL\rV\rKy*{tSQI*!q/cv\x0bK\r\x0b\'OH`~^N2-xXJjIm^"QYU3IGLO~"V\rg|Gx\\%?s~M[yDRfe<ET\\\x0c\nO-q=0\\+{d}VTB\'V\nuS', 'Ky*'), [28])
    def test_case_792(self):
        self.assertEqual(pattern_match('53zJ&Z\x08OKiK%\t\x08/I)\x0bey|S>\r\x0b7+=^s\x0bQ1^\ta;s*\r\x0b?+fv\x0b\x0b\n\x0by\x081\x0cj|Cjd0u\ns8q`\t\x0bBs2o\x0c)Zb', 's2o'), [68])
    def test_case_793(self):
        self.assertEqual(pattern_match('Rx\n?\x0b\x08ruL@USA<VLVC\ndmyqYQJw\t\rI\x0b4chZ||`8CmNA\x0bB=F3 "nxd\tx}\x08wN\tQU', '4ch'), [31])
    def test_case_794(self):
        self.assertEqual(pattern_match('T\n\x08\x0bKs[\r\x0c!U\x08KYgi\nV#~\nI\x08t)z\x085BrO1!\t1m~~cjv~C%\r4\\\nwj}kY?\x08@54xecDw<P\x0c\x0cupkTU~F\x08L\x0b"&J2 \'*vsFr\n[\x0cmckg%&N\tW\x0c,X\tr`TR', '&J'), [78])
    def test_case_795(self):
        self.assertEqual(pattern_match("'\rc\x08,% r'\x0b<>x\x08;01h\x0b/?^\x08)4L6R\nSvMBV%Ya-)\x0bJS#o?!C!4yW1pr\t3}o\x0czWOt\x0ccH)#hMK>XG\x0b{' \t%6F^hL%K*\x0c\r{>(JLy!~z", 'pr\t3}o'), [52])
    def test_case_796(self):
        self.assertEqual(pattern_match("KsUULR6hy>'0\x08nwe~`vy\x08[?,sY_FQG\\m\x0c9}\t`\tlU|\x0c2#G8)d94N\tAoI40r`\n#d+*\x08\x0b\n;|-6\x0b#[z9l\x0c2*Z>\\&YE\x08?-/`EXh_6fxdEf\n0\x08-/CQ\x0b\nVX\n", 'E\x08?-'), [85])
    def test_case_797(self):
        self.assertEqual(pattern_match("L\r>\\v%\x0cL]tl%YN~f;l]hPP\x08,\\\nT\x0c\x0b[9=QU/pkt\ny2Ubug_v5lK14\x0b\x0c6X\n'F\x08EH\r\nD|Vx@\t+!t\x0bw\tD\r(!\r\tP\x08r\x0b\nYd\\!\x0c\x0b~^T\x0b\n<UO[7_H\x08^t\x0c5\r-", 'H\x08^t\x0c'), [104])
    def test_case_798(self):
        self.assertEqual(pattern_match('\rM0S*9\x0c\x08lxNK!"oy I9s]dSMUS,&T{\x08T\t\x0c\x0b1guh\tRy9oRD\x08rIY,\\Br!NR07Zbj\x0c\r\rtD]:\x0caJ1\\ixs`Ws&M2qL', 'S*9\x0c\x08'), [3])
    def test_case_799(self):
        self.assertEqual(pattern_match('o\x0cRUR`yvd\n+\n}^\r\r\x0bSu4J}_b)D\x08<K+\ry{\x0ba|\r\x08koBMuk%O\x0bv"6H\t"\x08\x08>lV!#H\nG@5kZ}n1!I}\x0b]J6}_)r[O\'\tFD{Oi\x0c\x08P\n', '{Oi\x0c\x08'), [87])
    def test_case_800(self):
        self.assertEqual(pattern_match('\ro|V`Ih\\\x0b7OV#\x08}F\x08bZG4|>n\nj*\x08\ns(mpd0Z\t`Y5c\x08{W^,\x08@u_",-V\x08v1q\t:QLg5\r`4bH\x0b)cm!@-\t\rq?lM\x0cZJ*R=^g4aIX\x0c\x0bR\r', ')cm'), [70])
    def test_case_801(self):
        self.assertEqual(pattern_match('Gi |,0\nO)M.|]UX)\x0c\tF9t(.B7\t\x08o\nS\x08l"\n*pI\tS\n\x08t\x0bu:.iD\t\x0by\x0cpEC\x08U\x08 Z*,&r\x0bQ\x0c;H\n\x08K\x0cQK\\T\t\x0cY\x0cng\x0c\x0c3\x08]7\r', '\\T\t\x0cY'), [75])
    def test_case_802(self):
        self.assertEqual(pattern_match('pOEEiS8>c!+7g_)IRY\r8\nc\r\r\x08|v5Y\n\x0b7Q}em{\nKt\x08w6jNv@\tY\x08\x08&V\t^L\r\n"D\r\x08\x0c^\x08}d\x0cvI', 'w6'), [41])
    def test_case_803(self):
        self.assertEqual(pattern_match('\x0bK\x0c\x08&Hfn|\x0c7%k^U%m62j1m\rH\x0b\n;\\Qn@G=\rB*PDl\rOlp,RX>Gk{/%Ma\rOG\n\t%[pB\\\x0c\x08`@[eEuN\tL7%!XI\n1]_Gen9J3|M\rb\n', '\\\x0c\x08`@'), [63])
    def test_case_804(self):
        self.assertEqual(pattern_match('%E0r5&P}YH4\x0bT=*qiv\t\n\tRkz/y\t^eY?U)!jD\rhVcY\x0b_Ms+3\t=s"#\x0bNlJ\n/#n`JLVCv\r-e1r]I%@)=k\rO+\'r\r]d7m{qO_~{4\x0bRrWgi1&', 'E0r5&P'), [1])
    def test_case_805(self):
        self.assertEqual(pattern_match('E1Fng3tu+L}U?\tGOfq%niX1uu!\tU(cifp\ns` S;7ug,\x08&\\\x0buB@?a>:\r>4wR\tkKz!Ry~b;d\x0cs&Lz&RJu*\x08{\r\n3H', 'y~'), [65])
    def test_case_806(self):
        self.assertEqual(pattern_match('D?.yzx.\'F3hJ",:%\x0c6\x0ctI 2(/@=\\LPWGqcS-VstDN\'`x\rm\x0b\x08[T|\ttAw\tm0<i]w\t>J I!o .', 'qcS-V'), [32])
    def test_case_807(self):
        self.assertEqual(pattern_match("FGWIT2=4AL|6\x0cbG\ncr&pN\x0c.mD,\n[\n9h\r8s:L4.\rB'/lb\td&k(xXB\x0crw\x0b+VC\x0cPrdcp\x0c!ASe%r5Cg\tu\nz\x0c\x0c{\t\x0c4f\tX7r\t1.X _7,H}\t?\r5:N:3\naR/>6t:2G", '\t1.X '), [90])
    def test_case_808(self):
        self.assertEqual(pattern_match('_R[&|tLkDdy6!h!\x0b\x0b+Z\t\x0b\r\t\x08\x0bK\\%G\n\x0b\ru8\'\x0b0A{"m*(\x0c.KXVI\tfU=^YnS+\x0cZF\n2\t))', 'VI\t'), [47])
    def test_case_809(self):
        self.assertEqual(pattern_match('\t\\E|X^O\\\\F]#Z*iZE^\x0bC9(V= s&3E\x0baetDB\r\t\x0b5z\ne1\nq\x0b\x0c}\t&\t?Va\rb uI`\x0b!XR\t`\x08M;"%\x0bq(Oaf]S.>Q\x0bKa\x0cy_\x08\r-?_Yq9^[\tK?]vfnz#Lm\x0c0N:', 'nz'), [104])
    def test_case_810(self):
        self.assertEqual(pattern_match("va.n\x0c?\n[D1K4f\x0cLM\t\x0bl\tdrC\\\n6\x0bofIH+R5]\ns\tt}e^\x0b\x0c6I&]\x0bpaM8YX@;'j*J\x0b-Kx&}\x08\x08q`\x0c\ta:%kG,nK(58Y;\x0b\x0c6rt.w_\t\x0b\x0cj_*\r3J}Nn[+>", '\tdrC'), [19])
    def test_case_811(self):
        self.assertEqual(pattern_match('kNmKiol[A\x0b8j\'u;\\\nbr~@ncm>\t\x0bC}l(\x0c+W\')\x0c\t\r)\x0c"iL\r!PS*sut}&f\x0c]ER!W>x\x0bq\x08\nb\n\x08s\\]BbHe\rdX8g?\x0bK=\r\t\t-qC8h]jMt>M', 'kNmKio'), [0])
    def test_case_812(self):
        self.assertEqual(pattern_match('(\rY5`\t3ts\\=;!\x0b<~1]%KvS8qP|VJ\x08[Uu\x0cVG"CZ\nrRY*NG9I\n}1FJbo*@\x08m\rx&4t\r"\t\x0c=*sVz\tnUP\x08', '\x0cVG"C'), [32])
    def test_case_813(self):
        self.assertEqual(pattern_match('\x0cA\x0c\x0bOVs?\x0b{\x0c(fC[\x0c\r_\r?{o)\x08zU bt+?Ro%/`1P\x0bk\n1\x0cNiJ"WSe,\x0c\x0bK?sq\n`*1C\x0c\r\x0bg"\r\x0c9!)\rT2sVhe\rv\x08_"G&-8CK~9\x0b\x0cqQ^\x0c<d(~\nc9+b&\t', 'P\x0b'), [37])
    def test_case_814(self):
        self.assertEqual(pattern_match('JH_Y|,R\toNTrd\n-)6D!\tltb-BLc\x0b!A#1BojnwFh? #JGFC:\x0csM3)u\x0b\x0bP0#Cw\tf!:_g9eQe\x08`+erIU}\x0bn4%tT]\x08>\x0b[/p?9d\x0bh5E\rBR"+m8O%D', 'FC:\x0c'), [44])
    def test_case_815(self):
        self.assertEqual(pattern_match("]\x0bA_H\rV{kw|&=\x0c\x0c\rLFq.4|m6\x0b\r'*\tUG\\\tj\x0c_ekW\np\n@g/ImT\x08xG\tIB\t2(]+\x0b|'XtZ\x0b\x0c\x0bt\x0cA0R\x0c\rW\nD\x08\n]yQ1wTN#%[?jb(HYG;^p\x0b}i\x08H#\x0c\t\x0b\x0c", 'mT\x08'), [46])
    def test_case_816(self):
        self.assertEqual(pattern_match('lb\x085v|U71+*\x08\x08Udl5t0B\'a\x0c(6h:CW6~Z&\x083D>9w&_O~")Qj,2\x08@m@\na8\x0b\nN\x0b90@#6>T\x0bT=8m\t*\n3+)\x0c=p;O3\x08\x0c\x0bH\rU@Hw!', '\x085v|U7'), [2])
    def test_case_817(self):
        self.assertEqual(pattern_match(')\x0c\\5rb7/:%0Tc~B^3[\nC(\nNpS7\x086z\x0bn\r(l\x08}aggy4g3Rqu(jB)\t.\x08u;V;[ arL?\t>U\x0bbL;G/DI%\r,@q\n\x08}gK:=j', '3[\n'), [16])
    def test_case_818(self):
        self.assertEqual(pattern_match('\x0bj@m*# U\r[d{/@\\2\n[L\x0bM!^5\x0c\x0cV:TKXL>p\rB&O"`iOP\n@V_GlO{8n[%\r\x0bZ(\x0cw>J3KAf\t\\P`uYHt\x0c&~\'B', 'U\r[d{'), [7])
    def test_case_819(self):
        self.assertEqual(pattern_match('Lkf42>P\rP\tLzUqB\x0c4_<nUV\r97B0Kr\x0bG}V\r(J=YHENSF\tC"O)I=\r,TrfSCCy\x0cr6zT^wR},qM\x08Htr>\x0c6j\x08U{zI\nk\\\rb\t9y\x0bH-%<@*\r`_\t\rr6#\':', 'UqB\x0c4'), [12])
    def test_case_820(self):
        self.assertEqual(pattern_match('|b7Z_#ysIV3\tq\no%S\rkc>/~:6\x0cPz\n#C*\tyoj\x08d6p.E\to\r};q|oLk!"D>6)/Av5;l-wzm_b(JhVG?\x0c&,D4DY\x0br3\n\t\x0c>Mr\ng{`<kYs', 'v5;l'), [60])
    def test_case_821(self):
        self.assertEqual(pattern_match('<<\\I\\y\x08\rt&YZu\x0b\x08i\x08+\x0c`ul\x0b\\\r\to\x0c\x0b@v3L\nj\x0cf\x0c)RHpI\r=80ktuA]"&Do]8\n\tEf]94\r\\/f@Y08c\t=7\nR\x0b-7D@4dW O\x0cH\x08pB\x08\t\x08jG', '08c\t=7'), [71])
    def test_case_822(self):
        self.assertEqual(pattern_match('G!b1W"rol+h9h<h\x0b_8aM\'-L\njh\x0c-\rG-/BGh;qJ11~9\x0cF\rW\x0bIt\x0c#?)\'Cv3\'_M\x08_\x0bZi]it\x0c\x0ch~Rln\x0c \r\n\tQC!ci\x0b\n\rWq4IIhB#2"j\\>Je9\x0c', 'M\x08_'), [59])
    def test_case_823(self):
        self.assertEqual(pattern_match("\x0bmZD%(b9(K(\r\rJ\n_NIdw\x08%kN}heC\x0b&mys\x08\\5'r\tH%nWng|8LI'juN~q L'\x0ba\nzd,2~XD!\x0bV}LQz7:\nN>A+}:78\t^\x0bjp*}^:_SM1", '}:78\t'), [82])
    def test_case_824(self):
        self.assertEqual(pattern_match("^2\nbf=dP\x08\x08D{*Y\r\x08\x0cC-X\n,(\\\\F_KH(\nSAg.,Gw\tXU\rf5b}hP\x0bBR>LLQ B\x0bW\x08\r&)#j'8\t\x0cS\t\x0b%t\t :\x0b\x0cD,\x08S@rC\x0c\x08jO*zWz(\n?\x0bf5JOc*[|lM\x0c", 'c*[|lM'), [102])
    def test_case_825(self):
        self.assertEqual(pattern_match('\nR\tT" \rsEP2&[11IM=RRqd!qX\t(%xL>\x0b\x0b2VKOo^(za)Mj:FZ,oq9_of&n\x0bYB\t}(>\x0cSoKSSW~>CeQ\x0c@7Hq', '&n\x0bYB\t'), [55])
    def test_case_826(self):
        self.assertEqual(pattern_match('1xDF\rqT/Q{\n?\x08^U|Ztf@@\nj+\x0c*"K\x0c\x08O#bE\x0c;,\x0cK^XPtDGq%VFE51?V\x0b.X?V\x0c=\'!MM_\tQn\t\rAS\x0c#\nzet;\\s2GW6Q2[\x0b_\tE\tCns1.\x08N\x0c\t}\t%EMG\n\rE\'qhvA', 'Gq'), [44])
    def test_case_827(self):
        self.assertEqual(pattern_match('\x0b)\'J>T\x0c\x0b\x0c2X"k~hw\x0bC)\t\r?Z\x0cm{^vH5\'\x0b\'4p\nAXrIZ bi,=\t@Pr%3-\t\tVtZ\nS9V5mV"\x0bm8SQE`0x1?CLr\rBH\n2\x0bI|xo!\n\r@U[\r\naSkI:\n\x0czb\r\t\nc.\x0b3y\tXh}', '\n2'), [83])
    def test_case_828(self):
        self.assertEqual(pattern_match('_I"\x0b\nFd7PX7X9\x0cs1\x0b\tFrH?\x08Y)XgB/[WV\x0c?zhL\n7;\tY\x0c\r @syU\x082|ry8J8N\r\n|e zaTqlI^v97.\x0be]\x0bki2\x0c0@{:ABvIT?', 'I^v9'), [68])
    def test_case_829(self):
        self.assertEqual(pattern_match('\x0c(G*+mVX3\n:u8\n/0m\t\\\t\x08\t@\tXa}-Ka\x083T)O\nW=Vt`I l;\t\rE"\tDHo}\rh1\x0b?}Pb4', '-Ka'), [27])
    def test_case_830(self):
        self.assertEqual(pattern_match('GKPU 2GXD_ZjMaXUBV\r@2`T#"\tCZ(7\r(N\tQHZXT8`}c\x0c2\x0cz_ c@1\r\tY\n-8K\x08\x0cz', '}c\x0c'), [41])
    def test_case_831(self):
        self.assertEqual(pattern_match('HIxh\x085W*\x0cY\x08<,\n2`i]\rUu\x08\ts{dAyhW\n5Y]c5\t\t\nW\nY}\t=tR1e\tsJ_Ab:u\x08Z&\x0b}B\x0bLwL\t"\nd|U_d\ni\ru0RSceL#lFPw\x0c\x0c\rb\n{\r\'OHK-;', "\r'OHK-"), [96])
    def test_case_832(self):
        self.assertEqual(pattern_match("i\x08_\x08M6/\nt!\x08Oc{t\r\x0cW,Hv\r~*l\x0bN^Kr\x0btk\t-\x0beXX\x0b&\\*b\td\t:~\x08AP&h\n#q[\x0cgdC\rb\n2w\\+g7\x0b_BcGQS}M\r\rR7OK!X.7d\n\x08\x0bM\n{'~D/hI~\tw\r\x0c\x0c*#F", '\r\x0cW'), [15])
    def test_case_833(self):
        self.assertEqual(pattern_match('\r[seMGl \x08V%/X\n7y\n!\rs\n\rVrb:RG\r\x08\tb+/L\n?\x0c+%!\x0cr+A\x0c\n)\x08fD>\\aeS!\t\\1q!_X,(Lf(5\x0b`Uw_#E/F\x0cDl\x0ce\x084|\r)-Tp', 'eS'), [54])
    def test_case_834(self):
        self.assertEqual(pattern_match("\x08\x08cX\x08\tPd)H4'\x08y)Io\x0cMTv!SA\x08JV|NUq^\x0c\x0c\t!d.\x0by'\n^\x0bn>k`|\x0cw)^rxgnNp\x08qcO", '\tPd)'), [5])
    def test_case_835(self):
        self.assertEqual(pattern_match('\tq}YP\nb3R\x0b\nhQf)(-,ucz5B\x0b72p\r}8kfZkn)l\tnY)\nh\nRw\x0br%a\ro.\x0c_.%8\r\x0c\x08}^u~fX\tS\te6i\x0cm\tQ\x08I.\r\nW0Ymg:^4\td&@\r"\x0bvD\x08|*\x0c@~', '"\x0bvD\x08'), [95])
    def test_case_836(self):
        self.assertEqual(pattern_match('BU=|UV({J\\uft41\x0b\x0cv\r7\r)i*Im9_\n\n@a(RK-k\x0c\t"/-J;\n7`%\t\x0bL\r`\n"L#;m\tAU \n', 'k\x0c\t"'), [36])
    def test_case_837(self):
        self.assertEqual(pattern_match("w\x0bH&bJc\x0b6l\nX7|y\t\n\x0bb3 'hn+4i\tIIQ\rn\tFqb\x0co:2|w\tDn\x0c&QXj2\x08cQ\x0cE\rJ\r;H\r`_\nv1N\x0b>Ah\x0bpbDK\n{\x0c\x0bv[c\tN\rI}.%7m%\ng\x0b\x0bj}e\n=ds\t&1z_'Nd9a`S\r", '\x0co'), [37])
    def test_case_838(self):
        self.assertEqual(pattern_match(' iH0o (xi\tEz\x0c3hgX]\rDM~\n!\\S@\x0c=\x0b"WL9 e3g.DO\rD\nU\x08H[.x8YY6\x0b\'+5v"8X\t6L|ojOQo\x0c\x0cx>a\t9\x0ctOX@%\rk>\r\rcz\'6zI^7\ni377', '8X\t'), [60])
    def test_case_839(self):
        self.assertEqual(pattern_match("6/4fo)J1!\r/GyP\x0b)R-Ce.cv2\r\r'nT!0\rON/\x08\r\x0bmN+\r6\x0c \x0cu1\t5\no|0\x08\x0c}3{\x0cx \rA", '\x0bmN+'), [37])
    def test_case_840(self):
        self.assertEqual(pattern_match('bM2@\x08J\x08k9s`(\x0cr@Cz9f//\nkkg}P:\r\x0bs)rI;{ga+mmU m@.|3(1Q:\x0c\r\x08GsJ\r3w\x0b\nsx\x0bJ?N0??be\x08\x0b\t\n^wfl\ry\x0c\x08M\x08p\x0c\'x\x0b>1IkW3"\r\x08Ld>\rdPZaZ-s[%{"q(/', 'be\x08'), [72])
    def test_case_841(self):
        self.assertEqual(pattern_match(')Kn"\r\x0c+%n\r\nY*}Gh\x08\n-|1*VU~WMH}\r0\x08Al\x08x\x0cFRLs\tY@+5\rQj|L<3gb\t\x0b(xX\x0b`\r\x0cA<7\tl^)J~Mj\x08K\'\t.%R\nO\r,/\t\x0bx\n', 'l^'), [68])
    def test_case_842(self):
        self.assertEqual(pattern_match('"\tLI_kP\r6i;\n\\\\U/&Z=/\tVne~i=*gm\ra>B\\;\n\rhT\':WG-o1Fx6\x08A\x0b\na# U\r2T\tBP&hwN\t38rO0WalfQ\'B\n\nF\x0bIrKE77vO\x08JJRf', "fQ'B"), [77])
    def test_case_843(self):
        self.assertEqual(pattern_match('\x0b[*\x0c\noQ[Kq v.pzz\nc>u!>MTaoL\t1)\n\x0b\x08)^#ai_G3*,z\x08L\n\x08\x0bPFZ\x0c\x0cu{)r\x0b_|BPd06:\x0bi#1W\\\\89 ~.`7\x0cJf[r\\+GfH\n{97\n\t]\x08<CuNnR\n', 'Pd0'), [62])
    def test_case_844(self):
        self.assertEqual(pattern_match('+C\x08qWN\x0b|"b \x0cT\x0b~R=,R"\x0brUfIFXP=5<\x0cb5O?uh|u&^/[\x0cqo\tV&y1\x08\x085-f4\n8h\n\x0b\nR7', '\tV&y1'), [47])
    def test_case_845(self):
        self.assertEqual(pattern_match('\x08b]\x0bn\x08!X|\x089}\x0c\r\n\x0c0\x0bo(H}e)VbJBtBKD\x08\t[l*\n?%]u\t=]?^hP\r<\x0bF\x0b\x08l\x0c\x0c9-PDeU#\rmApW\t.!,=\x0c@A\tDt4399*\riH6@RA\n\t)\\~M9O', '\x0bo'), [17])
    def test_case_846(self):
        self.assertEqual(pattern_match("[Yz\x0bqQ\r\x0bCSJ\x0c#qKn\x0b{k)5a\x0bv:RaN\\\t6\t^\x0b 5C\x08ki3)\tH\rWx6=k\x0c<9gN\nv\r..Z\tzj7\n\\Rg3W0`\x0ck'\x08Io>`Q7\x0cx\x0cw&\\+9hZk/[o@o", '5a\x0bv'), [20])
    def test_case_847(self):
        self.assertEqual(pattern_match('@3o9U?qn8>\rd((s1\x0b45`+\x08tDyq)eo=64,3"/G2hJGbBYD\x0bR"d[-1\x0c)SM"\x08OE_\x08=r\nA4/D~\n\n_oo\n.D\rwO\ngK\t#]', ')eo=64'), [26])
    def test_case_848(self):
        self.assertEqual(pattern_match('\t%/\tH\r^@+H"\x087LJh\x0cp#Lm9(&]QUyd|\x0bRX!0D\x0brBe\r\tU\x0bQ\x08\nc\x0c\rAb,hdV\\\n>Pc;p\tVe[w[t(Yw\t\nxM`\'56C\r\\bh\rv\x0ck6\x08r<\x08t72_j+p\x0bvti/j_\x080[\r', '\nc\x0c'), [46])
    def test_case_849(self):
        self.assertEqual(pattern_match('5Q<xx|,\nWdk1RvRtCl;To>@l/<5^\x0b%\t\x0c)\nf<+L!a\x0b\n~o\r*:\x0b\\r-XuULN(\x0bEF4\r\t]%,\x0ce\x08\x08\r\t', '5Q'), [0])
    def test_case_850(self):
        self.assertEqual(pattern_match('\t,d9*\x08;gqB\\vM*\tua]w\x08qg^B|\x08r/B/s4+R|#cbs4gdd\x0b.\nT1f\tz\n&g\x0b)TWel0=X\x0b', '\n&g\x0b)'), [51])
    def test_case_851(self):
        self.assertEqual(pattern_match("{ARr+*et/DP<e*b(VbH8L\x08~Wrg\x086ak^n\x0cQ}mgaRK'@`\ns#e?WE=]\x08rx]\r-\t\rX_\x08\x0c\x08\x08Q)pV\x0bq/Q\x0b\\4;'\t\x08@qx\x0b\x0c:XqmC\r\x0c\r\x0c?u'\t0", 'ak'), [28])
    def test_case_852(self):
        self.assertEqual(pattern_match('cU+\x0b3_6xcB\x08fb.:0E\x0c0Zt^!-:pgG\r\n~\x08@=B(|ZKlBi`\x08LtV)Nz\x0b\n?@09#\r\n\ty\x0b\n\n/', 'Nz\x0b\n?'), [48])
    def test_case_853(self):
        self.assertEqual(pattern_match('\n\x0cIdtP%\x08\nL\nkv(W=@f<gz/Mj_z\x0cJph?1:yj!=e{<T]Z\nw}J\x0c[K&S_ n#U0l2QK\r5\x08"\rdaj_\t42y\x0b\\\ngh\r5=>\tj.\t\x08\x08)rq:hzO\t|YCn^\n1y(fLp\x08rh?TSYX|r', '\x0b\\\ng'), [75])
    def test_case_854(self):
        self.assertEqual(pattern_match('U*/\r;\t9r\t\rb;\x08s\rulF\t-*|\x0b_)(9B"\n<\r^0\\\tnZrRV@_:6\x0c\x0b\r2(_L`x\'H\t77\r\x0b4|\x0c; \x0c\t8\'', '"\n<\r^0'), [28])
    def test_case_855(self):
        self.assertEqual(pattern_match('nb@#VQ Cs^s \\8Ml\x0bvyk-7:\rYZ\'EId"I\x0bO9RFO1wn7a\x08R|j\r\tl~=h<lN\rr~jyZz', 'n7a\x08R|'), [40])
    def test_case_856(self):
        self.assertEqual(pattern_match('\nzhm\x0b/DskS!tpyZ}0ion"{8*@Fz\'8\x08a)&"3vI\t9E +"U~\nYWjopY\'M:b#A\'#1v@!\no\x086\x08]Q\x08b/j\x0b#q5*V:Fc%#P-_??^jP8X*zRfzLa\x08#', 'v@!'), [61])
    def test_case_857(self):
        self.assertEqual(pattern_match('~mj~#znqI:\x0b.v\rI`v,q\n\x0c82~6}xCM}\rKpR8\x0c\t#?p\r|RS\r{1Rocx\x0c_t ~hVkj+\x0bj\x0b\r\n\'QV\t:VhxG<#J\x0cr\r|~fJ9<ZNf"s8\n', "'QV\t:"), [66])
    def test_case_858(self):
        self.assertEqual(pattern_match('p\rR]2H;]M\x0cWa8C\x0c6{U.:oP5w]ZWYmVq+*]Yx`b3mNNhi)&C{YC\x0b\x0c\x0cJ \n3Jz5~Yf/^]_\x0b\x0c\x08\x0c\n\x0bq)y\'x(*\x0cO\x08d\x0b0\r(yf!Z"\rh\n\tm', '*\x0cO\x08d\x0b'), [79])
    def test_case_859(self):
        self.assertEqual(pattern_match('M\x08CE\t!\t@=3#_,1M|\x0b)\x0bZXmj?\x08b\n\r"M\rZ+4\nh|k 4Gw{I8Gg.X.9tYoI{kft\x08\t]F{L\ry}I\t?Ty/jR\tTuh\n=n\t+\x0c\x0ca`V\x0b\x0bNEI\'9D\x08,#=<+@d.\n+8\x08', 'Tuh\n='), [77])
    def test_case_860(self):
        self.assertEqual(pattern_match('EI^be:/f[7\x08\\1`6k\rN\\\x08STx/Ox\n\x0cK_j\x08k\'<PC>I,\x0cV}1\x0b\x08\'2M%\x0b%t|\x0cu\npF\t~0\x0cq<X\r=`K.KR\x0b`9zJ\ry\x0cW?pOeO\x0cWN}cpXhzD}u"3}fy\x0b', 'Tx/O'), [21])
    def test_case_861(self):
        self.assertEqual(pattern_match("!\x08kI~uo\x08:T:\x0c&'cS\x0b|Bsp+Y\x0cW]P{w*&[jZyghu7^?.E?SO,\nT-Y*&Hz:Y1E\req{dh+(6;?\t{\tx\r]81_\tUy\t>\\,61C", '&[jZy'), [30])
    def test_case_862(self):
        self.assertEqual(pattern_match('76\n".\'+7D\nR{ok\tR9\x0c\r|GZvzS^NhnX\x086hP|Zzu9+csuk\x0b\x08</&YaK:uq]3?:\x0bsD\x0b+ &(06{5)p\x080Ec\n-eP9,n\tA0yHzo[0mL"g', 'NhnX\x086'), [26])
    def test_case_863(self):
        self.assertEqual(pattern_match('\t>i\nRca&Sk\x0bGjv.qFs5{xi\n9\rrg8?s\r\t\t\nBu+vP\nRNuqQ~ICK~?>Ify\t("nb', '?s\r\t\t'), [28])
    def test_case_864(self):
        self.assertEqual(pattern_match("\x0b &o<`\r'\x08\n?V\x08(CwKkAs)\x08'ii<'}H\\z[\x0c\tX\tP@\r6\\y\x08J\n`w\x0cc-Q\x08A\nh\n%gC\x0b\x0c\x08h0b@\x08\x08#A\x0b&_b\x0bc2p \nl~*%cYS\rZ8h,\t\tu[.\nb(NwFCyH(\n8\rs|\x0c2\t", 'wFCyH'), [101])
    def test_case_865(self):
        self.assertEqual(pattern_match("\n*]\x08U'YDV\nQ>/e2|fY|5'wQ\x0bQR\x0b\n\t\x0bkv\r0]|3q4\t>qZKsu9\r0]\x0c=\tSw8\r\r82", '\r0]\x0c'), [47])
    def test_case_866(self):
        self.assertEqual(pattern_match('Y\x08ph^ P\x0bR?#{}\x0c\\U\tI\tk\n\ty,D<\'J?j\'K;ofethS}J\x0cb>\x0c]\x0b+".v \tgSI\t\x0b)|2h\nLQ\x0bUQI\n&6x\x08P9Ur\x0bl\x0bBr#\r^H\t[ed}F', '\tgSI'), [52])
    def test_case_867(self):
        self.assertEqual(pattern_match('A\nJ<t\rpYhg]\x0cVXBc\r1S+Ow=?\x0bo:fe\ttv&\x08+\x0c\x0c)5QuvEQ<Ab\x0cF\n!"7f4R"\x08*8~P3\x08vjTC=#\x0c;u\r\x08U\t\n<9G\nWv4Y\x0bR\x0b:\r\n).ebdP]n\tn\'x', '\x08*8~P'), [57])
    def test_case_868(self):
        self.assertEqual(pattern_match(",Q\x08\x08\rJ\rX*x\x0bM!|tMT7|X\x0b\x0chhQsq3*N\x0c\td=|,\x08\x08%|)eA\n;\nZF\n:12AMozhNr\x0ccrD]qU+\tzR\rL!;U5{R~\x08t&8'@\x08r\x0b1<D", 'T7|X\x0b'), [16])
    def test_case_869(self):
        self.assertEqual(pattern_match("G{HW\\R\nor\x0c7/UjR\t@\r\x0cq+\x0c\nXLicS\x0c;6\x0b:\n)5>fOUC\t\x082I. \x0b3g3\x08b\rk#Y'>5\n\t+D\t2-@!\n\\:\tl{rntq%)PRqUFH\x0bLW\x0bY=rk", '\\:\tl'), [70])
    def test_case_870(self):
        self.assertEqual(pattern_match("ZA\n~nNY':\\A\t\x08|K)]dl9~ u|F\x0b}:5\\\x0c3%U1Q9.0Lo57z;q\n{+5\rT&Zv:\x0c\r\tM/WF\x08t6b#OE\x0c+Z\x0b\rN\x0cykkb\x0bq41.V-j=\x0b[rygN\x08btV|?_AU.", 'NY'), [5])
    def test_case_871(self):
        self.assertEqual(pattern_match('V&{az*=\tyKrC2!{DmyUC_#o.^<|D<\rb#1\x082G\x0b[VVU\x0bB\n;Y+FM\x08jI\x0b8E<:,Ut\x0b>\nm\'2\n&\'\'@"N3qu%f\rOvLL\n', '\x0bB\n;'), [41])
    def test_case_872(self):
        self.assertEqual(pattern_match('\n%?7\x081lWnd~s|\r\rnG&\x0bZ0f#eVxP>H^i4{QJR\ttv\x0cf\nhxh]u\x081i\x08Z:}wsZYGfY\x08Wu\x0b(HJbkJYiBV4^)\rcq)\x08]+\ri,]:7%', '\x08]+\ri'), [82])
    def test_case_873(self):
        self.assertEqual(pattern_match('a_rEA^1\x0b^W;,!-E9)\x08D\nnu\n\r\n\x0bKh&Jx>\x0b\x0c\x0bAWIM2zf{x\nr}eaU\rrBU6ksW@5H\r7s{GFJ^\x0bc\x0c\x08q~\rUy"D3\x08Q1BhS~YL_u', 'IM2zf{'), [37])
    def test_case_874(self):
        self.assertEqual(pattern_match('Ll(xYUak\n\x0bh&n\t r+W\rMdUB\tzMLTR"qj)MN*\r-\x0b3xH9ZL6\nm%I>J!\x0c=(6s[B>]]\'N\r\t\rYn;R?tm[zR\nTl!!K\x0cr>Og=a}M\rx+\x0c@`#o4', '+\x0c@`#'), [95])
    def test_case_875(self):
        self.assertEqual(pattern_match('sL;q\n\r/plb\x0b5_|1#?p\\\rbB],v?xG\x08\x0c,=#_\n)\x0b8PLt\trj\t`,V6 U\tUP\t&G=V\x0ccebUH\nj\x0bcpTZblLFo-F\\o&OI]2<', 'j\x0bcp'), [66])
    def test_case_876(self):
        self.assertEqual(pattern_match('\r^!?a^\x0cm+6\\3l_;\rYxlm\x0bND5B-?P7Ir=o!IA5\r\ti-._PSF#)U!{\x08IMY\x0cTD5u\t|\r>e', '7Ir=o!'), [28])
    def test_case_877(self):
        self.assertEqual(pattern_match('\x08XFkpE\x0bl\r[Xi0dY]<9h\x08,/eU\x08\x0cJ-\x0b>;2/A%WX\rP/\x0bB:_}L\x0b\n\nIhJr)=\x08\x082SuE\t:i/!go', '%WX\rP'), [34])
    def test_case_878(self):
        self.assertEqual(pattern_match('38sN\t\n\t\nAvK{BQtB\x0b\x0bog{\r|<4E&\x088R\x0bs9)8\nJ81^+:M0pNp\x0camS\x0b\\#\x08\x0cHN\x0c\r,w-lM^qCK0h\rPwWu]S', '\x08\x0cHN\x0c\r'), [54])
    def test_case_879(self):
        self.assertEqual(pattern_match('om:PG51\x08p{,\x08\n\x08szwEuq@ ]5\t>)O35&\nJk&)\r\r\r#\r`>LDH#c,\nF)7R\nrYx_}MG`Foy7', '>)O35'), [25])
    def test_case_880(self):
        self.assertEqual(pattern_match("L.\tt\nd)T969<Y\x0b\tEG2;/\x0c.\x0c\n\x0c8\x0co\x0bMkEI>R|\x0c2Gnkb +'XP\t\t1\x0b^:/>C\r\x0cJ587", 'G2'), [16])
    def test_case_881(self):
        self.assertEqual(pattern_match("4,J3\n\t)r\x0c(IG&\x08(\ni JT\x0c\x08qa(\ts8Z\tN3 x\r\x0b\rbPO\tr`8Qu?<|w\r_ \x0bxZ\t_,\x0c^\x0b\x08m\n\r'\x0cjH7SpbN@\t*\x0c\nW_P0W\nz\x0bSS\x0c%v", ' x'), [32])
    def test_case_882(self):
        self.assertEqual(pattern_match("U,1b<q~!LXz'c5z5\nU#{f6Jf-vJ7<xt\x0bN 3\x0bn}~EZ0\tWVBcLKO*tZX:\n1\x0c\x0bXmoP}Oms.:0'1\tt\x0cc?Q\tU*B\x0b0Nbq<\x0b\n\x0cMg\tS\x08RYi", 'EZ0\tW'), [39])
    def test_case_883(self):
        self.assertEqual(pattern_match('m*s[p`!lbP5f"7/JO;uydP\n\r\t\tU;"Q\x0b\rJ\t5RP]kcI\nZp.T<VR>g1\nw0\x0cYd;Ay|cIwP7]|\x08Gk\x0bg/o\x0b<@CMCdym7{', 'o\x0b<@C'), [75])
    def test_case_884(self):
        self.assertEqual(pattern_match('?l=\n\x0cEr\x0bAlgW\x0c\nyMs7Y5b0C5!|N\t0Seo0r2|/z\x0cG8S`_Zb\x08W??>nu3\x08`M\n5\tg8\x0b~He6\x0cQ,<K)\x0b2Vl Zo|[8G', 'eo0r2|'), [30])
    def test_case_885(self):
        self.assertEqual(pattern_match('o+\r\x0c#\r\tETu@of6[]l-@W\x0c*W9w\r\x08)\nYE?\r\nMn_K)Sp9:4J<AXq\rE\t&\t\\2B)\rb8\x0bg_!s\x08-\x08coG\t}^P', '9:4J<'), [41])
    def test_case_886(self):
        self.assertEqual(pattern_match('x\x08au*R/[1y=wyOwRU\x0cE vB\t[wXhY_>1Z32\t6Z\te)`!\\b\tWH`S"OqE\'X\x0cG"\tO4? em\x0c@b\n}"y{(\x08\nNW\r\x0806cs', '2\t6Z'), [33])
    def test_case_887(self):
        self.assertEqual(pattern_match(";=g\t\n\x0cgOx\x0b0TJVdfA(s']G;0/X@tahF2B|*YR\tG#S\r\x0bSpq!\rPuEr)\r}\x0cV|n7p\n&e\x0c\x08\rVrI+'2`<#\x08]/=\n+k18Z/\x0czV;?F\t{g)%U@\r", "'2`<"), [71])
    def test_case_888(self):
        self.assertEqual(pattern_match('a_^s\ro\rUsP!yIl{!\x0bhK8T\x08r-[\x0c]09+\x0b)\x08x01\t E{-D8LES\\\n&\t)\x0c\x0cQV\x0cUC\n1]\n|rrm.Ji\t|.2#b\x08!\tqPY\x0b16q!i', '\x0cUC\n1'), [55])
    def test_case_889(self):
        self.assertEqual(pattern_match('aK\x08|\r\x0c;Y\x0ch4H_\tc;s#~\x08F\r\x0czC<#,<b\'A\x08\rNx%b\x0c.R.K8fK\x0b6qOuNB4pF)8&\r^dO\ni\n \n/\x08|44Ej\x0c!\x0b-\x0b\x0briW\\\x0b\r\x0bp1q&c&\tE\t)VT,ev"6u>~dm(', 'R.'), [40])
    def test_case_890(self):
        self.assertEqual(pattern_match('\n|4 \tW\x08\x08E\x08\nRc,\x0b\x0c08VQsI\rV8\r8EQ|;UFbzNc\x0b>\'c@&!@\\\x08n\te!o/7_iGA.@]:JT:*z-\n\x0c;S{QR,E:4\x08r%\t#pN8"\x08g\x0bg!/r\\\x08eW:\x0cwzZ', '!@'), [43])
    def test_case_891(self):
        self.assertEqual(pattern_match('%wY\x0cEp}["Vq0t%<i\r@_Nf\r<P\tC^Ntu\n]Cxy\x0b\nFe#\x0bv#W\x0c`\rFu_n\t\x0bMk*[#\x0cu(\x0clI})w.\x08M"<h\x0c_QlP\x0c`z8\x0b;\rE=B\n|\rPdeH"ivB\ngU]\x0bD{oeMQ', 'k*['), [54])
    def test_case_892(self):
        self.assertEqual(pattern_match(':k4l+H&I=>RKp\n(\x0c7/1(@c\x086]\\\ny9\x08HF\x0ccfmA\\\x0b^,`\'\ri\nxsJ|\x0b\x08lBNd(\tHCcu\t\x08R|\r(68_sZ|iQ(\n|Oe^lsn\x08+"\r,=86\r\tQCy\x08Z66L\nJ\n\t\t\x0b<F:', '\x0ccfmA\\'), [32])
    def test_case_893(self):
        self.assertEqual(pattern_match('Uys=(\x0b\tB/]YT9so2s\rL&E17YC\t4\x08>e\x08F @2\\w\x0c6w\tuO_\nu\x08D\x08f`\x08r2\rfI\x0cH1eVKMhm\ty\x0bit\x0b', '1eVKMh'), [59])
    def test_case_894(self):
        self.assertEqual(pattern_match('O{/_\x0b{s?3V/_iQ\'o+\r\x0818&ajLIE\tU?]\r\tl\n\x0c\n\x0b\x08\x0b\n:"\rS "QEIkKIlLk\r\r\r/b&w\x08poAr\x0b\x0b;\x08\x0cZ\x0c\rg\tpb"\n\x0b\nP\r\x0c+ <?f2\x08\tz~\x0cBhE\x0b"\r@|\x08', '\x0c\n\x0b\x08\x0b'), [35])
    def test_case_895(self):
        self.assertEqual(pattern_match('JK_^s\x0bI9\ngA\r\x08,oF]\rb\x08TA>Yh|h/#t>0\rE*o"?c:(bG`^\r(cA%\nOao\n^\\UklC', '^\\Uk'), [55])
    def test_case_896(self):
        self.assertEqual(pattern_match('qL|;I\x0b!,U\x0bBA\n0=0.3s,\n\tphyX\x0b\nl\rZ,W;XW&\np\r\x0bg\x0bEzSA}l\x0b\n8\n<U @u|+j\x0cAwxyLI]1Z\t\x0b', '\x0cAwxy'), [61])
    def test_case_897(self):
        self.assertEqual(pattern_match('H6G\n2!\r7r\x0cMoTTR}fL\x0b9\x0c+I\x0cjP&`a=\rj\x0cLvBkU\x0b"\rF\rKi\x0b}F6IvE;\x089f50]=(`6q#\\|(7\n\rhylF>(E^T"(\x0b\r\x0bp\'pGiH)c', '\\|(7\n\r'), [65])
    def test_case_898(self):
        self.assertEqual(pattern_match('3%\tt.L_Q>[Sx,R~8\r S\x0b.\x0b4w\x0b;Y\t.3\nX\'+I:I9[1/@\nbe \x0ctuj\r?*q"<\x0c,X"3D\'K<\t\\Azi`E?bf', 'Sx,'), [10])
    def test_case_899(self):
        self.assertEqual(pattern_match("\nOowk\x0c8YPF;&\rM@\n\x08[\nR\x08pl!\x08\t\\FGNE\r71T\x08yaw'd#z3V|\tx!qE{r*\x0bnRg_\r\n6pJ{qwk\x089\nvK9[5O\x0c\rC", '*\x0bnRg_'), [53])
    def test_case_900(self):
        self.assertEqual(pattern_match("_d1@\x08o)\n3tOR\x0b\\(Vw%\x08&\\&\x08&1@\x0b'\rjX!SoTu3[)\x08d\n9,'64yF\r(\r|\x08F\x08\rV5?", '3tOR\x0b\\'), [8])
    def test_case_901(self):
        self.assertEqual(pattern_match('\x0bkAd\r8nzw\t^P s@"U)L\r]\rel!\x0b\x0b+zc\t5\x08m\x0bBc==\nrgy\x0bFv=Sp\x0b(o}U8\x0c)d\x0b~\x0b~Ko\x0b9De{["z\x0c)\ru\n:kpdWT\t', 'U8\x0c)d\x0b'), [53])
    def test_case_902(self):
        self.assertEqual(pattern_match('f5\t\x0cD\x0bh*.d\n(T?\x08\t\x089\n\x0cqG\nYEv\nPTKB\x0c5 N+j*NVF!q\nu1ct\r!\x0bkkdVa\n@1O3JR', '.d\n(T?'), [8])
    def test_case_903(self):
        self.assertEqual(pattern_match('IT|rE\x08<T5f n \x08p\x0b\x0b\x08m\rPeL2R\t,6"\n\x0c\rA\x08AcN-IjV:\'N\r\tZyRm9aL_>o\r:U\n\x08\x0bU\t\x08J,r[\nsX9IE9_R\x08s', '\x0b\x08m\rP'), [16])
    def test_case_904(self):
        self.assertEqual(pattern_match("\x0cyp\rtR\x08w\\}']\n;\\G-Q\np#uuH\x08\retK{Bk\x08W\n\n)Om0np}cN]\x0b.1\t*}\x08@F.DROl2?\x08H\nj\x0b\x0b#+Rz\tZ\x0b's\x08C}P:\x084Hbd*S\r+`N\x0cWyTf\t>*t\x0c[<i\r", '2?\x08'), [60])
    def test_case_905(self):
        self.assertEqual(pattern_match('\n\x0b,\nXEm\x0bTvgA?38oc(\x08p|*&9Y\x08&1-gYJoo\x0bt\t9[|uMki|0o9Dh@D)F\x0cKyq,r;3@chRxUf\t)\x0b2IOaK\x08\tpnN\r+j/I\\a;\tc|X\x0c\\\r<|\tmU\x0c', '@chRxU'), [62])
    def test_case_906(self):
        self.assertEqual(pattern_match('4\x08\'sTb\x08\x08c\n}{"K>>eKMiq\x08j>\x08\x08\r@_Oyb%e9c.d+Ah\t~.NC*\x08\r<q{=\n\ntUS\n?\t', '\r@_Oyb'), [26])
    def test_case_907(self):
        self.assertEqual(pattern_match('35\x08_{j\r`)*\tm.\rb\nY\tf_7po:KLqDHr\x0b\rJWr7n\x0co\thSmJx\x0c\n#\t>Rh< "nWcYu*\x0c\n\tB:Gq8<e\t\n=\x0c,6q*\tl+QM.\t@\\SfU\x0c&\x08Ae^#ON\ttxw', 'WcYu*\x0c'), [56])
    def test_case_908(self):
        self.assertEqual(pattern_match('o\x0cg0\x0c;\x0bFk\x08J Q0\x0cB[\x0c@\x0ckt [|C\n\nc+(\t\x0b\rxIhJ\'\x08\nEJf\r@Oe]2:i\x0cAMF8VrKr5\r DY!*5\x0cKSM2{CJ|v\x0b;%oCXrW`uda"iGB\x08\x0b`n3S', '\x0cB[\x0c'), [14])
    def test_case_909(self):
        self.assertEqual(pattern_match('?\x0b\rzzE4\r\x0c,S\x0bz8\x0b|T\x0bQk0X\nQ\x08:YoHA\x080=rXA\x0b\nG<:gk&4%*zuxH|\n6}]3n\x0b p4\nt"]omW\x0b\x0cMx\tk\x0bZ!R>JPn=tXH>OE\tad\n', 'k\x0bZ!'), [74])
    def test_case_910(self):
        self.assertEqual(pattern_match('\tuNi]O(gEht=2v6YJ\rp%Tp\rq9\\Cb\x0ck;@y\x08-\tO\rNz\rKyO(YoRl]s\rmx!\x0bv`;\nZ_\nFT\x0by}C\x0c\x08w&\x0b3?U-d!t@&u%Pk[}\x08\r04j\x0cG\x08|!("MA,', '&\x0b3?U'), [72])
    def test_case_911(self):
        self.assertEqual(pattern_match("bN>\x08_^7HMz`DiMGl\x0b\x0cf\x0c4s\t'jH\x0c}\x0cLu;&QZ\x0cP/\x08J\t#\x086Fv}GAYX\t\x08wF1!fp\x08X\x0b\n\x0b:{VA1,SdK\rj,Z\niO |BaF6Ikg]\n\n9<", "s\t'jH"), [21])
    def test_case_912(self):
        self.assertEqual(pattern_match('B,%)j\rb\r\r5a,y6/2\x084ND\ng:)\x0c"*`kxN}f<JFj\t1`{\n,H|`1\x08Eo-_Vw\x08fg\rk>O;&el', '}f<J'), [31])
    def test_case_913(self):
        self.assertEqual(pattern_match('\x0coL\x0c<VHK:_t*\tgxE,Rx\nu+,-IE+xhuc\n\t3UfYsO\t\x0c\t+:C\r\nDMGf+>dr5i4&\x08s0DI\r\x08LqF8\tgY\x0cn\r}5?}X,rENR\n*|\n\r\rJRCj\x0861U%bSQv\n2Up2oL\tRhk"2\x0c', 'NR\n*'), [84])
    def test_case_914(self):
        self.assertEqual(pattern_match('{#0\x0b{`m\x08nW9a?SxQV\r&~Lcfr0GgAKK\x0c*w3\x0blrJu5g#m\r>ICQ\x0crJG\x08H\r}\x0clj{(U+x[#g\x0cR&.h\x0bZg\rni{\x0b', 'j{(U+'), [58])
    def test_case_915(self):
        self.assertEqual(pattern_match('j5\x0cbidw\x0chkP[umgTr#S,S\rEspW)v\t\x0bLEy\nR&W-\x0c.qG"E\x0cbu\x0c\x08gm1Y~z\'#9l1I[7\rG', '\x0c.qG"'), [38])
    def test_case_916(self):
        self.assertEqual(pattern_match('m)\n\t-ct.a\x0bA\rj\rO)g_wI^*\n\x0bq6r895[GoAOv\x0c\tZ\t\nOu)\rhwUS\t}\x0bGHBmUdF\tc\nm\r\tL!mw\rH@GPFx=s\x081[3t7\rJxI:S|/@JQ,YrSZIZ\x0b', '\r\tL!m'), [63])
    def test_case_917(self):
        self.assertEqual(pattern_match('.)\x0c1\x08\x0b*-`%sMQVH\ncF\x0c{\tO\x0c=0fdlO]:*\x08A\x0c)-\x08a8Lt|\x0bjL\t&\x0c"!OI-\n<JOdU52AfK%xRd\x0chgxPR|\x0c%=i&\r5*S\'q^snVV\x0bb4R\x08 WT4', '|\x0b'), [42])
    def test_case_918(self):
        self.assertEqual(pattern_match('T\x0b4i%F+\r\x0ca&v\n\x08]P\x0cS=<\t(?#,V\t\r\r\x0cN>S\\P\x08t_o*\r{\x08^9Hq\x08b\x0b\'\x0c|Wa(5%ImjCvQ`y"7/D*a.O\x0bNe\rght\t\x0c\x08i4k', '#,'), [23])
    def test_case_919(self):
        self.assertEqual(pattern_match('\t="56\x08\x08<X.\rFMMX\rn&:H\rnqz9pCalC=U\r\t\t|\rf\tV\r\x0bG~@\x0c_(-p\tFIj\rxc\x0bi8\x0bioG\t2~NmVxZ|`V', '="5'), [1])
    def test_case_920(self):
        self.assertEqual(pattern_match("B\ne>'\nvcw)u8@ \x08l\n^\x0bo\r\x0b0\tHv\x08{,\x08W1iN]1lR\nbZO],&8*\x0cv\x0bYP\x08,`p<\rW|\x0bx\x0b|>+o\x08yku.%4tY\\ysVW/D[\x0cjnYfm\tSp\rg\t\x0c:n=g\\>bvjJy^1%y", "\ne>'\n"), [1])
    def test_case_921(self):
        self.assertEqual(pattern_match("\r\x0c\n9m@\x08'wM\r`xf}TKk:\ndq7*KW#\x0c[E6mI@zsE)\x0cy2/\tD;8lIq\x08'?EIH\\t31yL'd+PGDIWmo\tV\x0b4\nvT?{\\~|\n=uy\x08TAv{mEC\nDzi\ncZ\nlOSiu>\noFU", 'IWm'), [67])
    def test_case_922(self):
        self.assertEqual(pattern_match('j\tC\x0b7P[}\r\\kA1zPhv\x0b\nCvuJty\t<:\x08LriTA\x0cR~f]\\"N]doy\x0c%F\x08,\'O.O[M!0Yw\n\r', '\x08Lr'), [28])
    def test_case_923(self):
        self.assertEqual(pattern_match('o31%_;&.E=\r\rJbV0|{\nm_gA;-\x0c&,\r\x08e-zn\'Y\'\x0bL{Qq\x0b\\9eft#d~.\ti\r(\x0cM\x0b0\x0bO\x0b,[{^\rC4Yt+xM\t\x08K\x08\rx&"aF\x0cz\r_7]w-du\nef8Q,Wn&iR\x08x)3U[R', '\x0bL{Q'), [37])
    def test_case_924(self):
        self.assertEqual(pattern_match('!R\t8X}~-dT\x0c\x0b\x0c5\x0c!\n\x08kg~G\rRTj\nU ClV\n/J3\x0b\x0c?-wh]\x0c!%r !G~\rq\x0c+/}YR}`\x0c1?}KegWFdZGC#', '!R\t8X}'), [0])
    def test_case_925(self):
        self.assertEqual(pattern_match('\nUG0v-\x0c \r~\x0c\t";"J\x0bi2N>pVLq6WB7W"Qp\x08".\x0cL3~\\m0!\x08\r\rQK{>Dep\x0cNijtmg\x0bd&\n\x0c_\nM,\x0c[\tKeg6B\'5\n9f^#J36/\\\t)\n2\tJ\x0c\n>CmZ\t"\t @L\x0c\r', '\rQK{'), [46])
    def test_case_926(self):
        self.assertEqual(pattern_match('y\x0bd,0 6\x08M\rn3p>\x0bb\x0b^`u\n<I3</kCF\x08\x08EA];\x0c@8_lx -\x0crb)[Y\n3\x0bT8*PYNICq\x0b\n}-', '^`u'), [17])
    def test_case_927(self):
        self.assertEqual(pattern_match('E {\nv\x0b3p\x0bY%`ct`EqY@ubhZ\x08Bq@\r)ZUfiUU\x0b!-h\n\x08z\r\rO\x0c~kY\x0b~=lH.wF\r[l_(z)8<N7\x08NB\x08#(z^|:zcse\x0c}DzQu|?>>A=?\rs\rbCCn\nMl[(be)!Lq', 'n\nMl[('), [101])
    def test_case_928(self):
        self.assertEqual(pattern_match('\x0b`\x0bxniT!rsqe\x0b\x0b\x0b&Uy,sBoQ!- 1o\n2R,#Q\x0cN\tK\x08I \x0c{(\r&\x0b`\n\x0c%mf3[&+"X9!#{X-R4E', '`\n\x0c%m'), [47])
    def test_case_929(self):
        self.assertEqual(pattern_match('9|\tHW\n\x08\t^\n\x0bS\x08e"\x0c`F\nMjm_P<.}a\\U\x0c^v`LJL\nL-{\t^M\r8)\r{)(wUA\r\x08\x08jpSo)Mq%\rR;|\\kCO`7b\rY#R\x0cJ%N?<', '.}a\\U'), [25])
    def test_case_930(self):
        self.assertEqual(pattern_match('j\r\t\n@qGlz15STQ/k\x0c/\x0ce\x08rKQ0cqS\r\x0cG_rP>,\x0b\x08GHH(hlV\x0brj2%\t\x0b6DU;sT[a4\rb/:\x0cN`l', '/:\x0cN`'), [63])
    def test_case_931(self):
        self.assertEqual(pattern_match("&p\tA''IP\x0cZ\rm\x0cIi'\nz\x08OS\nSh\r>2\r\rp\x0b\x08/)fm\r\n5Q`\x0b\x0cyg//\x0b\n7\rX0&aF<<\t\\t\x089@\x0bO\x0b'9Gn4k \n%1qO\x0c5,Pl`\nACJ;", '\x0cZ\r'), [8])
    def test_case_932(self):
        self.assertEqual(pattern_match('bWk?SxI7YP\nX\x0c`\x08\\;d\x08%b\x0c>c\r(=o\x0cP8yOk"iV\t*|+Dz\x0c])6`\x0cv,\r^k\r%R/d6_KR\\,ExdN)l+\tgIqAG.t', '+\tg'), [71])
    def test_case_933(self):
        self.assertEqual(pattern_match('mf\nc\n+\rPUSm9pz~\t7[>"\tt\nz[uswQ\x08\rC\x0b\x0cp\x0c\rZ:\tlyb8XY]P0-\x0b8e\\t8xV\'o[n\x0bV:XP\t7KX\rrmIiK\x08mB15kBq\r\\DQWWaf:K\x0cE', 'K\x08mB1'), [76])
    def test_case_934(self):
        self.assertEqual(pattern_match('rvN?\x08Ajb5i\x08T,,R\x08o\r`@\nxK#adypI1#!/e\r^n)fl:\x08lab\\^~Vf\r\x08\t4^M"CM{\x08\x0bfjul0ZdZ{fqJVM', '\x0bf'), [61])
    def test_case_935(self):
        self.assertEqual(pattern_match("K'{ro)qR\n\x0b>\\Wq\n*0qQ\r\x0b\x0b\n\x0bV7W}\x08rH}/)\n\x08av=;J <3h^Mr1\tR\t\t\t!\tlQ1\x0ce\\[Rh}wEYIBL,Phx<\x0cO'I\\38\x08Zn\\jkyt\r\t\n", 'ro)qR\n'), [3])
    def test_case_936(self):
        self.assertEqual(pattern_match('`V\t\x0c\x08\rYd]EHJ5T\x08\r{\r0)%jT\x0cg\x0c+8OS\nsw\x08mqks1)BGT\\68<\r]\rip!WVZ<+ms\x0c!q+80et%\r\re\t;VJE&9K\x08\x0b[@c.X\t', '0)%jT\x0c'), [18])
    def test_case_937(self):
        self.assertEqual(pattern_match('^D6\rBV" )=b-^ar\x08pgai#2K\x0c_t"\n\r;-X\x0co\x0bXI~8dY\x08me&\tZJ\t\rd!RVO\n)bt\nTD>\n,^`uWjQ|\x0bZ9 uazf|EHV/`0\r#\n?+?\x08WB;S\x088\\(i?\nt:W(\t(o,', '0\r'), [86])
    def test_case_938(self):
        self.assertEqual(pattern_match("l\x0c@g`\r/l\\c-O2q\n\x0c\rK\r{}Bc\tC\x0cE\r\x0biAO[89R@Nv*rmE'h{~'\x0b\rcO%\x0cVp\nC=_>*}nq\rP:_8=hY\x0c\x08?^Ji#\x0c(rg*\x0cu\x0cJa\t\x08,PAn", '\x0cE\r\x0b'), [25])
    def test_case_939(self):
        self.assertEqual(pattern_match('*\nNMU?\x08:b"r(|B=Vqq`|\nENN\r,qf\n\'Zwf1\r V`#X&T\x0b\rB\x08SZ([^|5fkQ\x0c\x08:dO\tB^&l-g;Xek-\tO\n53\x0buX|q\x0bhCVk)-a~\':}CO)\t}~:\x0b', "':}CO)"), [92])
    def test_case_940(self):
        self.assertEqual(pattern_match('l\nFh6\x0b\x0c ,q?H\x0cKsp\x0c(\t^,|H\nxdq\\\x08>Oh\n]4j\n\rDr\\Z\x0cDEx.vTK{y\tiIFxQ,>:1\x08L\x08atl\n/9X\t\rlWa\rxR6)qU\x0bX\x0bTV\x0cF-\tyGdw0\x08h\x08\n&/FU{*x\tX\x08R5S(', '\x08at'), [64])
    def test_case_941(self):
        self.assertEqual(pattern_match('\t[@=WT]A\'\r"\r,43h}s!*k\\\n}\x08MN6\to!H\\x1=]k0~ZHZ;\x0c*/}Q.aU%3k/-T\nC-\t#Z]hR<d\x0b\x08cS\t\t~*aJqm\r\tMA\nt\r+#zysKhnd\n]\n\t\x0b%R-]R\rY5', '\r"\r'), [9])
    def test_case_942(self):
        self.assertEqual(pattern_match('n=t045xVR\x08;*\x0c5AA?\x0b\x0c\x08\\8\x08(apQ |^>|;WL:l},n,h]\ty!({;\r6&t{V\nS\x0cc\x0c}u\x0c9\n\nq\no[%"U', 'y!'), [44])
    def test_case_943(self):
        self.assertEqual(pattern_match('v:ZmM4Q^\x0bR\x08jziLxhh\no>\'I"\n2OH3TvSn#S%1_\tug\x0bIe9n`\x0cdfj?UWS\x08pS\x0cc\x0b', "h\no>'"), [17])
    def test_case_944(self):
        self.assertEqual(pattern_match('\t{hg\x08/b\x081\x0bP\x086c,&\nAVoTVR\x08rw\x0c2A\n8N/\ri@VCB\'\tapxT\r3-8@\n\r7\nh(}En\rsek*3j<\t<n+[Si3:1NH8\x0bZrXq~eLU[E?"\nl}B', "B'"), [38])
    def test_case_945(self):
        self.assertEqual(pattern_match('VF9V&\x08J^"j<\x0cAdvE7dfe&M-^z(\x08Xb{=?]HO5Bw\tD#UO\'a<(\tVI"d1=e)o\x0c>\x0b3;\x08U#S\x0bY#hgh\x0b\tjy,3H;%! sA;q{U)jawVf\n9Hs(l\x0cnII\nMh', '7df'), [16])
    def test_case_946(self):
        self.assertEqual(pattern_match('\tn(8\tgzLp]TJ\x0cB{])D%\n%4h!Y\x0cE\tA#u\x08ot`)\r\r\niz\n/6K>`YrS 5on\x0c8+\x08#{\x0bLht5\r8n\x0cDWY', 'ht'), [62])
    def test_case_947(self):
        self.assertEqual(pattern_match('HK]\x0b@yCO\n"HQBC.EF\x0b\rp\x08/hK}=\x0c\x0bZCiS+a}nG!\rNu\r\nY\'s.otc\x08}I/tU/=\t`\nF<M_\'\x0b\x08\t\rai~v\x08chk(\r4W\nyon.KQ!@n\x0c\x0bOkp<\x088E', '"HQB'), [9])
    def test_case_948(self):
        self.assertEqual(pattern_match("\r\x0b1\x0bC:l\nQ\x08+\x0c3i8B}Ou.\x0c/yG\x08d\x08\tC!^a\x0b\x08z!\t_J\x0b,W\x0b\x08N6\x0c,\rW\rasnw^7'a\\VL-s\r.B\x0b,D?/i]\nn\x089A", '3i8B}'), [12])
    def test_case_949(self):
        self.assertEqual(pattern_match('\rK:P7GO\x0b7uMi&]X)(bR:P-qdUp"[Xz@|ho8oQ\x0c)%\t] \x08\x08S|S\x0cf,O8#^\r,=\\9\nB+n\x0c6VeL\x0cA,hP:M\x0b/*2b\nj\x08\r5Q(\tq|l,d(;I]\t`[U^\x0bpVdQ\x0b\x08bB{\x0brht\x0bsz', 'M\x0b/*2'), [75])
    def test_case_950(self):
        self.assertEqual(pattern_match("OX\x0b\x0bu\x0b2-lVQ>\x08-*+47h{YV\x08g<U!'FCTPY7h\x0cSXP4/\ni2h48khcBS.fj\x0byvu\n&[z", "U!'F"), [25])
    def test_case_951(self):
        self.assertEqual(pattern_match("l>@H\r_\t\x0b\nv*RJix@_\tg72(\x0b@uA/N4tvP\tP\x0ckBar}`\x0cRoX\n\x08r'F\\\t'[\nD\ta,X-TWQu) \x0b0!*0RW]@\rao\r1\ri5YuR}fAW\x08v", 'RW]@'), [72])
    def test_case_952(self):
        self.assertEqual(pattern_match("ua\x081g\n\x0b26kO)M!Q_=mt&O\x0ci\x0cvl_g/K6z\x0c2\nH%c\x0b:YFW8\tLAe\r&hrF\rPX^J\x088w\nt\r'OZm.|g'\r\ty V\x08hb;\x0b\t}m\x0b", 'J\x08'), [57])
    def test_case_953(self):
        self.assertEqual(pattern_match("2Mz\x08Yl:oeO#o\x0b}75<XN\x0c!R\x0c<\tzw\x0c!\x08Y'6{hF+e|j\x0c\x08s\x0ce=NK!W\x0cH\r\n+\x0b}GiUx\rd6\x087e6x63Iq\r\nI`\x0cu\x0c\x0b+\tJ4v\x08F@ivw&C<;e2\x0cC'Y>\x08", 'F+e|'), [35])
    def test_case_954(self):
        self.assertEqual(pattern_match('\nLO"S}\nV^xd\x0b>w:rDvk/R\rLsPPu8TBbd\r7+\\C8cI\x0b!;,@W]B.\x08VH:~\rkc\r6QyU\x08L\\[\nW;(G|E\t1de|, o>*-nOP6', '8cI'), [37])
    def test_case_955(self):
        self.assertEqual(pattern_match('7j+1\\\\9V\t\tSB~7\x08mj]!\x0c\n\tZCSoC}\nr:ic(v_UbcCE\n!\x0b`]rl\x0b%c\x0b]?w\n_g`?[T', '`]rl\x0b'), [44])
    def test_case_956(self):
        self.assertEqual(pattern_match('i5944"M^\nn%=dctLCS\x0cX\t#S`;\x0cpQ;FxYE\x0ceoD8lVH\r\'0O^*@g2\x0c:"M. },-u\x0cp}%`=;tz+8\x0b8\x080C3V\x0c+Z&\nci\n\n\x0c\x08\x08Nu+hR-o\\?\r#sq\ruPT', '`=;'), [64])
    def test_case_957(self):
        self.assertEqual(pattern_match('dYcA>\x08*<gP~[%REk\x0bFp`A4"m\thr&Eu:E*O%6zeNt?iLC^f^f\x0b\t*rc6rzq-O<v.^l\x0cU\n\x0b\n/3Ly\nrESx@uyPPQ%\x0bsCn\tdcxqVR?e{y\x0by2C\r\x0bfEyo|g%866:_', '4"m\t'), [21])
    def test_case_958(self):
        self.assertEqual(pattern_match('\r\x08b\tQJ*?\t5Pmqk\x0c\x08n\rrH5l@H>UAg5<M\x08XO S8omZ) \x0bIJIV\t[AqU\t O\x08_!{QVVs|>ZWQJ\t\'\'(9";,&2,P%E\x08v[[U=@1K', '\x08XO S'), [31])
    def test_case_959(self):
        self.assertEqual(pattern_match("'EpxB\t/#sRCY8-\t}3ZY\t:6_{.kj\r).c;G\n\x0c}\x08/\r\x08.@ix\r\nW6A\x0bYm;OD~FWU3e\x08wk\nmxS\x08\x0b)}\x0cH\x0cpS:\x0ba5\rrkgp\tw\x0c\x0bx", '.c;G'), [29])
    def test_case_960(self):
        self.assertEqual(pattern_match("QT87q{N\n\t\n%\nj\x0b\rKvqAP_\x0cY/W[fE\x08y(M\x0cu's5V\x0b\r2#_\x0cg5R+J:\r\x08^\n>A\t\\ryNK(\tS2bd#+).\x0bx!T0GYX", '\x0b\r2#_\x0c'), [38])
    def test_case_961(self):
        self.assertEqual(pattern_match(">N|J5ips\x0bDxVr3@tV{.%L%*W~~hD\tQ\x0b#>'\x0cYbO4Hhgqb\r\x0c\x0c)z]\x08\x0c\tkH4,zoe0-\n86&\x08X3?`K]r~i.\x08Ri#FJ\x082T\x0bx7Dg-\r\x0bZ7g|I3{qOyL~~@T\x0c", 'hgqb\r\x0c'), [40])
    def test_case_962(self):
        self.assertEqual(pattern_match('\rRw\x0bw\x08C\toJ]n)\t\x08\\S\x0bZ\r\\\rm#c\n\r?%5H~\rCtOo\n\ru`jiA,<e9\x08\rq(-&Lo]7*jeu-=H>OD\n\tvZX\x0bN1eIa(!@y*k>XZ-r1\\Yf@c\rj\x0bU', '-&'), [52])
    def test_case_963(self):
        self.assertEqual(pattern_match('qh\x0cU\x08\rIvD|{\x0cLpy*Q\\\tX\x0chFp.:\x089S\x08JS\'d\x0bW0:\x0b\n>\nWCoL.(r"gOD5\tL9\x08\twz\rQCQ', '\x0cU\x08\r'), [2])
    def test_case_964(self):
        self.assertEqual(pattern_match("\x0bt\x0b;z\r\n?KL,gsJ3\t%~&tT<R|5TxLQKZ\tc\tKe6Z\\MeH\r\nrG3\x08&\x0b\x0b'^\x08z,ps\x0b09\x0c;'\x0cxsjn\rAo\t", '5Tx'), [24])
    def test_case_965(self):
        self.assertEqual(pattern_match('m1^0UydkK_\x0c}\t\x0cpA{cK\n%\nE\x08\\\tl\nu\t\tP!L\x08%\x0bcN0&Is+A\x0c\nm4.\\.c\nwRX(5y\r3U\x0bp\x0cMr4tzrqut*\n\x08CmS`FPlehyRc\n#rCQ', 'Is'), [41])
    def test_case_966(self):
        self.assertEqual(pattern_match('_\x0b~XU/\nBU1\x0c\r \x089-1gM,o{%\\NLhdz\n\t\x0cm\\\x08wR3:e\x0c\'1\x0bT\x0c~}83w|N&c<\'"@o(czMnmZXG\tl\x0cn \x0b\tnK#', "'1\x0bT"), [41])
    def test_case_967(self):
        self.assertEqual(pattern_match('D\x0c*\r\n-y"(rz(G\x08(d\x0b\r{\'\t1CNVlWEQ)\rQ-Mc|X\tI\x08e\'Z\x08\nw4k(\x0c{u:k\x0c!I38\'[qSt(\rB\n9lW>7T\t>B\r/~5~)O1nwNzA\x08CziP@iQ\x0bGj\x08h/Jk]:PiWw&D', 'k(\x0c{u'), [47])
    def test_case_968(self):
        self.assertEqual(pattern_match('V`1\t\x08\x0bt1\np0:SLL\r\x0c\x0c\x0bRZ\tY\x0c/Bc-E/c \x08:rE.\rPz??w]HunKp\t;U;o\t:=H3s\x0bS\x0c5L\n4V|kJ\x0c\tl#L|:\r\x0c', 'l#L|:\r'), [73])
    def test_case_969(self):
        self.assertEqual(pattern_match('P3:3f?&zC\nE`<mG@<T\r\t,\x08\x08\rrA\x08fW\'A[lqfkBOav(s,%"C\x08b7=vEIhOXL*\r7Sw\x0cLn(x1h|>oLd-dh7?bmh\x0b]v3E}k{TJOut\n oO-n\x0b\x0cGO\x08Mw\x0b', '%"C\x08'), [43])
    def test_case_970(self):
        self.assertEqual(pattern_match("Uc%mi\t}%WjaI{\x0bIc=?]c;^\x08U7K5\x0b\x0cL/5E_\n@*unO/xCCF >M**39UF|\to\niC-\x0b\x0bM'Q<oOKZ\tG:\rHM%h(hn;W#}_\tqYhC[UwcoT\r3djVMO\t\t.-\rJ\r", 'I{'), [11])
    def test_case_971(self):
        self.assertEqual(pattern_match('0\x0c\x0cb>GuO\t-S0c9g";\rw!9q%\x080gslS\r+zxAo0z86D\x08\x0bn5d-Rq]5R;@oMd :2b!;=t\t<e~8rNg8gR-RR\r\x0b\r\x0b\t~F& n\x08e\t', '8rNg8'), [68])
    def test_case_972(self):
        self.assertEqual(pattern_match("* \n+h/kN\x08Z~SC\nQpP!mn.\x08MBkX>'9\r>Wi\r\x08.G~fq)G)|\x08%;:ChDwi %7]kZY\t&u&S-8yl\nX", 'kN\x08Z'), [6])
    def test_case_973(self):
        self.assertEqual(pattern_match('5>(liITN5"\'/`\rrHg&N\x0833u\x0cVQ8V2x\tT\rl" i,h^\x0bi!_@&g*2E@aM<\\\r\n@,IU45rE\r\x0bw.mX[\nRJF{sH\x0ck\x0c?l\nSjrx', 'M<\\\r\n'), [52])
    def test_case_974(self):
        self.assertEqual(pattern_match('\t\x0b~)%""*=\r+hFxer)\rf\r\x0cC\x087*\x08,8d\x0c\t%=/}W\r<\x0b@t5{)~=Eep.Z!\\H\'a0YRS\rE\x08?M+\rnou\x0c2V\x0c', '\x0b@t5'), [38])
    def test_case_975(self):
        self.assertEqual(pattern_match("D\x0bf\t74b\x0b\rG}l?9\x08sv>S\r\x0cNTo\x0cAZ0x8e5-\x0bN,Z\x0b\r_r=(^mk#Un\x08}\x0ck\x08)k{pB'\r0>H\x08Mr4RI\x0c4F~\x08N", '0>'), [61])
    def test_case_976(self):
        self.assertEqual(pattern_match('TmYe _Y\x08G\r(-dy>0Y\t\tA?\x08[zuo=+b,OWW85zo\x0bx,U\tL`UI\x08J0\x0c*\x0b^X:q%d\x0bz\x0b\t\t\n\x08\rF`\x08\t|,C\x0b(=^ \rv\x08m', 'q%d\x0bz\x0b'), [55])
    def test_case_977(self):
        self.assertEqual(pattern_match('5FI\x0bV"32c\n\x0cRle\x0c\x0c=o\n2kkrd"\tBwoSd_\x0cg gc8:Gpn\x08#4.71(4S#\n)V|=&\x08dk\rp}x\x0c\x0cIFdXx\x0c|\nz\rBYt\nAr\x0ci#|\ryPd:M\x0bjuBM[J\x0c"7\x0b6n\tk;WlkQ', '\nAr\x0c'), [80])
    def test_case_978(self):
        self.assertEqual(pattern_match('\x0bN0nkK\n0Q!\x0cVTO_?`<P Q,T\n/)>9t=\x0c)Vx*830\t]\t=\x086\n\n"+Ecj}k\r\r/z\x0c\x0bx_l\x0b/Q?@k9o%x', '\n0'), [6])
    def test_case_979(self):
        self.assertEqual(pattern_match('w\r]PCVQ\x08\n\x08A\n<jvu;&\\\tnV_S%%\n/`W4\r\n\x0bIjO\x0bN8Pj? <VftmF%3KhEQ[0#\x0ch@\n\x08J\x08tYp#VfzrZ\x0cX\x0c9u`', '\x08A'), [9])
    def test_case_980(self):
        self.assertEqual(pattern_match('n\n\rF&#FYE..yx\x08E32o\x0c.%\n[%P \x0c0\r\n\'8S:Xs\x08\x0b\x0b\x0b5\t-t-0P"f}\x0cf\x0c]rmtz\nRw_R\x0bJ0#zkr{H7nC\x0b\x08(`k,dONlU8KNl]g z=u1c/\n\x0bl\x08\niSW\r{FM"', '\nRw'), [58])
    def test_case_981(self):
        self.assertEqual(pattern_match('\t;r[!\n\n^\\M\x0bp:\x0cv27@ DK0dN`?HB#lQ.\x08lGNum\x0b`?j\x0cm\r\n\x0bMs9\x0c\x08P\x0c\t+S\x0b*\r7BRI\n\t\x0b/c"[t2+\x08"5C\rs&xJo1\x0b\ni8;y*U:n~@r', 'I\n\t'), [63])
    def test_case_982(self):
        self.assertEqual(pattern_match('\x0cm\n\t\r#\t.\x0b{(x|K\x08J]aJ^]\t?~2lj%"P\nuE\x0b\r^{\x0ceX2\x0b78447\x0b :y\x08h\nl\rWU\t(:\x0c"`%b7L>T;({R*\n"\t5v\rHE\x08X|p~sZfLxkFqa\x0cg}}=[', 'uE\x0b\r'), [31])
    def test_case_983(self):
        self.assertEqual(pattern_match('Ar\x08i\x08\x0cG\x0b,H\n-/p)WW\rwg@N\t\tr\x0c"\t{z\x08\n\na3=M8_\tIK\nsj\tE\x0bI\x08%A8\rM_ >PMj\x08J9\x08', '%A8\r'), [50])
    def test_case_984(self):
        self.assertEqual(pattern_match('zGR\\;j>#(pYAl8:{aF}q;?\x0cbf\r\x08\nDX\r{\t;rJ\x08\taA8=O?2#^pFNCxw{t .w\'C2Z6?q=b_H~Y\t\r\rK6"k\x0b<\x0cQ~1\n\x0b{\x0b\x0b', 'A8'), [39])
    def test_case_985(self):
        self.assertEqual(pattern_match('p/[\'_G9"s\\c`b\x0c7y8*~cmgc#`bGD9#@YR(zR\t]6\x0cutGx&Kw)~TD]A3n\x0ck\re&\x0cB}\x0c{w^U)6d"\r"LR\x08\tNr:gwU\t#nIDk;', '\tNr:'), [77])
    def test_case_986(self):
        self.assertEqual(pattern_match('/pT\\A/-B}/\x08Pl~1q)C*VG?\n\'|N*^]}\x0b{oz\x0b#u@C\r+D\x0bv`\x0bVW0mnptg|nwmJ<\x08"|[G"Nh\x0b \r\r5=de/3)nM8v5;(gKni/.]\tl', '\x0b{oz'), [30])
    def test_case_987(self):
        self.assertEqual(pattern_match('>\r\rh!\x0b\x08!-qEwU"K(HO\n\t|\t1>\x08?\x08Tf\x0c\n\nau\x0cxEE\tt@c\rM,UL\x08[00u\tE4YLL^e', '0u\tE4Y'), [50])
    def test_case_988(self):
        self.assertEqual(pattern_match(':XFs?EsSJz:dPNgw\rd\rt\x0c\x08\r2X(zD\x0b\\s!t\x0bLb-gzE2\t~}W\x08n\x08\t(\r~E\x0c~\x08mN/\n+9syYHT}\t6>]\x0c\x08\t=Y5OML3QMD](i>X-\rGjZ\tCu\t3\r=y\t\x08+p9\x0cz!\nNyQCQA}\x0b', 'Y5OML'), [76])
    def test_case_989(self):
        self.assertEqual(pattern_match(')0y%#\x0b\x0c%{\tvD)kga8:-DB\x08^SKGf\nx\rjlb\nSIrGko52>P;*_**\x08 \x0c%zqb^WbR\n^mk[\x0b\tY1Pi}&_EWl\r:N\x0c=o\x0b^(\x0c(p\nS.qDl\rUP2P', '%{\tvD'), [7])
    def test_case_990(self):
        self.assertEqual(pattern_match('\x08%\x08]\x0c\t(I1F.K,2\raM\x085\tE@E>)\n_jTYr2\x0cd6@fG6\x0b\tx=*,%\'4W\x0cV]m\x0cY=_V1\' \n,`~N@BYUUbY8FV3+8nK\x0bpQFV^WT\x08m5_\tVJ8r"]\nso', 'pQFV^W'), [82])
    def test_case_991(self):
        self.assertEqual(pattern_match('(n,58l\x08\x0b4mbA\x0bF"(\x0c"7x!4\tO.\x0bV0 99\nR\x0c;kV\x0b30v\x0c#bt\r&\x0bm-OQB6x\x0b3T:v5\'ETru\n29PiZ7N2&\t]\nO\x0c\'#@\r^r(T}ZHi\r(R@', '29Pi'), [67])
    def test_case_992(self):
        self.assertEqual(pattern_match('K\x0ccm8Eyq"h+Mi\tE>_\'\rYN(\r!{cfe3pkC\r\tg-\r\x0c>.\t3K&-l`lGsX\r\t>e^!2\x08\n<JszE\x0ceJ^/|n\r|', 'JszE'), [61])
    def test_case_993(self):
        self.assertEqual(pattern_match('* n\x08(B!b\x086Sr\x0c6s\n22G\x0b`?\tf2E=\x0cG\x08\r{Bx\tN=[,\t\x08gj\x0b/L@w\x0cMhBIIYf2s%nq:&wVYD#q\t\rM\n(@\t<h\rdftv2qR1Z6O\nm|', '\x08(B!b\x08'), [3])
    def test_case_994(self):
        self.assertEqual(pattern_match("G1#i\x0c4p6EP\x08\r''sC\x0c\n\x0ccm\tfZ-q\x083 \rF\x0c\t'(\x0cO}l\x0c\x0clLY+c\x0b#qVTJ>&]K\n#7FM\x08@T\r?cEY\x08Num\nQ #y\nH3M\ne3Bf<j\n\\\x08z(\x0b)}H<\x0ce7bQ\x0b*\r\n\t8", 'J>'), [51])
    def test_case_995(self):
        self.assertEqual(pattern_match(';{\t84UtdQ\\Wi\x0c4b\'T}"A+ds)[J\x08\x08\x0b\x0b{o\r+\n\t%>OK(Q|\t\t\x0bj`{pS\'&[k4eO>\npy\x08?\x0c^\x0b:,hW\x08K\x0b\'u4};A5g\x0b?.\tm\t\n\x0b\r\x0b!\x0cx\rE\r-s\x0c#4\tX9\x0cw~<\t', '+ds)[J'), [20])
    def test_case_996(self):
        self.assertEqual(pattern_match('L,\x08w\x0bs\x08M:}wXMpm{x+,G0p`b>\x0c\\\'F`\\-E(o\t\x08\r8\\`aUJdk+<P4dn/Rk9em\r_v4\rYY\x0c\x0bx\t\x0bG}\x08V[dLW@\x08\t.\t\nx\n\t}a3V"I\t\t)n', 'F`\\-'), [28])
    def test_case_997(self):
        self.assertEqual(pattern_match('C+ekwy\t\r3Y\t1\x08T_Xo~\x0cs \t\x0cAT\x08g\x0c,T\x08VS9!\n:E|q=K|w-I)c)W"BC_dRo\rqg\r=6]\te(.P\niLM\r\nq\nbFCl;SFbk@n{ocMJes\t%*\\*/\x0bVFXFsV\x0c\\z', 'Fb'), [83])
    def test_case_998(self):
        self.assertEqual(pattern_match("{X].\t>xe\t\tx#.MSs7@|G+4fEB\n\rMjjv6 @\x0bpg'I\x08\x0b\x0ctl\x0b#>%(k#fp\teSSVeD,H?q2\x08-2u^\x0c|n\x08\\\x08bO D|Uq\x0bw'>=/`VMiC,|#%fBUz'7", '^\x0c|n\x08\\'), [69])
    def test_case_999(self):
        self.assertEqual(pattern_match('3;C\rJe}L\t>hvvL\'Q\x0b\x0bgj{@+RQb=>F\t\x08\\j+mQO_y\t\r"3K?#PK?#\r]\x0bd;nK\x0b(/L\x0c+\rH\n\x08Y&1\t\x0b\td+\'~!g9(W9a', '3K?'), [42])

if __name__ == "__main__":
    unittest.main()
