import unittest
from suffix_tree_matching import SuffixTree

def pattern_match(text, pattern):
    tree = SuffixTree(text)
    return tree.search_exact(pattern)

class TestGeneratedLowercaseCases(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(pattern_match('cl.^Qmah3freSiYn9o;U]v*c0aYy_Bv{_Q=f\nxj\x0c7G&ZL+Wdk]74', 'j\x0c7G'), [38])
    def test_case_1(self):
        self.assertEqual(pattern_match('A:.d\n9[SB8`7NgL#*FB\r:?FJ.r\x080r4bS)TJG\x0b\n,<"C s$YY\\fN+>#MKa~\\q[', '?FJ.r'), [21])
    def test_case_2(self):
        self.assertEqual(pattern_match('@e/BRdIl*TRQ|A,|K:XUi Mf;Y6EyISJ]\\z#s[x=68c8DM( E4Y*fy5)Or.*&v/\x0c[zPQ[K:c<V?OPUsza6auCwnszn&-W%', '#s[x'), [35])
    def test_case_3(self):
        self.assertEqual(pattern_match('F[6C(GkW{X<yR6b^^Lp\tAEg\nB\ni&,U{2|Swz\\3kLH.&3dr[imd9*SfL>$sYe&~S\x0b(BGO\x0ciYn,#<?~`2?vEnj9){j@Vm]qt&1', 'vEnj9'), [80])
    def test_case_4(self):
        self.assertEqual(pattern_match('83}S_j\t38op$Kj5{T\rmBJQ EZ0(8?z#RMs76Y6\rF6j{\n<eqoR\\|k3yx HSAxQzv7"LhmGB\\`Mp$)\rYA)2#sGvUn (Wd7l', 'EZ0'), [23])
    def test_case_5(self):
        self.assertEqual(pattern_match('xk<\\<T6]\x0b<U*[xJ*\x08\x0b\x0cRH!9<3L?I2Hx-"\x08zX!1b(z+904\x0c1ON@_)j2),9/84:AT!d3', 'I2Hx-"'), [27])
    def test_case_6(self):
        self.assertEqual(pattern_match(';^4.AHC|26o<`7(L+PG\'R\t,JltwR?\n.{ s8Z@{9<p9\x08_eu.%T"\x08[eb -mv\\^b#W>/', 'v\\^b#W'), [57])
    def test_case_7(self):
        self.assertEqual(pattern_match('Bvl>V -1o\\JSc0QX}pLEEz"0a1t<#=(KyB{ry=cS8(<nFAL\rmfvXcPqJlmy^q=o_W3~Ll', '(KyB'), [30])
    def test_case_8(self):
        self.assertEqual(pattern_match('d\x08EI\x0bM).A*z792bPvHM\x0b{BC>l05<oDt=D,ZGrVbl\x08,Ai%FS[r5S*\n:6p]8Put! 8&_{O_~-UYu|8a;\x08@AGk*S.j', 'u|8a'), [73])
    def test_case_9(self):
        self.assertEqual(pattern_match('aYam\x0bfam9V;?3-!7h0\\-j5c\tFsH:kji!QC2b{h*CW6,*$7j[qAHVrYW~x)"E;C}V[\x0c~;3)Zr^?*\r#4]]6jDS)K{YhOg`|a\tTz', 'rYW'), [52])
    def test_case_10(self):
        self.assertEqual(pattern_match("8\x0c$5.aQ_ka/\t7/rU+E'FC\\t=C'N# g=7[b'\nbc_\x08SF@k5^g1g+wFU7rrX\r\t\rR(@Qgf~#z~E \rG", "b'\nbc_"), [33])
    def test_case_11(self):
        self.assertEqual(pattern_match(':\x08S,v3/p&9]cff0H jB0CMbm=6G`-&+{}J[;6:tVPpVFl ]s@;W2o8\n*U\x08F\r20XXt)i9?$k', 'v3/p'), [4])
    def test_case_12(self):
        self.assertEqual(pattern_match('3#%Yc1yo3_\rje-uCqsfo@1*I%~.rGa}$tAQ4pK"/}R>qjz\'zjX4F?\\ `,&3SVu!^3;FC\'1II!\n7(x', "z'zjX"), [45])
    def test_case_13(self):
        self.assertEqual(pattern_match('G2wYq9B}DQ34#|z6zDz4tH+m3 N.X@HOlK \nYNp7TO]Zm\x0c$F%\rb899?Z1:_\\?{IlQ-', '#|z6z'), [12])
    def test_case_14(self):
        self.assertEqual(pattern_match('6_\t$k"q\x0c>q5tJep)GfbCEwA*FuC#>e{8wwh80\t\rP*Z/QVcnE=NbeFFf5Cx4/j+<+QJ&<,w6#Uh6`@i+aU"g(/$A', '+aU"'), [78])
    def test_case_15(self):
        self.assertEqual(pattern_match('\t#T\'>W8\nwhDH(d)dWu->a{O0B)}9ZE\x0b"#R4\'$^ \t!3GOT?N\x0b|\x08xGXb$WeN\x0b;,#>0cgT\x08rwbV."$97&Wj"P', '3GOT'), [41])
    def test_case_16(self):
        self.assertEqual(pattern_match('M_+r*5P 4}Kp9Y!8;dXsAx<pt^[drFX.25.r;$3\ri.zH>9Af"">qvF/b/?9B\r#rrG`n_^7deWPDIV rsj\n\x0czW % uOuK1sZa~Tq', 'B\r#'), [59])
    def test_case_17(self):
        self.assertEqual(pattern_match('pW.Y\\i!7zKG>|R0#QE\'|-dY.1$S_{}\rz|yxP42B*\x0bS+hwg(ssFuIDpP"\'e);h;MG\n\x0c\'=!E 9Y0+"\rqz>#M?!}M ~JC6\x0cYFB~J+', 'Y\\i!7'), [3])
    def test_case_18(self):
        self.assertEqual(pattern_match('vebKjKfp_Tg+1.C%Y{\x0b\\J]VQq5v\t$i9u"\\xJ?/e{\nw\x08\r\thR-l($\n(aBQpuftp^?Ykq)>$4#\r\r}w', 'Tg+1'), [9])
    def test_case_19(self):
        self.assertEqual(pattern_match('}KMMn1MbeMv>\n,z,Pm+wb`^zr9;Z0V\t#\\\tx`:{[?UC\rCv*(4u.Nqb|p=Vtr=7s^ j:;&uc/Lw/3G\n', '\t#\\\tx'), [30])
    def test_case_20(self):
        self.assertEqual(pattern_match('*wl7!Q;5\x08\x0ciIe\x0cqcj6]H=yYMRUg(!zsU?b.Yr},]\x0cOyG~8\x0b2$Y=I [9hU7<xLQ&', 'OyG~8\x0b'), [41])
    def test_case_21(self):
        self.assertEqual(pattern_match("ovsGI1jni\nkW\x0csgi(0`wFN\n\nO\x0cadDT2Ko_\x0c]%P!~39/OV>x,IBvXH.)/LVxrsAwZ\niAkb'\x08njD<N^\\`K'0P\x0b/b", '/LVx'), [55])
    def test_case_22(self):
        self.assertEqual(pattern_match('5t5V^o!"F1>8r"fgP9,ipevMkY\x0bLI{%;q0LvSPqH-\x0b>\x08UBNo\x08SL`JU_}g8PdH^v\tU)?', 'ipevMk'), [19])
    def test_case_23(self):
        self.assertEqual(pattern_match('Y;r+Eu KTT/ZAkSV\tWn44!7k{1x\\w\ro3K0 #2d]ehRITv\\T<Z,.GFX%cuJ$xwr\x0cKM86L\\[`#', 'k{1x\\'), [23])
    def test_case_24(self):
        self.assertEqual(pattern_match("@l /\x0cUN\x08hX=sM1]HD>|+2xI;p^!(X1}/^z)pVEd-'BmU}u0q$-w\x0c_%M", 'xI;p^!'), [21])
    def test_case_25(self):
        self.assertEqual(pattern_match('/V=4d`KX|@Y|\n)%\x0b+uso\x08|Leo-9}*\x0c4fA|F"##W7c!iRyTqM_v}>NGCj^|?hMC$;/BxFagm.;Sz\x08VMJ\x0bmTv$:I_]Y%FJM3x9', 'RyT'), [43])
    def test_case_26(self):
        self.assertEqual(pattern_match('z-cyl8~\x0bStr!KOd"O9C#rR3_.CKm\r=r4_Qo}\ntf9#hK,T^yK\r0u%T  _\x08~q6ua?@\'7gG.|*i=K&II(_f', 'T  _\x08~'), [52])
    def test_case_27(self):
        self.assertEqual(pattern_match('\rG3vl4\'&xdE-e(|k\x08:g-PvV&6|UkO|zy[3}OL R:!8%:FJE8G4g\t\x08pC5\x0b\\R\'{Q\x0c-VGT7)W/s"\x08#c$(', 'O|zy'), [28])
    def test_case_28(self):
        self.assertEqual(pattern_match("<,1cf2:-?juQ\x0cJ&#y!%#sM\r`65j#Te>t@#<jO\x0bgJf4@i\x08/#-sh~-c+\x08fWPu1lZY>BR;=[`>g-\n:VkQ2@H\x08$|pS'r\n&Kg` ", '<,1cf'), [0])
    def test_case_29(self):
        self.assertEqual(pattern_match('.g#?(%z\x0baHjwGxF+#XHdM[\r&;xtE"[3$\x08X[(fqaJd#6K9dtTG69LqETnNZq]V\x0cnc\\[\\I4AR==\x0cV', '.g#?'), [0])
    def test_case_30(self):
        self.assertEqual(pattern_match('Y{~Q=/MWNgP{8U7>4*\n1\x08g=>!P55ndF\r\\CF1i6a/$K z8\'}f3Q\x0c+<\nU!6)\\le"oV3\x0cE{B/!Wsu\x0cqi-90a(WMgy+:d(F]', 'F\r\\'), [30])
    def test_case_31(self):
        self.assertEqual(pattern_match("#MbVV%?ln(2.g'+z=NUEt_\x0b^_-n9NCp\x08KgFKz3kXjWoNEXx[IYnUF=;2!O|zX\nL", '=;2!O'), [53])
    def test_case_32(self):
        self.assertEqual(pattern_match('T\x08B|1Bp+/(q#2o4xDuWT;RSM?ZR#{\tT]#/H2ms)d$%}^xlwDD!s\x0byrQ\x08_5 O.', '%}^xlw'), [41])
    def test_case_33(self):
        self.assertEqual(pattern_match('uFI.f\t!4LM.UK649G@-`aL"Pb("lxzHW&gx]J_NT\nC \x08zS\x0cCh!ue(BP6/2>H`#q', '\x0cCh!u'), [46])
    def test_case_34(self):
        self.assertEqual(pattern_match('5oR<V1N~dKAb3~!Q\x0cjOd_Gzq:mrZs\x0b?6\t9oaf8l%tyMprj_h31UA"h0PkR>gfQ=bM.bL@PnqbT6^R9\x0bBY5', 'kR>gfQ'), [56])
    def test_case_35(self):
        self.assertEqual(pattern_match("<\tdX6o}opuDRh9~=&0Y6!F)SeA<r~h:aM\\1zm<cefRe%';W2z/xWc~Bcs;\\#^J2j`!g[.lu)IX\x0cz*<d5r", ')IX\x0cz'), [71])
    def test_case_36(self):
        self.assertEqual(pattern_match('\x0b`\'Dr>3%7>4(:Kt\r`?sUQj!iV<:!|\nnc-c)r\t %ZTzootA9|QVjv%kQ\x08b 0|`/J &!H+\x0bL1Lf"qc', '(:Kt'), [11])
    def test_case_37(self):
        self.assertEqual(pattern_match('&c%~PbtD?i9r~\r]gv+8<\x089M,i5z[J\nfX\x0b\taRTL\n@okai`\x08#_QRw\rOV>2d@hn-*v3\\vM`Dw(', 'RTL\n@o'), [35])
    def test_case_38(self):
        self.assertEqual(pattern_match("pZo;Ji5r8\nDK!$J!su.SIBb)Nn,47ue$_svDfgdU-c#\rol|4\n`tpOIL\\C{!('f :et]", 'e$_s'), [30])
    def test_case_39(self):
        self.assertEqual(pattern_match('K[Y_z\n692ph"}jeJmt}$jf\'V+X.2hn(F%(;N`\nyz%%(Y%pFLt)$zv0DqE~W?<xK\x08IY>r1?c;.fa|-kw', 'hn('), [28])
    def test_case_40(self):
        self.assertEqual(pattern_match('R"ob!y>V0kGAxw\x08tW]*t0=t5zP+NES\x089;oYcD\'\\0-g~vb{\'z-mca>`9FUq%\'Z$;NA\x0c:r=d2C\rxj9ZZCT3E[*I@WD^D\\9qZC a)V', 'kGA'), [9])
    def test_case_41(self):
        self.assertEqual(pattern_match('DPGp1sD0f;CJ!Z%jSjdmC[\x08ZYQx. E*^S,FRi1F\rcf+[w rM:,>)@2]u}OQ5Dw0uFaXu-O"/I>\x08(LvXD#@m%_QAj\\;)', 'C[\x08'), [20])
    def test_case_42(self):
        self.assertEqual(pattern_match('R*3C\n6":~?#lD"UjoHOV/J$~p9S>5JEL56$rsK@c\x0bdQUZr:%N\rq\x08M#!ExZ6rs*$C:Bn_pa]oC\t*HMs%7(trOwr~I\nM-?yXF@\\Z<{', 'D"Ujo'), [12])
    def test_case_43(self):
        self.assertEqual(pattern_match('h%wqIA HbIl+l7Sjx\\xY2z[f""dN]lLlR\x0c"(w9rq9gcfP/.x7?9v\r5ubFZCvA"b.#bawI=w\x0ciXm\'\x0b`E4D4lpZ\x0cC\rQ<d', "Xm'\x0b"), [73])
    def test_case_44(self):
        self.assertEqual(pattern_match("5bgNKQ'sh2JV!!bj}3ez1\n+g\noOxcMJ C(1?qk*nVu]Tlez!i']cvW:#&6HgGGe4+\r\ne_sQ", 'J C(1?'), [30])
    def test_case_45(self):
        self.assertEqual(pattern_match('.\x0bU]9m\x0b7(K!b;"Y=D*v!5t;v4e"0FV.B{>/~6"\r\'$dD1a\raImm1V+T/lbHS\'lc\x0bcEV]pR2(t+\nv\'FG^k/8/E\r;;n', '/lb'), [54])
    def test_case_46(self):
        self.assertEqual(pattern_match('7Fe&\x0bwg4V}u$P>\x0bf8+|<elNgO$M\'afkP)@L |\n";0P;m\x0c^k#Ij\x08Evx:6]\'\x0b/46', '4V}u'), [7])
    def test_case_47(self):
        self.assertEqual(pattern_match("fI;\x0c/LL')\x0cG9\\I)%D^0IR=R<-a986fTSLw;lJ?.aH=.icWMT<`4", '^0IR='), [17])
    def test_case_48(self):
        self.assertEqual(pattern_match("F|x\x0ct\\\\0mhL-4AGlK%M&u{Ni 48xB\tBYp;^v^Dgp'?J6+H71F0yg+R:UtR)qx&r: 3*Ab", '+R:U'), [52])
    def test_case_49(self):
        self.assertEqual(pattern_match(']$p<u.\\3RB5[~V}+<~A)_NmB\rL\tAUdlY4n\'do5&0^+nz+_+JC mK$}?8xk"&%F1qxBVh;5(7<T"}X\x08BR4$XJy)re=', '}X\x08'), [75])
    def test_case_50(self):
        self.assertEqual(pattern_match('<Yu)SRt\t(8c#V(tI9\\c9.\n%4d=/mpHCPlU 9PW.{&u/SNg[<OhH]!V2eI', '\t(8c#V'), [7])
    def test_case_51(self):
        self.assertEqual(pattern_match("um/LR%#G8)JP-3.v9ldA~UMvKwiY5fm=6j_(rF2q\x0cn\tzcS/6A'~3\rhu42#-\x08 .S~Vo/h{>K\th\t^G\x0c@=2.\x0c\x08wP+k", 'o/h{>'), [65])
    def test_case_52(self):
        self.assertEqual(pattern_match(':8KloW|GG$l1iJ4\x08|\\ec|.Di\r)\n8K\rSG\tTk3 W?\x08rP)dV50Y\x0c\x0b3oEBgr/8{', '8Kl'), [1])
    def test_case_53(self):
        self.assertEqual(pattern_match("]|q\\bKY|~SD-LR9)Y\x08BS_x(S2\tyu7?\\-er>4y\x0blJjMnE>zN[\x0c_pN9bMSZBf~Z%4^gvBlc%QuygAcg(4G6wokG7!?X']iJBa", 'wokG'), [81])
    def test_case_54(self):
        self.assertEqual(pattern_match('jU\x08R]I&.h4#"*j2c\tN,.~r;i\nteh@S\nH_[_q9uk%HGRf*B^2qiw+>-?u[0t(i\x08Qa#|:m-ScUGsoPE7t^K$QSB-U', 'U\x08R'), [1])
    def test_case_55(self):
        self.assertEqual(pattern_match("7/,G'>\x0822^(!>0?\x08pT;EHQo[SG{+tZENNr>D`\na+\\\x08:[\ndS\x08k:[!;V\rqJ7Cp\x08_uxB*R_s{8#D>}H8JU;", '(!>0?'), [10])
    def test_case_56(self):
        self.assertEqual(pattern_match('CC\ny,TOT2T*\re4TGDQoBG3U<LJS3C\rObd2F{ALzvr*R,ff/v<3,_:xC$}bP($.K3it\t$$#ukg_Q6', '.K3it\t'), [61])
    def test_case_57(self):
        self.assertEqual(pattern_match('iiI;c*YM7v\x0b?dui X2BY]a^\x0c8AH*pPePWB\x0cpwL~~ )iFWtY"Wx3', '^\x0c8AH'), [22])
    def test_case_58(self):
        self.assertEqual(pattern_match("Z70=d[a1_OH<i'oV~xQCp[DE97GtxyYY?(9u'n&2~\nW~e>^xY=|s\n~4PSqq8\n-wx!t{sG>A`SXy", 't{sG>'), [65])
    def test_case_59(self):
        self.assertEqual(pattern_match('leu_i9R(h"UG:ml\x0b*Gt7P|oU#sf<t\'#|@f*Rr\tO/~~2<tAy+G8.(d?~eB(\'%&BX&|5sya\td', '7P|'), [19])
    def test_case_60(self):
        self.assertEqual(pattern_match('`qs/mm8A{Gw-o${\x0bp|\r705G;/@0qDxtf,?{]O g)zcD)%&"KlP;jy!1pE}KHKMjW]', 'pE}K'), [55])
    def test_case_61(self):
        self.assertEqual(pattern_match('wV--~\tJzDf_y%;*Mo.\x0b|.bB)U~mC)KAGg\rjwr\x0ckd<dpzkeghi?`{!\r)(EOLcX)R]2#\x0b9}sH1\x08LV38xc', 'g\rjwr'), [32])
    def test_case_62(self):
        self.assertEqual(pattern_match('ys[*\x0b;#"Z[U\n\x0bx)5e`yr=vxz-\\m66l_"Yl?x?\\b2\x0ctsvz)KN]NeXh', '\n\x0bx'), [11])
    def test_case_63(self):
        self.assertEqual(pattern_match("6(0CjuQB-\x0cSQMO)/@vmwm5m/\\ x)_wdlfMz4G>iGQ8ia@SAT.iy[*{WOgS[0]#4)'n\\vDDN;G+\nlnY%5\n ry>Rh8_c]", "'n\\v"), [64])
    def test_case_64(self):
        self.assertEqual(pattern_match('2HTPJ4\x0c4!;X=E{xQa7t=Qy_/sd\nCt8-&`(O/^c.57!~,@o6o*eIT_NouC2GnR%`MAO+\r5rnq%0C\tlb', 'O/^'), [34])
    def test_case_65(self):
        self.assertEqual(pattern_match('NTh!3bslx<0sC4a~UXq iR&eK.<um:TUuZ*\x0c:cFl:~]BUs{S=b[\tCvD 8J', 'q iR&'), [18])
    def test_case_66(self):
        self.assertEqual(pattern_match('^y!:ftg$(l!xihDpR](X&Arv{Eai@\'<$z5\t%PzY"S^g+uW+w5_$TM2*w<E&^\';<{\\x$*fao02\x0bam\x08@', "'<$z5\t"), [29])
    def test_case_67(self):
        self.assertEqual(pattern_match('Rq6w2e?Wd!$:\tUCy#%Wh-rra0NyA6;)~]9UngUZ\x0cC9j&+PU3;x\n42fT)%&G=zs%1cC:u\\6t)Z+(8}h5k,3"\niwA\rh4%!W?r,8\x0cs', 's%1cC'), [61])
    def test_case_68(self):
        self.assertEqual(pattern_match('8pcr|GVb0@%rW)>}ziyt)8PYZI\nI~JTPy!+)]C>o8+%v%8Z$\x0cJjq{ho5_NHUA?\nm{n"|1hZR%', 'o5_NHU'), [54])
    def test_case_69(self):
        self.assertEqual(pattern_match(' PT8|w`Zj\x08~=cd2e[@;I9\t"{6|d[ek b"u_G4ue|Epcm\x0b /RsrRDD;@T~F`@j1\x08`g', '4ue'), [36])
    def test_case_70(self):
        self.assertEqual(pattern_match('rM|0>>xa!ogfv`4P]mBv)<u\\]CErQRj}vJYZ*-)=@tN)DHw8CQP`~\\c@ZdY3-UfS6\ryxT:wm2bH-CxL`ax84xL?B.S,iNz=i\n', '*-)='), [36])
    def test_case_71(self):
        self.assertEqual(pattern_match('zd\tmps$wfs_W|8`LD\rZf(UN;#a\t!%cX*kpvEzN"lfTB\\\nqJEz_8I$SMm~xd\'!7QiSVRw=?Fwi[\x0b;!qI\x08^eqw', 'qI\x08^eq'), [77])
    def test_case_72(self):
        self.assertEqual(pattern_match('G<t2|lH\x0c@U]Q(OLP:mkIBXTL<,rZkjPM*x\\\x0cp+-p?/4o>\tgA:\nFA\x0b 9e3\'|\x0cO(YCB|5tts_!G-Cs,u^\'t"', '_!G-'), [70])
    def test_case_73(self):
        self.assertEqual(pattern_match('{_Qo_]FLQtM)x\x0b;*em|@\\Ji:\\ih7^I((y-rgEva_0|XIuiw{#se<Vq567K#A0yYO\x0b.', 'tM)x'), [9])
    def test_case_74(self):
        self.assertEqual(pattern_match('^E shoTm\x0bz56X-.P+CT,[\x086N~w-t:Mp^S&B8 o+$0Z r8I7r`\n!\x0b{AOtrxto=wYH `=9h9\\ij', '7r`\n!'), [46])
    def test_case_75(self):
        self.assertEqual(pattern_match("r$\x0b'vmAYjzF7(|%MqT\\.r\x0c?bN1 jYW0-HNDD}?/XsV.V5oQ{M\x0bVi-nL/<ae=%IP", 'D}?/Xs'), [35])
    def test_case_76(self):
        self.assertEqual(pattern_match('|x>)v?` \nQhL_mZn`8z4x.\x08"`hPp"\'nk33A:R_\x0bv\t0a \nF<]K{Sj\n%;\x08t*"[`$9cX._I(JeeO\\{l"\x0c~hCe*,4F\x08', 't*"[`$'), [56])
    def test_case_77(self):
        self.assertEqual(pattern_match('S46c1L|Ov[Ng&szkM.]` 4CCw\t\tG0w6PCT@rBAB\x0cR4fd..11-9\\_#|*62D#9p\t>(6R)6LH0mX5&$!,pFA$M#F@0-gG^q2+8Nz`', 'w6PC'), [29])
    def test_case_78(self):
        self.assertEqual(pattern_match('G#[%?e?N#IUhYY%OEHt2+NLL/I"{~4z\nkeGc4AxBq`ys}.>xQ9kQ8>7Z\x08#\tmLa:%(2~sbjN[\ty6HAU.$eE_)lFn0\x0cmM_ O', '0\x0cmM_ '), [87])
    def test_case_79(self):
        self.assertEqual(pattern_match("]xH\\KN)e\r]a+[N%Jb,09a,VI,rE1:6}!J&}\t~&u_sgwnO\niqsI$L\ti6AQuc-6g}fqgl\\spz'fxi", 'xH\\KN)'), [1])
    def test_case_80(self):
        self.assertEqual(pattern_match("dp/\r\\k09t0g4Rty{)/YVf]|IZW[e19U\x08Kw]F4f\\fh|/Um(WsB/mDD<XtV+0Tz!L_LnM 'z_nqv|y%h-@$$tuO]-^0g", 'h-@$$t'), [77])
    def test_case_81(self):
        self.assertEqual(pattern_match(']:HiW e{ tSzw/qu.#i[m)AB68e2zLiHW&yeAQlbCXCrAN|"kR9z)8exC3,kV4L.tBni6W5pF-A3sD_\\^B/q', 'AB6'), [22])
    def test_case_82(self):
        self.assertEqual(pattern_match('5~,{/wrNR;[MFru2V^Mjx%{>N?HQ1F]))(u|R5pPZ8qzE*oAP5', '))('), [31])
    def test_case_83(self):
        self.assertEqual(pattern_match('>"hy(\x0bkk DVA\'V\x08V"\x0bg#Y^a|%1Yn\rvgfQ60ps7rKhY4Nwj,An6Vs<Ka;R?1Nj:h[BH!b7,\\', 'n6Vs<'), [48])
    def test_case_84(self):
        self.assertEqual(pattern_match('pZYD1?X ^y\x0c`oGjnBYHGBTdR0TxG.zNC\x08u^\x0cb+A/Y)l3lg.2.&o#6?JD@&lM|7M\'x_dEHcPk.8kjGXH8R]4zz:\tD3c}PI"2xC', '.2.&o#'), [46])
    def test_case_85(self):
        self.assertEqual(pattern_match('jQeH/S37vqKw%ir,G2!\x08&#@e\rs.FXR ZwB^fBvG:0=o\x0be\x08OHU(@D', '^fB'), [34])
    def test_case_86(self):
        self.assertEqual(pattern_match('Z>p\rK1\ta"eNh)N\\\t(P\x0cJL\\8ShsF[q."E\'\x082r(2*d/I3P_dX[eczw1:7#H\x08qcz=\x08/&T', '."E\'\x08'), [29])
    def test_case_87(self):
        self.assertEqual(pattern_match("Oq~}\t_mu|R/_)!pe gF~ZK(fb,yTl L305t\\jO\tg&>\n64U.kNlP'q<\x0b\x08J)WT[a1(jwCdfGOFba]\r[O&)]D#rzM~$\\4;`QE", "P'q<\x0b\x08"), [50])
    def test_case_88(self):
        self.assertEqual(pattern_match('VAYOj[Q{w{<EVf6U8CHQB-\\C5ftB?*FLg2@Anl8^{/MtS!g?=@!C&^eDG*xcJZ:', '8^{/'), [38])
    def test_case_89(self):
        self.assertEqual(pattern_match('l:#VR4xoQQ.Iw/@Zs\tQ8caP,,!"[rR(B]Yy2~K:2u6*$\\EwQ]W2v4uM\x08w)yh;H.#?0-Fqn', 'xoQQ.'), [6])
    def test_case_90(self):
        self.assertEqual(pattern_match(";%5E*5'].Ogn%>U}F\t*Z't3S,Xe\x0c}7`2f*/~/bcHn<2(iT Rz\x0cH*w)I jd:1gta", 'iT Rz\x0c'), [44])
    def test_case_91(self):
        self.assertEqual(pattern_match("j&xX,&<c8di0?cxdH>I2,~aQ.\\e'})GOl7<H/8S\t[2M}{4_8)<Y-ge\noH", '2M}{4_'), [41])
    def test_case_92(self):
        self.assertEqual(pattern_match('b.=O"]<zB>I"$a1FU$T@QUA~~m*</tUZeGRv&\'XF\x0bZClgJfqaD1o~U2dkD>K>f{M>vE', 'UZeGRv'), [30])
    def test_case_93(self):
        self.assertEqual(pattern_match('6XgWMZDjH0Eff>H%/G*>\x0c}!lj8b*n\x0b\x0c\x08xGcP`\\8:IE,;^AS}\\\\Juf%-H\r%3 U1~\rX^_k$~[=-u\tx=!? =h1', '=-u\t'), [71])
    def test_case_94(self):
        self.assertEqual(pattern_match("*Y.21D\x08=K6EaNBU/V1'VIC:,sY?,lc#kX3L[O;cfD+e`m?Kb>|mt[xM7k^KqX] \t~)vb\n`)=z,'PEE:!z*z", '`)='), [69])
    def test_case_95(self):
        self.assertEqual(pattern_match('l#hz!4)QaV\x08\x0bo-NWZ6sm%gP3|/k\x08)r}GJ\x0c\x081oqy]C)i%3C\r~Ov.Q.b-@^UYZThg6Q\tH!~[d2:ElxU:UB OP_!_/\t\t', 'Q\tH'), [64])
    def test_case_96(self):
        self.assertEqual(pattern_match('@3/\\bE8\n\tRW;$Yt~axwb0IUu\x0bW$.>k:"}74*Za<"-[Wz\x0b:Y.6\x08N\tnZ|f;q-E,V*:rTj4DPZ8\x0cx', '*:r'), [62])
    def test_case_97(self):
        self.assertEqual(pattern_match("BhVu:rYZl|K\n_EPBneN6m3(PKu(bRG'mbQp(B,<vD\x0cDHq\t7)s9\n7#\x08w7N9I#m(WUL", '_EPBn'), [12])
    def test_case_98(self):
        self.assertEqual(pattern_match("jOe\x0coV,\tS}=Hi_L|eYFY^+bc)o,\tK;S\nfYYf;Ssy76.E*g(y,//Tc{k\x0c4!E/VZ[?QkH\\T $fYKH?\x08Gd'rS*RE&", 'Oe\x0c'), [1])
    def test_case_99(self):
        self.assertEqual(pattern_match('U2B\x0b\t5b%\nB%1XHw)wH?mt6vr5m\x08p\x08\t;;ZUYd]Ptz?n\x08EaxzmxI]R{\x08ZRf5_eyu%f', ';ZUYd]'), [31])
    def test_case_100(self):
        self.assertEqual(pattern_match('O:o[,BCB]IbaOR=Vhw\'\'zF> Gz^G\'Lk~\x0b%{\r]Vob\';R }\x0c\n/6;X:i3a17\\.%KT>E0\\H|i;&lc+B,\\2DO79=Q\x0ce\'"[Y\x08%cVK', '\'"[Y'), [86])
    def test_case_101(self):
        self.assertEqual(pattern_match('M,|FX{Hu"qwzM/fY\x0bAW#\nh\\i\n_%>^:Y\x0bo~;jq0\t#<-3!\tKgP`yL!4(tp$3rJp,ixxi0F-?pj-qdHUQ;\x0bVr>xj4SYkTZxFYTIh', 'tp$'), [54])
    def test_case_102(self):
        self.assertEqual(pattern_match('iKy/_#AY:Qb%DF[j.l+ee\\vI[Q!q&_9cZwNyMj/~&?6Fo\x0b y}F=a@S3ga<"[IlG.Q;X7', '<"[Il'), [57])
    def test_case_103(self):
        self.assertEqual(pattern_match(")a&fBoFS|9}V(1K\tX%TV\x08(z\x0cxiTjQ\x08FY2Mm-&4ov*7@Oc\x0c(:o4yeoqf>K\x0c\rIULt]<^$l$]6'burV.G!JG*ae", 'o4ye'), [48])
    def test_case_104(self):
        self.assertEqual(pattern_match('!Q(;k}ebA~=0{^3\n@^BIm%(^YR@5|A-&\rcxy&\\GqC2FE8/1K%zbxGOy\\', 'A~='), [8])
    def test_case_105(self):
        self.assertEqual(pattern_match('wpFE\\T_H\n<v"\r[Y}!g^&|HV,~{<Z2|#|=IP7Ndib&f\x0cEcj|WdcXn{|2mn%eq9%)&*l}!+R,2Onl:!D-.(+\nt3 0t<J2(PB/9', '*l}!+R'), [64])
    def test_case_106(self):
        self.assertEqual(pattern_match('MZqI~2F"%m;U.Fp8&9\'e{k3&~>ge\rBOWQ@so=\'\x08\x0b{FE>"0oLrD3B>Z5 N[}i5\no1~_"^\x0b', '\x0b{FE>"'), [39])
    def test_case_107(self):
        self.assertEqual(pattern_match('\x0c(=V,fEd3t(:8HNUj~WZJU}4:)D\t\x0b{~\t#\x0c%+2a=7$\x0b\nC}}]j~=cX\r#G', 'U}4'), [21])
    def test_case_108(self):
        self.assertEqual(pattern_match('=G\n,FLI?7\t[)J01#It\x083E7m<E\x0b%2MN*V9h0\n_z\x08Yw4E\tP}n (L\\L\\LSQBmV.0??sZ\x08_( uh=&~\\%lqUA`JBc', 'UA`J'), [78])
    def test_case_109(self):
        self.assertEqual(pattern_match(']bugDr\x0ce+QD*sl"{vj\x0bK\\H$d\x08]Uy"6h\x0c->S_#X(\x08Od<c RuXjYmk9 c}"8\x0b', 'gDr\x0c'), [3])
    def test_case_110(self):
        self.assertEqual(pattern_match("yx&%el4%d!Ct!5\n(66nmOS,+0q>d<]+x4bD`TitI\x0bH9f)'oS}[a7", '\n(66'), [14])
    def test_case_111(self):
        self.assertEqual(pattern_match("t^f%q[\x0c|!S:SCJ\n$F[3lC\n2U$K45^a.I:&IROUfScu)\x0cneN'ZE\n%$nx@?8es;h`0\n@w%!%xlbi?M", '\n@w%!'), [64])
    def test_case_112(self):
        self.assertEqual(pattern_match('mXW\x0c$|aNgW[MiDDcx/c\x0bK?3-/w:CQHf{f>}#?\n{ceae1?,s{;NB{', 'Dcx/c\x0b'), [14])
    def test_case_113(self):
        self.assertEqual(pattern_match('NNo\n!`x21E&H5K@<Fhv>-o7Y\'9QL1\x088F!`V<yuvP|Yqi;  AV0;^5E6JP"GzyPDU($mr ', ';^5E'), [50])
    def test_case_114(self):
        self.assertEqual(pattern_match("P>,,f#OC4\x0cA;=R\\\\x))\\R\tr\rfxZ(a#1|T~Q,&JI,'%1wi~89NB(sU\x0bBwCW6yJt*((uMMv+pey8^Eg\r^%:", '6yJt*('), [58])
    def test_case_115(self):
        self.assertEqual(pattern_match("vNS2~l\nOZ1Q}8{\x0c`Q@7<QHnROp\x08O2v\r^\t-$F\r<Bt-rx9g;G\rJse-!J>4'CXQ|U'|ylieO>sL", 'QHn'), [20])
    def test_case_116(self):
        self.assertEqual(pattern_match('\x0bjX9 d3?0PauP&Af/\'g1k(Qe"lEtii3X5nWjCM{\t)C0^\'d|jW!5u{-!2qxyDB8 QBJ*0e\nHH1\rx!<dM&)vRk;W', 'B8 '), [60])
    def test_case_117(self):
        self.assertEqual(pattern_match('*3&)9&q<d(aMqiF=WWlqG"4&Y~|$:,>a\x0bGL+\x0806(Od4\t,${)J&;is6bk?^\x0bHn\t29"d`qMF:971^}:9f^(w>OA;W\x0cL-^iE', '$:,>a'), [27])
    def test_case_118(self):
        self.assertEqual(pattern_match('{g_6/a,eT\\Ez$3<)vk MCPs\tA)U$\rpP_["kD!i#^\tL!ZX*R%~m[#kj>r6/%K6B1h)', '[#kj>r'), [50])
    def test_case_119(self):
        self.assertEqual(pattern_match("e6'5/pY4Xb?pmy>37<1Y~T5e@aeDo\x0bRT <$dz}~r9q6BYTg RRSGZ=O4(p$Rdy\x0bKX>;kx]H\x0ck#Wh:'cSZ-Z^\x08<~8WDF.TzRs,/Y`", 'y\x0bKX>'), [61])
    def test_case_120(self):
        self.assertEqual(pattern_match('\n-e+cR{(qg#vh*I?:-h^C#]SDe#*s%(*:gwVe&To=eft<\x08@s\\tCR|\nda`qEe:]+J[', ':gwVe&'), [32])
    def test_case_121(self):
        self.assertEqual(pattern_match('?\x0b7}em\x0bWi\'(g\r1F+G,?+IF3):!SsK^z#`Ew*r9~Q0nG!Y$hJ\x08"VG! +%*', 'G,?'), [16])
    def test_case_122(self):
        self.assertEqual(pattern_match(",Dgh8@rFUm5sDN6+k2c\n0`5'\x0bP)fa)Z7:}Kd%:;%5p\tJaH$&8QY!.y Ul-ua=OIYC0'HGc\\'V.m6#H<i:RJpd#@Be+B", 'ua=OI'), [58])
    def test_case_123(self):
        self.assertEqual(pattern_match("lW?\t@m`xJNG-8'HQ&eZv&O$~\n,j[c!)q(0Hv\r\x0bta`f$jO9\x08pg^a&=D8", '`xJN'), [6])
    def test_case_124(self):
        self.assertEqual(pattern_match('^8[\x0bUwL70Z"RC_nP}iXV3^z<_f:=NjJms@\'V(g9>bgZ4F\x0clY}D~};[UX+Jbz[ggLBXI*S&\x0c up.C+M14~\x0b"\n*', 'D~}'), [49])
    def test_case_125(self):
        self.assertEqual(pattern_match('>j|\x08Z2wL=bh"\x0bPg$Xs\tWMkn8w>O-i#aF8<)LPUK%SWc?{d)Fm#', '8<)LP'), [32])
    def test_case_126(self):
        self.assertEqual(pattern_match('FE#dZT]WBAS1u~hAVm&ln2B/wlw#k\n:R=87W$y~U-V-jWc-Ckq_P o ^Y,A;jNT.:O\rwi{/1;PRDe;Ur.Izd9%', '/1;'), [70])
    def test_case_127(self):
        self.assertEqual(pattern_match('qWM_+OE_y"gD<3{Z.jh9D?}e@/T&~=`xXYQ6>2|\tMJ7dR;409=_82XU\tz/^#g*aO7Sw.OU6sF+', 'T&~='), [26])
    def test_case_128(self):
        self.assertEqual(pattern_match("_|i3xE~xz]Dd`\n#OO'$I\thXZa!Yu?>&>\x0c(.%%7Or<u`MEVH7>!2:?4g[p4=R'WoUqzv[/zi\x0b0Ez&:Nk]UNs", 'Za!'), [23])
    def test_case_129(self):
        self.assertEqual(pattern_match("s<\x0c8I9&0zT2OAw\x08mcMcO3KJ6i:CX6QQ0v,`\rS[4gwHq)x-hrUu-RhRL1VcXNl#A]g'q\x0bg9lTIpAcdXl5<<L{7}^j?cGGy'8", '3KJ6i'), [20])
    def test_case_130(self):
        self.assertEqual(pattern_match('RI|nE]pa\\m1<GEXAC"Z~wY\x0c:\x0bIQ)uk4{#t1{10ZoF(Vw|GwHbWKF+oy\x0c\rsB\'xe\x0b\x08+d<rn:I2j;sFq`,FVu{.-ql"6AR\rZG', 'Vu{'), [80])
    def test_case_131(self):
        self.assertEqual(pattern_match('}Z8p/5:$rl+jL{mN\t37eMqoS1\x0c@9a?!mwu5_G\tyWP_4d5$vnM=%#v\x0b6Ua"WYsOnt?C9no_\\.U$de4|\nAam', 'mwu5_G'), [31])
    def test_case_132(self):
        self.assertEqual(pattern_match('o#o%M\x0b<[my61W48 <AZf"Ay\nd~}IYu\x0b>-_X$;WGE^n<#KDD|I8ML\ts6);I`v8)}]', '61W'), [10])
    def test_case_133(self):
        self.assertEqual(pattern_match("}g1>\r$sz%33|VH*\nL^,W8V[\\aV 0'7\rK-_1)hs`*-2Iq\x0ci\r\x0b-QuVlCU9\x0b/\x08z{S\tgfosf%ZR[fk(J&pBX[D{", 'V[\\aV '), [21])
    def test_case_134(self):
        self.assertEqual(pattern_match('.f$\x08?e{wL<\r{:`\nN(;\tb[{7=wULLu`MhN{q>A.r^*Y77X&go/c)7(R3d&IaT-@5zN(EPi&.E,*t%r;$4{_+%>[yjN(i/V#g 1B-&', '%r;$4{'), [75])
    def test_case_135(self):
        self.assertEqual(pattern_match('s\'T/Lt`XY!18h`{]TJ6t:Bs"1N1hLzd$-@_-6[0>>0IJRla:?m#43L[2*xy\x08/E_Hn*KM\n )qnV\x08QeH3ZImQ\x08t\\xx:S..', '0>>'), [38])
    def test_case_136(self):
        self.assertEqual(pattern_match("'1fo-`z_v\x08^T\twwG1UIPE,xZ SBG\x081Q:M534cIa&Rb(8s\x0byVtW%.\r{L<~`&Xi\x08,yOQ!bEnhF'n \x0bZm^^v*#7|MdUyb?\x08\rzXwDm", '\x0byV'), [45])
    def test_case_137(self):
        self.assertEqual(pattern_match("\x0b+\n'<#I.)tWr|0\x0bW<=]ge\nbvHS84\\y29T9D/)A_bf`D.TUnEqw$*o_S1CJ`W;!09", '$*o_S1'), [50])
    def test_case_138(self):
        self.assertEqual(pattern_match('*s0:Wd>dFa%oy,MO!,Gxe.:;6BM:H\x0cViFM$YDx3\\Jt#G&x(e@0\x0c\x0b(};>tOn', '#G&'), [42])
    def test_case_139(self):
        self.assertEqual(pattern_match('kjqLCvzVppB_$isqSs |I?;=~Q"$y5o//h0>bbpG7Nzx\\m2UJB', '$y5o//'), [27])
    def test_case_140(self):
        self.assertEqual(pattern_match("vH*Ux\ncR\tx_=_HA\\?6hY&GD9r4n=,G? (_B|2\x0b6][KI,uo<mqFN|G; <^@J'Kp", '9r4n='), [23])
    def test_case_141(self):
        self.assertEqual(pattern_match("V[+}Z_c_2{b )o2v*?]F<NK|'lD27TZ-aKWGo!>\\#.$Q!.\x0cd\x0cru1\x08u(;ZrXI!\x08lna5w\nK#)1azUIhn1wKo*:'", 'd\x0cr'), [47])
    def test_case_142(self):
        self.assertEqual(pattern_match('|\'&\x08Rfl.,Nb\x0c=h`"K;:l:_\x0c@tfd@%.k9b"F"l\x0barfX\',TN}n,6]^CxVs[a-|w0sD"\x0czc &VZ\rq\ts>E(=i4dmtS\t)<z(Q', ';:l:_'), [17])
    def test_case_143(self):
        self.assertEqual(pattern_match(']Au<W85s2{aqe~/M7wdyD$Jd4s\x0cm$rZ[XtXL7=~?vORb-/W+5(\':/C&v\x0898-"B}EihGthf"x2V\nGB#2uc+PJcU%ZV', '5s2{aq'), [6])
    def test_case_144(self):
        self.assertEqual(pattern_match("K%26w8Cj0.DR>44\x08GsnH\nD'GrhMt6&d\r-0Sp4%HH3VB!*Z=YP3\x08yU\x08O8}dz\x08=", 'K%26w8'), [0])
    def test_case_145(self):
        self.assertEqual(pattern_match('UFz_CgpQSY"F\\y5;}Ou]B/?\'x2lL4:3F{lY5m@0[ E\'h%l=^>A( ~@`]4!p~', "'h%l="), [42])
    def test_case_146(self):
        self.assertEqual(pattern_match('hHE^|=:\x08L7~PL&>L[.pmwc/m@JxUv\x0c!XBmz~+k\nBTTe= |Ra \tzXm%8/&7tZM":e74[]`H:OzCe|<J9Q1_[#1~qU\\nK\x0857j', '&7tZM"'), [56])
    def test_case_147(self):
        self.assertEqual(pattern_match("y`JIPJ^{i_nmo8w9`YI$JKB/w}Y3?g`1Hf%K{waY1?x-wKk]|n:\nYpk^B-.J';EuDu{Z\t", 'Kk]|n'), [45])
    def test_case_148(self):
        self.assertEqual(pattern_match('i>Ym`g;qbQ?#Rt}7Z4yi[IT:([zb0iS}@\n{y#VOI<2gV`i[9<JF{Yb45k[enzd1', 'JF{Yb4'), [49])
    def test_case_149(self):
        self.assertEqual(pattern_match('Io\x0cVlT\x0cr*<=zk2*P^\x08e<#U`\x08\x0b!a:#;4pSW+.[N#$qbPgqczAn`T1I5V\nD"i\x085ov!zd', '*P^\x08e<'), [14])
    def test_case_150(self):
        self.assertEqual(pattern_match('\\szCIaW}WYC6saj0av_t+*"\x08bm_0\'Ts\tG;[#(Lc~]5|K)o|\x08~@@M=\'R\x0cQVpj%Zj9B$b}H]%[Y(Zb\x08/;A;\r8', 'Lc~]5'), [37])
    def test_case_151(self):
        self.assertEqual(pattern_match('6)g<j\x0c4XB;nq@s\n<4s~<=\x0ba2o;\x08VH$nHaE?\x0c81nMk>4"cM\rSm |=2H`BG\x0cS', '4"cM\r'), [42])
    def test_case_152(self):
        self.assertEqual(pattern_match('3})\\u4\'W,h;}DeA\n7s_42VT}qW0Kn[IUt\x08!mxO5~+"z0}"ys\'u_.y)PDS\x0c3u\'=q6i>"3a8Sv"|`a\'6@sy0Xf\x0bCk\x08tDl\x0bZ', 'IUt\x08'), [30])
    def test_case_153(self):
        self.assertEqual(pattern_match('Rxi)[{hc0Cy@*t\n^Yb\x0c~~)\\=_*~irBvEg\x0cQ~Ib!\t;zEJF,ShQ5T-h1fP6\x0bgTm|g+.ZG4Jf*O"z>V+\'\'**hh>{', 'P6\x0bgT'), [55])
    def test_case_154(self):
        self.assertEqual(pattern_match('V&R)@JrBaK+BL\tzI2/Xi=Hj\x0bYaNw\x0bA eCmB(NnfZ\rk[L-&\x0cr"j\x08s/f\tio8T,m?!hx=9[RDUW', 'Z\rk'), [39])
    def test_case_155(self):
        self.assertEqual(pattern_match('xFQfmk=PIEIed{e},\r"<VWmAWA Y<"n1jZx3{^6\'?fXuQ+uBNFfg_6}\'Y=!Rivg|%%\rg|{VG-31\x08dD&Siy', 'Qfm'), [2])
    def test_case_156(self):
        self.assertEqual(pattern_match('|"&\nUknk0O1&SvWM@B>O\rH\rYcl~b+45CC)k67.N8\x0b/9-43v\'$eb;k9Ng%p8EB^{ACb}\x0c!dLs^%Fx#\x0c"0Gc\nlI-+b', '!dLs'), [68])
    def test_case_157(self):
        self.assertEqual(pattern_match("7nL7e5q&wz(9'WM2w@9:\rgq/%g4~1}ZX[_4m2{g+\x0b5149u]6c>A py", '2w@'), [15])
    def test_case_158(self):
        self.assertEqual(pattern_match('G5z\x08wI;Wv?P|9+[;9i,*?B?ts@#")NO/<qp.^-QbI\t4"6a\x08pqK= .q=L^e7P|V\x0cCZQc4/1-T1L:=((\\c<5Q SGSqS<_mjsE;J^a', '\t4"'), [41])
    def test_case_159(self):
        self.assertEqual(pattern_match('UB-*P 2?"qi%A=oK{\n{Z{A!\x0cm"0.&HP"^Hpy~ezHh3nC$LgV7bM,;W\'tCo\r]Yw9-Y', '!\x0cm"'), [22])
    def test_case_160(self):
        self.assertEqual(pattern_match('axUTz]M-|8!<lACsu<wI\\P]Gu!(3yF<ws-YsiJ}`OgG5YHp\x0b-F4=MOa0oAA;8-vM}ug\x0bTg ;q@b\x0b:))Q0l', ' ;q@b'), [70])
    def test_case_161(self):
        self.assertEqual(pattern_match("J*E)?'>kSqt+\nPI0l>~\x087#\x0brm<|~cH;~:slJr~\x088[]yiyCF$5E\x0cOPG!Qe5Y\\QSlF\x0c", '~cH;~:'), [27])
    def test_case_162(self):
        self.assertEqual(pattern_match("s{XKK\\S')V7~mx[;8jm)S(!a+{abX_4W-+eo])4Mt%`H[jQwR:?m)fx|T\x08c3577I QR-kMjhb\nr,zVF\x0c%!9'y3(c=s", "'y3(c="), [83])
    def test_case_163(self):
        self.assertEqual(pattern_match('""zkWP\n\\\tuxX]sX8MaL9kn6\tf/)k*.VK^1k\njc?zFH5Z1mn9t=]`\tSXaK6LU_0)J\r\t9PT:xMM1w', '.VK^'), [29])
    def test_case_164(self):
        self.assertEqual(pattern_match('[#C/(N\\"*>>j"~%cA74E%^Me\rDoN~pTRamAvH}bL3\tk41wuGY&4GWazH!cr1Ms@CT)6UoXV8F\x0c.z\'=y<\'{cK', 'AvH}b'), [34])
    def test_case_165(self):
        self.assertEqual(pattern_match('epYa_.t\nX<Gx,5#Y$hT6\r2`&Lri-OV-\x08~zZ\rxRDG\x08688<)Rw\x08_\n.]{V\rB(]\rnK%OF\x0cy\ry`6|:1P%K`[', ':1P%K`'), [72])
    def test_case_166(self):
        self.assertEqual(pattern_match('iYCF+\nb"vy_MC?a@Pm;txxj\t[,2s[/x!/>h?N;]Dt\rToc702V$rXC#t3G?f$+B\r?.E,NL', 'h?N'), [34])
    def test_case_167(self):
        self.assertEqual(pattern_match('z!5FL#cM\r!1[H3W<\n`0y5\',z\x08"gP,".lJa\tflS5Hbbwc9 v,<,FJ?Gj`xr-R}$6@O*6(:x L?M#2 \x0b5\r=m:s4', 'v,<,F'), [46])
    def test_case_168(self):
        self.assertEqual(pattern_match("{\x0cJO'ZZ@&.s%TFB,?c?(`1w^qulF?]Of:D)dvb=2`j/N/4gp|e[Ip(]140]l", '@&.'), [7])
    def test_case_169(self):
        self.assertEqual(pattern_match('suH~St[D0a"c?\x08q4tY&@7&D,E6Xy\x0c:Ejxu8nQg\rE^kuNn:%\x0cbAMT=gaU q:[ v~xnVT]Eekq"z\nM.yJU\rF3?io^p6gMm}XQ8m', '[D0a"c'), [6])
    def test_case_170(self):
        self.assertEqual(pattern_match("Ib&}c'N!@ g9X:gy\nnr])^0<% \x0cNkm6\r1Yqu3IlBoV1I4,;c\n$c~brU<\rhvRShBq=\\2~B", '<\rhvRS'), [55])
    def test_case_171(self):
        self.assertEqual(pattern_match("PbgtM3N\x0b+{!-e>@%/\x0b_:>\x0cD.UJ34>:TnO.*f)[uH'm-)dGH##=`~wsVj\x0beO\rZ|=}i,\x0c)NY=]kq\x0b\x08!LH.\x0brvB}DSLzC6?}X7)Y3c", '\x08!LH.'), [75])
    def test_case_172(self):
        self.assertEqual(pattern_match('s/l$d?()yN\r\n6u_om\x08u?-HS\r/\x0bi`Hl\x08K%i a\x08\'B6uE>n:/t[3[z "}\nY\x08yaztwZp\'UccpTR0:$H1c?.', '\x08u?'), [17])
    def test_case_173(self):
        self.assertEqual(pattern_match('Xi\x0b"FJs>aX _YCYK+/N\\@;~Cy\x08}q@b|)H4.tyC}\n"3P~9c:T[Tn\r\rW#oB2%#vXJQmz7&l&uW>e#H\'', '"3P~9'), [40])
    def test_case_174(self):
        self.assertEqual(pattern_match('O\x0b2F;s4\tT"\x0c\n|0\x083xWV}Jx\nk3K2ci_ rt2Z9<s`8cv(R[#J1Oo5Z&M\\1]oJ}foOw`?RN', 'x\nk3K'), [21])
    def test_case_175(self):
        self.assertEqual(pattern_match('"$nC\n#?mL%\x0b4sd*\x0cmQ,G_kBvM*}&Xv]8<B@,nCE%T<0[\x08\to4a"9y\x08^`D/\x0b|bq\tvDK.|Z\x0cQ|Q/', '\x08\to4a'), [44])
    def test_case_176(self):
        self.assertEqual(pattern_match('t\x08YVr`\'ey\x08aP\x08Te2\rH#uNO,oRN+ \'j\n){R\te!NMU,fEhp&EQ?"mPH=JG+j3r"Q e7D\n|t\x0c_Ja?^eT&B1\x08"@En!.8Mz6-zke\\bCSk', '8Mz6'), [87])
    def test_case_177(self):
        self.assertEqual(pattern_match("HW\nBJ\r=oa6X(~G'o7pt1^Gq,OW_jDu5\r'$c& 9c\tvp.Q]nR#S:`75n?[A58z=lGV'", ']nR#S'), [44])
    def test_case_178(self):
        self.assertEqual(pattern_match("{4EI7xS89U\x0cbA,y>,ts$Q7sY\x0c\n~pd+?^GNT$iO\x08p\nPY-M-_5>}F2|+Q^Wu-w*'ay:\tO", 'ts$Q'), [17])
    def test_case_179(self):
        self.assertEqual(pattern_match("H/Bwj@Rf0V&kj'Z(rcR=kK0RH[ULc}wSRPCmp)>1V h`q*o[Z2gJYp'mDe6U+.\t\x0cOx/l\ngF75<3;%(,w-$<wEf^Cc\r;", ';%(,w'), [75])
    def test_case_180(self):
        self.assertEqual(pattern_match('v\tFN.`1,YE;W#~\x0bxWrF0s"!3St)HC Z3\nw"8;{2:aEg3`bo$n"Df~MEP69o!\x0b2kt=in^a\r-!7Q}_zG%^:tFl?>T>Z(I,0#w\x08\tWUm', '\r-!'), [69])
    def test_case_181(self):
        self.assertEqual(pattern_match('T\r6}sUpkH{VdZCOC[f,6X9?]y9c-}4;WSRw_^J4aZ[\r;q\x0baxhKb8-Zt]y<[}K-hOe;qQiInDgo\x0b1crR]tKqanr|S!\x08QLd', '|S!\x08Q'), [86])
    def test_case_182(self):
        self.assertEqual(pattern_match('P2n<tYn):~)5!\tx=m"\x0b-pn^3b=G\rhbycW- \'3[aSdi^__4BC2]$CzoW@`[W\tXM3kT`Ph ', 'P2n<t'), [0])
    def test_case_183(self):
        self.assertEqual(pattern_match('\\=\x08\\(t><suNV{hd\x0b\x08F$u/VVus;J]4\x0c(#KH  \x0b8XT4-WNaypj\x0b@<', ' \x0b8XT4'), [35])
    def test_case_184(self):
        self.assertEqual(pattern_match("pyt\x0cNn@! 'hWcU]O1UHnZ&iQw>YJ0C;\tt_\t:W7U_}T\\[^c=f,:^cM:xL<0*`Q64d0A9\x08 [*@Jy\tL$!<\n[+YkbJj@$.", 'Ykb'), [82])
    def test_case_185(self):
        self.assertEqual(pattern_match('\tKX/7l:9mNJaA!L?s?x#P6vMy!"!66P`@\x0b"9y@[%mN\n(Scr^]lx?{g&w&j9\'TB}vgi3E@+-akBR/.v4]Evm7', 'KX/'), [1])
    def test_case_186(self):
        self.assertEqual(pattern_match("RmUEN\x0b{&Tv%*JwR&[A$JDZJS<o!:sLU6X;qX&+}||)kotXO-PW] \x0btIj7'tn+ChpA~J!na&X", '6X;qX&'), [31])
    def test_case_187(self):
        self.assertEqual(pattern_match('&:!,gn`? np8dyoCN).~[G0h\x08(#g^pv)&@.1>al<mEU"G^4:uSz1$Y ', ',gn`? '), [3])
    def test_case_188(self):
        self.assertEqual(pattern_match('68CRpey=L8vv43O\x08\r<i337551d2\t-Thx1$_mIJO\'%D\t7F\'K}&/X3w3nd@t"', '&/X3w'), [48])
    def test_case_189(self):
        self.assertEqual(pattern_match('GV,9x^`;Awe3e/D*lC\t%SxV^*i?7#r>%-H55X\rRYm>Fw&Co%G*.nLw[%Po5-6ExmVK\x0bUg"p!gX,\x0c:"2bx2#I^$\'hX<`\\4/+SJ}|f', '7#r>'), [27])
    def test_case_190(self):
        self.assertEqual(pattern_match("=hfMWH{=<FaLJTw91p}1rerXz1Bh$2*Ze'L)T!(edFVXhz-Z7oMojFZP2J8#A'f/o9Xv[38@(C\\Sz\x0bD+__\nv\n", '+__\nv'), [79])
    def test_case_191(self):
        self.assertEqual(pattern_match(' G{\x08UtSw/q13/53z8~sa`b$XHL*-0WH;Hg]HR$=$D\rEfV9,eX; \\XN5r\\w1V%6|$ \\BR`2#7idA;^3}QN=L*)', 'dA;^3}'), [73])
    def test_case_192(self):
        self.assertEqual(pattern_match('"J/+C!%ikDul3HruACULx[\'P7x6v,\nw7 |uuv#5*[+etI]E6j{1o#(:}9>o.%$Y/X', 'x6v,'), [25])
    def test_case_193(self):
        self.assertEqual(pattern_match('&sk\\mgy{l:Qe\t*hT7wf"J["\tR{LttJzD7gB\rb7-Ndv5"D*uPy\x0c,:a', 'dv5'), [40])
    def test_case_194(self):
        self.assertEqual(pattern_match('][,}s\x0c\re\x0b~5soQ_CcJm1FkvWD\x08zw4xm#cWRWr3h"+de_A+UK4)Jqb\x0cne"', 'Q_CcJ'), [13])
    def test_case_195(self):
        self.assertEqual(pattern_match('> 5] CC>/k =\x0b\\fT;!2Kf>q5&j^55m1,8A\x0bdfXZpxIj3ciH[fX"MbQ (\nESHN_yV<7k?<\r)B7wwnM", /483`pifnhP', 'q5&j^5'), [22])
    def test_case_196(self):
        self.assertEqual(pattern_match('*mvc3F\x0c,FA_bS^eWyH@E|\\)*/2X\'kW<,<n1~,&O:|\'H7}c|S%FS2l9l BDP*{Lnq`PlUl\rR]Y(-"Ha{$oI@",&;^P', '^eWyH'), [13])
    def test_case_197(self):
        self.assertEqual(pattern_match("OyjX'2Ck5Gq>XXO{MvIHOXf|T_>p|qMH@f\nCek:kLxCIL>iuyMzs|R,fa\\~t9:?Y%yRuE'\rYw2+=M4=M,Ws\ta\x0bK)9wE%9Ma6Z'&", '|qMH'), [28])
    def test_case_198(self):
        self.assertEqual(pattern_match('yV11O2(r\x0c1D,GiYz4\nJ|g\x08\'|:pqFZN5jYAPnJ# zgb"vZ5mQZptV', '5mQZp'), [45])
    def test_case_199(self):
        self.assertEqual(pattern_match("{7$Nz0QH%(/8-|v.q{hYE.Be@r`,`'<p^eA%2AOU7e\t{^\x08l}/7L>zSg", '\t{^'), [42])
    def test_case_200(self):
        self.assertEqual(pattern_match('8E&dOGDX9>SbUsURA`a]{=C$Y&.Xf_)o9YV]})OFEfatK:*;\x0bY.c&{&d\x0c/n .xE/(\'I2AP.}FN}f^#W9-=uyy"J', 'A`a]{='), [16])
    def test_case_201(self):
        self.assertEqual(pattern_match("Znx]fA26\x0cJe\tV~\\0/)Y$}*.\x0bGNyCYB5']wg*\n162Gec25Q\\dJ{poPi/3", '.\x0bG'), [22])
    def test_case_202(self):
        self.assertEqual(pattern_match('@\x08(n78zKj>5E[uXz}R+qoXRLo4x8CA7\tU/eiK4~gnWd%|,;sbp}HBtd:B"W@p', 'nWd'), [40])
    def test_case_203(self):
        self.assertEqual(pattern_match('#X~ol/t942\x08Chef4s7O)K\rLc<52P<7s-EK4zo9KcnfclGxqGz\x08l0TIu$|#NM8u}NhRj:8~.&ShmXBnXK\t6T', 'f4s7'), [14])
    def test_case_204(self):
        self.assertEqual(pattern_match('/\t\nxJiO+l2Q\\O3nI1U0y,mU7y\x0cdJp ?7=1Z<C\x08\\Wb!}+![\nL-\n%OX', 'iO+l2'), [5])
    def test_case_205(self):
        self.assertEqual(pattern_match('ixyR);\\Rjqv.i:z`-{p16.i@>P A%_f)t~zhWvSo;Y1pKi:o\x0bYY\x08[{;G&|~h^Htzq\nH?Jk\\BVa/T<D&#H\\^tqw|NF\\hUSFzXJ_xI', '@>P'), [23])
    def test_case_206(self):
        self.assertEqual(pattern_match("6asu H,7q1& P\t>/0y2vvl1P{>0Ymbo;('&=>$AoGK\x0bUF4}*MFnUw(?_Dndf;AP<eH", 'w(?_D'), [52])
    def test_case_207(self):
        self.assertEqual(pattern_match('Z$oNFO^z{?P:A0\x08p+uWC7.+9n+ly.n:l\x0c4n6LI\x08:q-J1W\tij`l9lLnE{724+q&wiX', '.n:l\x0c4'), [28])
    def test_case_208(self):
        self.assertEqual(pattern_match('qw\\YRQ..hcA+.2&\x0c6Se\')2"l`oqNbVOw-Eg<xf/Im)D4j#0ap:A\x08$gjff!J}L\t[mgZZL~+(', '0ap:A\x08'), [46])
    def test_case_209(self):
        self.assertEqual(pattern_match('\x08ElO\x08#r75$D\\:#TphF3u}]R+ >filhn.S96IH)9Djrrx1{x0]+^!NgmCTj.A\n%).t"-H7?+\' $ZD\rEWR_M^G\'rA=6,V_#\\As\x0ce&', '\n%)'), [60])
    def test_case_210(self):
        self.assertEqual(pattern_match('mGTV2\rR[E\x0b\ts_Sv.N7]%&G;zkdi*mLK3IO0C@f\rZT/Is"2OivyR=sgS|J6(\'A42/rEz=u\'k-5S0W;8,DU5i.oxR^BE{)83)sNf[', 'OivyR='), [46])
    def test_case_211(self):
        self.assertEqual(pattern_match("4)}`h;C?\x08/ \x0bF2yPc\\[.](KP6\rgMGlMMbgPTIQERQ4FGywb'\x0bK~OcM\t\\=Zn(m*Q", 'ERQ'), [38])
    def test_case_212(self):
        self.assertEqual(pattern_match('D\\xt};:O$=e^K%P?%FeFT d1bU\x0bm0Vmf9kYGqj`*#|=>\x08XDpn&7acqn\rWL\x08k-vc\\x3TOq]n', 'pn&'), [47])
    def test_case_213(self):
        self.assertEqual(pattern_match('m;7fykLM_o"O@DH4gkr\tUUD{\tI|Bt\x0cxo\\c9EgzgR%T5p/]\x0c8!{&G$Dy8~ */\x0ceMIi1W><WEJ[oNhWb', 'xo\\c'), [30])
    def test_case_214(self):
        self.assertEqual(pattern_match('QtUP<V".2V)mZ\r\x0cQLjOH\nD<A4Skb}bVytpYm(#{=\'\\S"eZi?iwJk^ b*:KW8"2*+8l\x0cX\x0cKe,v\r:wjd>q\x08^', 'A4Skb}'), [23])
    def test_case_215(self):
        self.assertEqual(pattern_match('I9|}).M\nR&l\nV7<"8k\x08\x0cx0t<w98j^uz56@ba25?Y@4\x0cYW0t,H8\r&?Q\x0c\\z`{H)D\x08\ruG\x08\t]=$@X9#y]&:3.^tu0x.$\x0bX EDMz>k', 'uz5'), [29])
    def test_case_216(self):
        self.assertEqual(pattern_match('t\\8]r:S5]KTz[1(-is\\y&k"_v#,.\\XxH4?dO]Rx%O:ED%bt\r5&`I:Lz==\t\x08m;u&D32F\r3 qvbf^', 'O]Rx%'), [35])
    def test_case_217(self):
        self.assertEqual(pattern_match('$\\wB^`mjC,C%\\x}oH,:>\'gMB<e<8oG1tK&%A|T/(\npU3k0\'IY=iAWKaA}Vj`6:/DH<wZX*nE\ni(OMTNn&"Mz', 'C,C%\\'), [8])
    def test_case_218(self):
        self.assertEqual(pattern_match('`\n#l(*w"q=7 Ep(hIms?p`!wP=LU#2\'|I^4\x08+Gu\'Y\nw5S }\'kwz. MM5[O}qQ2HQiW6nq2_6:1tv%\x08^n<V8ie&gsC@=qbvgS', '1tv%\x08^'), [73])
    def test_case_219(self):
        self.assertEqual(pattern_match('muoHuV\nQ7k< 6%j>Grj-r~\x0csH"O%&u`?yC^$3jgP"\x0c*<WE[2[M!J;hQq&gu3ea?{]Av@f&b}[Df.^\x08\r#a{QNE"', '\x0csH"'), [22])
    def test_case_220(self):
        self.assertEqual(pattern_match("8oWzwbg:H:>Pm\ttKy45Yd<ZZh83\t{.\x0bw'Jjm3`WT\x08/Zw5G1mUreNDE$n+kT8zRfnwi8~o", 'g:H:'), [6])
    def test_case_221(self):
        self.assertEqual(pattern_match('@h"B?|4PRe?R&v\n/~)[fSr% }Y[|cV*-F~G?j#I&jnm+LZEL{WxUGb`VSt', ')[fS'), [17])
    def test_case_222(self):
        self.assertEqual(pattern_match('~_v`^TLi<{]\nx}nDKm6iz0ZAG,\x0c8}\\U:#\x083nSOr|WA W86?d=K~.\rg2x\'7+~Mlk>+l\n]a"vfpw7', 'nDKm'), [14])
    def test_case_223(self):
        self.assertEqual(pattern_match("G}#8j%-p\ni}'WIiI5!KwF,x e;-@Xf-eb',*g\n-aw_Y88m0(n(", '#8j%-p'), [2])
    def test_case_224(self):
        self.assertEqual(pattern_match('m1<9\x0b\rDJ*1#f%sv23#2.e,=T0>,pSk\x0c. WWd3n[BO*eV$\tUmbq$iT<r"#_2yCAC#4]M)^yVc\x08_+jN@=&Q', 'Wd3n[B'), [34])
    def test_case_225(self):
        self.assertEqual(pattern_match('VXt3yV:@gh\')JZ3]0m3K\t0&)_"@*l\n>T2k {M0q_$(\t0Is4[<EQ', '(\t0I'), [41])
    def test_case_226(self):
        self.assertEqual(pattern_match('?)9\')|]R29|OYv|S]E3$G"E*)8bIr\n-(pSFN=Y$JeGpv${,w#{`73y:KE~O', '$JeG'), [38])
    def test_case_227(self):
        self.assertEqual(pattern_match("?NGd_AyST1}*_8GJxUeHtv*F>&'L>QBDFuJg7CFRdV\x080Sa:*,>&7h@z", '8GJ'), [13])
    def test_case_228(self):
        self.assertEqual(pattern_match('=?^8Hl-d"LDf :+-,1;aF\x0b6T1\t!-?VG\\{.4rl{{Zt>X7FLA2x96kKf\t\'g`_\ni}]6-wMjgw/t&F(3k*,\x08 \n6uqS=_kIF', 'Zt>X7'), [39])
    def test_case_229(self):
        self.assertEqual(pattern_match("B6'?Oc0HXH{(H00g\x08wNp/q8t%}5a4{0+s.V[\x0bgR AsGI?Af0\noID_&CU|#|KfV$`b{MAc,43R\ty", "B6'?O"), [0])
    def test_case_230(self):
        self.assertEqual(pattern_match('/Xs}2m!xZOR"xhb\'y7%4Y!Ao,~!6KZ%ANoG}t*wUAo8,v/vkih*\\bs\x0c=j*p%Cu(^{c6jNi&', '!xZOR'), [6])
    def test_case_231(self):
        self.assertEqual(pattern_match('Bp3HOhrY=zeWB\\c\x0cDVP,Kx0[6WU<"-\n)l}MjkyrWoE"vB\rEP#os2"TI@r~x"6xCQ,:S]>*lA\te(<fVvSNX!@KM\x0bl', '2"T'), [51])
    def test_case_232(self):
        self.assertEqual(pattern_match('2\':p"X3,o2\x0c~6ZAT.X,!~d!\\&Fjdm6+)/+XD(@)W"01@g\x08/P4>HG#LvAgii<|qD\\', 'p"X'), [3])
    def test_case_233(self):
        self.assertEqual(pattern_match('1NW\n*p~B"{}xZNe 4`#}M?x\n$}`\rM48C7R\x0bb/yn*uqMGlHUZ*?<\'O;T%}FL|#Gfy)5|J@5\\:\x0cBa\n4y7"!D', 'uqMGlH'), [40])
    def test_case_234(self):
        self.assertEqual(pattern_match('s!`EP}6 #G!]%X|CM<8"!1b%0-"5MaC&\x0b.m\'1\';*TV//AZH1O4PH0[\rm', 'M<8'), [16])
    def test_case_235(self):
        self.assertEqual(pattern_match('pw/cS=2OBpj>CNw4uB\x0b\tZ8\n}m;&gNI$cX|S%->p;yvlLB>mybX!C', ';&gNI$'), [25])
    def test_case_236(self):
        self.assertEqual(pattern_match('LQ]B0e8F Y\x08rMDU>A%0#1t0"J\\cj"cW"E\tUPu(\tBwKTb3UpIUa$hFJ4e4TTgw-mn$j!"SCHr,IQ<_UTx+34,WT;v-D ', '%0#1t0'), [17])
    def test_case_237(self):
        self.assertEqual(pattern_match('2:$;\x0bBucM[L\tu4Gfo}E\x0c2bm(pQ(GB<T0Jp4M\x0bmpg\x0bB-Ua\x0bLP w;NFO~&n', 'NFO~'), [51])
    def test_case_238(self):
        self.assertEqual(pattern_match('/!8]`I$"6A~`h_Mlo4,OfI^mOre0\x0c`0,WAZ]\\?\\kfOh ;VM!7].{rV|;>3Pj{c\tmY\x0cMB""}<9?#8x~8\'ze2O+Z\x0cW', 'lo4'), [15])
    def test_case_239(self):
        self.assertEqual(pattern_match('eD*+QM423*rwiJ{nG[2!\x0bzV&\x0c1rD-q;MqPA[AA VT}s=3 ZAmcK]. r %)DQO x*e YqWc`Qg6Pz{PR]6kF>', ' VT}s='), [38])
    def test_case_240(self):
        self.assertEqual(pattern_match('PK4\x0c\x0cSn@h@kQyt=_8Y]*p2S}si3zOjT\t"/>JcGsXspj4*#k\'jcE\x0cID`e895lc[l3t}k7sB<\'r\x0b\x0bM\r!\x0cbX8', "sB<'r\x0b"), [68])
    def test_case_241(self):
        self.assertEqual(pattern_match('oj{yu%c\nH\rdhi\t\rXJ{F~\\M.%G7iT#D)))z5\x0bN.\\3J{Rq$q:M_]vH@Ohs^[w~>JMq', '{F~\\M.'), [17])
    def test_case_242(self):
        self.assertEqual(pattern_match("DNlmy.-:MYRXvo +51F6_\tH,|HS_\\$ X*hx>>Vg-ykpNr~a-P1&K\\x*[`\tOiJ#[t3&{Uvu\teNdvV.jqXBB$P%v$Nv'<bn*!Q4vh\x0b", 'YRX'), [9])
    def test_case_243(self):
        self.assertEqual(pattern_match('g:G:N~v+?bB#B,RK=?3^kA$)Q4*By0Uy=6QLt`F}\nlaG:4~2sKu', '3^kA'), [18])
    def test_case_244(self):
        self.assertEqual(pattern_match('IN\n:lEtE_I.w"Z\x08D`?L#"iRRo;M#B-^\x0c6b1<u?Rf=X%7;@:/bsotE\x0bSFCtl:\x08n:J#\x0b"trb6py\x0cls\\t8IX|Qq-&>" RzRI-Y<iZ', '7;@:/'), [43])
    def test_case_245(self):
        self.assertEqual(pattern_match('6{2xrsf_faJMd,v|yg"DxNri-9_H 8G;.Zz1xL\'2ZYqo&\x0cGk\x087J(6=Rk"$#?\tZOsWdZT', '(6=R'), [51])
    def test_case_246(self):
        self.assertEqual(pattern_match('qko^UU;Bb|U^od3f|\x0ctqaMo\'klVfkIil\to^960\x0cpr3:oYMi=SG$"|aj`S]\'\'PXi', 'kIi'), [28])
    def test_case_247(self):
        self.assertEqual(pattern_match("?&VrJUG/}+\tC71\x0cI28^#w~)f{snPNsk\t_`xzs^C*E9'v_a*PnD!3Y8e6<", 'f{snP'), [23])
    def test_case_248(self):
        self.assertEqual(pattern_match('`K`I)\tJV+#ab\\4]<zn^m>{\nwDyxv=5F3gf[Rn?m/vD5Y*8Zv-KR_h@uT~A\x0b)G0:;#{50TwJ$9_', 'vD5'), [40])
    def test_case_249(self):
        self.assertEqual(pattern_match('>tC\x08YdU\t5%\'gV:}uYu\x08(<1r\x0c#4s\r4(63g2vXKTNy;ly=T [Nw<V,5C~\'\x08<"\x0b$tJ(6MF\x0c?\x0b#.{qwg\tTER|cIJ J6L0K-G', "~'\x08"), [54])
    def test_case_250(self):
        self.assertEqual(pattern_match('kTo<e1*A[G5xKo`q:uhrdCJ.Nkc_$>[fg}h`6sfuc>Mu\n4GukU\x0b.p803mcy,3Z]/u?KxTdb2xeqIrs3st2x}hC}hk8%', 'uc>Mu\n'), [39])
    def test_case_251(self):
        self.assertEqual(pattern_match('Lg>{#[t38-0b\r/:@XPW@w\x08j\ng}lmue]\x0b,2\tBuKJwPU-ThfEI"xv\x0c}}OUsOc.Lc\x0ct $7ZUL}C`-m=f?2io\rWs\\"SJmc<%', 'EI"x'), [46])
    def test_case_252(self):
        self.assertEqual(pattern_match('\ns\\&OrA$&Ccj}vsmy}Kd-3"vvr\nZZ#\'h4#.LothM`m-A\'!ce!P|5-;q:G60\x08 sXLz r', 'P|5-'), [49])
    def test_case_253(self):
        self.assertEqual(pattern_match("11.b<by)~48\x080(lbJfd$'#=ylQ~N?TaK,}Lw_9ex(uuDHU-#\x0coe$PYP@@a<\rZ[)<r", '\x080(l'), [11])
    def test_case_254(self):
        self.assertEqual(pattern_match('^iM#n>`?K\x08/\x08=\x0bf"+z)\tYt5ZMP\x0b5x\x0c\r\nbvx\x0bu*rt|"8wP2)ku\x0bs\\;n"Rnj?H-3Myfi0KFQf^\\\rms:w\x081NLJN', 'Rnj?'), [55])
    def test_case_255(self):
        self.assertEqual(pattern_match('/DG)FJLIuG%lU;+rG%ra/`&{c`iW"*uu\rb? .*=B`DHb%`ZD%f-9"Lq".<1mT1&d\x0c4dhP"bhUdj(/^[bLf"\x0c+8D\\\x08}zTMY\x0c_@', 'dj(/^['), [73])
    def test_case_256(self):
        self.assertEqual(pattern_match('t+9n@zj,\x0c?F\rooHADg\nQeoG*Nf6MEn0#m.:=R5:_jStLH%4U@=^\t9])<1\\9h$xwmqwbLP"#UcLVo>LurKa5U=><886', '1\\9h$x'), [56])
    def test_case_257(self):
        self.assertEqual(pattern_match('0\x0cudFzVgk!@.\rlPzJ$khkA\x08hC@B~S6k\\"w>,\n`y+@@6#B=QwW45Ti7L(k[Lz:-3\nl9\ntk{H-KwK2BE\x08!S7T]z\x0bnYZi%v!', 'k[Lz'), [56])
    def test_case_258(self):
        self.assertEqual(pattern_match('rT&RnjmH:::2Jvo!R~5oWZz*g+Z6io~Rmb#[XS&y..is=:E\rlWdk6fT`O_TcXmE6\tr', 'b#[XS&'), [33])
    def test_case_259(self):
        self.assertEqual(pattern_match("!&/P[6\\v)6!Ttg`@bk~S1NIjDiQkmnj>`3d2P?dqHE.I(%!qy\x08nOw`C%8X'&e&bH_Ku{)qH", 'nj>'), [29])
    def test_case_260(self):
        self.assertEqual(pattern_match(' ;4jha\'W|0x/iY\n.\x0b`d~`:ObevOo,(nDV33dUD=<58C4.2~PTolC+!0<bBm>k7796|h,W#,Cy_\tU<"?%|CdWf<OIq\r}!3\x08lg\\', 'Bm>k77'), [57])
    def test_case_261(self):
        self.assertEqual(pattern_match('NMYwi*9VMUrZb\'s`\rw>)_~8rI~kD8m.~paNOsPeM#Q6eY~+lXjeBC-Q0M"~EVDR$oY22BRI`~', '8rI~'), [22])
    def test_case_262(self):
        self.assertEqual(pattern_match('-\x08z1@twXjm15_\rdVd2h\x08q%XTG/dfC4g>IgJf@bNRL*m!\x08Y\x0czd~XnRfuqGnglfvyJXo\x0bRrhh{fQ\x0bC\x0bxRHH~Rmv./', 'd2h\x08'), [16])
    def test_case_263(self):
        self.assertEqual(pattern_match('teRCs$PcU/s`L&.7^\\\rx"?_nBLOX\x08v\'\tB\\`ARaw):Hb?-q9**j>p!pcRPxZU,h77\x0br{', 'L&.'), [12])
    def test_case_264(self):
        self.assertEqual(pattern_match('-heMIfhTMI7;y]92 \x085*&Axh}VpK:\\AzdQJU`b_<y9E/D=HUF\x0b\t#!l"=Ci', 'VpK'), [25])
    def test_case_265(self):
        self.assertEqual(pattern_match(',\rgcpc}/%@NTYBLS\rqlrv6Wg[T9TVZMq\'L"!R>Fx\x08/)>gK6h/\x0b]$Xt~i\x08ef)B<NBTVL\x0b?\x08V\x0c8ec/ d3=+\x0cA7<y{, \rW;}=eyv', ',\rgcpc'), [0])
    def test_case_266(self):
        self.assertEqual(pattern_match('MSP(iJTVFnP2^glpZZUZ!Hiy8~OCo\x0cucM7g`i}pi[C\\IklowsBQ;&f.2~(', 'UZ!H'), [18])
    def test_case_267(self):
        self.assertEqual(pattern_match('bZX?#\t[tlc}mkAwPYY*-Hb3``k`8\n/\x08wK\x08ED`pHdp6\\pK EnUSar`', 'bZX?#'), [0])
    def test_case_268(self):
        self.assertEqual(pattern_match('0\n"^W: q]"I}="2gi\'q_*7cY8/Gm@0,IfbMch\x08@i3Qbp;00=#\\$dyP)\x0buS1', '\\$d'), [49])
    def test_case_269(self):
        self.assertEqual(pattern_match('eCKU*emA\t\'{F$f@C*PT\tP2K\x0cX\nVeG3v/_*<7}E6,P[Sp$?SkT"X8\x0bF~-)e|1"8TJ8>v\\[E', '\nVeG3v'), [25])
    def test_case_270(self):
        self.assertEqual(pattern_match('x~;D\'=>SDaV7V9\x0b)-;=lF]!mx;\x0c9NA69;;bkQMpJ}JG*~&40A"^\t1x28;yG\x0c?<{euld4t+]0*Ff<c.$[-FPavC8~{', 'A69;'), [29])
    def test_case_271(self):
        self.assertEqual(pattern_match('e{0.s\nxm4wW*N=W,7j"CUVu_06he~M1`\x0c<\x0b8e"OTryAAJ:MX1uUIfRUPj2*D=&R^$,Q::G', 'wW*N=W'), [9])
    def test_case_272(self):
        self.assertEqual(pattern_match('$Ob_$\\HHoc7pp73\\M7l"UrgPMs]GTNF|a\nH&iIuQ\'^:qu7\x0bD\x0b=U+\x08\x08xtKr]@G1)#hlfA{-/&\r?m"j@sFO_&FzMRV6', 'M7l"Ur'), [16])
    def test_case_273(self):
        self.assertEqual(pattern_match('V@`SJfAmN_Mdvkg8C:pj.Fk;&\x0b|YxP}.~de$}y02v\tpI.-`cEajx]Q+T=O.Yv,UEIE%\\-pl0+R*Ar-^(7uCNW', 'IE%\\-'), [64])
    def test_case_274(self):
        self.assertEqual(pattern_match('bK\n2azD$\n1`3_-LU\r!Jsm\todRc|-J|Czd\x08~EgG>wVJ$Lk&LUT9|\r?%mNK%3g([C@G~8#tyy^a`8WKq*', 'Lk&LU'), [43])
    def test_case_275(self):
        self.assertEqual(pattern_match('{JxFlr~`dpSfr_:\'bKB\rFJGYK"=*@d@~d^ivlx\x0c\nl2iW,YAJX/-WzpL', '@d@~d'), [28])
    def test_case_276(self):
        self.assertEqual(pattern_match("LAYm)9_cn\x08J^\x0ct[4DuP:tkJqcU]VIB{sWP`]0Ss@'L5\x0c+Ig$Sliyd0Pv}d`:#<Zb(?dLp~~},Z:5h-72?\x08YQz.os;pO=;\x0cZ", '4DuP:'), [15])
    def test_case_277(self):
        self.assertEqual(pattern_match('V2pX$k|a\x0b\n=E$VVr7ZI2)(3k3KW<b0J=#\'}w9@]}w?\rd?%H7F;T|%HY.="C}D|QAHrm', 'V2p'), [0])
    def test_case_278(self):
        self.assertEqual(pattern_match("\r?][U'#~(a}BqI?tkIyH$|ygZjkOgD:ni+-]tm7q,?ayl\\u#<|M  mNs\x08^=+(Uf*'O", '#~('), [6])
    def test_case_279(self):
        self.assertEqual(pattern_match(';5*r\\H!;V\x0cB>}WCtz|[{M^&kOMB\x0b 3x4Hrj#m`{^nJ$Rbp#~F![={D}H,&^jE|oVmnYCnGE79LSO_W{xq)\nLb8a\x08\n', '!;V'), [6])
    def test_case_280(self):
        self.assertEqual(pattern_match(',uq9aD]"G]gis><U\n(lSKinz(\'+\nrnW4UiN8gVM?CBG\'Aj<,cl\t=Y%_-dxjq01tjk(Xy\x0bvzONG', '\nrnW4U'), [27])
    def test_case_281(self):
        self.assertEqual(pattern_match('PA9{iYq]|qPf(.9*[Md5VMjWKsj_!s>5\x0bO%?n8<ND~F7fiZ8BDpUrsB"#$@_2s', 'iZ8B'), [45])
    def test_case_282(self):
        self.assertEqual(pattern_match('h=j~N/zIp q\te3GzMebNOd~6 /<#uQ5 vwt!Er*|8EW{s7.={[)-)3p)0{+$lSB!@+?}hOC">>u<', ' /<#u'), [24])
    def test_case_283(self):
        self.assertEqual(pattern_match('X+"db.i$]%!(X,i?C2VaZxCr+9#FH%,_0s@dg\\Hx\x0cMTFy7<\\5CNJ%x7km-ha}>P\x0cc.H\np%yh{H1u#Hs8c', '0s@dg'), [32])
    def test_case_284(self):
        self.assertEqual(pattern_match('6N(z!K>\n+u`F|2k_\r[qK\\19<zCQK{j)JW}ox?nYT./GD@Kgj}I>4yf:l\rs(nY', '!K>\n+'), [4])
    def test_case_285(self):
        self.assertEqual(pattern_match(".'WkKvE(c][Uu\\;OvaFb&NoF.KGxM3m\x0cy_KZ44NKp[?Oe#=>k`:\nFkC/cX<=8Phexj/|V72\\[Tz1+", '3m\x0c'), [29])
    def test_case_286(self):
        self.assertEqual(pattern_match('Rp\tsR\t-Y.2.KM"E/oWt]\x08]")jq^YR(eLCmUC&wK#p`C\x08UvLW6Yy>};F', '.2.KM"'), [8])
    def test_case_287(self):
        self.assertEqual(pattern_match('|hh8>\n^1\'T&UU9L2:71K\x0c.\\1 \x0c5T\njfO&Y@o~W|_mxqoDji"UO9%J 3S[bRhiyiR>G;)spz84Jrr0xl1$()?\x0c|)=', '@o~W|'), [34])
    def test_case_288(self):
        self.assertEqual(pattern_match("ZNE!9`XU7-kC5p8Xx]Tnq<N~Orp?\t^}p'U &#`OqXOfw@-E~#'v6m6'}}{\r`C,X&BYV2|%i,", 'p8X'), [13])
    def test_case_289(self):
        self.assertEqual(pattern_match('QVsU5@0yKwcBmJObN]u?v&!T2?=UA*5G#A8\tv\tD2%<\r9/fzUDEtYG|mFusw\x0byYmu', '*5G#'), [29])
    def test_case_290(self):
        self.assertEqual(pattern_match('&S%R-$9o\\vXU|yifz__`64uq+t9cH:iOetyy:8|M_)pz1[T.>cswT8>{\x0cJfh&apZ,*a:gL?Q[k4r5uE$j/h"a[eO+E=(Nip\x0cC[\x086', 'uq+t9'), [22])
    def test_case_291(self):
        self.assertEqual(pattern_match('R|E00=dF[y5/X+71??\x0cJI8wK\rc\rd^\x0bv`E@h\\rQiiti&\x0cSAxwH#LM2hHsL\t,', '+71'), [13])
    def test_case_292(self):
        self.assertEqual(pattern_match('|fl2Z6f"ySv&?\x0cb0Q=Ongh)hG,Z/IO7\';>/xkr24aCRD]~eo\tjcNpoQ?z`WH\x0cv;_q1v[[ ', 'Q=Ong'), [16])
    def test_case_293(self):
        self.assertEqual(pattern_match("fX=22A\t?n\x08o\x08z,ZZ'qLhQC+Y \x0bjCE1EZr}=?8-'{*\x0b\x08 8Uvo{&lu,ew3*]}w3!AMv`Aid!Pi+opW;:q1\x08nbrtJfr4XM#)u~j0JH", ' \x0bjC'), [24])
    def test_case_294(self):
        self.assertEqual(pattern_match('Y\tAB&4,0R[^?gl&d4yE+jkOyXQ<\x0bxw+d\nX%ZX\\$DX]Y}uc_tQSu~0\x0bP<G3|m&E6_\\]{IWMw#&U0\nr{DZ', 'E6_\\]{'), [61])
    def test_case_295(self):
        self.assertEqual(pattern_match("Eqh?.$(QSEk(%4y/D2W$1@\t9Aqn/l\\,dV&o\x08,c\x0cgcG]bx{,&H28n+-\\2;[zt_#9_E<7z`stX'?AKD_", 'o\x08,c'), [34])
    def test_case_296(self):
        self.assertEqual(pattern_match(']FUzFVuB? RaK&/h -35ot(wZV;Nk\'|@72MbK/zTht+g^y\x0bSe[KpuIYc\tmWFn)NVyuZl-4+\t*J&\rr+J?S"Xq$g', 'g^y\x0bS'), [43])
    def test_case_297(self):
        self.assertEqual(pattern_match('\x08(ci\rWb&In2v ;v6z%c^`%r,\\NIBv2{nmv?rB`2Fr`,&!^f#Bi', 'mv?rB`'), [32])
    def test_case_298(self):
        self.assertEqual(pattern_match('od\n9`s&VhW*ljHgPOI9R:7\x0c^!A^YSugo-+m_24*Ge.sf8;-XnKz\\3L\t$LCsF[K8]PR\\dt.$VnA(k', 'o-+'), [31])
    def test_case_299(self):
        self.assertEqual(pattern_match("fr8=\nn*mM{<p\x0cWKCgQWtaN-4''p{:\x08<UltF1t2M'%5Wr7y+}%f,IFB*n&<Vz!%jAIa\rXZq;&|:2>Yza@KQA1r", '7y+}%'), [44])
    def test_case_300(self):
        self.assertEqual(pattern_match('XLgIX{HMwQ-+BzrN\'gmJ;X_V^f-<*49(*jvJ2:lq@~D@R,#"[#M.u4tv4wZ?kNe|\x08Gj_]4', 'u4t'), [52])
    def test_case_301(self):
        self.assertEqual(pattern_match("wZ{[\t.L@/2H?l{=4'y@aCpb(<hS)MX[^/X=BM<b\r/2D&mFt9$4h\r>x\x0by`@l56$'@,`I", "=4'y"), [14])
    def test_case_302(self):
        self.assertEqual(pattern_match('#F7JJC/S8n""[72H~ty\\\'W]quc!RFQJTeNI-s&"r?ErC{I_?7&@Z}o{\x0b9GPq4m-9/0|MyKax~_u2J34Z', "\\'W"), [19])
    def test_case_303(self):
        self.assertEqual(pattern_match('[.wzC,.26Tf Ox/%Ab9su)5R/hRsZ*#wW9`]?[h1 Cq)\t.V!M:2f"]IDZr"K,} Q)LIufO)>xW~-&;Z:t4t8e[RP }Z-]', '-&;Z:t'), [75])
    def test_case_304(self):
        self.assertEqual(pattern_match('q+JW~jG+\'-q3u47>^H3~#&3\rc4\x08|=n<d/P(<U#|$rBv^>FavY_<jdBq2qb\n3{2r=Jmz\n:(T~\n"M\rJjOd W', '(<U'), [34])
    def test_case_305(self):
        self.assertEqual(pattern_match('kcUBFh|6I0"V%%\rRe:lQ5myDh2MY{a)f\x08/"Ov ,v>c[OMLH6U3R}R:/>/KUaVxOO:+[`}da`-5\'~O458\\,YG', 'v>c['), [39])
    def test_case_306(self):
        self.assertEqual(pattern_match('St2SD4cF{sh~m&G_Xct\n0%W)hP))U9x |b;0ZYg"R]fN1S93TL8z.W0xine>|{\r\\VE$9o6c&myK+Ww%!\\Nfmx\\O', 'h~m&G_'), [10])
    def test_case_307(self):
        self.assertEqual(pattern_match('[,*~Z+l<3Uzi1Tq$#02FlfeOvDSP<-BkI]Z|kWPFb{U.\x0ce\r4O)Q\rA6`t.,Ejz"25o%@R\x0bvjq.', 'zi1Tq'), [10])
    def test_case_308(self):
        self.assertEqual(pattern_match("u\x0bCDb/=gs{-T+;bXq\rp^MEL\\;bs9{&\tIn9^;V3A\tDMKSzoq%9\\WdxkiQ #8[2=g![bc,z\x0b:@CY\x0c'bG=by\\", '\x0bCDb/='), [1])
    def test_case_309(self):
        self.assertEqual(pattern_match('x.duq\x0bIN,N~3Y;,JnNFD]"\x0cjl1mX@~}:\x0bMSYVfO;_b(K*%& @]9kL*m}z\x08KO\x0c+D[b8%!`\x08!BWl5%4TT"i**p\'G6', '3Y;,J'), [11])
    def test_case_310(self):
        self.assertEqual(pattern_match('bB3\x08:*\rl\\;@zcYVb\x0b.2M@wd{k\n\t8yL]02%m5\\QRKKKHx\r+5M\x0c\tt9[\x08J\tp&tB!Tw)WS,*A{N4p7W5\x0b[\rd', 'S,*A{N'), [65])
    def test_case_311(self):
        self.assertEqual(pattern_match('[Dbgs[VZvPCzsF/)|(%9hAAr2)Lr\n|_\'3|)W" >aVE489xYT9YY\tvZ@S35;H_ql"X~3SXYonZ($M\tsDw=2/}r^/QJ4U~.)d%\x08}', '3SXYon'), [66])
    def test_case_312(self):
        self.assertEqual(pattern_match('\x08.=?8 %syt3/\\\rl^Yi$8*+&I!70)}\\fu\\f&3una<}jO\\aOXiR%(tk3g4V*78zbN(Z%q\x08}7n] ~/u.b3\trHN%Taw\x08\n6zcK', '70)'), [25])
    def test_case_313(self):
        self.assertEqual(pattern_match('m&dRt\x0bh8i:X,\x0c)kw188J%T[DxrFWoA=dOU<?a+@#~}EF`3|aF>58g/}ZD)OB%6*H', 'T[DxrF'), [21])
    def test_case_314(self):
        self.assertEqual(pattern_match('EzN9e&7KkR-|a>jAhM\x0ca!\x0c4L1>/U6+a=\r:)P*0|Z$dbK,7U\tYdhTM~UeKW\n7JTi;[<4\x0b5`+S(Zq(cmZX7>T \x0cirmN', '>jAh'), [13])
    def test_case_315(self):
        self.assertEqual(pattern_match('G8?Adl9e_(\\\n9,D%!Ag^B#_:"HOwUE:~5!k6\x0b5God-m\\\rLQsa^%(;>*WvUM', '\\\n9,D'), [10])
    def test_case_316(self):
        self.assertEqual(pattern_match("hG\x08e$uCNw0y4vH%vfpgk'3LrC8eACjWtT+:nw\n*JBde>|r\x0b#/(f\\H*Bn>@ek|H](\x08hOS=p)\n]\x0cL!'oY,k f'", 'w0y4'), [8])
    def test_case_317(self):
        self.assertEqual(pattern_match("ow2WtY<_Fe=tf'ukUBvXp}BSC\t#.1E9I?H?c-qUOM\x08R-hs\x0b/:L5rr~F\x0b`l`mK@!=!<N=H)Nd'l7K^Z%'$\\*^h-M", 'l7K^'), [73])
    def test_case_318(self):
        self.assertEqual(pattern_match(')[SP!\x0blHn2YQ Q3Fbn8(e"yA2]K+%#w=k=&0Rq\rX"xg.\t .)n]b3%k329q#3W9l:uEQ}\x08T>5mbPAmXp.L#"=e%<\x081rG;-K', ')[SP!'), [0])
    def test_case_319(self):
        self.assertEqual(pattern_match('"w:B\'] (l$w)&QK>[mC<,8vMS05De\x0c5wwN9pU6\\wX|[\rh@"{hD)52\nYrh6\x0cw+rK9eZ5\x0cF\\D:B9rH\x0cx', ')&Q'), [11])
    def test_case_320(self):
        self.assertEqual(pattern_match("^V6Q]NE00hVt#]sKF*&'9f2}>EA}Q'\x08\\5uFm\rbWj\tv=|E>uwb)*M\nzwu3>a xrRiwISh0=a\n", '\\5u'), [31])
    def test_case_321(self):
        self.assertEqual(pattern_match("?l\x08[z'6I.&eKQpODT?n|jFxWZj6\ts-:\x0c4&b$#c\t;M#)g.i/AO&|\\kj}\n|-&MK\x0bjU:pHa)'6~V|2dX\te\\s7b\t2,t4Fk=DZiKT]D[", ')g.i/'), [42])
    def test_case_322(self):
        self.assertEqual(pattern_match('twAV(\tVAV4}~\t>xq<67HLuwdL\r0Wd@iV\nRX?7Be.>oZC^lMQqZ\x08B\x0b:z/#P%?UA', 'QqZ'), [47])
    def test_case_323(self):
        self.assertEqual(pattern_match("Jl%pfd1AGXNTJ+[%8v'1KgJCk/mwr\x0b W+J!KP]Il{dJf2I_rJV71\rQc[", 'pfd'), [3])
    def test_case_324(self):
        self.assertEqual(pattern_match('BS*@im?9GoQqed=g\x087Md]QN{*bwzRJ+5sPgJR*hkzfjWiIB|q4!Hw%2\x08*V]qaeK `Y#l\'ZGCC":N\x0c #Q=tF', ']QN{*b'), [20])
    def test_case_325(self):
        self.assertEqual(pattern_match("Lpy7-9T42I@T^+\x08u8EM_f{z%bB\nC4CocU.~q&Jr\x0b7>JpmPc<9>\x0c='<FU-FinmWc9_MEP+,}", 'bB\nC4'), [24])
    def test_case_326(self):
        self.assertEqual(pattern_match('kb!^j=Et[63%Hqk6.S\x0bdm7VuER&NUywCT*(~SY+@>!\nb?;PAaVTE\x0bj_a7*$0Klz]jB%7S#W', ']jB%'), [63])
    def test_case_327(self):
        self.assertEqual(pattern_match('-Xw|jFazaR-]3x\n9_e"jY+:gyT\x08(0.^%-Bl\x0bkCfRo{M&Pop\x0cW:kcAMIehR[~d<:531evkYPzIl&Ie5G', 'l\x0bkCf'), [34])
    def test_case_328(self):
        self.assertEqual(pattern_match('=`Tp[ <i9V.nA l%ZM=>T,\\9\\V~=$w+J\x08M$<ekcw9Q,~"]\x0bF%xH{G*a-1+\r\t{d,1$s\'*w\nww/-\'7@q\n)p', '[ <i9V'), [4])
    def test_case_329(self):
        self.assertEqual(pattern_match('d\t.1/ugl*2\x0b*IDao8=^iD*nxlq|q*]F&B";7\'qul{qQ:qy)ouS<{+VZA,gK6 kT_}VG s#58G\x08TQ\r/', '2\x0b*'), [9])
    def test_case_330(self):
        self.assertEqual(pattern_match("N'pv`[F M'I,'4c?@r;v*,>\x0bq(O}9 }=[,\\jSP$2273[lXr+[5(x*'8Hn%`:dh8m\tt|6N:oc`D/Xhu=1Khp2F\r", "I,'4"), [10])
    def test_case_331(self):
        self.assertEqual(pattern_match('QFM}J[[!iI0/e6A%_-b~\t\x0b[NaX62Z2HIr\x08S1cdYFwV(wYb\n]j|];$8~s72AWv?z^D#3}0M[\x0b]~q8eNn\x0cg_q07\x0b2iwz\ryb', '~\t\x0b[N'), [19])
    def test_case_332(self):
        self.assertEqual(pattern_match('kZ$:ES;tb\x0b,;j;sbAeY1\x08xm?`#AC7$uv[!\\.>5,> T[2u)\tI`l/\n` ofw&V^`,p^1=p\r7+&H"ve>]u+ Z(Q%!A\tF7$jjoB"LG([9', ';tb\x0b'), [6])
    def test_case_333(self):
        self.assertEqual(pattern_match('Mt/nA[k<h@wM>+w=2j&\n\nQ`*Vg_lf>z \t}0dwS7La\x08pFj{6" nL"rq%\x08[a5#$\x0b+r2cx}z(ly\\ga2o3N^^E+ad7Mv}8hvH', '\n\nQ`*'), [19])
    def test_case_334(self):
        self.assertEqual(pattern_match('cBB$rZJD-1\x0ba"Yik(Ma1\nU7,SY#B*k7[A<1j8u\x08qu&SJ\rL-wK7*{qw?wFWH', 'w?wF'), [53])
    def test_case_335(self):
        self.assertEqual(pattern_match("'se:E:e}Hf\rDJ^v'ZMh3j4qT\x0bW+;cmy_zkr+\x08^AyqxmvZ\t<\t2$z3j_", 'e}Hf\rD'), [6])
    def test_case_336(self):
        self.assertEqual(pattern_match('3D!yp>8`\x0cdw[\x0cIS!5L-7I>w6!q_]IA>v(5yGP5,Fl>TQ5jYxrdcj', 'S!5L-7'), [14])
    def test_case_337(self):
        self.assertEqual(pattern_match('fLOgQBK!g=ci-Z, khzDiA9dMS9Q^N(<R"pK\'Wq5j9^}AEy>3rLj9[yQB"<;"C\'v\x0bmEg\\EL^6S`AQQFm', '9^}'), [41])
    def test_case_338(self):
        self.assertEqual(pattern_match('72fXq~QZ,e5BQUQ>MOU\rpXI=_i\x0cwL/$Gv*kZtc<R7Z\x0b>{w ;-@5;qv3:', 'Gv*kZt'), [31])
    def test_case_339(self):
        self.assertEqual(pattern_match('1]#(.B8/${\x0bMz\x0bxOuD;6&>"]}$:Ix{A\r?g4zw|DS,@.aSY6Q9G\'Rvil_w^mX#PUWrEt(p0 ~B@lt\x0b9,\na>,"\x08#[B5O)v', 'xOuD;'), [14])
    def test_case_340(self):
        self.assertEqual(pattern_match('0DCQ70;\\50nX\x08%j7\x0cN84JPQ(M\\+{MP2|c,Vq\\C1}1&vu<y?L[lWD,EP^v{', '1&vu<'), [40])
    def test_case_341(self):
        self.assertEqual(pattern_match('+bcP~6Niu1oO\x0bZM1{H|GpT0yPU?flm|Q\'M"^=?}U_r~0Xz@v6CyI', 'GpT0yP'), [19])
    def test_case_342(self):
        self.assertEqual(pattern_match('.zyyf2\nrE\\8Uofm:VQ;AQ{\x08\x0bh-..NGee6GZ|cu#J\x0b19Ex_@QqrQ8_s+i6M7vWj\\s>0H$', 's+i6'), [53])
    def test_case_343(self):
        self.assertEqual(pattern_match("\x08i3Ye:yFAG35}Gs(gBshWTRV\\]|/+OY_$qI62dmm=l`/F/q =x~t81uog[73&Jvlj@BfC\nz8YIM=\tn\x08_s3|no4+6Ml)'H", 'z8YIM='), [70])
    def test_case_344(self):
        self.assertEqual(pattern_match('~X+;-~):A}(5Pv!&i-^[!Ahh1_R`Bb@kxqD\tpUJv\x0c7NA1!bg}-w\x0c_', 'g}-'), [47])
    def test_case_345(self):
        self.assertEqual(pattern_match(">|ZNUqV\\`7JH9Rt{wC@SWL=]O_p`ltylOK'xOJ`.mBmZ5T<\nb}Ep1", "K'xO"), [33])
    def test_case_346(self):
        self.assertEqual(pattern_match("\\~DB3wYe!A&\x08s,U5I; !1=NO`Z[BsM\x0b>pWIU'^yDfiTTR`7!0H", "IU'^yD"), [34])
    def test_case_347(self):
        self.assertEqual(pattern_match('Rz\\DMUXas\x085,\x0c"I\x08|a 7g>=8Q6w91~T`4"tZV:Z!f=\\k*\x082nb\x0c;6V\t8KjB', 'b\x0c;6'), [48])
    def test_case_348(self):
        self.assertEqual(pattern_match('r{MeCK{-R0cy\x0bl>?"haA,V]7#HdE&7J|B}JFO6f`24|KH \nz9V5j=wQ\\,P09?\\>g{8(Hx(D}VJz`c^', '|B}JF'), [31])
    def test_case_349(self):
        self.assertEqual(pattern_match('K:=%^NP4p3{uJ$4l!xsq"O>qs|z\t$`[HG>=PNd/w$)-Ka9Y=7Dr}Ho >', '`[HG>'), [29])
    def test_case_350(self):
        self.assertEqual(pattern_match('hjmQy\r}Kp)5lOY`}0pGu\x08SJzMNeG[!su0A:x\x0cEw9\x08v&%1`X\rWM`>|SZ~ I:2\tz`|#jisPE\t1*O;^%', 'p)5lO'), [8])
    def test_case_351(self):
        self.assertEqual(pattern_match("$L<`S\t\x0bUnMH]UL<E%&:f[xH$ZHC\x083.B:hw\x0c/q\rz\r3~47^kHv}rJa} \t'|\x0bUwn n^qskE8 ._j3s1&gnn0lFZ.8kCG*<'", 'v}rJa}'), [47])
    def test_case_352(self):
        self.assertEqual(pattern_match('LU^jpgK6KgoHxI"p\x0b53i&y\'\t\x0crt8UGu|odWqV9JQ-EBlq4z]DO\x0bf7\x0b~y5mP8X6', 'qV9JQ-'), [35])
    def test_case_353(self):
        self.assertEqual(pattern_match("7jl\x08>= '\\p$;hY\x0b-9 ^fXt69gJ4+9@-BG:]oD4=\x0cTJYyR\x0cSsn||ipl", 'TJYyR\x0c'), [40])
    def test_case_354(self):
        self.assertEqual(pattern_match('u lqxf!1wfi3]m,/+f-\t1jICQ?w]66PhWrsqFUZgji9?\r\rO/om=rF;SN:g%', ' lq'), [1])
    def test_case_355(self):
        self.assertEqual(pattern_match(",1\\|g:p]*p=4']MYZo<0M@@]'>uF#0<`=Q2C PfqE.+:5PLS#\n4..LkWAI+!\x0cgD)]~k`c.0", 'M@@]'), [20])
    def test_case_356(self):
        self.assertEqual(pattern_match('H~;BGSM=%"Dp_d){-j~{N6hOysGT)n"/2v *w[?6\tlk#mF*EX_ay,}anX{.', '\tlk#m'), [40])
    def test_case_357(self):
        self.assertEqual(pattern_match("$*pLw(xO)DNca;9o5`48wA@iko~TFT>'\te14i?*,Sx!T&3/Q5]1MURrNE7cHb$a75l_w)\n` ;", 'E7c'), [56])
    def test_case_358(self):
        self.assertEqual(pattern_match('rB\r&k>vl`UQF\x080ZLU-t\x0bE[Ng\x0c7]Pr*V e-$v\x085q|"!zRHH"`AJoB\nA\\. f0M]O#', '!zRHH"'), [41])
    def test_case_359(self):
        self.assertEqual(pattern_match('LMw}pW|N@Vz\\\nLO:,]Tx;*Y[g9fdGBbxTCF%y\'5qQAs"gL-}U\x0bSVDiImEC^$U1Fj|S\x0c.c\nt>/%UR`$_as~*', 'dGB'), [27])
    def test_case_360(self):
        self.assertEqual(pattern_match('ooz-[wr0]]C\x08-6J9!E~DDD~uE%Q0Niw1WiDMKjfRo_$A:TIJ3$MdHk\rbB-|Hdoc)ok', '-6J9!'), [12])
    def test_case_361(self):
        self.assertEqual(pattern_match("tC-X]J\x082\\q5q5n#4\x0c\t\\Ynz}fFj@0*\\iaaZfO$1hgk=)e!a\x0cc3=\x0bm_r.'}e\tV\n", 'k=)e!a'), [40])
    def test_case_362(self):
        self.assertEqual(pattern_match('\x08\x0c\nhpOSbR^sx2j02;\x08+cC O!)^xx\t\x08b1+aic8fcQEgPHX}jp?(\n+\x0c|4Ki', 'OSbR^s'), [5])
    def test_case_363(self):
        self.assertEqual(pattern_match('yd5DdewBR6!k(6qca\n3r:4\x0c)\tx*lAf).nDQg5(T^2?pp+}]:ih=\\SiI_wV^|6<"rVJXSN<J', 'd5Ddew'), [1])
    def test_case_364(self):
        self.assertEqual(pattern_match('Q$U{\rN$S2i)`5\\\x0c(Yj(_8!45G\x08\tim#[t2d(ft +=5au,BuQbcHF?;-0', 'Yj(_8!'), [16])
    def test_case_365(self):
        self.assertEqual(pattern_match('Zml6]D:yTk-Z67KF\x08\nbJv,Wl\x085E>X>1y\t$4\r%Uqt} p;[v2i|rjnf,PjDLI', '\nbJ'), [17])
    def test_case_366(self):
        self.assertEqual(pattern_match('"\r\'+3_1gMZF(V1Gu[&._p@].UiR}VE\x0c1jt,\x0cR{\n\rHO7<uu\x0c\\Dz8eeniRNGR_:\nAuMD\x0c~XUqv>0)\tV.|&dPo%2jYe', '_p@].'), [19])
    def test_case_367(self):
        self.assertEqual(pattern_match('n\t3%dQ{\'hD/(HOJ+AjK\ttv"Ot$\n~G%%1]7G!)p@M]9+o;$ajpa8od[ u\nu#}x\x08', '(HOJ+'), [11])
    def test_case_368(self):
        self.assertEqual(pattern_match("'J~ccU}u[/#GMy\t%4P\t.S~+hS,H`+7uN*&to\rmt5\r&>,Rc\rArh5u=K@\x08n\\W\x0bbWL{Yzh\x0c[V", '*&to'), [32])
    def test_case_369(self):
        self.assertEqual(pattern_match("u.\\h\x0b+v#$:S,-C`N'\tdM,#dlVBVc_\\FTK!M4T$-19MqG\x0bi#)m5<G9eM7qD\x0cx\x0c98J/2&*s2U&zk^3J'\x08gIuN_5\t\r^> ltFgI'?Y", 'x\x0c9'), [59])
    def test_case_370(self):
        self.assertEqual(pattern_match('8g~VU/EM_A#dqN\nxwpC5!-f<PO{p25xVc0T*vj*7lg)t5`pG TmKW(', '-f<'), [21])
    def test_case_371(self):
        self.assertEqual(pattern_match('.xMM(%&qZHV_QHF\x0c|\\w\nKYk:"c(l \x0c<Z=\tyYZ>( GrOWuKt{.<0>\\A4n42.Wp;w<Mi``u4JxV5O_+#x,+we\x0c_', 'O_+#x,'), [74])
    def test_case_372(self):
        self.assertEqual(pattern_match('jr5kyc8(p%AR:bW/RH"V!leHu_n\nfzo[/sa@zs5Nwrn4g\r~xOMGe%HGL<o{9rL\';nO\\&?P%9[5XNY2,*>J;Q;6-Uox!U@j', 'Uox!'), [87])
    def test_case_373(self):
        self.assertEqual(pattern_match('YBA)42xR<ZRt"pBUCi!\t/S_[6|U~-ohI[j(\\Gf{A$5\x0c\rT[*euW\rCID5[<g30R4FFmc5i 5)@d[QRJ(Gc-f', 'FFmc'), [62])
    def test_case_374(self):
        self.assertEqual(pattern_match('k2ZzVUk;!c\rIOX\tx_yU\x0bt*P=V\x08E0^K\trK)-:<!@`w3{+C!\x0bk\\`KIG.<Oh>{X!<:(hgU\nV^wwOn\x0c2s0Z', '>{X!'), [57])
    def test_case_375(self):
        self.assertEqual(pattern_match('-V9P\r\\0Qheu\x0cX\x0c@\n\x0bEAH/%ne\\,J!e27Fp\x08_g,-xGw<\r3 ~>j\t4Br }% ', '!e2'), [27])
    def test_case_376(self):
        self.assertEqual(pattern_match("cmNt\x0c6=&ojV|&MmsBb4?S@9lJ9H<W.W%7>\x086\x0c<gm3+\x0b\ta[.aYuM`\x0bL{CY~ZT(\x0b'Cj,5oCm", 'S@9l'), [20])
    def test_case_377(self):
        self.assertEqual(pattern_match('L~LDx9\n6I:C&2H#tR(lNOCoO+B_kJ|VL\\>5aabaQr#q\x0c!r\rdERS)c##4', 'oO+B_k'), [22])
    def test_case_378(self):
        self.assertEqual(pattern_match("$Ug>J:p\t4o?\\s)ejb-wx=z-HW[=>H_![:lE>P6' 3xd)@Hw\\d1B|]J>O", "P6' 3x"), [36])
    def test_case_379(self):
        self.assertEqual(pattern_match('RK^/)bn9@LH\t* &sD=\'SZ XwSmJ 3z?BO\rQl\x08f#l``2]2`eZSdCB8Cl-r"R)-S_VfR,k)i/UE-)0', 'VfR,k'), [63])
    def test_case_380(self):
        self.assertEqual(pattern_match('o)[uEj?P\t7\'b\'e\r8D9Z\x0cF-_=I/VQiH`-rvhZ+sjg/3s0P@gBfx*_"(\x0bZiR|!QPhnV{\'><@*f~\n/[ia', "nV{'>"), [63])
    def test_case_381(self):
        self.assertEqual(pattern_match('ihh[_,{\x08rq5\'z?fC{rnZ{\r"&EQ&_J3p;dQLb\x0b`RC,pimF\'_l$-[\rMlS$nb!\x08F{\x08QM.De\rxt\x0b5-BBtzhvLVyN$\'Fq', 'nb!\x08F'), [56])
    def test_case_382(self):
        self.assertEqual(pattern_match('jU[|l"raT54`J2f<=:<P[{0T=>$>c0BlX4 \n"qR_j+w}nRBAq1*HV', 'lX4 '), [31])
    def test_case_383(self):
        self.assertEqual(pattern_match("\tru@6?XI^6StQ(Raw5~*-Xgg='=rYu\nhVAmQAM;MXT@7q-twp\t\t1\ncOiHc{l;hW\x0cmx\t\x0cB4%e~0%j=9,8&]m_\x08]K:u6", 'QAM'), [35])
    def test_case_384(self):
        self.assertEqual(pattern_match('AO/cZ#J"v{\r))f65)d\x08nw WB?i\x08\t:b\x0bAnbuJ<t&\tpW>7"v5y.\nYT5^R$\\Y#Ca;7gdf^9HXea(C<EwwA', '?i\x08\t:b'), [24])
    def test_case_385(self):
        self.assertEqual(pattern_match('*zI+A*LQ\x08(NfIM_FOgkFPv2i@lS\t~fUprnT0g,~&iBGv 8$$hH+L$h\x0c`Z} "\rJ#\x0cz|:u[?jXlnD<Cjo]C\'4!\\7myt1Rj;m', 'yt1Rj;'), [87])
    def test_case_386(self):
        self.assertEqual(pattern_match('{gy7lv &ktz{\'({FnOS LB68=^7\x08vLqN>;s\'nj^7pcv#}Qj*5cy#"ue*}x5/S15/|r4q%j8\x0bs6}b[0jCl.]@=', '*}x5'), [55])
    def test_case_387(self):
        self.assertEqual(pattern_match("~](\r|wH,8`cDmoFZ\tvy|lIB\\fy'`N}Z;\x08\x0bCL|D%]=|,Q{?fK3\r.%mgdBf*\x0cq-#1,6Cv& -%[Ix.<1-+ZLMu _Fer#7", '%mgd'), [51])
    def test_case_388(self):
        self.assertEqual(pattern_match('Ako)\x0c1oB?Fvt2P%\rA%XV:]`Z=3Zakmc-k8{%!!)Mts#$:eiAe\t/O`I#8@0Z@`2b{n\\P|_1Kz', 'Fvt'), [9])
    def test_case_389(self):
        self.assertEqual(pattern_match('R-Jrr{sMhyF:)h;p}1E:\x0cl-iC/8^I$\t7l3J,`<HKxG+j5z\nM3EwX;,zg\te={k@5`dt.\x0c\x08', 'xG+'), [40])
    def test_case_390(self):
        self.assertEqual(pattern_match('+YD=$\x0cB2MAP\nNFQDos<:?g(\x0bln^^s/>juev0$5W\tB\n\\<p\ruzmq|<IAk^\x08r`\x08bw>2|', '\x08r`\x08b'), [56])
    def test_case_391(self):
        self.assertEqual(pattern_match('DjuN-(Vy{n%G/1 m\x0bPc1U5Z}P\x0b,E$7i\x0cRnQNV]v&hoc#UF5w\nERwE<i=>c7^>&y%K=FjHtV,N,_,?0LIJ2H<^', '&hoc#U'), [39])
    def test_case_392(self):
        self.assertEqual(pattern_match("&T8G(\x0c\n6![#TPcaXp+-.3\n!akm_42/P`FoQ=_K\x0cI1K ^c/q-0%=pJ*LUjr\rAc\x0bO3h=qX*t;r64Wd'p [ s=MT\tA~w?R", '%=pJ*L'), [49])
    def test_case_393(self):
        self.assertEqual(pattern_match('V!my/,6#y?}*P>\x0b%?b7mL8[Iylp\\|=\\lh=4\x0bZn}+V`YR?:i@:>20I##zuaC8;\x08\x0cz3hU~%B!D=]1X4%pA1<G)8g\x0b}Y', '8[I'), [21])
    def test_case_394(self):
        self.assertEqual(pattern_match('/G%>:h7"I>7GJbvui-N\'}\x08&i>^vL\\:J}T;/z%leoQtPns&]C-U<uykL90oKi3Zg+"^\\Jjh|#LOF', 'z%leoQ'), [35])
    def test_case_395(self):
        self.assertEqual(pattern_match('hRhr*/SO3\r(R=o]46,we[0+[mbNR=P8~&m4;J\'x\r`QDr<Gjl]C$4xyd{U"EINch]W`RD`GYk$U2S@{5:', '$4xyd{'), [50])
    def test_case_396(self):
        self.assertEqual(pattern_match('@qeh\'?V_ADm\rryoEixx -`%tkvNCCm)-\x08d&`\r/Un%Y6us\'"Jp{Z\'sr\x083pH\'UA&\t\x0c_-N-BG\\/yTIM3wye', '-\x08d&`\r'), [31])
    def test_case_397(self):
        self.assertEqual(pattern_match("HK5O((&hfqzal;>/*6ehJNPYh\tL]X|u7DD~e9#%\x08iDn[R(k}X3'Ba6(oeugJ k*`3\rZ@}Lt*\trv'Wv:%S]w\x0bK'l", 'ehJN'), [18])
    def test_case_398(self):
        self.assertEqual(pattern_match('8p)TYZ4|_iddW -Ojt\r3M_iD$7A/+O\x08O]W+\x0b=H66CL1-\tX:RKN:&SOVqSw\t', 'H66C'), [37])
    def test_case_399(self):
        self.assertEqual(pattern_match('+!=d&k\x0b\r&6U%LZD+~P"K48g<w|`i#Mm.>Uj9O&\'AMfRF^qe\x0cU.LSI:A\\cL\x08Zv2k-\x08rTCs2\ncGE*9', 'D+~P"K'), [14])
    def test_case_400(self):
        self.assertEqual(pattern_match('4GF2J#aM\r@!Pt_\x0cFp[?3k:$P}MbZ& $04\t"|S9\\q\n{JDg%S;4}\niSKFd\rOx@k!/#FUBQ\\!%\x08F]G}AJ)\n\x0bN', '3k:$'), [19])
    def test_case_401(self):
        self.assertEqual(pattern_match('UT :U5ba7?p#\\gExn[\\Td> ~b\x08^)v\'a"D\t\x0bM(UkGVZKV#gQ<dgJ', '\'a"D\t\x0b'), [29])
    def test_case_402(self):
        self.assertEqual(pattern_match('G$~4de\x08Jj#uf\'w[W%\r\\-rJ^p"OR,ZV7#C.XxY<$ze\x08hwoNCYve/%51.`ZzD3l]o|', 'woNCYv'), [43])
    def test_case_403(self):
        self.assertEqual(pattern_match('c8K#N{i#I; .y}/M\'Jb)rRH%Z~.2\tfu4nPyCbuDOoj]c"}kO2T[C+|l72apQ9@E=', 'Z~.2\t'), [24])
    def test_case_404(self):
        self.assertEqual(pattern_match('PZr%5>=Kq;.2Pe4Xa7-2(BRrg5VU35x8\nXOL$d`_dfcLt\x0c2"u>avZF.4\nRG1LuH>S*j*jl@}Bw1F.A3~mS:]6:d\\R\x0b', 'cLt\x0c2'), [42])
    def test_case_405(self):
        self.assertEqual(pattern_match('pN[,fpii%pZdaI=,=@4\x0bz0i0@1\x0cs"rc\n{Ne6~;\r\rQ[isFx8..\tx*O<+?M&\tQE?9\'d}TrlY382^Zh}', 's"rc\n{'), [27])
    def test_case_406(self):
        self.assertEqual(pattern_match('zRjJVFRit%=5%\\W\'G"\'i/\\blXSxd jL\'0\x087<\x08954YX"[[+i\r6"+B2ofnpP;5a38rOrkc4vF.F`~\x0cifeXi2', '\'G"\'i'), [15])
    def test_case_407(self):
        self.assertEqual(pattern_match('7J\n(0ODA.68@z/i&\x0cuCx"#^sulpNR+^61A|1\r7kPfqC{IVuoCfDtw:ktx\x08z}0r\n', 'A.6'), [7])
    def test_case_408(self):
        self.assertEqual(pattern_match("FN0';'LKkhk\\/#-#6aZeoWJV(>8f /@D|j^u7\nIgHlPw.wn-k>", '#6aZ'), [15])
    def test_case_409(self):
        self.assertEqual(pattern_match('<L}L77u(\rjrf:i\n3E) -r21W67!(Op"b7\x08f&_\x08yWROq5h+p3~ttka ~84G7|y:A=%uD&_n)D', 'rf:i'), [10])
    def test_case_410(self):
        self.assertEqual(pattern_match('!s\\}kq2{/5Qgc[H>LfF!U#KOc1P]j(\x08(8CBJ:Qz`~*><$&.#*D\re66&d~F2q', '&d~F'), [54])
    def test_case_411(self):
        self.assertEqual(pattern_match('~zl<\rftb9]y\\^%l$"#e.-"y\\n@q!E@$,@^<\t8)$f\'8F*L/p@HCG_t\n\x0bCK-Ph9Dgbom|c"', '<\rftb'), [3])
    def test_case_412(self):
        self.assertEqual(pattern_match("NO+cL^e+^wjV`_@b5\ruKOuJ%mKO^aNc)[\t'NN9]7!\t5Y\\z LE1H[!us%yJrWA37NT0ri\x08", 'E1H['), [48])
    def test_case_413(self):
        self.assertEqual(pattern_match(',*N-V`:>PLZk,8S?}U&o}sz\x0cvqrA~\x0cN}y-\rGc:VhTwFV-Gh]hn*q|Sg8\n$*Ct7_&\x0cfE]M#IBK /U{H]F3].\rM{\t~5', '3].'), [80])
    def test_case_414(self):
        self.assertEqual(pattern_match('jp\x08Hr>/\\v*3kRl\x0b2qD2}U\t/:MrS\r{bFwW3\t34k7$kIP4F8Ny]t>":=0RyVCuoO:A\\e#[<w&=5<8F>r', '\t34'), [34])
    def test_case_415(self):
        self.assertEqual(pattern_match('c!NbB&4oNzC#"!ozhw*8)jCo]#3W|V(Z\t\rBiak\\ixtU7EZ,F+XG85/<*LK', 'Z\t\r'), [31])
    def test_case_416(self):
        self.assertEqual(pattern_match('\x08t![+h3\t#Nqm3(?\x0bU-7)p=~N~xN]JpWt/3\x0b\'\x0co\x0cy\t-ye|LiVE7PQ\rcy8kGBJ5)?Ph}E0Z6z"l\x08l OsG:', 'E0Z'), [66])
    def test_case_417(self):
        self.assertEqual(pattern_match("\x0b#qL0*YAJV#\n%Rko{c|wmvc!Pd?mI\x08F>1l`0\x0cv4qpj7yA4\x0c\n'\rS^`^+F.Q{$4b%$_3*J8?\x08(y$Qzhg", '.Q{$4b'), [56])
    def test_case_418(self):
        self.assertEqual(pattern_match('ruUzr+\\d\re5c,D\\\nZ+A\r-UR;%@.Lc4jk\x0cB5f\x0bNhn}xmxQ* w<$}cj;h)p.^P[cP |(1<s', '\nZ+A\r'), [15])
    def test_case_419(self):
        self.assertEqual(pattern_match('0P:@+}Oj.]`apkO{\x084V6Y}5bgc \x08FcA\'\n+iEb)0ajZ3s\x0b&\r.8{^^M/qI\\H`\n"dnf$I\'#\n,2qU/', '\n,2qU'), [68])
    def test_case_420(self):
        self.assertEqual(pattern_match('.3i$Wq\\O\\Z&_IQglOd[+\\4\rr[_0tiz;PG=bz15*W\x0bG`>4=>L%XM(e>+!oi3*|!GsF\x08yUB3\x08$G.:9oD(BWb0J[pki\r<\x0c9', '%XM(e'), [48])
    def test_case_421(self):
        self.assertEqual(pattern_match('&$Qi .K__xVo[HVUs<*QLu"{/\x0b^\nD\\xb[\n;Wqp{c01MTBV]]}]3\x0bcgJOb)zKlZI{x=4I5vR"qnT;SJ*Z#', '&$Qi'), [0])
    def test_case_422(self):
        self.assertEqual(pattern_match('fU2j\t,=DzMW>YoV][qLg>\'^Zk\x0bi0Sz\t_l3BU:Ov$2lB %EfI!\\Da!$ic"E-HK=\'$V-vW&*/40\'R2B<4cr', "qLg>'^"), [17])
    def test_case_423(self):
        self.assertEqual(pattern_match('TAv;p$l_bc<vJoXm6{G \\RZaM\tlsb=5M8+}vf9L(!\x08.)J%}*B4QsfM-_j$zQm\\ \tICy@;w;[;4F8*U#R6XSALAaGe', '4QsfM'), [49])
    def test_case_424(self):
        self.assertEqual(pattern_match('Z82Y-_^?X{V+qc@fxZU:\t~Z`s>zuw$,\'L\n\x0cB/(y"z%\t*N;V_LdU^X', '%\t*'), [41])
    def test_case_425(self):
        self.assertEqual(pattern_match('\x0ba,_0x9mW@"G0M,$@n\x0cul W-Ub>9\nae+[A\t=,ZaMC6+j_v%9\x0b#A2T\'x&?8*Pg', 'l W-'), [20])
    def test_case_426(self):
        self.assertEqual(pattern_match('uRTE-UcZ?NzoiLkOk1i JTpI`o\x0bz8X\n$\\^@T|Zh;>@\nBnEIK97zJ^muf"ol#b65c\'.6S<r0n`-g *[~)Y|{.<Aw4k#6wEwg~Bi', 'Y|{.<'), [80])
    def test_case_427(self):
        self.assertEqual(pattern_match('$-]08l9< .Cd}SgDiqs\r&poB(lB)p#=m6pwM2\nHz\\\\>d\\s\\J/\r*?E\x0b2w\rl$7c~\x0c', 'l$7'), [57])
    def test_case_428(self):
        self.assertEqual(pattern_match(';t5w_8Rsf5wC`12c,ef1U\'=j+M645\x0b9b>/Z W"\x08%%u%f8W5`qln_-ycHU"[gk_P=<\\Y|kaac\n~4[]?', 'M645'), [25])
    def test_case_429(self):
        self.assertEqual(pattern_match('jz>Q>!_X~eN1}2!nN_J/Fqaqw4H\x08Y]tu@\x08D36\ta4\tMwAwY#+X!mY%\t(!a', 'H\x08Y]tu'), [26])
    def test_case_430(self):
        self.assertEqual(pattern_match('{1+w$-#^6GAfw+VHRTI/C\x0bh?kbjj5/iQx\x0cwa!7$p+Zj!Cdb8n|?B\toFp(18?}8S`~gz-Q7F)L[:CFppadmD)|?ox', 'p(1'), [55])
    def test_case_431(self):
        self.assertEqual(pattern_match('cQjU\n1YX!&,N<rQtO,HOe,JX?Z{}p3tF8& +\x0c^3%Yn\x0bbMM\x0bbDebIT88\n pg*L@"Mr<sqwtyZ@rnv#Ryhk', 'r<sq'), [64])
    def test_case_432(self):
        self.assertEqual(pattern_match('e~Uc<\'\x0b?\\.!38xja6g3:S)0d8\x0b>^5tZw{Zn\x0b^p-`eTeU%G]$2f>"*MdQTEOUJ*(/kSqE', '"*MdQT'), [51])
    def test_case_433(self):
        self.assertEqual(pattern_match('RGsn4KvcH9+."|W AA\n<xb9qOd~2"1\nRww!P,;8YZt\x0bU\rP=9T"l$2in{QSpK[VlzY^:\x0b:dry0G', 'w!P'), [33])
    def test_case_434(self):
        self.assertEqual(pattern_match("'u^ZsZcg;(CMe;b7Gi({6y\t{gvv$\r[s3qhZH/%`t80AWo=EuD:uyY$AHvx2O4H(p", 'vv$'), [25])
    def test_case_435(self):
        self.assertEqual(pattern_match('3 ;?dpVW=%)f(B7F\n/<zxRq\\1AwP; giR?yTz*)u}Z6EB"8:33GABf\x0cj)eh*GTP8Q_Mt@F%D~>q}F)SLs/y_T"gb9U', '\\1Aw'), [23])
    def test_case_436(self):
        self.assertEqual(pattern_match('\x08t\x0b{iQ\\\x0b8#;!!ap|Vd-=M6^vy9W#VzoqO\\OROQ=X}-kOSX@z_2 zr1fHyl<EF( +n" EY @]bsr)\x08|uF2J/\x08u\n$gx2<U:', 'zr1fH'), [51])
    def test_case_437(self):
        self.assertEqual(pattern_match('Pz<doIk_&yQ7fDB@ep<@DptSW{()+z30 \x0c8IAU@=wBCW/RD i\x0b&a1iWKkFpy{yOa`*Y5"\x08G:j2via\tV\'X\n@>;=O]TI|di*rY', 'SW{'), [23])
    def test_case_438(self):
        self.assertEqual(pattern_match('4B)?\'ybik5\x08mIO72\x089}nf2/>">26K"aFTQ|%TtXt(y$C#\\\x0b[~2*wX\n-?\n', 'O72\x08'), [13])
    def test_case_439(self):
        self.assertEqual(pattern_match('\x0ch~}:Ms\x0bKieD\n.#8:IEX^QdmV4ntL2C>W*)k3QA9XUMzfn\tua_r7C8X{F[BZ\ro;j#ttQ,Si0(}.j\ta.4', 'C8X{'), [52])
    def test_case_440(self):
        self.assertEqual(pattern_match('\t\rL\x087=iB)_ZSU%\'Sj?t$1N b_C^1>b#n?ZI/zg_cs"Zh;kf)*73Ayu`\x088+TVW16]ln@a}r/<q3!lLvw\\>Z)9m-@q;+\x08\\"0yLMYgH', '\x087=i'), [3])
    def test_case_441(self):
        self.assertEqual(pattern_match('BlZe\x0c>-6=KFvIJ83\'Hmbu&Gs&ie")UC\\WWo jzMD@N[;@N\ny%QZFg\x0c?qsAM~+t8&k,}9S?\x0b"Mz8@Z 04L;C00k\'H=z\t5p%;aA}', 'Ze\x0c>'), [2])
    def test_case_442(self):
        self.assertEqual(pattern_match('kS?=^C\x08Tl\x08on(c\\C\r;%rYpT?f;~% WI~.KNK(F^}"L@/S3\'LS/', '?=^C\x08'), [2])
    def test_case_443(self):
        self.assertEqual(pattern_match('y( []~U2] "$\x0bKYhUr-@6o$KAPY6|.\x08\tq&LMJlK9BYTwngOM\\-ii}3LiL[s8Lr!:', 'LMJlK9'), [34])
    def test_case_444(self):
        self.assertEqual(pattern_match('Yv\'BW\t`Wh~1U[;XkzfX#@{NZQQA/r\t,n"HzX~5[x?=O|-C;J~]M"8dd1qPo9p"+/\t&4\n]za\x0c&*\r\ri', 'h~1U['), [8])
    def test_case_445(self):
        self.assertEqual(pattern_match("$cl`uje1yx=(%O\t^\tJ:PVqyffFU05LCdC(X'Y@_}E/fR|tV.82>tD;*'.PT7{h$@Gh+vj$0[\r|8!sRS7H@", '\tJ:P'), [16])
    def test_case_446(self):
        self.assertEqual(pattern_match('"[Xu\'8iSnG\x0cT&:6*Z=cH<`qecfC/}|\x0c4\x0cK"f1J#`1e\t&qrSkNdPI', 'K"f'), [33])
    def test_case_447(self):
        self.assertEqual(pattern_match('Uwe~D)]*\\T+*N Uo\x0bfL4J!?[\\]xWE7UJZ#65&# DQ\r:\t|n;\'a\n\'`.z|I8` yd)a2.s.#42}z?yw".{Yj%VWb*e73(VDxM:]:', '+*N U'), [10])
    def test_case_448(self):
        self.assertEqual(pattern_match('9f3x\x0b:Fp>\t\x0b:T8/}4(o*p\x0c) xj55.(~\no)76BP&E/FhOjA(R`D1quMn7j\n*O#I*\n8*`TzwQ\nn_##A', 'D1quMn'), [49])
    def test_case_449(self):
        self.assertEqual(pattern_match('[`\x08Sz4CQ61p*t"zG6[G>OdQjm <!>Z[}_6I`W:\'ix-js#wKcQ\x08E4xfyE%Bf\x0cP^$ZHYHEIS */}8KY\tC*(@c', '8KY\tC*'), [74])
    def test_case_450(self):
        self.assertEqual(pattern_match('\'|U2\t[J+k2R\t:[s\\\r"*jDn0G\rgk*\'\ni\\iV]j?DqSUhZ/|fs&oz', '|fs&oz'), [44])
    def test_case_451(self):
        self.assertEqual(pattern_match('L\r<iZ2/8fY;}\t;,&t/cS0VXg/JU\x08;Q}[Mim8\nbQ[Bz.V~OSPZn<BS\x0c6l~fZ8Bvplmb*,{\x08M-~">#9Eg!]IPk}BoqIW_\\&sGO', '#9Eg'), [75])
    def test_case_452(self):
        self.assertEqual(pattern_match('fe\x0cVBAV0&3\x0bOuuol~n) \n$0%6/wpzddDc#S[DZ!$xq/\rri\x0b/]GXGgwZ', '0&3\x0b'), [7])
    def test_case_453(self):
        self.assertEqual(pattern_match("|WdNB*msyC-|m=}IAL|1nD1R\x0bKO'Wg{iaf\r%cdBPF#|SCAzU\t>_Mw[%aZ<U`\x0bN59w8MrKi\r+l7\r6Hal\x0c", '}IA'), [14])
    def test_case_454(self):
        self.assertEqual(pattern_match('s!sc~bbDe^j1TbUXXVp_~|beQzqn>\t9/q]AL#(uO2NX=WKuE/6+\n+&(S"CB9?xS@7h>\\{4^[[M=q\x08~%[%|]:[M-b\tad\t(IWIOO.3', '/q]'), [31])
    def test_case_455(self):
        self.assertEqual(pattern_match('+R$  s\r~vb\x08g\'\x08|)q#5)uy,$\'cHvj\x08`ea??mD"=5[m]}!:HVb3K3p*|K~ww\'^KTOr', '~vb\x08'), [7])
    def test_case_456(self):
        self.assertEqual(pattern_match("VjN:.:1`a\teC^Q\tTxlv){lYhsFM,Ep6smAn;<'aEb&9Z4/C'i+kjMNe\t\x0c2Jo\x0c\tOSi{.B8=Q-\\|6Mx@HC_A1MP\nVxs", '@HC'), [77])
    def test_case_457(self):
        self.assertEqual(pattern_match('sb|a@y`zq)/@N\'P<(t/9,t{PP54"9K6C\\r,xg(C%gXgEDLt15Gq;|\x0c<"o1cmT;6so]mR\n`o72IH&Vb5', '"9K'), [27])
    def test_case_458(self):
        self.assertEqual(pattern_match('2kx{Y<f_7x^"LZ1ZcOO^Zd2CnuSJ5GN" j,]\x0b\n\x08>>\nksnjnbdB.\x08[\t', 'x{Y<f_'), [2])
    def test_case_459(self):
        self.assertEqual(pattern_match("eU?%VmiuQ8.2[;u4\x0b'9\x0c]o!\x0bVI8F18q&cc=!P\r*jVQ_{7U?N<|7xn/]o+P\x0b!9\nkSE=9QK/", 'SE=9Q'), [63])
    def test_case_460(self):
        self.assertEqual(pattern_match("KBb\rkU+\x0bSH^O{a'gOkex6eWS=1;p%&CD\x0cq+cPeT_T0gt5\x0c\\,ik", '\x0cq+c'), [32])
    def test_case_461(self):
        self.assertEqual(pattern_match('ffkpb!j*YsC\rA@\x0bj0?(g;E>\nMn(sU`kO[chO{\rb\x0bPHa.S@D#\ngC9 ircIXh=\x08qR*H|Vs)i7Exr kuDCx!oT;', 'sU`k'), [27])
    def test_case_462(self):
        self.assertEqual(pattern_match('s7uY~,X~0kr-r^(`_&{Uy+j?}g dyDdUmV<v!!Xeg,\r3Df51KiLg>\n$cio\nZR/DHtr ', 'yDdU'), [28])
    def test_case_463(self):
        self.assertEqual(pattern_match('7O}xJF;Z5paC|N9d@J, C)S}zQY_\t=c2R"/%w Igbni?T+\n}7GfP{E_ZYR/', ';Z5p'), [6])
    def test_case_464(self):
        self.assertEqual(pattern_match('F+1Hr\\Y//e}^vL}gr~0061rdqL1N`B4V?71\n/~c-1e.fMcR=N\x0b2qzPgb%frf+\x0b', '}^vL}'), [10])
    def test_case_465(self):
        self.assertEqual(pattern_match('!<6O\x08"qkWwC\\SaxGU\nR7{*>z,A4 j~{nF]U?vcWPV5wQ\nE~0U1<`bSx-X%tQ&RN-L{|M85zYE7|U;cb]:dp($gN0', '\x08"qkW'), [4])
    def test_case_466(self):
        self.assertEqual(pattern_match("\t?\r&qb@aiijw9Y\\xP;Npa2dZLm87\\\x0cU:zCsp3pG:'DGv3/V'D}\x0c'z^h['A{Vmn", 'xP;'), [15])
    def test_case_467(self):
        self.assertEqual(pattern_match('>9&+:co,m?Q)\tsx:e}<|ZHmih[G)S@8.rc;1a.YjwckFXE:bT.=BG=~H-e"zh]$Sw|\\qEaPUWu', '9&+:c'), [1])
    def test_case_468(self):
        self.assertEqual(pattern_match('qpL.O\x0bV/\rwW5ESZ;2 Y8]T$@nv\x0c)YjwsS#w<;wA&-h|/jF\x08<j;x\x0bK MK[4o#4', '5ESZ;2'), [11])
    def test_case_469(self):
        self.assertEqual(pattern_match("= !\x08hU#_M>&Qky5Tcx)Zt\t6qTY9yN:^@\r:~\rf&.U5o1kf.\nFV+HQ.}nYzAOfF'AAjX", 'yN:'), [27])
    def test_case_470(self):
        self.assertEqual(pattern_match("DGf''7=B\x0b.%<U@K.01S}/\rOKy>{k@a7<fO\t8U[=7N8\x08V]B#p[*\x0btr9*Q:+*F&7j[C6b1jrK'\\1;GA", '7N8\x08V'), [39])
    def test_case_471(self):
        self.assertEqual(pattern_match("* RA8\x0cK+-y8YIk.W:T6PhTB.!HQ5`Sc-:(-$tHo\t' {-r+rs%#\nM}h", '$tHo\t'), [35])
    def test_case_472(self):
        self.assertEqual(pattern_match(',(ocyH2q$uFn,tiwiCpFZO|rT}F/>@[Xj!x`e^pb9{Dg\'*bkR;~\\^0yd5z<fUc"1\x0bFgu"`', '[Xj!x'), [30])
    def test_case_473(self):
        self.assertEqual(pattern_match('I\\`sk?bX5S9^ GM*qMNPm`0u~co*-+T6f<FFq\'pv2"M)iu2r\n4)&', 'qMNPm`'), [16])
    def test_case_474(self):
        self.assertEqual(pattern_match("t.!7{*.(A*+-5S\r1Gg\n,`&t(l@fYaUlhBNS3KEI6:9,8Dwm=_bcl@f$F9;`Pz*.{0EsIA'T4BU3Jl)rs", 'Dwm=_'), [44])
    def test_case_475(self):
        self.assertEqual(pattern_match('w.s73"/?\x0b(\x0bz2\x08\'%q/haK{\nys#9M7x>)>H6n%E:RyDJTzM W`ayT)t,W}:;\'<oo^f>4<)#&|^DHVQ_%uY\ny@G[kgl]', 'zM W`a'), [44])
    def test_case_476(self):
        self.assertEqual(pattern_match('+"U~7FEE)GCT9+]\ttIqs=~T].eFXy9Ies4 rqC-7i;@)eex\\V]v]k&W\nGd\t\r\'zig7', 'y9Ie'), [28])
    def test_case_477(self):
        self.assertEqual(pattern_match('E v,6hM,~{ki\rL0U-%^h#r~]\t1^D)`j)gZqx.>PN\\7|Q6PcAB58+Z#]]hz,Yx \\5!U-nfhB)aR.p=vt', 'i\rL0U-'), [11])
    def test_case_478(self):
        self.assertEqual(pattern_match('izv\x0c\x0cy\\Ou_\x0c=\x0c7wPh=x\x0bXT5{<]ul!Z%WIdo$Hc@g4N$/2`v&^o.Ft3\nWMkbTkAc.isHDcIn\x0bX\\h0Iv mbxHMCtCP[|Z*iJ;*W', 'kAc.'), [60])
    def test_case_479(self):
        self.assertEqual(pattern_match('=ti:\n_\x0b}d8YwpWRz{F#AcWw<S60"Ll8;E=e>j9sCVK*B\x0c|b\x0ccFR`0aj(%vVQdCB5*o$}e 8"bu%v\r0&.oj|\x0b^\tDzVo<-t5!@]83', '\x0ccFR'), [47])
    def test_case_480(self):
        self.assertEqual(pattern_match('\\ZnoR*$\\:^-V\to]<F5"sVpK3mOyQ=^OJt*m`j1V\x0cJoujL}Q>\x08L-f.z[\r$C4\'AO]g\t}L=b*#\t4#vBpZ|Z\x0b2*Ma#-mdasP', '-md'), [86])
    def test_case_481(self):
        self.assertEqual(pattern_match('MX/@wi]R<:83\x0cvkh2K|9A_\r3|/mpRd&YLndh4Ff8IAur\r\n$+OY Uz=', 'YLndh4'), [31])
    def test_case_482(self):
        self.assertEqual(pattern_match('0HkQ31=@}JE9CL_]}L 7W*+>LBS!Cs`2@_\t7vb~%6nY6Cy0]}dRR\x08WQ1p\x0cN[SZ$J#qIl`%I*ENy &1t+', ']}L '), [15])
    def test_case_483(self):
        self.assertEqual(pattern_match('Xzw%fTu \n?V-VELC53*u8g^l+9/+^!.B}a$Rlz?C@8492sdQbyJ9t-', '/+^!'), [26])
    def test_case_484(self):
        self.assertEqual(pattern_match("U}ki*V-4coq9wi%K]J q'w.-e_#fH{k#=l&x[\r1\tZKu+)V&YG?Atsd9LtM`y\x0b,}^&t-[Yj4\x0bM\rFH)2|S\t#cP\\0L7c&", 'Yj4'), [68])
    def test_case_485(self):
        self.assertEqual(pattern_match('N\re?[E\n"IgX1gj@EE\r~qv!S,EDf/\tN(=\r5C\\7\tp\t6!07M*L05h}OuZ$v<>H#0i\r7M#h|r$g)I[ D)Wcm0wo\x0bw\tQr', 'o\x0bw\t'), [82])
    def test_case_486(self):
        self.assertEqual(pattern_match('B#a\t!r"`=$~BC|z&GU||p\n6g=t %iERiV%[*sXV fg\x08/_I"#{k}D(r `7U:Q\r\x0cP5\x08xa4U~:\'Yex\nKpx94K5B', 'g\x08/_I'), [41])
    def test_case_487(self):
        self.assertEqual(pattern_match('G%F/@TxG\\kq,sa x/W\n5 6`a{j\x0b3\tt\x0cUjS?\x08l9tNfO\x0caG>E=a(8R #qg*IlE\x0cuQqp', 'E\x0cuQ'), [59])
    def test_case_488(self):
        self.assertEqual(pattern_match('mf?yh.mE(>\x0c2^d7c-@W\x08roa\rza}E C?D~"Tt`co#jdr,9e%)=\x0b,/j&0)>J Y&\x0b\x0b\'*4A}LK,VR[n`eVCvzu,M/?<;6Gu>', 'roa'), [20])
    def test_case_489(self):
        self.assertEqual(pattern_match(',_F#/dG)L@sMTJJym=utfZl}:|&u$5Y(r\x0cpT\x08!q;\t\t+qN\x0c)#B:`#.(p7?FKbh\x082)%S>N\x0cTXvKLRXfRWlPJD\r"*J', 'RWl'), [77])
    def test_case_490(self):
        self.assertEqual(pattern_match('5S+6lOK.4dDo"fLRQJ>z_ur E3:G3T: {a=@p!86Eqqr)8Y6\t7\t-|\x0c{\\Q<o!E~u\twdu58rt}ieS', 'T: '), [29])
    def test_case_491(self):
        self.assertEqual(pattern_match(">F],$2`QSwll'AM#^P{e5\\\npns5a/:'\r?$@^3rnT{N<j\x0b\reda6d\x0c[-u", ":'\r"), [29])
    def test_case_492(self):
        self.assertEqual(pattern_match(')`\\+n6A(dN"Fp"~]G B5\x0b^,0lg;@\x0b0\'A}L"A($&g%IMTe)v{8U=669T.FlAVFs\x0c&F', ' B5\x0b^'), [17])
    def test_case_493(self):
        self.assertEqual(pattern_match('>(UU!N&,ET"\nR1/!E3_om!~HiB1)&,O9@GqM*fM/$1mmbK(<j6"?t*<<H0kln\tp/\\c1R}<&\x0b', 'j6"'), [48])
    def test_case_494(self):
        self.assertEqual(pattern_match('nW7HI+XB4$S\rB##*X*NS)O?\\aS&&>|}m>\x0c\\zQ=SY\r\n\\[KuUWRxRw7tJd12O4#3VOIE', '=SY\r\n'), [37])
    def test_case_495(self):
        self.assertEqual(pattern_match('A5F"=,REK3\rn9^TPj.\\Q:xp@G\r|.+]pCb2[:4jeD(c(\\tA6\'/7{\x0b;VY', "'/7"), [47])
    def test_case_496(self):
        self.assertEqual(pattern_match('BiBRa\nK)d<i&H-FD\nO19D#`|P&]Soc:<3DE>~dpo6\x0c\rd8/t5TW5F&9OrZxuH^qdo%>WPSQqsm', '9D#`|P'), [19])
    def test_case_497(self):
        self.assertEqual(pattern_match('Dh"^0W ;j|9OBq*X~ eM>;:.?]Zs[^c5-uB:7heO6e5xW!#,%O8V', 'xW!#,%'), [43])
    def test_case_498(self):
        self.assertEqual(pattern_match('}#xqfk5C++(a5O\r&XWT4P6EUb0^kMD.EO]/B\t+cLNZRW+sh(+E\r{z_7UbPLdNw', '{z_7Ub'), [51])
    def test_case_499(self):
        self.assertEqual(pattern_match('Mu3hZjK{[VVeid`u%\rNV\x0bxch"H?Z2)%-";QXHO#\x0b$MSQ)<f\n=R[)l[I\rEYO(yK:sv74D,z+f%M3f\nF5$5FRg[6E6wc*\x0bS\t-7HvU', '[I\rE'), [53])
    def test_case_500(self):
        self.assertEqual(pattern_match('gR, @/Ze\x0cx,CPQ?6\x08 IfRCU;$z,MfQf3ZNw"z#\t$~4;X<q1\x0b)8d >]', ')8d'), [48])
    def test_case_501(self):
        self.assertEqual(pattern_match('$"\x08Q\r\x0bk5c;t9XxFwyY#81_K\'8\na\rdE\rgB*$p_o/tuAlCxc|Vh0"N VK&@#@EbE%Y{ @CC{Y:X<O`HP\n]', 'Cxc|Vh'), [43])
    def test_case_502(self):
        self.assertEqual(pattern_match('%+4YUy5[PX|Bq8+? {M?Ps8A45x_rW56y`\x08C>xt;Y do^#_X\x0b_`^yD=l*H2Yoo<b"#R:?eR19%zqqV?\x08BF@ 1a)1', '?\x08BF'), [78])
    def test_case_503(self):
        self.assertEqual(pattern_match("8.`H6^`jo'oD~GRP{`FG\x08g#qxy,iI\x0bA(!<X(p4-2.!\ralp>{@0@[R.y:<Yh\tG\x0bHP06H/hrM$Y", '<X(p4-'), [33])
    def test_case_504(self):
        self.assertEqual(pattern_match('s3Lz\n\r/a_.GFoE\t5uA&q{q17|\x08E\x0caz~\x08t*7\x0cR\rl#\t\r52dEZ)+2]uLQB;jml=%v\x08z', 'jml=%'), [56])
    def test_case_505(self):
        self.assertEqual(pattern_match('.PgZYH6?.7_6+fH:8RUE>2a}\rER6iSM+}2; G+"$HJpFn%%d\x0c,xHa\r,-SU9', 'R6i'), [26])
    def test_case_506(self):
        self.assertEqual(pattern_match('t=Jm`%\rfJx"3^\\\'6\\w`|"3>qpYk54Q~> ,>lS.?lA\n\tl9?mYMR8(DjIG4]{#Ja)Ip\rB=#?g-\na\\', 'mYMR8('), [46])
    def test_case_507(self):
        self.assertEqual(pattern_match('\t6/e1E<Wo cOp=Z+;FjG\n>NpUX;\t{nA\\\\#nr)IcVz\r62NB)NGsd\'T!<>A="ryF!\'Wj!gC|\t3', '>A="r'), [55])
    def test_case_508(self):
        self.assertEqual(pattern_match('\t>3v\n\\"F"DS9PCL\x08AdJQQ$g()#m[_Af/u4_a\t6Ljm\n!-h\x08w|xRif.S^@Xa', 'w|xRif'), [46])
    def test_case_509(self):
        self.assertEqual(pattern_match('\\r|:{9auz\x08T{q,[UK1\x08Iv/`HpVIl]]Hc!\'f7-x<An6"aIq32wRZ$-]-4mm7DMAuuOtF\n7=K;<QARbg)l/Ll6|f!,?v5\rmT/N\'', 'v/`H'), [20])
    def test_case_510(self):
        self.assertEqual(pattern_match('eHq6%Llu|j-_?@$*?#uL\t*+ic_j=4.j$B!iG|z423-JgDl/wsn&%BMWZ', '423-Jg'), [38])
    def test_case_511(self):
        self.assertEqual(pattern_match('f)Y!|tp\x0bFDmVM5\x0b]]"<#/}0w\'l[\rb+\nJ \x08#a!X\x086PN+~$PbxGUo)H?i:$m\x0bFg/rYMi2dtb\td\x0cW56z=1y1', 'f)Y'), [0])
    def test_case_512(self):
        self.assertEqual(pattern_match(';TmCo`\\YF:}j&!!_@gWuf:cl9C\tD"Bh;-[HWEN2uS<qDZY}~1^\nu, nwuH*X&t$p{kp&&dJ<', '\tD"B'), [26])
    def test_case_513(self):
        self.assertEqual(pattern_match('MB&j2L?;LQUf6ei\x0cnzZjo$LGX%Z>a<<DUwBcd4]YghBrUn%)9GUl8\'T)Y"c?p\\_\x0c5\x08O$,Qi`M,>\x0bv5NOu\tMb>@\\n SgZ@L\'I?{z?', 'SgZ'), [89])
    def test_case_514(self):
        self.assertEqual(pattern_match("[Yjc1\t$[I,0*m;e4ZOM>1B))b\tL9eU|#R@>sCk(\x0ccwoq2!26@oC$1?>dTa|'llx", '4ZOM>'), [15])
    def test_case_515(self):
        self.assertEqual(pattern_match('H5+4/X/lG[0`zK3`1rQ[r:[%@9QT~Qz%\x0ceUd\nv1An5xi}ul,\x0b`|#|Q5r\nZ>BWVN+K7}%j\rM<Z<NXf\nSr#\n8]#Qvx"8?', 'K7}%j\r'), [64])
    def test_case_516(self):
        self.assertEqual(pattern_match('*u:8e{UK%d/h\rG/S+f[!E(\tx(%#0bgT\tRc>W~:r91:\'U?,$ixCf-ZTB3X5 ? TI)pJ5JKO_! |Ezm~"0< %U0\x08rF!N8', '%#0'), [25])
    def test_case_517(self):
        self.assertEqual(pattern_match('\t]"`I90~0:\n>x_LPfo<@i\x08OCb!\x0c:eANq} U7P}qVX4!uKH\r\n+htLm(/G8`E1*hQat/RK}x-k^3zm~C9O;', 'b!\x0c'), [24])
    def test_case_518(self):
        self.assertEqual(pattern_match('f[|:"l(c|tc6{*4k\x0bOxr@_!I(zc.Yu="7Hpy=0rV|cj(uyc|DX\t<_&6\\./xJT-Wh\tH\n!P2,@QVSVAEj', 'c6{*4'), [10])
    def test_case_519(self):
        self.assertEqual(pattern_match("{yhp_\x0b.g\t6!\rO5=e,h@0yDb6}-%a%c9HFx50-k5c3/\nQoTEWKy\t0A$C!\x08@K\x0c_X2M!{|3Z'~", '0yDb6}'), [19])
    def test_case_520(self):
        self.assertEqual(pattern_match('7`==^V3f.@a;[aQU@qicJ-t5\t4F@\n?|ojb04|ZB\x08|dyE\x0b|Du5|a/[/~] N=DT\rAj6]~$\x0btH9XB56cvnjeWN7', 'Aj6]'), [62])
    def test_case_521(self):
        self.assertEqual(pattern_match('SNI[Dt\x0c W^dTet+pmw\r#k$3F`W26k`<"&U|\x0bXL#vbA(n\x08\'XE6KU#(>$H#6i?-', "bA(n\x08'"), [40])
    def test_case_522(self):
        self.assertEqual(pattern_match('VX,R4:\x0c *R%("GGES*:P!~\x0bbsUym8Mqug]\x0cwI\rVAp(B# G>a}\x0bQgc\x08}a  4K]\'/IhGj[n9P*', 'j[n'), [66])
    def test_case_523(self):
        self.assertEqual(pattern_match('#4N]d"As!]+\x08=BmB6,ZXKNdci<wU<z6<TmX|#/\x0bJ?:.}{\\ \x0bIoz0-U9,z2f\t;GVR2a{}5~k"l24@4m', 'a{}5~k'), [65])
    def test_case_524(self):
        self.assertEqual(pattern_match('\'rR"Td\t><_wS~\tzUhl/ke\x0cN:N6T#fQK(p9tf@E1e}Q,H=!sRLJ7rc4AWMq\x0c[8t>\r1$8Y\x08xgExrQ8odT3V!_2MbmM', '\x0c[8t>'), [58])
    def test_case_525(self):
        self.assertEqual(pattern_match('Yj`Zrkd?@\x0cQ\rcN\'P?]pYLhZ9dfWf2F,"*#_Q26AB\x0c\rRMO` m50G\x0b*\ns4yUhCHlIZFF`Um(mu?M9nU-xT,m\'%?ho"=F3G_"h<9K(', '?]p'), [16])
    def test_case_526(self):
        self.assertEqual(pattern_match('`*_a$ATIg^-w@?,L}8s[u@zZ1o3eH\x0ce\\\'{dDZZ+fwa39DSbRl"kDNq&\x08Q_d8pfBK/7i/=io_.>\x0b~Dq9c^e\'_\'89', '39DSb'), [42])
    def test_case_527(self):
        self.assertEqual(pattern_match('pP6?JT}}0_,k.*wq##)m!7Y{pri5q\nvUV#Q?!JcI_}o"-+Li_A\x08^2v\tP3n#Tj^ZUplq#2yP/-E(', 'Uplq#'), [63])
    def test_case_528(self):
        self.assertEqual(pattern_match('4"p\x08xn1F*SG1\r|Se+U u,c>>c<-6hTT4F!+N"P,1)n\x081G2:=sR0Q.YH\n!', ')n\x081G2'), [40])
    def test_case_529(self):
        self.assertEqual(pattern_match('(j*[A\x0bQVo^U?z4J/|=!/_D`$|P@-7JL0)ur {pr;!/ysQa>QXl|[UPQ~JraVh\nBlCxe#5! "jR', 'a>QXl|'), [45])
    def test_case_530(self):
        self.assertEqual(pattern_match('Ck`*|,HklK@helEEiml+m}.84%9_9qtl0w58>G9q:he#4BQo$m}l<?weQuRs{fBCv,\x0c7VweeSBWDj\nm|_F~H&ZCSs', 'm}.8'), [20])
    def test_case_531(self):
        self.assertEqual(pattern_match('(i\x0cT|\x08`JsYtyImN7w/GfkLGnnX$FQHL"\'Fy">vebun\nnS%[\x084F?/0Q.UJ *Yfw&O:al{c\n\x0caaZ(hdx\x0c;8"LrIu)\x0b', 'QHL'), [28])
    def test_case_532(self):
        self.assertEqual(pattern_match(')!>C*XsY_uJo4"*0R[f#MWZNc\rOs2I`d\'Yf%2jwgaplJ i,jfmiHh', 'f#MWZN'), [18])
    def test_case_533(self):
        self.assertEqual(pattern_match('cCNFl~De4[uJk,>^jk>m\x0b@:1Wk*\x0cEZTu.[S\x0bNT$\\AZT`-V*ONX&@ys}"v(f\'g)EP@\x08[:B\r46F7UBk\x08ucXN/\nOeQGtN?!`OZAV', 'eQG'), [85])
    def test_case_534(self):
        self.assertEqual(pattern_match("Ej ]5FLf#QkWVYiev7hvchvVdiE=8yhQq'HWXY(e%q,p+4-\tL6;[@L,S{}=9+QVJ^xU\\0ln\rmz\\1!RA8R.3\x08\n:|1B", 'R.3\x08\n'), [80])
    def test_case_535(self):
        self.assertEqual(pattern_match(']Pnr^%O)@\thT,"{]`fwW=Vaai\x08hQ\t}\nc!X$"dh-ryVCy^\x0cfL(`wD/', '{]`fwW'), [14])
    def test_case_536(self):
        self.assertEqual(pattern_match('G/s0BJR2e/aF~Ctf"w_! 6Gv\n[anOvC04],^EGq,l\x0b JhtygET ^ww', '~Ctf"w'), [12])
    def test_case_537(self):
        self.assertEqual(pattern_match('DnG-0t4SdR%ekpge+r$M+y\r&\rCbk6[w8>Z3)A2K!K_#u?f\t$I\x0cV"Ek^PL0 ]@\x08Z7~88xxP\r2Z`0>af_vH`\x0c^l', '+y\r'), [20])
    def test_case_538(self):
        self.assertEqual(pattern_match('thF`tR)$S\x0b\tsL\x08 W\nelOa Ey\tf*"M!)v6MDzjG2<Xo>3z`y\\7W\\CRrp-`WnT0"3Z\x08{`5A`k*', '\\7W\\C'), [47])
    def test_case_539(self):
        self.assertEqual(pattern_match('LSjid=v>^fD Y/Zke_aJ?b3$\t&7w-HCyq(.LLf}tg*Rd^>ku#Fk\x0bA}9hKqJ_5ipvIDUcv+\\Q#;|saDy63L%Fz]:k3(.<b*:E}K', 'Q#;|'), [71])
    def test_case_540(self):
        self.assertEqual(pattern_match('u%iZ<K\'$e2[h(UalAa$JXT pK-jH`*5h#Knpw>O:/j"w}dMdGmD=t.~X#\rf>1\t?ck', '"w}'), [42])
    def test_case_541(self):
        self.assertEqual(pattern_match(')0Bvxo=n {^|JM`\r$ T\x08Vk$6Wd3w;\'\'(9.0.29\n/4-4DQQtm"8]\tb', '\r$ T\x08'), [15])
    def test_case_542(self):
        self.assertEqual(pattern_match("y0@h(Q: <0^(h1\\!dA6@ pupX%AV!'6(N,f&si\\ia\\Z{L3[6pb\x08M}ubG_3%PX-v&Pab", 'A6@'), [17])
    def test_case_543(self):
        self.assertEqual(pattern_match("Yl6+@5D@8Tiru\x0c6\x0br.GdF7Qf<X\x08Yv|>r/  >MFzw[-WTNJMM/^2k}+\r7&W&DQeB\x0czUK':l", 'ru\x0c6\x0br'), [11])
    def test_case_544(self):
        self.assertEqual(pattern_match('^5QWy_J8pi"d#*B<$\tDwR\x089n>on>=q7~(gY\tdOD#z-{\'Q{z\tS(g(72@A2K4\x0872l 7JW2za[i\x08^$E9<6xl&3.L5-/9f!', 'pi"d#*'), [8])
    def test_case_545(self):
        self.assertEqual(pattern_match('gg6T\x08\t:-q\x08c5.my_]O1KQ= fQ@=5r.|~\\[~/c=h)e`*/\nN9bAWW;IY_', '\x08c5.'), [9])
    def test_case_546(self):
        self.assertEqual(pattern_match('*y\x08>QsdIu?{_:^B%cYFe:fd)FE;*|MVuh8}vtBGwX$,bn:6i;WDe26bs^H!iy.&BON3yj^j8(HpcqQ-\n', 'N3y'), [65])
    def test_case_547(self):
        self.assertEqual(pattern_match("f.dx\x0cIK.2n1L+}KNx;PTh ^\x0b\\p-1K>-HDo:9A:Xj5PXg)+1G+x)IGJ\n\tJ{FP1?6<_U)s\x0cwQHuLE/!\r@8Il'{&8cHDuuR%8W\x0c7\x08", '\x0b\\p-'), [23])
    def test_case_548(self):
        self.assertEqual(pattern_match('a0cpEaV@2e)54>RqeQ}`z#9<aL(XA5>7L@Kgu=d":M\x0b0AHYgH\x0b"j[ g4sx\x08V<v\r.&iSh\tvAmOYg!2EUW~M+h5e%=+cVLS*\tD', 'v\r.&i'), [61])
    def test_case_549(self):
        self.assertEqual(pattern_match(':: _-vU|=9jX}s|l&:H]BkB*=&/\n`\r0Pf(l\tysL\x0cTXHAv;051}U', 'U|=9'), [6])
    def test_case_550(self):
        self.assertEqual(pattern_match('ov\nZS\rp\nHQsqrxO*Po<JmC<=\x0c\\CaN@AlixcjL~J|\x0ccm2z :BgX\\D\x0bq 2L?\t;f[|1\n\\T[V}I-)}{a.', 'I-)}{a'), [70])
    def test_case_551(self):
        self.assertEqual(pattern_match('/n%\x08j=cHHi1WFN@<e0l\x08pqVMSU;`FBOH_$%Ps/"c*V&@5#0+bX?,G}}\x0cvT=(N\x08j:B_[', 'i1WFN@'), [9])
    def test_case_552(self):
        self.assertEqual(pattern_match('h0@w 4{Ko>o{Q>oU4f-}"5wBoR,*,Sb~INT/DQR!953S`7\'0rR\x0c\x08;.[d+n0BTKc,2c\\BO[bKg\'H/bxR-<R=', 'c\\BO['), [65])
    def test_case_553(self):
        self.assertEqual(pattern_match('F#P"\\4Z3tw$<*N\'szH~yOq1!:WFD\x0cfS~t4Fa{czN7uKWZ]eS/=8g\t', 'uKW'), [41])
    def test_case_554(self):
        self.assertEqual(pattern_match('4(H$1la\x0bKWqA\tSxVz8WO?BrFImj[wujZwGnr-|q&yt*ZqOV17Q9+#bXQyuy4*hX1]VJIs\x0bj;$I=m*;|\\6\x0c-\x0807Ab"', '$1la\x0bK'), [3])
    def test_case_555(self):
        self.assertEqual(pattern_match("MMu%EPxC0*SRc~l+:6m{\r]E\x0cwI81\x0c!TQ)Xi\x0833<xD\x0c8*;/xj-?TP>PRcVZ1UvwqJW??qZs'E/o2<3\\2_3XY@\npTN0\t", 'Y@\n'), [82])
    def test_case_556(self):
        self.assertEqual(pattern_match('o=b;AZW.[\x0cG.Dw;Hfy)VNB)s5a-x#y:it@X;mYP11]0DtOavPi~\x0b@\x0c 67_qt|', '0Dt'), [42])
    def test_case_557(self):
        self.assertEqual(pattern_match("8vOQt[xjR'*{aFkaXM/<U=|LI*\\5maY\r2}U2&,ki\n:?A9I__@iXsv_Ug/BAe57af[5W,ak.Nn4mfnLN]KM,sR<-+0j5|{", '=|LI*'), [21])
    def test_case_558(self):
        self.assertEqual(pattern_match('x{v`gsb\tx\nYrtUt~Pr;\x08I%3*{B\'uT\n;]V"qlwT&TXD]-tI"w E\x0c\tCZt"j{1P}We9t/tV?9b\x0cvs"-b^6Qrw(\'', '{v`'), [1])
    def test_case_559(self):
        self.assertEqual(pattern_match('zbD9|h)"RG3j*O:STr1$8kM>].GIc$]{-ri\\AZkF4W^\'J22UG6.c', 'GIc$]'), [26])
    def test_case_560(self):
        self.assertEqual(pattern_match('l`x$o\t:B?|\th.|+9$S?Nv|E#v\x082]sN}Ak]^1gRr[sq@U"r!=ZQQ<2/AHOP)\x08>r]66o.iXK6p%D\x0b|,b1', 'P)\x08>r]'), [57])
    def test_case_561(self):
        self.assertEqual(pattern_match('~+\'8X-#N2n\x0b}|\x0cHux2]5\\(+FH.K.N\n\tvi@&<;(@(wfey6KkU6f\tt"9QHek\r(e(m#Ue-p<V>RZRPaJ*{bGlOe|M\x0b;/dt<Xx\rcCJx', 'x\rcCJx'), [93])
    def test_case_562(self):
        self.assertEqual(pattern_match("K_<g'c_O,E#y:(Cew= X567'=zot.m!RGe^Z*]ToOJ?\x08\\<HE{\tf(gHk}*iR*>}\nlW/C;L,eEt>>@aFfN\x0cz&z\r", '^Z*]T'), [34])
    def test_case_563(self):
        self.assertEqual(pattern_match('J,z"h\rC1Nzt9`XG*dE(E,P\\B\\{q^XjE?DF6<i*8%BGw[tOQe3Z<_p>\rJ%m&iI+K$Dde', 'tOQ'), [44])
    def test_case_564(self):
        self.assertEqual(pattern_match('URh`-r9md+w4\t\x0b_\x0bl1Y`cG:Die"2IQ;YOX3ekWZU#%Gx]sz\x0cK>;Y}wh5OFOI`;0 8mL!0f_Buw\nui_{]\'}{m3vDP*i-Nw.i6|', '{m3v'), [82])
    def test_case_565(self):
        self.assertEqual(pattern_match('FDBDnMceoIB>Y%B`0u=~MMLgjZ{Y\tvx2+[0bv#qIOV?.VW-yvjq,R66l\x0cLOca', '%B`'), [13])
    def test_case_566(self):
        self.assertEqual(pattern_match('y].p|,7X_\t\x085\\zNvl]^9LN,)/2[\rw\x08 \x08T$@|+_Yi"<Ih!H@P%SX6\x0cyd.`U', 'l]^9'), [16])
    def test_case_567(self):
        self.assertEqual(pattern_match("L|7c!&ufA\x0b~c(7zlZ])/z.lQ%7,\t'Qu8B]\r\x0cp!*%R%YF}3Y>>)#id35oCAg><),3}x7fc<1c_8\r\\Pv\nTEne;XB2$tSFL.\rId#", '7zlZ]'), [13])
    def test_case_568(self):
        self.assertEqual(pattern_match('.n1~P3c\x08\nkuj$M\t!\re+-p1^8A zz!/B |o[+f8vG1>f\n?aJ%bE\n\n\x08*FMQ}7gj/E:@-:Ny\\]_DTC8T-b7F\x08>b%', '/B '), [29])
    def test_case_569(self):
        self.assertEqual(pattern_match('"(~scKAJkQXs[$x\x0bH=/$-A5\x0cLn\x08-$\r`HYh_/bL&\x08f{d\x08@: )EPGV |Gr $mMIq[e!/:J7GNwz!!T>', '[$x\x0bH='), [12])
    def test_case_570(self):
        self.assertEqual(pattern_match("p/j\x08P+Ep4\x08&%`;x\rKa)u\nm>=yAf)\\k\t*\x0841L'eJ]J[u9|0yB0mJbu!", 'J]J[u'), [38])
    def test_case_571(self):
        self.assertEqual(pattern_match('@Z4P6LHISz+C\thbt\n\r,|`8Sc\n{hf&a~p$D,x_I1^7\rHx9wp5\tOcA,#_jQDJ"3!;F$4)\\&ViPg7A9)W7F=>~i', 'cA,#'), [50])
    def test_case_572(self):
        self.assertEqual(pattern_match('Ike oKmRo\n*3~b*T/AIB>\x08wQp*Q5AQcx-V/X2SgR`Juv9`O\\8=ohJ"-|kc+m=/*\\u`zUCy6!sP|', '`Juv'), [40])
    def test_case_573(self):
        self.assertEqual(pattern_match('s#y+{q#s"7\\Dv9ur\tgPFVqARY*%ikF[XwS:=(8"H|o+-iYz|)imi', 'S:=(8"'), [33])
    def test_case_574(self):
        self.assertEqual(pattern_match('!=:|r}\n>jvo5fY9n\x0ci\t7qO:r>H\x0cnBRz0F.w9(\t\\^W@ :@^])poj?AiaC#lda', '@^])p'), [44])
    def test_case_575(self):
        self.assertEqual(pattern_match('Qw^F\x0cd\r&za>==Q0hqv>xXQhSI\rJ]sI],mGoJ9yxb\rV"yjn!8I<7lx)48. t\x0by91jxm\x0c\nm$(&', 'SI\r'), [23])
    def test_case_576(self):
        self.assertEqual(pattern_match('aA1;\x0c@@Dn_p\nCbKr(Uk#t-\tkk!#{Pv+._@I6B<k\x08$\rH2r}zas;+}"7h`W,L`\td\':bI&>y{"Yc\tlM-PqZ)HaSa\\#LP', "`\td'"), [59])
    def test_case_577(self):
        self.assertEqual(pattern_match("g\n'B#3SS4$[P^(T%>]o?-(%`{0dI?f\treVw\x082uR7]xyj(E+VV;SR2ghCM`-GC-4\x0b5EG[BA/e2[Pfn6MFI+%[C\x08rJ", 'ghCM`'), [53])
    def test_case_578(self):
        self.assertEqual(pattern_match("@v-j'2C@fcNJl\tC_t^%\nPy7yi*eE0jmh9!JfT5Qx3\ne?UO5[2=nYiX]{tR X:h", '^%\nPy'), [17])
    def test_case_579(self):
        self.assertEqual(pattern_match('M>!g9i&AYxQCf9yKR!R0VmbaYl(9!,r}wNtp0J[Io\x0c,PJaQF\x0c1]Pw\\2&1', 'QF\x0c1'), [46])
    def test_case_580(self):
        self.assertEqual(pattern_match('r_t=@+uI=LxnHo@@5q2(\r-l?ihfZe\rQ=hI.<ON"\r)\x0c5Hwo?g#D;^9,(jZ,49?#[7hn{MH $*U{u70z4l', 'Hwo?g'), [43])
    def test_case_581(self):
        self.assertEqual(pattern_match("Q\x0b gTH+7rtU_B5d\x0c8\\Zvaf>W~?iR\t85A8(=v,Gkq$[8Zt('Z4Nb\x0c|K>l!rdNs!nv81.[I4d\\k?fa1xXP", '.[I4'), [66])
    def test_case_582(self):
        self.assertEqual(pattern_match('blm3rUV$kg5+\r[D!:|\t&4}1JFa38JK^lO58@";>{\'p5SiofPi\x0bf*m+ [0M&\x0c_/*$^U&i30nPEp<I\x0b\\tp', 'p<I\x0b\\t'), [73])
    def test_case_583(self):
        self.assertEqual(pattern_match('Wnz@Bwv\\KQb<&y49NYrE13Of)\tzg<RA<SlW \x0cx`WpW~U7WG:xy}*\x086P\n"CU@j-<Eh*6(\x0cj\\', 'nz@'), [1])
    def test_case_584(self):
        self.assertEqual(pattern_match('$\ncW0^Tl\\pQsToWl{*(6`]%7/Z]Kocm^i?b^_:P|hM7|,vRmKTP:z8 JbT-h:xM>\x0cQ!ez }l4\x0b6Au/;>\x0ciT.6M{N(_%~Qto|d\x08', '!ez'), [66])
    def test_case_585(self):
        self.assertEqual(pattern_match('=3w1=OrKc;5CqVT]b%K|aUH\nG)(M*5wB\t(Sr\n:Yb(8<uVJE@O\x08Z5V4*P<q!aVFZ{AgA', 'K|aUH\n'), [18])
    def test_case_586(self):
        self.assertEqual(pattern_match("av`6541#P4.vMwt^%9nU\x0cr$\n}-fe5HDq@a5iX\x0c')?ViC\x0bVcN|}NdJ\r(vD\tyIC.oQ\x08#zCZox\\=\r/I1.8ebd8-D'V\t", 'IC.o'), [59])
    def test_case_587(self):
        self.assertEqual(pattern_match('`~.{\nN~G+)f/LHz6\rr3UgBG>kc6GyFyHQJWQ"knU__Ga.S\t=YVkTUwGjIK\rw^ON\x0b)\rGSA.7LgO(\'2spTK@q\'&duP0Sn"p', 'BG>kc'), [21])
    def test_case_588(self):
        self.assertEqual(pattern_match('[56i]=<BTI a0Yq!l[cP0b|YmxNeYf$mh:D1Xr?pWml<;1:~`Bpq"<Q,%+Mv7oTH5lUoeXQ]Cq~E~$.#W$6idI\\\x0cF', '1:~`'), [45])
    def test_case_589(self):
        self.assertEqual(pattern_match('ML(A)neT=W/Crp)Zk>SLlUkW\n+h={z3M*.VbC)w`L_3f\t<\x08{W73<H\x0bAHR anXfQMD-~}hu>', 'MD-'), [63])
    def test_case_590(self):
        self.assertEqual(pattern_match(']xHA{;V;O!3Q[]yW+F{6\\icSV.Z\x08\r{",Ns]5#D8e$^y<cfWY@b\tmILm7fI8G\'}+|D+pD1V}#s;>3q-^%4\'`dIJC{C>4q\x0cZ<7qL!A', 'dIJC'), [83])
    def test_case_591(self):
        self.assertEqual(pattern_match("\x0bX5J0(P{6XzK|3/\x08p$=~x5Y@D[^?$OB9Kv%j%60I<Y`,*c)gDDFYuG=\\'wPW%Un<,;\\4M4AH(7Tp&9H$\naB9hA$.{N", ',*c)'), [43])
    def test_case_592(self):
        self.assertEqual(pattern_match('?v_-<d[=Yl8H_DccK{)g\x08S!\nBN67$/Kh"2gp|ej3e J??Te\nhnH-\x08STy.B\x0c', 'Kh"'), [30])
    def test_case_593(self):
        self.assertEqual(pattern_match('\x0bX!xg|kj~B$\nId\x0b\x0b\\]a%ZC^\x0b)}l:k#SSNVeybG$HdY~p\\#C$fi\n}KgFq_1uX(\rt', 'd\x0b\x0b\\]a'), [13])
    def test_case_594(self):
        self.assertEqual(pattern_match("j6dfwy\x0b#+l~+bjL+fR?iqZl6JWsA8hf\nz'7~b`G8Mx=B') 2\x0b.$^~l>tt=t>{-fJvq\x08\t OJK<0m_\\sRqr)|\x0cL/m\n^l=B{Bph", '~+bjL+'), [10])
    def test_case_595(self):
        self.assertEqual(pattern_match('sJK!7rHa$G\x0b`jy\x0bl^W7"7j9Qm\t\x08Z-8L?Vikey2e.IP??PP@r&&6=!X)8Mgllka+1\'JB?49\x0c`c#t', '^W7"7j'), [16])
    def test_case_596(self):
        self.assertEqual(pattern_match("L_1|]VZJ>p\\IzI.z6Pm \nDpC[OO'JmO`A<9\rZ0<#Yqu_l4Rk\x0bxC8[<tg+@\\lk!QH*,pER*']Z}$w11mx3u3DJ3qm:v2m", 'DJ3qm'), [83])
    def test_case_597(self):
        self.assertEqual(pattern_match(']R,pNV00gEl910*u)85^3k\x08o9c<";\x0b.>MG<A;}}PP+!Y!@mE7vdjmPnS9\tf\n5q\')\x082-\\rB+75', 'A;}}PP'), [35])
    def test_case_598(self):
        self.assertEqual(pattern_match('aph@!.aSy&q{/fF+z`,meg t,Ipi{_1\n\nB#ysj!h;/&d]DEVn|K\r$:7IT%#<qb\x0818p,hT\ntuVu,', 'F+z`,'), [14])
    def test_case_599(self):
        self.assertEqual(pattern_match(' -Ik]DK`y=\x0c^_.-w{F$:Qm.\r\rr"_DJ!<\x0c7@]4>2N\x0c&nw3vyGJi7=C.yCxK\x08S\x0b6,M~Iw2vXg\x086Sp)cZ[v\njcS?l=B~c', '2N\x0c'), [38])
    def test_case_600(self):
        self.assertEqual(pattern_match('S@;P`l1;w\x0bRUj/\r{)uSfgP)F[R~mnsTO#~\r_( \x0bBPt;Ozj]X/1I@S6m|FjH[Ub--}eC<)', 't;O'), [41])
    def test_case_601(self):
        self.assertEqual(pattern_match("+A&pAr!6S+P^[c9mEO_)z.LS(i[O 4TX|bU6Ze\nz`Sk{^U'(\nfu\ruMfA`MpU6$-J\\+=PAT=F", '4TX|b'), [29])
    def test_case_602(self):
        self.assertEqual(pattern_match(';7"x\x0b.]aL\\4,BOA;:Qk|N2iCBg<IZRA4FyQF8\x089\x0c,\'!y\t9:KOe2?cuch3\x0bDu5\rl4#<_  ;%\rW Y\nN([', '2iCBg<'), [21])
    def test_case_603(self):
        self.assertEqual(pattern_match("K;IW,'b~e><taLMG8oy\rU_.M+ibs95/wDiRIg~ Lzq1\x08ydM<|H5s]OB-Uk\r|/P9{Xoz~~$jNDT#e;O2B", 'M<|H5s'), [46])
    def test_case_604(self):
        self.assertEqual(pattern_match(']Rb\x0bSgJsr6wIs0EO4rpcA\\ mtVX jixGa&nz(}9k"6C,ngfnH/%tEgr)zK[oOqEE4Zg-=yqK\n%6/~?~#</F', 'tEg'), [51])
    def test_case_605(self):
        self.assertEqual(pattern_match('qzCXRVrS\t7(W]79,\x0c<Ph{5xgl6ZuMY2RprlS0nRnM@@84$w%\rh*,mJ1\x0b\x0b\tp5Q+a*18c9i;A`h`1Wz^q]', 'W]79,\x0c'), [11])
    def test_case_606(self):
        self.assertEqual(pattern_match('?eCa;:lx"kE/5EnRm*4d*(gm5<qTJ-n/WWVfL}G\x08*\x0cf\x0cM6x8tI:`[)E_,\\/E]P&2"8P', '6x8t'), [45])
    def test_case_607(self):
        self.assertEqual(pattern_match('\tJ/gKe\\>5@clm5%xWK;+\\(;KvAEu 5Nd\x0cphL%M;VOpT{3Ybt]27uH<"(PVg_M<\x083v?!tG5\x0bg:89VEH`k\x0bi:-0#h&\x0c*O', '?!tG'), [65])
    def test_case_608(self):
        self.assertEqual(pattern_match("]1xY_,txb`0W!<>'q!o\x0c(Gbj)2?GK}@`>lu\x08h0dZwG\r\x0c[SxLFRwQXG\t]\x08}tp|p;+['Y8f", ')2?G'), [24])
    def test_case_609(self):
        self.assertEqual(pattern_match('K0#sZ[@@rB//&\r(M_w)%\x0b$;71ki],\tW#q}RUn>z(E*>CD\r#8\x0bs0Ws?; 4l1]fBjOR8\x08B\\]U>y,I^@Lcb"ZYu\x0cjer20', ')%\x0b$'), [18])
    def test_case_610(self):
        self.assertEqual(pattern_match("\x0bgDl\x08!LulAX%OM.b1 W\tmeoBNdY#hr\x08qGbZi\\bj_%\rT@'n>c <:}\ntn;7\rf6[\t>q=zsNS/RQ\t`dGQ@rk(#;\x0b8\tny;k(#Gp\rzbb=", '\x08!Lul'), [4])
    def test_case_611(self):
        self.assertEqual(pattern_match('l(x;0jcUK9\x0bAzkU0g\x08XJD#6uk+P}=WRmE]<dJs7n+B&;mRYbC]\r~J,,X}fBdrhW~l~AQ;`x\x0bZ0q', 'W~l~AQ'), [62])
    def test_case_612(self):
        self.assertEqual(pattern_match('JR4\r~\'hnG\x0cHEw\x0c#f_!\ra&@B=3.Abu!t0- 57ADY6BW(*kH:I5g\x0bd"ZsfOE#T:5(67C|\'%T1=oG?UHy~N]\x08$', ':5(67'), [60])
    def test_case_613(self):
        self.assertEqual(pattern_match('qk?(+:j&FBH2y/\nwBpGzD FPVlC2m9k6X@hdC#%ee\rQKOrFtxOYlV\x0cf', 'wBpGzD'), [15])
    def test_case_614(self):
        self.assertEqual(pattern_match('n rpE-%|FLc#8Kfk\nEROdJyMQ)_ij|}6y <d}5|c"`%3ozpyHq\t#y8i', 'yMQ'), [22])
    def test_case_615(self):
        self.assertEqual(pattern_match('$\x0cXLL\r/A\x0bLYpm"nfJ:n(!e0(]-t.-Qhna[4])P?FPFh5G|FFU\x0coBM<|"bOC6wn9~&=fj\'Fw ', 'LL\r/A'), [3])
    def test_case_616(self):
        self.assertEqual(pattern_match("<QI_l84Ri|m`b]R2aPYP QNskj>{]_\x08;k1w*y'vp=kfWYu`\x08zH`v\r\x0c]i!HBMYgxLN=-!4", 'BMYg'), [58])
    def test_case_617(self):
        self.assertEqual(pattern_match('ArisEW?goEjGw(.\t\x08S\nb8u~K$PTLs\nm{e_H\n^Xn3*[O9}1)@^ ),T_CLuMZ;E\x0cGcToX]\\z~(V2^\\', 'W?g'), [5])
    def test_case_618(self):
        self.assertEqual(pattern_match('OC[H$G=/d@P1=F)$qp]Czv9_EAr\x0cXb\n3NkRr\x0cE\'\x08S~LpUD2{6;5i"a]Z&u\tfsy./eh', '1=F)'), [11])
    def test_case_619(self):
        self.assertEqual(pattern_match('NP.YnQiS\\RY>o55b6" PSM*^=\x0b5O<s TG/Q6zRPZWSvj5E5LXk#\\', '5E5LX'), [44])
    def test_case_620(self):
        self.assertEqual(pattern_match(",^=\n}\\} Io$M?(Z)WA.dtb.2vv=g'eS=B2Dp\tJo#\x08L*<i+|S>8(rEya39?+ xns6|l2/8j},/ahrAGA*35bM/W_K`F", 'j},/a'), [69])
    def test_case_621(self):
        self.assertEqual(pattern_match('N|\t ){J\x0b\n`LTcJP h~j+Oco,pHD\x0b\x08S&"l\\,`%iE_c7\x0b\x0bmE4&6mTI=A$Gs%2', '7\x0b\x0b'), [41])
    def test_case_622(self):
        self.assertEqual(pattern_match('l!\x0c&W]rk+ClvA)rG|4^J*E&g b2THbj\x08wm_M_qr.9r\x0bNbGdH{_y_KajT|\\', 'rk+Clv'), [6])
    def test_case_623(self):
        self.assertEqual(pattern_match('Bb.?X/_jOWV1hExO,fh7w*2qQVY\x08[BvL[Lu}5I\'?`>s`Hj/ZtsQOl}Nn(\x0bv+"=D7#)8`C<]=PT\x0c$)eq)F8!lkrq%or1s^RWa/+', 'VY\x08[Bv'), [25])
    def test_case_624(self):
        self.assertEqual(pattern_match('+,g2e"Ay~908-1Few{jfU6fVB%lMG f_%;6kw;CQ2S-=]8}7$q\'g,%\x0bLr8m0F', 'g2e'), [2])
    def test_case_625(self):
        self.assertEqual(pattern_match('\x0bJL [\t6>5pe`PXuhTy29<XHyk3W\n1wrlUUOq]rU[HW]!UzXn p[U\x08B?5u8@n7Q\x0c~~', 'U\x08B'), [51])
    def test_case_626(self):
        self.assertEqual(pattern_match('lN(,6~Ky)QixpR\x0b0$N%,\tB\n*I78Sy!Cy)Hcca>N[U1*OQ>f\n\x08AV*3Mtmz)\n0', 'y)Hcca'), [31])
    def test_case_627(self):
        self.assertEqual(pattern_match('v\x08U=f<2|)Qg39T|x\x0b?;DH<[Rx\n%U;E4D") y4LvB{6DTUSzpr], rB]C7\'%z>E1"yKpn\'<n%_o3uw1ZQD^6AD-awYh', ';E4D'), [28])
    def test_case_628(self):
        self.assertEqual(pattern_match('0vj}WC&"Nf1zi}/!<T7Ff1[fxE\x08\x0cRY3JY2Kf{:ScKzVSiA\x0cd5BgoX\'Ezi%\x0c', 'RY3'), [28])
    def test_case_629(self):
        self.assertEqual(pattern_match('8KetD8#{Tz4]`sjn}XD,YDE{j]C\\r*DsV`sR<[h\\:lHsq]t?+t\t!fe7ba81~B/;!$SAwu]?4p#BB`Uu(%t|-e_Qd;A%t4[\\a4O', '7ba81'), [54])
    def test_case_630(self):
        self.assertEqual(pattern_match('yks~ "98+^ES3\\k`HQ[2#h>IQHuYi`dY&-*g@)5@n]E\'=r]j>T#zVZxFmK#:~O#OvnD]xCTc2Ie[_eOw#uU^}t', 'Ie['), [73])
    def test_case_631(self):
        self.assertEqual(pattern_match('~T(fv<<Ce.\x0c"Yrric>ZwfRoL>!")R9SIpB/E0V$A~L\x0c\x0c4>oA?qS^mQ#=xhO^JK^#wXMqq 4!">A2Bh}JGJ1\x08q.', '.\x0c"'), [9])
    def test_case_632(self):
        self.assertEqual(pattern_match("co$]^Jq,Do`\x08Ka_\x0bhH#\r_\t)YZ#>MpJb0JNa6'[d9\x08nqdh\\oWbZxD7]!SJD-VDp2I|>s3;.-=n`c}eJ ", '\\oWbZx'), [45])
    def test_case_633(self):
        self.assertEqual(pattern_match('3scbg-*df\x0b<9Ydh0Ug\tR}-sVIR$#:\'AZ\rp2fVD"$~Bu[+m\'>\'p&GdDJ~\\WfZ=I,i5', 'DJ~\\'), [53])
    def test_case_634(self):
        self.assertEqual(pattern_match('/sq})RVl#u6CH.rrcz|#s4G&#3*Pptf^D2\\.A=yC^Rv_(IU$iBsN=5WI++%\tl9.\x0c)9W\n$C(hx2wpsc0DVhQW^8_[Vi(`,7o\x08^A[v', 'iBsN=5'), [48])
    def test_case_635(self):
        self.assertEqual(pattern_match('Yz[_GX*Wxj\r9 :!s<\x0b"1Cc/K\n\x0cM{\t_;1=w\x08cc;6@|\nBEg{Od5d&\x0b1-\x0b"\'}0pL8\tl!PlE|wcx_3Z~*%^oQ4f s2um', '\n\x0cM'), [24])
    def test_case_636(self):
        self.assertEqual(pattern_match(':l"O\tDh0LwEdil!dSnztVi~UB=hFs|4-YWtQ3D\nPTDI\t(~:LY?`\x0c~LPPIG\x0c0\\j?', 'Y?`\x0c~'), [48])
    def test_case_637(self):
        self.assertEqual(pattern_match('e> !\t_s)}\x0c}h}8\x0cQ<Am\t=JSRh&_6|zgK3miws\t\x0cj? f3/k//i!z)x~U\x0c~BRlci2ghk1d', 'BRlci2'), [57])
    def test_case_638(self):
        self.assertEqual(pattern_match('Dbfe}0IpXQ)D)4!oW\x0b)k\th[8q;[?89W7&}qX<%3!cUI,q?SSJjMYC3$KH\x0cpqJG.EaWt\t$UI$.=W', 'Q)D'), [9])
    def test_case_639(self):
        self.assertEqual(pattern_match("Zy]>PByJYBS,.(w5'IB-2b/[#g+mFM4HTj\x0c V6NyVMNP\rfc$d)F7s*zaGsZ3w!/*U)|ZBsTDQ[g#r\nffxZd5F4\\0|:T3doE1", 'zaGs'), [54])
    def test_case_640(self):
        self.assertEqual(pattern_match("gfueu\nZ'$/\rax]iVRV2.c4:Ht8@~ \nCEgB]ZNm:)^\\7ew{]~HOK`RJ]iX[", ' \nCE'), [28])
    def test_case_641(self):
        self.assertEqual(pattern_match('3a>+r\rjM]0uXo4`L8qOe:L5e Rr<\\h [<klXxNu6xhFP,P4>{\x0cwe$1EP=?zc%9\\.\\+q<41f06ve5GFDH', '>+r\rjM'), [2])
    def test_case_642(self):
        self.assertEqual(pattern_match('\rf<1\r[Yx+5>c;\x0cr%@\x0c[=bM\x08Vyj}}NBmSIQ^A\x08$_kH ,IC~HY^+Z~~~\\_/\x08\n!)IJ"i(5k.^9\x0cnH~P\x0cFL`VF ;Sd=91fCDdl', '!)IJ"'), [59])
    def test_case_643(self):
        self.assertEqual(pattern_match('pQZFm?R;Kcz fIRd@h\tXr$.>Vl3j?o|f\n .<M1)9v*\x0c\t?A6hQ 7v=_b', ';Kcz '), [7])
    def test_case_644(self):
        self.assertEqual(pattern_match('\t}__\'6.0i[~y\rb8o=ThC?}OE\t?i=TrYFx,5<6.vZ8([sYJb\x0c"l', 'x,5<6'), [32])
    def test_case_645(self):
        self.assertEqual(pattern_match('{MW)_}@UHB8E1nFJ8x%BOnbKkU?\r7TbL3Ej)]`{R1*`"E[,G?!T_h\t$\x0c1y;-W)\\3JA\x0c\'>*,*#fwM0}bq\x0c;J}', 'B8E1'), [9])
    def test_case_646(self):
        self.assertEqual(pattern_match('7QF^XxnEpxq;BPlMb2t\x08MxQQ|P+\'\r,f\x0c[GZqwQ$+poQA#\x0bq2GC7AwABCoD"f^2m:|U+?n\x0be1#jS?IWv%Av\nzVJw', '\r,f\x0c'), [28])
    def test_case_647(self):
        self.assertEqual(pattern_match("%VUu'dz4M]CWK#Mb$0\\)OCSoE\x0b7qZX@)[KzA=(N`hv,/[8Ub\ndYL?aj*kRDG", '7qZ'), [26])
    def test_case_648(self):
        self.assertEqual(pattern_match('GxQDg@Ow#ARUOlR@h![A bV(9UgBpId7^cJ\'Ji`{H~M-hCE;tSRgW8;\x08_an]\rP&{fSW9C [rWJ1j"faT<gPP P\tG\n\t', 'h!['), [16])
    def test_case_649(self):
        self.assertEqual(pattern_match('DUYe5nR(y%!@{Dj_\'[{*L{b^[*=#sBDXh#+pXI\'xF1\x08o\x0cWlclpNXB?t<[.!\\1!$@kaV\'I\x0b6B"\ty5O)ZIX@24~`', 'X@2'), [80])
    def test_case_650(self):
        self.assertEqual(pattern_match('rD]q^CO d>Yz],mnduVe6<PWRyfzkM/]&kSEr~H0YxPx1axGkzXH#2 Gumdq<a"=VvZw[Jy', '6<PW'), [20])
    def test_case_651(self):
        self.assertEqual(pattern_match('y%-Es`_J"7U1 cl.U(,Cp6:X;3^rE_Zg"c8_m|NC^6Iy|0m\'vu\x08-.p3jF*8 i}b!{x~,X', '|NC'), [37])
    def test_case_652(self):
        self.assertEqual(pattern_match('D\'"sC.c=|m#u=&zS1@TtL9/+Xd8z;*Z\x0btm@$*{4fw*QFxrdV[:G1Ut\n3!N4S\x0cr\x08lhzOzEm9YK{K', '\x0cr\x08lh'), [60])
    def test_case_653(self):
        self.assertEqual(pattern_match('K\\3H\\!OEBG1!BA9)uIr\n^`K\nx/I~:MED[ZjQM^\'\\uZOv/)\x0bXN/Y"I+@\x0c0\\?R;qr.Qx\'YlzL(<Y+`=w{wq>fjKJQ.:', 'MED[Z'), [29])
    def test_case_654(self):
        self.assertEqual(pattern_match('`k;*fKqZ`B3][l\x08h \rm,L\t:r\\-P^dE/k k0=0Q=p8S{}k3+:},hblDI}H&IP4FK7lHs%#b[@', ':},'), [47])
    def test_case_655(self):
        self.assertEqual(pattern_match(',FDN4iD\x0c|*v&_(46ZI(]N9_xd_64Q9y*h^GX^ul~-G}si]`aGOVw\x08C4~#jHK.@U', '9_x'), [21])
    def test_case_656(self):
        self.assertEqual(pattern_match("[-IJZ yS^v;~k'xy\x0bknu;'TPL+']r+S:D\t(4`;&XQR.Q~EFe'nek\ntPq#Fz*zx*d't+!f$c)e*8Mn\x08/<=xK.qU*7D]z[", ";'T"), [20])
    def test_case_657(self):
        self.assertEqual(pattern_match('a9V*k4srxOLr]dM\x08 TIb*O.(s5)+8n^+bRg3?`=|($E^FF@fQGc_`}~8>9ZWZ[mJwy)EH<Lf#._RI%# \\f7Ir@>,hl!(q3', 'M\x08 TI'), [14])
    def test_case_658(self):
        self.assertEqual(pattern_match('0=2Y]\n>*L^JXB9](\x0bSG^x48xkk\n,qRrvbh(yU_kUrH~h/K5\nE+?RwX{V_,P2', 'K5\n'), [45])
    def test_case_659(self):
        self.assertEqual(pattern_match("TVAHuAAa@715L3J-_d /KYJAr>vu\r\t$;Y+kOC}dtFKt4IHFnL,@nOOtQJ'uM7\r\r\n|R1]/1t,h8:=4Hl8'<", 'JAr>v'), [22])
    def test_case_660(self):
        self.assertEqual(pattern_match('T\n!i6>\'+<i+lYSR5/Os\n~gQ%d\x0c^+\x0ct*%8-39VgJ."*8 W:Sj%2;$f', ">'+<"), [5])
    def test_case_661(self):
        self.assertEqual(pattern_match('7#w]\x08MbP;FlW1:a\nW \x0cAITGE.l"["~QjsI\x0cl$vg/rjA&g\'(I::,\'dr\x0bmSCz},]`mbgr~M<+Ud!G`zG9\rECO]IIsfokSV!yC3?', '["~'), [27])
    def test_case_662(self):
        self.assertEqual(pattern_match(")0Khd0~u 9BYHt~Iqrn.22p(N~3b\tz+_'1V}\x08eR&B z|5\ngu@por8q|*&:wFwx_GT)yS_VvE'sn|&D:V%8", "+_'1V"), [30])
    def test_case_663(self):
        self.assertEqual(pattern_match("rnt~jH d\\5k9YWBEFN&N5(iB,.*Vv3m8@K\n6f5Zv L0m\r-2Z><|$]_5JQkgmexGzpW<WY`})S<'8yW\nz<3\n;UF2ayRL67!K$^", 't~jH'), [2])
    def test_case_664(self):
        self.assertEqual(pattern_match('vy0[G\'-*[s2\\t!~"\x0b"eSD]d7!UD$U_da\rf8\n4\x0cjK>\n^qJvEz\'eWDu1tV@.}aCZZ\t(o\n', '\n4\x0cjK'), [35])
    def test_case_665(self):
        self.assertEqual(pattern_match('g[iywBKR1{<}"J~%2fXd{\\s1\r_}("#RSu<"q[e{N\\;.{*`{8lIE$~S3q}t /!Rnk.\x0c>\na"kCtV1y$IY', 'R1{<'), [7])
    def test_case_666(self):
        self.assertEqual(pattern_match(')&aQD9\rrd.fI<Z]\x0bmPGY4+\rXFBa{iDaN\\7R\\a\x08EF\\l[Xt-K|b/p', 'D9\rr'), [4])
    def test_case_667(self):
        self.assertEqual(pattern_match('Nq\'4=51=_X0M!<W<WKwkH8`5ZC\'n<5sVV$Z1gy{1uC]Of^#j*3f[NT`\r\x0c(6;LP"c|me[J<JgYVzyI]/Qz', '1=_X'), [6])
    def test_case_668(self):
        self.assertEqual(pattern_match("#<PxkH8}Sd\\jc|DgoCBGQ6-Eb!k`e'ern\x0bHGB\t$56a{+|8pP>90}|_P<(5s", "`e'ern"), [27])
    def test_case_669(self):
        self.assertEqual(pattern_match('NzRP1(9<gM`*\n,65 {&o#gj4?G6Ix1e:smceCzd8^g\x0c\x08x\r/`-{am', 'mceC'), [33])
    def test_case_670(self):
        self.assertEqual(pattern_match('gr7\x08 hFp"f{6oYzIO~V\nV3tR\rkDowo%Y%t\x08/\';^ZW\x0ckamUV-aVc9@L\x08@|s0g~8Ypbe|f;C&;`*9Qj\nf{"YKM".', 'c9@'), [50])
    def test_case_671(self):
        self.assertEqual(pattern_match("pKA)^`B~cc'!b]Rb(+T[>\x08}{tG':pZK\rg\x0bFHM{4.Xlq:L5W<f{e3", "':pZK"), [26])
    def test_case_672(self):
        self.assertEqual(pattern_match('[\x0c\x0bmI#KL/]"X_6P\x0bM"%DIiiSZ7A$Wk1r"\n\nb6VB>RE\'MId"M#*=&,\\K\r{I9SfY\rx%KWM\n4>B57', '%KWM\n4'), [64])
    def test_case_673(self):
        self.assertEqual(pattern_match('Z=$<p{_v#&ltI"|KX-Two\x08xI58c5>\r}A.:ZPua+,j"]tEnmL/f<j\n6ll<,*%{pi}N', 'I58'), [23])
    def test_case_674(self):
        self.assertEqual(pattern_match('>K11Ps8wPCfgjz6~d^4\rbb|IP\r=[pull\rsnMT\nN-Ta/{m"on\\0$^_U', '-Ta/{'), [39])
    def test_case_675(self):
        self.assertEqual(pattern_match("0g,(f6-|2y&#r~F@|81S,i}y0+U%&=mn]|9JNsB:p;9470t+!ulS39)JVajJy1vbSO\rDD{Sgn)w\tRek\x08H<JCZ'?qvy%<nS", 'JVa'), [55])
    def test_case_676(self):
        self.assertEqual(pattern_match("1w0\x0bT.>-<\x0cT9d'46ly'eLd7'+$B1^_UM]?B=)Q_8laz\n'*}L2?%M:v}c3", "y'eL"), [17])
    def test_case_677(self):
        self.assertEqual(pattern_match("*7(H?<tk()+}?Sl_;W'=W:8^J:Yk^c@Kl }+XN/[#CMRR/gtU@2Aug*V)ZL\rm*%sIS|.qN  >9!&_iOb+T.aJ^6U", '<tk()'), [5])
    def test_case_678(self):
        self.assertEqual(pattern_match('%t<:2idY}hiALA<ki#0i_Rb\x0b2svSZq*OYQw-DGjuW<x3R[/&W1|KSzDO|\r@#/', 'Rb\x0b2sv'), [21])
    def test_case_679(self):
        self.assertEqual(pattern_match("$F{Z+lyl\r.H9VX8|@pAt2B8\rw9D)a7t5\\$w\ru3XR<Kl[}-4$A{>S\td4w'X;FAR_ZFPK3o|NZ7q4`O", '9D)a7t'), [25])
    def test_case_680(self):
        self.assertEqual(pattern_match('?2\nZc&ZKQ2 xp%xf$Cga\x0cM9NSEZ$ze "^MZJ\x0b M\x08wT_%r&t,,N4hr;&0F.X+jpLmA\x08M\r}lRa-WBhZ}-)\rOi\\q FIe', '\rOi\\q'), [80])
    def test_case_681(self):
        self.assertEqual(pattern_match("\x0cJ1-t\rT~c\tWPmx!;xSoTy8_}5ek$I :li\r8\nd%'oU~8GD~d;WR*8&xUj:nZ\tI_x3Q\x0c_=Er\\auz}Y4T8?R>}9Dk'H?#eA7^#>", 'y8_}5'), [20])
    def test_case_682(self):
        self.assertEqual(pattern_match("\x08Tn{Y|IU\x0bc|{AoQ,W'c2x,}9mmiHW%()#|rNmF_e~JDS^wnzfV\x083", 'nzfV\x083'), [46])
    def test_case_683(self):
        self.assertEqual(pattern_match("@|\\fh3c<0(1Yz1'1O&=ZMj(|@\ts3'^0S@WPWc@ZRVwi~lA\rSY3qXVbHCRjp`-u9Y)}Uz", 'u9Y)'), [61])
    def test_case_684(self):
        self.assertEqual(pattern_match('}X nH2N\x08f<"0\nvP>hq6"KD\n]aW]\'2 jl\x0b=loaJw]_!Ahs}H|#U!|"x8-4n3^S}_[g}.\tMq', '6"KD'), [18])
    def test_case_685(self):
        self.assertEqual(pattern_match('5\t.v)YadSW`V,\tO\'e\x0b\t!S\'TFALDlts+=\tC/Y&">5\\!L5 ,GAdlj"XzcyWeOq^nGL`C\tt', 'LDl'), [25])
    def test_case_686(self):
        self.assertEqual(pattern_match("y(WQ9$F4aj\x0cg8\x08^Hz\rDOls|7DjZ]gQq=9'\x08j*GsH:nj5YW@gg1ajlHAJ7J{5G\x08Umo!^", 'j*G'), [35])
    def test_case_687(self):
        self.assertEqual(pattern_match('LC/TvHIo~6\x0bZEsy[uSo<\'9?R\t_Es2cgY#wL\tt<:syw>}!/yZHu|a9lc0E\x0b"C\'lF`xGUEv!t', 'lc0E\x0b"'), [53])
    def test_case_688(self):
        self.assertEqual(pattern_match('OaB+ydoE"!\nG{\tde,>]\ns<uW\'Z\n{9)},\'8\\y&%Y;>aFe=\x0c4B\x0cSzu2g(FPKSOoD67Nb4`kw-x"3n$+w94c', 'B+ydoE'), [2])
    def test_case_689(self):
        self.assertEqual(pattern_match('fP5xn_CmVYMk 26T2kiP{&McQo/on||qWv4[\r([Ip%4mbZzj0Ufy|X4\x0cp)~C$OT0F.H0%\rN$P|', '0Ufy|'), [48])
    def test_case_690(self):
        self.assertEqual(pattern_match('^0Mg3\'w#>y/}|cN(iPEa|QFv[L=n4\\E?AS$"sQ3Bk:s7g-%Q]KDU/JzyE`89Rb', 'DU/Jzy'), [50])
    def test_case_691(self):
        self.assertEqual(pattern_match('\x0cJ>7C#m=\x08I{&0om%K"Q`bUM!/|=~X^VqVgxt|U1^1?KOC]hU\\B8b;er1\\$i#\x0c@&Yl[aae{F/W!5-.}:9!', '[aae{'), [65])
    def test_case_692(self):
        self.assertEqual(pattern_match('2I[=3`FrG!A?r,yPX&3.^_v!mW87zEnv@Lb|%:=,C<WpC\n~\x0b\\vBsIF\'"\x0cl', 'r,yP'), [12])
    def test_case_693(self):
        self.assertEqual(pattern_match('Q7pcS 41B]>me`q|\x08\'hT%9og,81"`{@TRA?FZ:E!Y`bn\t@G=I\\kUd$}G)wc)/2r\' #\rgwOF)t;S5~$YI;<CzB$7\n<Y))p#Be\x08H:', 'I;<'), [79])
    def test_case_694(self):
        self.assertEqual(pattern_match('CGN:j$X!C1HwU*(1L(s@Q3^v1\t!nT 8w@ofZ7*Z\\!LaId8:]>\n[OMD0W=+Hs', 'T 8w'), [28])
    def test_case_695(self):
        self.assertEqual(pattern_match('YAV\x0b#WPr##%KW.\x0c3_{8l3o\x08-?,>k4rT\tHVfj(/M"O\\_##\x0cOKKX+7fGM"6\'\x08.U/ `C\x08^-;aVZ,f<F{MRg:KL\x0c(\\)]', 'KW.'), [11])
    def test_case_696(self):
        self.assertEqual(pattern_match('E}\nLdtBI>=nhv|;" )pNcT<:kPz,B%m^BR}TauY":t)\x0b7q]*x"~42\x0b/[FADNB=F"R', 't)\x0b7q'), [41])
    def test_case_697(self):
        self.assertEqual(pattern_match("!4T-.\x0bu nWsBWGM)\\cQn569U2L8C'n(>>=\tnp{Xv1,c>FFPgb!u`&_xu*f\\R&ALqtO=sE\x0c?0SdYoid6J'ri+joE,/_i^/yC)@", '/_i^'), [88])
    def test_case_698(self):
        self.assertEqual(pattern_match('4x=]Fq.&jH6LY09_U)KAxLScY7I:b._*`C,K7<$mv_7NhOFii9}9Z7~-jfm^a>X1^"\nbx)t";Qf"=^o1PqAd>0o}7+~', '>X1'), [61])
    def test_case_699(self):
        self.assertEqual(pattern_match('{H#{A.\rA+F6[r92V8s\t8$H2+YzZIL~n\rKdN_]FMj`c4P_9srHB(~C%/ffP\n\x0c|98&F,F \x0bd93', 'A.\rA'), [4])
    def test_case_700(self):
        self.assertEqual(pattern_match("NM$]AG/FcO7|qrre/\rc,\x0bd\x0cA|/WReypU(v~2oe'dhLS );5fsZB\rZ}\x08S-lTR_4~u\tcJX9t8-hS", 'O7|q'), [9])
    def test_case_701(self):
        self.assertEqual(pattern_match('\x08uXGGpev."+{L`fb9}I4+zn#T_k7r3e^|V!ql&sNQ.anYfIJM\x08`4I5ffbn;p7r>\tTNMc3a8q\\', 'XGGpe'), [2])
    def test_case_702(self):
        self.assertEqual(pattern_match('t[XG{1[w7(1x/:}B@U\x0b1B=]YI^d6&\x08)?7\\.0zCX~=pl`XJgXBvXwct0`', '7\\.'), [32])
    def test_case_703(self):
        self.assertEqual(pattern_match("1oD|@:Om}PZcqX5C>1s'8S$jKUY-[0(J36F1~s$#S0C&xK=n)fB0UX+jYUd]MVg[cq,V\rdodLZ+`\\f$", '}PZ'), [8])
    def test_case_704(self):
        self.assertEqual(pattern_match(".cU|sUHO7 gA'r$q&4;@!{GYy;i-z_@je\x0b=r!e{E\x0cRcG,\t;}u6q24", 'G,\t'), [43])
    def test_case_705(self):
        self.assertEqual(pattern_match('18M\tA!\x08F\n sAIZ\n\t)v/W>|\\BDT7A+nQWnmABUbEb6N/?cQ \\0NU8\nB81<1?i9K;D!*FR', '\n sA'), [8])
    def test_case_706(self):
        self.assertEqual(pattern_match('on}m;PhjN[iT8\tIB!+>Z-wAhD\nH!XtUOAOo0?A}\x0b+m C#7:zS,b\\~Yb)Cn6d+L]L\t=z\r.>xoJ*9L', 'L\t=z'), [63])
    def test_case_707(self):
        self.assertEqual(pattern_match('<Es+6A\r\'I"Q\\\\5^!O,hI7uQeA}7\t2LEBl\'sLP|s=\x0czt<Rj\\=eo1oHP7~O!R\\-gQMa=Eqz0uii\n!\t', 'Rj\\'), [44])
    def test_case_708(self):
        self.assertEqual(pattern_match('D{?&c%{9&j)^r[\n\\\roTH^bJo>5ffq]*_r,_By3?>G\\}$i\nHgO][E#\x0cg>,)`5~g!y', 'q]*_r'), [28])
    def test_case_709(self):
        self.assertEqual(pattern_match(':m;#_qWp65P|`/X\'\x08%:&AC6apPZco]\x08{\n.R,A,|^fho-64u_Ow?U#e]I;\x0c\\:V_0=[x?9H8q)<=:cPPO-`\x0b`-7+Xd"<t@', 'co]\x08'), [27])
    def test_case_710(self):
        self.assertEqual(pattern_match('9&,\'s?M<HzG7a#(UgZECN6"\n^>o:!G|Z|ec4.Jcx0xzf>ZK,\'StFl\\F1EvA|gG3 .:V\rW8\x0b2ts^\r+W\x08=[mXx*7S)vR', '2ts^\r+'), [71])
    def test_case_711(self):
        self.assertEqual(pattern_match('\x0c\x08WeD<f+%rp+d/bh&*&K5"|AGx^T\x08bhL/sDOTo[1#)\rVI!rqohn\x0bBp2=1/d4Dp:T', 'K5"|A'), [19])
    def test_case_712(self):
        self.assertEqual(pattern_match('(VSd/E&J_b$fg>}vbgL7qF%8/-0jF$G"3U wnX_YpP\x08wve~Cb_6pjC6|G{\tt7y|WE_FC^=R!1f3|G_b|;(a38\t) 4>*\r&X,', 'pjC'), [51])
    def test_case_713(self):
        self.assertEqual(pattern_match('UVus\nB\x0cQ9\tRGEe{{>_Fi3+bPoJ?yDZPMwqY[UI892W=ZpZ\x08$/he.(cHp= kD&/r|\rWts#YXd@lrmq QJ', '892W='), [38])
    def test_case_714(self):
        self.assertEqual(pattern_match('4\t\t;\x0c9O8iwQ)<4"e~bi\rRyB7Dc$\rzP^)Hxc\t~i/W\x08tU*<U1:0nje_nz\r^1\x0b(UrRfMM)?|0yRW{`Km!Nio.-9d', '^)H'), [30])
    def test_case_715(self):
        self.assertEqual(pattern_match(')teL8mK;b-BO\x0cT\\a<\x0cPnmv \\C189X34-x(5*Inime6&C ]]AYC\x0bTT$2]@x$sGb6{[v%~:)F5{', 'TT$2]@'), [51])
    def test_case_716(self):
        self.assertEqual(pattern_match('OF2I~G)\nxY<?6D"pBw8#vi,Rd+p\x0b@{Bm9=;8Z\x0bwN[z>\x0cM$y `t5Bwv&T', '<?6D"'), [10])
    def test_case_717(self):
        self.assertEqual(pattern_match('K\r(\x0c\nF`#BpTd9kW%"L6IL\x08nt\x0ct-hP]5\np}`Fg+~\rBZ6BtJ\x0c;,\x0c,L+R(x31Lb*&nv%c$Zir*}u\x0bB\r[i~%\x0c]UvOXW7 |K`hy;HUU<\r', ' |K`hy'), [88])
    def test_case_718(self):
        self.assertEqual(pattern_match('@/1F6kR4%@W\n,o/+L,PCyS6FD"oP,H1aqx\r#\tA\x0bTDMIe-ANubm+c`~sqUR^7sX{J8oefM/t1$Fr&)P*U3{yzkt`SM', '8oefM'), [64])
    def test_case_719(self):
        self.assertEqual(pattern_match('\x087uv:4\n,>R@P1m9azX\rOF=>)?|+>Y9h[W9a+62vgJgEf\x0c]=~ZIK&fwoNxY`q*I', 'a+62v'), [34])
    def test_case_720(self):
        self.assertEqual(pattern_match('lqW&PJS\tp}?`s=m*`bA\rY[\rK,S>W\tr];~>K^\'O@3y"UB4H?T&/(``w<S3kO@[FEI\nN\x0by$k0]HQ\'\\e@{^s\ra+>^ UHUs15c', '<S3k'), [54])
    def test_case_721(self):
        self.assertEqual(pattern_match('\'=\tjPoo\x0cxcC\x0bX\x0c]I#=H&qgx!Jpw\n9\'\\rY&x;YK);|\x0cDInK>cyF"Y6]0:9m\'vO^aa:\\3qPD$lR7\'za;eA\rg%Q=\t\rKFdA7pt"?2j', ']I#=H&'), [14])
    def test_case_722(self):
        self.assertEqual(pattern_match('o=\x08MW|0\x0cpu(3&6%Nq!X\x0b? 8PV&&ilA+}3XT{R$+1la0b..I7xe,K\nEh}u:5', '{R$'), [35])
    def test_case_723(self):
        self.assertEqual(pattern_match('d;K,$#<\x0bY\t8\x0bhC:tr\tWibYx) 9\x0cRjC:Q\t=~$(F\x0bJt;|*.fZ0c0,"2\n', '8\x0bh'), [10])
    def test_case_724(self):
        self.assertEqual(pattern_match('R2>$9hv@a(bCUs]l<cK%fbYX!#cwqn)\'L\nb`[d`,+./-WpR[oY\x0c[>In8p_2"$?l]I]My.VZ\'NR\r),ew\x0cd\\@jB\n(*$jB', '!#cwq'), [24])
    def test_case_725(self):
        self.assertEqual(pattern_match('J(?g(vW>(2|{Ba7UhA"Ts4z}:TC4Qvh\tf{Qk*@~0dQ4?w$+HC$i(+|8k3Wn*vT3Ba8!', 'z}:T'), [22])
    def test_case_726(self):
        self.assertEqual(pattern_match("x`H0IWZgYQq38qn@,BT/wKjl^[<nf;Yzc?\\- #BP>g5(a\x08!{'JG0/-S, {Wq", '`H0'), [1])
    def test_case_727(self):
        self.assertEqual(pattern_match("%Ec(v1jR]Ej.i\x0bin5W{8*G\x0bM@ x(A-oxm\\`v2gXFLPNtX}y\rK-Tp#1 |s%4knd.AYbD\\^G#7~?<'F!:0,", '%4k'), [57])
    def test_case_728(self):
        self.assertEqual(pattern_match('+}VX&i&,)}2X:Dr>,\r\x08]/Sfa0iM]<H=K+FfA.(BJUUaT&N5)C0kYI\tVC7<l', 'C0kY'), [48])
    def test_case_729(self):
        self.assertEqual(pattern_match('sq3A/W\x0b`7Fg8hS|}O!9!m_1?\x08+vZY&E`rnSl9yi&/gW7W@nw\x08z"h^1cQ13/GcN@=', 'Sl9yi&'), [34])
    def test_case_730(self):
        self.assertEqual(pattern_match('"1ZzRW=q\x0cp->&4T6[@aI(C*/\'F-xroS(\nh e2Z21FY,{ed\x0cgd}7\nx\x08zH\tF$*YI ', '21FY,{'), [38])
    def test_case_731(self):
        self.assertEqual(pattern_match('^\\uh6o 0:Wkc\x0ct/h@b.yY8L><\'QQ2O2\n0iKShmL.>y!-\tcE8<p;\x0bQA"Bo;%sh|6!\r_[iBg;^', 'Y8L>'), [20])
    def test_case_732(self):
        self.assertEqual(pattern_match('b,\nmT!wn+z7J\x08\n\x0c#)eSBDX.@$mwd^>9?]J#M99k}7\x0cyy`6X>O^QWs.k<=-W?S\n)`R6cb%7W0k=3', '?]J#M'), [31])
    def test_case_733(self):
        self.assertEqual(pattern_match('u;Wrx8;%W-\\I\ruTciB#nEZ\x0b{-}5\x08pwL]*e!\x08)!\n`eM\\lUwH_92zu-ZW@@r;PQ9WY:#{,Wc]{@\n;\x0c1Nn\n`7%ilVp~\tp/t1Q:-[', '\x08)!\n'), [35])
    def test_case_734(self):
        self.assertEqual(pattern_match('s8PciQ5n(j-[QM=4n-$E*fCW"$9.utQh16YDnev_ 0vR|izE%Y\n', '[QM'), [11])
    def test_case_735(self):
        self.assertEqual(pattern_match('b-rMfA\x0b\x08wi@Su\t?I<@\'a2)g-GT-\x0brc6J3&W"@MJziqUk\tK6*.}WP{iKs]\ndo@o;?FPyd', 'c6J3'), [29])
    def test_case_736(self):
        self.assertEqual(pattern_match("M(J_dy[CjKbxh$~@&<GFs\n'D\x088<d->E^H_<:#w0M1( 7RXU4:Ap0>8W\tYR5^1LG*(&Q 'HLo,\\\x0bqe+G?", "Q 'HLo"), [66])
    def test_case_737(self):
        self.assertEqual(pattern_match('~/J"nxpKGyR$`lCZ0_\r2- NgaKz+7jy3LP_Kp :W\x0c<8\\v2f%0SQbC&MtOo(u<\x0c>g\'%r$7', 'R$`lCZ'), [10])
    def test_case_738(self):
        self.assertEqual(pattern_match('\x0b43Sy3}N%\\9\x0c!Jk=xb[Btv\x0c<Duu`Zbyt]>|\x08KYJZ+=v\\|13-Jv_\nJp6D|*`.NC}%<}vd&ju\\.P', '+=v'), [40])
    def test_case_739(self):
        self.assertEqual(pattern_match('eE,ZG(\x0c1Z;Q>h]mQ_:@Zg(;WV:#\x0bO3!uH3O.\x08#^&\nNt6\nOm\nr3.=%//X=(IUh,@uidI[\\_B.AI.7LnVvNa', ',@u'), [61])
    def test_case_740(self):
        self.assertEqual(pattern_match("RNACI9@~@BRxr_nObVE\x08rz@tI]qO(t]$&J:.\x0cL-)Qy&8(gr#$\\)u&l`*3'\\i\t+b,vfL", '\\)u&l`'), [49])
    def test_case_741(self):
        self.assertEqual(pattern_match(' T5<-hW+<b_\rgv<6%lJ)+\\?7ZPj(&FsVMxV`Pv/;<Hg>F\'L\twZ;GYDA\x0b<^C]@"DOb\\R\'', ')+\\?7Z'), [19])
    def test_case_742(self):
        self.assertEqual(pattern_match('Nb4h/dV:^gb4eFQ$vaY^L05wG^Lu AD pIg\x08_))L"e9\x0b(6(RSal.%,WTk;~8E=h<\t4,*aPM+?K\x08m,\x0bhG', '(RSal.'), [46])
    def test_case_743(self):
        self.assertEqual(pattern_match('h#Q\'#\'e!}Pq\\<J,xj\nu+t\\(;2\x0b\nY-2\rrtJ%bw+~5!BN\x0ct:V>4K`t=nM53y_L]}[|T6|N[_,t9]]+J&jm*cD;ukdBf&O"#W-', '~5!BN'), [38])
    def test_case_744(self):
        self.assertEqual(pattern_match('"WnO\nA__N@:c[f\x08EhR`X>$E,"%/cvx(SQ(~n8{nT+Vr5"@D3D;`E\x0bFGh2pD^x\\_4NY3T,\'FNww%*', 'N@:'), [8])
    def test_case_745(self):
        self.assertEqual(pattern_match('G\nip8O#"Fl-Wr\\FqEk{6\x08\x0b=+\x0b#7\r%dh`KY3uK]4bcwKs`\tN1&IF_,k8OJD@!z\'r/I-A)hB+LK', '8O#'), [4])
    def test_case_746(self):
        self.assertEqual(pattern_match('mgYfS!H3nio2_QX\r*C,|qG :Lo.{LyS#GXuq\n:rG]cqu5>h#X0]si$3?Am', 'Xuq'), [33])
    def test_case_747(self):
        self.assertEqual(pattern_match('*R:sW&P:^^KFcE8~>12VXV\t~t}$\'(M%) ,z3O8<e?<C3+rH>xQLrj1&*5`83Psm{84LO"tbA', 'R:sW&P'), [1])
    def test_case_748(self):
        self.assertEqual(pattern_match('n\\7VE(",Ug(yyj*A@,2#mI\\?8r\nq\x0cHL#to\\1-|x)/4]C $!LSgn/Ll)wgcT5', '\x0cHL#to'), [28])
    def test_case_749(self):
        self.assertEqual(pattern_match('m[Y&3\n~b~@>PvpJaIu|P!_S(&-m i\'MW.wZ&vDKyne^Xk/E41Wt,qTA [5Nv03V6u\x08Kh"a\tpwLmXk9r|^rqz@n)d', 'ne^Xk/'), [40])
    def test_case_750(self):
        self.assertEqual(pattern_match('Wv|"{%Ly\x0b1+[Algo\x08gZ?6Za`X(L\x0b\x08kl$\x0b/mcX^t7c\x0c~E1XV.NJ\x0cM~#k\r0_Rj>AC"<+.*%5T.Qm\r%`$k}={cf3aaE', 'j>AC"<'), [59])
    def test_case_751(self):
        self.assertEqual(pattern_match('2"dj("S6)3wmmRP"\x0bA7#P\tCl!?>7yT;~CO\x0bORo}4<\nkU}9JB0cYe~N~iA`v9q8Z`:o\r2?B,B]PuB(ia\rna(SM', '"\x0bA7#P'), [15])
    def test_case_752(self):
        self.assertEqual(pattern_match("`8Ap],7V;Z<Z@KuX[\x08(T=9/i<e\rV$+'=V16sW}EdO_FVn50~as\x08\n{@E93u:>H^hfMHb3kwxF\x0c?Hk!s*m|G}k", 'n50'), [44])
    def test_case_753(self):
        self.assertEqual(pattern_match('{nN6-qmT^?K05}0F8{V\x0br7pAMp$Nmg\\3Tz4P;%u3z&P\x0b%\t`zm%,', 'AMp$Nm'), [23])
    def test_case_754(self):
        self.assertEqual(pattern_match('~]H\\`vho@F=.\x08LxG;["l\'3Ae5W_?{\x0bc"^VOL"I5+Y\x0bC=;c%kb\'3uw\t0-\x0b5##2o', 'c"^VO'), [30])
    def test_case_755(self):
        self.assertEqual(pattern_match('l^W\n)s .0m"u#\r(WXK,n^{1DDFBoF9W(xG\tBG`!x*m$"\x0b\t\x0bW&R3\\X%2;vp', '\n)s .0'), [3])
    def test_case_756(self):
        self.assertEqual(pattern_match('p"`9cY^w+Mp"6*H<s\toLb\x08\x0czfS9KqlPpcgoDtQld5[>[)q7+;7{|H\x08\x08 l?iY\nK\x0c`kuuZLG,c3)J"\'{>\\', 'w+Mp"'), [7])
    def test_case_757(self):
        self.assertEqual(pattern_match('\x0c\rns^>/0?1Yr>gX1y@\nXESjxv[4+u;<pr^>Kjk\x0c;I\x0b#:c_3kI]', '>/0?'), [5])
    def test_case_758(self):
        self.assertEqual(pattern_match('kr~[0`=v]jy]^3.zrM\x0b^v?\r:FUu\nbSu[ZsB)T[mcP\r<c><98 RA6m', '.zrM\x0b'), [14])
    def test_case_759(self):
        self.assertEqual(pattern_match("V>L\\^<*AnoFa?EKw>&Mb44KYwMT\x08Z6qEy7C0rbZ's(\tV>yH4Nrg>\\yo1\x0bd\tk;q$6JMo+iVQ\n'td\r", 'H4Nrg>'), [46])
    def test_case_760(self):
        self.assertEqual(pattern_match('dD~0?mV%_3Qp;\x08J]Oy34$BFY`i]*[gs-.+12d9/\\&(fOC\x08w%jFX\n)r+$|"f\'\x08Ud1', 'FX\n'), [49])
    def test_case_761(self):
        self.assertEqual(pattern_match('-1ci,`c%L[Qj`P9\x0cLsfHSO~T\x0c5\x0c2]I`U$=oy_UzKw|ZO.0==0:N\x0cy<7ptqCZ"As2|{_@FRi1gnpp1;lr:P\\%\x0b:)@M{,6=', 'oy_UzK'), [34])
    def test_case_762(self):
        self.assertEqual(pattern_match('RD\n\'8cwr}t\x0b|1K%a\n*9Y\n^"#e-"y48>_{af%T@\x0c;\nO^<mr;]ADf/4}hlx\x0b(4#,M</<Ww(X* &wNuYO\x0c;E_=v-<', 'r;]ADf'), [45])
    def test_case_763(self):
        self.assertEqual(pattern_match(']\x08YT;is\n%$2Qr?9.<<1(CWmYdF\r\x08lkPxZ89Ky]oKQBLaj^IZ2YmvY(l\x0c\n)sn(DMZ\x0bt4dS,K\x0cmC\x0c]Z.!\x08UIL,.Dp', 't4d'), [65])
    def test_case_764(self):
        self.assertEqual(pattern_match('$pbI7!|poLU8"C#(kVy\x0bh\x0ct.E!2P$AE(,{o8]D-A~J9&P=Tp5FR\x0b6hj$=*)qyWpX/:mACr*D~lVAQ\n-@oM\x0bq}', '\x0ct.E!'), [21])
    def test_case_765(self):
        self.assertEqual(pattern_match('zn\'(0"\'BR<O"_k.8d\x0c==`JH\x08lvT!8/$[]sq6`G\t\x0bB4i|`apy\x0c-;\tMM-WEks9r~vB;dg\x08NVPNNFz.p)I#s.mV7|xBA\\fMu\x08+\x08XTR', '`JH'), [20])
    def test_case_766(self):
        self.assertEqual(pattern_match('Be:<~>:n)@ YQlS*k[0@0H+Y[Z:X2.|\x0bVUrF8\x0cF(b=tC;z\nO{jM"u:cCh\x087oR3.Ls<(4vi\x0bsMN?Lz3$W|Z', '[0@0H'), [17])
    def test_case_767(self):
        self.assertEqual(pattern_match("AQJN=#\\c2aLNv4Z<(wT$'@?%h1DIz['5+&G/h:@,4g+#\nx+\x0bn`dL0", "'5+&G"), [30])
    def test_case_768(self):
        self.assertEqual(pattern_match('rI>WlbJq!|^l6I("M2Q>]8z"S^Xc:O .k&\x0ctOd=R$E.>l}g2M%b2j;5X#\'\x08;Gqh\r.+dp\x0c=j/Q&{%}Z#LU', '2Q>]8'), [17])
    def test_case_769(self):
        self.assertEqual(pattern_match('_(ifZhl@M\x0bee\\&\rL$vfO961&\nk<v}YFE,Ui\'Jw[RL\\]Aw3w&sC3"oM|j3TL17V.%H*5`\x0c', 'vfO9'), [17])
    def test_case_770(self):
        self.assertEqual(pattern_match('W)xM;2$OH"u\\?4%\n5!^fnCgTWXi&d>.<!:)L~hOHH=\x0bOL+,Z2Q0gwi@H8Ci"cDZ92,4muw}q)', 'H"u\\'), [8])
    def test_case_771(self):
        self.assertEqual(pattern_match("QjT270U@QKW I4InX< \tHw\nkEAL+2iS!#X{.e[Nx;GqKKZGl'3u\t:g9SnI", '.e[Nx;'), [35])
    def test_case_772(self):
        self.assertEqual(pattern_match('-xF;\x0cEBnk+U0m%Y"lbQN{9&F!=5t\x0b5<=S.Hn\x0cxR{+EQq*]~\tB5\n\nG=B]{Aa*WQO`GI\'%5b:X#', '*]~\tB5'), [44])
    def test_case_773(self):
        self.assertEqual(pattern_match('\\os,TF[G[WLk&`*h[):+^;BkQQ?6HLLVN,T57V0! H|rP"*$#z\\2MJ-~iazYQN-XT;=K:\rr7bc{-', 'T57V0'), [34])
    def test_case_774(self):
        self.assertEqual(pattern_match('~1kJr(\x0c~qa\rWS^/cI\x08}i8s]@Z]l&#&\\K::(Q^eMdu}oQr):"P_u;)(a', '(Q^eMd'), [34])
    def test_case_775(self):
        self.assertEqual(pattern_match('qJ`p"g=/`$ZGqyADau;32^QZNe~16BUId?k`>b^Yg,jW6&SB\'f~6W', ',jW6&S'), [41])
    def test_case_776(self):
        self.assertEqual(pattern_match('/gt&+$\x0b&TO\tG&\\&x!3"fj(e\n6Th73`_F\tb/PJ<<-4+\n`&uI<Ew~NM:\rGPC3:vY9~I(kgr', '<Ew~'), [47])
    def test_case_777(self):
        self.assertEqual(pattern_match('mc,1/H^~l\th."+{`\'KaCAdD5WIQ&U[o&85t!I\nt+\x0cr0>`U,b8DxA?\tA4e\rg\r=I_HWxp,DP!\x08!+\r4\noE}{YM}fD{kvGO`{?Ur(', 'l\th.'), [8])
    def test_case_778(self):
        self.assertEqual(pattern_match('N+>O2d}"E3!r>\\.(PYzbAA2wr1bQ\nMK29/osh*hC"}B=tqfMTd%J^F~*jRoM:;D?NfdRR^>"^\x0b\x08\x0b!G6\rV\n te6y5', 'V\n t'), [80])
    def test_case_779(self):
        self.assertEqual(pattern_match("B\x08\t#f(v]`B<1[[+a58m&]s9}\x08}LnGmt3~t{hyx\t'O5?`bF~z!ewJwShn*%y,o$v$R,nZOJ'xv,R%KDW.mvU?", '+a58'), [14])
    def test_case_780(self):
        self.assertEqual(pattern_match('j,;b=\x08\x0c)sTR\x08DxqO,\'aZ9+pg]XU1j2K`pX\'(1!1bytj]_\rHVOG)\x0cW8y\\!?,W"AE7.^?VX\r\rCK6f', "pX'("), [32])
    def test_case_781(self):
        self.assertEqual(pattern_match(':yF!qYY\x0bd/g2t!7u6@9"d/\\cUGj9CK_m\'J6B<@QEm*>?*=_9x"b!V\x0cI', "m'J6"), [31])
    def test_case_782(self):
        self.assertEqual(pattern_match('%@\x08]7LQ4qrW7QVXyTxM{;Q/\x0bsSIhHX*Szzx;2oIc+\t3f\x0cl#.Zbyq~', '*Szz'), [30])
    def test_case_783(self):
        self.assertEqual(pattern_match('5NAuwze@[9%.q9AsrK\x0b\x0b\rK\x0cNaM?a\x084\rKKdN%Ky/LNt(\r}X)K`IXV^CJ', 'K\x0cNaM'), [21])
    def test_case_784(self):
        self.assertEqual(pattern_match('d vogevo&Ij8&)WxEn\nS\x0cO\x0c-2\rCYb+7G\tk[4{8H)<FmDiFYhp?U\'.3_^ RFL<\x0b\x084iC!Zc)d*$p"*N\'P@96F~S+<', "Yhp?U'"), [46])
    def test_case_785(self):
        self.assertEqual(pattern_match("o+K&r.iH_S.5+00N\n1\\cn+]o]H-2iCC0oiVWT&D{TT7j,~D>AX'=)\t+iUa|~0ol1]N\x0ckvOnJc7YeO82F<1\n3VymZ5`KO$'vZuc", '5+00N\n'), [11])
    def test_case_786(self):
        self.assertEqual(pattern_match('Dj|\nIB2(j?*Y  :!\\uWfpC-@k^4Bb?eFo^@{=]MnrwQuw:][SYqusj8z :W-}yJ\x0b\rT P94 v0)*`pN}]N', '?*Y  '), [9])
    def test_case_787(self):
        self.assertEqual(pattern_match('4#TKl9]JRXwFsW349Equ\\=+ouNn~\n|\t;-WWkcXm2<B\n\rn@JZ<8C,@=82_aoWxc-t.Ro5%:', '<B\n'), [40])
    def test_case_788(self):
        self.assertEqual(pattern_match('N@*["8+RcS @2u!Li_\x0bMn\\,\n!JoMjxn:7\t\\B2%ujS~?RS8Wb&$Q\ts.`&kH]q_<\'1rRPLKi}9Hx\x0b@|yX=F0PW', 'b&$Q\ts'), [47])
    def test_case_789(self):
        self.assertEqual(pattern_match(",I\\-t4Z'oq9H9qEUT*oHSm:#9RxiW614~\t:=yqugU=[\x0ckrg'@>!3\x0bD:`", '\\-t4Z'), [2])
    def test_case_790(self):
        self.assertEqual(pattern_match('C\r\'5%Ot\\+N~byFR*/tOzmA"CPknn+\'j2VXH!8Tq7Dv+L+q+b\t&{"\x0c-lyZ<<[\n*_Sl!(xAm\'DYEH|b6Ec9\tg', 'l!(xA'), [64])
    def test_case_791(self):
        self.assertEqual(pattern_match('0Er31d(t\n8A@Fd7SGfKDrE>"jq\x0c\x0b%jH\njkB!?0&xGG_NeQZ/!\'$JD"Jn{jHA\r%q0qi/RQy|Btb8-K', '!?0'), [35])
    def test_case_792(self):
        self.assertEqual(pattern_match('Aog#\x0br%!\x08UNc328GHcc/M]i;^VR:e rxsE\'(W\x0b98$V+V \x0cEo-j&5,w5C}"}\x0cD+JHh5y\r.lZn', ':e r'), [27])
    def test_case_793(self):
        self.assertEqual(pattern_match('j=aM?5sM}\x0b"-ID[RvowkQ/6AFmNSpfO"Z"k\'mMoE<8":.(}ABrz<b|&UWa+P#D\tHNJn-#\'n<.5:{<x_!x. $+ eA,|jQO=b', '"Z"k'), [31])
    def test_case_794(self):
        self.assertEqual(pattern_match('hLPSNd4`\rhrLV$N+Fp(it#Sl?l\';]kGw\'8#fDGp)I&n0~b<*rpX\\J-Y1>5n<{b$!U{{vufRL4+rWrrP YO;dT"A5e0(q pt+', ')I&n'), [39])
    def test_case_795(self):
        self.assertEqual(pattern_match('P!&y|"+\tQ4_::u{}\n\x0b3(i-J:Yr\x0b"dTC#Oua@\'zJL;iUU>t.):y{{F\',', '_::'), [10])
    def test_case_796(self):
        self.assertEqual(pattern_match('\rlY$y\rI@s\x0bHo;5b[u<5Z\r4p,^FD\nX\x0cK;HBr.\n3\n#\x08y0OL\x0b_W&\\7', '\x0bHo;5'), [9])
    def test_case_797(self):
        self.assertEqual(pattern_match('r3#i?UH*0\x08Uh\r8\x0b;#F\x0cq*w=zjA~P]#~tU6d+o\n\x08|FI:tu~u\x0bK\x0c*EU.Mi1US*F(sf8%,G5Gz" pCJ\x08\x08"\x0bs', 'i1US'), [55])
    def test_case_798(self):
        self.assertEqual(pattern_match('_L`t~_B3p\'T?g>:7:8GZhHc:SP\tK-/%0#daO9 vqPi-aw6g7*(X$x\'"k]!3)7a{EV@\nS+eq}7\\05o\\ kh0{51GV=mcS', '#daO9'), [32])
    def test_case_799(self):
        self.assertEqual(pattern_match('{hVRh>QY{jp2AIX_ 0wX87 o@d~AE.E59D>W4l=a!\x08p{s0nOO:p6\t6#X', 'nOO:'), [46])
    def test_case_800(self):
        self.assertEqual(pattern_match('79.$@;_V0M;Pa814C+\x0bxvu\x08\x0b@Wy;4$=GxY{,ZS>~VA]+fifjQf`bU}t\x0cm\t-~>tNWg R=tEeV}aWM?g1Gk:N<:Z1@juv3Qs', '~VA]+f'), [39])
    def test_case_801(self):
        self.assertEqual(pattern_match('vIu`NT%skF*YlyK2l\nOREwM@qZqt-1cmOA|hKpTz@&QOf2KWFB.t,A\x0b3^q@gsisw<|8\x08c4HCGei Cl$Y,11um5It$k\\\rNC', '%skF*'), [6])
    def test_case_802(self):
        self.assertEqual(pattern_match('rlxr/>#K<,l4\x08$Iz&8jDwBy5?G!3Pfc\x0cMB57UtL\x08Xv#z\nTB"nKJ3F)-(z}AhfS8Lpnd,7dHE?!@X`XB,MNi*L', '4\x08$Iz'), [11])
    def test_case_803(self):
        self.assertEqual(pattern_match('d^B6BodT\'/\\{i^OK=\x0b|y\'\\6~O>:;X|bGC<GVLnT\\#\'DFJ\t="rz=HQ@e4@G', 'd^B6B'), [0])
    def test_case_804(self):
        self.assertEqual(pattern_match('%m}Q\x08e*]<XNeE"wGKl.A)Rg{(Ip6#F*\'vZ!\t?CtMC#\x0b6Z+]\tMU<"6C;<8d>', '<XN'), [8])
    def test_case_805(self):
        self.assertEqual(pattern_match('_MQ_Jk+9+[5:i0~F<\x0bT*4ZDWYb.$w<(^G`+)),\x0cs$(#\x0bI\x08@MM@m"^', ',\x0cs'), [37])
    def test_case_806(self):
        self.assertEqual(pattern_match("'(ut(}\x08yYRmI4\tO_[7qaIL1$Sv*\r]\x0b'}gD853-N{r$_b!8d)\\#\ri\x08@\x0ceKNH9CT=[3%8\x0b e;w&ODt\\", 'mI4\tO_'), [10])
    def test_case_807(self):
        self.assertEqual(pattern_match('$QqP/khyN<X~\'2HnY9\tW*%OSh USKFsv9jFqa6C>*J\x0c?nCnQxATXxx, \r=m"ETwTf>Y$0V(\tG}#JQ\\ RO&D0k,&[vNY\r8\nc\x08.3N', 'sv9j'), [30])
    def test_case_808(self):
        self.assertEqual(pattern_match(' %RgKc}@vr(Q=|.$zG|\\JCxO%ZeVcG@SO0X%.-mSxd+5z_m1LpT5XJ[P', 'z_m1'), [44])
    def test_case_809(self):
        self.assertEqual(pattern_match('fDR1Es\\StbJg! :4>uA TmrdLho4- G}w~s`\tPXMpZ>f|=uIW|{s#n6E[r\x08', 'rdLho4'), [22])
    def test_case_810(self):
        self.assertEqual(pattern_match('1c9!-R.NY4$\x0c8\r2a sb01+@<TX x+%aJk:Ud.SrSi1\\[61GH{p\\\x0c:', 'NY4'), [7])
    def test_case_811(self):
        self.assertEqual(pattern_match('0e;\n<\tQZm~e$17w<\x08LZP5Hg|];\x0cYfP j\\.Bust65M8Qu;U]0z=EI"lR7^', '|];\x0cY'), [23])
    def test_case_812(self):
        self.assertEqual(pattern_match('~k?u[u{/8qDil669Uc TRQM1n,z^IG`2<Wt#F3o3!_C\x0c=LJ|JBCl&*Ju"u+"J<e4/4~/B"fvxrb%<VOyqdltiP|eL', 'C\x0c='), [42])
    def test_case_813(self):
        self.assertEqual(pattern_match('@$vQ2Gw*5LiS$<fA|"f9o|^FW\ts[llm#a#i\x0c}J|P}f[/iD7C2f=t*ijZ', '[llm#'), [27])
    def test_case_814(self):
        self.assertEqual(pattern_match("-dRG#:9NPmBNb&k%h^xW>Q/Bx@!L(;;%Uj'n,6]@\\nCcSY!Ss +GR=vqf", "j'n,"), [33])
    def test_case_815(self):
        self.assertEqual(pattern_match('Se7*(gY\n[:lQ$=J9eh<[Mq\rV&OPy}3ZVL[JKiAsb>VgX(3KBo6Fbu%)JlT]/gmF"CGrPJ9h&3!|f}', 'JKi'), [34])
    def test_case_816(self):
        self.assertEqual(pattern_match('\txCx>6+>%bYW~Re{[ybcfV46N0"WT\ts8\x08W.nS"9,K\'L^OO)}`X`\'=%w y<1F6.&+(H', 'O)}'), [45])
    def test_case_817(self):
        self.assertEqual(pattern_match('\x0c)ns1m>Tr^J<fd$LH\'kO -I3~rL)XO"kd{#DLqQ%ZNQ_@rD]G,}||.1f;Gm,2U1.^2vdYUS\x0c\\xzp{5\\5,', 'J<f'), [10])
    def test_case_818(self):
        self.assertEqual(pattern_match('n\rkK"/~m,N\'*YynXnO&Msb\x08"P-c4AvO]lq7kqFN1)RVS\x0bZ/X|\'*nK3D#d=6<nx#)3Z1Ma[_:s109QtQ,s;rjstmRdn+\n}[', 'n\rk'), [0])
    def test_case_819(self):
        self.assertEqual(pattern_match('6q&u(%f}6YY|9wk:\x0cW S+-CBK>/<6OyR>8C?;<:/i^fw575g,*[vR#_efqReJG$m%\\rtOnu^uT', 'wk:'), [13])
    def test_case_820(self):
        self.assertEqual(pattern_match('{LOW1d-P6zEgAUj\td?>X0;<b"6b_4GpJW\'#Lkyvk)Aji-~0@YBZQX%YM{a\t_r."Lg@!.?sWg7-CF^`Rl7~%()(\'V*=Y5^\\!5dI(E', 'X0;'), [19])
    def test_case_821(self):
        self.assertEqual(pattern_match('BIjc&`p)5l=]z*HxQ@d=\tt@Y]Wh~z+}[9\x0c;Jh9:jI{>Kdgm2tDsIQ\\UO1$b:l,qBaCLaqZ9l', 'O1$b'), [55])
    def test_case_822(self):
        self.assertEqual(pattern_match("UF43K6qAsMLp^}&'??MW> 1~\x08 +vs!L.aD\x0b?%44:\\l9 vq~#P?>5j1E*@+Y3yaMH),r|s2Jto8y^tds<{\tG|8T;b8gryil7yqiF", '8gr'), [88])
    def test_case_823(self):
        self.assertEqual(pattern_match("X`vduRFx-?y[G26|)ghx'KN%@79H&6O]`\x089!Hlp_3j4U2u_&sWJ=?ks", 'lp_3j'), [37])
    def test_case_824(self):
        self.assertEqual(pattern_match('_ZfDE;.v>-<DYz[]c[s"o\nBI\x08nA]M;:\'%@mq;zS|Es"kYR(ZyGh&S\rt^-&A3XaO-]gh9 C!>$9^|/*_mE\rA2,A"k!84#`bm', ']M;'), [27])
    def test_case_825(self):
        self.assertEqual(pattern_match('8><VuclV0*3s{-G%h-HJ,6f&j!S:;]W &%mX>r\x08PX<,|bRP O{sX\n\x0b5MQNx\x0bRW\x0b}:A8Ab\x0b`[hhuZ7jQ', 'b\x0b`['), [68])
    def test_case_826(self):
        self.assertEqual(pattern_match('fp\tt>Rl~%2J\t1Nab\rkbNU{8Xq6luz?y*}9l\\!kDZ\\9Ne^pVbe:ONj', 'be:'), [47])
    def test_case_827(self):
        self.assertEqual(pattern_match('M`"\x0c.x{N@5-\x08I3_tP>k\t.\x08.6~t9;$\t=d+R <N\x0b|H)iV{A\x0c@ h(9W7pavveB_t5Ot19fa!\\Rc\x0b8e1KOlwdt@$WP?7U[vXZ@"QU', '5-\x08I'), [9])
    def test_case_828(self):
        self.assertEqual(pattern_match('uxO.2^ /6j\x0c2xV&l%fI\x0cjz{=\x0c;*\x0cV~f1L[f\nA}qFHSv2;14HONQI!Y;h-;y7qS~', ' /6'), [6])
    def test_case_829(self):
        self.assertEqual(pattern_match('wzRrHxe#bhXg4<3}x]6FV GgQ+)qMkCR/FF=U)v\tC%%":>kF "`_@e\'/eO9VgJeKO2`_|u2', 'VgJeKO'), [59])
    def test_case_830(self):
        self.assertEqual(pattern_match("=C9IZ2\x0b{ItbjJ\trG%&mhvnuWO<\tD/'IHf%(H1HKcvnIogPfV}='", "/'I"), [28])
    def test_case_831(self):
        self.assertEqual(pattern_match(',\x0c\'g]01a\niBXRuW=!\t[Q=}\x082\x08uWBD:k"9$RfC,jBdtl\t(t|0{"-t(0Hve[l/gb\'z', 'Hve[l/'), [54])
    def test_case_832(self):
        self.assertEqual(pattern_match('/F/m0edJ?3oo|g&QnbNp\t3X:\nngl,s`GfwF!ev(9}tKo;&2@\\hl', '/F/'), [0])
    def test_case_833(self):
        self.assertEqual(pattern_match("1\tpS@L|v3A=}Ie6f5A\x0c)da?I%#_Lr8-7)I29't`vVVc-d:&h\t)R31!FM*r<cB#T\\=+py?l|.SJ", 'f5A\x0c)d'), [15])
    def test_case_834(self):
        self.assertEqual(pattern_match('%*?eF5uH1pF\x08KuqIe^\'E&%S|h"Q.qB$1i:v~S3=tQ\rkh\x0bAwSb=|6b]emgda|I$9r-NIF', '1pF\x08'), [8])
    def test_case_835(self):
        self.assertEqual(pattern_match('s\':Q,#]9Ba(#/[[vX"j/ykMg(|J<6qu8/B\t<W^{2SWYJ*Vg]m,^Pi J#F)c=\tW?-\x0cj#R%JF5\x0cS>\t\r*z\tsgwVMj?@@?\'?', '%JF5\x0c'), [68])
    def test_case_836(self):
        self.assertEqual(pattern_match('Ey")uIn/l>c;88r)\rcuIg#G8O2+/|zp\x08C0^?\r_4\nR>{:\x0bA\'O5DuMTs,*`hDsZRgyPkB){|52;3Hb:I48xSo\x0c+P|Lz\r\rg\x0b383s', 'P|Lz\r'), [85])
    def test_case_837(self):
        self.assertEqual(pattern_match('}#d<b_I8r_&FyC6:/i`_))9Wll>d\x08cB[?gZ_R|W"?:irGpC^_#M;|s:=\x08~ou3i}>s\x0c3\x0cQ=YkW<I#l+Z!7-z*0V\x08Hf8}d', '|s:='), [52])
    def test_case_838(self):
        self.assertEqual(pattern_match('=@d%]Jq34,{%N{+ iemQb} )]9hhww;HpkA3o|68(4_}{Tbr-\rr|oO<CYM8LH5T2Y+*La{w/-f9)7Cq=ud& 7twh', 'r-\rr|o'), [47])
    def test_case_839(self):
        self.assertEqual(pattern_match('?">ve<>lE4{GtRQaN.Jb+pqwaq!nKCJ[]t&d8T\x080S}sh:CU]\x0blQwTsU;o?q\rc-\'YKR0cYb2s`vp3!UA@26?ns[:O~jn]$r@CsjD', 'h:CU]\x0b'), [43])
    def test_case_840(self):
        self.assertEqual(pattern_match('Ho##[F(sB;1!OVlr7-YZ`p]Rr;<{QG*\tatIt=2,K\tPV"c-]vNH|*h\x08HD.\x0cwN9#sS<MV</iEI.#+0&kw:=kZbHfi,P', 't=2,K'), [35])
    def test_case_841(self):
        self.assertEqual(pattern_match("#8)qT,(]\x08hw##'jYa:/\txNAD!O_%G\\^,zo!dF3GyILsS2^\x08t9)Pp6tadKtPAIa[A`*", '9)Pp'), [48])
    def test_case_842(self):
        self.assertEqual(pattern_match('`:CCE$)_z{U|3/]VH~oY_K}"*J\\S}\x0c2h^dEb[umbg\nQGh5%e26#8x*d2qe=Rm{H6~iLj"7Huv[#', 'Y_K}"'), [19])
    def test_case_843(self):
        self.assertEqual(pattern_match('oD.6\x0b\rK\rLLPY6dQ\x08fa\nNl2LbpfdSS\x087IoI$tw>KMviP\rWeg?YNMM,6X<4eQJ?nH"ONherg;b6za\x08AG:`\\50ej!$|D0S)p\r.H15=h', 'bpfd'), [23])
    def test_case_844(self):
        self.assertEqual(pattern_match('j26=E`+fDEOE\x0b}\nCHp&w^>dw{gX5}Rgl5^=k\'})H!r[JQN;B[2`Zo\x0cqy-\x0c8bQ"# f', '!r[J'), [40])
    def test_case_845(self):
        self.assertEqual(pattern_match('Sfq s^m37Gxgpifqk3eu?^\x0cU/1\r=%m0(B/KZ s8@y3enXx(zKxou=sIN$=>NzL\r/\x08\rxYREJz"\x08qvq6S8skH\\_+UI7-.', '/KZ s8'), [33])
    def test_case_846(self):
        self.assertEqual(pattern_match('lTV?|z"d?kg8\x08a) y\x08\rt}PNSDw\\zyRM;k,b\n\x08I$p(?`?*u"Jf1\x0bNd(OPb14C<;W46\t3,.B\x08byv+\'eM:', 'a) '), [13])
    def test_case_847(self):
        self.assertEqual(pattern_match("4W |&J<\\PC(NEL&rkw84X8<UnCzKb\x0b?'Uv=kmVi&zD +}bl\x0c~WcK", '}bl\x0c~W'), [44])
    def test_case_848(self):
        self.assertEqual(pattern_match('BRGWK3sB0QM*hgJW\x0b~f\x08\\(PqI:9U^"<Hqj"*R?V;X~D\tbl@<]PA:)H|\r" U847>Tl8~!G2@\nCky=hn"g\n', '@<]PA:'), [46])
    def test_case_849(self):
        self.assertEqual(pattern_match('\x0820)`Ol[nN[;^c\x0c[:tgE>mpbqSo~!nX1.P8*B0\tM\rIE.R$\nt?.tDtE5Gz', 'mpbq'), [21])
    def test_case_850(self):
        self.assertEqual(pattern_match("Ve#wLJEv){\x0bA\nJTt^0?qfy(xh0z>>\x0bTA\x08\tTxlkw<\\?\x0cv~t<VZGf'c[2wj\n*(sCa\nc2L]AG\x0ciMS_VR+'ky28vJ8rn+6.n->Ve", 'VR+'), [75])
    def test_case_851(self):
        self.assertEqual(pattern_match('a%2ZOY2OPkRh5:q9~*DmIgg~~;h& |<dWC{p?:+Sv\t0db9D[TD.sI;\x0cc4Lxw\nus\rY|_$chIIZMT(T{z[Y.U\x0c\nJd[()', '9D[TD'), [45])
    def test_case_852(self):
        self.assertEqual(pattern_match("mW\x0cfTM(GIYcG-\x0bqLmBVM!m'T{@rfP:r7S\x08nzm )Tq|^-q Ivw|;\rJ@Z\t<|<", 'zm )Tq'), [35])
    def test_case_853(self):
        self.assertEqual(pattern_match("aqmL]{BCw4Ns(D\n=\t'T>^a:I87Njx\x0cT)lP(~])u- !'',a'*)oQ0", ")u- !'"), [37])
    def test_case_854(self):
        self.assertEqual(pattern_match("u_lOZ}n}\\_mSd{J>Pl\x0c0RUYA\\@\r[5+`ON'agdL\n,0D\x0c\n\x08y(NZRsJ\x08`\t/LPHqDQheetUc?k|M5\x08{iTjf&a/PJVFw{t'?G8,Q5S", 'f&a/P'), [78])
    def test_case_855(self):
        self.assertEqual(pattern_match('geFj52}\nYyr$$\\^PF;b?Xlt6DfbB|l\'\\u*$\'2zed6NK9arf,(Bg2e\x0c&lc@i=l>{OS0-\x0bzI*+&]cnZM]l9"4ta]', '?Xlt6D'), [19])
    def test_case_856(self):
        self.assertEqual(pattern_match(")Aa+9JLHO@D3]ElC$'\x08-%VlM\tTfKs10fOT7~^q=`GIj85NPfyixdj<\nK@c#S&/-wp\x0c~HBlIIF(%7i.w(\x08P\x08{", '~HBlI'), [66])
    def test_case_857(self):
        self.assertEqual(pattern_match(')|m\\{\'&$Z,~]/J|wmlU$"mal6QkcO;N+= Fy;\n5zW(\rx[&U;qCDmd}>5[@StuK&U[t4\x0bZ=<I\\JHt1Z', ';N+= F'), [29])
    def test_case_858(self):
        self.assertEqual(pattern_match('8Mglf=S9mJ ej."c9I16PtNVGVV\x0cqTD {;Ie}!amET\n>Ez>pBW~gr4%@85% 8 v^UaWOG<2.f4m?\\"BEAX8!i9O@{', 'VGV'), [23])
    def test_case_859(self):
        self.assertEqual(pattern_match('pz\'^dwq1"\x0ch\'5@ADcP)/.jrjs4A`j*nS\\F$O-UV\x0bwxe\x0c_=~sl@w', ')/.jrj'), [18])
    def test_case_860(self):
        self.assertEqual(pattern_match("kd2r1z<eu'\x0cW0<Z'SJpUjm<}=:$'aA%+D4\x08nMQ@:4_43kQ*j\nj}\nM/\x0c\t\x08@4bT&l7nZ&+*.!bd~&P\\{\x0bOW\\{dA\rT}dRJu\tW", 'r1z'), [3])
    def test_case_861(self):
        self.assertEqual(pattern_match(' X$]"NDSP+~{\x08(I=I%B`EH:`N<C@rqd|Q-\x0b*]\r@opWY5CAF g*\'!xC12G%2b\x08 ', '12G'), [54])
    def test_case_862(self):
        self.assertEqual(pattern_match('vQOO#y\t,F?VM[+59\x0b\rcfBO1K,y#x\x08M~\n4\n]>7?O\r\\%Jv7N, MI28XG.g K!+It tNDDyw>j[2Q=vWK~01ZO7s -.pm(3} 1*&u', 'cfBO1K'), [18])
    def test_case_863(self):
        self.assertEqual(pattern_match('=QyB<w@Pf*B7)".\rnNlX5~2?2;2RNjY+D=$l<h\x08n.2kkA(TI&tE-OfMZekzxNdX%U\'$sfK\tC', 'NlX5'), [17])
    def test_case_864(self):
        self.assertEqual(pattern_match('La]qn*(g(@_AR1tmQBtY\x0bi\\*A,\'!b7:k\\.+1>vJUra/yGC,S8"$KL$', '*(g'), [5])
    def test_case_865(self):
        self.assertEqual(pattern_match('7$sdraiWD]+8\n\'jG\x0cCH?"D,&H:_Ba\nC\tJLNs`8nVK"u"/S YgpN<GsC[ajpk {', '"/S Y'), [43])
    def test_case_866(self):
        self.assertEqual(pattern_match("'I\\qJr&?K2bR+)BSqLw4OKgnZ-( ]/$uhJSXxZX#aS:PR9Ok9[]PRtJt:(6", 'PRtJt'), [51])
    def test_case_867(self):
        self.assertEqual(pattern_match('xEP7h,m*1}p7vnz261MmFc-"}]C>1%R0dRt9Z\nv|O-.\';5J?{(&E*:rD\x0c( \nk`\'[^hX\n\\HR`', 'h,m*1'), [4])
    def test_case_868(self):
        self.assertEqual(pattern_match("5]hq)y(~,jTgTjU!gL'Q-GaC\x0c*s}E0\x0br@qHd57>P,0;(JOu*w*Q7IC7oV^\x0bq-~SW", 'y(~,jT'), [5])
    def test_case_869(self):
        self.assertEqual(pattern_match(";J;R?yu+Q%q&Z[DV<]t\x0b1af\x0bP=x6?|uX\x0b\\jsuIY!\rzL\x08<'ElaCR'i-", '6?|'), [27])
    def test_case_870(self):
        self.assertEqual(pattern_match('4\\K?3Rkl?~c<\nq/im2V@R1f/"WzB:\njw\x0c#FuAE4sxOvcwX5N;1j3O6:/T#(\tZW=%9VvVyPCiUS"=4-G!aV\r&:|7?{D9_m=O=6', 'B:\njw'), [27])
    def test_case_871(self):
        self.assertEqual(pattern_match('z;Dh1g$&!(nhTU7_YLy]GI>,R_.\'UNZ^Lj3{7.2vG%qA<\x0buH/J_n:x)-KuP/+=0bdjX"?k$uo*_&M(p%~ixbtD%', 'z;Dh'), [0])
    def test_case_872(self):
        self.assertEqual(pattern_match('28I\x0b`]U{z~qs\x0bYFHr2evao)=c)k;hV:hW<sed^\',!*;g"?2\\+I^\'qaK`s(Ke_5AsO', 'g"?2\\'), [43])
    def test_case_873(self):
        self.assertEqual(pattern_match('3C5;o^5"7\\\n;+\\sv j:_*[eV\x08j-<RG\rdf9w\'~f<ADO\npA{$EQqRgvxN=IPQ3\rX3$hyB 98I-ugr', '=IPQ3\r'), [55])
    def test_case_874(self):
        self.assertEqual(pattern_match("oo#\x0cz|cXb'PJ\x0bG]P}CDfw?ZKgPVoYG~~C=v}]N#&T7 \tq;MztR1@)8e-UrHm\x0c\\O5", '8e-'), [53])
    def test_case_875(self):
        self.assertEqual(pattern_match('\t^E(L+!9z\tWT4/5xsu[+NQY!a\n\x08u",7F+yf|b\x0b)mKgZh?f.2)XH?FXF/~PU^Q\x0bv]hadqif!)ebT3Gko/g<mSn\\<V', 'ebT3Gk'), [72])
    def test_case_876(self):
        self.assertEqual(pattern_match("\x0bx_J`>}? *@%w3^6aSe+8CG~<iEUq\t<j'ZVb\x0cNQ0\x0cC[a_I7OsyE[.O|.#ci{/^k/m6p\x0c\n@:L\nLyn628a9.~8/\x0cTpjRBVO\nh7", '28a'), [77])
    def test_case_877(self):
        self.assertEqual(pattern_match(".{HmxIT~X>>bI!Z5/[\rk5Cc\x0b\x0bM]{OU\t9&Xwxo\x0bZh|$a7dD'z%\\bm48yNRdJb8}x2", '&Xwxo'), [32])
    def test_case_878(self):
        self.assertEqual(pattern_match('Y3BA\n~SXc,H\x0bz0oBtN]\x089-p{B,}@Rb\'ts[:oh_udj0I"~mkUZ%]Y>\x0cl,d#YDfAN6V>\rGOc', 's[:'), [32])
    def test_case_879(self):
        self.assertEqual(pattern_match('Jx19took*H9%4\x0b+yCW.H=#WH|"VH2T$Llm#5\x0ccI`2\x0bzT&2*y\n\n /+_Vr8${Z\\f]', 'm#5\x0c'), [33])
    def test_case_880(self):
        self.assertEqual(pattern_match('^DYHc%Wq  Ms~*EV^&y\x08fN=!ex\'w\n\r6/xA3>[!+v4BsU`~P"\\U#>XIEK}M5o0eb%!iav\n\t~}\\MJwb!l`^Hp(', '4BsU'), [40])
    def test_case_881(self):
        self.assertEqual(pattern_match('(\r,jlcUuL\n2r#cjzn\x08p\x08%S|]b_NE0Mg#C=O?99#"q>_4UH$K![SCl;DlW8=/p^rK6:qD,`\x08!v(xJhKn?R', 'O?99'), [34])
    def test_case_882(self):
        self.assertEqual(pattern_match('^XewhTA1l\\)\x0cy\\KtPD2Y^QP%/X\tH\t3\t.v}EgQ\rzB\\e\rGnSQu/XJBQ', '^Xew'), [0])
    def test_case_883(self):
        self.assertEqual(pattern_match("S+}~r6AjugdhcX_R<9T\n):MB_VLq-acY9G]vGjgbu,1z$k\x0bAoB.\x0by2umfz5$14z-!_'kd^7HZT\rz`-6;W\x08slcj_i3>8viX-uK\x0b", 'jgbu,'), [37])
    def test_case_884(self):
        self.assertEqual(pattern_match('Y6t/i,\tVuO\x0b<n)e\x0c9K\\UzgBZQG%j\x0bJL?M\x0b^ZY?NAt3#ZR@kZ\x0b<XKm9.;yZrl1PTv?"o\x0b1gP`66}(J$/&|2\rRWxnP', 'gBZQ'), [21])
    def test_case_885(self):
        self.assertEqual(pattern_match('m{`Bkl 9?OOL}>E.U c|Ae;7T+;4Z_`Jp}:frU%?K7t\r+>#Em4j:`\rD+F)2f;UcLdHu*}!5,4)H/u\ndi#2h:r{K5', ';7T+;'), [22])
    def test_case_886(self):
        self.assertEqual(pattern_match('6D3\r\t[cMiS}DiHzKKs_bWo4`Mk:FwGgQ\x08X7_kd9&8r8N\nCgY7>o+\\VH3]T_n\x0c joE', '>o+\\VH'), [49])
    def test_case_887(self):
        self.assertEqual(pattern_match('E0PkPJ0e9>Y>I%)ngx9Py\x089#NC\x08r3bB|@0D?NDT\r\t3XL&E]x97KIim2` \x0c7*\x0c*7(<g!+H\rLn?G=#tQfCvVaxTKYIh.xI,', 'C\x08r3bB'), [25])
    def test_case_888(self):
        self.assertEqual(pattern_match('<x"(ov"wLBE1dIc"\x0bV2\x08/X#wsTm.aX\nnoA\t. XCJR_+=By[SeIch\\Du<Kekc+\nB\\3)pn%Bd#W,rXAU1hyw=5BVXJ', '2\x08/'), [18])
    def test_case_889(self):
        self.assertEqual(pattern_match('tOQop4`V4\nT\tU3^cY3q:;QcJt\x0bHsW#"{UmZ.JgC1;OkTWk\nHZP-o2m\x08\nL?#<F~\x08a344\x08R\t0&5/yIE"1v;@00_k7a;`{ ;,LATmcy', '~\x08a344'), [61])
    def test_case_890(self):
        self.assertEqual(pattern_match('p*$kt/\\ta.R; \x0c1CP \x08\\ms#D/C<mG\nc(-K m@2dD%{XFP\\ZMxBE\x0bLyeyL', ' \x08\\ms'), [17])
    def test_case_891(self):
        self.assertEqual(pattern_match('+UK!m\r\nrt\x08\t=LE+\ttiM1lXBgcr|Hbf3O\n]0!`.V0}vvoRSi.T(3Cv1-{@wOIi3K+OCYS', '\ttiM1l'), [15])
    def test_case_892(self):
        self.assertEqual(pattern_match('\x08FLB}gWl\nL8]+=ju[{yx{ol[@)i}\n0<+d=eQXWR5):+~\x08ZVx*W\r]>cx*7x\'="gF[yQw}iz(<A"\x0b.se#KoM', ']>cx*7'), [51])
    def test_case_893(self):
        self.assertEqual(pattern_match("Y*jVEcym!2z>fk\x08tb)\x0cF\\T'K^_q,\\H]|H+$rU$2/ yE\nv1eack\x0cuX\n_4_~mr}9=hsZ}hXzv=;]R\tf<3o(yQrC{T~\\8jU-\t`QjO0J", '3o(yQr'), [78])
    def test_case_894(self):
        self.assertEqual(pattern_match("8a]]6-_osbh!@f'`$iafaD)g\x0cZJBinL\x08B[s]Eb\x0c~B#8\x08XcXZgE^!}EQKa#dlH^", '`$i'), [15])
    def test_case_895(self):
        self.assertEqual(pattern_match('IMsV\x0c1?9ue8]jq\\\\r[!DguMW VZ=7b A]$AE#kp`|GF^O8NcCXhW4nCO0TdKl6hg0:wBPHS\x0c9^)nmK\n9QKT@PW3\\^.', 'sV\x0c1'), [2])
    def test_case_896(self):
        self.assertEqual(pattern_match(')<iN2\tsVg2jGs\r\tHjV<R\\U|`EA\ro[U+Tvop-i\tsXa* \x08$VPZ/M\rp@W5EL9XO', '-i\tsX'), [35])
    def test_case_897(self):
        self.assertEqual(pattern_match("4/^S3a\x08OG^\x0c;7PT3\x08Jc[:*KUw; k$#2o'ZtOp^^r\x0b\\zgXDiv1kEv0b7z_+U\x08d7vFx2>) @T", '^\x0c;7PT'), [9])
    def test_case_898(self):
        self.assertEqual(pattern_match('}Cq3\t&:uxx)qt*2zune.[IwKdpXVpys*\\x((xB4# =6\x0b;t@ (gyJ(o[bs?Zxm]#i\\ZlCr/YHXh?_<y8q-M@2\njC3;', 'e.[I'), [18])
    def test_case_899(self):
        self.assertEqual(pattern_match("&=JuKrwRgCt7+#nd4|+W'mfn`zR:p)\t]-H.i(=zg\x0bUq\nqx{8jMF\rbw_ebD@", '+#n'), [12])
    def test_case_900(self):
        self.assertEqual(pattern_match('&V\\tfh/\t>kx.3bPaV_Lb<8).z2a(uwgT\n`no1jggU?\\BjG4OT9K4\r}!m``ajU9`LV9!(f, .yb69=a6t\':"VD&NP+t<\'hF', '/\t>kx'), [6])
    def test_case_901(self):
        self.assertEqual(pattern_match('/\x0cn9t9_w$I8sFCEvG;AdPZu\\8v|gfe\\4]\'wG\'Pm;j;RtC{\t4Z5];G-"+xR\x08t)A+U8', ';Rt'), [41])
    def test_case_902(self):
        self.assertEqual(pattern_match('MsSQ<>6]kr}9tjht\\ h4#)/|aD\n.+l8x/f4`22n@L\x0b<yqxg`U[$hT+I5VEt8-]V^+\rX/J(;kL1[~hZ;j:i-n\t', 'VEt8-]'), [56])
    def test_case_903(self):
        self.assertEqual(pattern_match('Che)~8WS\rO~&{&`}rk;41+d:\x0b:ncjM\r,x\rx{S\x0cKL\\yl+*,e0q{ws2@+l|WkR', '0q{'), [47])
    def test_case_904(self):
        self.assertEqual(pattern_match('N]aMRK\tG[rEV(MFdj\\k2idTnM})l%Zz#^Lg?\x08dk\x0cC"Iqert"6FL5E9n<7K{aCycEb[y^f{))dGVWcH\'elDhL7zL_a\x08!MwNnR@', '})l%'), [25])
    def test_case_905(self):
        self.assertEqual(pattern_match('S~|2b6z1uovg/}T,?3|BBY\t%/UkUwIEJu;0Bh,F(V\\;JWE8#GCInr)<JQv=\t\x08qI[\x08aT]+c>>H^&MxXPu:ea0k(06!a6%F', ';0Bh,'), [33])
    def test_case_906(self):
        self.assertEqual(pattern_match('#3<\x08P/9^Q\\Bd*ZWL+^#@[*`Ch#u:)\x0bQ\x0bz+k3\rplK7\\4f\rKeJqmjN!o;uj*8ChH&Zi_],qA{BFFMI\x085|FyU1S2q/h', '|FyU'), [78])
    def test_case_907(self):
        self.assertEqual(pattern_match('(q+/Sc\\b3Vb1B\x0b(Z#aK:#BU6s{n<?\t\x0bX@]$<\x0bk3cm4JE474vX{i|6\x0b-\'L24\t"\n&e\t\t{z^=v b{S3/6QK8](&', 'BU6'), [21])
    def test_case_908(self):
        self.assertEqual(pattern_match('qZihtvmb>XP#mN<G9~Y7\x0bdeUGG3B~Lkn^=$E!6je][\\R\x0c qXxz</E[uj\x0biU3QS99$\x0c', 'mN<G'), [12])
    def test_case_909(self):
        self.assertEqual(pattern_match('$sFH4/[9P`h\\y~gv\t#]n)*rvn`7}#1<9UIQ R#)n\tGGKwZ>|J$4jtK$9]u2~U\x0c[\'V"aH\x0cb', ')*rvn`'), [20])
    def test_case_910(self):
        self.assertEqual(pattern_match("uoFtWAsLW!lpnlW35^\x08k@v>'}|o5U!2\r?A1>oHty=oO+ScJCSZ&QF.X-Q6", 'Z&QF.X'), [49])
    def test_case_911(self):
        self.assertEqual(pattern_match('"a\np=%CZ#\\\tClG@{xurA]0ubQ0h+O\x0cmZ1|*<-E\x08Y6rjHxV\r_#\x08UQU]jE\'}SJ&d\tq[s9?`UkY9?P\r^S~\n&jKx)\x08~OW,>UNs4Z\x0b3f', 'J&d\tq'), [59])
    def test_case_912(self):
        self.assertEqual(pattern_match('{U+7f+i)^)jaz@RCR?Z\'$"v\r\n?i72.g{44"\t@};I\'\\(Qb#`GgE8J7R:(DCm3Q<\x08 67=93/x', 'Cm3Q'), [57])
    def test_case_913(self):
        self.assertEqual(pattern_match("+t_u'FrZ\r`ober)Q.?-a?r{3+{Ykm;\x0b`EQx^>\rQg_RP)_m&shQ<5i]1q\x0c6hs\x0biRrU\n3*&1", '1q\x0c6hs'), [54])
    def test_case_914(self):
        self.assertEqual(pattern_match('je"6|&@r/mM?a\n?0@zn,\n\x0clHMPl\\[1u{zDEn-\\/>b@7$$#.O|d9p_-6r6N\\L)HB\x0cav={"', '\n?0@zn'), [13])
    def test_case_915(self):
        self.assertEqual(pattern_match('18j],\x0c\t|@5127ETrgv5G"gs)=EyfS}B7Qz\tCMrLFiYW~^md[/z]5,>2{M\x0b%;f`gj0-^7EI[]!,?e37|\'\n', 'z\tCMr'), [33])
    def test_case_916(self):
        self.assertEqual(pattern_match("A4\nb[1F?9d?rw\\VRc(|~X(.U\ta0yN)s|3ng7Nf5p&#[leC0']NfnA(id+SS|l2!_&\r87f?DGu6isD33&\n7~Xx:t9", 'sD33'), [75])
    def test_case_917(self):
        self.assertEqual(pattern_match('}?Cm[E:Pz*|rGH3/-x6ZH\x0c)eS@(4$S o!ejKQ8[ha!-d<\x0bDXV#H(\r;Y \'\x0cQ"dLt|KfC6[qE]', ')eS@(4'), [22])
    def test_case_918(self):
        self.assertEqual(pattern_match('8$eUBy\ro>\x08"^d(s_\x0cfc>{#a. F&clId|@AU+v++.<V}?usFL~AY!,gl $\ny', '"^d(s'), [10])
    def test_case_919(self):
        self.assertEqual(pattern_match("N8\tI:\nQvW9`!iHh?6~YsB.o 1qo*/T dQQof-bKV!AJXst=Zm/h0?p&i^m%.l*YbkWM]'(\r!*mE9w>n,ZHD)N", 'V!AJXs'), [39])
    def test_case_920(self):
        self.assertEqual(pattern_match('w\'zkS%Jp,LJoIc&3aOP?YAJ39nIiy*JR/"T21WAn:[a|SVbSZfj:9#TBUC<sN=nyd2k', '/"T'), [32])
    def test_case_921(self):
        self.assertEqual(pattern_match('@nc}!yofea6D[TU7{\rJ~:J\x0bP$\x0b(=?3x^d^+1k/Vv\'_Zar}<UbYP"&Wtus\r%OcSt.yyj[Gx?H4id', '&Wtus\r'), [52])
    def test_case_922(self):
        self.assertEqual(pattern_match('.:5P0y<Pz{k"$FkM6\rR\x0cDW}s_@I_F%A|UQM|K`\x08j/aQu4u44*^', 'DW}s'), [20])
    def test_case_923(self):
        self.assertEqual(pattern_match('VSj\x086RO&U(y\'+e;"eQ$2DSQqu~NE0f3\x08B)M/ 1tcg"3:i8vzoYgneKkoHy\x0b^`hip7+z*YPtA4Km4PuVxY=`', "&U(y'"), [7])
    def test_case_924(self):
        self.assertEqual(pattern_match("Cl\x08S\\1J{!GFwj1zb.1XU1V)YAt<n:*yG[P[yY\\KuT\tm!B[,K,3\x0b\n24z#\\'1+L3R=\r\t=pwf@i&8CS\\UClh@ar", '[,K,'), [45])
    def test_case_925(self):
        self.assertEqual(pattern_match(')K4,\'j`"W"b\n<`w!CfuOeu)&5\n$V?n@R5^  w0w)nrHOi*?4p`>?j,\n"I,X7rB&~0%&F,0hVUn\x0bul\r\n\rVs\r41M5\x0bA', '\'j`"W"'), [4])
    def test_case_926(self):
        self.assertEqual(pattern_match(' clt+Po8"3\x08/lX}^\tjB;tN{MVQ\t#~;9Gkh_v^Oeo|CMl{%>A3+tOQ76ukPAaP&m8>FumPYuK5|1aF\rcz\rsqLj)\x08tt0e`B2)F\x0c-d/', '>A3+t'), [46])
    def test_case_927(self):
        self.assertEqual(pattern_match("!-9n@xF$K@5o_@QF@QGp>S@8>6TkZuWN$'8_`:OJY6.7-.Xi2zoL0Nh<jMUi:lm3RuyrO04_DG", 'Gp>S@'), [18])
    def test_case_928(self):
        self.assertEqual(pattern_match("vwbM[K~sjN1bLZ,?x^QRgGaQrX:D?<K1o{'g@&/4W7K\x0bh\x08p`YBx\x08|@.b;\x08hqT.N29]-)0!`.^[F\tQA\\} S#@t|z]F/+\t", '^[F\tQA'), [72])
    def test_case_929(self):
        self.assertEqual(pattern_match('K\x08p*BL-1l-Vj:pL(GmMs9 AmL2r%[o"#Q;6P$GpP\x0b7u9L\r(#;`~!(M7#@F!Q4;\rX6D=p0?n', '!(M7#@'), [51])
    def test_case_930(self):
        self.assertEqual(pattern_match('*p|bqC3p^4zbSP?9lS\x083G5p\x0c@8{A*i\ra`_I^&zBcpND"Yo|$%"q(E\rg3\x08IWaF \rQdhC=*\\SDX%2A#6S', 'a`_I^&'), [31])
    def test_case_931(self):
        self.assertEqual(pattern_match("<xDa\\$*}Mb\\/iEH3Za,(/4=T&y'1I>&kv9:^GU+E?DY%TKgG,Uk3`juq2T(\\yMXQt}", '/iEH3'), [11])
    def test_case_932(self):
        self.assertEqual(pattern_match("mp;CN7l@hzhb\x084(*SNtBu9 ;Z9gM;mC(zB$'*\t 1(a\\LQ(poZ??N\n5", 'poZ?'), [46])
    def test_case_933(self):
        self.assertEqual(pattern_match('%{4n\nP"a96ke=[M&JL=^p\\EQkz,:Xg\\6l|T\x0cja%{OhQzxXIy8S;\n:/_#:`w!\\\x0bF6jD1SLraK1KFHY;-lknl~', 'Y;-lk'), [76])
    def test_case_934(self):
        self.assertEqual(pattern_match('z\x08D~LL4-Nmz4x"Q@.*4VW\t24ic\x0bX~@(? -Ah^E\tDiI\nfyV<,e:)Ty} Z))#JPrpD5R{Owx\'L\x0bC{[1h?^o#MA}_]v|B^vzp^', '@.*'), [15])
    def test_case_935(self):
        self.assertEqual(pattern_match('>of \'s$I,TE sa4OQ5? ReZ|Gz=0e4e51c\t?k<\x08qH_<04"]\x08x8Czvx}WQq%[4+$$A (', " 's$I"), [3])
    def test_case_936(self):
        self.assertEqual(pattern_match('$hN+2D3/(R7IhQBL}G3b8S\nu#-z4*OS/*d8>\n1%]4j7EXHh7^/UT@"-O2`', '7EXH'), [42])
    def test_case_937(self):
        self.assertEqual(pattern_match('L($k1AS\r\\lXR;Z)#&b?_3,AU><i\tz*aO)`-Up.h\\*K5#JyC8"yt;e$M\\SZB\'K!EO+ci=zYEh\t', '\r\\lXR;'), [7])
    def test_case_938(self):
        self.assertEqual(pattern_match('P)P=#,]HrC}#PhhFb(`J,VSYxu^^\rJ5&~\'(&vh\\|hTv%_!>RH"i7""vf:j$?d3.0IjO8<', 'P=#,]H'), [2])
    def test_case_939(self):
        self.assertEqual(pattern_match("NEdjYN-OTcq(;\rBRsf%wW|hfw^\n'ZrSS~t|U\x08D&d6l?$j2CwH`J}\t8FA]N/I", '|U\x08D&'), [34])
    def test_case_940(self):
        self.assertEqual(pattern_match('\t._pCUU`yel7M56Jl"4DiXBk[_Egqj)@z&3=@l\rpD6l/ \x0c\x0bPsb.kUOI.{', '\x0bPs'), [46])
    def test_case_941(self):
        self.assertEqual(pattern_match('_c0D{C\r~~\x0bx^.rtl2(/SoD@,=D[Y6a\\=HA:Rf,K=`9N\\p4Rc~m3ujh}(u\t0z2`:ME', '\x0bx^.rt'), [9])
    def test_case_942(self):
        self.assertEqual(pattern_match('RfyO.vo-H}U?)"J!#DfGi=&`|ujO)Hx,D7W34}L*[\x08i-\nlw\x0c0RS~Nu^7aHrk\x08\'n', 'Gi=&`'), [19])
    def test_case_943(self):
        self.assertEqual(pattern_match('734i#o"_Jkx\rz,DT\x0bI/u@.HGA+H\t#Xb![?GD\nl[\rT#|F`z|wry"|u\nlQ y8CB"', 'u\nl'), [52])
    def test_case_944(self):
        self.assertEqual(pattern_match("SP_kK?'Wify\t=acB/Whz/8p%|yC#jre\x0cknp3Nnj5E6zs9?Q>0s7hOm63g\\\rULN[*a2A", '7hOm6'), [50])
    def test_case_945(self):
        self.assertEqual(pattern_match('RuURg)4f[Q\x08M!hXlG1s*e;\x08B^L_\x0b[u|=<|q0^Ee)sv}sN\x0bu8]2u[NQed7*`C6wGhKfdsIG$6W;wH>}rnG', 'ed7*`C'), [54])
    def test_case_946(self):
        self.assertEqual(pattern_match("o r2|6\n/X|%n%lhDu7?OH#'4!rgHpSKKLz1f|s~o>:ZrWZz\r\\(wQvVh!h\tMFh20Y&D(R<D}9jqftb:|}hIMw$}(N\n+rt\x0beIR, ", '\r\\(w'), [47])
    def test_case_947(self):
        self.assertEqual(pattern_match("/x|`eN<u\x0c).6\x0b?\\\\zO*q+!A\t\nhB42c6%iZMTSD'=]t<-\x0buQ`,e", 'hB4'), [25])
    def test_case_948(self):
        self.assertEqual(pattern_match('|/d$3i}+c\'<G%SR%IyCf,7HqZ~\x08927:\x0bE(nkfZ~\n@"[<N/-\tnYrva4\x080XJAJ",~xf*1?=I.Y"!xzP0$<', '}+c'), [6])
    def test_case_949(self):
        self.assertEqual(pattern_match(" Zi19r&0uyu}#_$;w F\x08oP8^\x0c5=D=\x0b1*@dVO$o_<\x0b3\x0c^qfx](cM.#Z',ifqv{}K5t\rL-h7_0^*[1(d", '\x0b3\x0c'), [40])
    def test_case_950(self):
        self.assertEqual(pattern_match('\noaSt\x0bTVei@_"->5\rm$i4SpO9>6d|[K~9H9!QfYW]\trU]{tEND^!_WJVuL-8p_$n,a\x08-cZ):B,h C<@fL%I&\tO!%kzcl{C', 'C<@fL%'), [76])
    def test_case_951(self):
        self.assertEqual(pattern_match("p0\tix',FU}M7`SLt{BCj]ly{UG\nCr--^$%/ctQ}EA\rB{gwc_}\n^~\\5f4^@zkqbd", 'A\rB'), [40])
    def test_case_952(self):
        self.assertEqual(pattern_match(' So4MFy\t!Mk\x0bGC"Z:"GHG%\rf"EDS9vkI,\x08RxGb(Cz3x1G%a3P>MSTQRO/A(X$`ooEr5U_z', 'x1G'), [42])
    def test_case_953(self):
        self.assertEqual(pattern_match('/4Da\x0bI-dRx,^&\r5V(AIo$\x0cf\n|srLPYm`W^OT\x0bzyye\x08Z$sA\'0%=Z$\'*,A7vL632vc05\r6xe}T;T9d8O)8z)zwT("', 'xe}'), [68])
    def test_case_954(self):
        self.assertEqual(pattern_match('x6P8O\r!GYo\tpipc:?4b06GYAob\r&kI\x08ijF{ t]#q\x08tO}<8GMd"YI#d"5.\nJ"<ScJ_DZpjc=?X%IM', 'GYo\t'), [7])
    def test_case_955(self):
        self.assertEqual(pattern_match(',eXI!2P[dcyYTkjMgJv^mw4Z_\x0bRWo\\1#OfQR]ZK(,y9`$D%+\nn"a5Z\x0bI%ayVY\x08P`t-Mgy@dK6`s)O:~9J|7Pv4901z', 'gy@dK6'), [67])
    def test_case_956(self):
        self.assertEqual(pattern_match(' =u7m\r-qL\\qq6(=F)Nw8L`Z\t^ 1{=J">Wv4sxP?*\\C(%"#Di^<9rVd[NI;"MOX', 'w8L`'), [18])
    def test_case_957(self):
        self.assertEqual(pattern_match("2lyG8<6Y96'\t>8ei/4YP4O\t7e WRk>\tlGGr9^)}0@^`R-.5\x0c)e%~jKd0\\*(NNoDFBMjWV'A ol1f(L[", 'GGr9^)'), [32])
    def test_case_958(self):
        self.assertEqual(pattern_match('FJ1->F,\x0bT+6re9JK?.5K\x0cvgaP)\tVt4`pE`2n_9w\x0bPV,FuZt%+AK*e=iR-,?(bTR>G\npo:1%\r3v\tlcjwSU3/ L^M', '+AK*e'), [48])
    def test_case_959(self):
        self.assertEqual(pattern_match('R)[/avvQ}x;>)/\r \'GR#fQ"%%\r7R=\'_7Vb7m5<(I55|Ot 1-2Oe9\'IaF-z\nDHvP j\x08iw:?lC)JB& \'3WJ5sNIaz"<#[oMJmxjP"H', "B& '3W"), [74])
    def test_case_960(self):
        self.assertEqual(pattern_match('i72H3 Nc.ec6:;o+]l7H7i-U\x0bZcd;\x0c/#M\nGk{SCX%hB$5iL6FN_l6/\x0cS~;^szv;VedDX,:|a]b2(*\tI.{G#c"\x08na5d]ByA\tT[', '/#M\nG'), [30])
    def test_case_961(self):
        self.assertEqual(pattern_match('L3y71S48)XwK^U3,%OWg`K,Z;#_}H L1N16Mfnou_:=NEjN[7*mo|\x0cBTc&=#OiT[J~rY?\x0ce\x0c]A^=dbWWMP)1~"on{3VV\'wF\'', ',%OW'), [15])
    def test_case_962(self):
        self.assertEqual(pattern_match("m.8jil V8d^DZjbt\n8(fD)u\x08d%=!_0A-\nu4S--bgs9[>hQ9\x0c@\x08G\\H/8q'8PTclA10Y5\ta$H$;", 'm.8'), [0])
    def test_case_963(self):
        self.assertEqual(pattern_match('\n#Z%[8X&tyFTM7bkQT`<_c^dC\\J*C\\D|3]H0=ou_7:z>r9?C,<1(o8&,^I#35@h=[FrHqu\x0bkbk|w]=@', 'k|w'), [73])
    def test_case_964(self):
        self.assertEqual(pattern_match('b}@ZG)Y)[pGdp&1\x0cIV"AD)wY[nvqR1\x08j\x0co)Mg1Tp|\\Pu|LFA,GpdY!&k', ')wY[n'), [21])
    def test_case_965(self):
        self.assertEqual(pattern_match('&%-2+RMnj_u+Q5iZ=\x0bf@*"#~Ja$E=B)K|\x08/p)#j\x0cO|="D#+\x0cT5:y6vo~2t$[vf54', '6vo~'), [52])
    def test_case_966(self):
        self.assertEqual(pattern_match('7m"4bXX`ISipUp#p6\x0c3>0qncG(u\'rw\x0c#\x08S9?9\'\rQ\\?dB8d,@L8F\rn#Qq=m$b?Q@Cv9[)d"d3\x0bOevCxiVW.Jt]~3', '?Q@Cv'), [60])
    def test_case_967(self):
        self.assertEqual(pattern_match('wDXmi3X@T5YU_8`[?Y)E!5kkJ\n,3MG,i"TS\x0bdYT!H0p(0~E7!XW8j3VyW))?A`Y', '5YU_8'), [9])
    def test_case_968(self):
        self.assertEqual(pattern_match('?=#^pq\x0c&LY0j8aZ5"`W)_l`z\')#7H*bvtJ7_mJSyz#qvR;-ebR]U8}v$%D)', '7H*b'), [27])
    def test_case_969(self):
        self.assertEqual(pattern_match('8\rLKqim!F#"zuY\tix Tpbp^\n]\rb{]<=BokkKls* }x"[:eEn*4E=S*\x0c\rloi ,1@z-hj\n3z$+*S*~b,.\x08\'f\x0cy\'"tK', '^\n]\rb'), [22])
    def test_case_970(self):
        self.assertEqual(pattern_match("Ze?PnmxZNk<E`6O4Uv`UBBnk?lb\x0brO7F\rn;,.e)pg`\x0bkutIB\\f>\x0b^;>kWkGB0?-;6[<i[\\Pl['j2GgcF[EWD>V", 'xZNk<'), [6])
    def test_case_971(self):
        self.assertEqual(pattern_match("N9yn;_vO\rA7eE\nxHJ<1@sgE6[m16^0819aK'H>Vr8R_7?\x0c-{\\UktQ$1dS&f1E", 'ktQ'), [50])
    def test_case_972(self):
        self.assertEqual(pattern_match("K]S\r@<gAIiQ:'Nd'$\x0c+DJWQ|Q>P~G\nWN%4?\rGncvJ\nw1pNw50+U", "d'$"), [14])
    def test_case_973(self):
        self.assertEqual(pattern_match("P(#T0,Go\x0bH )G+rPwk.iC~g\\twMR:l/RCXA@?m\x0cy&$e,\x0b@,-G;QC#iXi`~;\rq8%\x081j'[[VBH*4\rtYb~m\x08o(\x0ce\x0cF:VK", 'o\x0bH'), [7])
    def test_case_974(self):
        self.assertEqual(pattern_match(' PF%zGjw.k#ARPHmVv&4Ox"V_0Z/JZBey=<xY\no,mge&G1%?y:=_<PC/', '"V_0Z'), [22])
    def test_case_975(self):
        self.assertEqual(pattern_match("iG`LL=xWHKBZ19\x0c\\Q|v:'k7cl*sH\x0c*HK<H1va?;P*8|)VP\rB4}3g*@;G_w\\i\n~Ct;tujKLQLHylN07!\n|5L{tP2C", 'L=xW'), [4])
    def test_case_976(self):
        self.assertEqual(pattern_match('B" KxA,\n)T-~puU?\tzAX\r\n4aMeiw}{aWMg6.2RVxjP\rk%aQ<E?}S(hO\'M_K;unovELw+(X;q~Onj?)b\t%', 'AX\r\n'), [18])
    def test_case_977(self):
        self.assertEqual(pattern_match('LuzB\rr^fJ(8H\x08NeK-}Y`-32~?\tBe[lF$\x08/`g)59d27\'4xn/="fN{a.XY#c}@)D:}\x0b%fqMFN3C&~lsK=\'', 'eK-}Y`'), [14])
    def test_case_978(self):
        self.assertEqual(pattern_match("Kj<'qX#r^x {Y'+d&-\x08D9`klGv4E:{O$i&G&&R*2Fan[OFMm[2kI]EOu&5bC%6\tIWt}G\\ny.Sxp3d/[h}", 'u&5bC%'), [55])
    def test_case_979(self):
        self.assertEqual(pattern_match('r^Bkh#*\x08h8caf\x08,_@D\rf2,\rv^\x08P\x08-6d;He`ZZi",!80x{h!7Z1ADT-p1fU/24A6gn20eL84pHP,$2*s\\M3:fGU\x0b', 'Bkh#*\x08'), [2])
    def test_case_980(self):
        self.assertEqual(pattern_match("\rm\\9&Vl3W&{[;n\x08%Q`E7#0i[n{D\x0cINr(FL# w7H6\n-lK\n/E,,c*'Sk\r0\x0cG;bA@Jtc&=P9c?k>h", '\x08%Q`'), [14])
    def test_case_981(self):
        self.assertEqual(pattern_match('pC\rUCSjP\\D.I#6/L}g~Qwyk,q\\6XN+t9\t7w5n3(nVD^V?U:s)1 p6FP', ':s)'), [46])
    def test_case_982(self):
        self.assertEqual(pattern_match("\t;|W>'!sP+{6R=}1-\x0c>Ak4'4m%-[Hu`\n\x0cLrwVP*)\\\x0boO,@5}J$WJixYpSzp!7MUURpu%=&'?P1xK@", '\x0c>A'), [17])
    def test_case_983(self):
        self.assertEqual(pattern_match('e%|A6Y0u3m<"N@%x(waii}F4-)1\nW?f^{`Y?3`+\twE%\x0ctXX\\foO@\'~0KIR\x08NFQB_\x08n*$Cd*X', 'wE%\x0ctX'), [40])
    def test_case_984(self):
        self.assertEqual(pattern_match('@.C-&$%3kv0e>]HZM\\1/ ztR0/_5SoT7e>BDQ3<^:.R-T%:LHGWC,tihaa!M9+O', 'T7e>'), [30])
    def test_case_985(self):
        self.assertEqual(pattern_match("0@p[g(aVbdC\x0bB_eY+Og4kO/|2&c)A'a(|I\\j}[ses,q?Z\nJ_BYR%Cu\rbh\x0b?ZXr#x`&)}jf8C*M$q`8oNPA%V4a<A\x0c3Nr86w4;Y", '[g(aVb'), [3])
    def test_case_986(self):
        self.assertEqual(pattern_match('Bz c"nl\'8b&StnF\'*isUM*\x08f=yi\x0c@bUuB\x0cb!n;[2|Q!G~_HRx8BQ &qc_]@t8@[=\x0ci"<@&J\x0b', '8@['), [60])
    def test_case_987(self):
        self.assertEqual(pattern_match('uX7ii/k1<\\n8W&+2j\'bhl%4\ny:72f@K58Zg\\&/q$>[Ui0"^v*lUPvW<g,\x08U`IU\t8KnV.jo6MxEGE}$C\x0brE', 'lUPvW<'), [49])
    def test_case_988(self):
        self.assertEqual(pattern_match("n9xj!,;!h'y;O<-LiVU\rbXgwF'r4oOIKK?kP\nZ2{zbm!!{ VW%\\J@zq!51cjS\x0cMFv)>|W\nM[zR=AL`#gw{0\n!Op/=", 'M[zR'), [70])
    def test_case_989(self):
        self.assertEqual(pattern_match('[elMVP/q\x08RooJ[6&{VW,Rd@v?-fv*X}`Gj}b\x0cp6zNP\x0b3t\x08](/iby-FrbFj\t^Syc1"\x08c9FW\x0ceM\x0bF_=\n\r`E&L/xl;3Ypdl06\x0bhnq`W', '-fv*X'), [25])
    def test_case_990(self):
        self.assertEqual(pattern_match('2"?f2"{*mjJmgPB2x\x0baOVmd\nx>OBZl2]\\5?T&nZ5!A;;kPC\'p4crcR]9u,M,fo&R6jUJh', 'o&R6'), [61])
    def test_case_991(self):
        self.assertEqual(pattern_match("q~LW`iPp];zPa;Y2Em*k`5'*'Y]vZNH{OvL:O|d;i|Er*I/$[bMQ:R\rbr1\\$|!`,LiaXn( jxVL\x0cz(", 'Pp];z'), [6])
    def test_case_992(self):
        self.assertEqual(pattern_match('5ZV/yR$lSr\nls_t@X|\\fRHB)GQH3gm?i\\n^ /A\nb,`_do8\r4+\x0bnUT6*wxu:Gj<Dv\x0b,{#dP,kV6_YBXSgenDPM==m\n&ng"#TC4', 'u:G'), [57])
    def test_case_993(self):
        self.assertEqual(pattern_match('=wNhjqr#b_yQLa-4F/JoFHOD*-.@bQxj9y5PO^70H4S>"\x0c#,~OR6s', 'jqr#'), [4])
    def test_case_994(self):
        self.assertEqual(pattern_match('7ke\n7b]99\x0bJ|*Iq8%K^\r qO[/h\x0b\r_`EHV\\\\c9kb\x08*. CmR\x0c)|Th]hw?rC@7:+(A`4', '_`EHV'), [28])
    def test_case_995(self):
        self.assertEqual(pattern_match('Qn hJ!N\x0cf(D]>qX:zS&"\'LT%k]u2\'YF~&{(+rm\'Rj.QVA}^p0i\'+[INT0', 'T%k]'), [22])
    def test_case_996(self):
        self.assertEqual(pattern_match("T1{Axm_@:43<w\t~;7!Z\tk!e^-O@I#Rgn6@A\x08[#'d<&9Ao]1]YwVx/\\Ao.\\N6jcwTkl862Q(MK9}E{#\rC) ZSLN2H>J\x0cz22/@\x0b", 'kl862Q'), [64])
    def test_case_997(self):
        self.assertEqual(pattern_match('Y}rY{Ac%m?/wH/|uv%Tc2.<PC%\\4?eNAo9cE"i7F).65lPX\rIiK\'F2iy,U(', 'cE"i'), [34])
    def test_case_998(self):
        self.assertEqual(pattern_match('5d\'YJp?W&_osB*[8/ "|J:.!<lbk/<"&IbU5oF\x08vVjieLqfaiHgdv7ZG\t&EE}XDr|A "=CXf,?MZ\r\x08n{r vxV`Mz(:N5CJ$c', 'fai'), [46])
    def test_case_999(self):
        self.assertEqual(pattern_match('_@1\n~\x0b|7Wrsxuf2#twf6/.J\n(E.\x0cKq7IVvM"\x0b{NvV("bbb;f[w<Eh(d,&2fo")0}XfQ.oD\x08`x:rn', '7IVvM'), [30])
    def test_case_1000(self):
        self.assertEqual(pattern_match('\t4IVc\x0b\rT{a-s)$7u<|e;~CgJ*,,0k21`eh!|C=K\x0c%`x;YQw% EwB0\x0cu63uQ~\'4Of#"qyRt\rAxJ _t>T782oK^\x0cd&0}CTP\x0c0R', 'C=K\x0c%'), [36])
    def test_case_1001(self):
        self.assertEqual(pattern_match('\rylMI[[b[={~XB?G9g"]49Z_9`B\x0bA;i86e>^XnM4\'.3`mY/I!%y2A<dUH4z,sm', '/I!%y'), [46])
    def test_case_1002(self):
        self.assertEqual(pattern_match('["\x08a\x0c+G9\rc5V/\x08b~wk[w=}a/mM[KUO"Wy5\tY!\'p~&jf`g1C&5isG# bO*s7XL', '5V/\x08'), [10])
    def test_case_1003(self):
        self.assertEqual(pattern_match('&>|)3,MeJ1L<tY~=gg2Rq2X=~a\x08E"4GYh1SD>lox{\n[;:~9FA:5TVwQ|2x\tU', '>lox{'), [36])
    def test_case_1004(self):
        self.assertEqual(pattern_match("aIN~%Pv'V_mkQDEZ@x\\ZfXv'2%LC02zRg)XrN.Ay3S\n*;w\\577Astk\x081=\\MEXY|DNB6K#._Q-m]wXpoE/2Z?Tc=F\x0cUO@NFJ", 'Q-m'), [71])
    def test_case_1005(self):
        self.assertEqual(pattern_match('p@K5igi*tVI$G7BYMi\x08B*\r\r9SgnB<?X5P?6M;I=\n\n%a|:fM0TXh{B/;%Mx3NZ$1Ypdu\\]!\\IEm D]P', 'h{B/;'), [50])
    def test_case_1006(self):
        self.assertEqual(pattern_match('\x08x0A.xJ@shu!JHc P.T(\'Rf654eNso#ygjC\ryvBIi3p"iP9M]g(\ny[X\\ISHZm}@{O\'gGsIVkBu\t".,|&)5svPr_9JP', 'BIi3'), [38])
    def test_case_1007(self):
        self.assertEqual(pattern_match('&2ic%beL&\\,\n*r_rc+ZPE\x08`mQE ].=FAvV+YqL$KPr\\T]-Iz&+W[MAH1m\t\\,ma{~8U{hW!"$k0+\x0c\'\tq~A', 'T]-'), [43])
    def test_case_1008(self):
        self.assertEqual(pattern_match('C.!P-\t89#(?Qi`F)9_)2)E\x08Oo\tj$!1~Ujjo\n&a*mAc,VOtp|w 2:cE.U/$_!Y;?T5"R\x089r', '*mAc'), [38])
    def test_case_1009(self):
        self.assertEqual(pattern_match(";\t5phHAXqag,lpt )J|C=Wu5Cv\r6` ]cHv6[XAC.HaM=$(YR\x0bO\n\r~$br'js/S!FFdSGfk~|QDS$p?X1\\f\x0c17Z8^'T", 'C=W'), [19])
    def test_case_1010(self):
        self.assertEqual(pattern_match(']R3:y7!L,J,QoO7fr{qR2!|G%V`!Z_ZMMoM>\x0ceZEfe\tH)W+<"Z17W', ',Qo'), [10])
    def test_case_1011(self):
        self.assertEqual(pattern_match('a3<TS^"\tTe\x0b7UKP$l:-%=w{@N\nApLPHgB57[bk*xzt7`##-8fVG/dBgPf^~E?|', '7UKP$l'), [11])
    def test_case_1012(self):
        self.assertEqual(pattern_match('je\x0bdlt|bYDtdJlt}_{BT@\x08gD-]$t*7z|V88q{)ywgDu2\t\x08.:qA*m}i.\x0bxHPa1/5k', 'BT@'), [18])
    def test_case_1013(self):
        self.assertEqual(pattern_match("8Hzri\x0c]/3A.-k8/Ftc/g@;R&<7\n\x08#=cg'VaC$n,rr-5~\rs[mO9?d[NaOSrlfYZ4", "g'Va"), [31])
    def test_case_1014(self):
        self.assertEqual(pattern_match('U Ic%!\\,lP%`P6Ve\x0c&9k\nB<5Th $:v2UO?Q46G_>B-Z\\VMzEm6IL=mmb+`Kj|k7jAHU;0u/i^K5y&h$]Ll&', 'k7jAHU'), [61])
    def test_case_1015(self):
        self.assertEqual(pattern_match('; :7&Xian_e[zql"B/\nu p`t.WV1*Nc>8`hj.fjHnz25y"_0-%(<Ir\t}LotN$Ung\x08<",=]T', 'Nc>8`'), [29])
    def test_case_1016(self):
        self.assertEqual(pattern_match('+o/>/h8lU}0.zX`?\tDD)n68:&"L\nmJe=?5il{j\tH)Sjz={1xX3VK', '{1xX'), [45])
    def test_case_1017(self):
        self.assertEqual(pattern_match('\x08|j\x0bkZ^0h gY{<`\x08y7ZWLL\x0c`jCLC;hE\x08H~4&g8koL\x08#pX2ZAUi', '^0h'), [6])
    def test_case_1018(self):
        self.assertEqual(pattern_match("WO<j`^!IRo\x0b6ria{b3t9QE+\r!'QoZ Ph`Yo;M!zfbUi,SU-e5 CedqMJ\r\x0c", 'i,S'), [42])
    def test_case_1019(self):
        self.assertEqual(pattern_match('"&4\'&m?r6HZkz\x0byYj-8H^onux\\!0f/!hE"5(qY(66\r5n4<TT\x08QL/,=P5FGzHg\\Jwl', '-8H'), [17])
    def test_case_1020(self):
        self.assertEqual(pattern_match('V*[}&IP7>z9K[<M\ntIe9ZRB/w*W!YW| 9/l[3RM3(V^k\x082c.fKNhe0<T&?7"_f/\\*Pd{]WQY\tC4Y', '&?7"'), [56])
    def test_case_1021(self):
        self.assertEqual(pattern_match('{du,=n./\\z3m3q/w\x0bu_<puofb\n_}\\H\x0b845>djtGDj)/_+sJ0; ', 'uofb\n_'), [21])
    def test_case_1022(self):
        self.assertEqual(pattern_match('[`\'&4dTq.he+G\n>\x0c@"~bWZM\'-\n]CJi?Cw\n_]d0iS*AR)!|T9[aYb=\'O\\Ubi', "aYb='"), [49])
    def test_case_1023(self):
        self.assertEqual(pattern_match('@24f(NNw[)Uz\x086?DTK5e%D|"/t!WEn\rA\rT=2}r[49@JXKMt/Ha/7m[\x0ca1%@r', '7m[\x0ca1'), [51])
    def test_case_1024(self):
        self.assertEqual(pattern_match('M{"HM\'c\x0bkQp7mc@k|oo.nl_s\tTLZBq:[r<\t^K#;n *>Aj}r!a9"~^*;vI~i7aaiWJ*yUNSa7.&$K c [\x084_,n$V@TaIah=q+\x0b5', '9"~'), [49])
    def test_case_1025(self):
        self.assertEqual(pattern_match('HcNF"}p;[40hx3mP1XKdye`}i\x0cLph\nyVm,WF46x\'+SI!RL#:{\x0bCCa,jhokx5ku/9+gdh-MRN<l^"7alh;Bq.#NDk', 'RN<l^'), [70])
    def test_case_1026(self):
        self.assertEqual(pattern_match('~?"<JN\\$k^\t^22BHn.ks\x0c{*(\x08&9RG\\}_\'5u:z\',="&|e\\JE`oQ|+=Pn*d\x0b/F,yI[h~8H\tehTU1l9l}y#=B7o "A:yk2oiF%cU#V', '9RG\\}'), [26])
    def test_case_1027(self):
        self.assertEqual(pattern_match('!!od\nl=bKv>jzJ \x086,kp9FoK2q[a0LOUO4N[i<:xdoUqm*a;OooOw\r|ZD/(>7TP"C^', 'w\r|'), [52])
    def test_case_1028(self):
        self.assertEqual(pattern_match('h3cw/\x08IO@L9\r}ifKwG\tS1exkR\x08#p=c-U\x0b!/ONP_4zz^.&+5T)r4b\x0c"1\'\x0c', '/\x08IO'), [4])
    def test_case_1029(self):
        self.assertEqual(pattern_match('&9j0y;i$Q<#;<<X%,U\t1$\\CB6N2<<;A@I-5Z\rTw|c1uLM6k/yEd\r^vaw:h%L|\tl{wVmK-]80\\sGf\x0c+];d*KWrx', ':h%L'), [56])
    def test_case_1030(self):
        self.assertEqual(pattern_match('?\t"6<w|L/=\t+$\x0cloY]\t:d&PZDS\r2feKTDse7BSz|yD8\'vIChrE{nH=LP\\G+cD=xaC=UZ{-/85)$+&=?t5&nKWF\x086@\x08mT)Q?', 'S\r2f'), [25])
    def test_case_1031(self):
        self.assertEqual(pattern_match("Wh:_\tO+Vf\\oKINGJsG{)?7lLCr`!rIg'8KeEd]R64\x0b)x]z|Owni\tU2;6E[-", 'Cr`'), [24])
    def test_case_1032(self):
        self.assertEqual(pattern_match('*2}C"j!;}\trbU}+<\\%~6l{B(Kzm<x\x0c/FVq\tPU1H@9tUDQRZ$%\'ey_,0^zkIFBV', 'PU1H@9'), [35])
    def test_case_1033(self):
        self.assertEqual(pattern_match('V&U;q(-~jI\'`B-<Q?H\x0bnRA-I#|ObK\x0bs+JBe,rkH(Fmr\tM Pr1>u0|@J*"', "'`B"), [10])
    def test_case_1034(self):
        self.assertEqual(pattern_match('Qnh|)ZrI{4x8v3;C>*E%#eCT[xd.Xzf\'nYJnOPpCB9dqQ,k&sU"hI\'v1hzY2D+', 'v3;C'), [12])
    def test_case_1035(self):
        self.assertEqual(pattern_match('Z=\x0c>{fm\x0cRKFmKLsL`fM|-LP\tWiEx>V;8k;^zW{.R"D@AUN1]\tzTdW\x08h~\x0cU=L~\\fvJY0psdM.j]*KCP%"3p4WV`eZBd#,hzLDO', '{.R"'), [37])
    def test_case_1036(self):
        self.assertEqual(pattern_match('^&iziY>NKPb7Y.Q]tSG\\Q?tsLOKB3W~skjoXV!?n6(M\x0c"}u;nf2}%>o', 'joXV!'), [33])
    def test_case_1037(self):
        self.assertEqual(pattern_match('[\x08J_Z!rK/}Sq\x0b\r|4yFr,lVeX\\Z^BZ{d&BvYg_sn7\n!q:0m6C<)>5W~LZcl?;Z', '7\n!q:0'), [39])
    def test_case_1038(self):
        self.assertEqual(pattern_match("G/sWKQ:{/]b@7L%E/tnz}j')c'FP/7`}~ykf-\t3:\x0bgs|Ob&*\t\t:)=$KKSnif\x0br|c|=/d", '=$KKSn'), [52])
    def test_case_1039(self):
        self.assertEqual(pattern_match("{snjsWg4_2Ywh8 |;Kc{x<*\t1bm\t]l`>\nB\x0clVW%)fAfLci_S\x0cm<79fkac -\n%c,Hl`R']\x0cZo)1^U^ih=$ixM\r(g9", '\x0cm<'), [48])
    def test_case_1040(self):
        self.assertEqual(pattern_match("%AwIdz7oLn0_Aj{{SaMQ->fS\r ;a&XA})r{o{!0A<&+'kz==A7C\x0bg9r?j;fd[uw=2EGiGK?}b@bif", '0A<&'), [38])
    def test_case_1041(self):
        self.assertEqual(pattern_match('qKL5a6rr8P2e2YeU<}2uC<MAgJ+sbu"o|r})B`&+j|\n5q>+`pG7J[5&\x08vm]d\rZF_0~3DNet{b)U"\t/\rN,kW(DB', '"\t/'), [75])
    def test_case_1042(self):
        self.assertEqual(pattern_match("yl`^\rRu7'*O\\%,M];T6=1p1@?N;0 _*9 CcH(e5|5p~Y*%b@BD-la@\x0b(^uWQz@v\x0bPOR\r\t+KRO{VCeFQ=R?Sq6#C", 'eFQ='), [76])
    def test_case_1043(self):
        self.assertEqual(pattern_match('vJbqUhQ)WX\r&X/#n\x08h6X!AE+L4&/`8TR:m\x0cV~FSn8Bt41@Hy\x08sh~m59&k=7PLlPgxu}d/qPu7KD\tqna3,,<DTD\x0c', 'h6X!A'), [17])
    def test_case_1044(self):
        self.assertEqual(pattern_match('"i;P-%E{#^\'A?z(\x0c#\x0b]<"Hd^1jk"F=R!>g{"*3B. LfG\r\r[PggwrFxKUG\'', 'A?z(\x0c'), [11])
    def test_case_1045(self):
        self.assertEqual(pattern_match('5{yXL`h4\x08:Bl3R6zx!>xXl)Njs:\x0cWE>/-.@p\x0bCPw"1:`Rx*|Xc{\t', 'R6zx'), [13])
    def test_case_1046(self):
        self.assertEqual(pattern_match('$8I]\tU\t 0M1Mh AZ8eJ\x0bnIF]3:#\n*O-s?C=vY1e%-t|lgDf!lP:+;OkP!\tmq-0y6U"5yG\\?*Uts]fde\tk:@KVfn-^zp)1?', '3:#\n'), [24])
    def test_case_1047(self):
        self.assertEqual(pattern_match('$\nQIyTX(\x08,|\nY\\ca\r(9^]\x08FOA+?*c*Bd0m;^404N,=x"LAv\x0bm@\x0bL=!=H]NRC6<$f', 'NRC'), [57])
    def test_case_1048(self):
        self.assertEqual(pattern_match("/Z>r:=X84:>.[\x08M@B7<]2T.6a*(r'dV--UzHO8LOmtS5L,aCg6#EbU,$KTg)|8R?\x0b>`7X4=`Vh#Qs+mdZE*v~RB+-[k\x08;E1\x0cua\tM", 's+m'), [76])
    def test_case_1049(self):
        self.assertEqual(pattern_match('S@.\x08F}<N/@n(AUi?H;j&&bf}@sA{tsw{z{[\\$)!0+W?YQ\'aagUA\ngI\'&"\r(?<6u:O-hI){K.lV"/\\k$vpMP{\t:.ykn(RK', "?YQ'a"), [42])
    def test_case_1050(self):
        self.assertEqual(pattern_match('*DCOI(+>< p*OZ\x0bsaeSY\rS/q)ooe\\xA]}J_k)iqHa@(66mR]aL\r\x08M\x0cDrin(ez6-m]l.3GSN>th_"', 'k)i'), [35])
    def test_case_1051(self):
        self.assertEqual(pattern_match('5\\yC\\fOP*\x08g>yuw>\ty\\t_P@Q\x0c*?TQOFX\x0cla%&}a`0?hv1xy6bV~}.SMg+-\x08WYo(Tnx~<nSER?\x0bj,34K[FOVj4cFkBw[r', '\x08WYo(T'), [58])
    def test_case_1052(self):
        self.assertEqual(pattern_match('gVE3\x08ipry.^E_A>GhmQqxup\r%W<fbAAlK~Yp=rK;mql/\nZec!cM/3SV&[\x0b\r;H:SBox?.lW', ';H:SBo'), [59])
    def test_case_1053(self):
        self.assertEqual(pattern_match('t\x08?\tm>?PRGyoAtTzzaD2r9{<j9IeO*@ w4}nS9=As2A!+x bf=\\/yJ;Jz8\x0cS2V]Px{w\\\x0c{Z', 'A!+x '), [42])
    def test_case_1054(self):
        self.assertEqual(pattern_match('W\x0by)9F:Lp}t\x0bIbO\nI*b_l+)SuQF0-H;?adlv}:Ary75fvH;C_TFwf1(5\x0b(!7uR[MLeI*My9GMC#~-]VDY-{<1G', 'vH;C_T'), [44])
    def test_case_1055(self):
        self.assertEqual(pattern_match(':!\x0b\x0cqtM!PV7b=oyPos(@ayTu{[(UIK$f8:N"w^yn5ms?}&X&\nf', 'V7b=o'), [9])
    def test_case_1056(self):
        self.assertEqual(pattern_match('<ORX$&_`Y)LI}.#lM\nElJ&<,l1\nu6-e3lhm;Z5)\x08D.#hL"HGL5vi}1r9if~} 6D\x0bunuwn\r},1hT\n8w|I&Gn{pe ~~T)c`"cs', '\x08D.#'), [39])
    def test_case_1057(self):
        self.assertEqual(pattern_match('M> 2Q\rX:~cS@\t/eKa6~2W3\rnif;x<a9\\qq[N5^^3$S9no+eS\x0b$.', 'Q\rX'), [4])
    def test_case_1058(self):
        self.assertEqual(pattern_match('Cf?"#HUVrt#n:PML\\%\'Oq^DGZM><\'g}\x0c@Z\x0cHW  /CSZPSZVt$>a\x08<VU{#vpt\t!egN$^_}9Uf+Q^,bGTfz^3lt{~K\'QX>', 'SZVt$>'), [44])
    def test_case_1059(self):
        self.assertEqual(pattern_match('B 6<A!$JVf}]yd,_\x0b#\x0c\n/vm1-d)$!m$XQ3=hdTAP\x0c\x08Ag-D|u9>p6mspKBd\r^r"+3@J0E<3@_a[ ~{AB9O~^oq#J5vL\\HA6ZD', '#\x0c\n/v'), [17])
    def test_case_1060(self):
        self.assertEqual(pattern_match('B*Wfr.K#ff4R_$$\n,Z@1\x0cQH_Ij0\x0cn{]bx\nTd^EWj/\x0b\x0b\\\x0cP#/=xo\\Su )h2SQRN\rFu\tJK}', '#/=xo\\'), [46])
    def test_case_1061(self):
        self.assertEqual(pattern_match('I)Z"]2g5-<:rI*V!Q5iqX$N(a.gAl\tv03+\n >Qv_yN\\~qb ieSZ!(\tN%j+V9({zsU+y\\}Z;up<u>K\rt):~&_\t/4q\'+JE', '5-<'), [7])
    def test_case_1062(self):
        self.assertEqual(pattern_match("r%w||'\n'?Lv\trLCJ5SK5R[~+3\rmp2s1Ooh8P=bB|Z\r)]0GfTC#%?`%X<K9d`hS6UBi7KQ0p", '<K9d`'), [55])
    def test_case_1063(self):
        self.assertEqual(pattern_match('o@[ \t\t[\nO!$Z,0PS7Pv`e) b7i#@fyO87LSi\\b\r=^{%9IlfI)y\x08w<`.3dUq', 'Z,0PS'), [11])
    def test_case_1064(self):
        self.assertEqual(pattern_match("jX\n^G#E`4Z33k|n:Zs.<?\n|ZvSkz7<C&~Y2K`F@GD'L<dJ*_m,bI\x0b3mH|GIMsHo!iE", '7<C&'), [28])
    def test_case_1065(self):
        self.assertEqual(pattern_match("\r.zq&?\x08P'\t6C_uu)BVGH>I-jhHeJ3c7~/02SKe6oyZAEXP\n]4gB8[km\ry.K/[", "'\t6C_"), [8])
    def test_case_1066(self):
        self.assertEqual(pattern_match('-0$F(\r\\gD<4\x0b=\nWo=+#jO.j^i5(u#\n7\\1]^0"pm9O{fc]8\x0c2wptE:\\\rwA|}y{8\tJ=G]bSr&\\:p', '-0$F('), [0])
    def test_case_1067(self):
        self.assertEqual(pattern_match(" E>U+ZQUcQn:y: 'B%`siYTH`Ke`x'#KX#1|=s0Lv$wB%lyI\x0b\tAu`T{'4&(t9A4~{{]o\t)wu&b?$Un2%Qn~XK!P`7:", 'n2%Q'), [77])
    def test_case_1068(self):
        self.assertEqual(pattern_match('8BV"\\JKOAg+P%k%Y`(FeV-ML0Du"AuW_n3k60:^k\x08@ Bb\x0cRFRLe7$zt!?QZ??%K*P#V6O=94SiDi:(X\'^o`&{r[%iKgxCuhy+', ' Bb\x0c'), [42])
    def test_case_1069(self):
        self.assertEqual(pattern_match('.o\x08~`\n\r\tm!B$n=T?KBlrp{6F\x0caBr6qMnd1\'_T;s/\tY!/W0u$\\\\F$\\?^X{5WLYp%*(JqU^*|~f,t@"Bhrgi6[t}xG$^', '/W0u$\\'), [43])
    def test_case_1070(self):
        self.assertEqual(pattern_match('6(\\^oHPk\r^1\nLxp@K$9\n\r.VC>"2`0p37-zw/*fT;_2ImTv@=UKtYWvo~G .$r?a]3q<gG%\n4P}o\'B~B(X\x0c\x0csTxt~Qn', '\r.VC>'), [20])
    def test_case_1071(self):
        self.assertEqual(pattern_match('[z%W1AA=Tjfd|gSMPiIPd0^\x0cNY]Z#t}fo\x0cF>vlV:+?v[\r\nETKwtjm)BEQyX!h^62n\r`\nXzr', '^\x0cNY'), [22])
    def test_case_1072(self):
        self.assertEqual(pattern_match('{/Ac.8"^J&ZO},\n)6b2x"sC|.s!/-\x0b>\nDPuw*9RG<1I}(`;,U)O"+', 'C|.s!'), [22])
    def test_case_1073(self):
        self.assertEqual(pattern_match("\x0b_iB[V5O{I-0/VeRS{J*hxy5`F)Ij6(M63\n~b*d\\X(\\W2ghdk}aZXDUXJx!;ZDX'", 'I-0/Ve'), [9])
    def test_case_1074(self):
        self.assertEqual(pattern_match('AyE#9/\x087qA\x085g:n"%]\x0c)!+z}t*&\\&6U\\b75O\\ti~mYTJt;;=x"6T5l|o\ryxF4XU#Ck!Dq~%*\t', '"6T5'), [49])
    def test_case_1075(self):
        self.assertEqual(pattern_match("5&<.\t;M7f8#GBB\x0899[D\x0b!zA'CT`8DooBd\x08s$1lh@dm.:@L\r\t$0#]+\x0bnK)u8$l7<0xK'\x08F4-\\Z*XMhM", 'T`8'), [25])
    def test_case_1076(self):
        self.assertEqual(pattern_match('NmIoLfR\x08;{*SEBpYIYTGM)"R=\r2uOrZ]\rI$>1?RZGWFjR.!A"grt.;A#~eG@jD6~=Z"e3k,pr\'R2MiVk/tVE\'3_][H', '\rI$'), [32])
    def test_case_1077(self):
        self.assertEqual(pattern_match("qT}H-\x08(Fs^.!mTJ_&BxeLl-NSiw,X9!7C}>Ru !SHZHB`{Pa9' ly{EIvJnpu@71F9shvx#\rES\tM:.VTm'KjXOfQ\tl%", "9' ly"), [48])
    def test_case_1078(self):
        self.assertEqual(pattern_match('.\ty\nfN49W-cHO#]te+8{\x08V}8%H}`}\tM"(mcESh(+J]YjoNJtk0j{6nWS\x081>MY>=O4,x-*Anu\x0b9S(G?/$1CH', '\x081>'), [56])
    def test_case_1079(self):
        self.assertEqual(pattern_match('bHN*p\t:H?B}CQs#\n\rUdNeAR1t*HADD;]ltRtMBcS{aE}X"[3o]Ac}rlJ', 'H?B'), [7])
    def test_case_1080(self):
        self.assertEqual(pattern_match('RJRkT3Q<s^\\IG>T([S%`cRR5\x08B"s\nC;)5*?F]\x0bPny=nA+@oW\t-Z\\\r;0R\rapdW;S\t`EW5u4 x', 'y=n'), [40])
    def test_case_1081(self):
        self.assertEqual(pattern_match('"ZU-\'RiQ1$bv&.t;ajLI\x0b=B"@qNN\x0b;R\nt#ik!?&3xx57H*"R6\rvZE\\<+E0JRW.#^%B%I!K{6(H |2#?I44[M', '57H*"R'), [42])
    def test_case_1082(self):
        self.assertEqual(pattern_match('2\n4#!d> $\x0cT7V?<g/"\x0b!r#S#^ggiB<2"UZ@^|WIJv;OkmO)!Kn>yOE^W\'x,(Y+?K\\`h-\x0cH ', '+?K\\'), [61])
    def test_case_1083(self):
        self.assertEqual(pattern_match('U_3[-G78;I30K&$-7uc$w9|!|H]A(Ji";\x0cZSJ E!\x0cS696\\4abvEY/cL*}48D}F\t}e', '48D}F'), [57])
    def test_case_1084(self):
        self.assertEqual(pattern_match('6>=:)g>-yWM?\'Tfpu!MBOCH6GL<6"Iaq\'mzE]=pADUN#3RS\'%l@9k$\nxt`!qwCB\r2O\t)Y}i', '3RS'), [44])
    def test_case_1085(self):
        self.assertEqual(pattern_match(')Z}({D~1\nNTBy\t\\Ts+.QdG*Yyg~fDf"vQ<)+z3cI\\\nqyRIa;\x0cn#^', '<)+z3c'), [33])
    def test_case_1086(self):
        self.assertEqual(pattern_match("bn%:N'J/y.:J-V\n;$gQ-XSEIHT{<kp9Wp$x?#(rti`^LB}V^5BgJYC^zE?!,GzP*e*A>Yhq7\\[aS;w'4B6c5wj_3w`_)kd/T5M", "%:N'J/"), [2])
    def test_case_1087(self):
        self.assertEqual(pattern_match('&b;1K5\x0bjp67eW\'CN`\'J"O[T~[laD\r]&:0H}*~wF8v;R:2)A%-9t*0Du\\;Q,-Cw>DG', '-Cw>DG'), [59])
    def test_case_1088(self):
        self.assertEqual(pattern_match(';<y:PtGpZ\'s<d\t~3|iw?1-x06\\XN[O8",?\n(+$v3D\'Qu6}Wqx\'qcUR"nC\x0cCdx<ut"U^k\x0bKgYL@Pj4qc50\ne4t@\nG#t%Smu#*T\t', '"U^k\x0bK'), [64])
    def test_case_1089(self):
        self.assertEqual(pattern_match('b,g~)7fw#[]LC^\r_~r&;*\tYk!};4?tuzVpZL/&]5:^xCco0s{[B\rS#j*4?@j2pCGHg,M9< D<a"s\tXb Ze', '[]LC^\r'), [9])
    def test_case_1090(self):
        self.assertEqual(pattern_match("BM8#/L:F+s-=*UQ!|jY76qJ'aCAw)6dW7hu=KuN6^pJZk]1\\;!CJT<@ik9}tS76EIEXn|i-Hf/k~leo\x0b5m>Fp.`+7\\Y+KfezY", 'CAw)6d'), [25])
    def test_case_1091(self):
        self.assertEqual(pattern_match("jO,&;5T5p?u=$\tuqs(d*E@Q=AW\tp-:}b~s\te\x0cn\n{\x0c^KBW$j6,{hyt>\\cekeUTIp{\r\x0c'\r_>", '\tp-:}'), [26])
    def test_case_1092(self):
        self.assertEqual(pattern_match('$VTO1Az.\x0cRD7Ki1g-%nTw|\x0bxO\r<{A\\\nbK\n\x0bw,bGQq \r8\x0b\x08L=\x08J{mhThwDW', 'hThwDW'), [52])
    def test_case_1093(self):
        self.assertEqual(pattern_match('4\\:WmgH?W[V,MM28./]l*ySl7MFxN2:+\x08sI]B34R/`O!O4@_3M)qv6|Lki5bOO\x0b})s', '/]l*yS'), [17])
    def test_case_1094(self):
        self.assertEqual(pattern_match("Yo5#sDf|\x0cRRIo-/M\x0b(T%Su59ws[f3&s?YD2bt$_j0*sL$EiQjz&leG4bD_\x08p*g1)5C5F=E\x0b%p4G3$}'l1FB", 'D_\x08p'), [56])
    def test_case_1095(self):
        self.assertEqual(pattern_match("Cl_`'Q7T$]Fv5[\\Tm[\x08\\Z3h.e`x\r ;9VPO.Y*\n~~DQQO\x08&4\n&=3Gxh}(EpR[#~@ikk@H&xK t?$2jqoM\x0c`!J0\tj|6s_\x0b", '?$2jq'), [73])
    def test_case_1096(self):
        self.assertEqual(pattern_match('ROM@4\r;r7a4elO\x0b)}vP\t-bxm.%S@2JN;=e"7l[{.5\'p9CnPK~\x0b33A\nx2/91 &}VG8.W7S4"\x0bX/w5-<XUk+V?3u2^}', 'vP\t-'), [17])
    def test_case_1097(self):
        self.assertEqual(pattern_match('C6^n~oi:tl\x0c#XZMmJcU;.Of|\rTcLsC5w\x0bE\x0bz\nvrz"5^-Ei:Y\x08mU8EeHuo&:E#\r2Ms~EbCBAvUnl=`B=Z=7iITPOfHJ@Yu`y:', '@Yu'), [90])
    def test_case_1098(self):
        self.assertEqual(pattern_match('O\x0bPM~P u3i_W2$Pg\\\nztBBh-q!4_EC\x0clN;m5u5~~#^$M8l!RxlS;"\n~,iW\x08\n)*etZ!EPN[7l,fQAB\'i$e\'LN<yqQ8CnJ9GD\'),\tx', 'lN;m5'), [31])
    def test_case_1099(self):
        self.assertEqual(pattern_match("uNtcN%+#^}\x0b^Una'vpRM,.)(:yxqHu6 5Kv;1ypmHgT?Eov{|g|]Y[,b.}P[ABbO=,uAu\x0b", '6 5'), [30])
    def test_case_1100(self):
        self.assertEqual(pattern_match('{-ALtr`3B~>lZ0DdmjDWq_&ssBDPI=o%BE;RNmsca\x08WXr(sdx5NO cdEy0#e2ZJo)>pKa#*wtM', '-AL'), [1])
    def test_case_1101(self):
        self.assertEqual(pattern_match("_42{T+:wncNDCV_Z7(2sy6tZ{\x0cktH>Bd#!1*c9UH]P<xL\\\x08O`c'pS!~?#g_!Q&GM1js']q7zj/Swn-O/", 'sy6'), [19])
    def test_case_1102(self):
        self.assertEqual(pattern_match('6=\\9(L.?Wrq7@W/c=%_"n}"5ug&@vv&;Vh<K~y"q[1/Y}Uwa.#U*SyY>e\t,gqr9KmJ\x0b', '"n}"5'), [19])
    def test_case_1103(self):
        self.assertEqual(pattern_match('^!>ER0:pkHjd[ccmx^boR Z":w\r1ret{\t>6X/-n(2wq%yOy\'=Z\tk6ocFLJa7>+,N||*!B5~R`$', 'LJa7'), [56])
    def test_case_1104(self):
        self.assertEqual(pattern_match('w>"(5s3H\t7qM.g((:#\r,U{\x08Q)I=Sxd}t,TpGM.Tje4h\rlh\tPQCCK+?p[C?F:%.7g%q$5%w%\x0c0$vg wdAemt`^dH+\'E4p6Kz~%', 'M.g(('), [11])
    def test_case_1105(self):
        self.assertEqual(pattern_match('Kxdk"\\0JP\t\x0b,J\x08-ETZ\\P(2lX"JW))@HJDdwxB,sV#\'ShK/q\x08$w7k$+U{*~?X-J5<9DaAH2P.Lb$\x08\\p.UK&7ko[\'zJg+}!`', 'X-J5<9'), [59])
    def test_case_1106(self):
        self.assertEqual(pattern_match(')m:c+eQ.g 0\nS]<sM\n|I S}Hij9\rmsV;s\x08yU|U#~g95h)b@\r\x0bx=2NOVZB"\\UcI|!\x08^', 'V;s\x08'), [30])
    def test_case_1107(self):
        self.assertEqual(pattern_match('"\nE=&:<+*a[;?Ci{`kAQvE\'d@b.wHk0?)_"02*lmsA+{3P=Yz:!TLK`h|bOcJ&\\Kk-#b', 'kAQvE'), [17])
    def test_case_1108(self):
        self.assertEqual(pattern_match('\x0c&{G CJ0W-%d&t6\t,+\\yH|g\r`KeQPexKhWT#?rE#\x0b JaVUP8p\x0c|E\x0bot\x08?uT{w+PcNp\x0cc9lS"s}G-m\x08GP%\x08esX;9#', '\x0c|E\x0bo'), [49])
    def test_case_1109(self):
        self.assertEqual(pattern_match("U\x082q~vps='%pDu|`n{$??y~Q|q7&ezP._9S2K5?xl$,Uhdm20P,9\x0c@60EC1p", '_9S2K'), [32])
    def test_case_1110(self):
        self.assertEqual(pattern_match('"]I~tg@$0H\x0cG?jM.F/]0jNcs+iNf_Qnf>S^W\\88S?g:Q<rCw([e6,8d[`~I1<+_ /htP@w3.U&d3eAGF^^}g?Et\\Q=0', 's+i'), [23])
    def test_case_1111(self):
        self.assertEqual(pattern_match('\x08/:[7YGSM<eVx:t*ZDAr\nb^5;e0i}K6p1&SE1#i`6@0NNHGRX\\\x08)tZ>Jf?I6[(\r%C1K"r$n\x0b\n.Xa`e=q%NTS\'ME/}', '\r%C1'), [62])
    def test_case_1112(self):
        self.assertEqual(pattern_match('5Q"$SY|C$hZW{\\6X!E=k?;}>W./gmFqE/%=-lH\'M}NttG5JTM3kj$Vkep-L*KH3:?ZI', '?;}>W'), [20])
    def test_case_1113(self):
        self.assertEqual(pattern_match('FG\tS\r/qU2iycatr]Y}~4*26q3.yA~<#pN\nR08\\h_Z0P:8]v~V-\x0bkZ:[Av^ls\\Qu^x3\\`Fjmt', '[Av^l'), [54])
    def test_case_1114(self):
        self.assertEqual(pattern_match('2I#i*d*-T3iy(2^XBj/<xfHuUr-a?f.,7ik vyoZ{53$~B!{]iXg5|B`h*%)Y\n;f-1)Zx+(X|G/o)>4y\t<9"\r\x0bmO:L g}', '5|B`h'), [52])
    def test_case_1115(self):
        self.assertEqual(pattern_match("f_W)$zF#qe,5#j7=FZx~\rb\tQ:2pj\n/#F\tX8#O;+y6I&[;Y'~J1", '$zF#q'), [4])
    def test_case_1116(self):
        self.assertEqual(pattern_match('3i<XhW!5>qUrT%az.-F^fow?DB p\x0b]oYmG@RS2YB+,4`\r2qCkp]XgY$\rwr ~rIlu%/LnL\n7+.l^s=ZxyG\x0b;n,`(vQ\x0cy\x08]\r=.*aYu', 'qUr'), [9])
    def test_case_1117(self):
        self.assertEqual(pattern_match("B3KD&nwQ*h\teO!%R*#K \rfmef9\x0b\na;mZT\x0c.@=czd'<Y>dM~]L,]laRe\rAuV", 'a;m'), [28])
    def test_case_1118(self):
        self.assertEqual(pattern_match('j%`}7\x0c\x0bY2"qgI+iPlWx5R]/u*~q+J&vtG;n]OqEQdG~7{L\tP)#!6h', 'G;n]O'), [32])
    def test_case_1119(self):
        self.assertEqual(pattern_match('mq/5.7YH0,T],2*ejto>$)?j*Os9\\aORUG05c{FL6\tp/&r=31X n<Qnv"\x08{?w6a~=}0T', 'nv"\x08{'), [54])
    def test_case_1120(self):
        self.assertEqual(pattern_match('S}k7: \x0c:(\x08_fCw*2Apgte@y,<YkXNd2QZW/d{jn^GJa\r_M{h$>dy^Lm]+V=bE<_YHR:h+~', 'w*2A'), [13])
    def test_case_1121(self):
        self.assertEqual(pattern_match('Q-w.P3E-?@~ss:hLCd^4m5=1ujdf{`ln)X?xe )\x0cPgTKu\x0c57tN`A\rv+Y3pA1S\x08R`5W~\r[T\r,|fM$p\nXus8TH4MQ&HEKijI7bo29', 'ss:h'), [11])
    def test_case_1122(self):
        self.assertEqual(pattern_match('_PK>`6\r.zl\x08 H&:+|"[,nx\\GT?JM/g\t@qefrZ@~=dv(rc0\tIW<ZZ\'(B;i<5oP|!a*%TEo9T;6^\tw', 'a*%TEo'), [63])
    def test_case_1123(self):
        self.assertEqual(pattern_match('x``thIHq\x08I2LhG7\tH^gFU.;"~w/|6Olp9Z=A2_jq^-m^Zt>#l|AU7r4a\trHQ]SPp,,%KDUtQX^%S6m!QgW:1%\x08("lIj', '6m!'), [76])
    def test_case_1124(self):
        self.assertEqual(pattern_match('M\\8!=x]km0w20/XK%\x0b>S(!9@Tah\x08B{/=]AM9:>J<{fADaVk&vdStq', '>J<'), [37])
    def test_case_1125(self):
        self.assertEqual(pattern_match("Kv>e-S%E>>TL{zWk\nE;3L]'^WrSNmd=wOQm{\rsyg?enzsv5&Y[^PmEd=B4eH !zrFf$0_pv\\CmPCc\nXV?L\x0c&B})'", 'Cc\nXV'), [75])
    def test_case_1126(self):
        self.assertEqual(pattern_match('/cOZwczF_g>\x0b..z^KgP<9\x0c:_Ql`%9cXkb18_y8Q~}/"S\rfn9<TE\r>#Xx[PL$*l,yhg8\x0c8t}Bx1y<| f,4\'~\'iy2', '9cXkb1'), [28])
    def test_case_1127(self):
        self.assertEqual(pattern_match('+3erz68]m\n4M%xIU6I\rXLX*to\n }lt8Cl\x08#$TYPmA2tg 6\nSe@$[Q}2 8%q?;X@W_cu{8}`JKLX8|^B3\x0chv\n!g\tmUq37nR\n#s', '\n }l'), [25])
    def test_case_1128(self):
        self.assertEqual(pattern_match('u_u7kESX8\x0b.SipR`8X".g9<`S([_$d90\x08(zhz *Ij#GS/{^@~./}D1@y3(\tojn+\nGdqt=rsJrxkCVKv4V1wEh\x0ccd', 'z *Ij#'), [36])
    def test_case_1129(self):
        self.assertEqual(pattern_match('ZQ6R?}|\tX1rHKG?E/\x0cUm[A\nr&2P9z;t=`)>\n$zO9hC*68&]$[dGmJ\x0bK}$\x08EPOw~4)`', 'P9z;'), [26])
    def test_case_1130(self):
        self.assertEqual(pattern_match('\tp0x-Su4Ng8&b^odX{^PklUSkZHb""CZG+oKK3wa\t6{$qs,d\x0c JNv5b', 'PklU'), [19])
    def test_case_1131(self):
        self.assertEqual(pattern_match('fu74dVbW8 ,B+|a>(K$!&Y\x0bjY.=*m5|ZYXp8XCLL}`[`)G["6vW%,2dV,Nt', 'p8XCLL'), [34])
    def test_case_1132(self):
        self.assertEqual(pattern_match('\\5T^Md*$PS\t=/>)sHn@K{<tk|nb5(AzE7RU;.z=\n PwY\x0b&2@Q^=l\x0c:.Vu&k# \rrj\x08f`8pUif2z-dA1C${F\x0b`"}]`)eQ\\+fg#9/', '\x0b`"}]`'), [82])
    def test_case_1133(self):
        self.assertEqual(pattern_match('yq\x08 :}[|\rK"/e}V*wdp0\rz$<w|C=$oJV7G\\-+&9p3Jn=DI;{J+l6m\\quj]:SX_B>(ZdrYz9&Z[PtZ', 'G\\-+&9'), [33])
    def test_case_1134(self):
        self.assertEqual(pattern_match('@(YQ5`\x0ck8o\t<l:%[LE{q"_"a\n74h\tE^vg\x0bZ\'8CO~wbf3xE^t.o68X!4-2y;z6b`[`\'sRE"\rLAO|#EN:#.2N,<', 'X!4-2'), [52])
    def test_case_1135(self):
        self.assertEqual(pattern_match('T~uOKzlNgh\tw xjKV~iZ|{\ndYNJ:FV;jk`CuAiX0\\)S\nd\'*}=_\tWL#D?:cqUR,/;#uSg\t\n"\t`EQ', 'V~iZ|{'), [16])
    def test_case_1136(self):
        self.assertEqual(pattern_match('\x08+-&_-;p\tD^Y6u6!`9roJ.vn6k)Csp{gjVY8\x0bnC4`\x08Ng$\\^;uZ+76n8G\x0cUEx#5qzSy-Nwf?.XRQ-Lnr#\tP!(v/i< ', 'RQ-Ln'), [73])
    def test_case_1137(self):
        self.assertEqual(pattern_match('[[wkO#ir\\m]:,2Rr\x08Ri5cJT1&[P9uX`}L,9#<?<[C\x08vYYQJdzn{3?)C=M{sfAU\t1RD7}m37l\x0c;8;\'efe~D"3', 'm]:,'), [9])
    def test_case_1138(self):
        self.assertEqual(pattern_match('V\\[mBZz[;a\x088D$)oULUPsOi{WTkw?NLbOB)2"e^KtNyUI{c<.:\x0bdB\tNT$ \x08!^YCB#c.(ouFrG', 'BZz'), [4])
    def test_case_1139(self):
        self.assertEqual(pattern_match('BU(OB-yhV\x08A<$:Tuae=>"RMzA\nZSP|\\ko<2Elf(Ro,\rm\x0b$[<!6jO>\rFj R*f*ryVYM{4uJ0S\\pNhu`QjsTg_-^\'+K}o7YdO9', 'Elf(R'), [35])
    def test_case_1140(self):
        self.assertEqual(pattern_match('-^?Q\x08RvsnL(a4sv\x08%P^*N]6L)-T!b_kF?:vx#.xC9R\x0c*j1q+9h 17_j}Pao\\A.3tpYV\\9rvY4P,mMac2s`$', '(a4'), [10])
    def test_case_1141(self):
        self.assertEqual(pattern_match('FGhcp%=U4\x0c_9hmIs!G%9b|lQTNLaot1sEL?ytP55a\tF[TPC0DjvxIcy,1-5C+U#1]\r.5+TYIO3', 'QTNLa'), [23])
    def test_case_1142(self):
        self.assertEqual(pattern_match(' H~;Lym}*61Y~wt\\}6lvOIH-jD;\n.BhiF!HA*4aNdJlmpK Y%P|=&Hy7*|t{Mh/3;H\x080W-rpn"%8M\x0c1\\8Ff:4}HU^\r:Wy', 'D;\n.Bh'), [25])
    def test_case_1143(self):
        self.assertEqual(pattern_match('Vs_`JuX}XIHN\x08tl7h!]v\x0bE#EnQ_:qv3!#z]VZWaeEZLiSC+pAlW7K,D*}xw"T1\n8{R\x08?HpY3\tqPfM5~', 'xw"T1'), [57])
    def test_case_1144(self):
        self.assertEqual(pattern_match(' vQAH):_-,S <$\nT.#AD&wORu*f;G}sK7_JsNW@hB9\x0b<y*)cUWav', '&wO'), [20])
    def test_case_1145(self):
        self.assertEqual(pattern_match("\x0boPyd \x0bmA%Ze=}h9t_iSe9/+\r3/zQ'W\tsA=B= J^a\x08)%5EM&\\>#\tu\x0cRF~OqUy9u\x08X=od(S6|m{TY:rGut\x08yUa!>Hy<ld!vBg*m0%", 't_iSe'), [16])
    def test_case_1146(self):
        self.assertEqual(pattern_match('vf?^R4X=i6\\-$>Vx\x0ck^g,W1ADf.mu7yy//mC\t]uwA[<hX|\\eK_6TH9+??(F;ksM_\\(Lh\x0b\\%50\x08', 'mC\t'), [34])
    def test_case_1147(self):
        self.assertEqual(pattern_match('x\t&l%$v><,V:45T\t3:f{n!{;VLzz1zGm\npAQ2f4{/\nmP(4wb%\nyA', '%$v><'), [4])
    def test_case_1148(self):
        self.assertEqual(pattern_match('\rT9H`9`@Y.m~.\x0c}F>!QI-,}9:oaS!dplP@E5Xn?,+y&=cP"Ca7a_oDo{4~.JnPs"fl}BF]`x|4)"+t4{pP@O\'<NJc', '"fl}B'), [63])
    def test_case_1149(self):
        self.assertEqual(pattern_match("c=FB(W;\r\x0bi5Fc:P>8HlQ?%D1sVm/h\t3yg'WTx\nh\x0b\\KHx*mK'@)=pD[63Tw+FFxm=<J:H&TBKDQ$6bq\x08\t;\x0cQr:\x0cWWsI", 'm/h\t'), [26])
    def test_case_1150(self):
        self.assertEqual(pattern_match('y.>D]G^)O2R$QGujk7)\x08<KxV4bt}>H@0"B<d]?L%dW8hP\\0NMG)>Mc-QN^Qxl`Q', 'B<d]?L'), [33])
    def test_case_1151(self):
        self.assertEqual(pattern_match('nWU)$G!&R!o@4*K%yq0(E9+LXHm#TwuxSs!Z~Fvr3:\x0ci>RM\';?Z(v-QNsB=\x08ur(fn|^+.-c_B2\x08"Vm', '$G!&'), [4])
    def test_case_1152(self):
        self.assertEqual(pattern_match('^\x0b/3=$@R=i]T3kM\x0c>6$N k\taFL&QRG8s21Z/;!SzVCVZ|fj[Gs\r=Kb|;b5td93\n-4O!', 's\r='), [49])
    def test_case_1153(self):
        self.assertEqual(pattern_match("cCQNFke-\x08/%u!FDbNzx@CUUm0`88>I&'w^7zzDOLvOJ7B~iok=v\x0b5`-6^3#k3\rFMM#\x0b/{V<\t:!l;ii!`j$Jf", ':!l;ii'), [72])
    def test_case_1154(self):
        self.assertEqual(pattern_match('d7p,^` R5\x0cCW@L\x0b{\x0c}=pa(\r\nQ}:a+:en\tj]9w$n#+!|q_TC-z\x08|$5P:', '\r\nQ}'), [22])
    def test_case_1155(self):
        self.assertEqual(pattern_match('X\tluW\\F_(\x0bW=5=prVfUh$%9,aN,)]kf)%tf%NIFF.bI"OfU\x0cuG1o+,eP/T', 'f%NIFF'), [34])
    def test_case_1156(self):
        self.assertEqual(pattern_match("\twwv..Vrj^5X+tWm&qEm\x0cIy}knwe\x08Ru kMw|@9gpOxyU+h!Wm\x0c*YpcH|23\x08Lw8tS\nB'ZgYlT[T", '^5X+'), [9])
    def test_case_1157(self):
        self.assertEqual(pattern_match('S`hvZP\x0cV{zwi|fAAyD-#(%4o>U,{(615j*N`cw\tx\\N5d%c~2z0FC\tv', '|fAA'), [12])
    def test_case_1158(self):
        self.assertEqual(pattern_match("1}CL\nj\x08@Tw9iK2B-QHj3i{2C$)QW==u-KJl+TXVDw*[\x08Z@KKS8GESOG%T247 d@o/3LO'9$!JKUg='wRLihtVc:v", '@o/3'), [62])
    def test_case_1159(self):
        self.assertEqual(pattern_match('`P312\x0c?m\r<Oz{\rEat7}\x0c5j`-.VF[g\tS$uM\x0cE8"\')LF\toI#ht\x08M2-$)iba0].\nD:j&P%gZH', 'D:j&'), [61])
    def test_case_1160(self):
        self.assertEqual(pattern_match('#ypacZ)G(vUbR\x08s*k^L7h`K4X4Y\x08.\nVFWM`x7A`tYQj{ZSC;g0G.\\E`\t\rF3\tlglP$7-6-^b\x082Tfp6o.s\nD el\\dd&:UspOv', '7-6-'), [65])
    def test_case_1161(self):
        self.assertEqual(pattern_match('D0t\nq"Q<(m\rC\'LB!bX=HC)K,W&)\rDd5bS[BaolS>\x0boG!Nr*gV(\\!\x08m\x08bug\x0bn!rwK\x08eLYks', 'bug\x0bn'), [55])
    def test_case_1162(self):
        self.assertEqual(pattern_match("(OO?'c:ZaV]{vi&j!Oo|yH/Fu<8G}\nu{,f@sS2MYtkOh'\x0c$i:$qZ=b}U4lAPuF4{ViU&id5\rIPZVqWhj9=AsPddp`BK^/2", '{Vi'), [63])
    def test_case_1163(self):
        self.assertEqual(pattern_match(':y`#%@J"3`~#E3Tn@Jt\t,$l\'tJ*,3cwyD-Fm tL2lVc!^4#>WU n*Sr~7o8K\x0cs:7"L^`v[=l!', "l'tJ*,"), [22])
    def test_case_1164(self):
        self.assertEqual(pattern_match('=R9U7 wXU-];.>c=-Ru3jpzwA+^%ky2/AI}s@z^y)p5$P>z\x08Zh_@Y', 'ky2/AI'), [28])
    def test_case_1165(self):
        self.assertEqual(pattern_match('+s:R6(yz"RW#R>Ud&$Ln{L>/h\x0cxp7*=2R71#%r|$4\x08,;YhGs=m-5:>\nO>V!;iZbzn K7 F[(\'088DOp\tgaia3', 's=m-'), [47])
    def test_case_1166(self):
        self.assertEqual(pattern_match('2C*|;jnoLrv:0eGQIlG-2pcNYk3ZhL5?bV}4W1yJMn%1TMZ\x08F{z ON\\=s82v]\x08w:\rA<W<Z3tO#x m_Yn)h[Hq\tXAW@h)) ^S', '-2pc'), [19])
    def test_case_1167(self):
        self.assertEqual(pattern_match('Eh2Z3ol0`2b\r9Z=J8B\x0bWtX\\WNurDg` l()zO\r5s+Mpz>jEa3R6v1Fx\n+  ^t})js)l.XaSf;O~>-\rMxJ9SLk_o_J3~48.esY\t', 'SLk_o_'), [81])
    def test_case_1168(self):
        self.assertEqual(pattern_match("0s>PVq>nPJ/8^u/YBQUR63m`sUA'@6P;U:K=G1\n}XBv odb\tcqkw=q(*vaM6\x0c'LXW8aM>\x0c(kh\r/j2 k\x0b-_{Uj$ CV", '\r/j'), [73])
    def test_case_1169(self):
        self.assertEqual(pattern_match('@M$q}*\x0cy\\\';_[a>GF2nOi|#I!Ufr,pDw&TIiFn1&wIV=L058s!8#Jj4V*\r\r\'\x0c*a!MYG/qr\'w\t"v!j\n', '>GF'), [14])
    def test_case_1170(self):
        self.assertEqual(pattern_match(')RVt}G)>\\#G\x0c&\x086]FO@]e>B}+\x08$Y!Iz_2)aV4UNi*?_CA%)LY</9k7IUAAF3XzR82tCv>(8DV5t<AgGsp/DkI|F86%|3\\53$wWHl', '7IUA'), [53])
    def test_case_1171(self):
        self.assertEqual(pattern_match(' S3,|i\x0b\tyyF\\sIdNH%V\x0cv)@QUU+x6x+khqGVzFW7t9h8~\x08w2o3A6b\x0be&n', '\\sId'), [11])
    def test_case_1172(self):
        self.assertEqual(pattern_match('ehnu\r?]wdvr|Q5gK.zf/,t\\+D  HF{&yiUi5[KJj@-V0g[kM:Y\tS~y#/e]vRo^Zy<e>_m&C9^J\x0coe`Czfd7Wods', '.zf/'), [16])
    def test_case_1173(self):
        self.assertEqual(pattern_match('{i5m~rdn~6 Q43^d9l\x0bmn{"TK}8VO:~\x0bVQE5I3&\rX?1pn\x0b+W?`16-X6]\nLKDQ-@Twua%lfp+l@]JvU8[7+Kbc`34 ,=Ru%S8T', 'n\x0b+'), [44])
    def test_case_1174(self):
        self.assertEqual(pattern_match('\x08\x0b+\x0bO:T\x0c/>|9\x0bk~w9\'DPIN%=w2[RKzS9UP>2B}DyK(br"z\t-"CLR&;C<|P%x\nVLgI+K?`_8D@|\x0c-#\\O.Jl}a|P :"TVJw|6', "w9'"), [15])
    def test_case_1175(self):
        self.assertEqual(pattern_match('\\jC(KSPCSF~@\\.HWbn\r-\t141n#Ju,aYs8[E@XA"}:j)~}uX*oOTQ +X}8,mB<\n>v2\x08ggZoof]ltc227IY#,.1K3aL', '>v2\x08g'), [62])
    def test_case_1176(self):
        self.assertEqual(pattern_match('k=l^Uj_L$kVx^f r)jK<2d!ndmP\\dDG$^rJ=ON\x0b\x0cN<N\x0bbR0oHy\\z5O<Nq}+<5Vkg %LGTD', 'Nq}+<5'), [55])
    def test_case_1177(self):
        self.assertEqual(pattern_match(']#tNMu#"cz+?DA\x0c-\rEm8\x08Y\x0bMzz-\x08$%\rt[\x08<J"\x08"1l?MqTS{,`?ap|_oz_!&', 'zz-\x08'), [24])
    def test_case_1178(self):
        self.assertEqual(pattern_match('GYWU3\n5Dzj;cr\r\nmO.-36Y8k0(%?:819G{ ]0n]vV>]:#Rt&F-zgE|.t/lNeq@9\x0bP5DBBK\tvQ^4\n4H\nC4\nI', '@9\x0b'), [61])
    def test_case_1179(self):
        self.assertEqual(pattern_match('#1u=6V\x0byz||6i#j7>w\x08\rV9b"\x0b%] D2\x0b_U|]\x08&%sT#\'=QM[=uP`h\\GfL7Q)zte?xL9sytG4%2]R\t3+[[m#@\nxY{\'%`eGe', 'h\\Gf'), [50])
    def test_case_1180(self):
        self.assertEqual(pattern_match('.\nhWM[\n8.eEpgHEc>\x0bcqU~_P&.lqz9H]r6`5\r\x0cOSe!`%?Z`k$e(p*N^83bc}>28\\$rW</B8/ALUV&RS8M>sREIrsv\x0cRry8xB)|y2', '\x0bcqU~_'), [17])
    def test_case_1181(self):
        self.assertEqual(pattern_match('98B(ryfJ:&D\x0bo0(M}]4;Vk@BclL5|7PFjEl\\rO9F}+kUgTZU(K&O9^sC(Bwda:fAO3p5XnX', ';Vk@'), [19])
    def test_case_1182(self):
        self.assertEqual(pattern_match('M\x08nk+$mz~iLXLfBlHHZf69HZ:fxF~"\x08e)Z"VBl<4BE58nK<-\x08b^  ', 'XLfBl'), [11])
    def test_case_1183(self):
        self.assertEqual(pattern_match('.(kY_Eo&&|y5|]u0\t$[U4#2J;^y=\x08{i;b/\x0c<>8U!-\tu-g\t#2OS /h-D!a0wy03JCVNMi WsU?B|/>;8!a,R7L>', '<>8U'), [35])
    def test_case_1184(self):
        self.assertEqual(pattern_match('Dh\nk-mCy6ZXdJ=}T|$L#xODUMIE]A\\=&\tcz@%$"BSMjW"W|.Xz$hm?a!^\r/q]\t=pa=#&9[85h"@G:]%', '&9[85h'), [67])
    def test_case_1185(self):
        self.assertEqual(pattern_match('am]2{SU>\\cb\\\x0bt\r6o,AoY\rYM!H+Fh_`O<;\x0ckt\t&8\x0c6*D,ftEB0\rzg', '\r6o,'), [14])
    def test_case_1186(self):
        self.assertEqual(pattern_match('$Y`g~p9\\3%Rs#WoJNMzbZAMZ!kfnMJ(3~p$*fqqmysA&g:o=VM5\\,', 'g~p9'), [3])
    def test_case_1187(self):
        self.assertEqual(pattern_match("*' lCV\nWNs-v6\x08$u(FH ~7h.Zgh\r@-MOeIj7{B{I\\q&xO&>e!Z'2#;\\bw\x0c~C{7a#\\@kI2Nspx%*Y\\'vxzS[#mt^h", 'FH ~7h'), [17])
    def test_case_1188(self):
        self.assertEqual(pattern_match('l_pOM/+} KU\nFS14lD!\rP&Q#\x080`thIpm 5Qv[t)$q%Lr7dH[]\r^9hN0.ZtE', '/+} '), [5])
    def test_case_1189(self):
        self.assertEqual(pattern_match('.G]Rq4D0=\'v3<-:v72iK5\x0c@S&;yc9v\x0bXg9O(zHk7+;Q~NeBT[(\ndDo"hoM\nRcdghz$@)KP{x];= 25i">gO4d,5\x08xUG', ';yc9v'), [25])
    def test_case_1190(self):
        self.assertEqual(pattern_match('+=Z* D\\qb2AkL1B[f\x08" [wvEbX|:gA\x0c{Z)"L<Eh0Ia$?z\x08k\\QvEp4X9u<+\x0cX(xry\t\\c8xA?PU2ceG[R1`abW@dY.xRgry', '?PU2'), [70])
    def test_case_1191(self):
        self.assertEqual(pattern_match("s&gV$37.E;+X+Q7LAXsKc5X\x0c7UftqTA6YB[@\t{:|CKG\\mg3i:rMED%W5c'j$j\x0cNVvD", 'V$37'), [3])
    def test_case_1192(self):
        self.assertEqual(pattern_match('jSy"Rtm/f$,WF;&coljBL]s79L=~QB&Chy!:Tnf&c*keqz]fcSP,WKo\\[FC7R?', '&c*'), [39])
    def test_case_1193(self):
        self.assertEqual(pattern_match('bsR{P!:B7W{Z=FDF>i[F\x0cObRTYX5lj|"1"2RsMM_0lF@Vp%X[\\};BsOofr]B54 PPb+3EK*=iC`e9O.;e,twZ\x0b,MR~-a[', 'wZ\x0b,'), [83])
    def test_case_1194(self):
        self.assertEqual(pattern_match('P.p{.-T-(:30N:a"I)]Iry|Zxd3Hj20\rqwDUK8=4/:cA#@ydpR9:=1Ed]#9V;x<^6|\x0cU1', 'K8=4'), [36])
    def test_case_1195(self):
        self.assertEqual(pattern_match("ne)!!8Zl|}!+F=RF(RjX'6!3M/|L:cFss@0e/o%?7w(Ygl*S\t_r\nnszf{(rr=Px,sdqLu\r5k}?\x0c", "'6!3M"), [20])
    def test_case_1196(self):
        self.assertEqual(pattern_match("*%'\x0b?D!=26,x~Kr8P(B=>(kerhd9t6M\x08^\x0c1g]Y@S5&'`+F`D:S/oa/&\r2Pds'2,lnZ_TJ,Nt\n]ya:c!9e{", '6,x'), [9])
    def test_case_1197(self):
        self.assertEqual(pattern_match('#<\n7]]|-;7^mZ~,^e_n2#cD`Pw!]]fVZJP\x0bY5"K=#Dm`\rbd>y1m', 'Y5"K=#'), [35])
    def test_case_1198(self):
        self.assertEqual(pattern_match('\x0bHkg#$0+t!#1N!1WUaf=t@z98T;K97\tZUswp1:,<G#R \x0cFd$*Pw\'0^h.",t+Kt*@>9pU(;r\\\r49(_0UJu]', '+t!#1N'), [7])
    def test_case_1199(self):
        self.assertEqual(pattern_match('\x0c\\z:OJ>u5=\r3)\nt!Ciq\ry!<Y-!&aj0hs1b0uG.P2|Pv*[*[a)TRZwfn`BWT6M3dHHs\tMP|hl[=]pMll@r<Jzg', 'wfn'), [52])
    def test_case_1200(self):
        self.assertEqual(pattern_match('ZoJYB\n}CKu\x08 {\royV-a.XCPp-z[\nV-UthOnjKb\n$(v30{QBz~BJUe\r]6ybf6&', '\n$(v3'), [38])
    def test_case_1201(self):
        self.assertEqual(pattern_match('CW\t$U/!(?]/o4zyXHypioK[zHJ9#f1E<wdn~pLO`Z\t}\x0c{r}&diOfmA7HTX"\'\t?Q\'4@', 'wdn~'), [32])
    def test_case_1202(self):
        self.assertEqual(pattern_match("QM0RPZk;q,]JfJ{16u&)d(G ]&?{tCsh!%@Y\x0bz$e1'e{S#W;*7:9afA?s:P@qNQBC/G|MN5", 'tCsh!%'), [28])
    def test_case_1203(self):
        self.assertEqual(pattern_match('tH<r`le}9J=8.o)mcU_\\,%8\x08WX%E|%kVlX<C)G~WF+TthV2,\x0b:~;\nv0H[+BYT', '|%k'), [28])
    def test_case_1204(self):
        self.assertEqual(pattern_match("^V;9@8!6%!d vSQPt>&Pj$u]>PO0OyHZ@<c|PS]!J\nX?a'!/A Y8/\n1n>", 'Pt>&P'), [15])
    def test_case_1205(self):
        self.assertEqual(pattern_match('6Z/ &"/;\'O4;\x0bYH>1?*g$JN^rV0)_^E:~UQ2;kL S"TAY3Nh,tpS1`1rF\t(,:t7\x080qM', '1rF'), [54])
    def test_case_1206(self):
        self.assertEqual(pattern_match('sHI=TZ*"+Lx$8\x0bQ@7&\r0\x0cd8`m`,1s7u>[Gtou?] (UR, N.@V^y+f', '>[Gt'), [31])
    def test_case_1207(self):
        self.assertEqual(pattern_match("SU@pLNm DVVeQ/KleCUQpykVMe\x0cwUH'v%\rMB>7 ST,Oh\x0bN..4A\x08\x0cae1*\x0c($-\x08?3br\x08vda", '..4'), [46])
    def test_case_1208(self):
        self.assertEqual(pattern_match('\x0b\tBjLY^.%MD\'\t:9i^"M00tqIK\'QK8b\'{`%U_HbJ<C&#S)G\nc\\*TwO\n\'@7X;\r^oG9R\\3^/fQ\n/iZr\x08="JdMaC:\x0bnu$aF3', "D'\t"), [10])
    def test_case_1209(self):
        self.assertEqual(pattern_match('V!\'[p@R\x08A(tW:_sDKdzxfx7TC<>>r)n\x0c$<ax F[h-7\x0cMF[IJd<yP\t*:C0U4|\x08Tace^nfn\x0bo:`th1"\\X7z`*omc`W;J1b', ':`th'), [71])
    def test_case_1210(self):
        self.assertEqual(pattern_match(';o\x08h\\{)2~p\r+Gjhz"Fjz\tj51sr&>BP#I[,8}SfBMR5yTQ%y8_j\x0b=YLo~gV+9)0B', 'YLo'), [52])
    def test_case_1211(self):
        self.assertEqual(pattern_match("}AsXw-'B\x08tFk\x0c\rQS+RX(915Ff(P42ZZdJ!8gTC4`?fT\nC*X]a TBrf3Z2 N6oxmO}[J[!cxU+J-iHa4P>+&|7kz^pW<cV|pF$", 'kz^pW<'), [85])
    def test_case_1212(self):
        self.assertEqual(pattern_match('\x08XrX{[.^QO{/rQ#@\nZ/cutgWSePh!@K@\tP;%pK`5|D00$-*bx?Ji*"sZb~c<K-$:jBbJ wHI5q|I\t?4s=s5y>6sE4.VF-Ul.', 'K@\tP'), [30])
    def test_case_1213(self):
        self.assertEqual(pattern_match('nVH~Nc_wV+!EtEG\n||(9?y[qX2oJ)PK(^&gkEH0 >E>:(I+?6"HazS/(aPpjkH=_Vff\x08cn]&`XJK"#<C^`KW)\x0b+%ET5a3\x08c:/5', 'kEH0'), [35])
    def test_case_1214(self):
        self.assertEqual(pattern_match('nQ-m)Sw}^0yoI`"0,(yn\x0ciw{0\n_GbK )ik^"0tQ|<N*a:":3\x08.M\nbS}\x088g+T KDc&+h\\@"!7,\n7Wf$tO|g5e', '*a:":3'), [42])
    def test_case_1215(self):
        self.assertEqual(pattern_match('g >~Q7WZYM*0dG-7x*16]\\u;i#,;abS@)rV;z*5c7}G7.o18uj\x0c%7I', 'G-7x'), [13])
    def test_case_1216(self):
        self.assertEqual(pattern_match('<KP\n1^-m*s~\\~E:Wvk;$/a$8wW!fX_w|2\nN|8_@C6F7~Os;e/2D<&\nc?F6-RYk[L', 'F7~'), [41])
    def test_case_1217(self):
        self.assertEqual(pattern_match('Q\x0cq-),ch`SUP8R?H$4v4{Oz{Xx"F)\x085MSDv\'QG\x08aX$Cb(~th|]T8JT8g 5;rE|\n O4{R7E\r$cQl1 >^o', '(~th|'), [44])
    def test_case_1218(self):
        self.assertEqual(pattern_match('[#y?Gws!a\n?\x0bo"+gT_Whd:exz4(]Z@;]O\x08*{\x0c%\'\\EnuY\x08g:=j?IpM%cJ&LULq_v\n!-$Pn\x0bn=Vx 3\x0br\x0c~U.< 2!~', '_Whd:'), [17])
    def test_case_1219(self):
        self.assertEqual(pattern_match(' K<4b\x08C^*~V^H%+Gn/`&nR-.-:K4q\t5:MG^ZsV8V@JtDB|ybc\x0b1TTP', 'n/`'), [16])
    def test_case_1220(self):
        self.assertEqual(pattern_match('?\\!\x0c\n,x<Dt8_gt*{kN\x08i\x08gy\nm"<mg0x|e\nGFgN2_/M0uaD:5hMI:^P.q,;ElO~E,%', '{kN\x08i'), [15])
    def test_case_1221(self):
        self.assertEqual(pattern_match('_0MVt\n(~03n#h2m;hj&`;9+5\\QA `URw4),\t)]B#V]\x0b2{C}G\naw_G2qjVyB%Kf: 6`!>Yf0v]6r5Rn^)7X"SzzgFn\\?6yi]to`>(', '5Rn'), [75])
    def test_case_1222(self):
        self.assertEqual(pattern_match('&Y.lyYJH$jj7:c~z6\t:K"{8KSk#!JTZ4uH4@9i9C=H<_#\x0b+bgWvEg @!3B\n0kuRE1!4F2\r^d_^?,9', 'jj7'), [9])
    def test_case_1223(self):
        self.assertEqual(pattern_match('0\x0cu>@MCDh0")D]U=8\np@4w@%qeKO;b=::3#AUmm:X[|8{~#kq\r^r:>-\rg\')7%/3F=%W|JUBJC4Sq)', 'w@%qeK'), [21])
    def test_case_1224(self):
        self.assertEqual(pattern_match('JeJa|;o6?>v\n*s"wP\\\tmbD0:19s\x0c[\'n/\x0cAR)!hY@KHG\'p$\r}92\x08:G2zVPZ~FY?:\nP9`\rciTA#z', '!hY@KH'), [36])
    def test_case_1225(self):
        self.assertEqual(pattern_match('s&Uy+#`\\1\\+-\x0bK"e;^<B?\x0czX_!T`Y\x0cF\tjH(S^%\nM|&]~UA}VoEofw9NK;[kS~:VS 2k!UsoFyy', 'T`Y\x0c'), [26])
    def test_case_1226(self):
        self.assertEqual(pattern_match("!,sOSB#\tcK<lP(\r{sqGd\tf6f4fSQV^^jw9\\#WlYS}N.!Spo$\\~G3]|.eDMu'Ao=iZn+Nxh]J\\Q#hA:A\x08^", '#\tcK'), [6])
    def test_case_1227(self):
        self.assertEqual(pattern_match("+C:\\V*gEZDwx\r\n\t=jqO\x0cd0C00x>ZRN(iH<X`?yxrsf ]'Y\nZwJ\x0bJ{fy0wr5W>)3\x08[2C*&[X", 'C00x>Z'), [22])
    def test_case_1228(self):
        self.assertEqual(pattern_match("0{pBx<{\rL|L\x08' /0JF/h9v|8YP/V!51,LC1U3*~P2Oxr%DxEbHV\\eC}1{mu,IH{c`/p>G#tAnNb4)?q^3;\nJJ\nV\rCTC<S>9", 'h9v|'), [19])
    def test_case_1229(self):
        self.assertEqual(pattern_match('_pJL\n&oO}Q{ /XPX|O*\'6=$~ZQw4|"\n yQ4UVrC5O&%IM-iR~CJ=^zX\nA{m%"`>d5*bCr2sxv+-@\x0c#h\\_', ' yQ4UV'), [31])
    def test_case_1230(self):
        self.assertEqual(pattern_match("\rXS{]DQ~~9\x0c(#(:%mFCP=KNO::NKsEiv+r%jjGFe\x0b4R '8<)2fLv<`\n[`?dJL~", 'v<`'), [51])
    def test_case_1231(self):
        self.assertEqual(pattern_match('$?G3"q\x0ck3\nAz7U-g)eG`\x0c\\O/@fkIR!D)?GPqz|alNB|hl\'L2Wvyz=D9Pdn$Rm1,_*2SkEM}\x088.8', 'Rm1,'), [59])
    def test_case_1232(self):
        self.assertEqual(pattern_match('sIl%V"cI}~*H0wieupE\nVoLE\x0bjCoW$w\\H\t7]mEKfT~WaT~#=|O', '"cI'), [5])
    def test_case_1233(self):
        self.assertEqual(pattern_match("$Q='ybtUI6 C;;W\x0b7yZMc!\x08GRp~w0t%+h8*[D\x0b!`LO\n\x0b[m?3p[m%PX\\:", "='ybt"), [2])
    def test_case_1234(self):
        self.assertEqual(pattern_match("+~r%EX_lT<7J~I'O&+sV}5V!LK|:Gh7\\t u'IOoR`[U'pgW5V\\_2C\n=x^ua\\\x08(}SkBdo';]\x0b\x0cN1,<u$9{O}W%R8=*'@[", '7J~I'), [10])
    def test_case_1235(self):
        self.assertEqual(pattern_match("WWqp=\x0chZz\x083G \x0b 9@qlSoOZ=<SaAWe\r:#!qN\x08oy5;z;&>*2n-g{<U\tN-ky%,f}Hi'Dxq2\tM<]@G'#HBdO7lSGI*c'jx\x0bVz&X\x0c;", '\tN-ky'), [53])
    def test_case_1236(self):
        self.assertEqual(pattern_match('T8uu\\\\U3o%%\x08Tw9Q*-;]Cmdb/M!EF\t-\ng[\x0c\'j*2=`~U(,%KcXGd}EB\n4_{m_?t4q?<]$7)b0H"}\x08A1,4h9w6B0_o+%Oo>(x2Sq', "g[\x0c'j*"), [32])
    def test_case_1237(self):
        self.assertEqual(pattern_match('X"P\\e2)s?bdzv|Hi)j<?!/~+:kfI>]TH\x0b376g\x0c@xk3On~;g><\rX[X\n&\x0b1:P$em\x0cJaM?d:57O\x0b.57^[\x0cpMit->', '^[\x0cp'), [76])
    def test_case_1238(self):
        self.assertEqual(pattern_match('[w\\~L5VJNMNPX"}e1w<DN AcYeP_qzP#=T5},X%fVV(I*kL4adm4\tw?Iy\n!gp_3Oe+~NNO\r\x0c9ShPXEyPZ/ro#l8t%q;"c]', 'qzP'), [28])
    def test_case_1239(self):
        self.assertEqual(pattern_match('!0uwl#gfcL\rbNaD+zf[(7@wbTVGGj\x0c[BfJUn\r>2D;,CB#^iI%\x08XK5!c0T/#mRnjG', 'f[(7@'), [17])
    def test_case_1240(self):
        self.assertEqual(pattern_match('mMVdoU5%hz5!@!IQF}#\x0b:rT"(2E}3)74o_LkRQ6@w%\x0bU*kn`pJ{DlX`%s3~I\t*e/M*8N.#\x0cZ4/~7ZC*?_bR|<E4', 'DlX`%'), [51])
    def test_case_1241(self):
        self.assertEqual(pattern_match('D7*CSOl;A^-i#}X;{/\\0+J46:!X06" k$N^\x0cC|[\'8R\\\x0cUiB|yw\\]\\m<yC#\\Om_!{42?\\9]', '{42?'), [63])
    def test_case_1242(self):
        self.assertEqual(pattern_match('+IGg V{+[\'gI5{1pAD\\VQZx~d\'_U:@RT`ki\tPrA8SFzHBr-Z\r3A9"Zz#', "'_U"), [25])
    def test_case_1243(self):
        self.assertEqual(pattern_match('M49Iz\x0bk6?AzNR\rrk4DIMr0Mop`tFIZh)!eXv%K>dJHy3]E2k%7o&,_@el', 'Mr0Mo'), [19])
    def test_case_1244(self):
        self.assertEqual(pattern_match("IHW(OTDr0=Z\tz{>JZo~!dRtv)AsnJGo;:7*Hn'(p+'~nWv(.gH#vb4e`81{]Yv}mqm-\\>q=`xvh|\x08]R", 'Yv}'), [60])
    def test_case_1245(self):
        self.assertEqual(pattern_match('Je({up<kg2GxQI\x0cPs\x0b+DqW,^o7\x0bx_\tUKSTRdqH\x0bbS\ndJ$&pp!y#1)P~"_Iy$K;>`\'Qx-?@*1UB[T4rp\x08p<e/\\{vK "\\b%', 'bS\n'), [39])
    def test_case_1246(self):
        self.assertEqual(pattern_match('H7u:W\tC%q!l%H"\x0bVX(+1u\x0bg66qNgC5.\x08+{V6j!IL\nF\\2]t-xy0VWcQ', 'u\x0bg6'), [20])
    def test_case_1247(self):
        self.assertEqual(pattern_match('eUdC:5t6Mq$IP/pw\nG*5t\r\'<C;/KI#% !B\njtfz"&I}uNv~jbDDvU`~qJ^eAl%+|\\BB0', '$IP/p'), [10])
    def test_case_1248(self):
        self.assertEqual(pattern_match("s^4oM6K6nN@_'!,VN;Bx [3AuV+=<2-b1&vAxH!D:Iaph&FK/\t\x0bY8ko`{a<i", '4oM6K'), [2])
    def test_case_1249(self):
        self.assertEqual(pattern_match("\r$/XSA3@\t7\x0bA\\C$ZFEA'\x0cTZjWY\n\\Xq_'Bd$va'yeTr]5Mx4tURdwEt!Ys=X!Ing,qSlA_hE4xL?cBaGShyaf=M0", '/XS'), [2])
    def test_case_1250(self):
        self.assertEqual(pattern_match('Z=V[>!y;!\rSW1\x0bv]oEgIq$+s/B_zSx>\x08@C}yO\tafH~_k=m>>,Vm\nY(GC\r', 's/B_'), [23])
    def test_case_1251(self):
        self.assertEqual(pattern_match("`SiEAy4y;vQH}Xp<[!'iFfH-OS\t)nNQ\ni%5bWX]5>K{}c\r\tB;H~\\vfA:-W=7F-BQo%Ak50(3R.q#>z,X:P", '~\\vf'), [50])
    def test_case_1252(self):
        self.assertEqual(pattern_match('X*z3^qPx\x0b)J*nmL`8u4|cv2bYT?U5Y=a#;ARz)8m+wx6n5s"5n(Z;\x0crk9.Xb>^k\t', 'v2b'), [21])
    def test_case_1253(self):
        self.assertEqual(pattern_match('&V_`O\x0b\\FSYiugs?UI/xYD&:p5eD]j]Q7h]\t\tPuW*7*O)1u;qWT\\,7iNE&}r', 'iNE'), [53])
    def test_case_1254(self):
        self.assertEqual(pattern_match('\x0cr17]<:K]n*9<[\top\x0c`A8QE\tK_`e^B"7fKO;[uv\\=9 "}qg\x0cVC(|i.Pn5qV8#ggPS>nuqD]M4;}\x0b_3)RsKx($R\'S4\x0ci', '\tK_`e^'), [23])
    def test_case_1255(self):
        self.assertEqual(pattern_match('xF\rx`t~jFU\tIi#e~waAW~\trjp~}gFff(7M}#=X":F;8D~J>X-/AL4"jr=\x0c8j(3uBd;Sas_RxbHas|', 'r=\x0c'), [55])
    def test_case_1256(self):
        self.assertEqual(pattern_match('\rd~Zq_Y!x6#&8\x0c`:vAextT*KK\n<G@\'t TM)U^9_Gr""1\x08$(l5P\nqgr/\\;eN|:KLFlYO\x0bj', 'q_Y!'), [4])
    def test_case_1257(self):
        self.assertEqual(pattern_match('pA e}u\tIh">UF:m)tK}0\tnQGvl7l\t5\rW2u~753Pc.wP%`o:8V8\\6zB$]/+VZv\x0ck!uz;W]K%Y_$\x0c31\x08K9kB9\x0b;(_+.R+', 'h">'), [8])
    def test_case_1258(self):
        self.assertEqual(pattern_match("k)'OJ(>gRp1On}=9WmF`pk\n_s(QsU&U&4D)\x0c#w~Q?PJ17X\x0bhCi.\r|.13d6)mv0KR eDJMG-TMs:Fk9z.pE!~", 'sU&U'), [27])
    def test_case_1259(self):
        self.assertEqual(pattern_match('}@(JU%k{T>~tRRI]?w_&SIsWX:B\nH{+G%ve*,H%h?YJR#eC.@Lu:7VlHWs\x0b', 'G%ve'), [31])
    def test_case_1260(self):
        self.assertEqual(pattern_match("b}bEq#^@l:<n1Z2/&\rZgtPIPvg>:G0Qk5++L$ye)+X)flp<4.aQj#+`i.0nM}y\x0bCU o)8F\rK&6:'p!+:\r", 'K&6'), [71])
    def test_case_1261(self):
        self.assertEqual(pattern_match('qG={ga`YHV\n{D|Y[eOX@o3Ov:,vc}F{5#\\_\tvR#ubK2j0b0wQ%IWbg0R98/`Bvo|UsvTQ2Ut9zD3tP4);\x0cF0]e_Re|', 'Ov:'), [22])
    def test_case_1262(self):
        self.assertEqual(pattern_match('M$D:\x08\t=&.o=M@S47gY/y>=1[m- `oX\njs\x0b\\H]=+ZajD0|Cw<@J{a`-?jbT\x0b?roT\nbsbR*_XL%h', 'jbT\x0b'), [55])
    def test_case_1263(self):
        self.assertEqual(pattern_match('\t|nd\x0c1uRdfr>`z\x0cS^19cs$*R]"-oE24R;&XpIy]\x0835X}"\x08X)\x0bVVF\x0bW8*F\'UtkcUQQm*', '\x0cS^1'), [14])
    def test_case_1264(self):
        self.assertEqual(pattern_match('a+r|[@,N\x0b(Q3\t%a\rPmm,<co^,J\x0b{#ac)@^=!geDVJ e\tI^+BlT@i)f/Yn9[X_Aygk\n`9p[pF', ',<c'), [19])
    def test_case_1265(self):
        self.assertEqual(pattern_match('tOg~!HB6yy`q\\~\t2)1*64U1X^LQ[eXd"FzlQj3]`B\r%zn\t~Ch\\SWO\t`\'z]tw%%m>l,I)UT!;\n5\x0b\x0b39Ugn9e-:\r', 'Q[eXd"'), [26])
    def test_case_1266(self):
        self.assertEqual(pattern_match('Og\x08*2w#a$ID4# \rDOYd\x0c7H$5kw0)g,A\x087x%#oY0s#N\'(UkuUn8-Y]D\tem!n#u\x08tvq7 j?~)1C/\x08\x08x#6<7:@Z;2tw|."3\x0ctR%d\tP', ';2tw'), [84])
    def test_case_1267(self):
        self.assertEqual(pattern_match('EE\nxeG8Zki\x08i^CnW+[Ov /O)\x0cJz =~%\'\n1:\'6ma2\r-JpH[nSn/>8Pq"+YVm5s(<g>{qLy=Ot2HH6\x08nT9c=\x0b{>2n@-.(aQa8@Xj', '^CnW+'), [12])
    def test_case_1268(self):
        self.assertEqual(pattern_match('RP3!\n0YP\tgtj1g5AHS\x08]t2Crx|18 -2Xc1g||/\x0b-<LE?&Y-y\t@e&wp,b:`\x08\x0bC\'r6SJ"`w9/~?VfN{;2xA]uy7=pX=5Xz!q]a:3Pk', '0YP'), [5])
    def test_case_1269(self):
        self.assertEqual(pattern_match("?L-f\ths=<RC@X-k'eB^\x0c\rV\nzQQ$o]E62eTgHza&c<A/9bEp`jSqL+wVh", '^\x0c\rV\n'), [18])
    def test_case_1270(self):
        self.assertEqual(pattern_match("T`\r1M'0>YDcm_(#Apip/!rco[r\ni2GX+K\x0b/FVDY;2[;+P<`Cai`zoJhRFc}I$A@u%|qRm[,", '[;+'), [41])
    def test_case_1271(self):
        self.assertEqual(pattern_match("OjiX{QxC{]!-tK\\IS1:c{J/\x0cF* s1'A<@ )!{a\tH#5_0SGA;[*[w?J\x0cX'N7/uW]\x0bjl.\x08=ND>%K", ' )!'), [33])
    def test_case_1272(self):
        self.assertEqual(pattern_match('iG"!\x08(go\rT\nj%>\x0bSumct8\tSBNcf\x0bTw#84=5xnk6\\_NPXZ5.(gyr{\'"<\x0bq%\'\\hGHgn\\AFB/\\;;HE$[\x0cf&\x0b7S=%.8B', 'umct'), [16])
    def test_case_1273(self):
        self.assertEqual(pattern_match('OM&CQx>aUtW5+4o2V"gQS<usHtp-M+MM.$\\_l1?38lJ/Jj-Qu}DM12\x08"$!7A=uSfyb!gY^d:k0&i\x0bAGL?u;R\r?o8^', 'UtW5+'), [8])
    def test_case_1274(self):
        self.assertEqual(pattern_match('\'f >\x08?d\r@x0FDpy/Mu9^Y=6.O;?z^&KK5Z}~!;0TD##\\*ae^\nTx4@!>_$^Lx$ v-_xl^c6+Hy"9.yZb\t|\r\r', '=6.O'), [21])
    def test_case_1275(self):
        self.assertEqual(pattern_match('nCOGm\x0b&I|b\nE\x08FVSOqHg!+R29 H&\r:-0Ed"THk#<"vPE=ugV/94\x08)D', 'Ed"THk'), [32])
    def test_case_1276(self):
        self.assertEqual(pattern_match('S/`)zU`"wf}/_1SNn,m\x0833dy<p4|\t3uKsuYB4\\v4+umQ~Qk!vU1\x08f3b\n!^HeN\tShR86Q\x08\x0c%|fe:<pK!*06`>^-[3`/A{D795Wi', '06`>^'), [80])
    def test_case_1277(self):
        self.assertEqual(pattern_match("\x0c/4:BYx~7'F\r'?\nYg7*xXG-<JSyhq\nW--=.ZPQ5%oO[~X\tD8<K'\tVD`_k47L;=m[h~vsY{CIV\n4 ", "~7'F\r"), [7])
    def test_case_1278(self):
        self.assertEqual(pattern_match('tQ4O (Z)S6k.6LH^%as78><ez<X3v,&;\\@\t\r)PezDnyJ4\ti21J', '3v,'), [27])
    def test_case_1279(self):
        self.assertEqual(pattern_match(' "f~q@Hgpj]&^\rfzHKN)\rR<QF~07b=kE5Vh<)]H-6p)@D{as_Z\n;CdHs&-WbU#\'tTdMhXejBG=Q\t\rcImd,[\'9h2jr', '~q@Hgp'), [3])
    def test_case_1280(self):
        self.assertEqual(pattern_match('XMq<eR=|u`VEAjf15ed1E-@F>"G=0i \x0bNdyf\t70wk<\\#Y/c8j~H"NWI-Z', 'q<eR=|'), [2])
    def test_case_1281(self):
        self.assertEqual(pattern_match("SI;H*}Y!fT]Q,y&g-\t17\x0cU?7.r'|i~(q3-$JJ#\\;-V.)v\x0bBxCuj#i", ';-V.'), [39])
    def test_case_1282(self):
        self.assertEqual(pattern_match("A2`[$~JkC8JB+jdX>|,\x08N[A)P&6D aKLgM\\qcQxky@M\\?r\r 6K`Y&d_LY<\rj{Wq6Y#bj'gNRGl\x0c", 'K`Y&'), [49])
    def test_case_1283(self):
        self.assertEqual(pattern_match("Ev;]TK'[D>M<+nN$iS0^f(\\*|ufpkC r-UV^l5mJ('!!-~uxy,+~", '-~uxy'), [44])
    def test_case_1284(self):
        self.assertEqual(pattern_match('A=@:8\'XGq+,N5\t=b`\n.lZ\\<AH6Ag{TAu;.c^DR_9\n&6t{"aaA6~dak\x0bRq?zfmYHOC8B@*b3%qj^P', 'b3%q'), [69])
    def test_case_1285(self):
        self.assertEqual(pattern_match('@R+?]ckF0Wb@T"7F7(;;,zE\'2AY3u/Yl^*9\'!Zkb\\A?w(N\x0b ^.ko!t{hV26<L*Z7(IJRW\nR\tWj z\\s=O#\r=R72TIw Z!JNeK', 'ckF0W'), [5])
    def test_case_1286(self):
        self.assertEqual(pattern_match("B.b|'_Q\n>mDDge[Ph\x0bhc-^nTyK@\x0cs%M/H\rD5s?Qq_A1H~\nPvdPh7{`3|7Ku3", 'vdP'), [47])
    def test_case_1287(self):
        self.assertEqual(pattern_match('Do?-9sqi\'\\fsC/$_`o-\'r"e=&q6U~"OD\r]]^\te\'=K`wafrd0Kn\t^k*B0rZLzp,cfGN#\n7PfF4K1`0h$n*ZXv([X', "e'=K`"), [37])
    def test_case_1288(self):
        self.assertEqual(pattern_match('$nW"+c:Ge@ $:%Y>ZJ\nPg\r Y@j&#;\x08sR9sPe=IspI|lB(q%;?dP\rb{MJl*', '\nPg'), [18])
    def test_case_1289(self):
        self.assertEqual(pattern_match("a\nl^M3`~0j,?0P\\s/?>8G@[FGeXlz&#(abm.Ktikv{01B^*SU|%Bt9'{Skpq\\\x0cT2i*;7d^z]\x0b\x0b", 'tikv'), [37])
    def test_case_1290(self):
        self.assertEqual(pattern_match('b]I\x08u\x08cU /4W=\tZGT@*02/1qa\x08\x0c8:C.aDL\x08\rVU\nqs%:r*[h-$mp"7DCx5/|+.zhE`y', '"7DC'), [51])
    def test_case_1291(self):
        self.assertEqual(pattern_match('aC\x0bHv!e3tEQkM6&F>I_A(xcaE#-XuxKYB;@)-D41^;,\'n~%*^n"2X2F\\a5 n@B~6Ci+D2;\\qTr\\[W$:,>p(\tK3n\'v?{', 'X2F\\'), [52])
    def test_case_1292(self):
        self.assertEqual(pattern_match('LdA2\t{nt;$v5TC}zdr\x0b\x08RH"\x0b+L+,\x0cZu\nvxu:wIfwR]>YZ)D-"OH])_7)M[-&{Esr=4Oa\\qWmG:$wx3)|;+hLfe\t6d\\]oW)Ou0', ')D-"OH'), [45])
    def test_case_1293(self):
        self.assertEqual(pattern_match('JZC{YAuio@(V1~.\x0bx6kY]0%(2WC&9OhTP._,zea\x08,`ii3IS^+V\\ADe', 'Y]0%(2'), [19])
    def test_case_1294(self):
        self.assertEqual(pattern_match('y@xHMT}\n%I\nG;gsq[A\x0br7lPmZG9iP>mhH2A^SaqP:;~+H.sL6b\x0ct_(}&v* qvheQ@YOi[^Ts [)YR\\<$Hr2|4\niYOep=3EL', '}\n%I'), [6])
    def test_case_1295(self):
        self.assertEqual(pattern_match('{6:}9~jq[^~=\nm;\n\x084Uj$n&UR^5>>8|`Eqi7(,pqo\\.=T#O>N/Pe[(!"uu_\'OE^Bekt7_e2i=CPm|H\nI\n52=c[LC;ChP\'H]6\nd', 'c[LC;'), [84])
    def test_case_1296(self):
        self.assertEqual(pattern_match('*>/RK8?W4[Wg*l;Izm2]~(;bl+BhZiZS!=2&*bg)G,l4j,(!~]@5ZEG/GF-|\x0c<', 'zm2'), [16])
    def test_case_1297(self):
        self.assertEqual(pattern_match("0Uc_)jh\x0b||H+*%L\x0cl8>SqBED\thQ\tYj~\x0c#\x08Lh:n9fec$6!'rP|y4>d~4%THo4nsx)K?I6LMR7\\TM<g~]]gLV|#Iw%JW:\x0b;|t", 'Yj~'), [28])
    def test_case_1298(self):
        self.assertEqual(pattern_match("mDRk-)$-v,[QZ&@>wOl{xBx0uc6]Q!NCd'\x0b1It&Ck2<)x@p\n#N7*fQawpD*g8;^l\x0c,a,}vDKixhou<pRa,", '{xBx0u'), [19])
    def test_case_1299(self):
        self.assertEqual(pattern_match('/m~n-I\\^"\x0c1W_u&r6\'"~TcmAz\x08Y/)~2v;r\\?uVTq^5][Y!)E&4hmE*`#WiF$DExSEl9JF~\x08\nQL<",n{', 'L<",n'), [73])
    def test_case_1300(self):
        self.assertEqual(pattern_match("+ZmMv4CRGO>a'|:D3[)W6kQL-Us`bFxPH7zL$En@i^E;F.WX~U|bal!LnheBP\x0brG/QJ6CV@6P=_]V$B=@80JF", 'n@i'), [38])
    def test_case_1301(self):
        self.assertEqual(pattern_match('NDX*"\\)l.7g:[i^ty"KOCvFrAN{sY4bxCR0WYq<I?wBZD}0<j!5R%87XipSgv\x082\x0bWOY}^zv<1?B\x0cx*Vk\\$L^u_RrhiU', 'Yq<'), [36])
    def test_case_1302(self):
        self.assertEqual(pattern_match("<)WLHvW@\x0c:Yypw'\x0c.g~\\@EA%YP!CDF;&g78eu[n\tBTUj3QRE^_la|Klb\rg%dBS3|JF\x0b/PX(PvsG=<H\nsU", 'S3|JF\x0b'), [61])
    def test_case_1303(self):
        self.assertEqual(pattern_match('\ta&lj\nafY,p}@Aq\'7q{)bE@o`$ezy#RH$n&mnS/hAM)c(e:0y}J\\sg@H>OkVt~*k@cU36R\t"3lNqr,a?Jp9}\nfsv-o\'&nW,jCU50', '&nW,jC'), [91])
    def test_case_1304(self):
        self.assertEqual(pattern_match('P<Vo(sap~:5rxc0kuCw8TZp%L7..Aq|z3irpY\x08Pso&Z!{L>4VR5 )PrP9\x0cSfWoW}2WlR&EZGh:NF5[:(^r', '}2WlR'), [63])
    def test_case_1305(self):
        self.assertEqual(pattern_match('k-|&Q|p;D^59VR~b~^\t1=~~iX~B19O{"$<fC+IC\'j,7zXi\x0c=*]p+(XVi\x08MChgDoQZ%!]a\x0bZtb+\nbISjR&1)CU]>%h Xn.+~!{$;Q', 'a\x0bZtb'), [68])
    def test_case_1306(self):
        self.assertEqual(pattern_match('K+>/pO7,adgDX9v31?aaPr=;nRfkMOx{fR\n\x08{6".\t4[yVlv2\x0c6iY0ps#@&mnJ8\tNw9R:^S`z,+@HM', '&mnJ8\t'), [57])
    def test_case_1307(self):
        self.assertEqual(pattern_match('dI(CJW5R&-[Iy}y7>GBMgo"AOv\x0b=8"T_!b}3R,u)!/pMx0gXZgI*+YR=)yW\x0c#.z~jMZ5i,Uuz67N%dCL\\zpZA?4!q9|zJ', 'i,Uuz'), [68])
    def test_case_1308(self):
        self.assertEqual(pattern_match('vo{44\\^(qt`8I7z8%*W]:O\t7U\x0b&<eCQiHlbcpx"u\\YI4)y2hevJLP+X6', 'I4)y2h'), [42])
    def test_case_1309(self):
        self.assertEqual(pattern_match("b^DZ`m5d*Z{q g34sT#-DX2w}^#Ms6 [ \x0bn~N~%Y\x08Ixf$5.6r6TJg5>/\x0b24?+uo,D2`+Yhju=vlqt'1", 'b^DZ`m'), [0])
    def test_case_1310(self):
        self.assertEqual(pattern_match('=?-y~*Wa)LaPu|\\F{rNFD5%G5z[R"[\r2UE(sy)\x0chU]dk\r5,$\nIOm<f$Z9orfwO{LV\\!T/DRcZU\'dw0o\'oeh0\'', '|\\F'), [13])
    def test_case_1311(self):
        self.assertEqual(pattern_match('u44G)[;N#(^$7ee!g4a$}FRY7P}M!}5hi\rYiRla!\r)*H1"gu%CVb?', 'hi\rYiR'), [31])
    def test_case_1312(self):
        self.assertEqual(pattern_match("rvqzxV/P:^x55}M0+~>?}Ry:z\x08?>it+w'8%[f=fImW64cnVe^n<Ubr0d7\\nRG|+B$&nyX", '<Ubr0d'), [50])
    def test_case_1313(self):
        self.assertEqual(pattern_match('lWw\x08bZyYLGHi*b@)A80eQIj!+(atnmMk%YwWPyUo\t`#>q0.\x08bRA"\'s%Cr`,', 'bZyYLG'), [4])
    def test_case_1314(self):
        self.assertEqual(pattern_match('_V:\x08\x08,[C*Nhj57rbQxt_B\x08q,b.\x0cB7*S+"\r 7ap6*u&N5%=lj!gb&\nRQwF@VN*T@xD2\n~r;2TmHxi/\x0bW<)y<\x0c', 'b.\x0c'), [24])
    def test_case_1315(self):
        self.assertEqual(pattern_match('zboPs=K-:*O Ua\x0cj68LuS4B@@S+C2ILvw\t\x0b ,~94\t\x08?~=!kY<i\x0c\x08\x0bVl{:y44;cU~gZWUxojUeOR[yPU}pC:?J`hAwV)#)ffB~', ':*O U'), [8])
    def test_case_1316(self):
        self.assertEqual(pattern_match('6wK\n\x08Gy/\n`,VZuP}g%,7$uCNw&53YA"0y G7= ~mOTN(R>{:XOUu\'"46', 'OUu'), [49])
    def test_case_1317(self):
        self.assertEqual(pattern_match('U_G[n+by"J<+q[\x0c(]Q\r=0vQ`Ie&]|z-WuQHI\'Sj<W+*\n"E_n(Ph+@<i9+N\to0\t"VHfV\nI\x08M,kbxaw#\'abvkp', "QHI'"), [33])
    def test_case_1318(self):
        self.assertEqual(pattern_match('gmG~j5uL)d_CDgm4!(b;Ge&W}?1<bO-"zjL?bO:O^m[e~)GCV}ER#As_D\x0bf-/!(O6cGh\r>.', 'CV}'), [47])
    def test_case_1319(self):
        self.assertEqual(pattern_match("*[<k53Tb\tLM\x0c/yot\tbYlc 7^q-\nDFr+s+C^gklfo^\rG@eA:BWgPh':2cO?f\ne@$h\x0bp/^x:WM~0~\nF5k0wiC", '0~\nF5k'), [73])
    def test_case_1320(self):
        self.assertEqual(pattern_match('A"6\x08!u4|\x08$@\nB-D?zjDNIZZ:\'LjlXR~FZg90hXsW\\58"FXU\'\x0c< =`}ARv3l+\rA<', 'u4|'), [5])
    def test_case_1321(self):
        self.assertEqual(pattern_match('%ZDN;}2*byI#qbx\n\tDS~/>\tQ#\\w,yL*`(s;KbQ#b0MXjK8n}eyTv|9jVQf[EMvA_It', '9jVQ'), [53])
    def test_case_1322(self):
        self.assertEqual(pattern_match('A\'#wpq\'~M%5ls_I(X\x087F"FJ> 1T7C!+M9v%XK\x0bT+edr8ZXW.ei]=\\]ELZT< LzX?LM~L/_E,\r2s4#iC|L(!F!>I5jx0', 'J> 1T'), [22])
    def test_case_1323(self):
        self.assertEqual(pattern_match('i7[l <3FtPxkv^@N}P:f.DRt--!.6ND=Y$M/\x0ch-\r@25$%zK.#m=\\,0eE9LtZeVymrz^KZY>&&M|XBIzT', '\r@25'), [39])
    def test_case_1324(self):
        self.assertEqual(pattern_match('=;nJc$2?Ytej,!~qs92L}gH]OVms%.dXcx)j*fFY]&A<<AB+*8:;Zb[xdq+{D$FW\t-{\'I/O-Woy[UpP1my)#rB%|#&>@uF"UA9', '{D$'), [59])
    def test_case_1325(self):
        self.assertEqual(pattern_match('J\x08)[T~^|VV@+^:O]GQ\x0cJt+zp 3Eo=i1V\\GyOxc\x0bQ4IY>aN8B!l9-"^Nyj\'_d\rxxPXy=J a!C\tCC6Xt  Yre8l`!X,J%bz_TX)t', 'Jt+zp '), [19])
    def test_case_1326(self):
        self.assertEqual(pattern_match("1V*ii|\n(%ps[Xt\x08q!']p4'H7>D7+*Hug(k:Q98Nh\x0bbf[!bxO$WwYUka/j*N+vV7=\r|:X0", '\x0bbf[!'), [40])
    def test_case_1327(self):
        self.assertEqual(pattern_match(':%S.c19\t"6\x0c%:d, s=8xea*#\x0c6en\x0b9w`s6i.\x0c~9A>l&BQ\x0c{g%\'$', '6en\x0b'), [25])
    def test_case_1328(self):
        self.assertEqual(pattern_match('tCD.K4=b|4v5>qU2" s"~~=~)_\no!J+\x0bed>0h}AOQ4i/[.M=Q=D_/\x0b+@.M:0<I`\x0b]I aVJu:3?h<&fAIA[B:Lsvq2<|f"', '~~='), [20])
    def test_case_1329(self):
        self.assertEqual(pattern_match('K@2.*5\x0bP@d\x0c]Ln lvlm\x0bN1)ljLeeb/\x0bVSw$q-iJHDdk4yo}59{zha\n[>;A\x08yDh.=$\n%*|Sgr!C\\\x0c{B4<|1\n^$IWMyo', 'k4yo}5'), [42])
    def test_case_1330(self):
        self.assertEqual(pattern_match('jE\nmHN*nR|\x0c&QK2&)[A\rj ~criCU_%&|IrqHBeWM5I,5\nQ\\>a)\n".o6OX-W*%0+i5\x08b6nro<c%!YON_2QPQY*yuIn\n\tv$CfC', 'eWM5I'), [37])
    def test_case_1331(self):
        self.assertEqual(pattern_match('mnCHPQ\r*D]WtE=TF0n\x08 hx2"FZ|b@B$p$lGtFK@\tq;h0}4SybpQc`ZRu!Xe}Q9FH?|=]4U5S\x08C-87+4e(\r<%HV\not(%O8\x0b>P', 'HV\not'), [84])
    def test_case_1332(self):
        self.assertEqual(pattern_match('M`#v\x0b \x08^J\x0b>TN7z74UbnYx7qs7T<Sjdj|)\\\t;P\x0bsHUtyKNlUW4$7N//x"N\x0b3{[aKepkhq5-az22aN,c-R', 'NlUW4'), [45])
    def test_case_1333(self):
        self.assertEqual(pattern_match("'>Gz9q!Z$!gu,Of:D\\f_?q8\x0b1%|7i5B\x0b3:I[I:Zd<Q96OTel\n1S:~YJl<_\x0co[m\\8;Nz0VVt4]A0n%[\x0bvO#Vf*)2EctYo66#J,Z", '!gu,O'), [9])
    def test_case_1334(self):
        self.assertEqual(pattern_match('fQy3Bx!}sk9Ua.+y<N*^\x08<2w3]h_r)]ttC#uen{/)S<`rJg{\\Ji0"A\n,F%ac+o2kU=bmGJuq3@t', '\n,F'), [54])
    def test_case_1335(self):
        self.assertEqual(pattern_match('98bAABMai9EM?}/Oz8g-mSv#-xsg4\\\'iW,kc6"VvuSO>btnC^Si/+Z_\rs#U>G$HL/O?uodR,\nl/', 'nC^S'), [46])
    def test_case_1336(self):
        self.assertEqual(pattern_match("E]d7sw&^F$='2Zfl\x0bT}r) lru-G@zF Kpb6 @9,B-kV.eB!d7&\\,z", 'E]d'), [0])
    def test_case_1337(self):
        self.assertEqual(pattern_match('6lo~\x08*3f`,x|dz\t9OMRGg)+vN DVI*`A:_Lr@z?va2m.AUQ-RBpT5RDP+8\x08o:;^qv-:oR<+X]`,<w}', '+X]'), [70])
    def test_case_1338(self):
        self.assertEqual(pattern_match('D#j5f!0i""4O&\r"^84\x0b\\21cD \\:`UJ{l,7j+#^M6RuHyZ[$0mJ\\on', 'f!0i'), [4])
    def test_case_1339(self):
        self.assertEqual(pattern_match('t;m(Y-@R^tYV$\\\\hLt1Ej\nr?rsj-=\tSwB$]iK7Jae(d~9)TV\\_Lz', '~9)TV'), [43])
    def test_case_1340(self):
        self.assertEqual(pattern_match("Lbl_.?7h&QpPYKd-L,+MZ\\O#$\x0c#?q9ndQ\tR^>'p;d|1F`_)\n7F!gGK-w!qUr", 'Z\\O'), [20])
    def test_case_1341(self):
        self.assertEqual(pattern_match('v}^%w6ix\n{^u"KE?,8|\x0bWY?G!y`L^6Xqaa`3~RY$~&C"WS~@F/x}&iaq)WHU^(*S<hW0avBGs9yL\t#3!VcW%\'=', '"KE?'), [12])
    def test_case_1342(self):
        self.assertEqual(pattern_match(":CX0{e>$xZjIes94Dh;dFAI9|2:u{2?%{lp=]E@ qmX99Cd/m'1}l+#ZMZhrA-7*{j}>20i(a[-CX$o\r\x0c)VE1)d`", '9Cd/'), [44])
    def test_case_1343(self):
        self.assertEqual(pattern_match('9SHaOTlgw\x08m vz*LVtIS^48QQOr$gO"Z]vw.Ex.3QN>JwcjQJT;bT#RgHj1zF0(N*U%R', 'T#RgH'), [52])
    def test_case_1344(self):
        self.assertEqual(pattern_match('~j\n\x0br\nC0]<9PhS=->Y~>CQW{i0McVpmiNPP</J_(bP\x0bMcGAh_B\x08Vq-7#)Z&4dLZ@o$%6a#ruAm4(]T5s{_fL_', 'cVpmi'), [27])
    def test_case_1345(self):
        self.assertEqual(pattern_match('Tq_U+c\x0cTelQ[yGw-\x0c\x0c0\'(b-`T5Uz-H%[!)(9G.| E"OlpJ2X|`1<!\t`[s]U,8jy_\x08\x0cI,8\t7~1DE', '%[!)'), [30])
    def test_case_1346(self):
        self.assertEqual(pattern_match('+=F2\x08x@\x0860eO@t"WT6f_G*Qe{*~;F;YX.SOeM<L2V(2CV~-2 )T<Z>qvLDq9Ij_Sd(]@p,/d\x0c\'[\r<7y=Z<, neq', '<Z>qvL'), [51])
    def test_case_1347(self):
        self.assertEqual(pattern_match('V;;\'*\x0b}/1TI6>~\\Un\x0bmfWu~@13VB8|dLY!\rSZX?^A=s2\\f\ru-"v-}N\n=eO(DVO3sr )_@&\rqh6\r"\'\nc', 'B8|dLY'), [27])
    def test_case_1348(self):
        self.assertEqual(pattern_match("OGh;2n^{WeMWidZBgL1eM.0_|zRvwS<K]xW+jc}\x0b9a7zoDpQtz[\x083v'V3", 'vwS<'), [27])
    def test_case_1349(self):
        self.assertEqual(pattern_match('oq"\\!z2eANYO~*I0f@yBWFh`+?QMZL^s%TZnbV;4,jG\n52+oSk\x0cdFQ|@CO_oDL&#,nQv(C', '"\\!z'), [2])
    def test_case_1350(self):
        self.assertEqual(pattern_match(' i\x08cH>\rA#i[TGBP eg\\jc"\x0cL#vX+N.j+W,cR[j2CBF,1y/KlmGx2Q>KN`Pc{0QV5@Hhqa9JF"9HI\rR6o\x08#= tkE?81\nQ1\t:9H;P', '2CBF,'), [38])
    def test_case_1351(self):
        self.assertEqual(pattern_match("'GdwRY7H&8 2H\x0c1^2sWqP?F.[VzgtLr1La%zCS\t}@)^wYEE8Q\t:Q%h$\x08pG`\x08,sos[SAmN5", '?F.'), [21])
    def test_case_1352(self):
        self.assertEqual(pattern_match('Tl!bo\rlgO\nNJ1j0vd*^c\x0c06AZiU :K\\*9gi;E:0D"b,\rR%S7y2PPIA%o10A+=\rbSxq6JCqO:uV2', 'bSxq'), [62])
    def test_case_1353(self):
        self.assertEqual(pattern_match('% >Z4\t{b4>e+{Xp+sy[\'\x0c>op[l}XZTWrbo>$-LFg!$y3=/o1n^<D9,QI\n#`"K\nhtU(CpDhm', 'o>$'), [33])
    def test_case_1354(self):
        self.assertEqual(pattern_match('(|x<\x08bx<id4P!Cg\x0b\x08 "F7X^TNgp]^dKk%ETO$kseF2JxvI=\\91R88g_mT9q5aRbtHFY%$6Q{+i$C#? LK3', '"F7X'), [18])
    def test_case_1355(self):
        self.assertEqual(pattern_match('5zN|dmp @eXk\nzRiSIB>i"0uh4Wc9NoD_s5\x0cT6mpnRhX~)WL$^', '"0uh4'), [21])
    def test_case_1356(self):
        self.assertEqual(pattern_match('R);o[Nia5<Q41:6H,\tjMmeA<j#BXu^vGW"r\x08>Ei&A*D}}o\'@Q&XiKv3@a.=T#UC7M_z)S<p-0YNn;0h[D,ln2XH3zp`\x0bS"I', ';o['), [2])
    def test_case_1357(self):
        self.assertEqual(pattern_match('Gk^Y/_\tBgk(_=SGHao~_CMKm\nE\r/pn0/P;Y$ha@YZCpZ^DZ1A&35AQ~6', 'GHao~_'), [14])
    def test_case_1358(self):
        self.assertEqual(pattern_match('f9ckW57C\x08whj*6]\r9:C+)BRJx\x0biR\rI )w/[XKZ#V\t/e6fcGJx3|a>\\ZQ$OV9+=f\x0cwwM.i_)^?7i-ByD', 'ZQ$O'), [54])
    def test_case_1359(self):
        self.assertEqual(pattern_match(')o(kl_kz C9\\Ky-Y=x?ImW_\rm3=i(]Z(Ktu>XrL9QLCH13\\\x08Qf', 'Y=x'), [15])
    def test_case_1360(self):
        self.assertEqual(pattern_match("&AUO!!B'kQ|k,eP@EL7z+o)a^}}YvvN_WaQ}`\x0c;k2$;\x0cyer(56", 'N_W'), [30])
    def test_case_1361(self):
        self.assertEqual(pattern_match("Vh%}4)$b(Bf,\x08_e~E/vGQ,(^w:]t@\x0c\\r7dgGy6@CqpxPW5'O6%~,zx)ddt\n\t3]INF wzbj#hws~f0kH?YHOMT8^Uint5TSwLI!", '$b('), [6])
    def test_case_1362(self):
        self.assertEqual(pattern_match('7DH811\x08jyeFE[EPeL4{<{QqW>:8`,lh7:dfaw3t[*f7K_0`Ixo,nq4/v0.', 'K_0`I'), [43])
    def test_case_1363(self):
        self.assertEqual(pattern_match('gJ4-4I\n7%\x0cfD/SK;-_"G$^{I/6vB>YR:C;mt3\tS)XV\x0bbHPXF(ZSs?@S&qw\\aY5t<rJn[SO*U_\nqB\\d,4tNo', 't3\tS)'), [35])
    def test_case_1364(self):
        self.assertEqual(pattern_match('^z>z ;8[/qg,|](/#SFCGiW"{:*KQ]%ws4|0Yy\x08ZB]3\nUnZNo}Tsj*n^^YO5\\u||/Vg3@@', '^^YO5\\'), [55])
    def test_case_1365(self):
        self.assertEqual(pattern_match(" Ul>I\\g~TwvgVEv2kDGO|fp- `TQZK;1?IAa/)7u.:AyjY'>!Rf?,y!siu?dlXXI[z\r4", 'lXX'), [60])
    def test_case_1366(self):
        self.assertEqual(pattern_match('zKHi\t_,!XG&\x0bnropt\x0bI:)j(f{H{$k1wVViUo=@\x08\rpjo(:\nZ^"qBhrRP#E2', '1wVVi'), [29])
    def test_case_1367(self):
        self.assertEqual(pattern_match("7D6Cg#J=:A\\rpmL$+l'^^t,As}-X2DgU[Xyn1\t\x08Y.\\)4(\\]N`(ze3#]Q-yIU)\nJa1EaAt-r#h ;0vd'?~SB", 'As}-X'), [23])
    def test_case_1368(self):
        self.assertEqual(pattern_match('7gh!~8 )\n~^gO@it~3 x$%DbI"L\x08z,N:wTmN{39-+O(ZR,/\rbKW*)NyLxkIb*-ao\nI9xEYQLE{~,]8j9\rOL;|7t\'#@!', ')\n~'), [7])
    def test_case_1369(self):
        self.assertEqual(pattern_match('`\x0bOf-\x0bfUz^@Z"J\tO";v *MNv\tK8U\x0c;jj&{pB\noqkYmt\x0c.$\n\nC#Z#0:!F%cO (|n$A8\r<?-Bm?\x0cs^7=Vn', 'Bm?'), [70])
    def test_case_1370(self):
        self.assertEqual(pattern_match('l\'l"j\'V3|,~~y[)y<\txzn[ iVn>i]teE?q$=i*d9#\tw~K20*\'\x08VXb-ZEjh?.hrqO\x0c[', 'l\'l"'), [0])
    def test_case_1371(self):
        self.assertEqual(pattern_match('`\'])SpXpap_`k,\r;2k=<:0yqM3bP4\rPi=;+_>T?._\x08582?w[,r&X"eDfHf(\x0b', 'qM3'), [23])
    def test_case_1372(self):
        self.assertEqual(pattern_match('9m9;QA`sy:\x0clr`PXC#TZ\trTWy5/L~<3r^@oSR9,p\\Y8\r(;:\x08UzV_C2:l(%u`~FQ^%VXR{SWH', '9;QA`s'), [2])
    def test_case_1373(self):
        self.assertEqual(pattern_match('f~\r3i#tkd>"iyx;@!/ghO5AJ\rwlNCf-ES~n-nDI(Ee8qLakY>J5>T\x08_j}pVM', '5>T\x08_j'), [50])
    def test_case_1374(self):
        self.assertEqual(pattern_match('38ixZ^(8lPiZL;/83pI\x0cS7Z+l_{BcPt][F]PNqd.P>@A7;ZG&bUsrRk$t!Kg$b9{I(ErG,0.t?6\n(%\tLjyt03n~}', '9{I(E'), [62])
    def test_case_1375(self):
        self.assertEqual(pattern_match('\x08(3(K)y!ncHr;AE`u?=F,{IOY]-#rt%\rCX&*e+"=\rl5\'w[}+4>\n#$K', 'E`u?=F'), [14])
    def test_case_1376(self):
        self.assertEqual(pattern_match('08\x0cvU\x08AXhF:Oq,Gl\x0bq`{.nukb6Z"z[o$R[U)o~Y/ac7d3wKttxH,{m', 'c7d3wK'), [41])
    def test_case_1377(self):
        self.assertEqual(pattern_match('}VcV\x0c_GE$ixR%mS8M-7hYS\\Yl,1m)/-51Iu4eX!\n)rxz^T_Ygv\r~W]%dWQ+', '7hYS\\Y'), [18])
    def test_case_1378(self):
        self.assertEqual(pattern_match("<bohu!8xC%mwv\\V*AqFP,H]Q>7A\r,L/y[$\x0bGeH\x0b?'?xF9#S5\n~ 0", 'u!8xC%'), [4])
    def test_case_1379(self):
        self.assertEqual(pattern_match('^*I\'*Ur|mMzAy"z"%V`>v0cJ{S]yz4AwAS3I{is\rIaM1\'<$i8z_,=I_"gx~8rz8yqV8{H\x0c][h\r{d3s[)SFO#/:en<f\x0b^', "*I'*"), [1])
    def test_case_1380(self):
        self.assertEqual(pattern_match('Eal0wz\x0ct}Hy6~CHjY*"e9!U]C{G-H/%CAu22HjzA,t.RW&f:p%E8cvR\n+kN\tN9+8u\x0b@eT3\rmdDL5$ll>&{b%r/Uh', 'DL5$ll'), [73])
    def test_case_1381(self):
        self.assertEqual(pattern_match("BJv)sCc\x0ck{mT/VVKY&S,G_K}>WO6`-f,P0U$dnfo?0!V^ZITq9&i^#\\1'sz'rkN1\x0c|^H]K8(", '>WO6'), [24])
    def test_case_1382(self):
        self.assertEqual(pattern_match('N^|{]P/=)paq\\Hf7sGfqd*5>D>oxj\x0bt\ti"@T\x0brri>YiMvA9(k=.+qa%Bx{4@SqQ65?SAU]&\'9=GE\t9\nN6\x0c+', "]&'9="), [69])
    def test_case_1383(self):
        self.assertEqual(pattern_match('rZ:1;z\t]ZfGk1q ni5aM}w>Uu~#CsrOFaEn)#$2T\x087pR5Na\t4CE:bbZs3~\x0bG_\x0c!x#o#7y6]MWiuN]2V}5-\x08/%q^3Rjp7sHc^rd', 'ZfGk1q'), [8])
    def test_case_1384(self):
        self.assertEqual(pattern_match('",r)?9Pr\x08qSKGC6&&JPld5sGZL`7KZ 8\tW!\x08\x08Z}b\tk$fhZ4Su\rum-rCQ2\x0cJ oZ<j\x0cgZ\x08!y>@60y\\zv@\rAg&hwJ\tb]Q\rVB', '7KZ '), [27])
    def test_case_1385(self):
        self.assertEqual(pattern_match('&a;~@ GCg-AqEXRky7_,\x08f|"J6aNZLqM^#~\'/hQ)+Yk,@f\\U9N*X;d;z|@/lAd{b}*w"z\'<\n+("', 'U9N*'), [47])
    def test_case_1386(self):
        self.assertEqual(pattern_match('$z\n.:0[V-f5GjZCCKukHU>6mrSq\nH1ac\ntNVB$XFG&)EP.Ywb.k~Ttq3', '\n.:0'), [2])
    def test_case_1387(self):
        self.assertEqual(pattern_match("&a_P=C!99)2t&MR#v'0 h|Qq6.\r<\\TK_/'bE]pt'uJ=m\n!rNONopzD)G", 'rNONo'), [46])
    def test_case_1388(self):
        self.assertEqual(pattern_match("B8\x0cU:&q!?Rh#\x08[gMD#\x08rO\r_xsczOk~szd7\\^oRl`Mi 0Ks'!m`'\rYXx%4V\r", "`'\rYXx"), [49])
    def test_case_1389(self):
        self.assertEqual(pattern_match("OQ#*4iRsCdHJXN}+Y7tmy@H19*?<Y5Daq'.H^P9i|,$A,*>%ltg7\rkMS!E6B[\\M.H?CIm:1{fmH", '9i|'), [38])
    def test_case_1390(self):
        self.assertEqual(pattern_match('HGAv6hO~s8HS<)w]\nm\rs"7FH7?*gV%lQS339b_o+O%U,F5^vDO(t7HzGk\t-*', '7?*'), [24])
    def test_case_1391(self):
        self.assertEqual(pattern_match('Jj)vKf7wWn%d]yN03rR,7^nYk7]pbvx$\tFa5=\rUK1}\r&xo2n`#O\\mMMt&$43=ueGOn', '}\r&'), [41])
    def test_case_1392(self):
        self.assertEqual(pattern_match("`HM4(9-%h$dQC-F0<!{RL21\x0b\\#@\x08/r_@Rn==\tR\tX651#dc\ttZZ*ec\r(}Gx:'w|c", 'ZZ*ec'), [48])
    def test_case_1393(self):
        self.assertEqual(pattern_match('SIRC$\'[D5Ckv+=6`e_H\'\tNc("@.mdlqf\x0bA,8,.\taR\'y\rpp`p#\tc22qv-?IjbM.,JFx4saCe,HC@JL3%;v\t?{NOU\\OT<@\rhAt', 'L3%;'), [76])
    def test_case_1394(self):
        self.assertEqual(pattern_match('ImzIAJglW`b(ZUo~GJXtKfd\x0cYiI+^t6 kyqKb.,LiA0Tnn2E(VnRN];kS,QC{iRNJ"%IWyG1H"Xa\n^@MV!/%o%n', 'IWyG1'), [67])
    def test_case_1395(self):
        self.assertEqual(pattern_match('pA\t\tGNR_$\\f_oFdf xY\tUps@a8J\x0b{n0Z^P)l\x0c\x08-n"`dvc/>gX\'5Oa\x0bo#\t10j8ev\tG;ib}}5|cZhE%DHB&Bhq(o', 'cZhE%'), [72])
    def test_case_1396(self):
        self.assertEqual(pattern_match('3Vyi!E@SP&<k\re9}D\\ )|]mqd.Z7yA~ZV\r5Bc4{9iRF$g&KueP1E\x08f6g_Cme17^fBhM\x0c#Y\x0b|nq', '~ZV\r5'), [30])
    def test_case_1397(self):
        self.assertEqual(pattern_match('\x0c@StAPzbq`v=\x0c\x0c?V#sl4/WL#\t+*A.H\\mTu1*&"OT)wt49jBr@>G2', '&"O'), [36])
    def test_case_1398(self):
        self.assertEqual(pattern_match('h;W9z1_bvij6<Dc7ORK0OSC\n~*J|5Xl|Ng)1# w*s8ZV,_Q_OH\tzuq|&`\r\x0b(f[E-gE$5\x08Q2Q:F\n33jIV~tSY)BUq]', '8ZV,_Q'), [41])
    def test_case_1399(self):
        self.assertEqual(pattern_match("q*rax~a[_qz'-x{\t*{DH;`f~WBBR*7c%:g 1E3n(\x0bl0fu)GgVU4L@gGE\\f\nEhbv&3|$xHSuixw^W", '*{DH;'), [16])
    def test_case_1400(self):
        self.assertEqual(pattern_match('m;^8eqxAar<V#MpsJg\nf0v~4Mkn|*9s C7rx*wmg6i@}U`uV`/\r?7YaCY+VTg3dG)}?tT)>4', 'G)}'), [63])
    def test_case_1401(self):
        self.assertEqual(pattern_match("\x0b@R[B\n\tCu`B??dd*O9nU\rLqcnt!I|~Q[v&2:N1=`Y7Fs'l3mGnH8K\rgkjU&l\r1R^qruu_(`\x0c?Wfl'>A>Ajr`%fv", 'u`B??d'), [8])
    def test_case_1402(self):
        self.assertEqual(pattern_match('(hx3{-6g,f_g&~DiH-{<]/\rYo>K}wQ\nS20)svSC-uWs7\x0cB.RT^\x0ca{', '{-6g,f'), [4])
    def test_case_1403(self):
        self.assertEqual(pattern_match('bs>X1(b6N#:L"}B-rkA:!\'l_RI>@Vp!h;\x08`QUCz_@:v2\x0bBtv"o^n0', '}B-rkA'), [13])
    def test_case_1404(self):
        self.assertEqual(pattern_match('\\Fes ;#~PN}cSERdS,#zD,\\xE$q)CQ?\nzi\x0b\x0bB"u\x08OG+L-b5B*L\x0c&', '\\Fes'), [0])
    def test_case_1405(self):
        self.assertEqual(pattern_match("_\n9@mpCO+7b_X\r!n\x08v]xl}t x-Zj-e'F3]`3 1Q-5y\x08X_uhpd-\x0bc}P~x4-(", "e'F"), [29])
    def test_case_1406(self):
        self.assertEqual(pattern_match('Z:El$ZvKCMmu/z{\n48ZeYlP1RAK?\\7vpO@#YjgUx+"fv2u`8jY|yD*FM[)7{\neu[#HNFet\\0<+e6', 'K?\\7v'), [26])
    def test_case_1407(self):
        self.assertEqual(pattern_match("NztTU8\x0c~*bjF|s~AkMb_4lSO-Yw\n\x08f6/OT'\n/fAZh?ZFcJ5&._c)vbDnVSOe<xEh[$\t", '?ZF'), [41])
    def test_case_1408(self):
        self.assertEqual(pattern_match('fu5k.QJVoH`SyS\tX5Zcr =wHPd@\x08x5]2B\n7w*w-N;7C\t<X *+m$a4q#wtQ@QwT?<WicvLW\x0c.uj- z_\\6+mzj/W\rW-MQ7', 'W\x0c.'), [69])
    def test_case_1409(self):
        self.assertEqual(pattern_match('QcdZz/lRy,Q-9,C6hj\r;8$rYS &+`\tjy2wa7j.z \x08\x0bX\x08k`Y#X=X&wGv{uT,Q!(|^M:\t\x08;cxgPRE4Ie8C460', '9,C6hj'), [12])
    def test_case_1410(self):
        self.assertEqual(pattern_match('@LoqK%Vc]|gG7L|%?%MLi\x0bu{l|D\x08F6ScD5m\nvo@\\m2{fd5zp.8\x0c`|bnz$b8c!\rpI8!', 'm\nvo@\\'), [34])
    def test_case_1411(self):
        self.assertEqual(pattern_match('KmEq@"Ul}CP.&;@\x0cO\'J_i0\x0cca`bFQv5\tVHCP\tHi\r:in|{\x08#<#8)Mr,;', 'Ul}CP.'), [6])
    def test_case_1412(self):
        self.assertEqual(pattern_match('R"KUgq|39m&\tt?:\'TY<<xPp>jFTYV\rH3%a\nP9Dm;VM~|";n%p,dq` W', 'Y<<x'), [17])
    def test_case_1413(self):
        self.assertEqual(pattern_match('P\re3z>\rf%&R#gJ}g!zMC\x08bm%QF}#mXvLG>VaTS2%YfC,bzt4D!uA3`5XC_S]Dpjz;Ix\\0eU~h~CkdXAU]Yz\\p~_f&\x0bCrI6', 'J}g!z'), [13])
    def test_case_1414(self):
        self.assertEqual(pattern_match('3C(o#]p\tLSiu"1w]Yu(!C\\5kI\x08&\nEJ&?y*Gq+bys\r,HY0A5@|OBE\x0csV"\'G5tk7uJf1$pVPcQ:6F}M\r(NO*!d%~9M5P6:RRkQ\x0cRA', '3C(o'), [0])
    def test_case_1415(self):
        self.assertEqual(pattern_match('8#{H@;!n|;>j~s@;@=;C\\|!Ea\tJo@Fn\x0c>?jdmWY\\@\x08Gn#F\\l\rEK#NiAfHL@m', ';@=;C\\'), [15])
    def test_case_1416(self):
        self.assertEqual(pattern_match('i2Fuj$s_\x0bR\'[y0H(K\x0b}v]:E&wN+p&~>^"^C\x0cy\t<xlq~4O\x0cg labM@\x0c_p\t#WS:\'wZgY,;n\\n\x08X%uz4wd)\x0bi]O', 'gY,;n'), [64])
    def test_case_1417(self):
        self.assertEqual(pattern_match('=0T]SUQ2K"\x08\x08b-}EP=P%$3`)%m|n1hq:5!67/LagF#V\x0b*/ykqb%kyR?,EDN\rac.!(8*2', '.!(8*'), [62])
    def test_case_1418(self):
        self.assertEqual(pattern_match('c\tp43r_\nTy LZ;wdimeBj!#"gkrca`3R -q$CR:!G-tDM6]&jl9$', 'c\tp43'), [0])
    def test_case_1419(self):
        self.assertEqual(pattern_match('xh\n v&WbCvMR_?m\nBP[zwyX#2b;VbAd&eGHPz|g9F"&tk8cSTN^[m U{qQ].c=hik/!wx&9yE#Mb2A\x0cYRt/Y[a1jLH|Z\rSVl~Q\'', '\nBP'), [15])
    def test_case_1420(self):
        self.assertEqual(pattern_match("Xq%q<z0\x0b\nB.>3av{*\x0c7wXL_r2OB!L71BWRcKK7m=1mKhqD2W/ZM$n9z~8~gq7P}<'t9z><PI(\x08e&Be;GyK(=yK!n%*8)\x085v|\x0cV/", '(\x08e&B'), [72])
    def test_case_1421(self):
        self.assertEqual(pattern_match("f}\x0cq/U\x0b<yjJ%j;#E\x0bUflRe}T\x08y\\{V%/'PfoMZqa292sfqjc8REL", 'oMZ'), [34])
    def test_case_1422(self):
        self.assertEqual(pattern_match("/J!%#;`~*VRyA)MX2O\x08%$/}\x0cIHg7,pWP 9LJ#DwV< q53'0h=PdFTRpaR)", "'0h=Pd"), [45])
    def test_case_1423(self):
        self.assertEqual(pattern_match('^Ma$(>e M4&e<+M\x0c4FLz<VBl(}1*FCEk|iwb+,/R,)hoa/VkI\x0cxH\x0bbM;<]M9.U]##zNFr7,}4A\x0c;', '##zNF'), [63])
    def test_case_1424(self):
        self.assertEqual(pattern_match("#N\x0c*Q(7g@'cx-`+K<m+!Sbp}6Q>zu\tv\nn`=L\x0b[\x08zoKS\taf7I\t*jX\\tfJOK", '6Q>zu\t'), [24])
    def test_case_1425(self):
        self.assertEqual(pattern_match('{^R3C&Rc0pK\x0c\x0c]Yj}7XGil9|1/dn)#3,#u\x08 &li33Z!ni\x08*t\x0cSgYWp#e2.UbrC(Ei({Vl}ADxZKJ 9?Qa:A2.V', 'Ei({V'), [63])
    def test_case_1426(self):
        self.assertEqual(pattern_match('@:/]]N![~QF)?+=l`9tfBz+9=/3Q\\E}<0lbr8&cG}AwnmA~,4fYJG.', ')?+=l`'), [11])
    def test_case_1427(self):
        self.assertEqual(pattern_match('r3~I}GPE]?]E1WePAq3wnyMZxuzV]9pk49;eg34vC]:QuX\x0b);P6"TiV0\'nNJlXaoPIXT^vcnuh{\t%j0\x0c4yn:Xr', 'JlX'), [59])
    def test_case_1428(self):
        self.assertEqual(pattern_match(' cT~5 >GL)~\ndZZ/AjvU&p2J)O"FyH3J"EJ\x08Z0<k0BB!MiY1!\x08[Q#|[&X-\'`|X\nsZ0Z[P7O{<B-\\$npa}+<LE\n\n\x0b,O\r.5*HqC', '3J"'), [30])
    def test_case_1429(self):
        self.assertEqual(pattern_match(')Kc_7Tsi%owo}4q@MC=\x0brd01(,8!s(;kx]a\n\x0cIn~J>{i]q7w. 9\t*0\x0b:DC1A+p@V\x0bNo\x0bEq=9\x08/[(HRB ENH_5H#\r.\t4^MU', 'RB EN'), [77])
    def test_case_1430(self):
        self.assertEqual(pattern_match("]YjCpHFK%z;fNA:|BmYu'}&@8NXBL1/JwuY9G\x080EG%f\x0c\n+;MlxyQ;`", 'NXBL'), [25])
    def test_case_1431(self):
        self.assertEqual(pattern_match('|\x08?_<z\nRI>-qwob*f I7- J4O\t@Lb4=S-N6B\nhcJO\x0c}xMfqv1-Y6"jmPLbHr^;_WZgW0:', '@Lb4='), [26])
    def test_case_1432(self):
        self.assertEqual(pattern_match('\r[-&CDS;\ruk<@Cg6@2{}1eO3ne20}\x0c\tS()X3s`/FNtCd?,\nIa7f1`Q>\twTrMp\tPc&\x0c!?u}Xb^,,. !i\t>C)>u\nx(stl\x08UXkX=)>', 'TrMp\tP'), [57])
    def test_case_1433(self):
        self.assertEqual(pattern_match('EtS1(^p;#\x0c?{7H)~(u^4O`_a><Usr{BudI-,Uy_;ND^Je5taj~sd*\x0b]Pu(\x0bO`}I78[xhH9\x0b8NS#lk\n~k:\nRipl\rM\nPzwDf\naO>X', 'zwD'), [90])
    def test_case_1434(self):
        self.assertEqual(pattern_match('5.P\rlUIISm:VM*<y4C<Tbqn3\x0b!H9vMT)^|a~q8iS)by%[r?J+>QLgpu}nFI9Hn\x0b\tW,x?:\tS?0fn"}FT;=K QYYD?BDFX"kv$x', '3\x0b!H9'), [23])
    def test_case_1435(self):
        self.assertEqual(pattern_match('YN)+65EW:+p)9\x08S}:qd+oOk$3{RKm~SNWKs$gT2\\7RB9O*IHjOg\n}sJzTk&.[.6NNJjdC`m%ogNN!aM=kU', 'g\n}sJ'), [50])
    def test_case_1436(self):
        self.assertEqual(pattern_match("Tm?yyJ`Ac2y35Kub-3\t['H{X3PGn\n!R2tA\r$>Xx*JyKOC\r/1+]!,eL", '*JyK'), [39])
    def test_case_1437(self):
        self.assertEqual(pattern_match('\x0b].50wG9Sd^=H:=/G.3\n@=?q:gH#&\x0bcV&s1yzjl\t1hc+pq|(hDpq"A^RQkhclU9>gc2uu%@1%#VVgZ# 3@%7ab9$J5Gc\'\x0bmGdp[C', '@%7ab'), [81])
    def test_case_1438(self):
        self.assertEqual(pattern_match('<qk`\x0by#C]u*TlH>7j_+/oL3\\>kXXB+nJHI}nw/tGnp*z5Q;\\NhTpps\x08', 'nJHI}n'), [30])
    def test_case_1439(self):
        self.assertEqual(pattern_match('O2X^_tb>"`3_>mM,>PSEcm9}\'057\\m#i\rt/,\x08"&B\t<rS6gT,5Sy\\/2', 'gT,5'), [45])
    def test_case_1440(self):
        self.assertEqual(pattern_match('YA= 4Ej^I8l%gwSEEb\t\\Dk,ix|sl=,js@jGKZMH%Vi\rt+_4J:VDukJ', 'EEb\t\\D'), [15])
    def test_case_1441(self):
        self.assertEqual(pattern_match('3SMu\x0b2pU\\bu"bbFxSLh47v{].u`u3lmCJTp g3$,*?k>\x0c\x0cd+K"5_\ngI', '\x0b2pU\\b'), [4])
    def test_case_1442(self):
        self.assertEqual(pattern_match('Y\'E<BIW\r*\x08f"#ZT{U{X`]1E%2&IZ&(\x0c;[5&E|&S=\\xYwO#!l`jKXCd+[{wJ!-[t^WJU}K#XB', 'l`jKX'), [47])
    def test_case_1443(self):
        self.assertEqual(pattern_match("W#I9RRvC<D|^XDl(xsNGV.`0$qeqZIC=+\x0cgH_]@X!G\te`HS i\\JC\x08B',l(b>QaHu82]\x0b0#ZCfu{2PpC", 'xsNGV'), [16])
    def test_case_1444(self):
        self.assertEqual(pattern_match('!GK?Kr)/0k9<~A_|\x08\x0cR\r_U\\I*w\x0c$+eT`d}tx4QM7|w{qTRK~+0"}.e*U\x08P3UUo\x08|,q?<A2^', 'Uo\x08|,'), [60])
    def test_case_1445(self):
        self.assertEqual(pattern_match('<$TmD~Vc>*"[\x08*2(}(n@B\x08` kGXp\'0T!k+$(kILXn-%}DQrA}|7]#*JiS~0\tf9I,bU\\W9h>9m2IAZ\x0byv\ru-\x0b%', '9I,'), [61])
    def test_case_1446(self):
        self.assertEqual(pattern_match("=\tFY\t#%uAtR,}zu%41)m?F};~oGpuyQKP<Ng3okBo}=T,'z8 F\x08l]Ad\t<kg=P<X.'vx}K\t.8a|G\n)I1~lcWo", '\t#%uA'), [4])
    def test_case_1447(self):
        self.assertEqual(pattern_match('N&:xfL2_~[]ac;(6]K Jlgo{F&0CN$40n,G.\x0clKl6]0#-H\t%z{`,XoPvq', '0#-H\t%'), [42])
    def test_case_1448(self):
        self.assertEqual(pattern_match('Xz*JsMR~b-s7\x08*4qGeD\t/`z0\nSjaP73+@d`#29roZuN\x08xu?#&lQI ', 'sMR~'), [4])
    def test_case_1449(self):
        self.assertEqual(pattern_match("I2q&N}TcY3^~nReuvk_?eV7\\eU4/ps\r5-c!):-8?'\npk_KuF#[.}wM->Vd\x087,|wvr\tg:qOAbr_\x0c}Qc/WB", ',|wv'), [60])
    def test_case_1450(self):
        self.assertEqual(pattern_match("p{B^|'\x0b(b\x08?\n{T)s4fYY#\n\x08x5=)s=WX9$u<FTFQ\t\x08m>b;>el5N|YL|\rH", '\x0b(b\x08'), [6])
    def test_case_1451(self):
        self.assertEqual(pattern_match('+NTo~V\'\x08> r!q[L-R+"\t9|y/H\x08Hp5\n&l/\tY_k!NL_Pukf{&Mv1X\x0b2+Nh]wW|.ISA9x#$n!Iou]/qhhV:B@W:K>MBm[a41-Ck.L+', '/\tY_k!'), [32])
    def test_case_1452(self):
        self.assertEqual(pattern_match("bg'7)#;p*.tK'tVF%ig1J<z[X|&G1WS\nD7br/&y*\x08juC,-:\x0b<{ MT%}MQoF[5AP5Fc", "bg'7)#"), [0])
    def test_case_1453(self):
        self.assertEqual(pattern_match('<[}j;}\'?}ek.`oGiJ`!}z;QId:w\x08{=@yzxZ#i"K\tPV}tDEWn\x0cpu7B,\x0b#p^+\nsZLxTnDl15HSg|LOJ*2`u', 'z;QId:'), [20])
    def test_case_1454(self):
        self.assertEqual(pattern_match(";Egy=\x0bp@37Q\x08<TGlZKEyP<Z3!]51%==?k'_,+sfg {Xd0B8$YS\\[`?", '<Z3!]5'), [21])
    def test_case_1455(self):
        self.assertEqual(pattern_match("6k%\rzht'IP6FlP5UzoG4kbM\\Q*ad1=|l/m3dSKLjKz%FF`Z#%($;Pd.>", 'F`Z#%'), [44])
    def test_case_1456(self):
        self.assertEqual(pattern_match('"-xp5=i00q}4`w9p"{\rCREDOk?$MD-f+r%vfI"B3\noJ,TlxB3>>,!|]iXZT o\'\x08@HK&&CvXfgYo\rdu\n}Yw#l{oooN\x0cEA*~:', '00q}4`'), [7])
    def test_case_1457(self):
        self.assertEqual(pattern_match('c\tY\rx1o*I,HhD=tsg0!\x0cBrp`Lx$b8~)M\r{fcSOGd]11|np.oiYBg', 'tsg0!'), [14])
    def test_case_1458(self):
        self.assertEqual(pattern_match('7PLJjBGpi[7L,\\sW-nP/v;K@j\x08,Z!\\Wxu1=[=|jT53LII`r4cAN/[nw!`df%,', ',\\sW-n'), [12])
    def test_case_1459(self):
        self.assertEqual(pattern_match('5aU\x0ctq\'\x0cujn^r\\A,:hcA/%tR=i<_s/&%"5bRbaG-P9\x0caF&bS]\n[x\x0b', 'cA/%'), [18])
    def test_case_1460(self):
        self.assertEqual(pattern_match("\x0b6$$KGm4(=!uSBi.ngxQS7I\x0bse{.8TT9(\tN'1a=G{/\x08ij.;B\rm!4}-@8V*", '7I\x0bs'), [21])
    def test_case_1461(self):
        self.assertEqual(pattern_match('18znvz;SN\nHR%H0# ~6fS7*5e3r024.,&!_1T>Y[dkt.5Z\nU\\T\x0c\x08GLWe_r{EhT>r 1sF{D?zv@x~obV&+<;~6', '\nU\\T\x0c\x08'), [46])
    def test_case_1462(self):
        self.assertEqual(pattern_match('LL?TZ!T]{s\'*\rB"K2\x08h&,[c}Xt\r7fZ# =\tAp~\x08\\eKu+M@_?Y#&5~f"C\x0c', '+M@_?'), [42])
    def test_case_1463(self):
        self.assertEqual(pattern_match('ta C@rQVy\rVSa[f\'{sqcY)}]zl(/Gs^\x0c>j P%/NFN2v!lSy;^b@SKT}^,,XzLv"puG)( .>t=eS_g.Sybe', '(/Gs^\x0c'), [26])
    def test_case_1464(self):
        self.assertEqual(pattern_match("Bh\x0b>[74$}EyGcn( @i*_7<^S]%k2IgLzU\x08#\x0bH9\r!'UULuJ9C*~4|}\r2-cwYZE0yFoyt\ttw", '<^S]%'), [21])
    def test_case_1465(self):
        self.assertEqual(pattern_match('ea:|"Fw#KoK={&._E`tgsj\x0c(^vZ .J\r3a$7kdb`E8AO/\'/^uvuyJ\x0c0,Q5abx|3+z', "'/^uv"), [44])
    def test_case_1466(self):
        self.assertEqual(pattern_match('6~kZmid\rn1p|/r.^SM+d+(E*HULis&_w{r"rMgs)jo\x08\nX&~YHz!-[\t>B\x0cZ0ZZT}\x0bie-/$^>>4wQrbu\rWOCE\rCl/R+6EM6zG', 'OCE'), [80])
    def test_case_1467(self):
        self.assertEqual(pattern_match('o[bI[ JU?3&:9J^-pgy&B=c8`E#<.y5OuE\tF"nJ{?\t$aS=_ ,@su@CL9NE<y)\r*`ZxO3/j=(4N)N\x0csAo4B,pIn4}&c%G_\x08', 'pgy&'), [16])
    def test_case_1468(self):
        self.assertEqual(pattern_match('<jBMv&]h|`m(WZgT[):V@m6kQBISL%+X>|(xmo}`PX\t(@.hAVgU\x0bvk\n+Z8\\R"bddw(D=/%=_<\x0c5q^~otc>DXawz+i', 'X\t(@.'), [41])
    def test_case_1469(self):
        self.assertEqual(pattern_match('5=Y5fTF%e$0+j<eIdMV-4C25+bN0a5a.v9;gG4[)K3=wOD+cWi2yX38', '9;gG4['), [33])
    def test_case_1470(self):
        self.assertEqual(pattern_match('p/yf\t\nZk0_fl"M|NU#BPU|;2\x08p&`U\rY,eWL\r<!)y>[Q.\r@pIA8Ek\x0c0\r@WwY\x0c', '.\r@p'), [43])
    def test_case_1471(self):
        self.assertEqual(pattern_match('l00 !`IW/iHg\n>1g}PR/O;:3$\td\\N2vRq1XesR3d9i/>(`HH}X\x08\x0cb\\I]M{qgL"!ZYO', 'L"!ZY'), [60])
    def test_case_1472(self):
        self.assertEqual(pattern_match('\n(;ddZycGg1|:Oc8+`^-?kBv\n?Ax7Y^3]Vv4Xy6|Oq$Isnjco9_!;*L KV,W)TMV)" N{E/\nm.&V9auiEk0+]s\n,.:d-', 'co9_!'), [47])
    def test_case_1473(self):
        self.assertEqual(pattern_match('0UJ`1}Y\t3:Z%gO:;2\x0c|b>\x08Dvm@r>$@9\\VXD@f\x0c@0:5<W;b+4$W/Hl/Ny%\x0bF_i\r\tl8Z\x0cz`dG\x08b.\t/{xCv)\rT{BD\t\t', 'XD@f'), [33])
    def test_case_1474(self):
        self.assertEqual(pattern_match('\'Ghn$\n.~H7\tRly@S$<f\t9c>_@!jP"v B+WRI3y`C,\\-o$~@]KQ\x0b`B^M*N5Qu\x0cZwFosjbg', '+WRI3y'), [32])
    def test_case_1475(self):
        self.assertEqual(pattern_match("bO^%7j%xpl-Yt^VtS+#fiTnX8^t@;\r_o[u>pCR:U=*A~g7:>R:sVCR'b.0w\x0b:cWvp>K\t@bY\n'j=G#2B(FtLI_l^", '_o[u>p'), [30])
    def test_case_1476(self):
        self.assertEqual(pattern_match('/LUwL]Uyv0".1&?yZ&"\rm$>IRWPFCV\nf2s##V{me"!`]3;BV)g\'Q0&-VJ3NPxU+\tY-M.$x\np7J->\t8', '\rm$>'), [19])
    def test_case_1477(self):
        self.assertEqual(pattern_match('\x08L/kAK3=091]k)`"<qe\r>o"(J[7+&7HRNupl\x0c\x0bc>V)d`B0Jn\\~_K\x0cS8z_BsoGx]t\x0c_:%\\K_l0`*l\x0c', '%\\K_'), [67])
    def test_case_1478(self):
        self.assertEqual(pattern_match(" D=6f!P+&bvbBk*WHLz/\n&'KeGg{_\\d\rShNwwaPtgSlu)w]Tjx@B(7Z\tE;\x08Wv4l^n`bT?\x0c*&W}j;o~l_'", 'NwwaP'), [34])
    def test_case_1479(self):
        self.assertEqual(pattern_match("G9o:m!IH\n?'@lx`Y/?q^BX<EGl0us^C|62sb\t,>'H[z;;s8|rD=]r7", 'Gl0us^'), [24])
    def test_case_1480(self):
        self.assertEqual(pattern_match('5@>~~VDGBS@5F0!RJA^{4\'40yJ[,_HkI7W&FZDsJYO\'aXM~l"%\nCi1j9{Ra!)K\x0cI\'+\x08_+,/\'u5UoD,Jx+ jJRB|8', "+,/'"), [68])
    def test_case_1481(self):
        self.assertEqual(pattern_match('\r0A[DX:hO\\mhwcs>IgvijbvJIK\'CSl:.t:,/FH\\@;4fb8FU;00W"wid%E4IruaRR', '0A[DX'), [1])
    def test_case_1482(self):
        self.assertEqual(pattern_match('HIUqK#^*D$L8\x0bsN{GI(^\nU\x08n5;L;3G3\x084<)eI)UU,l?qbMgl1av`7jQ;}3yAIt^:j*ZRB/ jn\n\rwWt2y<g;*s3g\x0cX_\x0b0W{\x08tF|, ', 'wWt'), [75])
    def test_case_1483(self):
        self.assertEqual(pattern_match('JtT{$t61bht4Nh/%\\l#G(d-b+z|;5Y-d|Wg{CFEAJgBU*Pew-\\;p|pzi}2a](h-[<*C{:5xaxfaRl{c]ee[P*8A**KMzZ', '}2a]('), [56])
    def test_case_1484(self):
        self.assertEqual(pattern_match("EcvBg?idyP|m86Mp\tUl\x0cVfzA\tjF9qr5tD%<j\nng;>RbwwjE.'fE^F'@j~\t/hPm!DkxBM\t.8R-15Q.C;", "F'@j"), [52])
    def test_case_1485(self):
        self.assertEqual(pattern_match("/z8L{O\x0cXox_i@ZR(2>xHKK\t_&4d]I(tfnsXfH\x0c~mC+-:Q<@@Q%,'^AJ\t?I4;*&ZW^R5X\t0GY'epl\x0bV8+]\x08n]_l", 'i@Z'), [11])
    def test_case_1486(self):
        self.assertEqual(pattern_match("8$\x08/7!H\x0bGkw@ChpnCxn@2Lziq))j'fUJd,c+Mp8;/P[Y<e |Fr#a#}\x08-\x0c;Zf76^&OlT\x0c", 'hpnCxn'), [13])
    def test_case_1487(self):
        self.assertEqual(pattern_match('>yBz~{.K\x08zR_mUKAvj\'Wm.fJnm%|?]\\)ReLLY[[u"XL\rfh(ZC:?1akyU>a', 'XL\rf'), [41])
    def test_case_1488(self):
        self.assertEqual(pattern_match('AV13d&|w\nt< z;x?36WC6?IQgdl\nK!)7"!w%u_(8e\n+C0uV/9ukznVEM2vh\x0bH6+\\L1!k1U;n55auor+S&UJ', '(8e\n'), [38])
    def test_case_1489(self):
        self.assertEqual(pattern_match('%\nFi{+xjD9q`/)r2[C,wRw\x08$2v:\rR{h_4c6H|=NeVxYJ1(\rV9^Np#"6+op_vR', 'c6H|'), [33])
    def test_case_1490(self):
        self.assertEqual(pattern_match('J\r_O&R(2~;@J&\x0bK4Ax\\CpmnY7Z`npMr8N)eWHx/*8C\\2+k!>9ubE:W"BQ"&8+]bi-\t-: Cuh-\nq\\%R(IABV`=aLP\tu\'', 'x/*8C\\'), [37])
    def test_case_1491(self):
        self.assertEqual(pattern_match("$eTs&\rV|3=,cO+f\x083 Y.'y%<hY_c\tU~S\x0bl=\\}N\re_K<L!)w46U\r\x0cl2", 'c\tU~S\x0b'), [27])
    def test_case_1492(self):
        self.assertEqual(pattern_match(']MX@~[8-U\rOUg)@%\nS 6\x0c^ic)el\r]G=:I8->12O&?R\x0bJ/nv8/9C:\x0bZ>@[/\nDAa]3c-=ZKI$Ab\nAVIu#9q@@N;(KLh@/ ;~&`z', ']3c-'), [62])
    def test_case_1493(self):
        self.assertEqual(pattern_match("3P-(f?`HoKT8P@rwo5a5C$\\\x0c#kb:!;\x0bT!8A\x0b9j_KV1'\\%'lda3", '?`HoKT'), [5])
    def test_case_1494(self):
        self.assertEqual(pattern_match('\r\x08\ns?1w6B!Xrkqym;*\'c>Z!v(}`RJ\'M6o_\'ib\x0coL4&+l>7@/+cbk_,"(yE\\Z9C~fty){`uZI2ZmI#i', '6B!X'), [7])
    def test_case_1495(self):
        self.assertEqual(pattern_match('_[}J\tCf\x08ki\\x*qYU-8ad4heVq^Vp-?|pd,|`%a\\#s#J9"[a8bbaD"', 'Cf\x08ki\\'), [5])
    def test_case_1496(self):
        self.assertEqual(pattern_match("J0FL9Nd; (9(QEyuK=nf\\^'o\x0b[ LN=_KK.\x0bx\x08-z_\\>_?TYFVw9#!i'rU{yr<cz", '\x0bx\x08-'), [34])
    def test_case_1497(self):
        self.assertEqual(pattern_match('#%V%\x0bjXIpkVJ*\t\t\\ps=Q9H1\rHVG\x0cTE\ru1oaG%)+a\rC\\U3vK/<!1l&W\x08KC\x08nsGE,dE=KF%xz;~!H[oZ5)n}:|q--kYC<vxD(=^', 'K/<!1l'), [46])
    def test_case_1498(self):
        self.assertEqual(pattern_match('Xyy>;u4p5rIB=s~$\x08]sKg8vo-m5JY9\\?7An1j{uZSDRm+%z`tzZ.;!){!', '\x08]s'), [16])
    def test_case_1499(self):
        self.assertEqual(pattern_match(')Z5@&/yRmWg{pU\x0b| u|FFM&!@M\ryI)jjvbX!4"h&R{(a*H,d[}P8J5vv9,\'Hk8{=kpOU-.Vx\x08@\x0c\'m\\\'0_pyHK\tjD|#XUc', '4"h&R{'), [36])
    def test_case_1500(self):
        self.assertEqual(pattern_match('R\n\'O^JF7vG$%QOmnU(c";tM=\rvTUx!\nl^\x0b;z$-Z r$:?THM7r\x0bG\\HE$W@uoyoiX\x0bZiEP<*AAX"7lo\x0cC7#T/', 'G\\HE$'), [50])
    def test_case_1501(self):
        self.assertEqual(pattern_match('vS|nYeNJ7>/\x08FaIe-UR_[j\x0cWK%{3 *?$5]+Zv\\[}]u\rqY\x0b_fUjX\x08\n>s/Km!6EPH^!8,\\Z}T4tqv+SWK\x08|nM?)>[LX])5\t,V\r:IB', '}T4tqv'), [69])
    def test_case_1502(self):
        self.assertEqual(pattern_match("6t\x0cg8eU#ra$(x(jc.s0K!+.:6<?(^>/6E:4;_|b h'4ev<>\x0cS\tR{\\HJ{^exX\t!&G9", '\x0cS\t'), [47])
    def test_case_1503(self):
        self.assertEqual(pattern_match("Q,E?P3\x0c.Mz[V%?WNe7XR:'mV7 \x08Lko;n-1bLRFT\x08+G}=l\\vpz`R^{&)}BXZ~]4 h\rx*P>gv3<C1Df1`0K/R'..\x0b6)kEP|", 'z`R^'), [48])
    def test_case_1504(self):
        self.assertEqual(pattern_match('$C%\\\x0b\\+a|m\x08GF\x0cx\x0b$ZM2q8B\tA+GN[Sv7P$(1%HfZ\x08}\ruXiWDth6$o.E\nN-l_{y\x0cWAcG.,ba@Ia|Z_!F^)e\r(D', 'WDth'), [46])
    def test_case_1505(self):
        self.assertEqual(pattern_match('jh*0Pom+rl4FyH0v*G!5+%3Az&KihAz/\x0cQ3jI{p}Y2 p>P^E{s\x0b\x0b3~3\tC@(z>OAq.', 'p>P^E'), [43])
    def test_case_1506(self):
        self.assertEqual(pattern_match('Gg[|c`BhY`o]"v}T1:*\rK%OC(KVf\'IfQ]?iq\'B\'8y\x08/$k8Bogu.;MheoW', "iq'B'8"), [34])
    def test_case_1507(self):
        self.assertEqual(pattern_match("hj~O&_oJa:DhaCF/0R$A_pp2yw`Mb2'6,/m|ftS\x08^Y\\-7\rpLA>'cTu_No.yWRz&1/G", "'cTu_N"), [50])
    def test_case_1508(self):
        self.assertEqual(pattern_match('0 \x08\n2ERxUC7tWX{)ae\x08b[TQL-n\x0csGbAbW=4-,ad"RZ8N[QVRS*6bp=KqFA_\'Rk]r>cuK,h%R^<2Sz}wl b{t', '\n2ERx'), [3])
    def test_case_1509(self):
        self.assertEqual(pattern_match('3GJbpkO\\w\x0cuN86o,7rfD"NSU%dGne\r3:~5Hd0N?RHnTk[}jFSk+}.^44_PjM$s]>\x0cC^\n/YQ`<f;=FwW', 'rfD"NS'), [17])
    def test_case_1510(self):
        self.assertEqual(pattern_match('pg8;f2I~xrvr[P@S7p\n;&T+N3IsBF*8SfdKUfi(6\t=_YhK(\x0b/j1vvFXM4i"\x0b={46v9M)R\'1-%\r?!q\rD\r7:>\nT', '_YhK'), [42])
    def test_case_1511(self):
        self.assertEqual(pattern_match('aOXzTL4>\x08\x0cj&g8qT=\x0c\t5Es@uI)c}\x08)zl>@*wK@o$_\x0c4@x%&(5\x0bZ,Z!vG*[J\tQ-6\\VX0?WyI ', '$_\x0c4@x'), [39])
    def test_case_1512(self):
        self.assertEqual(pattern_match('X7G)k\x0c]y\x085.\t\\\th}j#::I(X#nWnuq73<&me~]\ne*p/ByaC`uM?27/lKm', '#nWnuq'), [23])
    def test_case_1513(self):
        self.assertEqual(pattern_match('L\x0bq`}G#-VDFWL.H\rX|/"xt<FbB-\rh_vANFYni+Z\'wvM#\n/Stjos_N`?C\x0bz0oUR\rAf218Rt=ajkxrU %,[g', 'ajkx'), [71])
    def test_case_1514(self):
        self.assertEqual(pattern_match(',zX?}O^\x0bFp\x08h5uc[rKUPLCpi.8\x08e`|j9^NE]IgeC#245!\x08bs*|j', 'c[r'), [14])
    def test_case_1515(self):
        self.assertEqual(pattern_match('RV~bB0[`)8<<x#0_dO{1D\'TCQ[\\Fq~}+x\x0bX\n\tavXO&=;")POU*13F\n&"]or$x\'q\'5H(YenwHz7y1J+~xxfSUa)|wJ6 %B>', '0[`'), [5])
    def test_case_1516(self):
        self.assertEqual(pattern_match("RQQw\n\\>5\\?8PE\nX0i^ElIA'+Q`&Z-?%6s5;g\x0cD0i*RO\x0bGs(d>XWoH>`N>Bvl%,$6g_\x0b*]G~4veZ./", 'Qw\n\\>'), [2])
    def test_case_1517(self):
        self.assertEqual(pattern_match('z#T.7j=7v\r\x0bJ\t\tsrO@5 H\r`3/M ;XgO9=3J\r2~Qu,FKeJ_6lVJ:g K=`*N`JO%E<\ta4+Sg\x0cT}DT7X%CR9fLd7>^\x0b}31', 'd7>^'), [83])
    def test_case_1518(self):
        self.assertEqual(pattern_match('H%MJ\x0biBrAyY[rD&VxZK3y69q`.t]n\x0c"tFw<;Ucc|PGw#8<$1a7\\L2)@eg{9KY-eGBd<)~\x0c(U"rC ~_V=[\x0cvV]Jd;', '@eg{'), [54])
    def test_case_1519(self):
        self.assertEqual(pattern_match('XdN37v\n`=\\rqn2E\x08\x08\x0c]u=5r&O)@R>06xo0klQ\x08E]G>MYN"\t}`W|WtcJ\x0bQ?0\nW=Xl8O8gaz', '37v\n`'), [3])
    def test_case_1520(self):
        self.assertEqual(pattern_match('fpYw%,Y.]5LJ U"73?q(.yH9\' Q]\rbYuJ\x082Pd|Y]NWdK/;&/]+iLed)\n*D&L c\x0c3\tkI`Vz:+`Q9mJ\n', '`Vz:+`'), [67])
    def test_case_1521(self):
        self.assertEqual(pattern_match('=zX8SU3?-oLyp#d@%cHR/t~;t3WRsdF\\)SCp;9!%Q$qf;%-Jbr', '8SU3'), [3])
    def test_case_1522(self):
        self.assertEqual(pattern_match("e\x0bNN=f\x0c1(X)vm3a8!^yP ]g5>&>.h24E|P\tufy%'Lnz _t4Xjhd", 'nz _'), [41])
    def test_case_1523(self):
        self.assertEqual(pattern_match('V=K-GH4p$B}IM)\x0c1n5yV/mUS#`Z6_/%GR3\\*-Vnyhe\n%!i\r!rYiPX+\nTt(I2AN~A(-xL\r\nsSOBLLx*^&@$2=Gc_(n{U+Y"kD+&i\\', '\nsSOB'), [69])
    def test_case_1524(self):
        self.assertEqual(pattern_match('^2(UaGG.R\t\x0chC\na{\\v,d?L\t#\x0b0J.:(U2;\tw|5o1\x0bY7YH%<;2 KDBKJUD\x0c\r@74=!b\ths;LM9oAF_Ddt*.~+}\t"bnN#[WM\\q+', '#\x0b0J.'), [23])
    def test_case_1525(self):
        self.assertEqual(pattern_match(']m/R^|Bmb\x0cyJ|hPmb\t](J79Ng_z^xj"NE/khbrP"\\3\x08uEW"E,i+w2N\\-D0>-2/X_6|Ihj6Eew\tB[c*5A\x0bQ', ',i+w2'), [48])
    def test_case_1526(self):
        self.assertEqual(pattern_match('$f1^wgE_Q(;r{Z(cFWWpq\\:r,y\x0bedB{Bw2Mkf|hy\\+8\tRo*6:8`G!\x0cwG,R-]~r2/Qo[8', 'E_Q'), [6])
    def test_case_1527(self):
        self.assertEqual(pattern_match('(=:6V\x08jz~Pe\x08mIMWggF\x08<Zsb-P8q_!Q,tC\x0bn">%xB7H|0lUZyH8C</)\'yurQ\nsCSw% ?(l.c8U', '\nsCSw%'), [60])
    def test_case_1528(self):
        self.assertEqual(pattern_match('V]Nv\x0bsUQ=yr>wb0\x0bt[e\x0coP%Q-~sYGX;N6mG*_eXR\nNe%&R,7{QA_IDe"', '%Q-~s'), [22])
    def test_case_1529(self):
        self.assertEqual(pattern_match('IdZG&kdvh%zNM:-MPt<o&8~WX%[XM3v7ETHv5W\rT.gisdW|-V|?O6tG?~f5;/', '-MPt<'), [14])
    def test_case_1530(self):
        self.assertEqual(pattern_match('ku AB7~\rdwM%1F,&yYwh@C&\'Pp\\W{\x08HpC|ClWTh?VELBQ&Z\'"<F \x0cl#*,vm!^\\I\x0c\tE', 'u AB7~'), [1])
    def test_case_1531(self):
        self.assertEqual(pattern_match("@8va@[I?j_Do{QMn|\nCHI[lF31'NqX\\/&m@Em~sfd<\tWpA;I`m9z\t\\D S", '\nCHI'), [17])
    def test_case_1532(self):
        self.assertEqual(pattern_match('iJ3vKjVq}.|\x08<Z("c;D@T"\'\rO =4A}-7KMu fRw`2b\x0b\n^]YZ\x08s}xJhG%].=N\nY0!R(\t,6rgW~5z1p\x0c%\'61\t`=\'~%', 'KjVq'), [4])
    def test_case_1533(self):
        self.assertEqual(pattern_match('pKiD.HDje\r^^ym(xfdig"@e7)\\Y%XL{HK}8CJ\tvb )rCW/a_]ZV&M\x0cC]?)c[QiA1BL\tTe7Vi4>by \t,g%:~"', 'A1BL'), [62])
    def test_case_1534(self):
        self.assertEqual(pattern_match('y^!!)wTi/dshtQBUs\n{<Kh-"S<\r8(+C,\r@\x0c#U\nJ=}{E@u5[`WDJ}(h$0K<YVR{H[iq\nENTk4^Wl\t:/\\Wr4\tBF^v$cI', 'shtQBU'), [10])
    def test_case_1535(self):
        self.assertEqual(pattern_match('CkV\tMh)Mil}Qb\'\x0c|,O}0T][p8Jnee"o,s%#\n\nkp4^IK3q~tlcL.w', '\tMh)M'), [3])
    def test_case_1536(self):
        self.assertEqual(pattern_match('\\8t&zr%=<Di"D&\'6&e\'\r\\kJpj\niu"uo1RT{C\x0cnur\n:ryxZ0+6Gd', ':ryxZ'), [41])
    def test_case_1537(self):
        self.assertEqual(pattern_match('7P\\dd@JzkOBLMU~?+]<>D7s\rP^~n-1^@)H2F)JL>K~p&fS{QO\tE~$QTpzQW[E(7HneJPe<W@]5]6|p.\x08j9GKd\t }/m$@T', 'U~?+'), [13])
    def test_case_1538(self):
        self.assertEqual(pattern_match("jfi_%NIVh}OSFH5^s1n1MXi^eI\nJ 8%!4.#uOJXu/I>@[o'fz~V;Y2S\n?Un6ysUt|)mnmgkd~", 'eI\nJ '), [24])
    def test_case_1539(self):
        self.assertEqual(pattern_match('jtCV*c\x0c9zAL?Z9&-L\re1=FtIN^x|d"%|uX=h"{~A#Y#SMh$5B0Hlz \rI!J/3N0L\x0cGSMj_$P\rEc', 'SMj'), [65])
    def test_case_1540(self):
        self.assertEqual(pattern_match('t[bA^<NO<yp5.}\'s*4`1Iv6YnW`Vk)NP!W\t8X\x0bq?,sw`TTxf(]R{rF,\x08\x0cU\n"`iJ;I{aT"*_ut2(w\nCd_twsv;zEem{4f', '{rF,\x08'), [51])
    def test_case_1541(self):
        self.assertEqual(pattern_match('g>VG}LFvx\x0bx+{3u|NlE\x08B+:P#I7/>|VHmz^e=E8o=z||\x0c\rL&\'hq]nei0[h`)+[s=}.\\ st5?i_U\nRR-/88\x08oc0o(O"{M NY', '8o=z'), [38])
    def test_case_1542(self):
        self.assertEqual(pattern_match('8]>LH21{Qv3w7XN Uj#HP&WhTO-wM2F$QHoOr$4\nljB$.\x0b7$yD0-Prbve3GzlB&pH-h`m[Sl@k"Vp', '0-Prb'), [50])
    def test_case_1543(self):
        self.assertEqual(pattern_match('\x08g/=\nZ"60$r\tdAs49E_(g$N[8s2XOt>]ox:]6\x0cRr|l56-c9wmt`Fl]rx1C*{D', '6\x0cR'), [36])
    def test_case_1544(self):
        self.assertEqual(pattern_match("KV[n\tnC_\r$k\n'\x0bG_K\\O-&N.nXW\tnYPo}bUp/_iQg:a5vmuLioLuE4@2stFv<L(WUDqfKo~17gh8QbCWC", 'fKo'), [66])
    def test_case_1545(self):
        self.assertEqual(pattern_match('>s|c.z\\W%Hxn-WWa\\!GB#=2+X]S,\'#J14Cm@["8)G{ 9%(/k6 TQ\x08WS', ' TQ\x08'), [49])
    def test_case_1546(self):
        self.assertEqual(pattern_match(',X__RbZ^l/5_x\\(~>N+O~\t<\x0c\n2o\x0b ,e6nL.yfN_Ze;\n0S"|\x08\\y\rTp{OZd?~z["aE0OYMhK`e<z~\x0bV(ZI:\nN\\9A', '"aE0OY'), [61])
    def test_case_1547(self):
        self.assertEqual(pattern_match('FM[mo+Hy6`_I8\\fkf)[+C1+q^Vp,]Wb\n&)=kL:QQM.h($8u=#o2mm"7QyDEEZ^*=EtkM}k\n\x0c', 'Z^*=Et'), [60])
    def test_case_1548(self):
        self.assertEqual(pattern_match('ds#Ok\nN\nAo9X\x08=\tQeF!1(c{=Vt&DXzHn]\\ ~~#n%g 3_+}Qhh+g"7]4^cz', '~~#n%'), [35])
    def test_case_1549(self):
        self.assertEqual(pattern_match('\x0cgFOwrZlnRl9T`9921b?w_%]kW"d**n^CD+.c<*p_`$\\={\nAyS!+', '921'), [15])
    def test_case_1550(self):
        self.assertEqual(pattern_match('D\x089knwa(oPQ@i<@j\t]?N!cy2[rs-3$icJ"Vw~KYem\n@ep5Y]4<5v!V,f r)F\x0c|\nt\x0b`lHZUoHxUC.', 'cJ"Vw'), [31])
    def test_case_1551(self):
        self.assertEqual(pattern_match('"\x0c_o\x08AG}ITh|D2?d@6iO[^:Xk&bf@4|HAGbsT%\rlWx S4\rl@Q"4*a<B!T_"PVJ476SfKb', 'AGbsT%'), [32])
    def test_case_1552(self):
        self.assertEqual(pattern_match('H20ffGQ\n.rKz(A+gyzqr\\Hh=7~K\'9&@Hd09|yV\x0cDi=\t[L"IejsJzSKYiGl\\yWy\x084H3G\t]~]', 'zqr'), [17])
    def test_case_1553(self):
        self.assertEqual(pattern_match("Eq:OW`Y#W\x08!Pl(SM*4v2(\nDmOCfp)\r*f,)Ki\tpY7xM{\n'={PEeSZzo\x0bUp1vj", 'M*4v2'), [15])
    def test_case_1554(self):
        self.assertEqual(pattern_match('`hQ}>:E,*[V3gDC@S\nx0^*=a6\x0cem6I8ZxKsYd:QG;C!7,F\r+&++%6Iv{\rbk<kuPW*dm\\,AaT<@;Br~p`ae\x0c*-C$|3vv]Od,hLar', 'uPW*dm'), [61])
    def test_case_1555(self):
        self.assertEqual(pattern_match('DL]+MFs_t*VZ4zj9s}Ul9\x08]mm<$i&xP}n5qUxZ`^b\x0c;/5i8%?a4F)Jd\x08`\r%\x08g#H\rmMT7', 'xP}n'), [29])
    def test_case_1556(self):
        self.assertEqual(pattern_match("id6rE\x0c[e)FT$lCZ9.jVG^T35uGy7wlD0}4pcU~Yy<lh>?\n+$*v8\x0cC'd[c6v\x08%\tx)cFAY5$?z\nxg[f@>r$aLq:]/PF^6+", '^T35uG'), [20])
    def test_case_1557(self):
        self.assertEqual(pattern_match('}N?URPb\x0b"+{h*cKrgD<*\nL({cj Wu!Ii9!$*8\\S\x089\x0c\ru2B:zOv.OJ]:*ZpcrXT/+}!M1eunDbYQ zA', 'h*cKr'), [11])
    def test_case_1558(self):
        self.assertEqual(pattern_match('JGD@sCO::oX1FY0U{to [sL]y7ZjYx\x0cdM*C4\x0b(qyA$bTz}M`,[QbAXYGg"CFiZ^m)Q::t', 'bTz}M`'), [42])
    def test_case_1559(self):
        self.assertEqual(pattern_match('p1VKsD\x0b& qPYW4\rYD9/VB+ZbJ*@JXeZ !\n;C*}H\to8xZ>IGWOy,8I]f5S>10mIZ?}\x0b>i`|(', '0mI'), [59])
    def test_case_1560(self):
        self.assertEqual(pattern_match(',6q<r[I*dPU\x0c3\n/L,\x0bh=f1IZ2F`cIR/65v)Llk)_3D(,5|azWk', 'U\x0c3'), [10])
    def test_case_1561(self):
        self.assertEqual(pattern_match('\x0cE|[-k.,,9~v\\>qCZA6?=|gAV[\x08;/CjG{EG7!1|kF|L2MFO@p4\x0bIm_4a\n%eRnNT', '\x0bIm_4'), [50])
    def test_case_1562(self):
        self.assertEqual(pattern_match('_ :NgUQ_[$}V,9ek2j3<YC>JeVBh9FPKq9^s8|5nBXk qs\rW4eWYCs$QMdZ&E\\uCwCK,|!Qcw< l$\x08%M"d:', 's8|5nB'), [35])
    def test_case_1563(self):
        self.assertEqual(pattern_match("me]..`DO+9\tKz&t#sm[cCl4qX?0RICNY5+CgJ96V]xw0bx\t-){2L{8;Mp'k`r*\x0b]&@S ,!0?n`P3|%8 K$<", 'n`P3'), [72])
    def test_case_1564(self):
        self.assertEqual(pattern_match('@U8\x0bf\x08vBKiP+QEvi9\x0c0(>%l#5MQ^zDP^/\x0bs({~C#2;X|IMW)Vx(]\\?-@\t)P5/2z9? }r5T*\\iweK+1O\\@:+\x082V6', '\x0bs('), [33])
    def test_case_1565(self):
        self.assertEqual(pattern_match('rv)`9Wuv,Db@*,-|T{ES6 ZX\x0cs@Z1 yQy;C,oa`O$Zhm1#_HO9$F`Da#B/~UUf9L91~O\x0bHrw;4"', 'Db@*'), [9])
    def test_case_1566(self):
        self.assertEqual(pattern_match('KWk \n\x0b22\\d\x08M};4B!S]LAw/Vl:,8q#&{t(WmGBav\\Ot ORH\x0c>nXe`ir(yv: ^Z`Ox ', 'av\\O'), [38])
    def test_case_1567(self):
        self.assertEqual(pattern_match('1E`U]w\x0b5T" U\x0b!?\na\nE<\rM[d+Yw\x0cF~%NHv(X:=/gzgEECno&s #\x08%DG\tl g!', 'EEC'), [42])
    def test_case_1568(self):
        self.assertEqual(pattern_match("WV^<;\nOnFoge/@Yv'aF;$h`c!W5cgP@'4\\Z63&R7\x0bh<~#pj}Iu@V0}>sT\n*J\x0beq<\tF15.&e[).XqWc<ORDTn~YvrY;\rjwwJ", "P@'"), [29])
    def test_case_1569(self):
        self.assertEqual(pattern_match('vY?%s4\nj$ZfTPRz*tLr>1E /NQ\x0c~dTsga#01F,\x0c\x0c:8M?gdAkDSLW[_B>[XF9\r()B\tN\x0c@7\\+-j_U~:@CbK\x0c\x08Vw9rm\th[4nY^!Q', 'ZfTPR'), [9])
    def test_case_1570(self):
        self.assertEqual(pattern_match("=s |[x5jnY6pto!^2V895=Kk]LK\rF*~<fdBJIyC,`7MU]K\x08\r;bEC+[O`cJ1{|bE<SpM'&", 'cJ1{|b'), [56])
    def test_case_1571(self):
        self.assertEqual(pattern_match("Jl3oS>}r|\x08w\x08'mgm^D%q\x084XgV{FxYV\ng&WNNLW\x0cMgxfkd#RLt\t0},v-_$qpJ04^XCM_PU9Yc84@G#xC5", 'Lt\t'), [47])
    def test_case_1572(self):
        self.assertEqual(pattern_match("-%4\x08OA,{k+JE\toX9XeEyKVGB2Bk/;vD%)aL{0C6<gpK;Y{CS8hI).Gh93E'Y[fo\r'`n=YlEB4JpV9W~]~bKo~\n\x0crq\r\nI;+4_UYPu", '4JpV9W'), [72])
    def test_case_1573(self):
        self.assertEqual(pattern_match('|#bdBY*SSQ\\t]q.Lj"l{y"lfUEeaq2)qn4B!}( DZp!\x0ck8]e{{\rt`6Pc(fo%|T>/Mot"MIi0O>KZbw)MiW{%BcD00%EU\t"u~', 'k8]e{{'), [44])
    def test_case_1574(self):
        self.assertEqual(pattern_match('AhvRZb>)U 3\\>0MY,^^42 vo :B3^\x08`0j?mU/_qAJ?o=K2eX,dfeSZINY<i*k{y.#4C;E:P#KqZI|\nik2S\nphY9)\x0bW[p|W(z+Uj]', '?o=K2'), [41])
    def test_case_1575(self):
        self.assertEqual(pattern_match('H\x0c-y4Es=&G_a[tS?s!H\x0c^)Q\nG`@\x0cw-*sDLhOC\nw!w"1lNxC\n)lhmK(#', '&G_a['), [8])
    def test_case_1576(self):
        self.assertEqual(pattern_match("sk!\x08w\\98|_pCA].J><uN_\r'rv&5m/UZgZ|K?pS>\\~S\t9c*;2ktg%6?xvu,gs[d#^w?\\)Ao|L/[0'9~R", '&5m/U'), [25])
    def test_case_1577(self):
        self.assertEqual(pattern_match('3,zLB+f0kjOj=P ,nD*v^kfgPRAYK2<bf~v$^Q1Om`,"ksxwUW>V.]H\r>6NJ\tq\rgi\t-aK\x08s\nl2a/SkO-v Vkg\x0bmb$aA)=d44', '0kj'), [7])
    def test_case_1578(self):
        self.assertEqual(pattern_match('E;Psw<\x0b3#B?DMa)MEP\t{E*m-2Qo5!@[MbbwmW;=<.@DI4.FL~B~f4 -JIYb6VHjSfxAN9\\9Kh', 'SfxAN'), [63])
    def test_case_1579(self):
        self.assertEqual(pattern_match("Gn'=\x0c6\t=G1Dk<GiG)0~'yAwXU+`Ln+Md`$'JUPQIa y?8u3AWr{u%mi<qQ", '\x0c6\t='), [4])
    def test_case_1580(self):
        self.assertEqual(pattern_match('!Tbwj!9|?o}Of>.(Z"Tt}/7d}a*CM9+T\x0b4rI>qA[%hdnVGz5#l\\=Hy@(\rzpz-\naA&.Rq`9tR-w8p', 'aA&.'), [62])
    def test_case_1581(self):
        self.assertEqual(pattern_match('\tO{DLCG1jh-Tl,j?^@?,jJ4c~zgHDGVU0+u0Fc\\l"oy>jWv?6T5=3Tt*ah', '=3Tt'), [51])
    def test_case_1582(self):
        self.assertEqual(pattern_match("kA@L@l\\`5A-Qk2%IPrL8(\t\n|G02g~dJL24 rdwQ2\x0b8&j.X(A/^OmG/t\tt1J+\x0bB'OxcM=SfO@r\\!Buqi)7oa(U}9:f0\t#K-LPE", 'IPrL8'), [15])
    def test_case_1583(self):
        self.assertEqual(pattern_match("r\x08t%W1>M'\x0c:9m*I\nn^7xRB]%\x0ck@V\x08p0uMt;SpFJI=K1_&*ODY\rQXHKR318>o./?,@hnvW'(~+k\nEmg+#/{,G`Svjl", "vW'(~"), [67])
    def test_case_1584(self):
        self.assertEqual(pattern_match("['a\x08ch{DFeNQZ9fej]-LEyu M/_XBr\n Ku:%{cW\t%\x08][,#P%&\rM7aqk$gvBv\tJ-2KX", 'r\n Ku:'), [29])
    def test_case_1585(self):
        self.assertEqual(pattern_match("wu6:ml^HD^%T,11I7x(3gZ'EF(Hp@6U2SI4!B;.HE2Gm9y^R/B\n6OV]T9*sH|Z^:,)?Yt[FNK$K8Gartj6&[)", 'B\n6'), [49])
    def test_case_1586(self):
        self.assertEqual(pattern_match('Qk>@\x0b?)[sj%\x0ck9Ar@(SBzBF1yQ/Ru1\'rt"r \x0cepDDO^;%K4"P\x0cG2]~.V2rm\x0cLzs%\x0b\x0birbm@j>Vl+sIcA#', 'Ru1'), [27])
    def test_case_1587(self):
        self.assertEqual(pattern_match('X`:00[1ZuK4~)RPH!*;b(oqlo6_mz.T:):\'\x0b\nM5\\1rs^iJ1JenCn#^3Us5_1FH!*\'@b{#7"h\nGi2\x08m #KS,0>S0f\x08\'chi', 'm #'), [77])
    def test_case_1588(self):
        self.assertEqual(pattern_match(',k\x08Vk5V5lw &PV7\\3\tvi+lR`=JBGBPdK\\\td5(iQ$zK]\'g+Tr/prs]{\\yMt;\'cpS=\noiC v@8c\t*S(HCO\x0bq{uq|"`qF)', "\\yMt;'"), [54])
    def test_case_1589(self):
        self.assertEqual(pattern_match('A?[b."rgp;XT\x08Tao$W!$car v4r\x0btY,L$n\\Bf57\x0c,rSuntC>o\x0c{V"\x0b@\tbdQ8@KcN+NL(@fuQC!1clDX1r4', 'W!$car'), [17])
    def test_case_1590(self):
        self.assertEqual(pattern_match("9}x.T0|vpcQ5*= (m;peJ3/l\t>yzCa|acT#qo)Hop{KW'|G;39B0", 'acT'), [31])
    def test_case_1591(self):
        self.assertEqual(pattern_match('OGKs?~/xU wxeaW!C-u^\tM\nrt+\\lw ky-hKC\r@<vF)6Ey!6F;0ws^\x0cYR', '0ws^\x0c'), [49])
    def test_case_1592(self):
        self.assertEqual(pattern_match("1DVlwNDay.ov\x0cS'w}o{lSHRe0SVs-Hy@ao\r2t0 *\r9?1GJ~\tS*vV1_F\x08MV1daCVOsI", '0SVs'), [24])
    def test_case_1593(self):
        self.assertEqual(pattern_match('nzC~0y\r~vdY5sKa#0aI`]\tl<k!>n3H39Z;/\x0bQ|\n\txME*\x0ckv@oWg%5x', '*\x0ck'), [43])
    def test_case_1594(self):
        self.assertEqual(pattern_match('{-4TelstJAXn\rCHDS,AG[2()!*Ie)TRdar_$@Ui`n 09fB,~54167|HYY', '4167'), [49])
    def test_case_1595(self):
        self.assertEqual(pattern_match('Yh\x08d\'y\tU*u-Xhu~S`jr(ONtuk(oPp o%_8.VHG)\\YwALXj`"-Vljy', 'p o%_'), [28])
    def test_case_1596(self):
        self.assertEqual(pattern_match('"{\x0b)\t= b[4/nBT,[5O-f\t#IWv\n&\x08!!Q+9TW(e&c,]uhJ.@\n2\x0bKic0ek]XAS-}EAip=uY>3`FU=+{\\', ' b[4/'), [6])
    def test_case_1597(self):
        self.assertEqual(pattern_match('X7&ny={G$:l\x08~,tvt%N\nZ\x08Q)I\ryCge~My/QS~s|v\t\nK^=5u[7\'/g;h6%]gEY[CEK\r"+k"IC]J\nA-|>,rF', 'J\nA-|'), [72])
    def test_case_1598(self):
        self.assertEqual(pattern_match('t~,"vSoEp~5c_*Y\r1/;wn7EW)w5b"iVuQ<L=Ce]CnLZPRa1e?8oz5Q\'W^b)+\x0cR}mU-lm}6pa>NWVMe_6[P\x0b;AW/\x0c_bB~_N|Mb', 'SoE'), [5])
    def test_case_1599(self):
        self.assertEqual(pattern_match("%WDs%Bu#\r5-!=dy5w\tk$0DVrRDf~O07vmgTcX+\rl9'*Iqe2; Wi}aFj'D_[B1$8 R\\]\nFty'B Py8~&p\tL", '%Bu'), [4])
    def test_case_1600(self):
        self.assertEqual(pattern_match('bE<xUk{B\x0c&z--Y|-C\x0c5(/^Fn8 ]0S786K.XuNX\'`Fp>, ZtuB\\=o\x0c"r[&KQN0u^5+"$*+(u#iBxf7).bo\\CY', '7).bo'), [76])
    def test_case_1601(self):
        self.assertEqual(pattern_match('PJ"[ck2v;\x087B-$+\x0c\\"k<+s$xx#zg+$Zg&<|\tKyqBcfN,\x0cMf"ES0Vm ]![MwV>p\x08"NlgV$g\\Qf>M,7q\r?=CfCNTdAh8o', '0Vm '), [50])
    def test_case_1602(self):
        self.assertEqual(pattern_match("o~.g+qNh>q' *~E>o)#_!`WKjZ}!BokDQ0.ky%V-9[_?HzE dxWvYh!YH86=- w[};9-AC-e6\nsIGIL", '6\ns'), [72])
    def test_case_1603(self):
        self.assertEqual(pattern_match("NAzd4:y\x0bqHdYChByj0Shs>wR`+_Lr\x08`92u;Y4[I\x0cE1r0Ll@T`wupRJs;$x~U`#;\nxs3m}o.\t4xj3QrtIU/)')", '3QrtI'), [75])
    def test_case_1604(self):
        self.assertEqual(pattern_match("!C5.SW.5D.'XJDnB_AT(!dnx6 WLTwIX]jUK-M2'~d`R629F*OY>FK5)-YX/a=&|xKxgtYF;pD#>' ^*MutiS\x0c7c7oQ", "'~d`R"), [39])
    def test_case_1605(self):
        self.assertEqual(pattern_match('2UXGQ6/9\\o/&MY)WjKIdc6\x0czJ \'ES\'2&v<#Qa~B:=\x08nnm-Wgp^bG^"WoHSB5kIO\nI8\x0b@-id3 JeT`~~&O}?\'=fjF]j^x4\x0c\tbgas', "'=fjF"), [83])
    def test_case_1606(self):
        self.assertEqual(pattern_match('SEpE.~9;v1X*\'5{B<Ozfm_sd<|k9@xQx\nm~DTxc4"P#DW6y0@[\ruQ[O\t\nMYtpcOFepZ=|<?>l\x0cU\x08n_{\r6zy")hrm>J!DV\x0cy ', '4"P'), [39])
    def test_case_1607(self):
        self.assertEqual(pattern_match('9lra!(>Dn.44bZ%8zSE;2GIw>n(%,)4]v\x0c1rQoSdo%u;=Jp#T};@d~;1b,|e*!(pIOxc7Db\x0c\tSFZnpRdu', 'w>n(%'), [23])
    def test_case_1608(self):
        self.assertEqual(pattern_match('^TgV`n>/{6@DHs<_se8$B,n`UJ\tR(5X_1lzrr{te:Z6yWaJ6USk ', 'aJ6USk'), [45])
    def test_case_1609(self):
        self.assertEqual(pattern_match('zZ04m\x08,$CES:}s=<%o}vSDex[ew*WmK\x0bIu|*wY`rz)4\ncs\x0czjs&\x08\x08K2U\\~D"YExCX4\nZ`1i', 'mK\x0bI'), [29])
    def test_case_1610(self):
        self.assertEqual(pattern_match('M{Yx3E&Ue!ZXW6qNKb=x|_2L?^w$ b:?YR*W4d\'J\\ju"R7L#]Rrf5814kP[d{uln=S1}v`9\r?b?5"C', 'Ue!ZX'), [7])
    def test_case_1611(self):
        self.assertEqual(pattern_match('B\x0c\nBpwi)\x0bHkYb?\rKPE#.%E^l8[n\x08=hsdww5}b}tys_/*%vj-[Zb', '}b}tys'), [35])
    def test_case_1612(self):
        self.assertEqual(pattern_match('K\x0b,h$%\'YWx.Q7r04yVcu|M)R8!\niM0/danD70E$L?Y"u!H)09M^1;R+>sK,!5MW:-9"j\rD,g\\7&Q\x08@aBn5\x08\r}cugdaCv`(u1+S', 'H)09'), [45])
    def test_case_1613(self):
        self.assertEqual(pattern_match('Joy7Y@C#C<-oC8AMB(P2Tu^%__Gg\x081{sP9A1}?LphZrzI#"?v5cv?$[_@+ xOiC!0*79QZGeJxr@!T3\x08YDt\x08', 'y7Y@'), [2])
    def test_case_1614(self):
        self.assertEqual(pattern_match('QT|\x08hKAeX/\\4FTP>rs\x08\x0b[DfI)5G:\\Z_C,S:[$\\-W;iRU]hN5)mBoim>&j]+\t+`/"],hmac', ']hN'), [44])
    def test_case_1615(self):
        self.assertEqual(pattern_match('shU6Q{bdx6bQ2oOQSq:Qd\\+!|KnkcCK{]3g:w(R:P=zpRs<R2d[A^}SD', '6bQ2'), [9])
    def test_case_1616(self):
        self.assertEqual(pattern_match('\'&q1,Y=[:L\nC9a>2\\(MXHo"_B\x0b{M`@uVS%"0Gn_B9<7%tXU*xYG{k7D$DC_^s\'$5R5`lRBh57fan[5b9i', '1,Y=[:'), [3])
    def test_case_1617(self):
        self.assertEqual(pattern_match("i'9\\uso\rZO=E>2Zj5\x0bWE\nJ%}jsr|\\m_QPG9$}8<v`@4_^[cbeji!eyoU{;d\\9Rk~l/~C&!M3", 'J%}j'), [21])
    def test_case_1618(self):
        self.assertEqual(pattern_match('_aW:q%uVzWdA7z7C~F/"HD\x0c3BN%l6lD%i1\n<Ble\x0bxI -#\rYGX6h /8O047$wm*W', 'dA7z'), [10])
    def test_case_1619(self):
        self.assertEqual(pattern_match('; =N]x\x0c"\x08:VN_PY,!]\rE^+8fx:DKy6o&`tksj\\nBBrOmYH9P]h1Ny\roF4T[', '\roF4'), [53])
    def test_case_1620(self):
        self.assertEqual(pattern_match('D -j3HnT=*;;5\x08|D3qqEN.Memf,`CLl\n~/AaQ/\r&odCq?!|q`029N{d%q]1tPug-\x0c$H@', 'N.Mem'), [20])
    def test_case_1621(self):
        self.assertEqual(pattern_match("\x08gj<Tg'_\x0c8TS X~u-;j[uiJ,k|{5R_Cu?5BFd0/`h*~ky@f@\x08,vDz", '*~ky'), [41])
    def test_case_1622(self):
        self.assertEqual(pattern_match('O\x0c<4uVkF`WBN_v nmxy}cp~&e[,\t!P<.{GNC:+CF)?})?qL\\~c=D_', 'BN_v '), [10])
    def test_case_1623(self):
        self.assertEqual(pattern_match('2uwVF@gp>p\x08DENk:[=49xoDq}cI]q4Xh-Tj$3DsB7o2<$\x08\x0ciJ7\x0c9)tw<\\?!', '}cI'), [24])
    def test_case_1624(self):
        self.assertEqual(pattern_match('Q4Z=t\tEoO^JLVY6ukj9s \tF*xyJ)p6>c[{rHj}p^WXCS\x0biDywCfY/RNm G)\rDHdDR`io~g/Z,./pe.FZ OH', '{rHj}'), [33])
    def test_case_1625(self):
        self.assertEqual(pattern_match("!s^1p9AdB8>'*Mlhu6%1w1RU]GG{pR(=v/4?K;*Z%v\nae14f#D", 'Z%v\nae'), [39])
    def test_case_1626(self):
        self.assertEqual(pattern_match("&hrMJ-2<-&\x08w2 03FU%vgG}3-CVJwz+^ta/N|I\x0b?v'.%g#Qb%+N4a78:5hS yh#T:~}A<\tXOM6EZ7&+\\X^iiK", '6EZ7&'), [73])
    def test_case_1627(self):
        self.assertEqual(pattern_match('Ca]Po*uV"hh_]@FOa%lXbGF,,Mp~[P?ih/r)$tQ+: (=-Z{7M%_,s8=7w\ryFaz; l6/\n{RPN&Sek', '7M%_,s'), [47])
    def test_case_1628(self):
        self.assertEqual(pattern_match('JS7gpZBH1\x08XC-bxE9i\x0b}N"Ql6/8c\x08[E{#a\r4n0m;iQ\nib 3W0AMYp4xF@Cq^\tb2iMB}~&$U17Or8%runDb` 7', 'MB}~'), [64])
    def test_case_1629(self):
        self.assertEqual(pattern_match('|\'\'sbZ`r]z8-7|F<z2?E\n\\\n&\r\x0c|w:X%plRSv[89o\x0bDlK:f<P%Y9GEn!RNUJV \rQ9kDX/P\x0c"t;.[uV0.gOd5ie', ']z8-7'), [8])
    def test_case_1630(self):
        self.assertEqual(pattern_match('%_o_SrsQ;=\nEhzY]O%OgZ\x0c)y_Oj}Gs3\\+q0"l.;\t+1X0"|n&{@r)*#S%[pf7w\r\x08\nPc\x0b\'"L[\'mKg\\j<\'z', '\x0c)y_O'), [21])
    def test_case_1631(self):
        self.assertEqual(pattern_match("C~)_Ec=;/)5~MEgCDfy\nfw(=-o1+AcQBZ<u8igBkpPcPcyMgQ`/FpS, +DnN'", ')5~MEg'), [9])
    def test_case_1632(self):
        self.assertEqual(pattern_match('"ez3C*2`6,/T2FzkT[\'|x#o_0Pj^N\\[2my>\n3\'7o~?6Sc>8\'Gd\x0c^k4&C:s\x0bT\x0c,n`(wE7@k%$G-;\x08bs74,~+6kPI5VY9A>2~}', 'Gd\x0c'), [48])
    def test_case_1633(self):
        self.assertEqual(pattern_match("'(~\t_A9\tFDPRg\x0b$g\x0bLsuk6H^[KBRJ3hAV3uDu/LQn fU*H*&\x08^6~d", '*H*&'), [44])
    def test_case_1634(self):
        self.assertEqual(pattern_match('IbvKZ>GmO<a%=T_O,*oPlxO\tc/p\x0bW`eZ(\x0b%WDtDg}$x@lebIPk_Z#2UjS6h94\\M7;siX#$t#M9kET[P\r}yMJ\x0bZOINP[;@_l\\AM', 'NP[;@_'), [88])
    def test_case_1635(self):
        self.assertEqual(pattern_match('\\rJ"IWkCT!l6J8HS-ed.6MlQy\x08fzu\\`ND B@\x0c&56aTrLt:3Le2', 'B@\x0c&56'), [34])
    def test_case_1636(self):
        self.assertEqual(pattern_match('SbeN!Oa3Cj\tlu7fg8/?eXb\r`M<_lnpW@s^DF*C|?M\x08\x08PfZ:njttE.yy', '*C|?M'), [36])
    def test_case_1637(self):
        self.assertEqual(pattern_match('WkP:8Jcn?2:Hqwse\n33q!yO}tUc~#_{(Ap\rx>~v-[^)^xbxZ|s)j?!f(OT,A:0eB', ':Hqw'), [10])
    def test_case_1638(self):
        self.assertEqual(pattern_match('X4_/zmKucQBRqnBINjz:%jyr{SZ&.}~lin%S!=[\x0c0PnB0wEgs?.a)\x0cxN]k\\@KSJKZn^Fnml`_cA@}iZ\x0bd]7j%\tpmj+(m]!', 'yr{'), [22])
    def test_case_1639(self):
        self.assertEqual(pattern_match('\t({B)BT\'#0yHI/5S&SPX=0[/=b[[Hq!1gwMoDxyr\x0bu!D\x0bI\'WNh &HF"uxs,F@?\x0csWD', 'yr\x0bu'), [38])
    def test_case_1640(self):
        self.assertEqual(pattern_match('notX=r}>=W2,hMZ=-v@nttvu9mHB4Ust~?kdf4EazXpNfm:)qsUCF`T#\x0cQ', 'Ust~?'), [29])
    def test_case_1641(self):
        self.assertEqual(pattern_match("mz@{'3|;'PZ\r6j_E;_5:L@b}_s_2j\\zf\nWrZzXlK9\x0cF{8O9CE\\_m}DOy \\@Sr J:\x0co(u%b\t&)i86bu@.i`.<hkc\x0b <YJu*V%", 'E\\_m}D'), [48])
    def test_case_1642(self):
        self.assertEqual(pattern_match("%?(wEwLYW!Ot bg'{^fb))3;E`v[nc!<\x0caTeC\r4Rk1 v!i]a'ZH+|SS!Y@v[2yT}dyd\n5*y6/Nu,tq8/6@Kf32a7I@N /", '/Nu,'), [72])
    def test_case_1643(self):
        self.assertEqual(pattern_match('sn22-m`Jt\x0cS\rSSoi%9*"\n#P\r\\NvC%t2&}COo.h|d@\x08QpG9xYy3SE2Ew({MIf\x0bjCgQ<dpd mCHl\x0cWt\r12nx?E\'MF!-52xa~|}\x0c', ' mCHl'), [69])
    def test_case_1644(self):
        self.assertEqual(pattern_match('j{6(A}(*aq{y`9c]\x08xM^v@t|ila]YjR%<d&l^U(Lb\x0bq17+aX6yPjj^L0"/Hs+xY?qq#_j', '<d&l^U'), [32])
    def test_case_1645(self):
        self.assertEqual(pattern_match('|G{TZO\x0b`1MpVmoxyQcALa`A}eSi;3p<7%OJepxyD\x08I@_|ETOBB.TX*6mOb', '_|ET'), [43])
    def test_case_1646(self):
        self.assertEqual(pattern_match("V3QZ/_pzM+\n2Ab]&E{Wf&k!]'*<89Ci2+p^b]Z9/Ry\tJ/1PwsRK", 'Ab]'), [12])
    def test_case_1647(self):
        self.assertEqual(pattern_match('OX^;8^B~j*>Pk~B&\rHhq1J it*)9WKhGyrs-\t;]v)]z\\#7\\w0Xa4y\x0cJ5Os&h_\x0csoi:+^b', ';8^B~j'), [3])
    def test_case_1648(self):
        self.assertEqual(pattern_match('B.f*S,0\\rtOtE1+Dxz8ZY-GnziXl0a@\n5Ab\r$.|h~t[./C/_-);|Km\x08ER6bWN!Q7,', 'h~t'), [39])
    def test_case_1649(self):
        self.assertEqual(pattern_match("X5k~O 2'_y0KaYN_AS{_\\nB!qdGg^\x0cxJ}pv{uI\\[}a,%e4iv.UvVfhr)vMZGT)\\E&\x0c*?", ')vMZ'), [55])
    def test_case_1650(self):
        self.assertEqual(pattern_match('%+FZUVXHd03dW"V1^.>IO\x0c]kJz>Q~)~FPM%BE3#.WT^\t$^L!N"z/B~\x0c=~%b!1KD](*,(U@)p=a$j/O[\nJ5=B.w~K}(\\a \nl', '.>IO\x0c'), [17])
    def test_case_1651(self):
        self.assertEqual(pattern_match(';}GO*HD;RnU\x0bjc:ni|ulRU(q\x08>>.Wf5ZKf/Aw\nMe$~)-%Jl}A]{@tHg', ';}G'), [0])
    def test_case_1652(self):
        self.assertEqual(pattern_match('i#yOg$Gi;\x08~IZ\x0bX.:Nf`7mEfR^"G{P]t4<JH96Z\n\\n+N[T*/F\'Po7g~HpV\x08lT(>PY$JGda*QxI_5VA%7#D\nBT^oz=f1A[ku\nD*Ob', 'T(>P'), [60])
    def test_case_1653(self):
        self.assertEqual(pattern_match('2fR2Bo\r?B3\x0b\x0cDjD/ia: [\r}}Opwsd?n3z9_&W\x08&VAj_[RRXi(?[P]/fxgAs=3/QY4t,(,?Sdd=B?vAN&[/o"BU(p', '&VA'), [38])
    def test_case_1654(self):
        self.assertEqual(pattern_match("T,Q,0a-!C_wjY]*t$0L.Zum8\r0NRp|G4dCu:TKsS&O-P>5b<1%>%4C'aa(Q8)r;6\\uw?`O'[8ALWrP\x0c", '0NRp|G'), [25])
    def test_case_1655(self):
        self.assertEqual(pattern_match('X\\jH(\x0897\x0b\\l% lgX1Z9}sGW\txw]c?d\t-".8SMvfK"\x0cC"jU_\x08i)M|;Ye )16(qr014.\x0b#;', '".8SMv'), [32])
    def test_case_1656(self):
        self.assertEqual(pattern_match('>~-QL:r\\XZX0?*tq{W#U9`~s} #p<\tlN5 ]deD%oA\x08N\x0c\\K&Y0ESjAsYuY', '&Y0E'), [46])
    def test_case_1657(self):
        self.assertEqual(pattern_match("BOSPeuVV\rs1\x088RF ojMk|bexR](-q55!Y~.6\n1?y>x#8-' HYY9n?m5lSy%[U~y,(Di8<9''\n4TqJ", '(-q5'), [26])
    def test_case_1658(self):
        self.assertEqual(pattern_match('0YB,jH~"8\tdA\np["h\'8l\\[cg?{\'Ve3x,".fXD\x0c@#wVQDpav?~gxJ?4@k\\qO,vNd\tsJ=G[LT=-=(G\naA@RxN\r#=j`6XcO<v3', '"h\''), [15])
    def test_case_1659(self):
        self.assertEqual(pattern_match(' YpoRe05~K\x0cZSH!j.{L\x08w\x08\\mv[P.46F?\'t!8"G\x08#\n2$r5/dgiw}2P\\V', 't!8'), [33])
    def test_case_1660(self):
        self.assertEqual(pattern_match('<@Z@7*)(i=sQ#`\rS\x08_3GsSA_a\x0b`Vl#l]R8#h::^#I$vXu_a\nj~Ew', '\x08_3G'), [16])
    def test_case_1661(self):
        self.assertEqual(pattern_match('o[\x086YO=e\'Kp,z\x08I\t\x0b[<``l\x0bEuink/k-7Dz46H-lfS(YH`\x0bOi.!8Fc":o+#;\n{[sn0rPM*nBX\x08# )\rnWp3\'V`?,&6T\n"onqd<a', '\x086YO'), [2])
    def test_case_1662(self):
        self.assertEqual(pattern_match('dr/(V&z(\n\tl6[_$&Mp&6/E!7&o?@yn$\rXM]058ix\riozfjA[8Z:4F|\tk8([\rZB=n3Ao1r-sA~}vLi}:', '&6/E'), [18])
    def test_case_1663(self):
        self.assertEqual(pattern_match("5NS!5$D'j`B3beB t{33y_~IIY[Hhv?16gBw6{N%\\K7uv1DvxZjx@*\x0baT xU5w(}f/@!.OJ%,\x08i(Z*kNP>?\tNmhQ&?h,U*#", 'Bw6'), [34])
    def test_case_1664(self):
        self.assertEqual(pattern_match('g\'f\n}ru#\tk<v[x]{i?q^iidy^B?ngM=n-S}HGP\ndEr)Fr4_ZZpn@A/Bc$fDJt>,"?##Jg%B0#SPc\x08Y/(\rKNCP;', '-S}HG'), [32])
    def test_case_1665(self):
        self.assertEqual(pattern_match('7$CF3\\5e\rI`/\x08{UB~S@z }}fn|Mrq\t!U}Q~<oHg<=a- .ML#lvldt"b"mu,bk^/xXdb{Ge6l1\\\'3w;P%\x08\x0b$Ra4]5A;', '\x08{UB~'), [12])
    def test_case_1666(self):
        self.assertEqual(pattern_match('\'[\n2}Q?fX\n{#\'j"{^?)TDdUCs#={,l;:Q_SK1>A*w8KQbd^\x0c#C\x0c^1W)vG,kI(,=1x2$t`\'iLlr$*,+KY}dsk=c/@D~\x0b%+gv/zE', 'j"{'), [13])
    def test_case_1667(self):
        self.assertEqual(pattern_match('a,6.N8Ob"8D!>l(<mb2&n6d {dkY_XP|P:R\r\x0cD@N* e H)W6$C$XTo3)X:P"C8ji\t:DKg -#4\\"Pb#OZ', 'e H)W'), [42])
    def test_case_1668(self):
        self.assertEqual(pattern_match('UQN\rlqDyX\rX>h-x+\ta2$%J5Q,yT]xpEm\tXAo {ZyAJo\\~g\tI">wP/5sH<0^4-@LD\t4H0X6J?(i\\ELXDRgB.zA"WTXI+CS~eZn0', '5Q,yT'), [22])
    def test_case_1669(self):
        self.assertEqual(pattern_match("JIH\x08;?Z\nt,,aBTB$+')6\x0bjkxM*1^x'iRUX*[du?`>H3yS\x0b-wadaJ(\n`0gM>KZ'E8n|c\t631tfcRi/2iu\ra.2pJ&!\r!,", 'B$+'), [14])
    def test_case_1670(self):
        self.assertEqual(pattern_match('B-#5\'oKQU~,:zfs;"fz(|L~=,1fG,dwtH<A-&][uZz\'}ET99Fq-_U9\'dv', "'oKQU"), [4])
    def test_case_1671(self):
        self.assertEqual(pattern_match('om>Kv^>s\tU?\x08Kf$v\'Z ,=,R\r hjT[),,_3U}}]<;]x~-|#Z]mwDv_H\x08?$HL4Nuk\'?#mLGrfE\'E:\tMP`:K8"3O=b\t]o>Bcj>', ']mwDv_'), [47])
    def test_case_1672(self):
        self.assertEqual(pattern_match("\rg^e>i+  5BwmlgD1>EBA4k\x0ceblNES\x0cDN7BHWW,J55%s$2M.QgM?kbmZr~Jx';", 'BA4k\x0c'), [19])
    def test_case_1673(self):
        self.assertEqual(pattern_match("G4jNc,p\twd.1AP\n,(M+L#l\\ztGr|3\t$/Db1C({%i/T9Xu;3\x0bT' 1q{@3C[`%{ClRTqp[0c(u [8%ncnZ\x08#O((B'~QbW", '4jNc'), [1])
    def test_case_1674(self):
        self.assertEqual(pattern_match('N"Y50:"Y\n=\x0bYl(%b)t bHe2(u XS&\n@]uZ\rAC8:<wY*okM=5?,\tW_3,67/m$\tH,baV\'K+<', 'W_3,6'), [51])
    def test_case_1675(self):
        self.assertEqual(pattern_match(")W%|-b4]v\x08AtLE,Aj]> a \x08H/A\x0c6jtc^&oK~e~t\r?.jq6YheW/C$wl'Z.${_)\x08\r2IJ2K{xYi,}p \x0b0oM<T2u|pHM\x0bAi=@]o(", '2K{xY'), [66])
    def test_case_1676(self):
        self.assertEqual(pattern_match('\x08^lT}!n.)"Ta,x5k\\g]Bay\nmi7i+]/\x0c\x0bJDBdA[(D\x08F.M>/,>0v$z/t4\rG)j7\r^-9`[fgN>XfLZ,8 qM"\tn~V0SZN}', 'V0S'), [83])
    def test_case_1677(self):
        self.assertEqual(pattern_match('y2 Cjt#,/\\YrRk\x08+Lu-oll38at\t&J^`\x08X^fCt_`rZ=<v[Qf)i6-y\\^Hem3', '`rZ=<v'), [38])
    def test_case_1678(self):
        self.assertEqual(pattern_match('\\Y#XPi\\0p5<J-Gu%6#0=1\x0c=,+;hCq`_.sOYIK7\x08Y\x0bxUkl\tMfzd\\Bsz;a7t:CH9\\r6\\g"+?%[\x08e3', 'J-G'), [11])
    def test_case_1679(self):
        self.assertEqual(pattern_match('rjPk{\'KtN\x0b\\_5{\rb8?}(F.\x08(ibJ{_I,;@sO\\\x0bf1OZe1Ajq`U{\t\r)3I{I7z_*}^IaNDg >!lPo\x0b*&}}R`}X@O!U3irD<["Kjn{W*', '}(F.\x08'), [18])
    def test_case_1680(self):
        self.assertEqual(pattern_match('nZ?/]mtQ~zy}I+%94i*[OB\x08@@d0j\rni7ZE=(H}MsiKDs4{7%_o?1#pMA {^($\\|M8\rY\x08(%d`yR9\rWL6kFbgiW', '}Msi'), [37])
    def test_case_1681(self):
        self.assertEqual(pattern_match('N(1r=\x0cJxumU@=S,@W;=wP,@~\tlQMj%<GY]f|{iA#2IBU6B]5V,";*%\x0c6W!0&)X#\tu_za[\\p', '<GY]f|'), [30])
    def test_case_1682(self):
        self.assertEqual(pattern_match('>\r7"bsn\no62;1V`G9^s4rq&I8\x0cuCv3e`L3*>\x0bfH""sNoCZ\x0bBjUGtu0PaO)[&}us,!@.}\x0bte ^l.*#\r_UPO|0fv\n\x08T\r(9<', '!@.'), [64])
    def test_case_1683(self):
        self.assertEqual(pattern_match('KTwb\r SK(ga!#RIYZx8uxa}t[,@$L=QA\\`:r7UJbe{2`\x0b\\^o\x0bx&HR', ':r7UJ'), [34])
    def test_case_1684(self):
        self.assertEqual(pattern_match('9j,0\\a0,[t7Y9-N7O`3e$|j(Ei-[BRupl(Y4A_u%=0BP\x08e/X86]8/6Q3h-``)/xCJ', '6]8/6Q'), [49])
    def test_case_1685(self):
        self.assertEqual(pattern_match('Cw]fY\r]&v|N>a=Zq.:HLP$;$AO%,\'27lO\rljuud,\'\x08a&\nULtU4M\nYNYwuUL4+?CP:9i[UD"\'p5mV{3=', 'Y\r]&v|'), [4])
    def test_case_1686(self):
        self.assertEqual(pattern_match('%i)Xr Hrn&K_8\\\r!yM&H9r)%8By#b4#D5\r|X3eWf=kX;xjgA#tgb^P', '\r!yM'), [14])
    def test_case_1687(self):
        self.assertEqual(pattern_match('#(x,a^|WU";st)$-M\x0b\nVk:\x08oC8FHXZLQ&Pi<\n\'y@.W"\nyI^Q^I>\rF$p?~3=XY/\x0bhcCn39]OWm([Z}3ceqyeHt5SAg~,q*/Sw*#', 'yeHt'), [81])
    def test_case_1688(self):
        self.assertEqual(pattern_match('Nv0\rY?\x0b(%d-ek0EWxL\x0c{&=|qE2ZugIOwj-\tis*`~.gj3S,pQdB5bxACC\tLfJ%k$IA\x08[hjNJ\x0cm<cm^JF#!|\r=t46\rL\x0chKP2/=:;!', 'L\x0c{&=|'), [17])
    def test_case_1689(self):
        self.assertEqual(pattern_match('\nQ7>kqe#Qv]5]lJv`yE0[:+I\nC6{HG5O~+}L:-`T@fP;4{FF7A"Yb(;|~ \'IMu,b*J', ':-`T@'), [36])
    def test_case_1690(self):
        self.assertEqual(pattern_match(',g8\rAUk-z\t\\Izm\t~)pJKr\x08EmVZkGW\x0bfjb[~bQ\'i1y]*1A\rJh"7*nNf\\I\t)\\1\x0c+6.e1', '\x0bfjb[~'), [29])
    def test_case_1691(self):
        self.assertEqual(pattern_match('>%]f(*|\x0b?vn\r"|cq7(q"8^*wvbN4)[W\\@Qh4dB{J[>\t2MY[)hz{9,-NF-LY;uiNwa*yV4O9}b', 'Y[)hz'), [45])
    def test_case_1692(self):
        self.assertEqual(pattern_match("F}-9dmv&?8\x08 {;Mau\x08oYi2_4\x08n'\rCh|SPTts9b=Kh`vb|Ob_o>hGrs+EXN}2=ZL*&\x0bso E\x0bWH", '}-9d'), [1])
    def test_case_1693(self):
        self.assertEqual(pattern_match('l\x0bg\x08A"eRM::U~\x0cO\x0b\x0cwZN|wfliQ>^n\x08G\tWY!gqI>O$.)P\x0cF%8z%({ nkESB\' 4v+a*\x08si%hp`&}N6', 'g\x08A'), [2])
    def test_case_1694(self):
        self.assertEqual(pattern_match('\x0bsp-$\'JXR";\r*!UQQ5*BQ/wn/ifCSbt}p}Bc`R\r%Hm{ fD3Rj-\nZDQ^KW~D9"_\x0c3pX<ET', '{ fD'), [42])
    def test_case_1695(self):
        self.assertEqual(pattern_match('>wI:T\x089[-g/4#\x0c+)|#T;\x0cN6+Gm185XR1i+\x08J4cH:q30l U^\x08y\')k|j.O5\\{"%r\\FlvD2[C9L\x08F0wvR\x0c', '#\x0c+)'), [12])
    def test_case_1696(self):
        self.assertEqual(pattern_match('KuiyQ\t<EC}px"7X$J%\\]V/%(~OAKz|wa(p5JQAcE_4~Ug>]P\'{3UAEX.h;T', "]P'{3"), [46])
    def test_case_1697(self):
        self.assertEqual(pattern_match('y%\x0b^JM"9/*DGPbVrnm F0`yoxK 5ienC?@\n\x0bxj)XHr^@+T"dzCx\\|tQBv#^Ts87t@2\x0cgqKaH\\L [$,ur,Ay[!_3\x0cy', '"dz'), [46])
    def test_case_1698(self):
        self.assertEqual(pattern_match('[2yDEnaYD\x08Etp<e~N\t\\<qi_Ugrm:$}{tI\x0c0u2y8{?Ab1rjjO2\x08BB\t*j43\\<lC/rDy#e16', '2yDEn'), [1])
    def test_case_1699(self):
        self.assertEqual(pattern_match("'7?O,tWm]c\x0b~3HD}:Djjxpey\x0bOJ<|020\n?AvxD+F1gjfwah7Fb#||", 'y\x0bOJ<'), [23])
    def test_case_1700(self):
        self.assertEqual(pattern_match('o3a7FKjSG\\SvOnkjA:QcSeiLII\\g[MR\x0bC\x0c_}{\x08d.y\nRpaE|g^}CkMQBA,b&}aN%', 'vOnkjA'), [11])
    def test_case_1701(self):
        self.assertEqual(pattern_match('4k`xTVR]ZskT:pkgM4y-\nb&nS5lY0smE/M)u(j/>^fQO\x0bQ,)p9TjyV\x08\x0cP\x08kvxz6\njvs* +jYFnt~sH.OD7\rpY\rSujtcw', 'kvxz6\n'), [58])
    def test_case_1702(self):
        self.assertEqual(pattern_match("\nvZ #OqNinB9?&u,Bq&'DR>|RRR!CDyv;n\t00t.^}kEf+Y^r@cQ\t)", '.^}k'), [38])
    def test_case_1703(self):
        self.assertEqual(pattern_match('6\rk\'Y\t_C\x0bPJ%w4C!?z%]S&_Yco2wA$Z9,"r/\nu4Y=M4c.oE?}Vu=t)EM\t<}tMyKaSCB3C', 't)EM'), [52])
    def test_case_1704(self):
        self.assertEqual(pattern_match('N0ceP{9BkdF%"N(yV8*U\x0c%X;4Q_A<ZulxGk+ro2tE2R2<>y\tVrqMv;H2d)\x08rS(FdF|;uS.4sN|A.j7bK>5', 'rqMv;H'), [49])
    def test_case_1705(self):
        self.assertEqual(pattern_match("Z\tXm2)G@qX/{dK%&! i+yO7*\rKf,oG2j'mn\n3>u80C4Y$#k2Xf,2`O:UzrM7J}*pf\nr<Km`\x08Vk_?&b", ' i+y'), [17])
    def test_case_1706(self):
        self.assertEqual(pattern_match(';12Z_O{o\n`^`RFp%.im.x%!hM1WxeT;z50HC;<63##d2SSoJ-v|(3J4\t!WV7#{\x0bC!l4@\x0ceG15-;|F\rX\t2KZ1)h5!f.*//', '50HC'), [32])
    def test_case_1707(self):
        self.assertEqual(pattern_match('6TxTjA.*)~6Eh2(cK(%V,<jzEO+lV#3pMt+ q\r#w\x0b*rJAl{6CFopI(+.Wg7yC', '\r#w\x0b*r'), [37])
    def test_case_1708(self):
        self.assertEqual(pattern_match('$2tKB//O>Q\x0cyLK s}@((*R"\x0b/e%l;w^\\\nNi2@}r\\Ox^b\x08ALq$3=?`z=@*K>\x0b"e!Yfy\x0bHOdL', 'K>\x0b"e!'), [57])
    def test_case_1709(self):
        self.assertEqual(pattern_match('Ma-]3RhxY!q\x0b|QIr4nl\'VRvrzyE}b|b"Q\x0b5rh\rrR{:SDjvgk`7DVN:,,i*1Ed2\x0cZtB', ':,,i*'), [53])
    def test_case_1710(self):
        self.assertEqual(pattern_match("saq$&}L|,]kC\x0c}?rxfHYHh[R1J/2_+Aa*lXl\x0c>/$GO%3ELge+6LsKUr\x08h\n1}T\x0bk\r=Ku<f'(\x08$$O0<\x0b@55.*4<7E~a1\r.?*m<", "<f'("), [67])
    def test_case_1711(self):
        self.assertEqual(pattern_match('*ByCb\\a)eP?<juq&N*fz|S\twsCZkd\x0cvG6#TKomA[q"qr/\x0cB TZ$MG68$_gx:+/\x0c]\x0b"OHsHFF&=s6f', '6#TK'), [32])
    def test_case_1712(self):
        self.assertEqual(pattern_match('Nol 1P$m2hD:"^W8B3N8[Mh+Ad5";WhNup~6#"F46;Fgt6(D:cZXqGt\\CK\r!p@^q:"}Up!$8\tqOq_[@pPIAImF%i+.+P^TGn(^^W', '46;Fg'), [39])
    def test_case_1713(self):
        self.assertEqual(pattern_match('{<V\rkcj\x0b)Nr)l!p8Z$(-w&!Ii9iqF=\\%?b)\x08=1)cE@1^o3n}IRuG)l"z?.53Im~2B@Ur\'AI1W+pE]oF\x0c|', 'r)l!p8'), [10])
    def test_case_1714(self):
        self.assertEqual(pattern_match("*avpBPAW\x0c%IL%Epr\x0b!$Y5tGk|U{5y>'\x08IUjC{7lwx$hA2(t_BVb_h2`cM 'Z6i000A]\r~\x08hgu", ">'\x08I"), [29])
    def test_case_1715(self):
        self.assertEqual(pattern_match('P\x0b_;-8u$:k?\'<@$*Ew6DFa5e Ju2dZct+&1{P|\x08,sbzB~JlIRAhx4)(cfpVLN6"\x0b%AGA\'n\nXrxDYs48A},9#Sf{q(G', 'XrxD'), [71])
    def test_case_1716(self):
        self.assertEqual(pattern_match("JAUT)\t<'7QZ>^lK4!VqvW:\rNVE5:G8g}]\\{'z&uG)baI\nzGZeeN\x08_APXg|&Pa ot]&^v1\x08\ri~pKskUq~&V1Y\\__1t", ' ot'), [61])
    def test_case_1717(self):
        self.assertEqual(pattern_match('{u4w\x08E%Dn&#9B?Ld\x0bKP7MEnqJ8(~%QE<t7\x0c}\rizNGlrM`1E\nyT@d(\x0cY7+M%)R', 'd\x0bKP7M'), [15])
    def test_case_1718(self):
        self.assertEqual(pattern_match('ELOWZYrOg^+0Z/^}u\x0ctPThJ@9AEImN$TFAhySO8"NMwN\n^NX\x0cJ7oH2gSR@NSa]:--"h%G2U4nRd0"6%m=,', '0Z/^}u'), [11])
    def test_case_1719(self):
        self.assertEqual(pattern_match('y"Vd!\x08g >`vDb3;0):Vm:4YoYN>2"|Ef*iC3v@H0  \n&Yh*5 nT\x0b\rQ(T\tkt!i.Cj\x08^^DiB', '\x0b\rQ(T'), [51])
    def test_case_1720(self):
        self.assertEqual(pattern_match('\n\x08|&\x0c4H(ZgGs8o{4w;S#/VEl%LPA9n1zWtSH4awBprDu#Bn"~Cj]$Ba>\x0bgR7[79*;\re, ( \rmm_\t%C\\\\W`$\rMZ', 'gGs'), [9])
    def test_case_1721(self):
        self.assertEqual(pattern_match('knb@qfaB6yb;mIg "DP|/Fm"Zs9m!#J^/KC?nK|x<4r#H1gTUv-xr\r^\r*!Wm\x0c2,YcPI{1r83+QbYA%\rj)f|\t\')', 'Wm\x0c2'), [58])
    def test_case_1722(self):
        self.assertEqual(pattern_match("Ht*gf\x0cQBhnhN}Zo\x0b/2<T%K5oakh~bRP'Y\x0c\x08qamVY\x08\t\rD9\x0cVf_Wnd#_5>R", '5oa'), [22])
    def test_case_1723(self):
        self.assertEqual(pattern_match("m`nF_|D,v[YB\t^Q#E'[1\x08-\\1WrY\\\r?:hz~>ND\x0c\x0c{64$bTOD/6&f7Cam5\x0c3#$;'c(&0U+b%@$~FPvaW#\\&V", "^Q#E'"), [13])
    def test_case_1724(self):
        self.assertEqual(pattern_match('\x08DZUP\'p~\x08-6\x0b\x08Z$\rB(<BR/Z@eG]XE?Z"4Erba}^N(HL2n$LX8(A7sA5\rNxpxL1;IdtBTxa\'%N]\x0b1i=[M-\rvxE', "ZUP'"), [2])
    def test_case_1725(self):
        self.assertEqual(pattern_match('Me;({V{\tzS]>4qzBa"2P4B->J\x089@ E.B?4\'.qw:S&c^h7\'mN8j,IR\t-JiU:B\x0bd>z;U)H', '>4q'), [11])
    def test_case_1726(self):
        self.assertEqual(pattern_match(',%zSN_1twFh9:#8g|ghw92!7N{+OqeLSNl/20$;H"6>^B"?fv9ZLWM=o-o@*/^,f6zot=x|3^Q\\-1k1M9`*RJ', '0$;'), [36])
    def test_case_1727(self):
        self.assertEqual(pattern_match('{VbwYavLLu3 Wj$9qtFWze\\d3\rV$tUg)]c.sC75XlM,+/\x0bc|gWsG5@6MP5zD)Ty^\r hb2~', 'Lu3 Wj'), [8])
    def test_case_1728(self):
        self.assertEqual(pattern_match('lnG}uCL^W{)c\x0cHq02G~p#?$4cqs&xQj\r->+Z$#:a&n\x08wzlVQyKI1c-eWP~FyF*oI1#Ec!>\\d<sIW', '1#Ec!>'), [64])
    def test_case_1729(self):
        self.assertEqual(pattern_match(']112;81V,f5aE_\ty.6UW.s\x0b:jH5t!ejD>E{q[~\rF,ZG!wW[>`C\x0cfrBLF!K8Zo\\/&2?s;r#A\x0bS\x08\x0b4;5GZB=^@9y~rr-', 'H5t'), [25])
    def test_case_1730(self):
        self.assertEqual(pattern_match('Y@m;F17_F\x0c!tY3B9P\x0c/I#^7Mh\n@\'u/^K)xYJ?;\x08\r(j`0[?osPKE>w]EHB"\x0codkD5`<R\x0b-AZP\x08xl\\9nm]O,:Y$', '\x08xl\\9n'), [72])
    def test_case_1731(self):
        self.assertEqual(pattern_match('\x0cu[E%([3|>|\x0c\nS/Bm\nz.|8I1(pRC#)Xcbh0\x0c9w]*s^L{xU4\r\\=iD{i)A_UK', '/Bm\nz.'), [14])
    def test_case_1732(self):
        self.assertEqual(pattern_match('QwZNx"hYFc|6h9}tyLN0=P"Q=]\x08B1]v"s=/m3GRM6]z}WcH~ "cC^b *\x084YYOW;\nK?RR.J1U*}-i\\6W(w34', 'x"hY'), [4])
    def test_case_1733(self):
        self.assertEqual(pattern_match('+@jrX^W"t3uf[H\n6;9\n<.NgI{m:m=|ATxwZi=mNN>-Odu4ce\rHP}\\S5\nsR#\\I\tr~EOGhIY!?k;|mG2D+J', '|ATxw'), [29])
    def test_case_1734(self):
        self.assertEqual(pattern_match('XE3%n`3="+CN \t1b9/4DrE?o`q.S@js/uRA\x0cSZ%N11W=Y1@s!BZ<7m\x08n@wM1\t7rtC0/qdV', 'm\x08n@w'), [53])
    def test_case_1735(self):
        self.assertEqual(pattern_match('pBQ7E=r5QXdUcf-%KMo\t#>Ns1\r`{\x0b\\WjH+3c69J\r<.v1;\riZI5\x0cs', 'QXdUcf'), [8])
    def test_case_1736(self):
        self.assertEqual(pattern_match('4c.n/^h\t\x0b|tK3D\r$[*Y|MA%A/%9\x0b\'\n\n<#kL\rvs"Yc2}GS%3jT`', '\n<#k'), [30])
    def test_case_1737(self):
        self.assertEqual(pattern_match('(gD58\x0b)uvzW[*njusP0SNY/r!;q/Q"X*KCOg\t[8[Rz;PD!d{"\r":\'LGUpf6~N@u\x08b!a}1^H', 'Upf'), [55])
    def test_case_1738(self):
        self.assertEqual(pattern_match('|Oa_nTRvY [{[U\x0c0gzj`dC{+~T"zBB3+Sg0_g@@V.L*rj@:$(S', '"zBB3+'), [26])
    def test_case_1739(self):
        self.assertEqual(pattern_match('!9gP5pNRXnWrpm<OhI!|EK$o8rvz[qj!j*r|G=i,Qq<QsZUf^!bH%', 'pm<OhI'), [12])
    def test_case_1740(self):
        self.assertEqual(pattern_match('zo\'"E5xlR2<[`D8V\\!TL\x08wwgbi4k``":xe[[{L,bXlS~%&!s|0im]Bb6 Mj\\OZi\tJ0Id\'Fhb3|wrzK3!,>\x0cTtneI#Jb?e5}x', '`":xe'), [29])
    def test_case_1741(self):
        self.assertEqual(pattern_match('#`1Q\\Ifa\r#eDYleZ\\\\h\\Xs7^)E\x0c+f1E]Y\t>"pC]*?Z^p<PMEU0O_\'D]|Ek"h/M>$xDL}+5Tqi[0u&p', '|Ek"h'), [55])
    def test_case_1742(self):
        self.assertEqual(pattern_match("ZH\x0c/0a\\`O8q/>P}7a.[\nQEn=sdKN!?:(e.J!%w4,%si9\n!qh/\t<4\rAG\nf ERIb&E|Wi^* Gs8DWM'[Sf@^DG\x08vl%}n", '<4\rAG\n'), [50])
    def test_case_1743(self):
        self.assertEqual(pattern_match('(ESu`dYhFc\x0b:;a]uwIZ;D\x0bpdMot0N+x\x0b21{K?dy [<u?T^"//a&$i\t]\\/c}Gx>l,tWA\tnr`XPq[ \x08', 'x\x0b21{K'), [30])
    def test_case_1744(self):
        self.assertEqual(pattern_match("dH|n$$oWU>+w\nJsxP\\d_CtNI=a3R9c4X=y\rZ<iBI:^HT#@mY-Ow,C\x0c<+jAzy,/97EpFz'PP0Pqu", '=a3R'), [24])
    def test_case_1745(self):
        self.assertEqual(pattern_match('0z!kly%r<@tci&[>,rhckL7\nQuQR*\n8- z\\~d{y;^KJa;(aU(Z/>Ol2w}ucY6a5\x0bXF_11iZBOS:8i$xYkme(r\rfX~S', '\n8-'), [29])
    def test_case_1746(self):
        self.assertEqual(pattern_match("RTuASZLh/s_\r]Kn\rZD$)PWg,{H^>KV1t2cnFUZ;'S?bpw$j!qaRZ#?P#fJo^EDDLv [I*^y!QTR]\x08O\nMX@w[(DpO\rm1amav&6skI", 'D$)'), [17])
    def test_case_1747(self):
        self.assertEqual(pattern_match("nGOKt\rwb;8>$3Yau\t02SYm<[']yTb0sm(dB\\EZT0$>e(QIH<RwZ>5/N`:o\x08aIJ:BF^JRK1F@:\n\x0cdoM)c", '$3Y'), [11])
    def test_case_1748(self):
        self.assertEqual(pattern_match('\x08Lo\x0bqb%t\tN@^H\t T$%a E2\tCK3f@k\\V%\rM\r2w\r[6!HHABe*oZgfJcg}IcC>Y%/{Yw$q\nHf4_v\tc6dnLC#YyBx#g\\c{oF/l\x0b', '\\V%\rM'), [29])
    def test_case_1749(self):
        self.assertEqual(pattern_match("&/)Myd[3\x0cW10%brmN,*\x0b\\Ah_!y_0k%-H!']\x0bSd)%e<e\x0ceV:~ftV l9Ff)}gjFgJ|[{QvWVBg}guO W2 #YHHN+", 'd)%e<e'), [37])
    def test_case_1750(self):
        self.assertEqual(pattern_match('jF{G&T`\x08B>Q\n~56Bwr0ax^~ORFg\rIF>EnREfI.0^$$~~M~&l7v\x0bm6u8!7b#12YZc ,\x085m3U>bB-2iSPpf"b}>|sei', '5m3U'), [67])
    def test_case_1751(self):
        self.assertEqual(pattern_match('/gBR9`yNo|Gc3v;`yB%5Q$\\\x0bLN[i)LI(2\\*R7*Ld,n9COh\n 4O\nU$jsJq?YK', '/gB'), [0])
    def test_case_1752(self):
        self.assertEqual(pattern_match('&u9{pS$\x0bPK)]:0\tHqzSmA`POrwdVh^W`Pj! \nTZG<ACb\nH(0R.yeO.*8\t.3,2h\ro<)\r=j*{vPmsENBQ\x0b7SNF6Fq?A[5NdO;kmC\x0c', 'H(0'), [45])
    def test_case_1753(self):
        self.assertEqual(pattern_match('jaAMW{\nB[XMr0c;]P3t5hVvA\n4%g;\rtqo ,Ih%``vlM_(sZ!egz!.q9;ZTC\\AEc=H`jE@{)ap+u`0}#iG\\>\nL\nRH|f.:[7y%Op', '%``'), [37])
    def test_case_1754(self):
        self.assertEqual(pattern_match('pE\x08}\x0b]&UwW=BU,_[\th}%\t]0|l\n]5ln>YfS{g [Q}A"dPog+of.@sUMxJ `-202N<#Brh/Z', '+of.@s'), [46])
    def test_case_1755(self):
        self.assertEqual(pattern_match("-x+tO\rU^l1s#nU1\t1K6utx8+i\tYhl]^e'DszYFqH2r!?\r`$SsC/(vwpl^Z_", 'wpl^'), [53])
    def test_case_1756(self):
        self.assertEqual(pattern_match('* W+TZzd+=/mks\x08Pfdd>\tiiu5tC~)#89P3+\nmd`0<n:\\5&1lt~si1[t', '89P3'), [30])
    def test_case_1757(self):
        self.assertEqual(pattern_match('N]\r\x0bNaF*~\\p>\t>\\x"5Uo\r&>W"KH!\'uu /?\'~?KAo<_\rlb*n+tTWB', "!'uu"), [27])
    def test_case_1758(self):
        self.assertEqual(pattern_match('B\x08H"+,d2q\x0b g>wLx{\x0b5>Te4-m==G=,!/c"8 c~a\x0b,\x0b[|0Kb\tCT-&\ndY=6MU"lz+u,G\r#h`hE3Ls\rnA', '#h`h'), [67])
    def test_case_1759(self):
        self.assertEqual(pattern_match('\x08be&Bv^U4)k(TKot5p\nP}z[EP.}@>1!v)N@F_\n..0"rGF^$_+Sk\'K}I-8', 'F_\n'), [35])
    def test_case_1760(self):
        self.assertEqual(pattern_match('B\x0c\x0c#UtAYm\n_c`L /\x0ce wi^g2K:fJ*RHrS [gxMV!\x0bY3;_sgqIqEl^n+K(Y`H#MHM_9`1?q-dBWy;', 'IqE'), [48])
    def test_case_1761(self):
        self.assertEqual(pattern_match('-IUYmyG9@))9k]H\rJI+~B|d`TPvacs\n)28pk,_\rjI/\tUTM-28,\t;n!mVZ<j1Y@1rFvX', ')9k]H'), [10])
    def test_case_1762(self):
        self.assertEqual(pattern_match('g?Q!c(Ic$8_7V-+<Y\x0bD+\x0cjlK2_lXt\n2ogllmf<w!MsW~;0CAGiVLGQ=hcs9_,P2_}', 't\n2og'), [28])
    def test_case_1763(self):
        self.assertEqual(pattern_match(']}rjZ)+yrDh+X\x08!ra)x?d%A=^Ufp<R68qO#"EM\\7j0a\x0c\r|=>$\x08Eky+P|u}77{`!#y93XD.0[d', '+X\x08!r'), [11])
    def test_case_1764(self):
        self.assertEqual(pattern_match('yk]LZMC`edFvsm%s%<r|%:6+Lp"(Pa2ynyF)b+3&-#4\r\rk/=/dk"+?^7+83m\rF;"gv-<{l Z&-e.Y&', '"(P'), [26])
    def test_case_1765(self):
        self.assertEqual(pattern_match("CX mt\rC7wB~/\\N>5m%d_c%i}t5'VI00LKUtG+9i4\x0b]h'{+FJARJ)", 'N>5'), [13])
    def test_case_1766(self):
        self.assertEqual(pattern_match('<:]~%*1K }\rZLlGxPTipY9q#:]KH@).$:D{{5Y!ZzikJQw,P\x0b_&%n/A%G,w[d=z{0Q\nauZB<g"<Yd8=', 'g"<Y'), [72])
    def test_case_1767(self):
        self.assertEqual(pattern_match('^"eX$YW-/MwTZN@-@,?>}AJ>W3&-Y@7M`Jc_12Ybj=~u5h%QtQzNp', 'Jc_12Y'), [33])
    def test_case_1768(self):
        self.assertEqual(pattern_match('T@o0X%~i8cF*]\t>?`^_(Q{Hv~D!Sy&E)]bx..Mjy~a|\x086OcEk,@}^', 'T@o0X%'), [0])
    def test_case_1769(self):
        self.assertEqual(pattern_match('#NYh;%7bOq[\\99ZA<MAiS7)pw.SnW Tu\x08/FpFpwOr\nA=Kw%IdID*OT*lR`pi0955<i', ' Tu'), [29])
    def test_case_1770(self):
        self.assertEqual(pattern_match("{'\x08$f(g\t\x0cVVd}#;\x0b8A:\x08Ka@sM3wvZ\x0cq7x~$TX;1%>\nWD7aas}XX.>Dh4EtubW;\x0b?q\x08Cqq^#xpS8\nv=\x0bFdV4f` ", 'aas}X'), [45])
    def test_case_1771(self):
        self.assertEqual(pattern_match('Iv@T94\x0b(/ab CNN\t}r3n9E>?izDr\n/Y[Z~BB[CP[\'3TW!bt\n"bdyV#ui^x#.H"jMa+Fj*8}]\rH[-\n9I;t\x0cevdhla(\\', '}r3n9'), [16])
    def test_case_1772(self):
        self.assertEqual(pattern_match('&7b~vJ6wiC"x`o5oi<Gh2|f17]ff1M_"-I7| y^Z0SAE}Oiqbs<OW_1%x\x08\x0bX&#Q0\x0cdmWeYw}sci:z}W[`~&)` r', '| y^Z0'), [35])
    def test_case_1773(self):
        self.assertEqual(pattern_match('xv\t~)8\t5T2[dRa9A5\t5-?wV)}pimYovdc4:Kb6Yk[B\rZ`dm!F)9lx\x0cK=nxr-sj2t\\IBS\x08M2k@^C\x08oena6(#!l!^', '!F)9'), [47])
    def test_case_1774(self):
        self.assertEqual(pattern_match('Jv8\x08\nmcsJho[f;c-/yNc4FJ\tWa>U.|Z46\\{w%hxJ_fceu~<x\t]4v!PxvA>_8PD>kvmUwV+5xY]V6A(&b%|i4"6O/nUYYD9\\{~', '<x\t]4v'), [46])
    def test_case_1775(self):
        self.assertEqual(pattern_match("Ei*`N#-^b!\x08R#)ZTxm8mR<\nE{]E-eVH4evSL&|d\x0b;'+\r+a=tAdt!d;iL=kKZ36\t=TikLGTx7Y$|F%,6=+vU\neO-l_J4T'", ',6=+v'), [77])
    def test_case_1776(self):
        self.assertEqual(pattern_match('CAHlTpCa1U=/#\rh*Yq\t+L$Z04Cu4+LjS_:YO,%((j9l\rM\x0bTuX{l-|Ttko+{|6d', '%(('), [37])
    def test_case_1777(self):
        self.assertEqual(pattern_match('1_/ bDtdQ4FN+$j))xBF1k(u\tuU;q7n3a45PF\n|"@Y/m>uWk)2CTu27,;%C+*\x0b:Ru=<4\t3viVw5I6o5NA~Fw/gI', '27,'), [53])
    def test_case_1778(self):
        self.assertEqual(pattern_match('HU\\WQ\r"W1DTB2dU%\x0b1{!FsK=,W&HW}D_+y\x0b9EG>NuSp]=zuY?K/rb\x08^KI[_}wfE8xj\\OZlyf\x0bMg!(%Z2jyNP[y>j_', 'jyNP[y'), [80])
    def test_case_1779(self):
        self.assertEqual(pattern_match("Ev!&8h2U:<e!\ty)k\x0bo-k64N'*t>y9ISyOPLla\x08fp|T.j+8o*xN", 'PLl'), [33])
    def test_case_1780(self):
        self.assertEqual(pattern_match('qz>&\n\\r9a\x0b~.-Vd)2%g(odX";?f?Clo$C\x0c]w(zs^4\\]ZF2E>|7F<sb#|H27L11_\x0c\ttp4a;rgD6', '~.-Vd'), [10])
    def test_case_1781(self):
        self.assertEqual(pattern_match('V2f8<U\x08w]& "f= n\x0c.7/"\\2fu\tc*\\\tX~*,MS\\.\'0i*X<m@,]Lb', '*X<'), [41])
    def test_case_1782(self):
        self.assertEqual(pattern_match('~<u1-1EPeprjrFlj55]`7o?o6a}9>5H{h[J"|5Si[\x0cd5XQo-.v:_Bygi\x0c*l{Lf2\tNM^yb)BZ2lA\rBF[-0.fqAu>Y]', '5H{h['), [29])
    def test_case_1783(self):
        self.assertEqual(pattern_match('>23/P*kEr+h/ DKAkYE\'6B{(!"X\\{d=5o;\tBh7\rkGc.\x0cy7W7$Zf|*i\x0bsF1h\n\rQ\x0c\x0cZ\t,u*`6`pSKGl08', 'y7W'), [44])
    def test_case_1784(self):
        self.assertEqual(pattern_match("'\\CNO9SgtDp7'NJn_\x0ck<Ec<\x0b24g.W\nnNNpeK3`})m*'VsCSeweRaZr#)26S 9T/8dIf\r&^v0k&;jNac2Vsb\x0b", '4g.W\nn'), [25])
    def test_case_1785(self):
        self.assertEqual(pattern_match('^9DK[\nVOf4zC2?\tvH)D{Z+8%r_LWZI*K/2\x0bm$A\npx=646S4e6?ZkKa)!aEpV]NmhI16', 'r_L'), [24])
    def test_case_1786(self):
        self.assertEqual(pattern_match('Kh]B.^<O\n+Vv6d7ULz\rE+AD>5*j\r3u2sCEyV7o>MIpAadZWk\t"?bw]]k[o/cwj[LW<L;De"7\x0c[ENo\rJ', '/cw'), [58])
    def test_case_1787(self):
        self.assertEqual(pattern_match("BC\\E|U\x0bI#6m<&XxpWJxUA%LEp9oor7M?Hw:Cypt~93l\x0b\nCl2wk,o\r)AUBAvs'.og", 'xpW'), [14])
    def test_case_1788(self):
        self.assertEqual(pattern_match('IIo\t T9(Y%K"\x0c@iP8%rBK-y:6CFAF)h/+D\t\\L/9+y\t11&G=\\Iz1*q|5r"A81uk( `k/~b\'2BYQP{{\x08dJ^O/#u', '+D\t\\L'), [32])
    def test_case_1789(self):
        self.assertEqual(pattern_match('6C%[\x0cjN[)tJ_mMA\x0c%qp75%c;XYxh b2]i(k?~*u5]\tv56Jwxp(\x08s3Em37$p]*Bk\n4\tkb{Gcdb\x0b', '[\x0cjN['), [3])
    def test_case_1790(self):
        self.assertEqual(pattern_match('M42_JDl{V_&\x0cctf14,Ti\r^LW/wK(f7mV%h#^j#l]V:\rZ{:;q8q)/FhAQ\rgy', 'V%h#^'), [31])
    def test_case_1791(self):
        self.assertEqual(pattern_match('CV=lm~=EMi\x0cHlib_Q)ST-c#.3W@:jA/ft2dy];f`3M5\rNxK&r8 0P\x08sy?p#-5x@`o1}C\x0b>i/qR/(', 'y];'), [35])
    def test_case_1792(self):
        self.assertEqual(pattern_match('^2/;\x0c*Vw#\r\rv\x08f%Xo>XAQCM6}CQyBqo<5y"&0o~hD]li),\x0b?\n7\x0cMh', ';\x0c*V'), [3])
    def test_case_1793(self):
        self.assertEqual(pattern_match("<-:\x0bA1tcjH+Bbi0SCD.CXm;w;C=\x0cPJO#a[&M\r&\r4\x0bb~kTY-Cv`CJ-'/]8*^Aa\r_`\x0b/XN`?qqs", ';w;C=\x0c'), [22])
    def test_case_1794(self):
        self.assertEqual(pattern_match("dI'L<P^.J.Q NBov`l7\\|va5YvVA}9*?7t?\x0b{O5gzJ=7?;6P0D&J#2(5rl&.c;a\x0bNY'WiR\n~{j", 'NBov`'), [12])
    def test_case_1795(self):
        self.assertEqual(pattern_match('<PBx?;M]`5nY\tp;Y\tfN?>gV\x08Y=8rj!p<ia<D`9FOv,wQ!qz$qr1FtK%\x08wi\\OPj29Afn)9H\n7Yy~rC;d5}t{lKBW&.F6;<8xK', '{lKBW'), [82])
    def test_case_1796(self):
        self.assertEqual(pattern_match('75->\tow+(\r(\\gdGgk)xH@)d8e1_s_{~3C/-bPz;KQ`F\\Wa!HTr+n\x08+(}$*($k6c%d\rf4R3P vFTP-kMo<LmW l%#Paa\x0c', 'o<Lm'), [79])
    def test_case_1797(self):
        self.assertEqual(pattern_match('q!B~C\x081*mQ!2B_&\t>T-JS_v$==HDXB~w[^CMxA\t=vPdZ64=KjJaiX1e;dB~G4', '&\t>'), [14])
    def test_case_1798(self):
        self.assertEqual(pattern_match('B11j[w";1-\tKw,l:dHn-fz0Aot<e\rDX{\x0bm$-|Sj|Z\x0c--;Ene\\/}4xCN\x08p~J6:+/o{n"i\x08xz4q@5w`M79VNA5t32:\'@^9[\\Y]2', 'Z\x0c--;'), [40])
    def test_case_1799(self):
        self.assertEqual(pattern_match("RF8-\rd;jR$gK$r\x08~1${XI~>{&@*S?\n\x0b\x08Y!YAe^~&l`\x0bnX1'D\tD'c$[1_n+(z:#>r& =8fkl+))bz,_u?t", '8fkl'), [67])
    def test_case_1800(self):
        self.assertEqual(pattern_match('lh#"9W,X:&r#uv=R2$^,\r,\t7AM<&N("u3Yd0s|@&_;B4n^?\x0bJ%zx9\\2Uy\x08\x0c|m"_/e3\tsq%sW3rx', '("u3'), [29])
    def test_case_1801(self):
        self.assertEqual(pattern_match('w\'gYY;">S>U(PH>l\r*W(S<L{J\txLn{x9/1jV_s:IaD1o[bsB|}3sGCUHJU]B2r\x0c\\3g~f\r+:-H%(wlcV2m', 'jV_'), [34])
    def test_case_1802(self):
        self.assertEqual(pattern_match('T`_~EHD\'DJ+vv1gSN;%OHar?pa{P5-oM9&;9\\B9k@SRTvc3\nig"wZ0Lju7Z=n(aW1QOg{v=j\n]+|$_~/-\'*4', 'Z=n(a'), [58])
    def test_case_1803(self):
        self.assertEqual(pattern_match('T H{Vg{"JJDoaKr~^y"LG4|c7!29-1i,WQcZ1Z:i\x08O):yHj6EJgrINV^K8cR', 'JDoa'), [9])
    def test_case_1804(self):
        self.assertEqual(pattern_match("73z}el#Tj/Fd\x0c*.sMz=b4ZT*O[rBUJ$\x08}NZt\x08\x0b\t\x08K<pQ\x0cL['wj=>noIGYU9[\r3", '/Fd\x0c*.'), [9])
    def test_case_1805(self):
        self.assertEqual(pattern_match('h_uMQBKKQp^4Job75-8SnYXF3/d2El6it 6/w~<D#D3)G{TFQD]$8JO3B\\Qkw4l[u', '/d2E'), [25])
    def test_case_1806(self):
        self.assertEqual(pattern_match('/z>6f A\\1[[41~]X.+IdBgt#9"/Tdx}WH-d \'{6yQ2{wqo@L\'YD9/e_$0|6H[?> >ZPn}LO2GZ~,1Ux5? X*!5Lh;y82\x08Ygw', 'dBgt'), [19])
    def test_case_1807(self):
        self.assertEqual(pattern_match(':n|\x08"rT*n\'\x0bw7{;lmb34x5A:>hhp\nH\x0cj1SZCtkqtd>\x0c?b3PR1e!s4.=c.\x081Z_bDg\x0bZb#', 'hp\nH\x0cj'), [26])
    def test_case_1808(self):
        self.assertEqual(pattern_match("5wPxuq\nf]ebS 2:'Too1M\x08/;> A)u\t:[2p{c\\S=S#<dAI\n>j1c9Hi\x08Tep/", ':[2'), [30])
    def test_case_1809(self):
        self.assertEqual(pattern_match('{R-|[sQ4\x0b<d3XMZ]!39I$\x0b\\\x08)^7Ox\x0cv+y\x0b5*C"bZXLEf3F!VS\r3\\,}5y2QC;\n<&2+nyv\nuJPJ,&n1rQ0', '\x08)^'), [23])
    def test_case_1810(self):
        self.assertEqual(pattern_match('b<e>mC#s>*Hy%(ro.hH/zu(Un\r\n*twSO`&(EhK9z]nGydB\t|-|Xu^T aPiyK3^_d,Zt$bUC,F$[QV,!$j', 'bUC,F$'), [68])
    def test_case_1811(self):
        self.assertEqual(pattern_match('2fWem0[qwZOq#\x0c`7eR9B"&k. U:d WR+v >\'lv|0OP\'9d yH9CqF<3\td;)/\t,%e6QQJh)/Ig5[?Eqh2`!Z&WXgym=}?n\x0b556of', '=}?n'), [88])
    def test_case_1812(self):
        self.assertEqual(pattern_match('L"h]m2.(s0F]|f\'6Oqb>kr.|*Xk#\t{^\x0bpQ\x0buW1=y\\n/\\#mLy>PSby4Oc_)\tp<J%G+<[AUszV2bI+fvScqf', "f'6Oq"), [13])
    def test_case_1813(self):
        self.assertEqual(pattern_match('\n?K\nIzO1Bc^(8hX;8\x0c3 8cLPpD#K@7msK/{s8,Q=>u\n!Zxpjc98&V+}":BjlW,:Jb[^0~J\x0b>"Cl^%Lh\x0b(liZq-kpmh~\n|', '~J\x0b>"C'), [68])
    def test_case_1814(self):
        self.assertEqual(pattern_match('!JsD}\nGr=~Lal",>Xi}),~4R9s\'WpO09C_5>A[\x08\\5\x0c/r)T\\kA>', '\x0c/r'), [41])
    def test_case_1815(self):
        self.assertEqual(pattern_match("{X.'(&xP*L%BJYr B|$\x08jg[!n6Zw`\x08zN`>4,-D]13Zl;j'E-I@LYp-/W:Gj>?[;scKs[>", '@LYp-'), [49])
    def test_case_1816(self):
        self.assertEqual(pattern_match("Rb()659nI](hV8}P3v[KX0=}\nF2\n('T<yFpw2` X~=Nij@\rq]{xg\x0bY(", 'v[K'), [17])
    def test_case_1817(self):
        self.assertEqual(pattern_match('p h*@xAuxBR\\YBwT\rgMTX;V_wS>DI(HJ-Z+$=Ob\x08m9U?=#>y*\rjd@<}W@\n\rc; H5DZ|zFNZF}_mjJ', 'MTX;'), [18])
    def test_case_1818(self):
        self.assertEqual(pattern_match("!U.K{'\r=InM?Ah<j5f\tcTBk_,vpg|<i7a]~wM\rPM8;T\x0c@ln$fhJN)$m_\rm7#\\w]Gq\\;dqb\t+gBb3\r5V/G0F.+L;k", '$fhJ'), [47])
    def test_case_1819(self):
        self.assertEqual(pattern_match('\'1k>l\tQdz|BrcIk<x5\rH_tk|&WUl-H"\\qNnx:A~/~OEEGEF-\rjQ', '\rH_'), [18])
    def test_case_1820(self):
        self.assertEqual(pattern_match('r0}t\n YQju^W}j\x0cs|Rvr<kGxy|_b^\\4f\r)qH%\x0bxmXGL\tr\x08Dmv`.\rIo2\rOC#K/+!=!\rOdE.DVg\nGwRjn-Y*7&wOy=K~yu5vi\n', 'GL\tr'), [41])
    def test_case_1821(self):
        self.assertEqual(pattern_match("\\H;+I\tkfI\rf6[WbWV0i3.1'\\/*Y%;uz~tb/r68d@58NGDv5M\\f\rQh8QWj!{", '+I\tk'), [3])
    def test_case_1822(self):
        self.assertEqual(pattern_match('!\x0bWY?Xgkhm%6qT]{L\t\x0b.9L8`B~U(eAc]!I\r co4G\rbm$/[XY@o3Q', '/[X'), [44])
    def test_case_1823(self):
        self.assertEqual(pattern_match('bRS+y:2Z/es*`1\x0bB.\x08"^yHae#\x0b\x0bm/7<8sC 072KrP;Y1Yqqz`sMWp!2Bllh', '2KrP;Y'), [37])
    def test_case_1824(self):
        self.assertEqual(pattern_match('% P\x08|2r\x0bxXs3G $uZ].M]uZ46\t7}eX$\r"Y[h!ujJm|-|\x08A\n\'3Vx)UtM5ABT\rc', 'uZ46\t7'), [21])
    def test_case_1825(self):
        self.assertEqual(pattern_match('$_*vez5lc^\tEwz\x0bDC=B\\X?\\HNj|XE&NhK{?2M3/\r#8l!CM5SJ#hVB."yyce\\vi!.xH6|', 'i!.xH6'), [61])
    def test_case_1826(self):
        self.assertEqual(pattern_match('rs;\\iG"D^Jb$u~ya74{Pwh%/,kRMd<oU>Ii\'<^xDlNCL04x=t\\~Cte8P##!_oCF~$\'2f\'&\\3u"7;NCV \x08PsL{.PRBvv#>\x0cI', '#!_oCF'), [57])
    def test_case_1827(self):
        self.assertEqual(pattern_match('R \nfItVq>a.C\\J[Q-Y7Z|J8L%55->C0/VJkv+Zw?|54$?4@B?8i!~l!U)~\n\x0b^0KI_!h\npbsEB!Z#\x0b+kEN["{N`|\\]hL=', '8L%55-'), [22])
    def test_case_1828(self):
        self.assertEqual(pattern_match('1`dPi~k~$\x08;u<Q9n]@0@s4EY%4FAa\n\r?k?~$r\x0c&@`N^Z{*8\x0cz)5>R"\r!,n.S>N`O*\r^C$9vmSjiyEdQaq-FqJ]a+R2.O/Kt.\r/.', 'SjiyEd'), [72])
    def test_case_1829(self):
        self.assertEqual(pattern_match('GX\rn[Y$`(\x08]m\x08A:IPyC6BN4v_c(G.\x0b`9XR7v1{-OG._tPeABkfN^py_437GR~qmxw<u\'"', 'm\x08A:I'), [11])
    def test_case_1830(self):
        self.assertEqual(pattern_match('~yMF8x5neuSZha\'rs`Q`C{[|J\'(\x0c|-[/\x0bvw}1snQ\x0bd9j%IFf{Am{M$!y@&c#M"`sy^r(', 'F8x5n'), [3])
    def test_case_1831(self):
        self.assertEqual(pattern_match('@2Wc@7+CvP^36bpg\tD`i6-*Ghi1a6\x08jIg#w`mxy\x08KF\x0c6\r\r\\`{Vx6&Q~2Dv*z&MnP }Hf', 'g#w`mx'), [32])
    def test_case_1832(self):
        self.assertEqual(pattern_match('*?gG*5T@>r}5FtE"sfA0Sk~c%WS\rEpsm]f\'6tU5l3tp\x0b\x0b?n+z^O^1o0_ULoL\x08zu#*nX1?0Y,', '@>r}5'), [7])
    def test_case_1833(self):
        self.assertEqual(pattern_match('q7\nBx"fYg<Ws(ureI:7U{8S\x0cu1_d5tr887vGn\\r^VP\x0chcS\n\x0cSl?wi;_~zHgMsI\nL3n1A38Pnt[8w!NJ{7u"6;I:$\'|Bf', 'MsI'), [59])
    def test_case_1834(self):
        self.assertEqual(pattern_match("Y&'}U`[& LAHcjwa=8Cr\rW&o?:U|{PC\r\x08\x0cEn'7&ED>Fv%\x0c^IdD!SMa\x0b,91kY?UqqUm@@%T[cg4JF_P `IC?e)\tkgW<Mc=\rh4", 'e)\t'), [83])
    def test_case_1835(self):
        self.assertEqual(pattern_match('a(O6A]kr?p]dE<^&LBy9H&[\r\tJ\\;Yg\n)OR.u.6WCp8Sd!h\n5\nG+%s\x08i[[#1;}R,7a}c=?\x0bxXPGyl<\x08O+Z.wq\x0cTB{lGz<ypc{Ym', '+%s\x08i['), [50])
    def test_case_1836(self):
        self.assertEqual(pattern_match('-_G O\'c]!|<^=Eo2P]EF%NW8@e 4r|IxuU(-4/7&q3\n)UY<\x08~!mBS7g!".<Iv"', ']EF%N'), [17])
    def test_case_1837(self):
        self.assertEqual(pattern_match('Q\tTMfO5&~Wr$Xp7So?R"Owg^[<"t7P~0lz?s&(bM,#u8\x0c5$tD(}l\x0c=k', '^[<"t7'), [23])
    def test_case_1838(self):
        self.assertEqual(pattern_match('|\\/z~{t\r((F\\9Z0l&gCoZ|jJ{X\x0b\rC\x08}vBLg9v?|;S|F\x0btnB~2BM\x0c~CqsI', '\\9Z0'), [11])
    def test_case_1839(self):
        self.assertEqual(pattern_match('\nnQq`vY[Gs/><(nA`0r\r\\0k?pOKO#,I\x0cEQ$/6MZ.+W{J`wc^b/!F[5_', '><(nA'), [11])
    def test_case_1840(self):
        self.assertEqual(pattern_match('pU_Jz[l.>Z-+Gu6u\\\x08}wZ]<hC/x0S0*xu1GgP>Oxvq}{VG9ZU%\x0b`J^zY_x,zP\n\x08`\\jPF,.Wjt`RXb7g 4S\x0bZ', 'pU_Jz'), [0])
    def test_case_1841(self):
        self.assertEqual(pattern_match("\x0cc'kQ`6.,%\rBx\\,G[\t5EpiF?nd:ck.\x08_$\x0cQ9;/hS\x0b&pc\\6&L~abYbg~o\\_NTv&c", 'pc\\'), [42])
    def test_case_1842(self):
        self.assertEqual(pattern_match('P7>W;|BQm8\n6g<q$Hy]"{ xMyK!g,NKR 6"\t$5@ho\nOO\x0bdw"b{z0%VkL+Sn9V\ruMwkf}', '$Hy'), [15])
    def test_case_1843(self):
        self.assertEqual(pattern_match("&WG2.1?)7\tzcJ?D-K>;]1qQDcJ6]UUx2}$kO;\x08vT@\x0c7'g4/miB\x08vZKSbffL[NoZuu.Fsa9QV\n:\x0bS/hsCimMnftn+Y;7B.3|6Ze@'", '/hsC'), [76])
    def test_case_1844(self):
        self.assertEqual(pattern_match("{#3WHJqZ''cm0XT{V\x08Z -y1}w2lC*zIJ|3:%ph$j,jjbGm<].KJ W{^(K`+2", '3:%ph$'), [33])
    def test_case_1845(self):
        self.assertEqual(pattern_match('\x0crJ7ub?o.yk39UCJgj=3 \'V=B5"iKfCR^6br\'j)%W);In}H=7@6iAW3f57Q\x0cW?*^7{cLrjH+_\x0cXO[', 'KfC'), [28])
    def test_case_1846(self):
        self.assertEqual(pattern_match("uGXNe:Cs+q@x\x08f3PJ[\r.yI}`]so/qtHPv`Lz4%'E8Nq>-P]I)WVimm_q%", 'x\x08f'), [11])
    def test_case_1847(self):
        self.assertEqual(pattern_match("qSTuKf36$O]rh1\x0cUKQ\tas2O]\x0c\\b#|0mD;IWH%ka\x0bP+u?t<rU&}'CW,BWkh LT", '%ka'), [36])
    def test_case_1848(self):
        self.assertEqual(pattern_match('-HNdZ6;U*\nn\x08N\x08yq\nr~GOFBfP>YW-0gaNtqU\n:<_ihzGf \x0c&V,`/\x08 :[ =\x0c70|<f/}*g:tY', '/\x08 :'), [51])
    def test_case_1849(self):
        self.assertEqual(pattern_match('\rQ~^Td\\*X=owT!!ru.nO_gz5/n\rjS[%ysc#tH1zr3{M*Y^dZ4VG4:b!=\x0c.*eU3.dF\x0c#\\=R{%C ', 'z5/n'), [22])
    def test_case_1850(self):
        self.assertEqual(pattern_match('g[/ZXr\nuu01OK^BOzq=Ve]YQPNzxxqtH~)<!Jt;lmM?? \\H)[\tl;fr"f&lWA~JkR/Z=t@*a\rV1A38_7#(f0p<89f["ke5', 'a\rV1'), [70])
    def test_case_1851(self):
        self.assertEqual(pattern_match('w](X)_G9\x0c;`s29V65,dN_je,3\x08U>c; %yt)0!k5\t>o/T|}G|&?ult9fvZqhh2F^YzM!%V\\(29)h]?De1We0qs0cX\x08Vgp', 'yt)0'), [32])
    def test_case_1852(self):
        self.assertEqual(pattern_match('BsVfRNfnI-Dc`B\r"<bm0gC$ys|+/vfa3 "]>*3VMo5KobB@,-S~rYaw+G-/gm\'LLR]\x0bJ~sZqSiO2j,TyCVxXHJgHWW9&', 'JgHWW9'), [85])
    def test_case_1853(self):
        self.assertEqual(pattern_match("-r5b.B$_~[%w:}\x0c\nJ V)O[;UW?}'rS{<\x0c*S15DlQTIq'OxWH36", "}'rS{"), [26])
    def test_case_1854(self):
        self.assertEqual(pattern_match('[x)Ovj-A.\nDKFg<\\Q+ }"#=,RSUp7q1B&-`"#!>%M,W`SW+\x0cF~W5@@w@f#_xEv', 'w@f#'), [54])
    def test_case_1855(self):
        self.assertEqual(pattern_match('X5%\t_ad]r\x0b\n>th(w;,{g2i"i3}}G^$p -S{ouHcj*Dj\np\ng\nm:[9ri_}kWN\no?H$dbWR9|/\thtQ\r]bd', '$p -S{'), [29])
    def test_case_1856(self):
        self.assertEqual(pattern_match('+"J/~H~EC.Gj/]c-uV~\x08<iW~gPP7"!k/j];"3&gx$,s~tTxtrR)"3Wo+;TwZ\\)3T$\\a\r1\x08]4\';\x08b%+c7M7{t]Xpz"#U04)s[fE\x0c:', 'rR)"3'), [48])
    def test_case_1857(self):
        self.assertEqual(pattern_match('7D_tZ6X0*5pi\t1[e^)\reH\t\\BcUdRHQ%fa?,[,^z%a_3h#"4CQ?D2w?n`rZW[fbGM$H<p U\rvA\'\x08Kt\x0cqRQ/2NM6v\t;k', 'Z6X0*5'), [4])
    def test_case_1858(self):
        self.assertEqual(pattern_match("7tCfg)*[^41vl6CB[n\x0b%NH|p;6!~VRI\n=$Laz4EOHN\n\\oYg.y|\x0cuVw8',mB`;KqzDR=Qaw?[)WAOi|\x0c'k{CTZkA5k7", 'ZkA5k'), [84])
    def test_case_1859(self):
        self.assertEqual(pattern_match("\rZJ=w;2FrxVfF^gM,90n4})?MK'_xnVke~Eh&E47\x0coh8iD|$R\\} 7.ZI_sJ9sml~Hg`4.!CbqwV/", 'ZI_s'), [54])
    def test_case_1860(self):
        self.assertEqual(pattern_match('b4{S2Z},!y;_I31\tG\\BXf\x085k[P\ngk4Z>wj{V3h[m{LL<%\\afsyw3`A@z', '5k[P\n'), [22])
    def test_case_1861(self):
        self.assertEqual(pattern_match('FP$9`&\r^4\tgb%#129D$UP:LTWvq\nQ\x08w\'"8-f5\'wI\t}6j\x0cL?rS>n=Lw%\x08=\x0b%\\hXW\x0c(!e&', '129D$'), [14])
    def test_case_1862(self):
        self.assertEqual(pattern_match('\x083;{l `"?{xrU\x08\x0cu@^9E|HnA<S6)IJ^\rhmu\'%\\\'\x0b\'D"Vn\x08*+6e5ti~b\'X2xuGNQ`:7;G gSuDj\x0bfd3o&nzrn!aS^]]asJ?n)', '@^9E|H'), [16])
    def test_case_1863(self):
        self.assertEqual(pattern_match("7AE=1f]S+A]u}s,tzHx>Nn4  GEn&8V P*0\r\x0ba?}1ntU=NtP'L.ADiQM'", 'n4  G'), [21])
    def test_case_1864(self):
        self.assertEqual(pattern_match('%XBOd%UnT6Pf:v9G`MuK#r8G@Fno1C&3`p3X|xFXxa.6\x0ct]E!\t/l2+vt6X0\rNVf@FA UjW51TS$Q<A*', 'xFX'), [37])
    def test_case_1865(self):
        self.assertEqual(pattern_match('f2(z]\nIXlI_SBDOd kP\nKyR 7#hS$]IsiS`DHqR\x0b%7Vv?fk0[PqRy9r1_', 'v?fk0['), [43])
    def test_case_1866(self):
        self.assertEqual(pattern_match('wVW\r*[&ZWg@\x08)0vE#0[_2RD\tT$dr:\x0c\tjYkX5Ls~pj)>Aqd!i\rs@/Q]K1xjVjXQS"=(Re\r*Oud8EZ\x0cbk:Sf%`_dFMVh#b\x0c\'', '0[_2RD'), [17])
    def test_case_1867(self):
        self.assertEqual(pattern_match('z^~\t\x0bEME\r<:8V#LROfW9\tcF?TTbY\x0bf2=Wx.lFy0A%%U%m$dz(#1X<qD5@lgFRAIB"oTiJ9', '%%U%'), [40])
    def test_case_1868(self):
        self.assertEqual(pattern_match('X71[?\x0c{{Y%p/#  \r3? K3,e\nUn]\t82$ofQDEPJv%FaDWfEXxLnH"G,z-c\r>\tA"-E%^M3us{o:', 'ofQ'), [31])
    def test_case_1869(self):
        self.assertEqual(pattern_match('\x08W{,i\x0c^$Ym3&%oU,8zWT;hg>pl/iW$G\x08{L0`QzdkD@,;F;\r)ZQ)}\rCSlL+5%Nj~|2Xflhl\x0c^mV=O!H4l8;j`nE9!P\rFXlQ\n+\x0bHS', ';hg>p'), [20])
    def test_case_1870(self):
        self.assertEqual(pattern_match('s /;w/S>\tQci cooKbgb=T\r$\nKaLy9r5Pn+swDndzCFlHzmRw4I95uZ76W;+', 'S>\tQ'), [6])
    def test_case_1871(self):
        self.assertEqual(pattern_match('h3{@qkv\tb}Fhw._BibY\']WfMOXfwE3\\cd5&w:+Apa4f(\x0bC-"7\rLt41OJ\x0cbZu=9)]uz?._M\\_kvTTX^9nW$|Nu(;', 'h3{@qk'), [0])
    def test_case_1872(self):
        self.assertEqual(pattern_match('/joZH!\r,\x0bwA`%E\x08DpHeptV>R@1\rMQCb}2AcUykQ"CUM,[GCz|tsV`+/Xc[X.%0J#B)D\x08ix\n~', 'M,[GCz'), [42])
    def test_case_1873(self):
        self.assertEqual(pattern_match('%9P\x0b)KD2pJ2G"*nodFKlj\n$=0trz6j%{ kesz-$I<S$mjN0L9qBd%', 'z-$I<S'), [36])
    def test_case_1874(self):
        self.assertEqual(pattern_match('U8L7Ec>CG2=3\rDV%l(K1[6*s\rGz#9D3m!EGfb,uQ*[GmIwb_=o+-;K4\x0cZp;\n\na}a', '9D3'), [28])
    def test_case_1875(self):
        self.assertEqual(pattern_match("MqQ7y4Mhb]caNa=H5v:]KP\x0cJPF{}55\x0cn5Pb=L'K\t`lJ-Yv0)_YqZfhI{td:wgG5dq]S`RJvgtsS?!I0FR)T;/-3aX|J%Z$", '5\x0cn5Pb'), [29])
    def test_case_1876(self):
        self.assertEqual(pattern_match("&?A2jDht8G[t\x08!\x0c[C\x0bac\nQ/b]Z8P,'o,_cDB,O!\\-tD5GYcqm]IpAf\twDZmM/hwT{B<UCclWtD", 'tD5GYc'), [41])
    def test_case_1877(self):
        self.assertEqual(pattern_match('zKY$Jq.#=F,1<sI\x08mS2TNrmzz3H0jp?U7A>I9A<\x08V[[i+_}0>\x0bx_{%nv$0W\\$(f[95"', 'p?U7A'), [29])
    def test_case_1878(self):
        self.assertEqual(pattern_match('W/dHhWDY\r.y4dqR;\x08fcH"]\x0c(uzy2Ou8![@\x0b`cuv!a[vI;\n@tUd`{+"/Ga\x0c,K\tO_U.MOVqb', '2Ou8!'), [27])
    def test_case_1879(self):
        self.assertEqual(pattern_match('\rDS4\\hM2aiHNbkOs75Wh"0sZ[KYc[g,\x0b\r2n1c^75;\t"gn1PWhDq~|i,\x0b8Wl3nVi|;y(6#bAn0q\r5t:Xz\t8w', 'c[g,'), [27])
    def test_case_1880(self):
        self.assertEqual(pattern_match('kvFCL^\x08J9"826(u$*oyk|N*=|4*iD,x\x0b?m<X5"\r[F;w)\r\n`NKvqQ$2;c', '26(u'), [11])
    def test_case_1881(self):
        self.assertEqual(pattern_match('$#\x0cGjyM\'lYyA]g<hF%h_=1lr::q\x08~<4[NDF(z"6#M\x08[<J9/1{ok', 'A]g'), [11])
    def test_case_1882(self):
        self.assertEqual(pattern_match("qB=AT/7oe}7({r'KAE@e6\tkNO&C]Qm\n<pWM+/G5ODI3K8),AP\x08", '&C]'), [25])
    def test_case_1883(self):
        self.assertEqual(pattern_match(' 0.Z5vc+#(XBDU]"m;+\no~x\x08f*\n\x0bn)k,q[/TZed]-ux/dkOv`&S4>Ag}\\9\x0c\x0bP8\r5<G|5Qa$\rI\ng@Vq<FM\\; uq*yO\nM%:', 'yO\nM%:'), [87])
    def test_case_1884(self):
        self.assertEqual(pattern_match('\\OlXv!/c!@Ti-\x0cF\t_\x0b@4]`$!2U{j}}@9sM!\tZ5d\x0bWP$y$\n?E8 L?Ol4Q\t<|u7WQ&\\+WV4dq`*', '+WV4'), [65])
    def test_case_1885(self):
        self.assertEqual(pattern_match('|%\\0oSk\r>V[ gvl7 \x0b\nsq\t"1N>=:&-zyq@XVk6zLKn&\x08-vm2#]i)8LlsaPIhm~-3Pw].!Ll+8', '3Pw].!'), [63])
    def test_case_1886(self):
        self.assertEqual(pattern_match("[^hr/Ve_<--\x0bb<'X~H6O]i|t+X=$2hT%RqWSGMnf.6#U9SC2U'\tdx\x0cZ\noRR) [AW~tRk[", '\noRR) '), [55])
    def test_case_1887(self):
        self.assertEqual(pattern_match('Z[Ua\r<R]L!)cQHG\rTfe.l\tB}1\'kf^&74N_=}!V({c+"Tr/WLF=N\r\'qv+bu\x0bgpyr5Rq-K9ua w\'tv CB)MUo8;w35e*O--PJm*\x08Qq', 'yr5R'), [61])
    def test_case_1888(self):
        self.assertEqual(pattern_match('%[F6\rBM3E"n`A<[8Na_6/GdK4lf|y~ WLmvDz?H;\n19HB\n7b[PHgyheW[u=vMr9JOGUIr7hYm=fE&\'E?Y=zM%2E6+kj;5KkZ', 'Ir7hY'), [67])
    def test_case_1889(self):
        self.assertEqual(pattern_match('mD!y};c*J:=eP%\\m-i;Mk\'4]}uq$B?i6fmnqD]D#2n\nGx98"*oi}:6&hF@\x0cueldJ7\'z^0)Ebnf\x0bSEc3\t?eNx\\U[\r08%\'oN', '0)Ebnf'), [68])
    def test_case_1890(self):
        self.assertEqual(pattern_match('\x08O\x08)8#]M,GWd`[8WN*"fY>W0&\x0cE5YX@|vZOA~A"&+f@\x08C^J+\x0cATT\rV', 'YX@|v'), [28])
    def test_case_1891(self):
        self.assertEqual(pattern_match("1'|Y\x0c\x0b2B7&O;4kriURAhx x $HR0\r\x082N@~=cT\x0bw\ri\n^YVAA\nyajAteP{Nlj-MSG^fU#n34LU\n#0nMu2,yVgPnO*Y\t", '#n3'), [66])
    def test_case_1892(self):
        self.assertEqual(pattern_match("SB*S,2R,)!{uB =&+JM\r/yKhB<1?,L\x0c#5\tw2c'69fh u3/.<J/\tl[4`4J*T^n", '+JM\r/y'), [16])
    def test_case_1893(self):
        self.assertEqual(pattern_match('Thp[\rNS4tEoOaUlC3Dk5LNUOs:\\uc._A&cp7a8HEIc!hSMQtn:RL<GJ+~Kgt>^e~c\tO)[G9M^G]vY&I&l61', 'uc._'), [27])
    def test_case_1894(self):
        self.assertEqual(pattern_match('8U^E!A\x0cd]%/}=OBpkv{\n"q}w]vx\x08E"ryC_C4N\x08EoT^}!5w`8GHn;T&A\x0cFGtbA}ydp}=vZ;eB|=\x0c}Ui"1~j', '=OB'), [12])
    def test_case_1895(self):
        self.assertEqual(pattern_match('=#mnH\nY\r4;$ixxu\'O#zVHWkT _A=y\rkAl6.^#L _O\x08g/qM]J7CMgc"FS /[oS1', ' /[oS'), [56])
    def test_case_1896(self):
        self.assertEqual(pattern_match(";r;yw/FejlH)\x0b\t!j9 2.|a\x0cpBZ J8 HI_'?amv?_:q\x0bf/m5S1+", ' HI'), [29])
    def test_case_1897(self):
        self.assertEqual(pattern_match('}6;F!+ S9RWhA\x0b+Wevu\x08E11/zE\x08%ehA<Db{P=ItW>b d4pxJl@nn\'Xr\nYL[1KZ"]|;w', 'u\x08E11'), [18])
    def test_case_1898(self):
        self.assertEqual(pattern_match("B#j\r\x0coe`B<zyRl'F%hmb\x08{L_jHuZoYjY`|\x0cYC{$YO\tD+'\x08F1VT@f\t1sVyM\rC5qJ5/it9e#?w\r!F%U/\ra@", '1sVyM'), [53])
    def test_case_1899(self):
        self.assertEqual(pattern_match('wdC\r;>2|\x08J\n !s.|:K\x0beIE<f.CIlv[[]y=qSgz&Xc xxM~u#Jw,%|X d}j-B+a1uNnjn#FiU_$"q5\'\r6#o', '+a1'), [60])
    def test_case_1900(self):
        self.assertEqual(pattern_match('6&@p\x0c9_go{"OyLcLio\'GT/"V?mXKh2vvk\x0cyt|v$B0n/vowz28p|JFw9B]', '$B0n/v'), [38])
    def test_case_1901(self):
        self.assertEqual(pattern_match('\r\t5b+)?)j,Z!ugHD`pnOp<"r }~n~7=V?8|+^udkZ [.yWG\nEX*5\x0b4x/P\'\'\x0cZZTS.%5aVm)\r4{\\a2y>Hp%XQP/%\tv?', 'aVm'), [67])
    def test_case_1902(self):
        self.assertEqual(pattern_match('c^{.\x0b29Lhnsjh-p{lUMn"L_2!*;ZS6qk!WAPxkx$}>ZWP+_rNdC\r:kqDuitzL7YuRMulrR>| n\x0bS\t6g@[oXlybr2Rr\\:e-z.3v', 'P+_r'), [44])
    def test_case_1903(self):
        self.assertEqual(pattern_match('xLN\'4q\x08Bo;\x0bUQ<8fArp]0kCo&>bA5Y#pjox"sJ\t\t+9+]9.mG+?R-%T$}s|ZC7tu.o2N=ZY=][ Q-$aj?%F$-J&)Rf', 'o&>bA5'), [23])
    def test_case_1904(self):
        self.assertEqual(pattern_match('[AF5[p\'qp0"KqbA\tcS\x0b\r^}Wd1v1\n}O6Yi_qH;\x08JPyd_6!A_d,v7AG\x0b}\x0bh]eF\n#L+QC?*P+.N\nAxi^/hGNLRdIe2":=}', 'qH;'), [34])
    def test_case_1905(self):
        self.assertEqual(pattern_match('g6ogqi83X<\n?s2~Ctb>}sj6yw+rz^x{z,\rd1Fk\x0bES3\'r\'V*a"t<.p\x08LmG', 'j6yw'), [21])
    def test_case_1906(self):
        self.assertEqual(pattern_match('<A\t$\nlf^Q=2E^[4k=<2HytxSwn-]2]-j8x4n+{+4)6\x0b>\'fB\ti#K.D\x0bE\x08A>B\x08I,ttm,Z"Pl[', 'j8x'), [31])
    def test_case_1907(self):
        self.assertEqual(pattern_match("%S3A\rc)$5\n,yFX.QRg,2t#*\x0byhN\x0bw8Xj@E`d]qaP-H'\x0b,'LBr0w<IXlBF.,60kwck3YHG\nUoe|[>)]H'xsr", 'YHG'), [66])
    def test_case_1908(self):
        self.assertEqual(pattern_match('6k\'|\x08#>q^$MKJ:\x0bLa&Mmq&\t{k\\"4#>\x0c"h\\1.-XU3Z1zv:_1^.&l\'xt>.Elx46AtXvP-KKU{W[<^V%(6b>[~_1( \\\'HD 8?\x0blF', '4#>'), [27])
    def test_case_1909(self):
        self.assertEqual(pattern_match('[B?No+QpFT2>"8\x0b}"jRjN,(aH,:%90I\x0c(*L!, vUNkvp\tYgd_\x0bDa\t _Fh$(\x0c:u\\ecV62', '\t _'), [52])
    def test_case_1910(self):
        self.assertEqual(pattern_match('Z+|WO1 O<P"|lJ#!sa0*yck2hOcNjw\\JQgW+Lg\\Dm\nMiaGm2q>', 'k2hOcN'), [22])
    def test_case_1911(self):
        self.assertEqual(pattern_match('uZ\x0c\x0bp7*J\npo`\x0cO\\i8VQv\x0c49SV5;s5\x0cGPnEZdd(\x0bD\x0c\\\x08P SC.^65a6l(lK6\rhJVc81F{8S)ap#V\x0c\t{0Cp|c~XnX^g\x0c5=QR>Cj_A', 'V\x0c\t{'), [73])
    def test_case_1912(self):
        self.assertEqual(pattern_match('YReL\\\\"]Xto2V-o]\x08%|W5/tw|5\'8kdMVvL8IAG|(=jJ\nzK\ntJ]^j,cU X}#wiLL@732^).%x~|\r6N\n`Io\'SsMrO`C?\r\'', '8IA'), [34])
    def test_case_1913(self):
        self.assertEqual(pattern_match("FPqT|>nT8~cC-l[5;M,oY*\tr\tth4\tA:+\t\\&%'*Lq|\x0bTzV_r\x0b\\a_65>]?<mX", 'FPqT|>'), [0])
    def test_case_1914(self):
        self.assertEqual(pattern_match('\x08{a]kh;JU:{k"\t;}34+urN07WBga3M|~vuSPE\n\\0Z_-xPGj>Yv)yE\x0cs,g.>7!\t-I{?#8(EK%`/N< 9T3LV!^J~', 'j>Yv)'), [46])
    def test_case_1915(self):
        self.assertEqual(pattern_match('KR_0\r\tfY(#fqHF\r.\n^%_+8f;{-A0kl,VoFec/eZpC{QE7cK w)^-czsJMyW\x0bS5U}BA?ZB\t*\x08\x0clNT/y)q_/', '0kl,Vo'), [27])
    def test_case_1916(self):
        self.assertEqual(pattern_match("ryAQ*h#q=v0\x0b$\x0bEaKNJV_YmKs@K4F}?:%:wptR_QwpU-'\roGO50DZryS5\r^,L6Ll}.D[&PVaaF3 q#1", 'ryS5\r^'), [53])
    def test_case_1917(self):
        self.assertEqual(pattern_match('cF6ZC#0=wi\n,\\M\x0bpkjXSMdL@4%bPGmy(i\t|)MSU{\r\n\toI\\U)P1+Fgz5xR~\nTFc#3)O[)2=n,WkR!r~AyC\t>', '0=wi'), [6])
    def test_case_1918(self):
        self.assertEqual(pattern_match('xZpkZ\x0b\r7eTs}{KT_t}\ry;<WTc#V^\x0c}S\'js6",XQk -2&2dBAu!D\x0c9aNz9iD$\\v2@6w', '\\v2@6'), [60])
    def test_case_1919(self):
        self.assertEqual(pattern_match("&#?D7HA93Q*\x08\x08|qh,my_A%\\3r0`:I,_$]x2n\n0P5%>Tbz>w1z;2\tX!!1['Q!:s", 'z;2\t'), [48])
    def test_case_1920(self):
        self.assertEqual(pattern_match('\x0c{\'rbPaXQc}[^\'\r^`vdx_e~5Uqb92@<C;ZF\x08a]l81Ik8{0jt8\nJs<d74H.$?5ILA{,Zy2W2&V \x0by/[Mk|gFmx\tj"', '5ILA'), [60])
    def test_case_1921(self):
        self.assertEqual(pattern_match("m'|65w'>\x0b6_>QrH/0\x08^(qN;$+.kxBzwtE\x0beBC80J{h~''6O_!vC;;o\t@\tmA", 'Bzwt'), [28])
    def test_case_1922(self):
        self.assertEqual(pattern_match('l+r\x0cHA\x0c,u>`B4;y|)*(_k>o.i0A/a\x08@!JK|HxJ0g]fd|ih>\x0c\x08uv<?Q3F3/', '0A/'), [25])
    def test_case_1923(self):
        self.assertEqual(pattern_match('C_(,.|$Z1QfcN`|\x0cjd^Kq{4C{"8):-;p0h[5v;D\nOhkx/qn,dk0>&*R6_r4J^!', '\nOhk'), [39])
    def test_case_1924(self):
        self.assertEqual(pattern_match('57.BX8n<\x08p&n)"dWiCBR{dOFSA#l6e6!ros<9>\nf|b\\$WG*Gokw1 /R5LF++)\x0b4lBTor?}ZwqMyy8i2^', '"dW'), [13])
    def test_case_1925(self):
        self.assertEqual(pattern_match("RXmk_]QmYp1\r0VI!r5J9<%Y1,;`aXDQ7$M[ewHP#w1sp'wydOwC_a/n", 'M[ew'), [33])
    def test_case_1926(self):
        self.assertEqual(pattern_match("3dtkE('WcPo5ytBpmh$9R#n&i{}]N\x08N`3=D^`44T]>\x0cGDqJ\n6%bYpvN.sx)ABDh^y~0}/A-\\d8=|\\f/Xu&H93Qu[]frgD", "('WcP"), [5])
    def test_case_1927(self):
        self.assertEqual(pattern_match('>x%k;keMb:.pkUF\x0b~i~!rBeHRt76pp{x/k?vfxWQj+WZ\x0c&[k+~zYDQk!\r)zB25\nfGJ`,77@xh%s\x08\x0cr&[i\x0b7"mUTbA!O=4@6.I', '25\nfG'), [60])
    def test_case_1928(self):
        self.assertEqual(pattern_match('\tcUp13\\ATDVx2lk<R2Yngm^$0{DUe\nz$ )P-Jo%L:_"A0e*M.fE(\rZ9\n+*DpE\x0c"B!>G2Z=$UX', '*Dp'), [57])
    def test_case_1929(self):
        self.assertEqual(pattern_match('<2tb-69Zt>?RH:KvQ 3R#nO~e.wokAD\x0c)$la"v1Q[7a<(._b\x0b\nhPtz# T2G860\'m', 'a"v'), [35])
    def test_case_1930(self):
        self.assertEqual(pattern_match('S$-\r&.f\rN1^}`8(^``,>PmAzbkB6E{\'EM \n-f`HcVZ"9qsDES@zqz=~lDI', 'PmAzb'), [20])
    def test_case_1931(self):
        self.assertEqual(pattern_match(';\rXXg!FncU}>L)&Y~%~\rH{gLHPWJ~%a3@S4OwX96F;G54Yz\n""5^xnHWx=,5Sp.@b_xT1C0\'/\'W_,HS5&', 'W_,H'), [74])
    def test_case_1932(self):
        self.assertEqual(pattern_match('W|LI*bx@\x0b6=b ivqThu1w`$qH8;\tce\t}q\x0cur2aj0[jaw>%YUf}Ic"P%dJ:!{m\x0cLKkU4|', '{m\x0c'), [59])
    def test_case_1933(self):
        self.assertEqual(pattern_match(",3ygbfEw_5^xSP.MH-!qf=4+O[o(Gx\r?W\x0bsQp]@iNY88?\x0bQLfY&@`jQ;\nP,Te-oF^<{aDg_[4g*'M\x0csV}", ']@iNY8'), [37])
    def test_case_1934(self):
        self.assertEqual(pattern_match("}'\nsu\\c^m#+;,YBK}g7_rOZhRbRpvp`scK+-[SZ5Zoy:CYO]pd9LTT!`#(W7", 'YBK}'), [13])
    def test_case_1935(self):
        self.assertEqual(pattern_match(":P`iY \t(Mn;;y(p{y#C7OP}J>U$.QNDbOT=C\tKyUDx[ri!Nl*\rhq2%V0'H", '\t(Mn;'), [6])
    def test_case_1936(self):
        self.assertEqual(pattern_match('{12$\'&s&\x0bnlBvN:\'oS&\t`~FPGC)yRd}eaX)\x08"j7)!TmF\n7S\x0c(b~3\t!\x08pWEpM?', 'aX)'), [32])
    def test_case_1937(self):
        self.assertEqual(pattern_match('3\x0b|4+EqGz_K0%>\niPExwSG([QB-r83G&W#^}|PDLV>qpTJM7*`}3) 6lvExz(Qf>F', '([Q'), [22])
    def test_case_1938(self):
        self.assertEqual(pattern_match('.6)"z_<,^(ra|e\rpA0.!$^ICTJa @s71U$T7X#Ay[As?yU3,Up3]\r5)f9F\x085m\ny/90LyBXU\t(\x0cGl]o@T!wGR`w\'xD9\x08w)~|S<Lz', 'U3,Up3'), [45])
    def test_case_1939(self):
        self.assertEqual(pattern_match('RabKy[%\tzTE/_(>\\\x0bG%F:m(;,0)\tF%aOYtSLHvO~^^bxp"-AAU$a\x0c]YW.t?[.fAfN9AG>t1R{U6.9v"]>L=HSK9JC\r\ng~75pFB\x0c', 't?[.fA'), [57])
    def test_case_1940(self):
        self.assertEqual(pattern_match('<zmb8<X\rZL)H6A8/Lz\r.hlbA779\nn:\t\nqUH$\x0crNL^Xv"cD(0%s`B3`|6(pmn\'*COY\\v)>_pvIZF)\x0c%b,', "'*COY\\"), [60])
    def test_case_1941(self):
        self.assertEqual(pattern_match("z!!\x08ciIlW='pZR1`!oH]cwIPU\x0bVN`}d)\t_fgh\\VCz6Q@Df%CcydL;|2A@?#r&hqBA\t2(0MDJ#^{hWi,neNH=VqzO:%e9%", 'Ccyd'), [47])
    def test_case_1942(self):
        self.assertEqual(pattern_match("Tv\rHvaM~.&^Nxe[<V84Qxu:Np\t3.6ng6(i's0u^&d _D\nfi=PIn.ZiC\r{_1*oE9BSKSXxWS,#", 'XxW'), [67])
    def test_case_1943(self):
        self.assertEqual(pattern_match('6c\t2iqi(,F\tU\x0bB3@#m7w\tC\r\x08*^P/)"J|ZN}y\rIgn7/2%B\n|{<y0kOx%ij&v0]F\'_-J\ts8t\x0b)^%4', '(,F\tU\x0b'), [7])
    def test_case_1944(self):
        self.assertEqual(pattern_match(',*_io8c172T4PR\\g\tY",&JX1~Y`ZKf6D>kt<@9P7~+^scXMS]\n:p2nxdXjy~os|+?=p W:~gPfx]$xG:W6n;,-"VAo)', 'x]$xG'), [74])
    def test_case_1945(self):
        self.assertEqual(pattern_match("j}9Lt2f<\ran1|\x0c8Q\t7))&NFH42O_ <X'6@I#V,^\t_@V!Zvr`DheM\x0c,lOE I\nK8<t+C(#:HOgEs\n#6 +b", 'V!Z'), [42])
    def test_case_1946(self):
        self.assertEqual(pattern_match('R_Y&,F5>"X,\x0b\x0b(hGO5E/JMAkZ\x08f^Xr~cs7F\x0cyQNC5xz@{)[sPRq?|koKgiGlipW%^6<XyC2A4%<K', 'O5E/'), [16])
    def test_case_1947(self):
        self.assertEqual(pattern_match(' 2*8d17_8=Q,>C4 u-?x]@(;s?pYn3?P\x08jwcThN$J"VIB|B R/wq\t\x0bOJ^$Vc90o^{:i(vX^6Jg,8s\tV*ASCs>,J7M}q \x084Ofiq', '|B '), [45])
    def test_case_1948(self):
        self.assertEqual(pattern_match(">w8m\tImu}?$E}S\\@OPL!~7KSXy\x0cM{BHyqL'EDfoN8y%f76b#`%uwic~-", 'oN8y%f'), [38])
    def test_case_1949(self):
        self.assertEqual(pattern_match('Kep\x08c0qAXou6S`v=Et-"X\n?(! :ukF-|\x08\rN0n1\n<e-6Us@2\n*\\[P]uD&*biWQiq^[$PzS=,&D.{_uzB\x08{y(j', 'PzS=,&'), [66])
    def test_case_1950(self):
        self.assertEqual(pattern_match('OiH\n=P%_EM58\tO*v_Y@-\x08\x0bcU3LJ,H<ZK*Xv+z%xoj%N\n-f8d\x0bJ/Y$zHuzY}', 'z%xoj%'), [36])
    def test_case_1951(self):
        self.assertEqual(pattern_match("5RvC^e}; ^<:]g'7 \x0cm\x08Dp1/,}%0F\t[!g?|c:\x0cV&^i\x0c0T]Qr`]4v{lYWX", 'v{l'), [51])
    def test_case_1952(self):
        self.assertEqual(pattern_match(";du!;\nQ5f6%NaR;IbQA.+ey;F9x!mQ'_><||STlcw$5o$\x08zL'=2!>(Qr7\\{\x0bW))CAB3\x0cpc(9\x0bC!TBeBGHr+7<03(/Mm]\n'>A(", '!>(Qr7'), [51])
    def test_case_1953(self):
        self.assertEqual(pattern_match('Gkw5{*f_X-jp!fk{e@Hxof@>L4kug^,Cg"\x08rW|4"7TN~P~7\x0c,rYn^!/]', 'kw5{'), [1])
    def test_case_1954(self):
        self.assertEqual(pattern_match('e!,CjlSK[k7S\n0-jtoiC9rO9ONf/5r02&~R1=GU[L9{`R\r"&#r!aKX)N0c`2M?45NU/S-K$G*FV', '45N'), [62])
    def test_case_1955(self):
        self.assertEqual(pattern_match("c_3iQ@\x0br'`vtI8\x0c5X?6j.kz4!:tcw%%\\cp_{oL9(2Qb\x08lQw,h}\x0bReZa", 'h}\x0bR'), [48])
    def test_case_1956(self):
        self.assertEqual(pattern_match("FY}9U>.kIt=0\x0bI_+M\\x'Vf 3/{D#)OSG\n\\*Rb~w'm|[CF\r}=i\x0cB5H<[N0j!/:Z/j\r]#U!K5u+H&i5&>@]PL.R7<bNQC'\x08{pV!##", 'U!K5u+'), [67])
    def test_case_1957(self):
        self.assertEqual(pattern_match('7fDm!<I13t.\rw-G88-)eH $?X1!^U R(n"2hAIO\x0cR,1IN\t\x08Z@9W495XW;=\x08"x%k>}=Bmew@l6&0jFH>aqffr=B%lQ7=\':h', ' $?X1'), [21])
    def test_case_1958(self):
        self.assertEqual(pattern_match('PdfD!V*k~nv#]V6>Rr&-\td:/tU/Y]n\x08r_pnx$[\rIn0M>pTMF[ l\x08lhRR{X]p8T8f~KUL>}Z$J2Hnkb8-\rGBR\x08?', '>}Z$J'), [68])
    def test_case_1959(self):
        self.assertEqual(pattern_match('Md`uz Y/IrHN(^ten"=V0r^BM%=q;U\'Et\rmOl <hvN(VqW0YA=\x0c9o\\h@NmgJJA', 'qW0'), [44])
    def test_case_1960(self):
        self.assertEqual(pattern_match('vZt_JW[9uL6BS\\9nC*:\'z"0oww5wV\x083l=*X"3,Ci\'K#\x0cBHW=wt\'L@F`,ALWtR~8a|+wK0', 'L@F`,A'), [51])
    def test_case_1961(self):
        self.assertEqual(pattern_match('E<Xr{\tP7a*R~pRU^KXA7Lv6,si5[ZhB&RjRG41~{O+I7OhK_[eM{\\|hkLtP--\r$Z+UAPs]F3U 3\x0c=&v1<kXCa\nzz+\\q', 'RU^'), [13])
    def test_case_1962(self):
        self.assertEqual(pattern_match("tSEI|%&9.7}:`]?UNsb@?5l:idX&\x0cyRKIT\\lQuv&jj9xrrkY'3'", '5l:idX'), [21])
    def test_case_1963(self):
        self.assertEqual(pattern_match('w\\l&M:ulaA_|+<\x0czw$c\niYeDO5"T4Ln:qJ`\x08xhLQ0<csyV)e/ q`c+qiidD}rM\'\x0b2qV,wY;/:JMA6', 'qiid'), [54])
    def test_case_1964(self):
        self.assertEqual(pattern_match("HO1J=R0|?]DL>. 8C^!.i_F?a&qX v+Ukdu[S8\x0c)6'J2!W5M _\x0boc0)F~jaHa\tK#{", "6'J"), [40])
    def test_case_1965(self):
        self.assertEqual(pattern_match('"LTq>XdD6FFH:H\\JSl?"`0>NGw84u<]V\x0bcgyJoUr@sscf6x/(h\n</}\x08', 'l?"`0'), [17])
    def test_case_1966(self):
        self.assertEqual(pattern_match("\t{\x0cZd\x08\nk}^(bO\\n>wJnZ%gI\x0b3Xq)MH8J-8CRQJj%1XV%\x08>w$PAd>bXva<2E\x0c&vs+&y\x08BM;8bXL\\yD7 }J{$s*Nt5WY'X}p~^'", '\x0b3Xq)'), [23])
    def test_case_1967(self):
        self.assertEqual(pattern_match('j$]2IidbkaBO=B}t\'AO<_FrdG"IZ&|:{Y2*u9,b][5?RFPnd[(K-U8+`fTI0U3Y&H', 'G"IZ&|'), [24])
    def test_case_1968(self):
        self.assertEqual(pattern_match('l=vrXS\rC/:Q"|\\s"U\x0ca-m6U[?:VnP<8 f8aT[zKeK.G\x08bR\x08]%i\\+7GD~Tcm\x0bZdxvRt\x08y5oh:e{Lp)MLu=', '<8 f'), [29])
    def test_case_1969(self):
        self.assertEqual(pattern_match('fw&aIsF:Lq#ma8e$A1F\n)!YCtg\x0b)r\rj.zhq>Vr-puc\x0cB2<cKf,\x0bC|&', '2<c'), [44])
    def test_case_1970(self):
        self.assertEqual(pattern_match('BR\t\r.@r\\B*A;v9~\x0b%xNJepFwcO\x0cL]9;v+.6WbP\'p)"mL,Lr>Qf$\x0b!DhQ\x0cU {Tj#(yv\'', "6WbP'"), [34])
    def test_case_1971(self):
        self.assertEqual(pattern_match('(x\x0c4)4[FbXCI?g\x0bxn4l\x0b.MM]tO7$X/}5s8;&z-b\\-Z%x*Otm\x0c62l\r\\%d0Qr*3I+x}?|B&~5x%avW5lerg\t}I1i', '7$X'), [26])
    def test_case_1972(self):
        self.assertEqual(pattern_match('8M-\t7!]:3k^/>Qs@Ut"2qoY-8fozK]t3tiX>\'o\rrm1xMLY:5pI?J$+B(;OJ^_c', '$+B(;O'), [52])
    def test_case_1973(self):
        self.assertEqual(pattern_match('EszG17\\;6*@)B$yPh)$@AscJk|5asSB~-BD\x08)nZ_]\x0cDR?sRF1R&D*', 'AscJk'), [20])
    def test_case_1974(self):
        self.assertEqual(pattern_match('p ~\\n@{<1uk_h]w${{@cw)A-L"`2wd\x08N\nYvE;&K\r38\x085#V"$b9$4B,k\rxZ\tr3.}[GHSR9Z=D3|]bMyd0\r&$SmN!(`*\r\nk/', '\\n@{'), [3])
    def test_case_1975(self):
        self.assertEqual(pattern_match("/:{6*;'`ViExf}Sqq\tnm!|k39-'3u\\,=XW\ng.}>:q>X`jGaa\r)Dd", ";'`"), [5])
    def test_case_1976(self):
        self.assertEqual(pattern_match("CCrpQnE\r(ApPC@SUuzjIq>'A7 L(%~#n/(!>.,,n:`Oh.W'B&T5h[\rECp!\x08DXI+bn\rj7I-Oh|T>bu|*Iw-anf,eutx", '&T5'), [48])
    def test_case_1977(self):
        self.assertEqual(pattern_match('?r##:\r/^uF5GEu8qwHz\'1YK`9H\'"q~k8}M,yD6vZ#]PJXdIE:]53~{hb>C)p!&\tFDJ)9F-k2u.7.-Tlv?8yd\x08[+UlP#\n', 'DJ)'), [64])
    def test_case_1978(self):
        self.assertEqual(pattern_match("GiE_4<@|D4K<gU'TYKI }Xk1hTWMK2QPB'scVPgP6$h?iY8{oB+HL0fe4vN<\n6jIa{f(F", 'hTWMK2'), [24])
    def test_case_1979(self):
        self.assertEqual(pattern_match('\x08/%}2;\n\nyf5?[2W\x08BSVC&i#vZl1nwPg #Nx?Q^$sz\r;m0s~o0S^69azehu', '$sz\r'), [38])
    def test_case_1980(self):
        self.assertEqual(pattern_match("|tL1s$9afH5C\x08~ya\x0cNGorD+_$ww#M&H\n:Dk#5JQ@i.\x0b18?L4!ReX+S`?:3XAb4Un.%/['`5V>pZYi;Sx.Fmo](", 'Dk#'), [33])
    def test_case_1981(self):
        self.assertEqual(pattern_match('Y\r:GR*QW0#HT8&!q}M\r`\x0cu.kQU9k"#bS*I*r\x0bUc@H=+?GMe%\'gR+YjtFAX#\x0cR*ELF{I[ge]T#m>yg@', '=+?'), [41])
    def test_case_1982(self):
        self.assertEqual(pattern_match('I[(`t!6]QS 8M.`;9HO+d5Jb-Rt7nV"c#{m4|\npp *#~R{E/ebX|0<`z|1_"E70JDws([4l^-qF2xayn\x08T}3+', '#{m4'), [32])
    def test_case_1983(self):
        self.assertEqual(pattern_match('fc-5kGUa@QlLK@EGqE~qw(2~gX334}j9[bvv\r]\\Z:&:Qk.P\\ql\x08h\t=XOc\x0b%u', 'lLK@'), [10])
    def test_case_1984(self):
        self.assertEqual(pattern_match('RzqingCxrRD>x\\`2~1\r7YQ%kGL"qy(du@K8D5LsNa$TvPlo|(V!dTe\ng7;4 Mg.\t(\'Tis', 'Rzq'), [0])
    def test_case_1985(self):
        self.assertEqual(pattern_match("*%D#T']v}:RYh$h\\B_=$)\x0b.&AD$E\r!\x0cV-!_3K\x0c.}Y(wu+r\x08yl7B%FS 1\x08d)k0Z2", '&AD$'), [23])
    def test_case_1986(self):
        self.assertEqual(pattern_match('n<]Gd(GBI]ipV\n\x08;;\r\x0b[h*!RR\t;1|Y,XW:Qe"9uN\'\\`PW#ZH13\t+tbe@[z:r#}bo]q$|*dQ%hMSvE%\x0b', 'R\t;1'), [24])
    def test_case_1987(self):
        self.assertEqual(pattern_match('s0\'N3/&>YVetYJ\t\'DA\'z;qrMbp\x0bip!u/x)=-\x0cGdn.(,hx"u]y)PFSk\'$ uA\t*XETN', "s0'N"), [0])
    def test_case_1988(self):
        self.assertEqual(pattern_match('fgt.5xdD,9%_A62u\x0b\r~-}!_w{[#L\'z`sLG_1Ok8a`62\\|\\=\x08KFH|b\r}Ox!2))Lp*Eczm,$hf ;7U0En\\Qf.1JcA9/"O0e6jm', 'czm,$h'), [65])
    def test_case_1989(self):
        self.assertEqual(pattern_match('Or$\x0c*LU?}oRDdpLmR4@";D]p!B~VQ#xkZ\'WUod!>*Es_TWrbdT>4\x0b/qtM&OimF0IzQK0N ^Kk\reNK<a\x08D\x0bv/6\x08BetC@J\x0c', 'Uod!'), [35])
    def test_case_1990(self):
        self.assertEqual(pattern_match("*ON%a>'krJ'lOS*6x(8K\x0b76rH}UV=Y:\rg+e\nOqF`Sl%ZWR;3]gZ=> C43-mY!SL73N,\n_`HTk\x0c&,", '_`HT'), [68])
    def test_case_1991(self):
        self.assertEqual(pattern_match('[c;&^+(\'|aOXTO\'vKTH\'q;b\x0cA9?W\rdH"4l?\nF!tJ#>%iskH\ti&\t_!J(cL5G).WFk\r.j9Y-[H:7^AFx.|pR8\r:@CAQ^sX}_', '\ti&\t_!'), [47])
    def test_case_1992(self):
        self.assertEqual(pattern_match('X-2)+Ay~E$;~ vMM+<g,xd\x0c&V]\'>j0=8v6z!:a]inM>Cpa7Um9-NYz"72quS$lSXjK*i%,sj;vr}s"m,8G\x0b7O', '*i%,sj'), [66])
    def test_case_1993(self):
        self.assertEqual(pattern_match("=uT\rbWd3\nBqERiv2nPOx!'TTJeXs\t)]0dz4Q8<gj.RU4F(x$!i$.E&0H\rHQHp*\n/yBmohzq?\tY}en", 'Riv2n'), [12])
    def test_case_1994(self):
        self.assertEqual(pattern_match('!|W:"%{[0E\x0b9"M|r=fk\nab\x0b1+?MH(~3{3O"Mvinz8u3gFbzgLi\r@PV1?$Ns\x08{48:F\rUb', 'zgLi'), [46])
    def test_case_1995(self):
        self.assertEqual(pattern_match('TOh\x0c\'W{5<0\n\'`|NQv{+,6IzPmkbstIgkf/{#k|:2[*>d`0 8H,cGS8u T\x0b\x084vOP"F_oRU&GN2k@U[[Hv%9S8J),a/aza#>sM', 'GS8'), [51])
    def test_case_1996(self):
        self.assertEqual(pattern_match("R:{WcMav+5{v<.<|U$/x)4!,Ia0:>.\tM@Ywp)avD\x08^_IP#+\x08g5]Wk4fZSmz\x0c4^5O\nQ\x08\x08GL\tFl&[\t'`;A$L4&i&N\r.V'Ce_7Q", 'L\tFl'), [69])
    def test_case_1997(self):
        self.assertEqual(pattern_match('/&(jL}V{#AX`iWz9D-|\tcZ]Sh*<GH3[m>#,\r8\t>/8V(\\.U\'^/0C_\x0c_TW\rum|b8\x0bjeu"| \x0b7\',,SGG\rP*6VD1#v/eNI', 'jL}V'), [3])
    def test_case_1998(self):
        self.assertEqual(pattern_match('CDXV"5u#0*Dz_uP"zrj &\x08/vc\x0cv{\x0c9y\th+=!\\%Fo<m\' P1Q4FY@E3\x0cRk{8>in#=2P)Qr{N:[0\tKx/1HmHB', 'Dz_'), [10])
    def test_case_1999(self):
        self.assertEqual(pattern_match("\rBm5!]\x0c2\t3$zWm\r`0PR| 7;WWw[yQ\x0bz-9$VyI9N*RP\x0b6^73bfk\x0boyc:~DG<ccbd'w*,8IrD\tF4KL(T\\E5I\x0bs?", '!]\x0c2\t3'), [4])
    def test_case_2000(self):
        self.assertEqual(pattern_match('k5lg u\x0b`<M\x08]FzVgZ$T4~0f>\x0bADj\t35,+#hzhCD@RshZaqe\tdG\x0c8l?;?L`-1WJ?,&UiW~\x0bj\nszzGXB!2Blrd', 'J?,'), [61])
    def test_case_2001(self):
        self.assertEqual(pattern_match('&si(I.1"l<\'y\nUg5<N\x08\x08lvZ:[-\t)h6"k/P$\t&UiT1oXiTPpA1JdKI', "'y\nUg5"), [10])
    def test_case_2002(self):
        self.assertEqual(pattern_match('/A-43XD&|\x08~|M\\}M{{=\x08\\VDh`2d;\\yY_M1>M>"1#|cd-BmUI>T.w\x08C\t)1}:LNPu^b~C+q?J~{h%6_\x0bX6qk', 'Dh`'), [22])
    def test_case_2003(self):
        self.assertEqual(pattern_match('(c]nJ4Bhk+z8(9\x0b8@+z>NaAawB1T-:kyig5AsJz5CoVtUq!TFSLx?wZ@tqFH+p23\x08?\x08!tF)m+Oyaiu[=Ce#b=BbLe3', 'T-:k'), [27])
    def test_case_2004(self):
        self.assertEqual(pattern_match('s\tBU~{CwtrU)co-x}DRr -x<c#,sEpd(hU\x0bH&w1t"[(PRXnc46J_L<\r\x0bqYb5RefppoFVe3[F\n]', 'U)c'), [10])
    def test_case_2005(self):
        self.assertEqual(pattern_match('\x0cJ&Q\tfh;E$MN`+v2V:UG&~sqA2*D2U8wn\nKKA"Wg7zAxZ^O,Ri}_:+P4a\t<pA,)Dd%G+9XgLUdTf\x0cXzS0]Eoh~X|v(Ez>5#7Sf', '\nKKA"'), [33])
    def test_case_2006(self):
        self.assertEqual(pattern_match("p\noEAtCby~T|(-72^mDjT\n*y)=\tJ (at?/ie7oivpm``miJsl9!b8=#'V", '|(-'), [11])
    def test_case_2007(self):
        self.assertEqual(pattern_match('ib;^#<`*)Fil5-`Xx4XRp6pIrz5o+UqyISPQI_uIA5:,)1tqo0h\x08@#Cpe1sYluJwQv/5~\\s1*\\IH', '1tqo0h'), [45])
    def test_case_2008(self):
        self.assertEqual(pattern_match('K&eEQsc<vx"+W6nF8SE;d[\'n{>OP8i;~+93<_;q;[3N"_hj_$sJI$j"kB9[aB>kt:\x0b4\\M\'\\\t\',jpvL\tl/\'dq', 'sJI$j"'), [49])
    def test_case_2009(self):
        self.assertEqual(pattern_match('_!Caa;7,bgjBW="\x0ce$tY\t*!tN<"WK.30fZPk@]`5?l)WgpF\t@U\r\x0b@B!aYL<)WZYk:5:yY\x0b)..\'X|yHxy', ".'X|yH"), [72])
    def test_case_2010(self):
        self.assertEqual(pattern_match('y_07.Sj""F)X1%\'(+6=(n#l,AT*5.2kJj!,%a`JZPG#UAZ5C6}[PMILi\n_c%G@I,C%bjOxu?;fc.KPMG+v5:|U^f:>\t', 'PMG+v'), [77])
    def test_case_2011(self):
        self.assertEqual(pattern_match('wfQ\x0c^vF^Xmz-vc7nD\\MW9Gal87dGUD4/XHn^l]cU;Hxe\x0c4\x08O7([Z', 'F^Xm'), [6])
    def test_case_2012(self):
        self.assertEqual(pattern_match('MYl3+L7!\r0^U!!/pVZ~X_7,[odS<\x08s2-%i\x0bGT_P`WQ|2#d}_H{&1', '2#d}_H'), [43])
    def test_case_2013(self):
        self.assertEqual(pattern_match("CLA[\\T5!/6Y0'j>m3m>\x0cB|:A;rK_C6^[Vur%{>X>#UgA>p-T3q\rFY*_,a]J-nm&7:u$uMr9^6</", '[Vur%{'), [31])
    def test_case_2014(self):
        self.assertEqual(pattern_match('f+z{.gKs_\x0b[niq\nDoo:pB>/\x0cgqo0kZ0~$QvdvHIIiR+ /:1f;7^=Csgc\t\nRr`qQbow=|F\x0b', '.gKs_\x0b'), [4])
    def test_case_2015(self):
        self.assertEqual(pattern_match('hro6z9L-,ZN ^a\tm!.l]#yv;hlX)"\\f/j\',\'ClWj\x0bWX5)$GTq|Yhb k$-k-c/GBt1+%DpyAYR]qQ%M', ';hlX)'), [23])
    def test_case_2016(self):
        self.assertEqual(pattern_match('N5-)zSEcsA"\rG&FrM5&gX\\%piduyDj u=zC=wpk\x0bsi^|Q-90ju!!~3+**2H\\`aKY/0;olz}^4caK2&v^foXV%"bTat\n\x08', 'v^foXV'), [78])
    def test_case_2017(self):
        self.assertEqual(pattern_match("K3$lYATm9mdz/'^rGq@SoF\rsPTkeN!`\x0cE3<sl\x0c6Xt3!K8m^Zw4%B\\R\x0bXcXc.b[\x08#vH(#nF\\\t)\x0b_?\rFH7bDPmhsGqiMd?U{O)&:", '!`\x0cE'), [29])
    def test_case_2018(self):
        self.assertEqual(pattern_match(":^T`]SKE%,~}Q;L |#2rPBXzKO6Bgjf?DZE/0;\x08Q7iTdEILto'%\x0b", 'Q;L |'), [12])
    def test_case_2019(self):
        self.assertEqual(pattern_match('Fmv3[U[eGN&tPtdHcoO$gQ1M&fl\x0ciuX;cu&jdwi4iOG!7pIJ1*L^jM,Z,ec~S1 MS0L\x08;Q$D*MT', 'HcoO'), [15])
    def test_case_2020(self):
        self.assertEqual(pattern_match('qx(<Al?efTU&20Zy?#j6p{C6$XQ_\\RZ0l\rN\n^NF6M6c]8Rw]E\rZ', '_\\RZ0'), [27])
    def test_case_2021(self):
        self.assertEqual(pattern_match('-|{U+yV0~josRJd(iW1)hyt:2<%^ErQ*AO~f3\x08-~/d&?T@,ts6getm)$0+Im<j*#uh}-\x0bh*CX%,5\t\\D+M9[it', '2<%'), [24])
    def test_case_2022(self):
        self.assertEqual(pattern_match('b&K"4r@\'JeQ9E{RP}"fR1si]]nwhk~J%sbw8cKZ rXP} *K4m~q6ir;/\t\'mX%Oe,%t:L\t]C,"$Onel"+D`6q<{~p+a%)_8H&', '} *K4'), [43])
    def test_case_2023(self):
        self.assertEqual(pattern_match('iP)"^Hec?*EW\x0cyF<Xp:aa~b41z\x089c!\'TAP[t)% \x0b &Uya._u>GB.{Z.9hbO9ewUAk%=}hH`\n\\\t"Jn$)%E_[#}3l4^N}&: i(&', '3l4^N}'), [85])
    def test_case_2024(self):
        self.assertEqual(pattern_match('~@s)e(uIOAT!;d`FkLK|Z&AIjI L<N\x08-a.z./SDB1a8wU>Dm[8>x2/ijDty]C2_n6<M\x0cV@e(AI&ObvL0qH :fMN5)]b&[}[', ']C2_n'), [59])
    def test_case_2025(self):
        self.assertEqual(pattern_match('q<<seRC6Z\x0bXj9.:H`\x08I\x0bW^|LOEw_nRI V{\\"Bh$\n|J(57=*d\x0bP\t!]*T\r:mgB7>\r\'\x0b', 'H`\x08I\x0bW'), [15])
    def test_case_2026(self):
        self.assertEqual(pattern_match('?jerh:qO]C V(0Ts\x0b~ou\tz3RJ6bQ+U@qt[M5A,>t{}U/(\t%thgb]/6Yp"\x0cgCIE>(sa\x0bJ5lu~<QvF\x0bO)\x08\r$.{/o?LqE', '[M5A,>'), [33])
    def test_case_2027(self):
        self.assertEqual(pattern_match("z\rW\\g\x08_\x0c \x0bRB5chZT%5lo(Gw$ta7rgU;~8DpN\x08?5|'-/8=rF-Wa'+ZN~6nmsS_+`7mLH3FrPS0q", 'z\rW\\g'), [0])
    def test_case_2028(self):
        self.assertEqual(pattern_match('~.\x0c~YINB)zY)X\x0b~G8V\r-iBD}vF-T^="d\n4y;k(\x0cZ^u]CPzLYR)nKi,4M<lbl6cXo2J)b3o=(7@%F\x0ciX.TCZC>bmD\tn_D\x0bD', 'd\n4'), [31])
    def test_case_2029(self):
        self.assertEqual(pattern_match(">+)\\H =<\nXjTA?'AbAv HBumH|Bp5VP7qPT~BMDaP{|Sl^\t\x0bz0DE\x0ciy6 #MWJI", "TA?'Ab"), [11])
    def test_case_2030(self):
        self.assertEqual(pattern_match(")%mb~M:y*tJqE\x08pwNV,#mw\tS\x0cj:].\\[+i]3h^R?je[V\r#'k3t}(nPWw0\r\r?\tM\nNAS>u~^dfrw7{(a$i7FweT:a\n;$?&50_[zG+U?", '_[z'), [93])
    def test_case_2031(self):
        self.assertEqual(pattern_match('0O&;<:jrpqDP\nX"+9\'6)#\x0bUa2Z=1.$"~-R,HJhUv/HQt{l+i;ybl', '$"~-'), [29])
    def test_case_2032(self):
        self.assertEqual(pattern_match("qCxzUwZhP8%=\x0c'nY5j'I#4fAU;Yr&)W&I%SZv9K\n1Cj\\28{oC\tO_~]Zry()'\rp6", '8%='), [9])
    def test_case_2033(self):
        self.assertEqual(pattern_match("OwT0uhY_-sF,iwXJd$\n#|'/2E)9\n,yN+M-=U2Eg9czfK~\x0b6@;\x0cpC", '\n#|'), [18])
    def test_case_2034(self):
        self.assertEqual(pattern_match("e\rPsV|6LFiv+.o{|o5wJ^k=,[FdK`{V6'pz;~IZWObdX*B~|bzs\x08I`X5sJb$p~1@?", 'bzs\x08I`'), [48])
    def test_case_2035(self):
        self.assertEqual(pattern_match("^c*H7!0p7t&4>sO\tDX0?0Wx$615y]g9X>O{\ta4(\x0bCL-'Wojy0?[1P~)I!&Yv;\\4?w", 'DX0?'), [16])
    def test_case_2036(self):
        self.assertEqual(pattern_match("u8n2W35+)7@f?DaTm#Bvd,6*v=o{,L\r?*D2~5%slNrsuX'\tv\x0c8?$=9>3,6\x0cWq\x0bAa}0}:_z?J~gr(\x0b}\\W*/j~;A>eR$:72fih", '~5%'), [35])
    def test_case_2037(self):
        self.assertEqual(pattern_match('"~pcBWZ`q>&*2)Yld D)B\n@4wne3M\r/wl wK/cP~T|(jA\'0IvYNSfi\x0bF6H?bhIHz\t%"]3&HKOfJ`&2suV5/K!\tCb|;{', '|(j'), [41])
    def test_case_2038(self):
        self.assertEqual(pattern_match('q3\nM\t=Mh<GBk/Lp7"3i$d-#\\3<)F*.)\\;%\x0cWF".C4\\/\t=_"n^R`J1E]Gn{dgs\n:jz#g,o6A($', 'Bk/Lp'), [10])
    def test_case_2039(self):
        self.assertEqual(pattern_match('t%7Q?^(~\x0c(<;"eB_Z`KI753Qv<nf+y)[r#p:nGvt/Zp\nfk7Q(Z0-BW1qu"#\rbUVM{vXy;a2B"}\r1Vx\to9V1$y<CYe\t\x08f6xF', '"#\rbUV'), [57])
    def test_case_2040(self):
        self.assertEqual(pattern_match('%+P7^gkr7\t]uL84"l?Om"::{r2ftD43Nia$|TR)(/\nv`v\x0b\n;&~\'V^}.@:&jd\x08 \'&1[opN}|-', 'tD43'), [27])
    def test_case_2041(self):
        self.assertEqual(pattern_match('L8(Z3Z+y%\teK+WLgkfti\t6xW\nhsS \t@|yqQvzP#Y\t(^fN7}S<c\n>|550,t(5cUp+7>Z W {\n.\x0b%bV\r?O:0cJa=tl6Z@NW+', 'WLg'), [13])
    def test_case_2042(self):
        self.assertEqual(pattern_match('jF\'iX"% 9PEuu&`[\'%MeA:G={Q"rb7pZP*$vMXd?s}^# I=>t=5b9UM*uu)qu>Zz3}x(9R}8!!^>:zA', '9PEu'), [8])
    def test_case_2043(self):
        self.assertEqual(pattern_match('#K/{a-8m*=VEuAF&V\x08&D4EQ6\x0b["K\x08.uqOzf=c2\x08i5=ycw1FtpCJYBh{>n*\t08:gVFhUA\'\t7<WogpPwr', 'h{>'), [53])
    def test_case_2044(self):
        self.assertEqual(pattern_match('!]Rg!\'6z^Ihw.W)\rqGa|\rNDutBG\x08wuo8{JJI\x0ct\x08hhv{Qx*4BHTr}JN2@qOE_z1b>@*FORC/*2bF]iN}GzYdiw aJg=k"Lj6\ry', '\x0ct\x08h'), [36])
    def test_case_2045(self):
        self.assertEqual(pattern_match('VTKO5JUX\n*\'=1\nU$GBfG=H{]l`?S1h~EAhX5nE|6/F*sl%mO=t}J3i24AzdsX y-P(p .Z@Bf0\\eJ:gZi#,F"', '1h~'), [28])
    def test_case_2046(self):
        self.assertEqual(pattern_match("XLHUa;\\|i<'9,|?cbS\\;\x0bfj#1iC;<oG\x0b, N`q/de5-3[v;sOYeQ?j;b%%P-op=$FK0WNz[", '1iC;<o'), [24])
    def test_case_2047(self):
        self.assertEqual(pattern_match("g\\4OFq\x0c-$3\r-Lh#t%nMT@g'\r?\x0bEmi2\r9u?\x0c]<]|uc1Z i)N;kTCL\tI* |V.fUER-'|,w;R}Krzn?2t*x7qB\\\tXR;,%\t@B3~ZP:", ']<]'), [35])
    def test_case_2048(self):
        self.assertEqual(pattern_match("]Z=yV(qi$%W UWR'87OX'D2Zp)+NkAGp8w%g$C=]a^j^0@w@,2R(H}g8aQnIiTt3'Cd*^dof7t", 'Z=y'), [1])
    def test_case_2049(self):
        self.assertEqual(pattern_match('3p\r094rS d\t31WLk<qa^.5=}?zc]qCk<&ZVL02PLm`s!06h;|hN8y\n4^M,J&nSKStd((cj8j3|%', '5=}?'), [21])
    def test_case_2050(self):
        self.assertEqual(pattern_match('H*xTR>\rEF`fF"<TM(j\'Q8vCMxN{r5\nhVPYRv\\cH9i0E/}^M[,\tZUlyA3S5(zm2>(#w\x08@oO5Tm3\n#\t\\1_$(mgDR', "'Q8vC"), [18])
    def test_case_2051(self):
        self.assertEqual(pattern_match('lyDr3Tf][L%Q\x0bF#%e\tj\nn_U489Nv!$h/bfGz\\zHo<*/\'U\'OqV6"##oV:azXDYj', 'zHo<*'), [37])
    def test_case_2052(self):
        self.assertEqual(pattern_match('@RKo!hA1PUo\nQCZk/".@{!a^KI|]!*-ONUp"_UFA%4}WOcBKw]e``fx`z\rEp)sD$MA ]2UV-Li7Ogv\x08^zV[p|\x08a-', ']2UV-'), [67])
    def test_case_2053(self):
        self.assertEqual(pattern_match('p[H:3nhC}f"*XdO@6$CBg=\nUia2+?EII\rO"~T^!Kt/Hq\x0bEGT\t/~vRs%UlST {@oOR[=K|\x0cK09O%2C6&:bo\nM0Q[+j<n~,\n@b`V\r}', '"~T^!'), [34])
    def test_case_2054(self):
        self.assertEqual(pattern_match('Oj2\x08.0:\x0b:$T4eq%8\x0ce/o~L6$N4B!};.BSYnK4zxHs6b5%X!?4aE\x08g;DA_,*jjw<\x0b[e%KqWcTq<Lh\n', 'KqW'), [67])
    def test_case_2055(self):
        self.assertEqual(pattern_match('Ko+W\\\t-`y-$tP=fnU$cGz.\'Z+ePP~|n5l`!~=tR?|\x0c1~.?j+rvsekL-!"+o5gkF6 \nf', '?|\x0c'), [39])
    def test_case_2056(self):
        self.assertEqual(pattern_match('3*;\x0b"wwW\n,\tK3L"O3\\~?["[]@D:lC@.{&~Fr5A|ml?z8?F5#_$S', '?F5'), [44])
    def test_case_2057(self):
        self.assertEqual(pattern_match(" q97[\r} ToY$oP'\nDu`6v?7J[get@\x0bG(fN*Uqvad]@HI7GO+hsBS\ry<\x0b%vKMhk$E}8dM C,\x0b@ZHzvc5V3\x08u'^6Bhy@!%z\n", '\nDu`6'), [15])
    def test_case_2058(self):
        self.assertEqual(pattern_match('BNqzi\x087S7Cel]2=uP;L\x0c\x0cZ{E\x08Gl_z()w6($i;Vbc%GWX8g<?TfDuIP', '$i;V'), [34])
    def test_case_2059(self):
        self.assertEqual(pattern_match('8DB&td$;sXsvmC\ryra.y"c--ofwgJ_$rF"qC""\\&U1d/Pu,8}g"', 'Pu,'), [44])
    def test_case_2060(self):
        self.assertEqual(pattern_match('bV)1?\x08-CpOPG[R;O@r\x0c2\t1uVdf2]H-z\\`p`=+^M\nfmv\\\tlan@4x(S&\n}|Ees Swz\r(h@u{]L.%', '@u{]L'), [67])
    def test_case_2061(self):
        self.assertEqual(pattern_match('E[}0qH[\t5(\tFPMBT/aI|5F1?0kcx5:_\r;1M4D]Bp/qX?*D!(:hNJb(d<::3K9gfGe\\5ycFi+v.\r?\x0cJxkK".', ']Bp/q'), [37])
    def test_case_2062(self):
        self.assertEqual(pattern_match('qqOdQ\x0b\'3Q\tSGb@CTD MRY2,G}rdY1yv#2+SpE&\tu-;=O)7o"+h|j', 'OdQ'), [2])
    def test_case_2063(self):
        self.assertEqual(pattern_match('B\r\x08;G.v9\n+0j$soD~Uoa;f/#4AS!dt-QW\rbMc2h\nSdM\nL/}9)C!+D.83u6VvsU-\x08BrR1(/vxzbf~K*Qc%!|7[\x085Q', '-QW\rb'), [30])
    def test_case_2064(self):
        self.assertEqual(pattern_match('\\XS\x08"l)6\nhE`\x08.!\tiF$)2$G+cV\x0cV</IU@5kTh0/J~@?#IR\\8$\x08\x0b57V3c?YJ|@\'ec;L\r}Xw5OG]Gr33p\\T|\'o.E)Jv', '0/J'), [37])
    def test_case_2065(self):
        self.assertEqual(pattern_match('"rXVCL!bI^2O\nXEzUZ\x08@\'\rD3A-B&0o0Ow.U9\'w$y9Mi`Zw;M~5(Hg.Q3\x08J"{C8stG|@"a:H2Hjlm!*hU', ';M~5(H'), [46])
    def test_case_2066(self):
        self.assertEqual(pattern_match('.ic:4\n\tEdAD(0-Gc{]xBu6E;U]+Zk;LXpF\x0cHM"zei]$.N\x0bZj}[Qxn', ']+Zk;L'), [25])
    def test_case_2067(self):
        self.assertEqual(pattern_match(':\x0clbl4uuCgZ[0_(T:Kq6bi6[J|wMC(UY#;V|WLy_#w$ji\x0bsv!rwQAGj=kT,\x0c&<j-8\n{)o\x0bO&b<!E]o-Lq{NA@m2}/l', ']o-L'), [76])
    def test_case_2068(self):
        self.assertEqual(pattern_match('@?7LsHu=S:n08\x0cY"l9_T2o\'bP5r4UC%[M3!Pr9by&secT"8}o0JMGjmO8&>z\'Xrn8', '3!P'), [33])
    def test_case_2069(self):
        self.assertEqual(pattern_match("<$$wH/V^gOO`I ;aJTK7fH@^P&f!n>0gJ\x0bXV'p}m0#u^7o:=D6iN*IeJ\tr.[VNY/P#\tDr}5c", '7fH@^'), [19])
    def test_case_2070(self):
        self.assertEqual(pattern_match("<C$D2II of~-3OjNefXiRux2-.WTOy<c=TVjx\\tk~u$Z\nhupy\r#yoC\x0cwh~'Zj{@t", 'yoC'), [51])
    def test_case_2071(self):
        self.assertEqual(pattern_match('!h9]=>*9Q7Gs\rl6!l@Ph\x0b47G_m1NH+r8PY>3]CbW"\rZhrlO*T_+!US]Qa.ICVW=Ld\']X=`3boECw1\x08o', 'Gs\rl6'), [10])
    def test_case_2072(self):
        self.assertEqual(pattern_match('(\x0bR*h"WQF\x08r2/(\nnEV>\\&5W \t4\t\x0c\x0b+6\tOIIi)??:S~x-\tr]1rA1/8c#rnLg|gK', 'A1/8c#'), [49])
    def test_case_2073(self):
        self.assertEqual(pattern_match('?_@wVELjuHK/k\x0b7@qAre<Bf".Vw2(r)<;\x0cX\'-nT}u`BfD2+\nX1WSri |q:2prJ}T&D\\G', 'wVELju'), [3])
    def test_case_2074(self):
        self.assertEqual(pattern_match('&Xs"@+(iD@<0?b #;f?O8i{`k:*b78V8K(TSV%H-[5>YeukS] jU1Pv^t\nc*fXFT', 'b78V'), [27])
    def test_case_2075(self):
        self.assertEqual(pattern_match("w'rE\n4\n/Y=.G~'G-Cg5\n>Sf\r]vft?<-Fij)WAl4}.t5>XN\\tCbF?g(\\Q}oX", 'Y=.'), [8])
    def test_case_2076(self):
        self.assertEqual(pattern_match('H2U*i K|~@wW}-*E%[)7^=KdiQW)/\\388jiCxKI.bM\t&O>#fn]', '}-*E%['), [12])
    def test_case_2077(self):
        self.assertEqual(pattern_match('\t+c,yFlsG[=7YhH@=UrQ~?Y/\x0chH60\n%ktGU3+tw4AK44^Yye\\D\\[f@`n$._n', 'rQ~?Y'), [18])
    def test_case_2078(self):
        self.assertEqual(pattern_match("T\t6~ {n+\x0c!&!u+n;904B#n\nw?SlS0#%B&k7\x0cVeY.4M|r PZ#sJ\tC)&/v_bh#ASXHK8Sg_\rjyxq([\t,}Tb'2v2", '#sJ\t'), [47])
    def test_case_2079(self):
        self.assertEqual(pattern_match("%CXWOk/{qrZp^0!nKR\n6B4cHFS1x5w(nCow&NxY6R7zuh.^,/6YZ\\D^9{%Gzl\r9\t\tE:hHT*}ATeH96X-Gk$'}M", '\tE:'), [64])
    def test_case_2080(self):
        self.assertEqual(pattern_match('SKdL;poz&9ETy\x0b:rh0=PLe5573]SC\\BJhEj+;t#h)Y7,h\r<v/]vM&n,j7iyvj46yr_~)d`TU^B>#|r&{H~', '^B>#'), [72])
    def test_case_2081(self):
        self.assertEqual(pattern_match('(x$PNd=Yk\rV]v\x0bVH\rLCxesR9\r\tLC& 30RnFS8YeYv\nZ^-RmC(q:I?|4\nY{\x0czf\n}]iWK', '(x$PN'), [0])
    def test_case_2082(self):
        self.assertEqual(pattern_match('R.\\:gR/G\n\'iHV{Ik;<#vP}\x0c/1^[Pi0^R,\'EX\'\r7Eo/2UL<ny0\'&avj\x0c5YDQ>\n5iea:}:d9Q [XB<"t#8Y$%\'-DkTQ=%`(GM*D', '\r7Eo/2'), [37])
    def test_case_2083(self):
        self.assertEqual(pattern_match("*`\t~VCB$Hm4*dFa?36'm70@*QXgq71L2dD]Zc~F*^cqMye !NZ", '2dD]Zc'), [31])
    def test_case_2084(self):
        self.assertEqual(pattern_match('HCKFpMb!o\n\ntcyZ$HV[\x0b~Xe+kaLM.ARCDB2L%65\'pq{L<2s"}-i\x0bcGGK4B,eU?y5+1\x0b+\x0bV[a/TI&)P83(hj;\x0cgKn@tIO@', 'DB2'), [32])
    def test_case_2085(self):
        self.assertEqual(pattern_match('s}\nKjVUx6\r:?h\x0b]( "e7z-6pO(jY\x08D}&Vfe}uq1L9^mnxd bJP>ac[{=K>Yi\x0b7\\&[F*C30y|tI8i\'Gu`\n-Twi<\x0cM1Z2', 'jVU'), [4])
    def test_case_2086(self):
        self.assertEqual(pattern_match('\x0b6\x0cSc&?f;S&\x08\nniH8?6CHON"0msOw/+a7_,>(ypU{*`~)1vM/sh!*Gs4D3})H\\EI<tFVPc\\&_lJA}>DZk\x0cW5}[X\nC7#R)Oi.s', 'A}>DZk'), [75])
    def test_case_2087(self):
        self.assertEqual(pattern_match('lTj.%Ud7DS WS!3%ehyuo}}T(LOc\x08x"jUeaRiHICI<0&\tZ!_0<!o7.\rAPuz', 'j.%Ud7'), [2])
    def test_case_2088(self):
        self.assertEqual(pattern_match('k?\x08\'5a&Ojz\x0cdp_QiJdyVd<eeyrvg`\x086V%\neGQJ>~y\x08o5q?LYBK\\^\'<qzLb"z02_0PdP72O[B+B', '2O[B+'), [68])
    def test_case_2089(self):
        self.assertEqual(pattern_match('^O"63uK8jun>qk\nUV Wb[(OJvDe-6.S#-y!,A?*;fjnS%(]Clj90w7ckMeTaXIbw b%V\x0c(Wi\x0bqR6L.jHst3?=y]}0.6Kfyj 3~', 'j90w'), [49])
    def test_case_2090(self):
        self.assertEqual(pattern_match('6J.\\Gm7\x0ct~e#"7wCz\x08@s\r]19\x0cfe:4\rM%\tV4(4Lbv#!e\\SR &1t{r', '.\\Gm7\x0c'), [2])
    def test_case_2091(self):
        self.assertEqual(pattern_match('j,\ttgf]k04I$on"\'qxTLI(d@7\x0cP i`+Fi=\tXC@=\n\x08b7>7hC\x08&\rb_!NfaT4h^NQ_@Bf6\t1NC\x08G\tB>R>q\rO^oRNq', 'P i`+F'), [26])
    def test_case_2092(self):
        self.assertEqual(pattern_match("Smv(i\\szu<c^/[Zo'=SW>#PNA^,PH\\zA~z}v/\rf9^mlc7\x08\n(8\x0cUfKle3)aK$X\n_OV~fNgE%f4=~HBov", 'W>#PN'), [19])
    def test_case_2093(self):
        self.assertEqual(pattern_match('}KwDz0.HN4\\e6pDRaVxt[(Ur{4Z ob3I^W3aktm{)kNN(dd(MnV5sK', 'HN4\\'), [7])
    def test_case_2094(self):
        self.assertEqual(pattern_match('r$:#=\ts\x0c]+4XKUVE7V:%?agotrH21}zGVdp\r-.c$K5`ar(@.Z(=$;ku<:9Q3Ypz\nrTbS8!>J|JTK3/jE\r$#`', 'dp\r'), [33])
    def test_case_2095(self):
        self.assertEqual(pattern_match('CbCM)\t0NT2vF7r`mD a9JaID2SQ8JAu]O.B oF77QGuwE?_|&HTKm<"YTiv$cVCoxcF.E2y7\n)33\\J6[.Q,', 'Q8J'), [26])
    def test_case_2096(self):
        self.assertEqual(pattern_match('ZM!#e6<o\x0ck/sd$4S&J<eU4jcW#D70}z\\2ZC*ZW$pjl[fvMF`\nZK5r,y~c66+\tadq^\x0cI\x0bz3}x{@^{v[+3q(K+i|;V\nX', 'sd$4S'), [11])
    def test_case_2097(self):
        self.assertEqual(pattern_match('dgE\r~H\x08s:C*M?]_\x08v8*aFZ@BwQN`pjH Dy+&;\x0cf)~usB3-Ud5x@Z}8R|[`\nTZ!@2|^6TGG\r*k84sO.', 'v8*aFZ'), [16])
    def test_case_2098(self):
        self.assertEqual(pattern_match('`yc{qGB8IBj+leH\x0b4;0s}d:euR](98N5S\x0cN*P#/a~hWu_`\x0c~zX|=%c,\x08$Bz_dOty,xx[)&', '~zX|=%'), [47])
    def test_case_2099(self):
        self.assertEqual(pattern_match("'(`v\x0bVM1|&Jk,u|xyXXs\x08)gN-}S02[1A.Kdhz,lyGyiZzOpG*wp%>S\t\x08d9*\x0bVi~8.g&DcF", 'S\t\x08d9'), [53])
    def test_case_2100(self):
        self.assertEqual(pattern_match('\x0bQw-t>M\x08L.P;[n\x0bE8p0(\na9w"(\n)K\x0c@oIQ:[%l"hT_>>\x0bJ?E10\x0c!|~JfVRq]\x0bTo\x08~@+`e\tJlt\'NbE$gOq', 'L.P;'), [8])
    def test_case_2101(self):
        self.assertEqual(pattern_match('o@\x0c(2YX>LD16hZ=&kBQp_} 8|&fK2{&IJLf~/t$r4S5Uw[C]`Z+tz\x08L>Xi9o=$5l/\r30[&6o*k-o', '&IJLf~'), [30])
    def test_case_2102(self):
        self.assertEqual(pattern_match('R6}QqhM}Pr:01I%4eg`5$.Bn8,~\x0bHQjkZ"QzH[Yc&GIOWuhkjo\\Qzdj0.\rQ\x0cE3.i`&\'S', 'Yc&GIO'), [38])
    def test_case_2103(self):
        self.assertEqual(pattern_match('.CYo5GT7kts5?6|wIV%yZ"Y[a#U7PM(XQaqFyB*ms}6$9KrVI#|QDD N', '6$9Kr'), [42])
    def test_case_2104(self):
        self.assertEqual(pattern_match('\x0bQ"j\x0c&e@y> @*Rt\\9M;\x084GN&\ts,\'v,s3OfUA\\"%MfLf3A1?`7-xeP#e@Iba\'', '1?`7-x'), [45])
    def test_case_2105(self):
        self.assertEqual(pattern_match('YKj%;."W8M-~9t.B;$>V2:n]>}wbwB]-"l^Jqp_\'U2\\{&"u9zHjZ1=">\t4<8@xy`3>g%f', '>}w'), [24])
    def test_case_2106(self):
        self.assertEqual(pattern_match('\x0b)c;d5_TG};C3\r.$O<Z~y\t\r/B~\tHs\x0c8lk35aZ6Cja`\x08mL9Eob\r\t: wRTssY', '\x0b)c;d'), [0])
    def test_case_2107(self):
        self.assertEqual(pattern_match(".IDlgk8d~:5+(u4a6v#zC1zxH>BW6%p'h>ax7ZOi=KQ\nPmb`9G,w-oZt>\\n3c\rwKj", 'C1zx'), [20])
    def test_case_2108(self):
        self.assertEqual(pattern_match('o<u\nF{#`\\\r7e!igk99;\\BKw_D0`\t+\x0c/9;~b|cndr3XnLP.vSrda1x\r0|vH\'L $8$9FgyGK+\\c?85|7HgYBsa/xpMH!"QdwKzN0', 'BKw_D0'), [20])
    def test_case_2109(self):
        self.assertEqual(pattern_match("\x08?@9z*V2\x0b,~hkV\r:IM\n~K\r,pz~~hpxV_)zq(HL^k|B\x0c\x0b!8]TD[f$I*bq6\\1y_cry/'Zn8V=w4@J'", "'Zn8V"), [65])
    def test_case_2110(self):
        self.assertEqual(pattern_match('\\E3`Djntn=[ZGN?$6%\n{2%r?\t(=!qZg&5%\x08KdicJ+O(5r-|kd,Z:]F\nJyxdX=uHj9\x0c}-?RGj\tp>2,aI`$\tKy-wr\rSQ&]D]9j', '=[ZG'), [9])
    def test_case_2111(self):
        self.assertEqual(pattern_match(':\rb),\x0b?&\r<Gh{\tA<6^2RwN69GYs\ttQ,sXa\rT\n4>^tU,,Hx=K\x0bFTqPAgz!l\n&-', 'wN69'), [20])
    def test_case_2112(self):
        self.assertEqual(pattern_match('}}@\x08:({Oh";eA\n)poz\r@9"[;He\'9IGQ\n7!R[%6\\73UOjt\r6\t,[cXR(9\x0bu%2!z6DLh*z{pI[', '2!z6DL'), [58])
    def test_case_2113(self):
        self.assertEqual(pattern_match('tsG!VB@RixsV\t;cwy@Y%Fm[/kW\n\x0cw+|\x087&(/[|K<%\t8z}7U\rt{$6341,\\Y(]6uBO', '41,'), [53])
    def test_case_2114(self):
        self.assertEqual(pattern_match("a,bxm/8#ha#M<H|Si\\CX#SQ-)o)'Xwd6o9$2`}vd{EC.G\r3@Pkup,PM?_\tIK*EJ9uNXSL7^%y!|D\ne_/+?amR", 'H|S'), [13])
    def test_case_2115(self):
        self.assertEqual(pattern_match('$L|qY*Q-AD;\x0c2o21F|nO|vIRNW[0i(R""II2o,sjo.}1R`#_19{Hx\\lM1=\x08}"0vu}8~&BA0~9cdIo5zwa5T\r94^\x0c3_>(_y}=f\nZx', '"II2o'), [32])
    def test_case_2116(self):
        self.assertEqual(pattern_match('Bf*ej;ezG1Y%\nG9#Bj++]W5;yO=\\ KWk Gx!,7\'#\x08$\r4""?as&oJNQTNB[FE;/mFN[z#b,9>?j]0UhPD]', 'oJN'), [50])
    def test_case_2117(self):
        self.assertEqual(pattern_match('*C3\\e@|!"Y=$oW9\\(3GM@\tJh=QWeuJ,x4^SV\rV#%rXRZv&i ATwO_vPg\nmC9E\'~1OXX&4Qb0ck*jf`@t"QXheRAeS:Z-<', 'k*jf`'), [73])
    def test_case_2118(self):
        self.assertEqual(pattern_match('y2\n\npc`DhR\x0bi1Hc#+,.vf6*\x0cr\x0b)+Z|di@%/Mi8qIH]^<vPy\\0IY/K<AzsE\x0c\rFh9xL', 'hR\x0b'), [8])
    def test_case_2119(self):
        self.assertEqual(pattern_match(' `Y2*j,/#bX|QPatzz*Jh!$Eg,g,^.Q_ULIF#3ynhb:*iqT"#59; ,\'JTr/(!Av\x0b\t_?\n<\nL=\x0b7GE/.8[[6', "'JTr"), [54])
    def test_case_2120(self):
        self.assertEqual(pattern_match(">FJ0$%*t`)];?K=86G\x08~Ir-\\#b<2,{9\x0bcp|qH$x2KrE\\d^GwGJL|U9nzK_8x)A'A_U`Y:mvwx13,?Q#", 'K_8x)A'), [56])
    def test_case_2121(self):
        self.assertEqual(pattern_match('Xfh*gT@=G[#__s\t\t+\x08\n3T^j\\!n^a{naZSeM\\DeAv N9\x0b[V~%Q1#eC9Jay4@cDk9qqu4>THd\nzJ8].@8+jB3W(A$NNg<[:e47Ly', 'd\nzJ8'), [70])
    def test_case_2122(self):
        self.assertEqual(pattern_match('A4b{g_~zd6n{r)Hc#cp\\_=7BW::XdrxC~K\\p4\x0c\x0b0\t?foUb@h<?w`qQW}\t`6)-YTg3|xU\x0bI}c&4Xu}RuP$(\t!uG$fi6&&{`', '$fi'), [86])
    def test_case_2123(self):
        self.assertEqual(pattern_match('Ro4D,+\\YZR%dI#xM|*1a=34wJe hL0g7}D|[6\nMqe$Z !P/\\F$lqz;P3PE+d7b\x0b.T=M|ng}`d[_\t74A', 'qz;P'), [51])
    def test_case_2124(self):
        self.assertEqual(pattern_match('\x08zm,Y\'Um&qL+jr#QR"[/6JxA4bjun\'#Po01yTS!EpYC2/gySIq;aYDU,kE>', 'Po01yT'), [31])
    def test_case_2125(self):
        self.assertEqual(pattern_match("'ic+[WDZ.iy }{IJ!\x08nr\x08=x\r+;m0XQ<6wI=A~~U[\x08D,R>Hp\x08vWm`T\rO7t#O5rKLK8d9[?+5_[\x0b(ec?^r)", '=A~~'), [34])
    def test_case_2126(self):
        self.assertEqual(pattern_match("/VMHfh;Po\x0b BEk'xA1imqNre%!2W8(\n+\tjC4$/WB$i&xVv[iqWckJ%RCW>~>YbnYgeVv?[tc(LC$l?l.1Uk0?N6yw6D+\\NW{Z", 'v?[t'), [67])
    def test_case_2127(self):
        self.assertEqual(pattern_match("iU)j.c$K\nh\rI[ <'T\x0cB!%\x08t*~*\r3\rnvS^)a(\\\t,Gaah_b\tr\x0bO$>^ry9\r,E*\\+iq?{k4eBM\x0c[LLwK|v2]=-mkJxK y/>k", '\r,E*\\+'), [55])
    def test_case_2128(self):
        self.assertEqual(pattern_match("H<Tt!%lp+@q7Pp\x08J/M-[Wz\rPT8%*H4mlS?Q2`\n]'o:B\n*,){Fz~drvK", 'o:B'), [40])
    def test_case_2129(self):
        self.assertEqual(pattern_match("[5gN]Iv]g\tY\x0bw;.Ib:`>,\\8,!(Z~F1xM3@g2&,1 XE\\${'M<Kb=9XI6N6#\tpWC;vL1w`AgSNP]-}k\n,\x0bDWyz*\\Rdrxlsi\x08-w", '\tpW'), [58])
    def test_case_2130(self):
        self.assertEqual(pattern_match('L1dMe\x0b.Y0PK.Ws_\x08k`7\x0b+|qv\\,*:5#p\x08"m9ACAi)Kz)a~%vlpq@@]-W\t-,\nUua5sN+GA\x08Ak5*ub', ']-W\t-,'), [52])
    def test_case_2131(self):
        self.assertEqual(pattern_match('D.w$;PX}wd?Glk2{"i+`tZecP@]w k]bJH4$mD,|I\x0cnjx*\x08bUW_QzA;|ReOu\x0b0', '`tZe'), [19])
    def test_case_2132(self):
        self.assertEqual(pattern_match('ut\x0b\t$Og7hXk(E.\x08{o\x0c2_f%\x08q-GNus"`Q.AJj9<38Voh|6Q\n(\rq)106>>`=q,rdN!E0QHHX)cV\x0bl6#F&SEqf;E_V-:5wy;"', 'h|6Q'), [42])
    def test_case_2133(self):
        self.assertEqual(pattern_match(']:-C\x08a,|C\\i2(=SK-+<=*x<OS-v^,^-m\nmiUft\rcq"M{9Z+O[\x0b"8\\K_3[.N%32~%(OYf7A\'#u\r3}Xg', 'v^,^-'), [26])
    def test_case_2134(self):
        self.assertEqual(pattern_match('O^O4(O[;OSk+\x0cHQ@yO\x0b.8 $L\\w<#TCF"r2~S8^^o{bcV6EJSHwG{U>Z\n\\b\\a$', '4(O['), [3])
    def test_case_2135(self):
        self.assertEqual(pattern_match('6"os"YcR :l\x0cB%&t^Zuz~W\\`ABg!~Nd;`\x0bGuzlJZ3cOrU|5s5Objx[{;|\'-Y4NsG:PMG\n~SThi(\r2LYx|4D\'KA^G\rHflY\x08Rj', 'cOrU|5'), [41])
    def test_case_2136(self):
        self.assertEqual(pattern_match('lt*\\wsZ7O{;uTE7#?QwQ!48J3ld"BE/Ky]j~gtzDa\x0bS\x0bB~-D^aI8HsrP6RGmL603\n\x0c|"`xV:&kAyf?ECD~mbSU$W((K|exT', '8J3ld'), [22])
    def test_case_2137(self):
        self.assertEqual(pattern_match("bu#T| 1O~pC&&Y}SCz@Kl^mQ(?6b0P{;\n \x08NPn/E*qMF]0`l,'", '/E*q'), [38])
    def test_case_2138(self):
        self.assertEqual(pattern_match("I E1TX(7VbBH|s/bQ'FEfjXf]G8Z.1'X\\\x08a+AMG\x083]@YaL&\\r\r<\t-2Zvh_Dy,@\n|\x0co8(8Ae3O$vZb-\x0b)xf=T%v)1ll`m", '8Ae'), [68])
    def test_case_2139(self):
        self.assertEqual(pattern_match('?J]I\x08m_2]?FP\x0b?s|[|AZ<KW6:~uTv-7qTs.X"e.Te\'),Zd,u~FrD\n\n{d4E{+YegWP\tJa\nWWtDN~CO{6t\n3N>vf=i;8Z8', "Te'),Z"), [39])
    def test_case_2140(self):
        self.assertEqual(pattern_match('_ny`!yC"n.hCm"`K"<(53=Ug\'$BeqK|3P?C,~%JM*9VcO*MOW{dXl-Ak.Zfr0o>oE^ek$', 'hCm'), [10])
    def test_case_2141(self):
        self.assertEqual(pattern_match('g=|$!NJ%b?+5sG\nFt\r"c.U6SP(.o<WE4^J*yRB7mB~OA86c_\x0cU2?0>./_', '86c'), [44])
    def test_case_2142(self):
        self.assertEqual(pattern_match('1?wI3ZQg5l?k]\\.+<k#J^#][a6C!q9rf\\n3CIQs p1\re*R|3J\tAyfHYymz[J&,G\\ESD7vM:<qGB\x08L$-6|+OX\n', '\\n3'), [32])
    def test_case_2143(self):
        self.assertEqual(pattern_match('Z>OreM5:gijl\x0b_[\x08\nSpxEH={p<sqZ{vz03A4iR/\n+MeZ,v.H/\x0b\' "S|Q[<SJm]OENkn~E@2t(rJ}BN)7Eh!p=C\x08}.|\'BtL(Q\\y', '03A4'), [32])
    def test_case_2144(self):
        self.assertEqual(pattern_match("+P|j]\rj;+HVh/2{T}kd8\\hfQT^SfU.R}`jtj%KU@Obkh#|?\n}rh\x0c3P\x0cz'I@359.5,}&cG`\n_3q", '/2{T}'), [12])
    def test_case_2145(self):
        self.assertEqual(pattern_match('\x08QLeHZOWTbq7Q\\xSaj03H*S,UVQR~G\\D{B\x0cplHfgRV(\x0c_@;/dhm*rVC~Wp,lL\x08{l[c*TlZDH\n', 'bq7Q\\'), [9])
    def test_case_2146(self):
        self.assertEqual(pattern_match("D?d%q:p](W&?yx\x0b:m<UWNGgqLqB-9)J}sl)WZM,P=t/t\n@U>6\x0c3'BI~N}.7O(:O\x08GFR_a >:\thhn-,,A=_-0|w$h:X|7LLU#", 'O\x08GFR_'), [62])
    def test_case_2147(self):
        self.assertEqual(pattern_match('dG|lRYQk4*{b{rO}\r`&m)m1aE{&27s7(Exx7Fc:M2,a\x0ceh9<B2*4$(\'fr"8N S4F[I\nyd2\\a&-0e\'Y6D6+4YtD?&dUUj}', "$('f"), [52])
    def test_case_2148(self):
        self.assertEqual(pattern_match("<@KIhxuj&Y'zO5iTRpyeJ)qJi\\{(|#N!(20(b0d6kAd7P1U\x0c~3", '{(|#'), [26])
    def test_case_2149(self):
        self.assertEqual(pattern_match('Se%aYJGZG\t)N8cp\r5XW[:=3_7-\r/XCQ\x08Why{W26 r68A>W\x08Qsbt$^PF<R\rKM (oFE792-', 'Q\x08Why'), [30])
    def test_case_2150(self):
        self.assertEqual(pattern_match('6X^h4x1kf4;<BMkQBv^<B3Dj".u]DxyHr2#.1\'5vk9?J\nlvYv\x0bSIq\x0baV;(', '\nlvYv'), [44])
    def test_case_2151(self):
        self.assertEqual(pattern_match('DSoj0-BI\x08y;BUXxgti#M2\t@/\t~qi\n{9_"&\r\'o7Ogn\x0bj~\tkMSope:4<hsno=Baj=\x08', 'n\x0bj~'), [40])
    def test_case_2152(self):
        self.assertEqual(pattern_match('(..}1:Zvff@gyvz%{(I\n ,.(BmJ|]ye+IE\x0bL;xE S\t=\tz0O:]\x0b.5-&el,K<PcBaVZ\ryEF;\nsZns!("\x0bz', 'BmJ|]y'), [24])
    def test_case_2153(self):
        self.assertEqual(pattern_match('31fJFr]t&8mh }XeJ1[=`i\\\x0bA\x0bqLKe<~KyIO+ ?bXUQV/Owxuq(E\x0b\x08Bhf^Yl&D', 'JFr'), [3])
    def test_case_2154(self):
        self.assertEqual(pattern_match("'W4`nu2xVYLk<SURwFcL@+KRu~T5dkU\x0bnEP!<R\nX4?iR\x08!y=F;G$z7*LbXg^Yr\\I#ZTX7./", 'EP!'), [33])
    def test_case_2155(self):
        self.assertEqual(pattern_match('\x08Chj4I<y~{_WR8\t@?8i6;T]o[3w%rI0]ay\x0cS7G%x&@ta){@^p2{MPa()C=L}BYDS3@te[ZB>q]>4Zp(}^&4$a\\|@r"F]y0q|36s', 'w%rI'), [26])
    def test_case_2156(self):
        self.assertEqual(pattern_match('\nzuMe7S9Uty;mFl.DkF3@]\n1Sh=;C*"ka?LHGg|X"]J\x08,#\x08}r%*((Q)<<wR wxl\\b{TFvW9>r', '@]\n1S'), [20])
    def test_case_2157(self):
        self.assertEqual(pattern_match('Ia{|mamt,/z;HDK\x08-}L2!<pJ|JI:z:%G"wwJ*?@#NNkRh\rfd(Z*c\t$W-vuE(1V\'i-U|~2<]8][%9-BY<*X%\x0cbHqkl<l$7566h', 'L2!<pJ'), [18])
    def test_case_2158(self):
        self.assertEqual(pattern_match('\\R663ePpwgrN9lz;~hMf#:O92o~C9 n{#v:*[sy\rrb^w=21oJeU<Lx\x0b5Es|!{n\tSs\\1l_|qx', '{n\t'), [60])
    def test_case_2159(self):
        self.assertEqual(pattern_match('\x08YlfC|d\r1!\\HqFihUq@Q6Of>Et+`W&6\n}3\r.cPW0>TU#s9aXo733FZ.h/wy\t@', '\n}3\r.c'), [31])
    def test_case_2160(self):
        self.assertEqual(pattern_match('KCsmV8AtP;A\n:$<xJ_4{`~=:Bshi,Tg2F3EL/^*Tx<Nm21Ah&[+bN\\jK1\n]ql{cZb', 'L/^*T'), [35])
    def test_case_2161(self):
        self.assertEqual(pattern_match('\nB5#g-%Zg_@z\'\x0c7yZ\'-G""b@Tv+dB0U\'H\'*1Ij[4b^!%m\\xo\x08pOd_M4\x0bKW', '\x0c7y'), [13])
    def test_case_2162(self):
        self.assertEqual(pattern_match('BJ_k$<>w$rFK*7~b@3}f"e/g2imvf"w=!-yBwkyDFswO"Q&,y(Ay6J\t gVlV.K)8+oj9*%Kh', '"Q&,y('), [44])
    def test_case_2163(self):
        self.assertEqual(pattern_match('a{TLSy:YZA\\-jwZ\'_vu)iF]6lr^`OCQ\x0cSj5+CWt7yQ<LWd2%At\x0ca\r$9qWp<|]\x0cjLL\t0md&JkzT_")oBDT\\', '+CWt7y'), [35])
    def test_case_2164(self):
        self.assertEqual(pattern_match('JrIv1<(t{X(5Ivh_*3coX@r7}=L7[rJd2reewG+1\'Q\nZh_v?p.0P.\r:_CIWRe;)lL4L"lzUT\x0c\\~Fp%', 'v?p'), [46])
    def test_case_2165(self):
        self.assertEqual(pattern_match('\rBB-\\\\\\*kxYvA^ !\x0b^\\aWh8-$Ro&8IV#F3"Ijn\\XL}00>]Dz$\t)v_oe?twt\'[F.FERQ3lqd :s0]KF_-&t&8', 'o&8IV#'), [26])
    def test_case_2166(self):
        self.assertEqual(pattern_match("\tnrP\t@uS-l@Nf|2'\x0c\x0b_D\x08*R l1 blNY*ZdL\nS7E[u?\t(7|Tri5W*R1M@\x0b6j+3;", 'nrP\t@u'), [1])
    def test_case_2167(self):
        self.assertEqual(pattern_match('c1wRd1Q>_w%*\n!p(mf.\x0b_ZsrpAv7-6t\x08z8@\x0cb\n-i\x0b%j#_>\x0btF0=\t<@x\x0b6', 'p(mf.'), [14])
    def test_case_2168(self):
        self.assertEqual(pattern_match("\n8k;CwP6_pw-`B1Py<\\j\t;IXVhf7Wm-WSNf3qb&2/@'\x0cuP\\P$5FXz`>\x08R[!Qay\r@E:LJo'", 'hf7W'), [25])
    def test_case_2169(self):
        self.assertEqual(pattern_match('w\\\x08\n9Aytjd\tl1<k#`5{9!d5Hv9$M`2EFKf-rj=3`uhFT<[`#Ah=\x0bC\x0cQNI`??(3\x08tNc]H', '$M`2'), [26])
    def test_case_2170(self):
        self.assertEqual(pattern_match(' v1j$&r"f\nMD:-~V=6/xLXqWCBG_rB?TaI\r8d\'xCcequ~CWsOrm|%3Px_\'ieSv(vFC>Qa', '(vFC'), [62])
    def test_case_2171(self):
        self.assertEqual(pattern_match('\\kZ24o9YZZx$DU[p[?fak3{,*{hMKRzb.s87p~6oX\\ 1X2q`P65kX]6Dli90CI#vd5BD%BFk-T;!98N\x0bXAW:^;hT;\x0bn|?B!\n0:\x0b!', 's87p~6'), [33])
    def test_case_2172(self):
        self.assertEqual(pattern_match('b_[8/RIf0h/b_VAd*X!aMREg~a7[Y4\x0b|\nSB1T28*<m=kEsb=xs:%%I{M=gW\'dT9g4RfJcr[T]|YWb"`\nlAm#c', '~a7[Y'), [24])
    def test_case_2173(self):
        self.assertEqual(pattern_match('pS8\x0bN)R\n8Q6||jO6r_&.fU>rD~HSOf"z;3dxm>\x0c*RwatL_;tpk)n5S\t7tpt-\nXz7t\tG/lhS', 'pS8\x0bN'), [0])
    def test_case_2174(self):
        self.assertEqual(pattern_match('(5C4bDw5{gnJ!naf*qFR{\t\rWeJ.j2+\t&\nawD6\r6.7L$;lm;~^BD:z3\x0cuyWkSxUk0<z_zV`$:<6{e/QH~j%/$WZ xyby+:"u4,', '5C4b'), [1])
    def test_case_2175(self):
        self.assertEqual(pattern_match('\t>6 ^vGp +;Sh\nTR\x0cKu|b\rH0RSYZ/f+KJP9J]Z}TBhDyh\rKlND|9!', '\rH0R'), [21])
    def test_case_2176(self):
        self.assertEqual(pattern_match("U/\\CV\nfbNdopU$6?{]BeX2-_C6GxsvP>\tO')U&LW7*K{\tmwbL$?\x0c1ch(l?ImA&B5E9)b{^L?=M5CTi|\nL", 'C6Gxs'), [24])
    def test_case_2177(self):
        self.assertEqual(pattern_match(' $>,~ecPf_8{TK*hM:nC"fCx)^} mRd<y0*gN)K\\McJ\'%4|hQ>]mjr)ipy\x088C=.>;4z^ Td/MC\x0bs*Fa7;h&9|@VD{2', '~ecPf'), [4])
    def test_case_2178(self):
        self.assertEqual(pattern_match(">T=#C7'!?\\0P}4&M#)sC#,\x0ctI#uwvhe.sz)<n?C7|_\t|hNWf</oE\tW~", 'hNWf</'), [44])
    def test_case_2179(self):
        self.assertEqual(pattern_match('rIfv;zOK.$}5=)z[s@tVln-E eK\x0c/?:#lRtphN\tcKe\r|7WeW^Hi(8=T,LnQ*NN/`Xrs5C', '\r|7'), [42])
    def test_case_2180(self):
        self.assertEqual(pattern_match('d2,3},6^yw\x08H9#.&Z?uq=Q\x0b~BYs.%)x~\x08yX Qj3<T&A{\tmd;u|o=E+\\v<r/_\x0bO}|Spj9I/eBAFi}yr-_gM\\[)4U(@', ';u|o=E'), [47])
    def test_case_2181(self):
        self.assertEqual(pattern_match('9 b\x0c/aau\n\x0bZ$a+Q)OwtiAw9}l*Y!6F.}\tpAXJn]\x0b#gMRMhU5CXN"b|XF\'(&;+]&X5"\t4\x0ck;Z. POF>zKp9YCdL1\x0bxHX', '\x0b#g'), [39])
    def test_case_2182(self):
        self.assertEqual(pattern_match(">EJCx}X(I{Y)5%c6L}am9N'3};sd0nnJcOrlK+WV^0V*iMoJW0'fn5Z\tGS\tSIG7%:Vog6=k2aHM8['+", "0'fn5Z"), [49])
    def test_case_2183(self):
        self.assertEqual(pattern_match('%/|(k%59ZW"R(G3Ara@bm4{g\rP\nqQ}Oys?]xJjxM7Tkns+!-$~\x0b%8a^+rb/dmHjUk,\x08*cI\x0bx!\x0bP)Rb?', '4{g\rP'), [21])
    def test_case_2184(self):
        self.assertEqual(pattern_match('W)\rM,xox\x0bW~J;Rc|v\x0caMs6\x08\rn+Vn5*?\rqej2a[cS:1&0.>5"`Z/I\'=1VYa~]]mO=(&&O(=AeM.b=r;', 'qej'), [32])
    def test_case_2185(self):
        self.assertEqual(pattern_match('d\\z~E!}!h)hETaqXubExAv&XKP_;Ke^D>[T(I|?hy:$hu4~6E7K', 'hETa'), [10])
    def test_case_2186(self):
        self.assertEqual(pattern_match('>1|1*e0CYZma @~Pkx5d*HDYci~ oS%)WAb-\\L-\t\t\x08UixvXpv<$N+8b\x0b];?V\n"vOq\n|\ntE]iF\'eDUZ_@,3S+e( .pi\t0m)x($i*', 'UZ_@,3'), [76])
    def test_case_2187(self):
        self.assertEqual(pattern_match('BNeP/*?SU)Q&$[/#9tNSX\'sJ\x0c\x0c\'z1~,c3-AZ O/;r8"BaL\'E+c O$lkF(:D-KIT\n= ?FH~\x08\x0c`', 'Q&$'), [10])
    def test_case_2188(self):
        self.assertEqual(pattern_match(':2^E5E{On]/SF:iep#&laUoY[yK%Y-2C_Y2>4\no\'QGkk"d.`PWA7Z~Lva;IP&\x08%"f;2@*vVOJ*!9}0WgeVzCg4G2t}4[U', '"d.`P'), [44])
    def test_case_2189(self):
        self.assertEqual(pattern_match('PBEnuijaDqY\\.aiRm)TA!h8i~%N6?+CDNdlS*>{06rO^q\\J$2~-@$W_,a*f,[QiS', 'BEn'), [1])
    def test_case_2190(self):
        self.assertEqual(pattern_match('$p&4kP\t3ufCR\x0cG"-N!\x08>F_gt`mB#ikj/oR]&>y6\x0b5!|>o*Mp?9[==Iax', ']&>y6'), [34])
    def test_case_2191(self):
        self.assertEqual(pattern_match("SyF_PjhHq)u0,\\{zeknbG'R4n\x0b#mwXq{\tM, ?xPqDvA!W(aJ3jk\x0bDcq7;@M!S8\tM]A5m07_^X*6[<BO\x0cS5#D4IY{(K5x{w", 'A!W('), [42])
    def test_case_2192(self):
        self.assertEqual(pattern_match('~5.X1$_\t42cZG\x0bod|#}%$z27v^!|8Lw+@\x0b2)\\"x4hbMy\rg0yg8!0u`sjw?Cuy03u<jDtR-i', 'Lw+@'), [29])
    def test_case_2193(self):
        self.assertEqual(pattern_match('!Q8rWZN^?&ub4Hjx}\tg^5>/FdB$"=1\r9v{/\x08 ntL5Fjr\'I@)]GskCM]?RuS{u%e9<\\wpQ`j>\r\x0bK 5]nYx_o"Gumwp', '"Gumwp'), [83])
    def test_case_2194(self):
        self.assertEqual(pattern_match('2J["9vFf?[N\t(b\x0bXh\'0 ~lRP/{cf!cm(zH#\nAkdADJu*jvKLPVp*Yf$V\x0crCI97)e<8835Xi', 'Ju*jvK'), [41])
    def test_case_2195(self):
        self.assertEqual(pattern_match("d&DlzC}q}s*:IO}\x08UsZwnhd{3\n^x(\x08\rR_@imuK!AL%\rUarGt_pK'\r1", '\n^x'), [25])
    def test_case_2196(self):
        self.assertEqual(pattern_match('Wus!}ku]%L#{uUJ!kn$*8\nd:Gd(3*\x0bs26464Uo8uFp_\x0b9,Mpq]%n$|tv?hp\tLwe', 'tv?hp\t'), [54])
    def test_case_2197(self):
        self.assertEqual(pattern_match('Y\x0b-Htu4eMM.9:U&yPc|16ZlB\x0b2>mijHin<`x\x0c\\~-T/ufYXcJo\nL\nUBQ__g\t[4#Je;-uV.:}g:oXya*A\tL', 'x\x0c\\~'), [35])
    def test_case_2198(self):
        self.assertEqual(pattern_match('Z`?nI%;rx?65r\'i~@{hY\x08)HD{_@@O}\nK@eoIy9MG3!Hoqm@cXw\x0c>gU/F2LW@,@K5)`:T\x0b?"qZqFf@v*x', '_@@O}'), [25])
    def test_case_2199(self):
        self.assertEqual(pattern_match('yMG"~z]\\jg0E\t^5mpt9na*7RP]ylJL[2 }PRHdML8kb!?ZU8pI\\nq V\nMRHHyP}Ol:B<Nd=D_!B\thR!1~.;K:tyui<?"55', 'i<?'), [88])
    def test_case_2200(self):
        self.assertEqual(pattern_match('\x0cs34\x08MSF,Z^OH)mq;hO&T_~@BObTX=KL\x0cU4W7So%}lV\\9hT6IoG%T^P%Z0{~s[Vh7^>FO x8)W*x', '9hT6Io'), [44])
    def test_case_2201(self):
        self.assertEqual(pattern_match('-Jzon3w-O1L3pN&)$uHv\x0bAmj*#AjL\t;^{8|~k#E38%;|\x0b\\MCM{/u V@b-IyX', 'v\x0bAmj*'), [19])
    def test_case_2202(self):
        self.assertEqual(pattern_match('"O;{m:d59FAs5BN5bi:O\x08r15u3sNOe|lw"R?:&z*\x0bzltelG#$($a%yH|jb_*sjHc8aIx^Uw\x08', '"R?:&'), [33])
    def test_case_2203(self):
        self.assertEqual(pattern_match("{&lmK:}eOv'Ot4g}b:O%4|,D2&[O(Fj$_hr-m\x0cY;M4zOm;6qB6s++jC1oA}\\<+'JBV:qV84O8\x0b", 'Ot4'), [11])
    def test_case_2204(self):
        self.assertEqual(pattern_match('XFs%(H?V!<eT-Q;+ub/w0R_C`:j-Q1~C+8T$P/z`2+\x0bie\\rC<o{@!', 'XFs'), [0])
    def test_case_2205(self):
        self.assertEqual(pattern_match(')dm#hw\t:FLycN~/z2D8hztFD\'u9r_=nb5|8"T{Zed4D9Y\t\x08)646\x0bf-7mwq{Mkv3RE9BuDE]3/I*L$e2', 'Mkv3R'), [59])
    def test_case_2206(self):
        self.assertEqual(pattern_match('2F>LHIDW5EO\'ABgH>"W00f>_tpVH2\x0cbqw\\BY\x0cg)m=rAm.g6Q@ooL"iZ\\\tg\x08by#UkQ-FR6\x0bi,qPCq"-I\'\r"Ty~otkd', 'm.g6Q@'), [43])
    def test_case_2207(self):
        self.assertEqual(pattern_match("HU|C-+LR}9.-R8BDh`[o8Gy):r}KNv'\rmD@vn:>dn\rHJ}Oqc\tbFJH4)GU:U*pC5 CJ(", 'Oqc\t'), [45])
    def test_case_2208(self):
        self.assertEqual(pattern_match('2<U\ruSv..U?o4-D`>eUS$\x0c\x0bD:\n.pJi.9@I9Y{\x08At$dX\t8#~\x08(z$t=-DS4ru\t-Z<tLVjZ', '>eUS$\x0c'), [16])
    def test_case_2209(self):
        self.assertEqual(pattern_match('\n3^i4ly$UM9F5*|h0hA(EQ6\x0c(h6&i%U;S`Fp\rm@?R:(vsth\\ck] bH&@`od&\\', 'ck]'), [48])
    def test_case_2210(self):
        self.assertEqual(pattern_match(';+7bwjp7Qx0tIh~I:\x080\tzzpCc4Ng4:D;e\'x\x0c\x0cs\\EoO}P\rN0he6U\t"P2 %acEJTu4', 'Qx0t'), [8])
    def test_case_2211(self):
        self.assertEqual(pattern_match(']cIQ9W1dP@\x0bu5"Uf#dijIfHDDk7V/9|;P5%3Q?IT\x08O=8;l6WR\'_w\nBg/RtFDc"jrhtrQJ\r"', 'Dc"j'), [59])
    def test_case_2212(self):
        self.assertEqual(pattern_match("yWC6}<K\t[[4-D>;*hxH(sXhQA\x08=ux{yJK)3f\\\x0bk?Cq~4sP]mU\nY\nc+`I%U\\bILH&6f{+o7'`aVTaa*_c|B?`#B-", '-D>'), [11])
    def test_case_2213(self):
        self.assertEqual(pattern_match('K,Evm|"[Npk`\x0c9lr-{Mx}NM$PJep\n1x.3}ZRPH} YL0EO}GUDG+6;7Lq?]"XJyZ|BD8h_dyw?HB)*\t%m\\"\';xgD)?Zk2', 'NM$PJe'), [21])
    def test_case_2214(self):
        self.assertEqual(pattern_match('^pVw)075$E%*W-n!MT\x08rp#l?7FFp9!6`@"(,#j!\nML5{%E\x08!\x0b43f]"GEUSn`\x0bJxiR+P', 'w)07'), [3])
    def test_case_2215(self):
        self.assertEqual(pattern_match('!l<y7A\nYiL-Hm,\tbr]Ucu=|V+.kG;Q PY\x082vS-{wYB\x0bDH\t\r\nd5(7tD UR[c\x0cN ^$<hzL.\\)v"\x0bvc{_55e=V1q-7 xZ!*\t09$1AS', 'PY\x08'), [31])
    def test_case_2216(self):
        self.assertEqual(pattern_match("fn\t[l'a%y~Ws|Sa\r/H\t7\r:H:8A0IRc\r9?[aI-{-\nx>_/U;?Qp^3 k+ak;< 0PlZ:]]0SL.d O7qs]wgay?9bMT6$&Zlo\x081", 'k+a'), [52])
    def test_case_2217(self):
        self.assertEqual(pattern_match('n]*lFE{:3x-M|&5)$\t Z3#A\x0bXe`0$[j|q9v"Ehg!vp]*\rz0l>$p\r1pd04$+}je+@:x*h,', 'FE{:'), [4])
    def test_case_2218(self):
        self.assertEqual(pattern_match("x\rW!\x08Rub$wA1]Lz|:h'+If]U\tf`+Xz;\x0c\x0bCjBnvM;6LIBn~]j_F`T\x08~\rstqc\x0bRp<|y<j`4M~", '<|y<'), [62])
    def test_case_2219(self):
        self.assertEqual(pattern_match('P"T<}Q\n Q5k08QF^X7UPnv50\x0b1omn>gdH ,IU\t)ikwcz4*MgqA6#tcJ/ux\x0bdN\r&-V\x0b{fpWQk1[55w!x?:\t~0jE}b', 'v50\x0b1'), [21])
    def test_case_2220(self):
        self.assertEqual(pattern_match("\t@l1_wk\x0c67Y^P>7]o= eCPMrJXyMm':E<H3'N&qQJEz.*\rVnkD291wx?LN", 'l1_'), [2])
    def test_case_2221(self):
        self.assertEqual(pattern_match('6`:oJ]dh]r+o1\t(!"_.J4Dd_FC\x0bc*&TI\x0b\x08I^.:30BvqYb2X1,#]b#\rQT\x081\t^P]Mt[', 'J]dh]'), [4])
    def test_case_2222(self):
        self.assertEqual(pattern_match("2R:R/bV\\Ho4=Q6Rc\rj.dX<]Ji`PD`!`NhQQ.iU@Mb1\x0cVY`yxK]?e;]@h[;QdHieK 'NlHz$", 'QdHi'), [58])
    def test_case_2223(self):
        self.assertEqual(pattern_match('s`B+bFGek%c|8X\x0b%xclx$3\x08B9(>*#*_aYa|9nu>d!e`tNqJ(q!Dn>sY=*9lS4\x0b\x0c.ru[fe\x083RTr^W\\tPa0A0b(f%\\<i\rK', '0A0b(f'), [80])
    def test_case_2224(self):
        self.assertEqual(pattern_match(',P}!"Auv ob+W5#5Z?"\n*T`(y+Z}Q\n\x0buS![!wGIJZ)O(iS4,ClQu[H!uic!`H7r\\2iO\r9kAi+na4[l"FVIX', ')O('), [41])
    def test_case_2225(self):
        self.assertEqual(pattern_match('9N*R"e4*l]%*e<+AmH)~tu2kG\x0b2|Fb.dc;u&nDX}[j~a(2:9U(;N#', '2:9U'), [45])
    def test_case_2226(self):
        self.assertEqual(pattern_match('DJJxJU5"~2b\x0c\rQB>c0gfrvR@+DR~z<f)nP4\x0c@`27Z\n]V{Yj|;PF\\-Q2nk%S~EH+iV63v!leY{;U&7', 'JU5"~2'), [4])
    def test_case_2227(self):
        self.assertEqual(pattern_match('t$1(Ab!0Vp9y:\x0bSg"\x0b8)SI.$Z5Dl()U1/osx`jSTa\\]131?Nb\x08+\'b M0\nt}Tt;x0@9!.n"glPf', '1/os'), [31])
    def test_case_2228(self):
        self.assertEqual(pattern_match(' FO]E,p =(8)Qz4 a}fH\\ 5\rR>zL8R\n&TLI;Rax>t7ds1?\x0c;>"-;qW8ZOUYsFia3S\x0c)N/:|BSm=mB\t%RM=~L|7K\t]&>S8NBU5K', 'S\x0c)'), [64])
    def test_case_2229(self):
        self.assertEqual(pattern_match('`R$v-f\x0cvy?b%q"-ia{3\n<QQo"bDf*&yTDE1t6EA1?6B78%J:CY3\r,J\nzz/,.', 'EA1?6B'), [37])
    def test_case_2230(self):
        self.assertEqual(pattern_match('#0(3~A1R;n!H^t.=4x4ee-3ei(N@[9`PhlIt>M~\t,|R6}%Y0l;gHzDyaD7/4HPG|[TOtuC%;{', 'gHzD'), [50])
    def test_case_2231(self):
        self.assertEqual(pattern_match(',]E8 K\x0cDy%tE3>Bo x\nCN@tQkqs>]h_U\\7"dX+>1;v \r$QuKd]uE|N\r^cKar0W3@z?gZ3% $(\x08hRD\x08Ybr0@faG;\\ocE7<p^', 'D\x08Ybr'), [76])
    def test_case_2232(self):
        self.assertEqual(pattern_match('Y9\x0beK|"S4~pd=6s7nR`|CW1wX9\x0c\x0b2khb0.m\'PQp;mLc^R(:&tp-}\x0bu`$%Dwu?EOSB^q*WW8v8jCb/ebo$Ue.n&D.i"/3l$@', 'EOS'), [61])
    def test_case_2233(self):
        self.assertEqual(pattern_match('zg;P]\t\'G<%Yu\t9EuU@TIf*+eAdE@I2e1{B& BFhv2{JAavW\x0bYxhWl9|nP,zA+@FM\'[0"ZIW`O', '[0"'), [65])
    def test_case_2234(self):
        self.assertEqual(pattern_match('P\rw}|Ok_46#sBm%sd(}3@@nG6*Wkio07VZsM?{maLn>G02=JXTueXE_w#\n#-T59gw-_)vb){`2CQKO\x0bHeJ|?,v#*e\x0bc\x0b', '\x0bHe'), [78])
    def test_case_2235(self):
        self.assertEqual(pattern_match("B\t{[+z/\nIQ\x08Y+>nq^&uZm^H`&aG>gD]K<8JF&[;//@i$v7;mLopgl3ia{$:9;R\t2\t\x0cuK;r>RSfgW't*$0\x08`#|ZdI", '$0\x08`#|'), [79])
    def test_case_2236(self):
        self.assertEqual(pattern_match('k-g.5myh|q5lLYlwr<p/_vo.r6h\\,SBzy|!Q7PZU=75VT8Ig#ZP)6.I|@pn4mC_z"`F{\rnRA#jmXq', 'h\\,SB'), [26])
    def test_case_2237(self):
        self.assertEqual(pattern_match('2*FYpI3)A9&hHn<EdFNfnXeVX*#>j-m\'tTL\x08:VG^Z@01@;\'PL[=?\\c=BiYiH7]Pd"lUs@ c\rn\\^\\=DrPSyqSO\x0cl}.v', 'tTL\x08:'), [32])
    def test_case_2238(self):
        self.assertEqual(pattern_match('~\'7AIj(g+Tw3\rKX`$\r,:zn/"s@pt(eH&StxqZbS\\!&M(5~4E9?aqLKv!&fS', 'AIj(g+'), [3])
    def test_case_2239(self):
        self.assertEqual(pattern_match('\thj$Srw)`\\NUb7I`z\\>y\nqO,L!s"n(^gSJ5!HynrXYW4-dHQWb)', '`z\\'), [15])
    def test_case_2240(self):
        self.assertEqual(pattern_match('g\tp8&H*oXIc>AN/\x082<q\x0b/J\x0bCr\\SA6;)\x08\x08%ikRR^x3HJy5\txS2yToz\\#Tb%/u*AjP5q\t\x0c2kH#rL!Ofih', 'q\t\x0c2kH'), [65])
    def test_case_2241(self):
        self.assertEqual(pattern_match('En1h \n1baqS^!U!smOn+Lj5+;%p%~u[kvU0\x0c8Xm4( HfPrOL{i?=]`uk\nIbj4tKZ+pG', 'uk\nIb'), [54])
    def test_case_2242(self):
        self.assertEqual(pattern_match("gL\t|\x0bf\x0bBrSjDerEimt/\x0c2$=d'>bN?dy\x08>(ctxznbG1'M]=6Kye+d0mN<\x0b~8MnD/o3aC&&", 'rEimt'), [13])
    def test_case_2243(self):
        self.assertEqual(pattern_match("vy+=)f^\r>\x08\t#]~*:{}`x#XBW}n qf\x0c\x0bGXE2'm'7q]\x0b\tR!! }ndc0h` N.z?7,9v'|", 'f^\r'), [5])
    def test_case_2244(self):
        self.assertEqual(pattern_match('GT]I{/Z ~lUb/:\tIXW:k?\\4>mP\x0c<naYR9&$+:UyT\\ )`;oiV={1xn3%Vt2_V', 'Z ~lUb'), [6])
    def test_case_2245(self):
        self.assertEqual(pattern_match('G:ss[ic5}:b?9OV#Dx@QM~\r"\\K;\x084\n5R $CZcK~bP$|K\t6*N\'>E?Vxu\x08"l!?bY,L\x0c,ik3$dP"\r3p\x0b\n4>]dWB\x08\r\rK)0', 'l!?b'), [57])
    def test_case_2246(self):
        self.assertEqual(pattern_match('`\\[)n$xB/F|-\x081>N1Al2+L0?2iY@]VUtptW!Px%\n4H@XMC\\\x0ccu(<tks:\ndi\\>K\x0cp]V},l[@[h%dU\\|#v:SDv.\x0c.76\x0bcy', ':\ndi\\'), [55])
    def test_case_2247(self):
        self.assertEqual(pattern_match('~d4tSHn\x0ct/"$I_K6+CNZHT)?\'B;giDe%zRk:|Fw=9 %G| @CIn1U$z', ")?'"), [22])
    def test_case_2248(self):
        self.assertEqual(pattern_match('Hm>R">[=plg\\t~}=8M|_@~-o[?gV5trJpQh4EQ\x0cL)$7:3o&*[$tNkDqg_$^:M#[@qx5f"^', 'Qh4E'), [33])
    def test_case_2249(self):
        self.assertEqual(pattern_match("^ +)}mAsE/'\x08-L5I\x0b`\x08bC\r@\x0b4zKew 4\ryVoL'y`*2(\r=lYslYU{5.J-VXsX)8KS;DZ9lNZb,*ah4.>H", "E/'\x08-"), [8])
    def test_case_2250(self):
        self.assertEqual(pattern_match('EDR*Cs]++ov\n]xrd=79OFt!Ib(RCY8IcGP{/s,\n@c\x0cL!313CsnwlfX\\#Feha^_Mda%3HHF\x08$VO|szf\rzij"},Y}L7Se@VLAN&B', 'P{/s,\n'), [33])
    def test_case_2251(self):
        self.assertEqual(pattern_match('9T L=\x0cAOnK.#Mq$,/EBgaeE\x0bKnJwC/s#{{\r9Zt4OW/!\x08\\ksC;z c/MqXH>%`s7\x0bt\t<.Kw[4XVooztL*q \x0b=w|', 'JwC/'), [26])
    def test_case_2252(self):
        self.assertEqual(pattern_match('q\x08)}nWvX ~1s(y&VWV!uDRo^1 w&-FT`Li%Ke_/oH?n2@;!g[D\nG48\x08Z\t~>p!: 1jQ\t[3_i0L{tyN\x0b$', 'p!: '), [59])
    def test_case_2253(self):
        self.assertEqual(pattern_match(' Mvov"]nL";qz\x0bMgz_LtBVn<:P=E%{d\t6"z)>V0MG&nR"v->q>id$>>MSHdx-Y1e~wY6\rvd\rtHX4a~8a', '"z)>V0'), [33])
    def test_case_2254(self):
        self.assertEqual(pattern_match("Rt>jG\x08Ed'ru)nRe-$d0ov9L:Rg/G(BZjJ{;8as4jfy_CwW]dvUAV\x08tA^s~:-g$8M", '8as'), [35])
    def test_case_2255(self):
        self.assertEqual(pattern_match('\n_*lKl%>x4*g({gP[:h;k$9O\x0cY$SlcI];-IdPUZ7KRs?@"&\x08|\x0c\x0c aWBZ\\7wV9\rEdF&3P;|\x0b/Uf;S\x0cAh{>\x0cp $hk})=RM', 'EdF'), [62])
    def test_case_2256(self):
        self.assertEqual(pattern_match("8\\yf{0`\n4%'9,/Qa:sC:E\\#F\x0br]j\x0c;\\Kx5jNQPHF~J[Sa.d^X[&jR3MRfIgwl\t_Q.{=t(<\x08Inu}+5g,", "`\n4%'9"), [6])
    def test_case_2257(self):
        self.assertEqual(pattern_match('Ii`M?Q2(Zm}+_!:>l[eRt6o\nHsH+hYy+{\\Dfe5Xa=&-S 9Or\x08,/#IKnZt7 a\t)aP0"kw||sN/yQGM', '&-S 9'), [41])
    def test_case_2258(self):
        self.assertEqual(pattern_match('^=cS%(D\\l<{|"\x08<B4?\'y?kUK\tMXa?]yy\ng(\\tG4q:qn&HS~81Am\x0b`FCilj(E3;9cnKVbc0NB>|X#5\\E', '~81Am\x0b'), [46])
    def test_case_2259(self):
        self.assertEqual(pattern_match(',\r.Y(hT(v9.[E4T7JC\x0cY1<nU\\\x0cI\r*[mmT@-MX3|UZ1DZQ>D)\x08C?i:yHd}r#z<-74Q~kJ4Iy\n\x0cEKBc{CGG\n*6e.*5An', '.[E4'), [10])
    def test_case_2260(self):
        self.assertEqual(pattern_match(">W>&aaJ8\x0cfD+^4o_SH2))/\\Q\nykm;BS<('Jdv/:*J#YxeCT>Rp\x0b3Lce[w[S/", '))/'), [19])
    def test_case_2261(self):
        self.assertEqual(pattern_match('aFJ"W[{UhBQM[0csui{q@r\x08c:I\x08+ZZJ\t(bdx/Q}}6w\x0b8!AN}yF+_eIns\rEcUN|n|%2idR}S8\nt[Zr1E"\nLi4{E\x08Z|>&{\nQ', 'csui{q'), [14])
    def test_case_2262(self):
        self.assertEqual(pattern_match('xv.Jse.<3xF-\r</W9<Bml@K&0ik=0j;/%OpS%kGq>K<A\x0c\x0b.WJG4\r?M!7wZ_=;/mmHb]/e]?H<eL]\n~$\x08XfC=<N2\n"j \x0cg\x0c+?e7R2', 'Bml@K'), [18])
    def test_case_2263(self):
        self.assertEqual(pattern_match('yEu}\'/L(i~|%b\x08cw<\ry}X:!U_\tNWw\x0ciQdbt#*p]. Wxu$-UXv?<P[l(A5"%+hS_M$(O}Lqo"Cv', "}'/L(i"), [3])
    def test_case_2264(self):
        self.assertEqual(pattern_match('lYh\rMkxjO@hHKU86~W_=\rZ;Rt\nC\'6R5(G(J8"\n?Q!.\tB1%s:Qi"PWr/\nDan5H[N rcvVA\'_8D:jSDAk}g', 'i"PW'), [49])
    def test_case_2265(self):
        self.assertEqual(pattern_match('0IZfw_T YcTe~^yH!I"/%or:?smGzy!_|>b6S^.KXd8gN\ncZbobi', 'fw_T Y'), [3])
    def test_case_2266(self):
        self.assertEqual(pattern_match("YOLo(<U{_[s\\8l%h\r7te\n=duvr>-nV&8Tl)JVi~D\r\x08;J\x0b|/<o\r'{+H)o]I/\n,.;mqY3\tJ\x08~u]h", '\x0b|/<o\r'), [44])
    def test_case_2267(self):
        self.assertEqual(pattern_match('(:Ls`,U/@b1#}Cd\nDk7*1%i`k]J"68/bYn,\x08P\x0850\nje \n<-A+.Ik!\rUn{]\x0bODNl`tr', 'ODN'), [59])
    def test_case_2268(self):
        self.assertEqual(pattern_match("\x0b:ASPiEX{7#B$> h7&'w3a48NgG@)0ktsnEu-o:&G;+{_=\tf/,~<4ouz", 'SPiE'), [3])
    def test_case_2269(self):
        self.assertEqual(pattern_match(">E?n[;9!95*r.\\\rCL1MyQU#\nRGr\tKTt)a5H;Wf/4Eoi\x08#h\nJ3M?S?mq'f|ho,MwZyaQt'\x0c+~#Mt'L[7m\x0c=\x0b@(\x08/", '?S?m'), [50])
    def test_case_2270(self):
        self.assertEqual(pattern_match('mD#\nR3o,Oxj&i\nX\n\x08~sLwHu%h/k[zH(Ret0\'5vg^?"tw"7$\x0cGd+k\x0c', 'R3o,'), [4])
    def test_case_2271(self):
        self.assertEqual(pattern_match('$SE 3i+<v\n~"MJ`9ovZ@\\ WC4V0],~0lCVo}k.6ztxUT.wDz`{z\x08BCb:STW,Q\\@8jr#f\x0b&f"VK|^:&+', '<v\n~'), [7])
    def test_case_2272(self):
        self.assertEqual(pattern_match("tIA7hpCo4fg\t'7RF\t3v[1'|/1\x0co-d\\LUQdBR!?G{Lz{<BvYyWxxE", 'BR!?G{'), [34])
    def test_case_2273(self):
        self.assertEqual(pattern_match('w8|m%sVI^.H]*A.m-v>Z^/17xN;R\x08a{?IZ<)zAaaVhO1 `8$4s\x0cn\r\x08t2w6[C', 'n\r\x08'), [51])
    def test_case_2274(self):
        self.assertEqual(pattern_match(')\n;3.v@jCh\r Fuq5W/yb#/:9Vb1t-!\njuTUHK$[G 8uOEAf[ZY9j(eluxen;+Eq', '\r F'), [10])
    def test_case_2275(self):
        self.assertEqual(pattern_match("eg\x0bi\x08qYv<21\nb]@%)k4'!6MgZYo^!vvT8.dpJVqPFkp~+\n7VG6ab:h", 'kp~+\n'), [41])
    def test_case_2276(self):
        self.assertEqual(pattern_match('^T7INQ(\\gM5]\t\x0b\\U8;l1+^n&hgv)M4#q\rf\x0cqC~\\AjMb?.lSODd=RaY_\x0c}3#wTHtR6B\r:KQbZ]', '\\U8;'), [14])
    def test_case_2277(self):
        self.assertEqual(pattern_match('TP@\n_zu\x0bBBLJ?i$7)7~\x0be|_2 \n[c9Z57Y;jZ\x0b > =@i$,v\teF\\Qgd[t;', '_2 \n[c'), [22])
    def test_case_2278(self):
        self.assertEqual(pattern_match('T#/* ~$epO\nA,: ]M9@eZw\r.Lpa_oh]8dn:>H\x0b47b5Ed"H`Xa :2$m*gs!;l?n 1Bj(>h', '9@eZw'), [17])
    def test_case_2279(self):
        self.assertEqual(pattern_match(':;&xd[j\\4L/LO,AV%1n/|gm\r#\r}nO,U_G `Wa`Uw\tu=]o^Oc$Rbv\t<5s:\x0b3Zv7BZE7J3K/NhCI&%2AA&!o\x08_/', ';&xd'), [1])
    def test_case_2280(self):
        self.assertEqual(pattern_match('m.-|9yed}FD`Y{\\\n\x0be"=o#s8+\x0cg|mn&_i1`slZZd-bC]XvBA\x0b\tjM7~bMT+]jTyCRv!,>[CUi-JXn>Xf', 'ZZd-bC'), [37])
    def test_case_2281(self):
        self.assertEqual(pattern_match('\x0bLvYD`;yvG AYf\r$Kd\x08n5!W`yQ(cREz%$O|R*Du1Y}pE9A&lce\x0cSY@DtzH', 'u1Y}pE'), [38])
    def test_case_2282(self):
        self.assertEqual(pattern_match("nal1S@h9D>Teb\x0b7;N6`3Xego*T|J \n,b#!K( F]{U8A*r{3p.7/ERIITEa%*?6`M]Aih.+R\n@R+XEC?[xg.E6R,s2[U&n {'{", '1S@h9'), [3])
    def test_case_2283(self):
        self.assertEqual(pattern_match('sFP&\x0cd%u$;21X`&JICvY#<E{V}Fdj K:<IU0+\n3+ckKY6!L|)2?7bR1I5W', 'CvY'), [17])
    def test_case_2284(self):
        self.assertEqual(pattern_match('rsA]B7V"Gvwv)-C`nMal.F3y.}\r]`J?r;gY#<\x08b[p=p\x0bk]CP:94\'(xVq"', '<\x08b['), [36])
    def test_case_2285(self):
        self.assertEqual(pattern_match('G.T>j\\>r3f|B/"r$CpQ%GU|\n!DoK5\t-ColU9B#eFQ\x0c.ptgvYe$j2:>#3\x080NKA+4k2|6#]m"U|EHRu!P~k=&YqHc \n.Xf<', 'DoK5\t'), [25])
    def test_case_2286(self):
        self.assertEqual(pattern_match(' XS`~b_3.\\Io%!e@&*19_SH\x08FcnF}q@ie-?qsu idJ;%XykZ\\4P$a;{J\rW\\7{6$m(CNG>w(7wFIx+7', '%!e@'), [12])
    def test_case_2287(self):
        self.assertEqual(pattern_match('{\'\x0c>q,e].d"=f{ JYdiB=F+siA*b&Xm*V\\VY`mKAvw@[ Ynkq>^MMU%ow$de\\MB\x0b\x08[S:"d_f\\\r)D3\x0bQ_ZnW\'wCu<,#oyf%4WA#', '^MMU'), [50])
    def test_case_2288(self):
        self.assertEqual(pattern_match('E@~x sG2\\HXT8*Rmw532P*B_qV`DSfC/n,`^g+ondr`VNG\x0b(iHGnM4*lDa\n"FEk&\x08v@z*\x0c_5tTYMf!M\r', ' sG2'), [4])
    def test_case_2289(self):
        self.assertEqual(pattern_match('t\'BCsohxQ `]ZN"t!I\rak-P1v\'X*?Pdzr,)r<(NLqE0{Nnmg@lMc *If_ypvikMn', 'zr,)r<'), [31])
    def test_case_2290(self):
        self.assertEqual(pattern_match('Bz@Np\ny\x0cq)B8//G}kL.b=U"Di8z@s)4pyK00yHYl9}$!Cmb()z\nK7UNZdSTEB^Pz|qaL9\x08', '7UNZdS'), [52])
    def test_case_2291(self):
        self.assertEqual(pattern_match('B9(qbcm*.NX\trHw0ibm7/8h-zj_P0<M{q+MEAr5.%;\t3\tk~c5-k22;F', 'bcm'), [4])
    def test_case_2292(self):
        self.assertEqual(pattern_match('TUU(k\x0bL @,_C~Z;^heQ)dOt\tn+WBdLynWstE2) QSm"B\tMhE9[*J>-80F\\!h$Lv,2CzIpmcA7=G2Ab{}?dPfe\x08jaF', '{}?dPf'), [78])
    def test_case_2293(self):
        self.assertEqual(pattern_match('[D)&3#mABXQN\\[)4Of%"p`qKIDfU!n-w%^z\x0by-l1F*r\tEnU89+rh\t?TQ.ZBmWA', '"p`'), [19])
    def test_case_2294(self):
        self.assertEqual(pattern_match('Nk\r~\t*UD^ 0J\x08HfN\nb4U\x0ba4}M#&/6gO?q-2sIbi`DB$!O_OJ_Y3qtZ{', '#&/'), [25])
    def test_case_2295(self):
        self.assertEqual(pattern_match("xNrwkQ8MOfB=Ue:,sS#oA4q~UCZZ4(\\L[mvaRAnHHD*INzeR4B\x0cD{8mX<\r}Vzj'>,K\x0cu\n(9zE\\6", 'AnHHD'), [37])
    def test_case_2296(self):
        self.assertEqual(pattern_match('\x0c;=sj@rKt{N?[F7MRGD"I!^(\x0bs|%YLqaxkFMO1H{]H)=>?>p\x08E^', '\x0c;=sj'), [0])
    def test_case_2297(self):
        self.assertEqual(pattern_match('I\\NK^\r1Jc\t?\'rQ\x08k~4]BO^#d?g^~>ds\ra&\x0bt/gFGN{%%bYgVc \'Zd\x080JhUCH<~R4y.FD"k', '?g^~>d'), [24])
    def test_case_2298(self):
        self.assertEqual(pattern_match('x|T~Im=]~T\x08\\\\d}"(Kq7=O|\x0ciO!U\x0bAst3`e9xZg2AT7QPI,A8>#^pr#+\'"gb-H&', '7QPI,'), [42])
    def test_case_2299(self):
        self.assertEqual(pattern_match('cWpSH)at2U?s\x0bTu@fkNI@NF^:(U<w=VDclv<{6)!;#e#|\\(<T9&^N\x0b&@$v\x0c>0o', 'at2U'), [6])
    def test_case_2300(self):
        self.assertEqual(pattern_match('\x08h)Y5o9pZBv>\r4 d\t"#IJ>=,>qw+x~\x0bq0=\\@m51BLi& zgeVK[%2P*o*OWz$<%sTXDhX_\x083*yW}3HHKZw0:x!*t~[A\t\n&}id,', 'ZBv>'), [8])
    def test_case_2301(self):
        self.assertEqual(pattern_match('~.(e}4h\x0ck/TL\n;VC)6%Dq\tKoz&ZSjiIhdjO(/^eyaiE{Mvj8J@LkTXxB=\nK@-XUlFzxzMMx= {IXT\nM', 'UlFzxz'), [62])
    def test_case_2302(self):
        self.assertEqual(pattern_match("*QO+*\x0bc.\\e^^aJXNW}I!aOwB`|RQruq,}q=\x08AOzj%@I(#u)nm6 r\r\\'!W\tpYP<V`Sa#$_=V55/`", '!W\tp'), [55])
    def test_case_2303(self):
        self.assertEqual(pattern_match('+7O&<JX5o\nwVK7oKL_9j9L+Q++ix&T/Fc{%\n!a7,895AxgPE ``W0h', '/Fc{'), [30])
    def test_case_2304(self):
        self.assertEqual(pattern_match('8g2]H\x0cE $dVs DSGN,M\\pA7A6f:`$XUXwm_J}/W4?Y{4.v y O>IgL<,OH$5<uI<fl@yZa1H/9stl?w7/\x0b8\r0iq(^l/ht\x08Xi%', 'w7/\x0b'), [78])
    def test_case_2305(self):
        self.assertEqual(pattern_match('Dq6JK7<;~kC\x0c.;\x0c{OG)#e0!fr"}F6,_?\x0cN\\&a<RE8BHZO3[$[ON|*VKjR}78,JR\' 6&Cd j22C;5G<+WO(zVX^', '|*VKj'), [51])
    def test_case_2306(self):
        self.assertEqual(pattern_match('S5Cf23_-Y&WhV7HE7@ +`-&>RI$:drc)0M&o&|3\r\x08??kqkw)*{lI2@D(F@gy"3ANbYpol!3', '-&>RI'), [21])
    def test_case_2307(self):
        self.assertEqual(pattern_match('~}%q!k&j]=araR8lC=UN6qCWGc/H~:&?Quz)\n2Zy)+"`Prv\x0b;{#T^cp 2<!U{Y', 'p 2<'), [54])
    def test_case_2308(self):
        self.assertEqual(pattern_match('Tf)n{Q\r7j\\WINm]NZPq7MsPQUC&+\'G72\t6#?RWtm 03}wAThT\x08W%P%=M!3cs\x08nFU0P&KX-=zx">\x08Oxt !b', 'm 0'), [39])
    def test_case_2309(self):
        self.assertEqual(pattern_match('"cy.{2X6#p2gR/6=\\P%`.F9!\x08N\\vX\x0c\'~5H}Q0zH\tEGwT44V>/M`9V]o|7MUyhS1/AG\x08~\rk"\x0b(>FZ,\x0cgd+#CE4B+ckl@Us~#Yte', 'cy.{2'), [1])
    def test_case_2310(self):
        self.assertEqual(pattern_match('4&-"C@4S.1C^Kq:\x0c}i,np:aB./`}\x08U.r)",LC\x0c|Y&$R"&2}U:<J7uw5`DLzw\'J\tbiF)]Uj#$%xe\'\nf&J', ':<J'), [48])
    def test_case_2311(self):
        self.assertEqual(pattern_match('bN:i\t0I\tTCm.4zjnJ|C=ftrdeNhs5V\\}\r-xbdirO{^#zRH_]\\X!\'\x08&I,aMg05R\n3,_cJe"4\x0b-[|S', '"4\x0b'), [69])
    def test_case_2312(self):
        self.assertEqual(pattern_match('H@y-2QtP_Rh`TgQW@NV\nP;.X&DZhSU@\r\r7YXvhfy"8lZg/]2P*O~g\r8*8n2>WR~G1N4m\x0b@gloM2R6&LAi\x08Qz_\x0bhF-kk2]Y-[g &', '4m\x0b@g'), [66])
    def test_case_2313(self):
        self.assertEqual(pattern_match('\'ITK-19CKD^LeHKN(6Pn1DQcv"z$ycy1%_H\x0c)>dsF#!Ng>*y>\\,O[#=="/ahQ.v7rb\r!- K=\n85\x0b$fV', 'Qcv"'), [22])
    def test_case_2314(self):
        self.assertEqual(pattern_match('DrS.\t^Tu|=G& GZKhy\r #sC5bbq=;_\nu,h0"D$JyZ<%D\t)\'@t\x0c\nC8:dG\x08fa\x0c.NztEvE?\x08JVaR_', 'C5bbq'), [22])
    def test_case_2315(self):
        self.assertEqual(pattern_match('KyCy}dk=|^^-V[E)<a.D\x0cS#*/(}+\tWM&:,\nkeW7fKm4dP)94.@4mRO(omCF8)B(JWMc_j8ZiC.*QN~)T/s/m!JN~6', ')B(J'), [60])
    def test_case_2316(self):
        self.assertEqual(pattern_match("5XP0s_CghLXW=Myk0l~+/cD{7[Q+doxI5(@X\\1jxso HoSpa<\r'3C9DYL5?*|G(rjFzOT-AGFi$Ge\tmK5yMH 4&7", 'xI5'), [30])
    def test_case_2317(self):
        self.assertEqual(pattern_match('{e+UJ]_*0PNb_bm~|m?+rKyT$FV<ma6"w)X3^No7pC\t^ki\r\rkiy>', '$FV<ma'), [24])
    def test_case_2318(self):
        self.assertEqual(pattern_match('KRd?#4MHDSr%[D]If}*T\nH(\x08GTYxG,MCck512WW\x0bigH{?zd:H2AJrG', '?zd:'), [44])
    def test_case_2319(self):
        self.assertEqual(pattern_match('9{,kl^".>Qy-f0L\x0b3K`A\x0cux"t7>DBkJm\nz 7C_nriDavcQ,kAXX3CEfkdLl\t{6.;T9S)tcv"b u>f\\R-36sm&d^1n', '>Qy-f0'), [8])
    def test_case_2320(self):
        self.assertEqual(pattern_match('7dmj>iI*?+>oxbDx@PnHUH^i~6\n*[+EVtw,UixIw-fa5FIK@Ti ~0\x08byfU7:0}$', 'HUH^i~'), [19])
    def test_case_2321(self):
        self.assertEqual(pattern_match('h6[g|Z\x0c)J|\x0cOhC:Zk\n@E,2W+ppcMT|pEe3\\pB$ZuP5\x08c\x0c*Ptq4}`$(e;%/I\n7L\ttn', 'pEe3\\'), [30])
    def test_case_2322(self):
        self.assertEqual(pattern_match("wEamLi~I{T'&Dn&aZ;\t;9Fe\x0c^!ezte0i`h_o;pYk>x25v:2jkxO\n<Z!\ngoQ\rXNx91\x0bs$ENt?mBp/t\x0bKqYUz@A,0E@K'[f}", "'&Dn&"), [10])
    def test_case_2323(self):
        self.assertEqual(pattern_match('7d]"@%{p6{{(7{neuiF6s}Rj^0ShH9EpO~WzUF~N>-[#Nt\\Uj\x0cVS1$sYe\n ', 'H9EpO~'), [28])
    def test_case_2324(self):
        self.assertEqual(pattern_match('op.AeXuiye9e:{[S~?^TBU.rP"[!6aLk[=;wak[\t\x082Qoe(a\n}^|?s', 'Qoe('), [42])
    def test_case_2325(self):
        self.assertEqual(pattern_match('6o195I0+B5z.jE_N0M&\x0b",\'OG{!\x0bL&OQ$ YW\x0c{al8KpY)EkUc!~iY{0Zr:}7Co$<"JW(CqK|j>', '5z.j'), [9])
    def test_case_2326(self):
        self.assertEqual(pattern_match("<kyb_`XG3C=+ W)A[czW%G=Xz-<Ur$\n2m>ZN\x08 \ru\x0b$zK4qO#arWR}x5yy=B:O3OTG~]\nK6'<", 'u\x0b$zK'), [39])
    def test_case_2327(self):
        self.assertEqual(pattern_match("f ~qdK8y^u:*76'~'x=f]/]9|_rA dne(M.^~5MI\x08J6oK!)7[*|f\\$zVIMF* ", "*76'~'"), [11])
    def test_case_2328(self):
        self.assertEqual(pattern_match('xG9K2@E\x0cZLtL0^o%Ud?.ky?`N1 ]k[G~\rjU1I-7M3K}=oLw;sw%1%SXpO+KF.@Z^Bmtv', ']k[G'), [27])
    def test_case_2329(self):
        self.assertEqual(pattern_match("'o'`C:C4bPBZ?#Zv3c^}Z\n-{l7*0hu-Q~L8>5lq\n`u-\tOUPhDNS*D5G]J\x0cfq*_]w35NU&", 'Zv3'), [14])
    def test_case_2330(self):
        self.assertEqual(pattern_match('\r#j,[Ysrl\'xk)\x08R#d*208pZ^ozxW!ERx+TcUIXCu^e\'~wAPSt\x089yk\x0b9D*W@gwoe"*y;$ak=jc6@}b', 'gwo'), [59])
    def test_case_2331(self):
        self.assertEqual(pattern_match("gkKj,f,Ov`x\x0bKtQ#mRy;;!\x08.MF^D>xvh0\n'\t?o4m<@#4R/,4mS#4cKy!:6FH/@At&\x08SG^&QfiXV>A=q}^", 'Kj,f'), [2])
    def test_case_2332(self):
        self.assertEqual(pattern_match("WMnmQ\n5\x0cEO9)^\t^i y@9*M\x0bw!Uf[k0^nk0wcQXa^=i:P@V-g^k2y'M5g`zYf-VFa3/2`4tHE~mLS{8Bl`~4seOO *,%Q`", '@V-'), [44])
    def test_case_2333(self):
        self.assertEqual(pattern_match('[&(k2\rfCjr\\[]m([\x0b8)L-Q(V6)B\n5DzkHbv7u7@t.wE\rfVg{MjH.n(|', 'fCjr\\'), [6])
    def test_case_2334(self):
        self.assertEqual(pattern_match('K\rSTl=g[\x08(GpK/./ovjf\\>(OOc@$TU02E\x0bQ%v]aKPnyhnHdQn J5v>hg+j)63.~\x08E\\MbL3h_jU\\AO_8e', 'STl='), [2])
    def test_case_2335(self):
        self.assertEqual(pattern_match('[\\dbUd~A\\\x0c|Lr|Z%Cy$N%?R?Yp%(V6r\x08,*,R-\'8\n\'@"Ci3p}H<2}H~6Q\ty\'XIsM3V\x08 HR;H$t51z', '\\db'), [1])
    def test_case_2336(self):
        self.assertEqual(pattern_match("\nA0%^_&^n@M*';|CLc4\x0c)_Ian4hEpHPPB bTf_D`.j|Hi -c)N'TX0Yu::<", 'an4hEp'), [23])
    def test_case_2337(self):
        self.assertEqual(pattern_match('7Lf:Z*4;C_xZM\n`_[)A}uCrNY8GUM*0I_<o8mm\nsN!\'ns*2&\x0bCh3F|<pX\rS6X;&"TH7?)(%', 'TH7'), [64])
    def test_case_2338(self):
        self.assertEqual(pattern_match('[z2JYqx%tM\tV[J\'(H7g}f8k(8ZHw[.TU3]Q"^ac\t@DfG22r32s13\x0b\x0bVaX`^_wQ<A6&ny\'U\'2Dd5a7&)61 H u8d?b\x0cB[lofz7,\x08', "'U'"), [68])
    def test_case_2339(self):
        self.assertEqual(pattern_match('K"^>,58=3Kjg[\r-u[rKm2#mIp L+G+23!8\nS,8M$,\rY}&M%QUI"&eV`', '+G+'), [27])
    def test_case_2340(self):
        self.assertEqual(pattern_match(")>`1v*0H]aS&|EzVl\tT-/{]!fz'_1\rC/dbfH*wC:R[2-T7VxQRRf'[XO[rs8S:n:Pw\\`'m@//&h6ngK{Y7.3=", 'XO['), [54])
    def test_case_2341(self):
        self.assertEqual(pattern_match('Yq\rn ?%\x0b^aNH1_q_5g%&]><KYlpM<lAgA\'BJ!M<{P.tbMPCbhbF;1CK){Bzh/lF`;v_9"pjG:', 'AgA'), [30])
    def test_case_2342(self):
        self.assertEqual(pattern_match('*|"JMEVJ,!z7\'o >v;\\tV=\nq v#I\nZ?}e%FN]1O3\\22o\\^@h3hhTO}ivS(""pdNt!kTi', '(""pdN'), [57])
    def test_case_2343(self):
        self.assertEqual(pattern_match('F0yf[7;l|\x0bG@;dL5dP\x0bu\'~~\'\x08~(~=C{X %\rlQjd%FA6sYR;T\'<HS`w,MJ\r3\x08 z(<S`zb5V3UD+78IB8"Iw*a&', '5dP'), [15])
    def test_case_2344(self):
        self.assertEqual(pattern_match('Sn"c<tun{\tU>qxo?HZ69y/vD$Zf8\t~L7eT|. }jr(:{3W3Z\\Qm>^J_?,\\{\'iv{j9eB\tJ\tF^,v)h)qu@,:vI.qC|\n=[+yN/', 'L7eT|'), [30])
    def test_case_2345(self):
        self.assertEqual(pattern_match('K2Ty~hbqk^WN}\t;*FIcLwTOzP+i]a{iqU2D5QembF4<Bh B7Xx0t8c@x[u4]EE>mK("-90D\nVGm\x0bR\rUCUbAoEK', 'LwTO'), [19])
    def test_case_2346(self):
        self.assertEqual(pattern_match("r-HaX=~$_!a?hE\x08(JayY','\x0bM'<FGHWHl\n\rYi~KAs.6$ZuCE?>?CE<_av4VtbG3`XKf>r4n", 'aX=~'), [3])
    def test_case_2347(self):
        self.assertEqual(pattern_match('Jq{3z9)oE9:!x{_JqE7(N\\dZ&T{h}2t\t\tesIU.~)X[&6 3@b7)?\tjt\nOe%-', 'h}2'), [27])
    def test_case_2348(self):
        self.assertEqual(pattern_match('p=IjDxbES;OeeeT=PCmi)*3NF96DNG;T0{[vhA}7L\t\r4:thYXm;\x0bscY;\x0cA0FSr.z"D%jG/kkPSSR ~<\x08{\'4\x08m-\x0bMDPZCn2pBP\nn', 'bES;'), [6])
    def test_case_2349(self):
        self.assertEqual(pattern_match('|{4MUQhfP%k\\#3Mm}\t\'\x08h0.NIy,iMDAw"= \\`)b6yJtAiZ_\'s9AIr&r\x08VPvAMeB\x0b0\'_TB(fsdw#3KIDLb~J!=', 'vAMeB\x0b'), [58])
    def test_case_2350(self):
        self.assertEqual(pattern_match('?APG[AJJcg+UD\x08up{D.X\x0c4h@1m\'\r[8oX."\\sP><) \\Idte/iHo\'SKcRC]\r0anjT@roq-Yj<\tq#&jg\x0b+ i0Y\'wgQ', ' \\Id'), [40])
    def test_case_2351(self):
        self.assertEqual(pattern_match('>6O~HtE kJ7FBP6@7<Cy\rK<[\r/kVAs)x/\ncE5kuJG$+oDU3Hb\x0cQ:nr/hJ;u&R{', '~HtE '), [3])
    def test_case_2352(self):
        self.assertEqual(pattern_match('svi\td3`Gd3agV!UDLxmW$Aec\nJ\\Gs73\r6\x0bSE3"MP+n-.}hc*q,kTPsR6|zj4-6', ',kT'), [49])
    def test_case_2353(self):
        self.assertEqual(pattern_match("\rVUXXQO4N4cUEEcTY2? {,V\t+tPCK\n7FQ=T\nJq;\n\r2>o:W!_LN.:!|k\nc*V8\x08hlNJ'2Q@y5:a/%j*t*-}e_t`\t+ww\n\rz:C", '.:!'), [50])
    def test_case_2354(self):
        self.assertEqual(pattern_match('\\.}5;\x08r;G^,$hmo63j}Meo@RZ^W_)y"r d_):/v^p#^Tj+K5<[xA} $L{OeD~]{L7=OC!x5wp)*}I)OR\x08Odt[)6\x0cInyG2', 'wp)*}'), [71])
    def test_case_2355(self):
        self.assertEqual(pattern_match('9f:f{[$_6N\x08,\x08Zc.Dfs\r/krkAl-s00\x08|A[4+F`5r\'D\x0c\x08=\r8CTkaGPg"JJf$I`CO\x08\x08G(%X2\n,B\tO>)7r=XG,*5!5:U>#LM7bF\x0c;D', '2\n,'), [69])
    def test_case_2356(self):
        self.assertEqual(pattern_match('X\t<E"qm7>R"_z}y%z\'\x0bD.qTZE|$g1#*a>G4\'xh3\ts\'=M;+d9D+0"P\'NgW@Ir*KW\x0bM/SbCy\x0cM?J', '9D+0"'), [47])
    def test_case_2357(self):
        self.assertEqual(pattern_match('LB4\' \'\x0b@zyZbi9rFY*J"QVnT\\(\rE"WkZMm\x08fN>mW~T@egLQ_b/flO0', 'egL'), [43])
    def test_case_2358(self):
        self.assertEqual(pattern_match(';K\x0chQRfS \'t2w~eiW0E0JzcT+d,>LmAgdh^b\'jsZpuu~(zBJ8 8P<V\n|^NKVse`j\x08MFQr]/!~\x0b1FimTh`Tv.nFb\\"', 'puu~('), [40])
    def test_case_2359(self):
        self.assertEqual(pattern_match(')"= [3Kn@dx-MuuHFh/o\\YYU}WZ8;\'":<Z\\A-Ncc8\n)Y),nq[)', '\\A-'), [34])
    def test_case_2360(self):
        self.assertEqual(pattern_match("!ZSmm\r2\\F1@VDrd\r\x0b&uFJ1l}6x{**5A?MLaasd)tt$\n\x0cH\x0bPqg'>#&&e2,Q\x0bq,S", 'ZSmm\r2'), [1])
    def test_case_2361(self):
        self.assertEqual(pattern_match('Kp\x08M{"x$07zkKUw&vwpw.a040zlzJ\tp7n%QO2jVmyS4i%9U:qQT&Rq||_\rc! W50l@S:nnOW{iPP*0U|_n\x08c\x08e,W|*v', '7zk'), [9])
    def test_case_2362(self):
        self.assertEqual(pattern_match('92q]X{+tMq=e}F~;PlMr1\x0cWfCb+&.OfW>dn$I2`=X\n>o\nd\n7d\'*%^\rc*R\tl\nz+*eNw5]PD\x0bJ"OP-"ie0.7,D(:*@>I\tt-V?', '*%^'), [50])
    def test_case_2363(self):
        self.assertEqual(pattern_match('>SU>c]ZY(KfaDUP\\t\rjz%OYg@y!,rep|T{xet/[V$&rHMS?\x08<&+/I6P4h %(Bq|\x08>8v', '>SU'), [0])
    def test_case_2364(self):
        self.assertEqual(pattern_match("Y\x0bL%`O)j 8e p(F{S(!Xat@F'@AEVa5YgFk'0\ts@m*4\x0bE>)K\x0b[I>n)dt4nX3x5:HTS;71X\rI^s5QP,@:-o8\x083wW\x0c\x0c\\=U\nV[&DG", 't4nX3x'), [55])
    def test_case_2365(self):
        self.assertEqual(pattern_match("cz=88qe6k\n.,JG9u<OmO5D1c!c'0g1ut\x08D9btDI*y|pwJ/ism1`\x0c,:)~f%Pw\thX;~H\t08", '\thX;~'), [60])
    def test_case_2366(self):
        self.assertEqual(pattern_match('^)9J\t|*\t"=%R-3G%ZQ>@J_K<l\'Qj\x0br=/k-@?o89^oO~<\x08hEh#)$', 'j\x0br=/k'), [27])
    def test_case_2367(self):
        self.assertEqual(pattern_match('335k,*E*Jyp=gF/X6S\x08DO~i<*THXpkW:viy\n\nXcq"T\nV5r7i|\\haA7Hj0]jH\nZClW9[va4B36E#P.cn`=D\r4N', 'kW:'), [29])
    def test_case_2368(self):
        self.assertEqual(pattern_match('.W05y-8XJBlfq#`DW]cZ7RV\t=6M8o&DWe\x0bH5J\'Z&Efl=*K>Xgyr<Wz:ccutr\t\x0bU/LXaM\tCn\x0c\\S`rPG!jIke?"|Q', 'fl=*K'), [41])
    def test_case_2369(self):
        self.assertEqual(pattern_match("TG*}&}&=}+QVn>kO@/Jle@NL'JW0[MqB\x0c|8(f8!;Gyc2^Ck#TC*BU8.GW&ixqI'\r\x0cN<&V)YAe#9E", "qI'\r"), [60])
    def test_case_2370(self):
        self.assertEqual(pattern_match('NLNYcC*@zr`Um>0P_Oa{y(Y[S@5nFz>CCcz:Iqbgn=+\r6z}J<la\x0bet3RfHyPV<9]cG4{J\x0cGS7C\n)F`i+$j[', 'NLN'), [0])
    def test_case_2371(self):
        self.assertEqual(pattern_match('^I|g/w!5]?%\x0c~~"<\\q\',$\nA=cM%k\tVg34j7bmCJ<B^yW Jy:o+)*Yug', '\tVg3'), [28])
    def test_case_2372(self):
        self.assertEqual(pattern_match("b]1[Mh\x0b%ago2\x0b\n_@X3YNAV2ldN-(;F5.'y2Kw!bl~wk@`;@-tQ59g/Y7%2~T?Re\r\\(cHgvo", 'h\x0b%'), [5])
    def test_case_2373(self):
        self.assertEqual(pattern_match('\r&U\t7!tN$\x08-YQt~`|E2"d]",G\'Pas]tn0b<vWq\rXaF+Aa&hwo\x0cZ#`BQ2gP"3y_[|zraeOEQ\x08JL7)Da=Ml^1GCkyW %+x', '+Aa&h'), [42])
    def test_case_2374(self):
        self.assertEqual(pattern_match('<Q~pV\t\\ncN0-+b5e$LWGR# d\rE-SEV6<@hP<`nIo6n1;eDL"EXd=)l43$(| Z', '6<@'), [30])
    def test_case_2375(self):
        self.assertEqual(pattern_match("5Owx~\\FD$V\x0bNh@~}iGwID0]On4a1l'3GQqKr}#i|9p+tjY4/*a67\\Pt{ui49^DW\x0cLT6vBtjo.\x0b8<", 'ID0]'), [19])
    def test_case_2376(self):
        self.assertEqual(pattern_match("0|q[p6wTq5=WZB\x0bJ1X3\\oR)G}w>VulYZmS{RqvuG5Bb2N'Dol%r_X4Std[sn`Pc\r-Sg}g7s4-%>VAi?9e<0~X", 'td[sn'), [55])
    def test_case_2377(self):
        self.assertEqual(pattern_match('17+\'\x0cE4)#{z@`fq"J?e~M*>ph>bM|th s2*|]ss,co%Li\ne\x0b;~BJ`~e;`.C2/qLLQ.m|;c', '|]ss,'), [35])
    def test_case_2378(self):
        self.assertEqual(pattern_match('sYV+|/#S!Ax\x0bG{[R)zv#r2qBHAsoeTFDx*KM8a]g:AgR[D5w77GD<Bk"gD8+s5m|i.5({MX-h', 'eTFDx'), [28])
    def test_case_2379(self):
        self.assertEqual(pattern_match(")Q:jE2bMhO{#LT\tkF>cs%i0[j\x0b>\t\x08%Wh2E!I2N<H_vCzuO(&eV\\?B'22kX!;1", 'O(&eV'), [45])
    def test_case_2380(self):
        self.assertEqual(pattern_match('X$[W,m[KE?78y7WniAyL:2\x0bu^zx\x0c/tCc>N4RZT%:{%URyTp)dUdR=', '4RZT%'), [34])
    def test_case_2381(self):
        self.assertEqual(pattern_match("~hSO;7oARr@!ZIKo*cDd?\\s/'@1GOgHHCI:qkXt`;.6KgEf~\\4\nK*v vVS\x0c|#!iB(M!hP[", '|#!i'), [59])
    def test_case_2382(self):
        self.assertEqual(pattern_match("/g`tYWb&;$naq'A:Q!srY%\r|`9l6q6kI=zX6t=\\dho{oz{,_ud", 'tYWb'), [3])
    def test_case_2383(self):
        self.assertEqual(pattern_match("Y0\r@cXzlYS<'p\rh}#UW5iX<})3w?(?YeCJ,JC9D||!4/:\n\t6o/K/U<K_3>8.)@7lKxx", '\rh}#U'), [13])
    def test_case_2384(self):
        self.assertEqual(pattern_match('b )@\nH;3apm}7|bmBPAnWm pxpN\\Aa-<Yijna 3L62<9mZa$>C#%B`e-B3HNis]R}OD^4dohg-153[', '`e-B3H'), [53])
    def test_case_2385(self):
        self.assertEqual(pattern_match('7<Xc Se=[1cB6M^KYR@gMr+B:%\t<-NY/DTb4fo]BzADfU1$j>XS9BKjdV5x\x0cbI.{1PL%', '$j>XS'), [46])
    def test_case_2386(self):
        self.assertEqual(pattern_match(';|,5UEW\nD$wd#ud#6}9@BGm1\rp3YGN3\x0cz\x0c7\'5u$RxSN\x08YC+.s\'1C/?lz+G"J+Xm/H4Rq>~fdC>Gm=r2\tj8P..dmP mb', "7'5u"), [34])
    def test_case_2387(self):
        self.assertEqual(pattern_match('{B J^@:DPNpn]xF7cNkn\tcaqfLqN`7f/EDR{^9|i]_^\x08`d hIdC-d^=/^PC3TB^', '{B J^@'), [0])
    def test_case_2388(self):
        self.assertEqual(pattern_match('Co\x080(_Ijul\n \\O5*gJ~"E"xtn_2&FY\x0c/.xpy]WZ\x08sK\rd\x0ca#G\'S\x083".%X?L', 'xpy]WZ'), [33])
    def test_case_2389(self):
        self.assertEqual(pattern_match('9abr\'pn@,Fa{hR\rz/AF+;#Xw%d_k$^#q1-`ID5N[ceX"GGsi^MNt#:B5y[Ze%\x08iuQ~e6B\n\x0cY<Q2\x0b6?2t#\nvNoir4', ',Fa{hR'), [8])
    def test_case_2390(self):
        self.assertEqual(pattern_match("H4b\tF#rBhxSGoCAj#n,BU-CDh\x0cQ\\Z3-3?InZ+U23P\t%\x0bO+\x0bV=_r\x0b!d2BOs'1U\x0bY98=Q1E.7q__\r,yHApQp*drasyk~qX$", 'Aj#'), [14])
    def test_case_2391(self):
        self.assertEqual(pattern_match("{7I\x082m@]\\<@Ya`B@5W\nI\\g9l351se\x08R;uXR{<`'\x08$1\rr75`oMYKbYx\ro!\x08uv2\n[6LA/fb%nTFr\n{8oh^ljf%=k+( QJ=|", 'R;uX'), [30])
    def test_case_2392(self):
        self.assertEqual(pattern_match('\nPyP.Nw2\nwc82Rtmy<"Rql[;_s!|~>QMu`Pn|"VW\x0b\'?yIb(\r)XAaNgFD6', '\r)X'), [47])
    def test_case_2393(self):
        self.assertEqual(pattern_match("aP2pihK6CtkJ7L>=u}1\tL/3{>4*5O4QXgU]u+S)TOeyS@`0rh,M)Pi~TB6E\\'gfrut}+6R77P|P{Uqx\x0b^hzxR0\n", '}+6R7'), [66])
    def test_case_2394(self):
        self.assertEqual(pattern_match("A\x08J<8gCm\n`cdPZ-&i-QnGNkc=Htezms)L\x08[.\\4<1X'7WU*X2{eb=eM_>bq,^.Agbs:cDG\\p\ntQ.NRc^", '&i-QnG'), [15])
    def test_case_2395(self):
        self.assertEqual(pattern_match('W|5Q]K26\t(:Ex 0J<_DFc\\VRxq4%2EF\x0be\\1zr5@\\ik1,ZqnRK_gG=', 'W|5'), [0])
    def test_case_2396(self):
        self.assertEqual(pattern_match('mK_qjL8$yr,mD*x?j+IL9SF~rx<*;(\\\\W(n*5Tb[V|wYv=s|>}Qt{`J@\x0cx23mx\t#5s"*|<1"t^o>-~@1Utw>3_OK', 'w>3'), [82])
    def test_case_2397(self):
        self.assertEqual(pattern_match('ye=ClAD<n$]\x0c\tk\tz\x08?&.!P@{v?nY?2#!\\qs z=gty-}A4]$\r(8!DX.THid5>t$%K.|dM)v{ZihUwK9c*pksH$J"<T!V5/6A', '&.!'), [18])
    def test_case_2398(self):
        self.assertEqual(pattern_match("us5z\x0c\x0bY\x0c#8] rcPP3Z}efCo~\x0b4iq(~.u#UmPYRXQRF\x08[j\x08jXS\\\n+\x08=+QV)3U'G3)]L4s)T%Ktd=-K", '3Z}'), [16])
    def test_case_2399(self):
        self.assertEqual(pattern_match('-hPQ5yyVG)IhEv\x0b7d"H\nJRQaS\\O,PG"([31gpgBb.V/^q#dg8k\nt++[', '[31g'), [32])
    def test_case_2400(self):
        self.assertEqual(pattern_match('lMq:IW\tO?;;2nkYVH{EC9%Ms:b+(Dd\n1xY^vgj?oa3KCJ3?u58Ze>9@bup]{Q+h_S09cX%/OEn,%R@pe?=~KNU=!T.4uZv6E', 'gj?oa'), [36])
    def test_case_2401(self):
        self.assertEqual(pattern_match("'$A$|2l'+6{9hQX74aP!W=t\\R@}V('0@GeYb5Iuj:,nN\t)u\x08Y|?s{8`:OSH", ')u\x08Y|?'), [45])
    def test_case_2402(self):
        self.assertEqual(pattern_match('N2Uc\\Ov7-Qs0b^)[~BzW..[9[BG~I\nzSrJ\t"u#r,crVKD\t\t6(|3\x0c\t 0_7p4v\r_', 'SrJ\t"'), [31])
    def test_case_2403(self):
        self.assertEqual(pattern_match(')@|:]om!s3iwE>a[AP,c\'<PVpeBP]y\x0cmR]a.J2V|xt^L#Dk?u?_&Tm7CtW[4o"2&Z;Z-X?V}(|W]Oi$j7,\tV*snYj:,Qo]_\'h\x08c', 'V*snYj'), [83])
    def test_case_2404(self):
        self.assertEqual(pattern_match('zh\x0cf82Ou,BY)"vfED~~8tRLSvIUv;l}qqB"G*+P$f>X\ts\x0cE\x0cz\x0be~ia\x0b~d(NeG?x.s', 's\x0cE\x0cz\x0b'), [44])
    def test_case_2405(self):
        self.assertEqual(pattern_match('1|u]R8z.ew4^\'{/Is\x0cF-QXRq\x08U\x0bB\\2va%=E36"V[JZ,t\x0bOUnQk\tX', 's\x0cF'), [16])
    def test_case_2406(self):
        self.assertEqual(pattern_match('-+IC!v7k.Dib\x0bR6zLC\'\n+|=Iz-?\x0cyY\x0b7xRs/RmjcGdSGL5*_\\ lJg2Y_dS)I_`h\'C: )&o%8);/6t2bU;t"a\x0bj]_t.,l', "`h'C: "), [61])
    def test_case_2407(self):
        self.assertEqual(pattern_match("\tF@_Z:H:UPDj7'>S*xjJ3;.4x9>7aR=_nv/O/.fXrJL6~\r7Z;\nz", 'J3;.4'), [19])
    def test_case_2408(self):
        self.assertEqual(pattern_match(']hY`!8z/k+O(\r(~@z\\e/a+._u`#q(#\rWrlXsqeP)ONy(OM=8\x0bhrFBgd6o%m=jZ', '8z/'), [5])
    def test_case_2409(self):
        self.assertEqual(pattern_match('R;\tavOpYMujdos\ncEwj){|/?A32 \n|6%O5YtRFEb3$#-eBWRaCSk=gM=\x0bMVB&"<~h8^y?TPn4UG%)x\x08@\nyKyu(t0}C|\r7$', '\tavOpY'), [2])
    def test_case_2410(self):
        self.assertEqual(pattern_match('DG.<B5uUI\r.9N\tb\rM\rU=X,N;UACH\x0b_lG`i\tD_g5P)S"$.TYftHdK!\x0cXQ81\rk9%3=caXz7aZx6DrU_.z%DKMg|', '6DrU'), [72])
    def test_case_2411(self):
        self.assertEqual(pattern_match(')\\ .Md/F\t4u\x0c#d/;|#gEKsOg]`+I)3H!M?o%^_Sw>\x08d>Fe<lv=q?+A~H`\\#;\x0cN', '^_Sw>\x08'), [36])
    def test_case_2412(self):
        self.assertEqual(pattern_match("MG)G&y:kI7ASX#X:Rb(dJW}8?YK_'6k0*6EKV%V&4636H(:j/Efnv6Z,lMn|%O#hLY8#Vx#,){?R\x0c@V\tfj]4", ':kI7A'), [6])
    def test_case_2413(self):
        self.assertEqual(pattern_match("Z<\n;X&#-YNUK{6\tFIsTb{:94r%=ie^u] {(SpWGyt'A/JQB\rN\x0cX\x0b]5W+28e@CW\x0c]tZV", '+28e@C'), [55])
    def test_case_2414(self):
        self.assertEqual(pattern_match('k2)\x08F/uvmU\\6Yb}D5Lk?NEjF8"n*lH$6\rCvWt":`<0"/-J\x08s87H?Dax=\x0bGm;R3>75.Pgui=*ziy9[\t|1\nZ(rZ', '/uvm'), [5])
    def test_case_2415(self):
        self.assertEqual(pattern_match('fw~#Ndc\n+roLjr~D)JBe_\x08F9?>M5y2J@\x0cp]/!jao[KMz2T\nxGv', 'ao[KMz'), [38])
    def test_case_2416(self):
        self.assertEqual(pattern_match("OUa\rQjHiV\\]'4&9\\28wf.P=(`wr7eW$NcPB\\a(Qu(V):6\x0bKTSA?~6mIyx4C5jQF\x0bAdnL?zD4", 'QjHi'), [4])
    def test_case_2417(self):
        self.assertEqual(pattern_match('|2"!JIHRj4K@AqNn!=&xBwToTe abJ%m|FBU<uXWKs\r/9:t\r+x63=^0#7\t]mG1;%mJPc4HaH>ih&Ze~|[.c', '@AqNn'), [11])
    def test_case_2418(self):
        self.assertEqual(pattern_match(" Mr;!]sK!`]i\\*[d4cL*=\t<\\K:S),0{lu[`(c\n&b-(%['rrN+ihP(PXOzuB.M&|M\x08\n\x08xU\x0cW\x0c!*c\x0cd%", 'd4c'), [15])
    def test_case_2419(self):
        self.assertEqual(pattern_match('1\nJiMf2\'"r)+v_(&DxFntU63X(J$V%:vVO6Bo1F$356>IC"@EI+:6Uh<)6\x0b:zs=G`BTI"3S28>A\'I@6"', ':vVO'), [30])
    def test_case_2420(self):
        self.assertEqual(pattern_match('1VFn:;rdS\t pkCo-shNJ:>@x/_hu"Mq6)uERtk8Z2v>^&|L+hE%O\r"8G}d6U&5r', ':>@x/'), [20])
    def test_case_2421(self):
        self.assertEqual(pattern_match('p:`\t<LPF/v"&f#+q4r0(KZD\\Ht=,fUx]\x0c4_,(wQ!, vPh"o)>r)>\x0b|\x0cPk*]2ai,{281o\x08oFV}k`8i{YvMWft3,Y$8n6Y];\'^Wa.\x0b', 'D\\Ht=,'), [22])
    def test_case_2422(self):
        self.assertEqual(pattern_match('w-Xhz,l+]cjf{26`s9@AoZXX0;%F``p9dEG\\^A9N\'Ya}`TXu91n\x0c}px6^D(\r</*\x0cK\nq?/D>"0O#DZ +z*,\'E/yYGN4SAy\n', '\r</*\x0cK'), [59])
    def test_case_2423(self):
        self.assertEqual(pattern_match('fE.%S >9faK(C5b*xv2q\x08M)~.S\x0cUi|}U"00|3n_\r?~&(CI~bEH_L~5 R%c4T:/h`~T$c\x0b0FC(g4s\\;&F', '~.S\x0cU'), [23])
    def test_case_2424(self):
        self.assertEqual(pattern_match('wzG)y3*S0`r,|qFJ\x0bD8NKI3Cvh#7\tQoz\x0b,KVPhA\rciyK_ }z}eu\\\x0c=0qAeY[D%\tRj\x08x!"\n<=tVy(lp~1%H\x0b}W', 'tVy(l'), [72])
    def test_case_2425(self):
        self.assertEqual(pattern_match('"-4KO4C!\'<]+"Vvg~PLZk`m~vpv?&dp&9J\'Ez`302{nxdWU~=pLH{\x0bc-+*e?K$@f|sR=_FE=:"/o);6UNW5DEik)iZ"pBd', '~=pL'), [47])
    def test_case_2426(self):
        self.assertEqual(pattern_match('m~PN2w/"dUu\x0b\x0bcyJ5!O\n-{Oo"\\#\tVf ,\x08)_SnUQ[*B0Fn;s|O,ZqB>\'n!Dw#GNU57tjI', 'Fn;'), [43])
    def test_case_2427(self):
        self.assertEqual(pattern_match(':ux%{<\x0cB\tw#NJKZ*W@}:S\tB\x08]tTb%+8$=Myf4mT&BSZ4OkO[6FL\n7>1`5AH7)\']#&ym"m@v)', 'NJKZ*'), [11])
    def test_case_2428(self):
        self.assertEqual(pattern_match('ZC!ZNl)w`iq\tU\nu^c\x0bGG*|I@:T%Wz&Zj")N\t%?\'C\x089?}g)o#1~U^S!d#j$6NWk^1vk26&*8e\x0b=z\x08p$\\7\'A7<9P:"mKeJ``g', '7<9P'), [82])
    def test_case_2429(self):
        self.assertEqual(pattern_match('n@/<cc\x0c!>\rcx4+r{B{]%J9N37m-lZ"`H\x08}kPh(*6k74MP`_AS\'\\/(bR1CocQ', "`_AS'\\"), [45])
    def test_case_2430(self):
        self.assertEqual(pattern_match('-=f\x08UbqjS0+`YAED$agM\x0b=oRYQUAc4sVU|TuX!EVOb+t\x0c&mytjEP=\tqhsp6+Oe>,jC}vU]@', '6+Oe>'), [58])
    def test_case_2431(self):
        self.assertEqual(pattern_match('rp45\rn>`8$6qA"1}T6(u\x08{Jz{CA$G-{*0;)q:@J1Tf)Mj]o\t=1OMLv%lv}&X.R:\rPlOIAS^5}8{WWEiTv\x0bP', '}T6'), [15])
    def test_case_2432(self):
        self.assertEqual(pattern_match('N\\&2=Qr>zPx>(Hs:i)b-ITXr*.P_-J&Y+z\\d"Vz}[<+(<{kw.Q', '.P_-'), [25])
    def test_case_2433(self):
        self.assertEqual(pattern_match("i;g\no'vS[uv0\x0c!<j*kd-K@w\x0b=kqHp(Gbib|+N\n\n.qyix|l*Ol+6myCyVKV", "'vS[uv"), [5])
    def test_case_2434(self):
        self.assertEqual(pattern_match('\r=oG0_2L(C`S8Ni]8.{^GqPdZ=s${,W|q\tEAW]F6KaKPXh*)D"q)bR', ',W|q'), [29])
    def test_case_2435(self):
        self.assertEqual(pattern_match('pdK%*;77\nnkxatYG|2Ea*:8qz<\n9fvj>N_aY\x0bUI$[.\x0b>s+[%DuS2DsYNc$\x08mJOZ@)7iW{', 'DuS2D'), [48])
    def test_case_2436(self):
        self.assertEqual(pattern_match("S7Vpjh&E^,:k?X`39L Ee#iOwte\x08xJx0Kik#\\a\x0bPXS . >r'86d^u~Rz4m\nZ>:vS-f\x0cpV9w", 'u~R'), [52])
    def test_case_2437(self):
        self.assertEqual(pattern_match('Q;:n>(e{bXhj?aF ?^H\rg&\x0c>nsKve:t._kExGjv\t&{b$,TTr"\x0bL)-xX*NWb\\=Awu.X]g', 'j?aF '), [11])
    def test_case_2438(self):
        self.assertEqual(pattern_match('G$EmC"d2DDCwc0/>KA#;\ryhEc5K=:O\roM8 GRW kFb6\x0c@lrujdcj\x0cbSF8enO42TyN', ' GRW'), [34])
    def test_case_2439(self):
        self.assertEqual(pattern_match("a/gW&Mkl0W+*^\t^^/H3M[ZH4*\r$6jV[.Y'Z;Jw9('r\trS`+_laE[&&[c\nxyxpz:hvpC\x0c;`=V", 'W&Mk'), [3])
    def test_case_2440(self):
        self.assertEqual(pattern_match('ZpZdb>HOG\x0cXhXU>e"~,fHa5k \rNv61PF9Ht6^g;8A:\no\x0c)fs9xnG)X[XRfx||9J.a', 'v61PF'), [27])
    def test_case_2441(self):
        self.assertEqual(pattern_match('M|f(w"o&S\r/~$}$r,%Eu+aJl-PsT\x0b[8>CZN^i@@-i!X*reG09.YfXK4,34>?Km\tUV\x08rumy#r\x0cW5\'E]\x08^*\x0c||v!Es>5', 'T\x0b[8>'), [27])
    def test_case_2442(self):
        self.assertEqual(pattern_match('jyt>5[A,%!\n^`Zet\x0bv275m\t\\&{@*x)\t\\Qqfy[e:PS<1@G}.7pyQwfS1WZm{Y)bO]>8.}>gsh[25;NoFp\\FD{UWr]u%', 'sh[25;'), [70])
    def test_case_2443(self):
        self.assertEqual(pattern_match('e`2{MWhDn>bH<ZF:\x08b(@nqKG7k2u+WwN4.kYdu`"b&\x0b_l\x0cDf9koVWavd3e=', 'KG7k2u'), [22])
    def test_case_2444(self):
        self.assertEqual(pattern_match('6z0,\'Krh<:Rc3Z6\r~[oqSA|lS>F]h%\x0ckb^np-8D~\t,EVRPj-iFuC\x0cygA&[\r+\\-6hK5U"qH=F;I', 'A|l'), [21])
    def test_case_2445(self):
        self.assertEqual(pattern_match(')cO%GL<6D~cl0N$!v{C=&^{r\nM}62,06. ;[FnB;y[QzZBSf8x%M|07P5)h%&\x0c(_<E?mc\x0b`WIwGPdDK:|\x0cv', ')h%&\x0c('), [57])
    def test_case_2446(self):
        self.assertEqual(pattern_match('kqHT^s"3ULQt\x0bi\'lLQ6\x08\x0biH)Dn[\\T|0|5vc/^[Jjju"cl2h\r4bN\t]"a\r+Js\x0b\\#2.u', 'H)Dn[\\'), [22])
    def test_case_2447(self):
        self.assertEqual(pattern_match('dK>4hyR1<^k9j+A\x0cG.}Y_&\r^\t]9<8-bU]+|*t\x08\\fP,>]/&tt\x08JE,(}\t/hj,K\x0cW`plR#u2Qq[a]\x0ccg[&\x08f "{yM/\x0bQ5@KJ"', '\x08\\fP'), [37])
    def test_case_2448(self):
        self.assertEqual(pattern_match('9)x7!7-|{UL\\tRWj,]_n2=$J{dxA\t?~tiV!UaCA%7(9xg-]#wY7./Q7}^:!el QC:J5;:}iteIO^D8"\r<L!8l9Pc9XUtyi^\\', ':J5;:}'), [64])
    def test_case_2449(self):
        self.assertEqual(pattern_match('C9`vjNT]HHqR`^xiKf70h\to]Mpd2aRP4\tmd6\x08,3_&GN=Hmhy e=V', ',3_&G'), [37])
    def test_case_2450(self):
        self.assertEqual(pattern_match('}XVTa7AY\r[\rb]\r=zs?_1`59KZ%UBq\t;hK*pfZ/tcO&\\/+,$K0l-Paz0FT6;l\r\\6[jEDX.cqC{j/+}L*{r}7Dm2zA)7}v', 'O&\\'), [40])
    def test_case_2451(self):
        self.assertEqual(pattern_match('1%0\r+K7x>q%BM{jTBSb0\'h*ZNb\rcmt/8{EAVTP+\\O%Bk1lBB8yw8C2VAR\tN[4n\\\\fD*\'jz"S3', '2VAR\tN'), [53])
    def test_case_2452(self):
        self.assertEqual(pattern_match("_rr'm)10G/Sz2,[a$A4+Cq+7\tHTnS)L7Mh\x0cD,SOJ45PB(fgIf^\rgs\x0c1\\5X\tIO|S(g.'Fa oeZjB.| /6($I\x081`NOK|E+k`3*i", '\rgs\x0c1\\'), [50])
    def test_case_2453(self):
        self.assertEqual(pattern_match('91}e?M\t-A?T@_]r%@q$\x0cx@\\i>M*T|g }dxaA\r!*]C#v(\n\tK i&cadAN^pq;U`I2>?$+)Ug.]]Rhk\x0b', 'x@\\i>M'), [20])
    def test_case_2454(self):
        self.assertEqual(pattern_match('C- OLs*PS90zL\'vk><O@9PM%7(9?&3 =-Y4gziKc\x08{|JAi\nQesZxt{cD(/?"}T', '-Y4gz'), [32])
    def test_case_2455(self):
        self.assertEqual(pattern_match('W[1N grZ\x08\rc\x08&yx\t@Dcg`n:Y@Mc7QA2k\x0b,bnM- E@/$L:M!oz^U;d`&a@+\x0c<Vr{<z9Q+k;f#kghSu}mIPs.[AKw(1YArh=m', '\x08\rc'), [8])
    def test_case_2456(self):
        self.assertEqual(pattern_match("6\th]4t}~eCy3?K:7?Vf=pcDH7vMpzXmH90@QD.fFJQ>{Ix]U9fp%:nU%:}Je2HdEn@x-b\x08Iy$|'jAzK+ !-zX0", '@x-b\x08I'), [65])
    def test_case_2457(self):
        self.assertEqual(pattern_match("we-o(qjYW>_.nz\x0b-v/2%v<XX(|KE0\n):.q\\PaP>\\Q.uS~wQ;$\x0c$:\rEaQ[L%[X_\\zDs\x0b9Ypoiy?-HrN.@3/hG(j}{W<4/el-!g'", ';$\x0c$:\r'), [47])
    def test_case_2458(self):
        self.assertEqual(pattern_match('!\x0cg\nQ[q^k}Qo!-\\M\'Nu;"RZWv;//d}v=jpiLN@:^IP@F/ICvGNDC*PU', '!\x0cg\nQ'), [0])
    def test_case_2459(self):
        self.assertEqual(pattern_match('`o\x0cX?QlVg% Ty`JM\r80bt[U(MrYSJ\x0csxo}>{<HW\n\\0UtBZnR)s ix5E !B=^f=dR=8^S}br_*LAd}|AqXT,O', 'S}br_'), [67])
    def test_case_2460(self):
        self.assertEqual(pattern_match('RM\x0bIAV`Kp"b\x0c*Wx-*:t1[FZ\tN.\x0c\t.m~jo~`aJf@\tfu4?:n#7"+\x08+2|>\' 7>r9(k|tw\x0bjtS?W8jZ&:M/P-&IQMQ[byIH@', '-&IQMQ'), [80])
    def test_case_2461(self):
        self.assertEqual(pattern_match("ma(Wlw hEL\n^H':GxL(}.,f@@\x08rz~6os82nO`;KN\x0cqN7a@dmnf+RsKII(ur;;e>5'.$2!d?j", 'N7a@'), [42])
    def test_case_2462(self):
        self.assertEqual(pattern_match(';`b{LS\n#B=}%O\x0cnE8t-o6i@%f*!aQ;q\tC+EB$nRXBx6\n-dqsbsXRZ](9PE]N9HB}`wy@\x0b', '!aQ;q\t'), [26])
    def test_case_2463(self):
        self.assertEqual(pattern_match(".1g6?,AC)!4j@rQxw+;>%AEn4-SV'ket%7XlBtl\x0calN,Y~tTh?$UEWI jmg~G1&_ l=?Q\x0bT+G&\\x3\x0bc\r\tWx_>99ME\x0c", 'G1&'), [60])
    def test_case_2464(self):
        self.assertEqual(pattern_match('q(>H*_\x0cz0\x0bjRbHW?\n(tz:\n:mG< LTr#q`EHbD:ZvOx,/@jF+FNhRDB-1EFp"p\x08a-wVdU5wqH!{BV3<(>S"5WHF', '(>H*_'), [1])
    def test_case_2465(self):
        self.assertEqual(pattern_match("\x08C\x08>^S^9&f!CSD]rE\x08Ljla{|\t!'u}\x0c\tJSg.^m\\o\x0cczz.\r%/~X3mS>_LhAE;tV!,1bcb;bRJ++~=^Df[v9G=Y2k\t_xVMJ\x0b<#[@-", '\x0ccz'), [39])
    def test_case_2466(self):
        self.assertEqual(pattern_match("$I4K5LVpwcR:'P@K6 a_C1qu5F?q@R~=WU]}v5&lFlj@]5hMA01|#q4&:w*^.H1 :F(]m66S~TUZZV\rW'r97e\r", ':F(]m'), [64])
    def test_case_2467(self):
        self.assertEqual(pattern_match('\'lQB_:\\~dA>vumvMdnLert\x0bp]\x0ce\tH\tqP.JGLC7,jhE[^6R:z21Y\\\'[~|\'SI@#8$\nmKni=-$-=R}GK\x08o"GZ2Y', 'i=-$-'), [67])
    def test_case_2468(self):
        self.assertEqual(pattern_match('T\\ /8ZgSqjd;8Yau2A63d).Boy>O|q\x0b>f\x0ceQlJ2->+Xwy1b3[L]ZO5X|/o)-2_d`g j9', ' /8'), [2])
    def test_case_2469(self):
        self.assertEqual(pattern_match('y=~6kf^+vp&\x08/\rc?gGz\n g u|t# tv: -?(jbb`]@9zZD>DB0oA7@9\tY\x0cuNw.Fj3JqU63O#D', '-?(j'), [32])
    def test_case_2470(self):
        self.assertEqual(pattern_match(';[% a~pb?V4?<[2A_DVG\\"xi\tiX\x0b\x08Q!n1\x0b~4:"\x0bzB/t&:5\x081wcw^0UNjb\x0cc+HRP)owjq9(Y:UL:V\x0bebS"J=Tr> l3<\'U', '4?<'), [10])
    def test_case_2471(self):
        self.assertEqual(pattern_match('Qm3\\\x08;9zJsL~5d"#&PGr}N\t;8>[:@ic)[=c`yGrZV[ rn+0(Nw\r56{5s`M9)C#1p"9q1jpp\'\nFtH!a:|M*N7k\n;F$bWw\\W,\t', 'c)[='), [30])
    def test_case_2472(self):
        self.assertEqual(pattern_match('6 zP;iE/@EHGPQN3}c@[qGi5Qcah@\x08\x0c9`30#_5[wqv>@\x0cE}bRJc%[i6c+sTL*{_J=s%QW.r\x0bz1$tzs}T84jDCxU~)\x0ch/tA', '%QW.r'), [66])
    def test_case_2473(self):
        self.assertEqual(pattern_match('>%4LS2eV\\|z{q;}i:$smo$-(=Z\rfe<i\tFYif07bVlPw5N)UYcq{Z%G\\<&?>nT', 'Z\rfe<'), [25])
    def test_case_2474(self):
        self.assertEqual(pattern_match('Q7,V\ragrAS}@JW&"\n\rEGjGp-4&\x0cx\':\x0b>nXvlg"GxSY$$v TJ*,{/xF>SqstY770R{uQ/{x', 'jGp'), [20])
    def test_case_2475(self):
        self.assertEqual(pattern_match("rp\x0bcF\n}SgJs+]d(lNYkK~0.'6wtp1Z5;=TH#N8|F<{F+ENur\x0bf6.1?3#~o", 'YkK~0.'), [17])
    def test_case_2476(self):
        self.assertEqual(pattern_match("\n\x0c9e|/ UBj>' tO_zfh@Uo<MBf@|{szIPQ\\WBSV\\o\r-8\\HDXJ\nTR57%+!i:{t,\\)7vT{Ia :|bI(:Wwx=d/z';8LN", "z';"), [83])
    def test_case_2477(self):
        self.assertEqual(pattern_match('dvG^Hga_~blM85^-FpMi=j><U[p9u\x08=s+hk2&{$n_3crLS?:E9kDH(|~{_\x0c%', 's+hk'), [31])
    def test_case_2478(self):
        self.assertEqual(pattern_match("|F]58`j$QIx7N{8~:\t)7%#Z{|_(\np|MVG%;-tf|+/1&%W\nQU\x0b6\r-N='/{whD:xJG^.vbYU\r^eY@aHt!ZL", "N='/{"), [52])
    def test_case_2479(self):
        self.assertEqual(pattern_match(")/5O\x08{Lk~7!osnIu90k? <kh<ADQ_<}\\s\x08y]n+qV\\~&q]z|)^FHr\x08[bpL, t\x0bZY\x08`\x0boJ],KbN2H\n1#'m[\ne7", 't\x0bZY'), [59])
    def test_case_2480(self):
        self.assertEqual(pattern_match("~6QkGdjc@~R>\tzk3y\r{kp:k&e~dvchS4MbMVn\r^SwsCr4r*CV)a}[N|%Rev'M&?z@.\r|%db5\x0c,", '|%db'), [67])
    def test_case_2481(self):
        self.assertEqual(pattern_match('(J"r:pqy}T1LcYNqvs,(x1e}{f`RqNeD :|"tL u\\@Zfd;X}<b:`dU#DmN7zvV~_7C!\x0bXpCDSD4', '~_7C'), [62])
    def test_case_2482(self):
        self.assertEqual(pattern_match('Z"]MAJE_wP\n%S\rtZv)D@YoV9\nD*N^[G\rxLI]tcM2m{d,o6l<\'e#dVR67\x0b~ Ubb)(QDI]\ntaOX/"K?Lbn\tU)^_5Msmum!B8,g46 Z', "l<'e"), [46])
    def test_case_2483(self):
        self.assertEqual(pattern_match("~\rg.5D.ga\\X\x08t8n]0htg9=u>8]!<?gEgk4X'OU=B+#w%('jF\r\rHAV7$pS\tI", 'D.ga\\X'), [5])
    def test_case_2484(self):
        self.assertEqual(pattern_match('pRJ\\1XEEx&G#:P;-6^!ztVyy=?pz)?B\\:<w+kW!\ru0E0DIa+9{K|k', '\\:<'), [31])
    def test_case_2485(self):
        self.assertEqual(pattern_match('}ob.qK5?3[.mW=?54\\=\x0cC,7i[=:1Wmss?VCjLhz)C=wiz~M0r]XA$&\r}pN[v\\-*jy\x08QbB\r%ml+', '[.m'), [9])
    def test_case_2486(self):
        self.assertEqual(pattern_match('bK{\ru^D\n7DSl=y6+Cts(V#9l\n!|/,[sgiX[/e\r84XE5\x0c{p\x08g*XN~Y}VTf]i\n\tVEXV', '\r84'), [37])
    def test_case_2487(self):
        self.assertEqual(pattern_match('8)o.x5$km\'\x08twz\n6S/C|"~xE/=iOEhRF?FN6`:+S_ra,&u-IRN0|VMMqDpd', 'FN6'), [33])
    def test_case_2488(self):
        self.assertEqual(pattern_match('\rI9\rk@smCG!+:g+|IW8fr< ?,dX6"yX]Qc)&Zc7 P\\\t6W7EfZGyg+$\\\'_Mq\'(W;YXA3`owNH#>+6bPo|UTxa-Up8,t6', '+6bPo'), [74])
    def test_case_2489(self):
        self.assertEqual(pattern_match("\\4$a=)o10=+fOiY&<KcIV<an3{?Q:/lbnfPgy3#a'p}o;h.#Q#Tp m`=t;vkt", ')o1'), [5])
    def test_case_2490(self):
        self.assertEqual(pattern_match('.V&r*kxJl^b\\JvXJ\x0bE:=b:[&``yOz\x0cdW-]ArVI7\rjn&M,2f/XxhmHK.2D-kb<}S2}I|V#a%\\q&x+!9~J', 'E:=b:'), [17])
    def test_case_2491(self):
        self.assertEqual(pattern_match('5WG\noA;6[(0sG*SA#PM<rkK?-nGU87I=l[bZ;j0B/Z\tU*v8tOl#sB+ugM9\tu', 'Z;j0B'), [35])
    def test_case_2492(self):
        self.assertEqual(pattern_match('\n?:` ?={&L\x0bBq`2m}fR%ve.O!v6Il,\tJI"b,@>  Vhz;YHp1Y&1@<(gEU[D<-imdTk"czNt^z,', ':` '), [2])
    def test_case_2493(self):
        self.assertEqual(pattern_match("UP[X%RF5'JZ0Y#_anS<+buY[n*Ip%SX\rN\ncFs:5b\x08Q?{rOKn<QQ+_fZ|\x0c8it\x08&K{EvGf$L^R\tc}kD(?.v+!>1-tT@=?a\x0b9", 'buY[n'), [20])
    def test_case_2494(self):
        self.assertEqual(pattern_match('=/h#5=e>e\tNp{A5rrleRW:Z{KU\x0b6U,bxN\\;\n*:OvbwoC|Mu(G\\=3?Cz2,>:jTdaHB=w2yG0ruTe__Q~RT-2f', 'Np{'), [10])
    def test_case_2495(self):
        self.assertEqual(pattern_match('O9dR0xl]Mm[W{wWJNE:GhEC\'yjL[K`;j1c%%\n@kvd\tS/B}nNwUk1\x0b4-faqUhBi\x0bB`Ym\'<"gH \t0&\'8\rev?DZ6H5z_[yX', 'GhE'), [19])
    def test_case_2496(self):
        self.assertEqual(pattern_match('8`\rd#e\x0b0wMgFo,vX4K.gS+DPky b\x084mp\n\x0c\x0bEBrZU*/s:Z-yz"Mr\tBO7qd5BxGuNON!mZ<O(>Kl#_v\tmLAA#/SL\x08}YU*W1qE', '"Mr\t'), [48])
    def test_case_2497(self):
        self.assertEqual(pattern_match(']x-Q7H-Z8\roHnTvaC7ggL|:\n+\rFxksxWFO\tfgE6`_HUg\t]N\x0bckaRNVO1}]Zq1=M8GVR&ZJlNu*\rO\x0cQ\nf!1_<XuU=6}?k1r]P', 'g\t]'), [43])
    def test_case_2498(self):
        self.assertEqual(pattern_match('zCh2NnB\\+`D%KWw@69&\t\r&pap/-HeF=t\x08F`@|7pSM];V}\r+."xXHZQEU/W|n:]3\n', '&\t\r&'), [18])
    def test_case_2499(self):
        self.assertEqual(pattern_match('\n~}iSHk`9PUmoz,h($:;-\tOP3y\nsI-]|HJ@K7F?KDTA3l+Z[aQ<Z/qR)];]Eq7B8Q+)', '7F?KD'), [36])
    def test_case_2500(self):
        self.assertEqual(pattern_match('>%pZ4xjQ>=ih3Bwa\\),\x0cX?!2qyu(VTZGfJv\n,\x08z[{\t]:!3!C)00pnVCDp/VJW&z;#b?ygUf7P_G\x08-)u03a*\r0eY|\\}H-+H', '>%p'), [0])
    def test_case_2501(self):
        self.assertEqual(pattern_match('<,qGNZt4vb}+\' lNkToM#gZ}8e@xr\ns\nFw`3;u^7b<@%9Nl8/K{2paD0\'JJ_?L70^?MS^[+"q\t/Lg6sPJ[7_scfw%O%p', 's\nF'), [30])
    def test_case_2502(self):
        self.assertEqual(pattern_match('($YP"KR7_$~\'mt{,R_lk)m;4Do+\x0cY{A@x_AU~+_;xN,:\rE~YiJL|4\nV3J$5\tz\nh\x0be"*dS4}~\n\x08eIe$;%tXS7*VMO;z\x08q0K#7 soP', 'k)m;4'), [19])
    def test_case_2503(self):
        self.assertEqual(pattern_match("V'4}6_v\\i\x0c=nKJNHZF(\\\x08>?WOt'Js@@`%cG^d Pg\x0c#)9'!?rqo@Jmrlu\x0c\x08]4i]Ha{Vl|$}(\x08o5MUn19N0?m(\x08u\n", '>?W'), [21])
    def test_case_2504(self):
        self.assertEqual(pattern_match('(\t<B L$k-gZF@*\'?,\rQGn 8?h(n\n9:iZE`\'!2%oGd\'G\x08FPW!G]BWb\\^"Z', ']BWb\\'), [49])
    def test_case_2505(self):
        self.assertEqual(pattern_match("sn7^7@p* !b |]'mjJ ?bA6M=KBx`]0Kv[bfD|\x08Lq;Nd/zir=y+r9S\t)={56|76v#RHK)=9\x08D}|<A", '=y+r9'), [48])
    def test_case_2506(self):
        self.assertEqual(pattern_match('O\\[|wji\tN^ir2;3}]=cg(IR"mHLP]$!ikk\\_-OX,/6>`\t?R``{L\\kC@|\rN\x08I\x0c[`C]1kDglp.p+E \x0b\x08o}KA9ZNH-3y\x0cii\nt@m\'', '\x0cii'), [89])
    def test_case_2507(self):
        self.assertEqual(pattern_match('!.B\x08m63\x08g"Fl&DBGT+CWc\\R\'/;bn_3PJdI&)g|Th+FD\tEf>v%_Sm3I\r\x0c\x0c{gPC4AgSzd220hsymGF\t', '"Fl&D'), [9])
    def test_case_2508(self):
        self.assertEqual(pattern_match('H\tl4\x0cQ.U2)XWG7U_-wdNKq\rs\tkY.\x0bOU:&m\r\nc\x08dS@je^Jf^Cx()U6dFZ]{8p`@V?Dv##eMtvn@Rk\\aY%', ':&m'), [31])
    def test_case_2509(self):
        self.assertEqual(pattern_match('g\rJTG>\njp5c ]~6B42o1hz;K4=g\t=&%()c\t|D\tPkUoC<\\Vjw(1W\nBVK|\rtg\\lVO j)!\rZ!\x0bX{w\n4GdX*=_g#gg64C"$\x0b', '\rZ!'), [67])
    def test_case_2510(self):
        self.assertEqual(pattern_match('Z8;@Ms`T<7.6Z$2%$a*["\x0bB gd+e:-Uk.>V3a$i-b.F1\x08\\\tG8MTv\\[gn^Cfb`flvW-uXQ"v%;rSc', 'uXQ"v%'), [66])
    def test_case_2511(self):
        self.assertEqual(pattern_match('Wo\\e;a\x08ByqPv[YZ\x08F$I=nmdmAD}t/;T`rM%;xfE7 0y1*Y\t@Q*sl]B\n@X<Pm{\nulZvVPt-uJa#39nOkHX l-%', 'OkHX '), [77])
    def test_case_2512(self):
        self.assertEqual(pattern_match('{XJ\x0c-Q4]\x086l3|\\P/bl\\TaKa-hu-jNLg{_..wHQ[^VoZ,zxhOw\rI^GX&\\#Ru', 'Z,z'), [42])
    def test_case_2513(self):
        self.assertEqual(pattern_match("RO LX\tR~t^G Z\x0b+y;3{ZFJUR Lcd4yd,ht\rd#H0u,pZB3^k9}BPN\t!GK7M7=\x0cq`J?.38lkMlGI\nI'@6z23>iF^$\x0c,bd>Q\\z)(-", '\rd#'), [34])
    def test_case_2514(self):
        self.assertEqual(pattern_match('XB%o9kit=&-bGBXcDiR9P;Eydm}P{T{*\nt;]!\ryALSjmaU]>]L2sLv;V?BsqYr\x08"Eva_Z$c,=~/C.Vo=4f)hB(>/.1Z|fN4&', ']>]L2s'), [46])
    def test_case_2515(self):
        self.assertEqual(pattern_match('5r*|Et%Ln2 x,OCb?nts,\t[5\x0bF hrmN&J1K==t%pS@&O]pL+cu\'G@N\x08_<">{60L"Xbr_/IK\x08uu%\r~)mpHUF(N;^*[8!jz', 'r*|'), [1])
    def test_case_2516(self):
        self.assertEqual(pattern_match("pN\np\x08cW~m9%3neWhi,8YD^\t9E7>$Cer#`S(x.Q\tgVLEiZ\x08\r2Lo.'QE@igFL%2&s{~-BkL5G<ifeH<)@C3d3SE-6!v):4u7\x0b", '\t9E7'), [22])
    def test_case_2517(self):
        self.assertEqual(pattern_match('|xREP\x0b9=Q_K"`(I9a6dSE{f0P6aM>L)7\\>*o-\x0b1,fRdbUy\r"p@}6lF_\ti4BJuzR1p[r9.\'Mb#Y-F$cYO1/\x0bqe', 'b#Y-'), [71])
    def test_case_2518(self):
        self.assertEqual(pattern_match('#\'d.y/"4^Y</,&`drsBRY.\x0cD)aw}a<C90le/o Jf;,(USU,XK-Ne}(', 'o Jf;'), [36])
    def test_case_2519(self):
        self.assertEqual(pattern_match('_x#&tGw T}d.;-$FsiXXpN,l2t-(D[iz}p4^8`&\x0ca3FT\trcIx+;gigdZ?', '&tGw '), [3])
    def test_case_2520(self):
        self.assertEqual(pattern_match('Q":\x08]&cpc_W1)MZ:-vhx1L4\x08%Ht\x0bPylxv`g)|zuKtqOB]!"Iok$vm\ty\rRix\nmG-m5zGgKp=', 'Iok'), [47])
    def test_case_2521(self):
        self.assertEqual(pattern_match('On5xe@MJEsK\tE/-h,G`rlHXEMgHN|@u7"_>nZXp\\m-25A1WEWgh\\\r\t', '|@u7'), [28])
    def test_case_2522(self):
        self.assertEqual(pattern_match("F(|B wT/&K\n>9}p\x0bhO~WZ<4 Q**gxw?E+0bmFGL_|gfuM6X_P0>XfblQ,rSs5g6\x08ng4n1GE\n>Mr/?\\~!\n7On-A'un>--", '**g'), [25])
    def test_case_2523(self):
        self.assertEqual(pattern_match('\r0iB\t\\I\x0cp_zj6KYcW7fb lC$XQHzt:uVM)?o\x0b&\\Le5;O;<WGrO7hZnw z+$TF\nb|uRj*O>(m', '7hZn'), [50])
    def test_case_2524(self):
        self.assertEqual(pattern_match("\x087O:<7k;33\t kLH0+kNa=|$@\x0cAN~PP!#\tC|8$herMR['vAF<cUtU,5H3r J+$J[B3+;.(9bm", 'AF<cU'), [45])
    def test_case_2525(self):
        self.assertEqual(pattern_match('ac[u@&@YD0-G#.NPti?y@\x08K\t*~hXWDl*Mf9R\x082v\x08\x0bX#@Ox>(G[de@XrpDO6&Q,ji$0A5cP:-k[QZtE5BI8qssU#1_5cE*57\t|=', 'cP:-k['), [68])
    def test_case_2526(self):
        self.assertEqual(pattern_match('i?pM#`aFzISYo"$MF;8~G/lb<7F]8:p\x08i%Af8&\'A=\x08bhd\n<nXgBhlNLE?y]hw:[\x08', 'b<7'), [23])
    def test_case_2527(self):
        self.assertEqual(pattern_match("Q=mvTR~H\tR'd G0Z+KG3EehRe+7%rT,sT;'TX--mY8\x0bB9YA|mX|k&Q:mH=]``3\\%\x0cD3+", "R'd"), [9])
    def test_case_2528(self):
        self.assertEqual(pattern_match('IL0NV\x0bWU*?\x0b\t;G\n:bOmm.5A;mRyCg<$\x08Ppn6mV4A\x0bGWkr;Hn\x0ce\n1\x08*7/!%^=yKihnv \nN61J~@3\t', 'V4A'), [37])
    def test_case_2529(self):
        self.assertEqual(pattern_match('sJHp"8=#\\D[ebdGnC\n@ u$ddma\x0b\t,oICVJw[aq#]HzybT19.0u[!$ryig/ #p_T_\x0b9{28HH7\'jLJ/3mTQWb', 'u[!$r'), [49])
    def test_case_2530(self):
        self.assertEqual(pattern_match('v4`KqS6uOeVVNEG92&U><McQzD"=|az_K*\tm&;Y4RvsD:)IIN7kZt:T9NP]nHD<z<8\'cA00tjT', 'IIN7k'), [46])
    def test_case_2531(self):
        self.assertEqual(pattern_match("r3Vo\t3Up7<ZQwxLONv`02]!\x08h89`Ii%STfP\t4`I<1@z1_B7+{PoWpv2`T'4p+)%Tc\rKa]@-_%T;l]fV|)ro'1>U'%6eJ\t<\x08", '%Tc\rK'), [62])
    def test_case_2532(self):
        self.assertEqual(pattern_match('t&L]7QzH*Zl<*zQ{CQPyK074s.6F=d&zzwJ!IYOJN8{=x^v(|\roME#BQ^\t a!.\\M3\x0b\\%Ca]*>zT^odzh,x\x0b', 'PyK074'), [18])
    def test_case_2533(self):
        self.assertEqual(pattern_match(',<f=)+E\x08hI"e#[t\x0b{eob@,LJ\n_Nz`L23A]`-o+yV\rP4\rYA:$#__?];&q0QeH,8ql^f^4SUVQ2WR\x08\x0c\\', 'L23A'), [29])
    def test_case_2534(self):
        self.assertEqual(pattern_match('&nhLIh+(#d\n}4Z}u;1+mB{JAvp0:4T~/\x0b)[hj5~t51Blk@W$uUpV3fv,5\x08Mpo\t@', '{JAvp0'), [21])
    def test_case_2535(self):
        self.assertEqual(pattern_match('>/*\tL"?#|$c/@lWB^w[wB*uzsCLNQTmy\x0c,iHBgr(i\\j>AE@n7/)`*_,}6yN]f.,?YFec,taQ&Y-by/\nn:KrkG', 'YFec,t'), [64])
    def test_case_2536(self):
        self.assertEqual(pattern_match("~ep5r|F\x0c\x08 LGNR:(h#U hUwu-a{4tRynPI!FgBnj>\x0c1qj{8\x0b\t#Cz_A9u1x-7jJJ%U5\x0cNog'!N!\x0c1HGp?", '\x0c\x08 LG'), [7])
    def test_case_2537(self):
        self.assertEqual(pattern_match('Ri$BS\x0b2WMmpgj1WN|L!^%VLCgj7|\\8FNylybnE\n1~/o&Jp@{=\\?8qQ>P}N%', '~/o&'), [40])
    def test_case_2538(self):
        self.assertEqual(pattern_match('.}[~Y/->Yd^7OboB(p#Rxg=i5A7X8Kwj_0HZGr#\'wyS/_"5xn]?i$m\'', '#Rx'), [18])
    def test_case_2539(self):
        self.assertEqual(pattern_match("4S+`|G]jDj?]iox=/cj}MTlr?>hE!\t,s:#4-BQ\r\x0c?!c7'\x0cPCsHK*|*Y\tz@y3Hp<fSy{K{zw:+GPU$A7[D-C^\x0c$1|.\x0cqTi", '/cj}MT'), [16])
    def test_case_2540(self):
        self.assertEqual(pattern_match('km%-TW\x08%~a?; |S\x0bnr9Vx\x0c%7*\x08\r9*ud!P<t%"\t\'pe/P,D?>Bd\x0c %$.[hQ5uY0lPUh9hB<pG+!B&', '7*\x08\r9'), [23])
    def test_case_2541(self):
        self.assertEqual(pattern_match(',eyIptX,.G^$\\V9&`c0\x0bZ3y\\^H5i(Pzd4sb5\\;ri\t>#@%Ok:A8C,mdL|.}_^L]``|Oes3TL,*x[]+5', 'Oes'), [65])
    def test_case_2542(self):
        self.assertEqual(pattern_match('zwCd+,yj!~5wV>.{hD$@qKj5\\a\\rI^p)To7n$596<"cZR-~o*-:+*:ZDdnGeOcg5cuk+V/%URxG(J}3){\r.w-\'nbp', 'Ocg'), [60])
    def test_case_2543(self):
        self.assertEqual(pattern_match('bpsR~kxn-W\\bX0j-q\r8w<=-`?)nPq#>t\x0b3\t,0,@\\~M8\'K%y\x0bVx3vOA%Gg?kBnu"e4s(P|koD', 'OA%Gg?'), [52])
    def test_case_2544(self):
        self.assertEqual(pattern_match('FM\x08g@q|hbDdX:y\n}USgw<{8[Og\x08YLm`h+v xet\x0bRd; i!2wI+7%^+6B$cOEV7\x0bd&\x08,!E.', 'X:y'), [11])
    def test_case_2545(self):
        self.assertEqual(pattern_match('~>KXn[\x0cT:pfgfaE9;caCwm(3uXUF\x08@R%2(t(O~N2k99t(;];j(P@KH5`y"JWM6R=3u%BCnwoMv&/W-Iq', '[\x0cT:pf'), [5])
    def test_case_2546(self):
        self.assertEqual(pattern_match("O94:aO\x0c\x0cZrlh\rybdKl$8$|88^QmP][\x0cyYBO6S!Nt=<s7_YweR?,M\tWL?Yn)e?_2W(SowOxt&O1#u&(:}wQ3(+'b", '(:}wQ3'), [77])
    def test_case_2547(self):
        self.assertEqual(pattern_match('\\A(u4=i\rN7ofNkBo*d7\'I1QkTZ -L^/:hv`YfW>kM>jC7shTZ=(=\tlG3zh"$U~\x0c2X~OT-8wgf\x08)7ck0rg]', '1QkTZ'), [21])
    def test_case_2548(self):
        self.assertEqual(pattern_match('y}O_2zq>K)}v%3[b\nv|}` 5xKhlc4GNYl!A7|:P<3:843w\x0c>}\x08VTb4&OhK}m>x_dz25ww7OzjWQ\\', 'hlc'), [25])
    def test_case_2549(self):
        self.assertEqual(pattern_match('f2\x0c\\oB\x086jDR\'-BW\x0bnzF)f#NQU6,\'0Y2M~X1%- \'!"It\rE]!LE2XEjMM)_&\x0c^u{5DsX\n,@fHJ\\?XpfzuR+!Ho^@OF"ZD45:Y', '6jDR'), [7])
    def test_case_2550(self):
        self.assertEqual(pattern_match('A\t`!}6;LyZTtU_S(C*C4rL3U6"(>RPa+Wf\x0c{Xy\x08Ct+GGAf:#:1y#3RL\'ufa\'JcR"H_.\x0bGn1hfp\\\n}cTJ-0Z3N]Q\r\\%%&uU9qgc]', 't+G'), [40])
    def test_case_2551(self):
        self.assertEqual(pattern_match('LZ;5Yc#i\'e~7\x0bl9m8M]S*HcV#s3?Kt\x08(RXDzpIL,)_%Tq!)U~eqAc\tbm"<rt?c\r+B~kZ%\x0cqgs{CF 8?kEr\'TF3IuIn=1t', '*HcV'), [20])
    def test_case_2552(self):
        self.assertEqual(pattern_match('C]`:nL\x0b!ij8/I`6SDek:lo\nIxBK2D1e~ZV\r V|j^*EV\'7\x08G49}V%>G~AaPR~k"\x0bOB23!T45{,;%3&)5\\I|D$\x08U>N$]g', '^*E'), [39])
    def test_case_2553(self):
        self.assertEqual(pattern_match('m7K"D}h.S{`X).hyEDowk\x084w)kg<O&\tglh>OK4CB?NP#bg$LvCDm#+i6,', 'yED'), [15])
    def test_case_2554(self):
        self.assertEqual(pattern_match("=P]@\x0cysAa\x08Jo<lfoqq3UHQ$f0.Bgz-(}da\rfQ*k{XiXd[yr#Gwc\\EA-zN,\x08\rz'WPs>t`+fVyE6%%q=rGsz#CwRB@p]+5;gK7 Rha", 'UHQ$f'), [19])
    def test_case_2555(self):
        self.assertEqual(pattern_match("&\x0c\x08gM^N|MPQbLK6)mX\x0bl}c;$f=\x0bq2-{\x0bSxt-DyA\r5}0SR#8<'^Lt/\trG&<>P9.r3\rI},SxR Iv>b-r^\x0bX^cK)d?", '\x0bSxt'), [31])
    def test_case_2556(self):
        self.assertEqual(pattern_match('d>\'K,WTIwj]+XOZDAg6ygG]G/&rKA\\h"8B/\x0c|<hjp_\x0cU\x08a3f.[#3NZ', 'hjp'), [38])
    def test_case_2557(self):
        self.assertEqual(pattern_match('}(6DFXduF&eyeX1*|%)"\'h" Hy@{;Y" a \n470+fQV<b"M\x0ck\nk', '%)"\'h'), [17])
    def test_case_2558(self):
        self.assertEqual(pattern_match('y!6UqZqRjn(""Y;GAh_O|@2QMw\'lSF#kOZ`bV@`!\t(hyV$<W^aJH6\'1^FAo', 'V$<W'), [44])
    def test_case_2559(self):
        self.assertEqual(pattern_match('1vX lZO2iw{"a8l|r\'\ti4TO7h\x0bj(n$M?=,\rt\'$[\n\n4jfR/Im*P^F2Ax3VAG!ia,riG>n`lC_pAJY\\4KUz\x08cF', 'j(n$M?'), [26])
    def test_case_2560(self):
        self.assertEqual(pattern_match("290rAL]V$Cm\nyuH>N&Q%9cV20}\x08ulZ2`\\`e',~`i3};iviTW\tPnUql\t\tFpOjAP=H%9 G\x0bi\x0bi7", 'G\x0bi\x0b'), [67])
    def test_case_2561(self):
        self.assertEqual(pattern_match("-QM^,5*fEt!C\\uow$Vh\x0clg>pK&2s,<\x0cZ2b^TK?QByFhv'\x085TT^\nLLME-H\nb11-0NJdR-t14Z=wNR<I{i]78\r>,\rhmwMt/", '$Vh'), [16])
    def test_case_2562(self):
        self.assertEqual(pattern_match('-QcHyl;,\\vFx3c6Eq\r1!/\x08&kq6qUhIW-k\rac"\x08Zi<&vSA&B\x0b~6Z!}T1U(g,x!2ru~y,%.#yTf-EhOd{iF g+)M\'Yq5~5-zMgc=', '-QcHyl'), [0])
    def test_case_2563(self):
        self.assertEqual(pattern_match("#7o[C,D)L:`pAby@cTuvQ9y{,Pd`jej\x08P!'Y7%AEtA\tt3A!q \x0c", 'L:`pAb'), [8])
    def test_case_2564(self):
        self.assertEqual(pattern_match('\'S8v68Uk/"Rx*v?$e+?K#fLY~#z"2Y0XU.z0{E)7FS\\N\\]OFt&uW((V!WRh2WJeZM~|\ryiJ+:7', '8Uk'), [5])
    def test_case_2565(self):
        self.assertEqual(pattern_match('i\x08Oo]MoO8AVp\r\x0cG@X$omv/DR,%w${cZ/d>&FS~g]9[r,Z^\tob;QR0!as9jpmtq=P:NAx\nY\nC~R\x0cz|l\x0bNlZkQ=e#TbT\t}A5z.I1]F', 'MoO'), [5])
    def test_case_2566(self):
        self.assertEqual(pattern_match('QgYl\t1Pm4-9x86^2\x08bgX@p2Mi \n\x0bO,^ItK-5"v.H_LDeDw8U+G81u:w_', 'w8U+G8'), [45])
    def test_case_2567(self):
        self.assertEqual(pattern_match('9w0\tj*\n!\nu.:wJ@ -Q\rk"cjEQJ|/\t1VV_Su:wH//7{#3AxYsDV!]NK\nnsc H{hS^M|KZ\\8Ukm{_GkR', 'km{'), [71])
    def test_case_2568(self):
        self.assertEqual(pattern_match("Q_xxk;Ah;:,\x0c,I,Bq0#:xVm0Oh\x0c%~X8cpHm6D_6'JdK\nf\x0bkHn^P&<,_znP\t7~x\x0c%{\\\x08WS`]Hu(B$*\x0cF", '\t7~x'), [58])
    def test_case_2569(self):
        self.assertEqual(pattern_match('QYWo.v&lq >f"Ta~D1VoV(\x08:KOM(ZkvIBx||t[pLF>_eY` _wU)~%#\x0cn\\WC', 'Bx||t'), [32])
    def test_case_2570(self):
        self.assertEqual(pattern_match("xkjv#l10OUjZe,W6}83,HhHP%%8n='N4V+Pts@5[P\n%F#i~H %W7/}?\x08QuT$G\\\rf{L", '~H %W'), [46])
    def test_case_2571(self):
        self.assertEqual(pattern_match("P#L\x0b7(tSqWvA&cHx|hUx;)m\x0c'bF(fB+K25L)=[sGDjG!ea(Tm9qn-WE-\t@}Om\x0c%;74OzH0\\2U}#6!^r$\rVd,dJcJ", '74OzH0'), [64])
    def test_case_2572(self):
        self.assertEqual(pattern_match('SK%\\2zYNA@yjwwJ6]9{*%s=G<oE2}rge!ft\x0c \\4A%.(%_b|2DPT;F1(c;{@o5', 'A@y'), [8])
    def test_case_2573(self):
        self.assertEqual(pattern_match("P7jYe,~$eki1J'R4K~M?k7=@::9F1P=`%.Xl$5rZ-sgW8ib\\2\ngLb*|1'Oq\\\tAlU[Pz(?~H5U}6w~T9~W>mOM#R'SRL", 'T9~W>'), [77])
    def test_case_2574(self):
        self.assertEqual(pattern_match('D> 2K\x0co`I\n{,UrZI*x+#FKacN&3 eD|v"&Be){6[6sgq #7Y(aG,`x8+50w{=,k{K{@{JBb6O>?i#Pm', 'D> 2K\x0c'), [0])
    def test_case_2575(self):
        self.assertEqual(pattern_match('RCR`&;k#[Xi~d/o,S"\n73ENr ^=\\5BI^K;-\rj7>p&itVmbpGJNK67Gq\x08)y(n#N%', '^K;-\r'), [31])
    def test_case_2576(self):
        self.assertEqual(pattern_match('\\6Y&LP\x0c/[BtLCwCY3d|R%PI[<+$X9X-CF<w+"P"\\>ds&?lL-d2\nu\x0b\\]\x08iC")f3nn*\'\\8xz\x0b*Y', 'iC")f'), [56])
    def test_case_2577(self):
        self.assertEqual(pattern_match('=2\x0byKi&\rVO-5JWM5T\n^q<z=Bo|GfLb|4-~ p{7E\n\\Sl&j-Gs\x0cHfDX{s_XrHNqDp+gb\x08J#N}8ANh&^N<Yt:2a)M7', 'Ki&'), [4])
    def test_case_2578(self):
        self.assertEqual(pattern_match('.O\x08vG ?X6ZO18c}amRn&}55!p{at7=mH#+!1Ce;4M.q_o%!eeZ?x+9d_nRH7GdLC', '+9d_n'), [52])
    def test_case_2579(self):
        self.assertEqual(pattern_match('B2xt"lse+?(~\t)T1=cp5t\x0cD&\nwN7rpi,gRpD*UU@TCMQXI![t)\tw%', '![t)'), [46])
    def test_case_2580(self):
        self.assertEqual(pattern_match('3}L+q=se6\x0cgb|.|$}_C?!yB?(+IDIqEY:QT+kAp$-]KHli0FU$ve!S^O+J`+uZvUvM/4|', 'KHli0'), [42])
    def test_case_2581(self):
        self.assertEqual(pattern_match("mlq0!U53_!\r<=_72)^}6e\x0cgoxJT\t\\<25_Ca_+sA}XWS\ngi$z]%''(>!", '72)^'), [14])
    def test_case_2582(self):
        self.assertEqual(pattern_match('Z95Bs^<f}L1t`w;jBhI|z+@"C4aqub!5IXMX4lHfHx=.VP)W\nkT3~1*^4)Rg&YMeHOm#i\nWe<\nT+%M6Q5}k$k6yN[:=\\9Y_#o62', 'kT3~'), [49])
    def test_case_2583(self):
        self.assertEqual(pattern_match('#`<T5O@0j%;?_R#{lHys\'pdp\nBlo\x08AaI\nwqk92"!a]n\tb/T\tR\rt=r2@dGmuA?"\tJR*-\'^^/"g9;;)>', 'o\x08AaI'), [27])
    def test_case_2584(self):
        self.assertEqual(pattern_match('(Ew2)9M\x0bZ)$=8{Q/*\\8NKn/\\m;\x0ceR\rEDZXQWW<95&,gQk=&u,]mLnG4["g_ghX\tZX2C1m7a"s|f;04:**WpNFW\n,$Bx/dq9:$"', 'R\rE'), [28])
    def test_case_2585(self):
        self.assertEqual(pattern_match('ee[uN,HMCbIH&b#\x08I&%8V\x08-#Z}oNn.EimV]s#_9x_Q+D^gP_f=XFR.R1EYV^^C4u8s{/Wx\\', 'IH&b'), [10])
    def test_case_2586(self):
        self.assertEqual(pattern_match("V*5;hM4\x0c#fUl''9.bmR/G'6Y.Z.Q,J(\x0b6P/s}JTly}+>t\x0c?~hCq4p8R\x0c|Uv6W4cv#ejf:*zb\r`P\n/\x08P2wGkh11fJ", '~hCq'), [47])
    def test_case_2587(self):
        self.assertEqual(pattern_match('&"j29O]4#RUg=j(~SX|:# IQ*}16Sne/KL{08Z2h@+N5[\x0b1f"(\x0c|%^g.^!sLLy2R:%R)6TE LN!apD\r2]l}dDM?=m\x0bsR=r', 'TE '), [69])
    def test_case_2588(self):
        self.assertEqual(pattern_match('cUEBl qvK\nar)Z{<aIT,QZ"u|7t<gq7d#Lk!SRxMe6@Y>@DL*"X{@C",)U>\\IEp@;KXYsh.\x08pT@#uC@', 't<g'), [26])
    def test_case_2589(self):
        self.assertEqual(pattern_match(']1N#YT!ukYz~:\\ rV/z\\,\r"jpk:PpYub<{>Hp9~jHT>7H\x0cp9pv2U\x0c?\'\t,5;s~5\x0bZ#7IK[^5)#nCk\n/hSzu*4t%(qUx\ti[oqK[U<O', 'qUx\t'), [87])
    def test_case_2590(self):
        self.assertEqual(pattern_match('9T,H& %P\t\x0c[)&\\DmW}R4EiW|!N\rB&LoR@:37.nhRkP#45hp5)60\nLx16', '0\nLx16'), [50])
    def test_case_2591(self):
        self.assertEqual(pattern_match('t\\"\x0c.30g4 (<>`rU,G(r3}[3_l;\x0cu(tMEqy_Er4[\nJH3:b\n8Rk.k#m9\x08yr2e*AHgo1@\x0bExiTxj@/}*7iq<ZaLXE', 'JH3:b'), [41])
    def test_case_2592(self):
        self.assertEqual(pattern_match('A`X\\k`-\nu;oh|,_%}k6<\x08,J/Qs?u@iy:e\t7.^1\x0bz4\nP$CjO-_FH`0F3lKP?hz~1.x\n7\n*PF]:aw', 'e\t7'), [32])
    def test_case_2593(self):
        self.assertEqual(pattern_match("3%iys'[CF\t&zu4p-H[\\G_1!+.gr@KPu>q\rOc\x08b9>./x%'5\n-J@l5/[\rT+\rr}\\>.\r?bAN\x0b|^3w]\\G:`'?T \x080&|0\x081g-", 'Pu>q\r'), [29])
    def test_case_2594(self):
        self.assertEqual(pattern_match('S,L/=BpyWk\x0ce&%HQ6XeLS2kmkum^fd&1\t(621mr*\rA~\x0bdX1+\x08/{MwHiI^^54q51\x08=BY>d[}d^y"zc"<\'y^', 'Q6X'), [15])
    def test_case_2595(self):
        self.assertEqual(pattern_match('WZ*ZR.0Zwrcs\nD2n\n7Hpv$SSnXvtnWU!x_\'nol/%.%#d&MdO:"wvF_wX3_yS%Xq', '*ZR.0'), [2])
    def test_case_2596(self):
        self.assertEqual(pattern_match('\nm]`*)psilkHW)KbDu *Tr}~`_&2`\x0b3:Z/v{I!NT*U+DcS+k1\tVL<Le7p{V|tN2A', 'lkHW)'), [9])
    def test_case_2597(self):
        self.assertEqual(pattern_match('I&{yU?86Y`?Mo\t#U~+qi_F.sC\t voO(%W~\x0c/y&/iu3<B]\tr2sT719*jmSEtK&', '86Y`?M'), [6])
    def test_case_2598(self):
        self.assertEqual(pattern_match('\tv,0{*<,j%BJPWy>N&z6yEV7D.;%p+*\x08ta\nP(5xgbK:@t/)H7MWS*?\tA/.SiX3[&CWS19]', 'v,0{*<'), [1])
    def test_case_2599(self):
        self.assertEqual(pattern_match("x{I~\x0c]FT@F+&LD>C7~u\nzqNn|Ml$[ROG^kd02F~J\\)?' qq\t^@BHR9_!q3u\t$?#Hq$\\OAjv9&n%Qq?RO>TG&G", ' qq\t'), [44])
    def test_case_2600(self):
        self.assertEqual(pattern_match('\x0c\',=v\'Ng*ws";f\x089iL4;BiJM\tQhc)Ei\n[\r/!\x08\rv\x0bZ2\x0cUS@w19chq^\n/gj*Q(L^C+[S\x0b4,EWlz*xb*S4L=.}Hk)P', 'L^C+['), [60])
    def test_case_2601(self):
        self.assertEqual(pattern_match("p\x08l@m^&,ee^j~g\\Vu)aJ5k8;[wNC'bx(F7LJA|aruozcm\x08tq TY@>XF $usphZy~dD_Qpp\nXG+JVH-79 O1", '&,ee'), [6])
    def test_case_2602(self):
        self.assertEqual(pattern_match('=wmnFx*(\n5%T^9u\t=9!HG"C5k8en"3fAeUb4M\t+rRNw]m)VEz5d.z1{\x08SYMW9*$vgJ.SM>^-qZY|84-& S', '^9u\t='), [12])
    def test_case_2603(self):
        self.assertEqual(pattern_match('SA%v\x0blOu\n\x08(lcKqe*ms*.?"wj3\t.}/>[{K*-o[HicYWQv%AV>\x0cp-Y6d7\x0b[mX4`CmO?.E', 'Y6d7\x0b['), [52])
    def test_case_2604(self):
        self.assertEqual(pattern_match('8h5\x0cG<?6\'OS\n3W{"fsR(\\-r!gr/d\x08m0&RmJo0#]\t;om/Fn5ikVrdA#gHX"GaE]}8rBg5sXi\roIc&\x08aj', '(\\-r'), [19])
    def test_case_2605(self):
        self.assertEqual(pattern_match('hU6SK"2=.:C\rbE5;&KYM5*nG\x08F.U\no\nm%k{%zgk\tV/9=B9ZoiI}', 'K"2'), [4])
    def test_case_2606(self):
        self.assertEqual(pattern_match('^\\iK)Rj0>6jBgX@B?b=]g`\tgMw*DEMg\tA\t M+,x5:U9@=OIa1Uq4QJQ\\bNd]~b){Hohh)F.5<3s:~kU B+>Y)kF^H S', '\\bNd]'), [55])
    def test_case_2607(self):
        self.assertEqual(pattern_match('g&4iBqRY[7z\x0cX\\{J?h(>Y@\x08qywhr0F}SKvDYvKYBk\x0coc\rp\x0cCWe3>wr+RQpE}i\x0cUTQgM6[]', 'UTQgM'), [62])
    def test_case_2608(self):
        self.assertEqual(pattern_match('e:6Q1T4}5J%C95{$gc\\0=L&C$ICRPp\x0b`"vJ\t=\\kLFvH.@u$u&t^\x0c\'/G6o-ALz^nt>\r-(el#?*K+:oO\x0blY$,t)Jo`gY-YNbq\'9s', '1T4}'), [4])
    def test_case_2609(self):
        self.assertEqual(pattern_match('#:S%uL60F]{^J,<Tn#Bg.Y3*oC1cMtWXXTh%VdkFt*.)n\x08(!>:2<i99!.C-\trUPpd+>>yL*E?\x0b\x0bPmp"ZQ\njEGe?tf.<', '?\x0b\x0bPmp'), [72])
    def test_case_2610(self):
        self.assertEqual(pattern_match("Wo2ZL&h='f:D\t&>x$v+5/.p@>`O  :8}t \x08i\ta)<=\x08ldPz9O/AsM_y4M)CsA2KWy~Cy1@Vlt#.BC8M", 'Cy1@V'), [65])
    def test_case_2611(self):
        self.assertEqual(pattern_match('|UH#4c;1^Z?q}Om0$pu%%*;k-g| deEZ=`(99cd))(v] 7Y;j5Ht\t\x08)Qfk?F\\*}F:ik2W(/P{V:GC#&$ON0a9Z@BlUG', '(/P{V'), [69])
    def test_case_2612(self):
        self.assertEqual(pattern_match('&hC1IIV#QRRD7*/iJ{C>_rb2Q:<W&A"5{Q-jq;T&>I038$*"1[D', 'IV#QR'), [5])
    def test_case_2613(self):
        self.assertEqual(pattern_match("T+\x08:cy#Ku9lR!6RVZwcX\rz%gt#b1kR=xBHB\t4%\\q0N3.9mtixdl.\x0bv\x08%9<O_\x0b<\x08Pc#TJj<W'-O&<G1/oeh\tfYk1.W>d@l", '1kR'), [27])
    def test_case_2614(self):
        self.assertEqual(pattern_match('eZz9sIBZ\x0ba)E6nvhqRJ\n%U$6Abx/"M:~H$&R2>V# Nk+ Z6f1|g3]\x0bpJE\nrEB73+@\x0b,?\x0c%\\0Th=(\\)9q*l;ZqH,+l', '\x0b,?\x0c%\\'), [65])
    def test_case_2615(self):
        self.assertEqual(pattern_match('p!p{M\\#T\'MCyCh\t8!\x08>w23{-2fwOjHb;\tKQ\r;Du;d6"mjHd[DTV9C_5S\x08qd.', '2fwOjH'), [24])
    def test_case_2616(self):
        self.assertEqual(pattern_match('i|REc[SF5wCf|ki&@=6r0\x08?b+oL2i8fXCzixAn\t\'eD`PTp<c\r*LsUK-J2bRj%aDpCu.UnK\x0cb7H[w~Hd(V"6qMXs?SWed$3{w\x0bphs', 'b+oL'), [23])
    def test_case_2617(self):
        self.assertEqual(pattern_match('VIm|"d5IoR6jWWzV ng?mLlomv<xt/dxu[<?x4C~P!dHvi.(Y8vByQ9 4\x0c ]Sf-";=[[%4(v|\x08;', 'V n'), [15])
    def test_case_2618(self):
        self.assertEqual(pattern_match("^'\\G\r/w2z= 3Ia\x08`xh<>aapSR72LkDyIG^\n0Wpns8<EK]Xj[hn\\A-#!;NNt38\\JTN@n8F", '2z= '), [7])
    def test_case_2619(self):
        self.assertEqual(pattern_match('f?wj*F[c/uo<,NQh"K"~*/Ok#|jSS;E|2hCnmS%%\r)\x0bA1YC\'\t^H\\Ru\rDD}o_VUV4jzbfCS$t!t#"sM\x0cy5!l!DN', "1YC'"), [44])
    def test_case_2620(self):
        self.assertEqual(pattern_match('ueOR|"T3GiDG{KsOG6-X5\nBkYo:J9QiJk&Y9`(0UwNN9[OSj]?:6<\nx\'#ZWy{t `|H|5qgS`Y$R90_M[yY,jtKc3 o(FDS5y<^#', 'FDS5y'), [91])
    def test_case_2621(self):
        self.assertEqual(pattern_match('U`SF(*Jrf8|\\Q<J^|9R},j\\XdncP|cw\x08fq`p^Ou,qn=>bsoWt_E8:RX`2q{5CZ5k54jW"L-U9.T', 'Ou,qn'), [37])
    def test_case_2622(self):
        self.assertEqual(pattern_match("B)'4vpI4`/Fdhajru9#+E2QHO5b*W8${k[@Igg~HQ/j\t|!J2@Yp# \t^qU'&&-+A#B\nc)QvoOlyKvwe", ' \t^q'), [52])
    def test_case_2623(self):
        self.assertEqual(pattern_match('sq{#JUtOvLJ <^h]Wu~H-Ip%V\x0bscUOD{>k\tSudO#`EeQ\\<d;LeW0Fx8mxOx:wm"O"H^f}Z1"?4@ic\'"\neEg:', '\\<d;'), [44])
    def test_case_2624(self):
        self.assertEqual(pattern_match('.s!W/@G\'.i%J*4,\tx\twqR=7;Vu:+7"\r<18w|[%"\t;\x0b2aVywc@!RBxk=qo\x0bmpDWOpZe$Fk"Lu`#+G*LPnH8!{K&zr2i,>\x08Zn\x0b#J**', 'pZe$'), [63])
    def test_case_2625(self):
        self.assertEqual(pattern_match('\x0c?3/iTXhnigg4^2/{r6HUE[>QA&c<;S\n~o6 1H9]usDaaL?:0|@_`XG;I\n\x08[L"|EYf8R\t`+j^Gh4{&q', '`XG;I'), [52])
    def test_case_2626(self):
        self.assertEqual(pattern_match('"Fa&DW;}zY2hu10ZDi5aw7mjq"fKx@VYj<9)EMW^%.g~k+cc5L>=AVu=k}u\x08p\n_}Q\x0c\'V~\t\x0cRAHRaN5-', '\x08p\n_'), [59])
    def test_case_2627(self):
        self.assertEqual(pattern_match(']S"iz3|[4F\x08nu0\tv:<rHaxQ*Pg{`wtwCh2\x0bi;\\EL9^8NDv_j:B\x0b<.Z[1|!', 'v_j:B'), [45])
    def test_case_2628(self):
        self.assertEqual(pattern_match('I31>":/0uF[sa"$"r\n NIjlE id^{.89rU/+e-5+%"Kp+Qk4UZ[\x08vom]OFX_P@w-:{NV&la{~d0\\`8@\n', '>":/0'), [3])
    def test_case_2629(self):
        self.assertEqual(pattern_match("J;ZfEJ_Bwc\r[a6I~\n_VH57urYk\t7H<Qpu '&8}FQ\r$w\x0b.s,8mdDJ>]", 'urYk'), [22])
    def test_case_2630(self):
        self.assertEqual(pattern_match('OT @(6[Lw0R8|h:\n`e(X0v\r}Iknu2l,";F+tw&<%4d=6&H,[)W;1sPk@bh0z\tOMJq\x0bR OJqJm~n~f[0\'PMIp;d\x08>jc', 'qJm~'), [70])
    def test_case_2631(self):
        self.assertEqual(pattern_match('0)QLnf^3+5oG\x0clXhz31BZv}K0YRfaaI7$d7cF=jrOH6&H\t$s#~$ODcw-}9n', '^3+5'), [6])
    def test_case_2632(self):
        self.assertEqual(pattern_match("JL!M\ns'US*Rx*N(_J\tbYtrFi\x0cBGpU_18f>>.ZNQF5M7;s8cjtXXM!ng#?a5>b\\\x0ba9}np-?g{yw06\rN]e\tiuAl<aEsxi*", 'NQF5M'), [37])
    def test_case_2633(self):
        self.assertEqual(pattern_match('P.@~L#aek*)\x0ci5VJ#=0\x0c~ mYE7#`qc\x0c|A"9YA`hF!/xf{L8!?i`kw', '@~L'), [2])
    def test_case_2634(self):
        self.assertEqual(pattern_match('y9HD\'hY?UEC#BMVY~5T(+M2WCM5vM?[a6"h\x0cgN}_L}Z{\\+o( wJx#9;Tdi*\nLC#qG8J\x0ba@](Jpx', 'LC#'), [60])
    def test_case_2635(self):
        self.assertEqual(pattern_match("O-@SQ(]r00)e\nj>\x0cI:2Q^;k<DSzCi[+:fQ+w%R/n&3CQ\x0c5qt==\x0b\\A-:d^\x08z4\x0c%\n\n'/\x08", 'zCi['), [26])
    def test_case_2636(self):
        self.assertEqual(pattern_match("3dI_t\tb}<b)P<?+;$/dntXb]NO8zaL>'O$5N3C2D63PpAH{OAFzDj5Yi[QL2.!W>[h<AH$Hu]@(Rb^;afzQ1\x082O\\sC-%z}\x0co", 'C-%z'), [89])
    def test_case_2637(self):
        self.assertEqual(pattern_match("7L6^]GF|z!k13B81Q\x0c3>4Lk\rpj7S/\tqzVh|['Yk4phI3Op/Ev\nOj;xo\\M/~-*7t!\x0c,t\nB+kepM)T0[mL=&[", 'kepM)'), [70])
    def test_case_2638(self):
        self.assertEqual(pattern_match("AofOCbq&0KFOIq/y#Rze2x}^t]J71lh\x0c4=(lraB\x08FJ\\hrji\x0bvGb??2iK@0ar#DVz^+,)]F'y~xQ\x0b`f/!", 'Cbq&0K'), [4])
    def test_case_2639(self):
        self.assertEqual(pattern_match('SPy\x08RO\x0b>Sto0pzaCyY6Z\r+I<Fp-3\\HP=L\r1@v.}\x0bj3>f5-N58ds\t l@Eo', '\x0bj3>f5'), [39])
    def test_case_2640(self):
        self.assertEqual(pattern_match(']&+|x,J8Tf4~iDp-\nDSeT^Ez\r"=DZRX0O!5H2hPv;K^E5i}e~Yxb}?pb:fXa{a]wN.dib\tV1op^Is\n@Y"gV-$hg', 'dib\tV1'), [66])
    def test_case_2641(self):
        self.assertEqual(pattern_match('JiqeO,\nRuc5,L@4`vlZ:&jfiN63H6z3HxegaC!|92S95\n\r\nt\r-zBEv[79E?YNJW6*K4A:h.gV"rQ.7QKQ1UWL(p>', '3H6z3H'), [26])
    def test_case_2642(self):
        self.assertEqual(pattern_match('z.j2p3={\tj[rE:P7a.?Yu\nR|%9nCYkp<x N<.k`WHl\x08bK.u[|Mq2', '2p3'), [3])
    def test_case_2643(self):
        self.assertEqual(pattern_match('v"HD)"yjwB^.Dyo0wA\x0cg\t5,=d;]@"\x0b\tZ^mR1Ht9_]~*PiK\x0c:j"J{SvH]MzR&#fH"J:\x0c~"9B\nT\x08', '"J{'), [49])
    def test_case_2644(self):
        self.assertEqual(pattern_match("AERrs*a`V7]o>k\rZB@S\n1}6_5XK97):Rdt2SW(GSP8oukF.0(@Ph9_8]!s&8,3~_46&VYK0C4p/cCvrJwQa5'xt@a:eA09}", '2SW'), [34])
    def test_case_2645(self):
        self.assertEqual(pattern_match('`:Gl[>\tr]}wCBb{OB*]H:s//F$m/=ZwDQ%JQ}L\x0bi3sB\x0cb}fE<S[_|r3bnm_\x0b$yguD_{,5vE<YH*(\\UE\x0cjC9).#xCJrG]', '/F$'), [23])
    def test_case_2646(self):
        self.assertEqual(pattern_match('\'#O\x0c8*T^Y\x0b-5& QZDP.+Wq3I\t<D(h326T]tn;KEjH0U\t##Qrt\\qBDs8A\t@`@:+<(nxNCy\n=\x0b+8pKg)^"3$);\tq\x08Q', '\n=\x0b+8p'), [69])
    def test_case_2647(self):
        self.assertEqual(pattern_match('p\x0c+pI$DR\t&1&4u@@IbPk2g<h5|O3V7/7QZpBk]kZ{ v:ms6^.Z.y(;PoQr\x08cK', 'h5|O'), [23])
    def test_case_2648(self):
        self.assertEqual(pattern_match('tMoiY`z;e{Y PC\x083*N?^B&5hM\nk!\x0bgR9\x08WXpf\\k4Vz6M\x0bX41M3[@z{M?dR|gJg_W^-g+=H\ng4Ou6e`a"X_XxYA6Bq', 'k!\x0bgR'), [26])
    def test_case_2649(self):
        self.assertEqual(pattern_match("wY|>j==Ji),,\x0cftH^B>L*}UH\\9/c`lu;DbUI9cCJ4iv;dLu(c>i2'Y6#fE3D.oFARcaYq%]#M|a7l0Sm", 'aYq%'), [66])
    def test_case_2650(self):
        self.assertEqual(pattern_match('4C@Tuv*\'6o!f&KgndyWoe2k>=toH3<=|yO~$A&7~vXbxf\'}bo)rAS,>cj4}ULUGriw\x0c7/EY9b?$=7,`Op1__jb["R', '_jb["R'), [83])
    def test_case_2651(self):
        self.assertEqual(pattern_match('\r\x0865/a\nKr4 7e\rF^VrKV?Q&rEMJ VSJ:p+KyN}`6%@plL= C*/#^000\x0bxn)0YwCU |TU~@o\x0b5pDq_', '^Vr'), [15])
    def test_case_2652(self):
        self.assertEqual(pattern_match("Ur[yi]P0LiF\r\\ 6#\x08wb1Z%cH`xhgQ=\x08gf^H?0[|t\r!ATBLCcamL[sZU7'!*H+X$=p's$A`?Hick@\x08j`!vcP;/\x0b\t\t", "'s$"), [65])
    def test_case_2653(self):
        self.assertEqual(pattern_match('=cYF:5H4?\x0b<5"e5\\Y\x0cAg@;1J4;;.{?P/E,u_PUav/\r\x0cy<<B2c("Q/TeIxaz=*|$6 f}5RK)n*:"', '"e5\\'), [12])
    def test_case_2654(self):
        self.assertEqual(pattern_match('\x0c-["Dw=SomVO<`!R\\L^[~L+H1BQG>JF#=\x0b\'v?|]naBMRy7XU&!<;9DS\x0c?wB\x08z6\x0btg=)', 'y7XU'), [44])
    def test_case_2655(self):
        self.assertEqual(pattern_match('4l;lFRZM?+O @qWI*5z[PT>y1.X=qO71xUjGIXvN=/bi\nT_Ik>ffjWV)).fRn]I|Oq\t]UPYJ*q}cC/EI&tN', 'XvN'), [37])
    def test_case_2656(self):
        self.assertEqual(pattern_match('2da\rjA/L$,~]r<"-M\x0b9.K+\x0c!H2f%c?Ib"\tR}*$1q~1Ne^6T_6;XdD\'KX;w', '?Ib'), [29])
    def test_case_2657(self):
        self.assertEqual(pattern_match('Djv/D\t*Y\\hqD$eHdg/+~GrusM8/\x0cmemOms8[~OB(m>*D6fQI>\\1]\x0cOG^fCESL6*L>', '*Y\\'), [6])
    def test_case_2658(self):
        self.assertEqual(pattern_match("C/X|Uv?6dru p\ngg8e6IG\nbw+?9A@QfflgV5<DR={9sL?YlkL$szp/LW:gX'TVv4jK \n..u5Y@+svGBL6lvRku6 ` uG D/'Am", '?6d'), [6])
    def test_case_2659(self):
        self.assertEqual(pattern_match('`\'}?:U\x0cOP=>0E"BilCoK9Bn8]!x(c]l{%)(P[fBU3w.E@>YT]GJ\x0b!`@{Q\x0b&/%g\x08}RUA\\"m\x0cBh(/`\x0ct;u8j8/V', 'U\x0cOP'), [5])
    def test_case_2660(self):
        self.assertEqual(pattern_match('%Hj*3rRq\nX^t&U_z3\t2{\\#<b;\x0bCo=I\rw]MF"K0\'\\/xfbf#_f1a!>7lP\r!$juNK\x0bJ>7:SP]b:#\rI_z\x0b;b!w?$Ma],{?', ']b:#'), [69])
    def test_case_2661(self):
        self.assertEqual(pattern_match('Nw\n*A5B`m.mPu7rk!hm({~@f"pB)\tf\x0b" JrH:&635o&`C\'hLA,#', 'Pu7rk'), [11])
    def test_case_2662(self):
        self.assertEqual(pattern_match('K9J\x08oFb\x0cz*yF0/"z\'Ux:UBb:V}X4W\x08AQC8\nG!1Q][*Sb!\x08DlIom\'Umq?O%d\x0c*\x0b\raS1&l\x0c>G9w8kBP;!E?6\x0bCQ*<<-\\~ ', '8\nG!1Q'), [33])
    def test_case_2663(self):
        self.assertEqual(pattern_match('TWn~(8V8 3+j\tXU?/.f-\\R=\rZadvs\r$c5DTq})+I0weoZcr!kpDg)SbT6n$=\rB^{"*zCGjv?0G^1 Xq.,Ij@v\x0c4Q.0#%IP.$wUY', 'Ij@'), [81])
    def test_case_2664(self):
        self.assertEqual(pattern_match('vZ\r:?Ksp4jOQ;/9U~\tLU+d\\?)W2y\n~\x0c;W@,Gggz+Na1*86rR<1#:>8[z!7WT=QM0Y=id;zLuSKQ\\3:', '[z!7'), [54])
    def test_case_2665(self):
        self.assertEqual(pattern_match('[3gCC\x08\x0cB~`o$Eo(=D5Eicd(6(Zl`1CAQ?:$Q"+\x08K<\t6tUB%\x0b1@.c,Ff*R\x08d"zL!]_O9n9?\r!AiW8!W', 'cd(6(Z'), [20])
    def test_case_2666(self):
        self.assertEqual(pattern_match('M\x0c+/+0jAaa>$h?n3$\x08\x0b3fkDuP9y2]t;kIw.Q*\x0b[h)?$on-*a}Mg\x0bj?w_GT!*~!.x1r3~,#/DN:E>:te\x0c\\$1{;}h/Cd', 'j?w_G'), [52])
    def test_case_2667(self):
        self.assertEqual(pattern_match('aV|;\x0cT[:/=i\\2o<I\nPf!lGd<"qn(0o`#\tWI?8%.0`t|\rSF}Fh"5?eA[\x0c~OZ\n"K{0$bYp{TeW\r"abQ\x0bH{GtAOg\'\n', 'I?8'), [34])
    def test_case_2668(self):
        self.assertEqual(pattern_match('ps=|JW:;MxtnO?F?)FW-#qRnL.^L~\x0b\reBv\\\rq3RU\\T\n_\rz 2<"=t1y!3`jQi|NzpO\x0ctV,Y4],f\'8:', '^L~\x0b\re'), [26])
    def test_case_2669(self):
        self.assertEqual(pattern_match('B!tv "0TS/A#>+\tBC\\M<bEj`N\n*<\'\'so\\/^G}InGKc;>8C`W}EvFMp\taz+~\tyXmqC*,.NGY1_\\w\x0c^hF', 'FMp\taz'), [51])
    def test_case_2670(self):
        self.assertEqual(pattern_match("zH/\t\tB#,*\n3\t'6)7~XGF>h1d'Ua\x08'l}A\tMiX\rxctp wt9LMA1w{%Y", "'6)7"), [12])
    def test_case_2671(self):
        self.assertEqual(pattern_match('z(#e+Y"B&Y5dO\r 2o&}.Zi,j1hb!7e|%=l+E$\x0bo\rK!a2>" ;%9z]|S3;?H\')E#ID!pLY\'6LCS6jgdNy{Rl 1mS:^eb *_2u2', 'l+E$\x0bo'), [33])
    def test_case_2672(self):
        self.assertEqual(pattern_match("*=p_-g!4]p\\\x0c!*jK*.U?\x08}eFU_C}]z(7<-q9cc]}JN~ZdbdntpBvhSJ]XIH-_LoW^|q>%I\x0c<Y\rF'dM3'+", 'H-_Lo'), [58])
    def test_case_2673(self):
        self.assertEqual(pattern_match('J]OML{26`<1"\'C1lb[z\\5d\x08}+\x0c_k4Y\x0cna~N+~UdVt(DDj2`4e\x08w&B+05g\n |k\x08z4w0Ht.a>MflNMS', 'Dj2`4'), [43])
    def test_case_2674(self):
        self.assertEqual(pattern_match('Lr7]?VsB `"5^XS$B9|Q}XZmE?cn)!`@Je5=Ax?w @Hqoyp\x0b/a!Ohy^Dl96d`2E2\x0cyZ]),IDpLS|\rt', 'oyp\x0b/'), [44])
    def test_case_2675(self):
        self.assertEqual(pattern_match('\x0b4(0e6peb\x0ba}IFeJ7~}Gl/JffyxyRS(V3%-u&P%#\nE0KtNTe4Lz,`V!)1KIN', '\x0b4('), [0])
    def test_case_2676(self):
        self.assertEqual(pattern_match('%J=EQ&U2K1G%[wVct@r|^bsJf>^\n\t\x0bI+>y"$8x|}iZ/Q7h\rsO=`\x08\\D-U`l,Ss2:l:!J8`6~VQ0e.\x0c\'m@!&1zE', 'Z/Q'), [41])
    def test_case_2677(self):
        self.assertEqual(pattern_match("!L9@U=08\th\x08\x0cn,6o4V\x0b6TW/io\x0b]d4'u0u''_nCKKl5>q3.kyn7J=n%6pD", ',6o4V\x0b'), [13])
    def test_case_2678(self):
        self.assertEqual(pattern_match('!.b<"Ph&w*XmVfN9<}wS{^WYs?@1(z`9hM^.hnzE[Kdh\'\'7Zj}f+Tj2aJ', '1(z`'), [27])
    def test_case_2679(self):
        self.assertEqual(pattern_match('5!6M`P=aQp)^k%\x0b$\\,76\x0cW2Fm/\roR8v"S\x08zv3S?KT\x0bX1w~b2k|S&*>`Rd[|= X<SR\rtto3>4\nJ}e^>L', 'W2F'), [21])
    def test_case_2680(self):
        self.assertEqual(pattern_match('SFI{\x0cuT,`i\r:mZj\x0bfQd`@o%Ch\rp1Ik"Ew&/p(GY]HNc& R+#=p', ',`i\r:'), [7])
    def test_case_2681(self):
        self.assertEqual(pattern_match('p`_"4CyF4s+,gXd`pJ^-A\'rd#?>x\'LF4A\'B>VuZ#!d)VcA*JK*G)#0SmzNq{Ia(n#c', 'uZ#!'), [37])
    def test_case_2682(self):
        self.assertEqual(pattern_match("8sv'\x08B8q;T\\O55K4DSG/^,\x0b}++b2+\nYs4+X11Rx\r\n4\x08W|4U@f(hYd2SEj7]_R18PF\\\\`k%)vG}nOmmVH?Jt\x0c8>d^z>f|\\", 'B8q;T\\'), [5])
    def test_case_2683(self):
        self.assertEqual(pattern_match(';%\n_;U2%NYDV!_6/`1DT\x08GK=p;m=L#lPLU}Ui+`OD\t\x0cm[{=GFid', '_;U'), [3])
    def test_case_2684(self):
        self.assertEqual(pattern_match('>t6sN;6y^Uzm\x0by\\ozp"p(]bj{rFA,Zm tvR,sN}3YpQe\\"1\rB"a?fOB7<??\r()zaSe2PDihXM]', '\r()za'), [59])
    def test_case_2685(self):
        self.assertEqual(pattern_match(',}t~oKU#\x0co>G-d$NgB?jvoSH0V[yU)\nb6>$bIyg|k+{R\t PP)CFz2q}r_G>0Rh524hZ6W6', 'yU)'), [27])
    def test_case_2686(self):
        self.assertEqual(pattern_match("7DWoi@,hNsCo~H.*^Cj\\11@'L.,|8}$2!Xj9GuOR.D8l%0\\{r$E\x086+7g+ W\t8o=\x08@su#8+0(Y\x0b]mr1C&jc1-kWM\r[bi", '8l%'), [42])
    def test_case_2687(self):
        self.assertEqual(pattern_match(":~<ne7+W%'0/4lW\n84Wf^`6@N,e-Kib\tnx^sMg}.^+l'9'-gFa72ex", ',e-'), [25])
    def test_case_2688(self):
        self.assertEqual(pattern_match("Op&MtQ5[/DVyM.cga0EBXQap|F<\tPkFx1\\\n:#v3?8.FMQ\tW)1\r$ V\x0bvN#|,7_;EL&\x0bE#'|FmP4F(?@\tVayT+d3\rN%ZvWk6#]", '+d3'), [83])
    def test_case_2689(self):
        self.assertEqual(pattern_match('kp[rldm8Dg\\;txLBZdx[b$!z F"nr^E^\x0bl/,9Id\teM 0U/;|\'My5V\x0b^b+@2+C6{1 aT_30s', '6{1 a'), [61])
    def test_case_2690(self):
        self.assertEqual(pattern_match("\nz0l!oc1#00eg \x0b%K2aiP\x0c\x082@|y](\x08>@6J\\Z\tf<S49Pns,A%Vmo$Wm'\x0b", '](\x08'), [27])
    def test_case_2691(self):
        self.assertEqual(pattern_match('u/UR8z-Q_uN];K5+q"4,>Y[pM1fNze}wog\x08kix%XF}\x0ct<B<tX}@:pNY@0?dB]i#7zk_]x</lyV\\', 'NY@0'), [53])
    def test_case_2692(self):
        self.assertEqual(pattern_match('bH,7j4g_\\(`B4z/{6\x0byI@EmFy yd37vZNmz=I^Nk1\x0b_Rlp`\x0bL UsoFu\t=N] .Q', '\x0byI@Em'), [17])
    def test_case_2693(self):
        self.assertEqual(pattern_match(',lhg^]IEY_Y)Xa\n#S{DbrAyR50b\tA/&2\\c`o{uG#S8O%mJ~(p[\\R\x08p`EV4u\x08iE1`_`ozx%QQ&I ON7("zeO\\c \\b:m.<tW[S0b', '\x08p`E'), [52])
    def test_case_2694(self):
        self.assertEqual(pattern_match("0t<&ppF')%g0sG2(JrJytNr' ,GlJ^(p2`.rS&\r=/?bf 4)-V9^mO~HBSeep<K|\\e}c3!bA> F_\rA", ')%g0'), [8])
    def test_case_2695(self):
        self.assertEqual(pattern_match('p;.LQYuDF%fsSv8[t>JieyAdojoO\ntp{*m6Bh!G|<*Vt!#H@ma# ._qa]1`HPW=6`e?pa', 'fsS'), [10])
    def test_case_2696(self):
        self.assertEqual(pattern_match('@X@~F#dG~Yzl\r+Cx/ 5_2<%RgF"?\rhz(\x08k <<klXCjabq0?n\\pu-5lRT#Pg8\x0b@hk*7\'^0$\'jQOQ7:xk:Ur.', '?\rhz('), [27])
    def test_case_2697(self):
        self.assertEqual(pattern_match("m'9#kX{O]QsIrBmz{`mV#\x0bO||`p\\_tWb9}asr4~#iC@Sq8<h({tG@]SU[H", 'X{O'), [5])
    def test_case_2698(self):
        self.assertEqual(pattern_match('*.8L[R\x08`eId,a":dU(wL8adBTL`Q?rNPf.}0$M\'rvY]AQ_HA"\x087l"XGA~ff)w6$1\x08C', "'rv"), [38])
    def test_case_2699(self):
        self.assertEqual(pattern_match("e=MpbMIQb<O)]aYI\\@tT53\x0cb\x08WCO.e1VFi![&W}$b~cV}.hFKezt39E#:|{\r?~SdmP\x08PhM|=y<\\`LA,\rLw'?uXSZwp\\Fie9", '53\x0cb\x08W'), [20])
    def test_case_2700(self):
        self.assertEqual(pattern_match("%/k7T$kPQk7\nn2U\x0b2.vR~UbF-!5\\!l?-)84J-d)\\QuQ\x08rj4q\nR&'UtPhl&Ddzc;Zk!mvZRjj`g]w_Aj\x08oMA", '2.vR'), [16])
    def test_case_2701(self):
        self.assertEqual(pattern_match("N4\t&+\x0852 +`wQ|l@\x0cvziQ$1'b@^c|}lc9VZ\t\n,3cXsf2I%,f?+L/'5%9Q6~\r&hK[`<bM hsRW>?oO^w", "+L/'5%"), [49])
    def test_case_2702(self):
        self.assertEqual(pattern_match("J!Z/0^}d\x0b-Zq|y+#je8[[\ro=E/>ujh:uo#(Xy<jW[hw=jk?}\r>f3ncjY'7*.eX-TK'{Ppf@{`@jec}_c1\x0bxR39+", 'f3n'), [50])
    def test_case_2703(self):
        self.assertEqual(pattern_match('\r>\x0b`dFxl,rbEh4q.Q^=%<PXM=</~?kaQK=7_\rS\\tI^d/p8])k\x0b?g yx\x0bTbUr>\x0b>Nr/\nk\r;', 'dFxl,r'), [4])
    def test_case_2704(self):
        self.assertEqual(pattern_match("%3%3i\tbAA]_*M^Oi+,rmx@65)|+imI#<*EQ>9a8E?Mv@ ')_T)<@B4\x0cB^nC8s\\)\tZQS*v)rz*Q@&>s\x086/^nC#BG2'S", '*M^'), [11])
    def test_case_2705(self):
        self.assertEqual(pattern_match('vbn~}iwP>`OBvNA\x0by_SG}B_pgwm|:O5:)=#11+.U\t+wjxcw:vT/CW}z~\n_p7A3("t\r]7f..a/&MHjL(us-.A8FcW?jj}7', '=#11+.'), [33])
    def test_case_2706(self):
        self.assertEqual(pattern_match('b+5\x08A._5l5I$n\\L:O2H[/K`XE{EQtL$^U~rG4blB>7Ei(NIO0>G *~Q%tp@2A%J\x0b4y\x0c584\t5I;t;CdK%h@d]l|j/\r', 'h@d]'), [80])
    def test_case_2707(self):
        self.assertEqual(pattern_match('rX(Y2=&N%8E\x080R\tn8.){z]V!|?}"]n$O%!kO\rC|EBT\np$\t[Ah]kYIc(AAH&>(r\x0cRcluAd5vW\nm42', '!|?}"]'), [23])
    def test_case_2708(self):
        self.assertEqual(pattern_match("AAgW1#6o*ya[q19kBpno&\\\rpxf}?[rH\x08_En'vWn$AuqQp37'b\rU'Ud\n\\TY;:NLN~%#E5CutfwZ\t<(>E@Z|", 'wZ\t'), [72])
    def test_case_2709(self):
        self.assertEqual(pattern_match("L\\\x08'OAMKck<Mv8h5g1qgU=1UC4c2=IhF))w<1y`$-%O^X%KNvqAn5_j$FWil=jt7\t", '1UC4'), [22])
    def test_case_2710(self):
        self.assertEqual(pattern_match("*:34ZDC]onGR>baU/S-vhq;:wMx2&%}!M4W_.VIYbv\ncNzpv(~)gL!JWlp.l=9'2t^X\x0b'D(", '!M4W_.'), [31])
    def test_case_2711(self):
        self.assertEqual(pattern_match("d!yQIWuH)jJo9@!X8A5>lBY&^o<ALQ]uLA4Qj{799\x0c5LuRlM%k9\rcwX7n<xMVI\r\\SUD\rdb$i%v'!j$i\x0b", '5>l'), [18])
    def test_case_2712(self):
        self.assertEqual(pattern_match('\tGBDaheJYrK2+LAZ8/7lcb]qpL38\t>RDc-x\n4)|n_N2yp*NDbA', 'LAZ8'), [13])
    def test_case_2713(self):
        self.assertEqual(pattern_match("\x08uo%\nr'hR8v:[~p!,(adNr&+,8o)~xX6F]8\x0b<4Ngf`f]gHKj,YQFpO/N' I9\r", "'hR8"), [6])
    def test_case_2714(self):
        self.assertEqual(pattern_match('C%y{Gy+2=xg2mwf(M.\t\t{\'R 9xh\x0b\rYUtA#$%lWhUYw6eo}3?LqjJCWUAYhL!N7%eK|[\t%7B^Q"\x0b#s+n]|#', 'h\x0b\r'), [26])
    def test_case_2715(self):
        self.assertEqual(pattern_match('{?\nAD46Fo\x0bnkG8h*a7%_(CxuF&~X51m\nZm.Mzz&JM--K`0\t/kX6t\rY', '\nAD46F'), [2])
    def test_case_2716(self):
        self.assertEqual(pattern_match('jd_o0K"iq+nbxr~=8t;r8kSMJ0d{_AR-WWJ|S\x0bl a-&?&&Fu9kHyRn^\'eM,c<jp*\x0bl,NJ$uLWM`F\tLSnAaR9B`3frqdl(D@.)y', '=8t;'), [15])
    def test_case_2717(self):
        self.assertEqual(pattern_match('<+\r=ry|hDe@q,T_0:DP3tkMBu,EL~>xl`mz=y:\rr F6QIi.\n<=ge', '.\n<'), [46])
    def test_case_2718(self):
        self.assertEqual(pattern_match('[mv|szy1Z!jHuFflvI:iVzXMT&R1gV-R\x0cr,0xv\\:<-)tM8uM\x08@3 z1Xkq0Vd\n:@\x0bQ,TLi$}F\x0b9\x0bPr}Uha\x0c\\-Oh=,U}\x0cnOJINe](e', 'ha\x0c\\-O'), [79])
    def test_case_2719(self):
        self.assertEqual(pattern_match('A5}Ddfb^ufs+M]7&qhD;wZRk@s*hJN&F:ZsHY`r{P;0uNAu=|/N[_!?', '&F:'), [30])
    def test_case_2720(self):
        self.assertEqual(pattern_match('oY*vox`$V=mr{[r\x08tvtXds:d7DV/ynO,U+<$eo2x?tSWT*S3\\HP@q}E^,3e.', 'Xds:d'), [19])
    def test_case_2721(self):
        self.assertEqual(pattern_match("OPZxW\\CS6hLai'J_j/a<Wk`h)0I&7Bx|QQd\x0cJb<pd;F,TDm~x'8P#SS3[*RZl3=f?Igsg", '8P#S'), [50])
    def test_case_2722(self):
        self.assertEqual(pattern_match("',@il`\tT7UoCiRJ`IpDGy?M\r(\x0bb,-L5G^k:~,n8{t4D|q[da<*61", 'da<*6'), [46])
    def test_case_2723(self):
        self.assertEqual(pattern_match("{Bagn\\G)^~N&k DQ-I`&u70De\t'n*j*v!_`u/MQ`QzSReCSzCz2u}6T4!Dz\tz@-3r( `DD\x0b", '}6T4!'), [52])
    def test_case_2724(self):
        self.assertEqual(pattern_match(">'X?&$OmI1\rvo+rY~&t0\\=nK@6qo/}gdjZ=pXDB>@/++pVbPF2f\x08FhNa|o$pTn.+&<q{T0LlzPpw0U.=_F)|amU60s", ')|a'), [82])
    def test_case_2725(self):
        self.assertEqual(pattern_match('SA}e+-sQeho>_jh:B8d&[\nem^-\tIs_B!H&S@: .Z{}sfPRM#kfP\x0c)|1yb(C&`ba={E>0C5\rcT&"7rr\tG^D`\'utD', 'a={E'), [62])
    def test_case_2726(self):
        self.assertEqual(pattern_match('$C\n^gYh=pr\tv4+s0[\x0c\\|#k$TA`M_RF5w9i1,\x0b\rn2,y\tr)pInv=f]gy|NXIas1B5#,4g\nd[', 'n2,y\tr'), [38])
    def test_case_2727(self):
        self.assertEqual(pattern_match('f?>@UGa($=an<A~]\x08BP<UHl~\'Gbf6Cd\rd"f5E{vJ\\,cbG+wK.3x43cmk0\t/B7<QDTOyMnXG=', ',cbG+w'), [41])
    def test_case_2728(self):
        self.assertEqual(pattern_match('|vcir9bOq[H3\x0bq\x0clZ3KP8"\t\rNa9J^&K5l-PTyCv\r!$iedMxe_\n(k<,U>%[i$H.q\remE_;gLzw/m\x0cI\tu]3$atD*)r', 'zw/m'), [71])
    def test_case_2729(self):
        self.assertEqual(pattern_match("_I@le08S]m[UWp5::Xr6z^'zY\x0c_&q\nGeEByl[kP<s\r\x0b^\t$fnVKfx&tW1J(NJD}4U5 \x0be|UZ>:>l:|v\x0c^}/Sbmel0PFW,", '[kP'), [36])
    def test_case_2730(self):
        self.assertEqual(pattern_match('&*Jq=yN;\x08w1\n/-p:X;Rt$bv=iWzI24$Qp\x08\x08bF.BC1 4%t\x0b~.W[*<;', '*Jq=yN'), [1])
    def test_case_2731(self):
        self.assertEqual(pattern_match('YFqM\\\t\r0$Gd9X"l\r_;]!+};[DpSpU\n\rb(7j_L\x0cg\'LLVghrrkV\t&G!o%~\x0c[y\x08.;:<9Uw\r0dom#\'!UU', 'pU\n\r'), [27])
    def test_case_2732(self):
        self.assertEqual(pattern_match('"_JJ8V5QvQ(NUJEP.Wm@%2x>_As1]^9E^jv?a:D(\x08)Yo4Q,oSc7', '1]^9'), [27])
    def test_case_2733(self):
        self.assertEqual(pattern_match("q4JB]F|'t+uT@l$(3`V5hqQj\t:X13NQ5[wQ:kE\x0bkmPXY%:0Zw cel$ny%LstO-K3gHKTL`@j]", ':X13N'), [25])
    def test_case_2734(self):
        self.assertEqual(pattern_match("${]BMp.Z7qB;KA'\\MR\x0bi\x0b>%ss0$R6O>v04bR%d!cl[>nH6\\Ra$iKpHn(\tfL5-D1|z33/.\nE.B", '\\Ra'), [46])
    def test_case_2735(self):
        self.assertEqual(pattern_match('\tQ\x08_8-\'UP8T~}s\t){4[wtqC2Y!>0g=\'^0gjK!Hr<M\'uNmx`,kJ"Xz?wcRcMCf-ao{a52\\4S', '>0g'), [26])
    def test_case_2736(self):
        self.assertEqual(pattern_match('d2f>\x0c5|MWLzdyK7cA{b+IFe#A%HH~l:![ Y\x0bB5,awL\x0c\x0b2*QF9[\\TKKv7t*.NUHS[0s?+Gy<&<=aQe9i(@MzkR]b\r\x0c3~#zH$mYh{Z', '%HH~l'), [25])
    def test_case_2737(self):
        self.assertEqual(pattern_match('DY{aT+<. f0p<nfyR-)\\\tVGuP33SQ@Vr/\x0cI+`u7UT.\n&=gR]|\t>yKwK\x08q{|bg<"L97N\\n>_)NVg\x0bJzCyGZV,vZCJpVCYL', '+<. f0'), [5])
    def test_case_2738(self):
        self.assertEqual(pattern_match('SS;LW><HTcB:`ZauAaffwQz>7vj>iX-nF|UuX%\n:s\x08vrU<l{Hk&~)$`CRsN', 'W><'), [4])
    def test_case_2739(self):
        self.assertEqual(pattern_match("F 32Hsc(3nO@\x0bL}`7TGC.\x0be5WRBB\t\ruP+y%+\\-,oEB@]BesPO\t-r4XUz'mF}k.KAKTRQkPPx1u[\x0c\nB,@ibfH{Y0Q[im,", '3nO'), [8])
    def test_case_2740(self):
        self.assertEqual(pattern_match('(LII:NUj\t\\(Nb3Yv1E:J=w``]<HX=Ew7PTKd \r=m@=}]/H=3ip{<qBzfOy\x0c>fm<M{(%10`u|+"j$(5Ox#(,o', '"j$('), [73])
    def test_case_2741(self):
        self.assertEqual(pattern_match('zPQ-us+\'Z\\)?d-65o\\Zk?u\rMn\x0bOCt0"nfgY]hHlpAm>\'d5uqaz;\x08_Y/\tp#Qh0QJP.w$:zC\x08t2LUa%\x0b])aop', '\x0bOCt'), [25])
    def test_case_2742(self):
        self.assertEqual(pattern_match('\x0b*i952ye{sw"#d=\x08\x08; ,\'dJQ\'P&0>\t,UC@KkU}G7Td/2{.HC6]Na\x08Q~?V\x08s^Mr~lN,#6kQg+Ia`+sxjtDEX+?Z', '}G7T'), [37])
    def test_case_2743(self):
        self.assertEqual(pattern_match('FdT<NNt8q c!/+G.\x08^:1+]7fz7,|{ixpWQ(Ze7`jR\x0bqO\t@.M`m3p[5x]R7uyc.TDv^W["WBq:pULo`(<t;,K`ZoeC&3/rjKF_])o', ':pULo'), [72])
    def test_case_2744(self):
        self.assertEqual(pattern_match('\'g/G\tvs\x0cId1[Cts`Y\ne6]_K^=iL:b\r5|-,Ec8\x0bxSsl6"66e9.\x0cn3m_P76=', '8\x0bxS'), [36])
    def test_case_2745(self):
        self.assertEqual(pattern_match('u$OM.+p{h@#e\x0c-\\zR+{Q\rpbkszbRd+9i]G@^>Gm?\tvWq<)B)V|[Rwy\x0c#c\x0c%h5G\\w{{jMSz0l#@IIqy2n/.93PU nw$GmN=x"im', '.+p{h@'), [4])
    def test_case_2746(self):
        self.assertEqual(pattern_match('zsi^0OHUBDBPFq,b\tAMqQ|k2t>!\x0b~\x0b\rr*Vu_M\tzet"=~.`0z1{\t"kqJ:}CQI,z(\\0Vp\t-F>0', 'z1{\t'), [47])
    def test_case_2747(self):
        self.assertEqual(pattern_match('i\\?-UDw HOZ%|v\\4! *dB]XIo6}}u!PJtJW%&*1obk|\n#HB1BBYG\nO9HFq7b#ey', 'BBYG'), [48])
    def test_case_2748(self):
        self.assertEqual(pattern_match('97\x080j0iO3>zJGj@}\t\nGxg\x0b&#(oZ$Ptp\x0bl%V:G\rq<H*x\rZab-u2sci6\\/kpx(H', 'zJG'), [10])
    def test_case_2749(self):
        self.assertEqual(pattern_match('8zft~3ZWX%3p5=Yf5w^+RdN"|J,jVRWy|<MZ($I\x08W|\\XufR\'\x0bB\nYXMi18Bgr%5P>Q\x08gOi[\x08rvkNr6F8O>e+2bW!>2n;xBz><HUqU', 'e+2bW'), [81])
    def test_case_2750(self):
        self.assertEqual(pattern_match('{/eE3J>#X^Q\n?[\'fD0/LV\x0cX\t\t8=LUL~IT[!)Azr.vrrD^,fi\'*\n[bEnH#:F*|"mXK2', 'zr.vrr'), [37])
    def test_case_2751(self):
        self.assertEqual(pattern_match("]}l<\x0c5D?gc+(BFwl_pty\n:]6.@|ED$ =wv1aUlIn\x08PR8,0}?V9%%?zB'&oR*\x0b^wwralP\x0c}>Ds", '?gc+(B'), [7])
    def test_case_2752(self):
        self.assertEqual(pattern_match('0qp\ta#B0XI/DKO8X`!rO\n24PG1grJFV\x08Qjme.?)nYb\n+#nW\x08\x0c{|', 'me.?'), [34])
    def test_case_2753(self):
        self.assertEqual(pattern_match('\t\tZ00^|JZCFsoTc\n>y]1w1jA<FhD9\n#rGs=TWR+iz%-3rL7\r_~JZ\tl#>^a"sT7\tu/#%V', 'L7\r_'), [45])
    def test_case_2754(self):
        self.assertEqual(pattern_match('MHQU7fy6Mi$StOaRcs<wd>;>FsD,od~(+Q9./(4\x08P~;FYV2Fg:h`375%GzS', 'FYV'), [43])
    def test_case_2755(self):
        self.assertEqual(pattern_match('KKM#87q9Taa\'Q"x/\\v\tq=.RcmPl6$[kz9\nDP,6|.!\rL$P5ru`$sPG/}(W0$rArc%wH;S-LG6+WBC\\^6p^\x0c', '+WBC\\^'), [72])
    def test_case_2756(self):
        self.assertEqual(pattern_match('& ,I}F`w{i,R#u.\x08l7\tXI1-kU"(fBN7OBc1s\n!.:L:X-oxk\x0cn(\t("Eto\'Lfz6-xg[b4-)3me6$!5q`F1', '6-xg'), [60])
    def test_case_2757(self):
        self.assertEqual(pattern_match("Zj\x0bCT;Cr81zj=wz\x08fo\x0c|PyU,F]Qed3xR/q2\nP^2gA8pw@Y.etu -33Z|>\r]'\rSCvj3", 'gA8p'), [39])
    def test_case_2758(self):
        self.assertEqual(pattern_match('ACyT+/{#\x0b)U9/Z?,~n}36UdA=Aleo/jZd>Wa+L\nf\rr|]x#!9N_F?^,y}lX7.#Q|&\x08:\t~v7;c/`*:vLp', '9/Z?,'), [11])
    def test_case_2759(self):
        self.assertEqual(pattern_match("1]A'y7t!b/C3QY,q&B0XYj2\no/S6P9B#QIr7Rr\n}Dk0,xJu/R-&<xx%(Kz;Lr\nmI\\S2sw8Vx>;Fo\x0cJGGp55e-\n", 'o\x0cJG'), [75])
    def test_case_2760(self):
        self.assertEqual(pattern_match('oK_3wPV&i<ojrj\t{q(upR]OhqQ}Ere![S57%k\r_Iq8k+*b$T\n?mL<:Va', 'upR]'), [18])
    def test_case_2761(self):
        self.assertEqual(pattern_match("1&-G;VVb\\LR]?o\x08Qs_8y2>yi<Gk]9r&j78'3jP^=\t5y\x0bPlyJM7", 'b\\LR'), [7])
    def test_case_2762(self):
        self.assertEqual(pattern_match('\x0cV{YUmPgB\ta\x0bCK1RT}o}>\x0c;{9iYF+R+%MGRA@+V.v-p;Dw\x08<9bH2He6]Bnv(`^', '1RT}o}'), [14])
    def test_case_2763(self):
        self.assertEqual(pattern_match('\r\ta_mreua+\':aee5\'mgY&)0#wxk+lGi<ibA(_j\n+"/|jl\t\x08CL5W\x0b/7wk#>W=', 'jl\t\x08CL'), [43])
    def test_case_2764(self):
        self.assertEqual(pattern_match('d`N2JqHr\\I* Mps~=\r0@%Vr}Ur.\\;[{oUnOr;*Kg0s[,\x0b%jY(jb%2', 'Y(jb%'), [47])
    def test_case_2765(self):
        self.assertEqual(pattern_match("#3yD\x0cED6k'vdC6U(ZvU\x0c1Be\x0bsaVX6Ddi(C-*o/6^\x08DfoM2~AQF8J$7uK9[d)Pi\r^}=zD}vw[]*SjKC`(l<f'i\x08=(TvkEVt?=\n_`", 'C-*o'), [33])
    def test_case_2766(self):
        self.assertEqual(pattern_match('[F0ZQ\x0c\'RK66a60m\ttKFg!\tXa<\x0bk w<0xw\x08"$C7\nE&p8_yNM\'op6+$j8[\n`$kFXJW"KM\x08C$K-J#(OrnR`p,\tSrOra\\', 'k w<0x'), [26])
    def test_case_2767(self):
        self.assertEqual(pattern_match('hA8u\'cq"@K8\n\rROTKgiZ9P*=|5,R:tk\x0csq9Wd0fxZ?;}\x08*^eGwJLTN!2`q A8\x0be:aDe]Gf-eSPafYad"', 'KgiZ'), [16])
    def test_case_2768(self):
        self.assertEqual(pattern_match("#8y1Jx6_EN\x08F,83GB9FVC~Rq\x0bOsFV2'n'\rN<'I)Z\\\x08'\x0bc[frsI!@r^!6[_E;r9", "\\\x08'\x0bc"), [40])
    def test_case_2769(self):
        self.assertEqual(pattern_match('PAY\x0c2qCQ qL XOG)Ic0VpXVa91c2ncIYx7;}9J2C~Az797U7!E:[fqe.y#TU\tA@xjjMG', 'Q qL '), [7])
    def test_case_2770(self):
        self.assertEqual(pattern_match(" X(JA8\x0bpZ'{mjU\x08\rJ=Ll@T,t){k\r&U^c<2m? s8qSj|K\\\x0b'5rgFf1\x08=1G_4f9zvsy_zY", '=1G_4'), [54])
    def test_case_2771(self):
        self.assertEqual(pattern_match('f6\nRZ Pq6:pxXej6\x0b:\tgn<\\gz\rV?{vSMxJ9VI+C&AX3E}jq\x082RF[!I0vcJY_+X%tqFu[9Py69&l-p/mL{L9xHvrZ;', ' Pq'), [5])
    def test_case_2772(self):
        self.assertEqual(pattern_match('Q?f%!N3MjW(bdXQWBu$p\x08Fr7;9Xd.*&\x0cLlL3c1s5fGMW\\@WOw\\cSc', 'WBu'), [15])
    def test_case_2773(self):
        self.assertEqual(pattern_match('^muMZ-xf-!B/mJ<x`U*T&T9\nuG\x08t^){EDvJyng%O-i&^*Xh@`Z\x08m;8YXv-e?U\tp2_;@xgrTN&j', '\x08m;8Y'), [50])
    def test_case_2774(self):
        self.assertEqual(pattern_match('G&P)$\r2s\\~;0,<Sr\x0c#Q**@3k5~CL>MI(]GRLDN<4?^R}7YL\\&V/T QLL];7:jyf9TV=2 :4)7v', 'L>M'), [27])
    def test_case_2775(self):
        self.assertEqual(pattern_match('#)P L9\n"yODmSFX/(^J\x0bWOa@ln@\x0b ^oh\\k"%\n:-AanX~=#Rh\rb"\x0cA1g', '9\n"yO'), [5])
    def test_case_2776(self):
        self.assertEqual(pattern_match('Z8\'}:w,XP<ot3h}]V4\x0c?{\r~\x0b%*\x0ca$$@x@Y{@KlMLCaW] +Aq\x0coIG|cV\tQlv@dfOW\t\x0bFYnx2vr3~H>\r"oS_^\tn^v"qsIg(', 'x@Y{@'), [31])
    def test_case_2777(self):
        self.assertEqual(pattern_match('2Q:y*\t9S5]Ir?ei#Bv8oSm\x08*P>:$h_jkpT<pO~\x0c!\n,:\x0c,HYkUo4PiGi\x08|(Y!=f7<gTT]M+>T4"\te :+TN`\'S4[', 'Gi\x08|('), [53])
    def test_case_2778(self):
        self.assertEqual(pattern_match('\ru{M1f$X-\nART\x08/=H<DRk]p?yW)IL)UlKENu`/v?J\ngvpi*zf}H\x0bDzd/KRrR6ynH.PYTG&&AX}?82:', 'f$X-\nA'), [5])
    def test_case_2779(self):
        self.assertEqual(pattern_match('@p0ce)m$\nQDKWs#S?gZHKSV\rjgUm2afUE6"qph\x0bY/;Y`\nk\x08g;1Vs>HrSKF[pqD*j_Mp', 's#S'), [13])
    def test_case_2780(self):
        self.assertEqual(pattern_match('A1UU|;cS9z`X+&\r\'+,2}$"`XVw=`#^`}\x0bKdt/\'&4\'u*,\'Q+Kc;p;?a`)sw)8PZ=-7fOY@\tMr}0K', ',2}$'), [17])
    def test_case_2781(self):
        self.assertEqual(pattern_match(']&0Z3D|X`I?)UxN].~%K;CfUy-k.n:rcB(uQ*wES\x08mv=\x0c\tR6hoM3-:@#+D\x0c0[w-HP"zI3Wu.Wx<j', 'R6hoM3'), [46])
    def test_case_2782(self):
        self.assertEqual(pattern_match("M|d8DhB\t\nEYA \x0c`Dk&AM4uXA!&)J^'P:ORq)h!!y9\\6WL (movHiwinp\r>3vqII8dN-A{o[ f+", '\\6WL '), [41])
    def test_case_2783(self):
        self.assertEqual(pattern_match('p\\wrCJ{?`U\x08 \x0cwProkANEkwfDW`ol\tIP1C{\x08[Z\t]*~d~bf\n7mfm^gm8gwXH&u5kv\n{N\x08gFkLh M8_zl\x0bK)zA~', 'u5k'), [60])
    def test_case_2784(self):
        self.assertEqual(pattern_match("v3^2=le2S5;\n;J.Om=D$!s\\GP!\tj'4`#H:AQ69~Xl'N8e1|9%XOdy.?CrclZ[Y5HP+\x0b:*\x08`+9B[\tn8/\tDt2|~1K\x0ca(.MjX.", 'Y5HP+'), [61])
    def test_case_2785(self):
        self.assertEqual(pattern_match("SAC=sZ'.Z^BlWw%N<Dzu`3W*'6DeDJX_-^ HhZlJisA }#t4fn]'`6X1JJiT\x0b{B\x0c8_25\tEjb}]33d+\n2YtTp<kJ/kxZF(<UV|^", 'p<k'), [83])
    def test_case_2786(self):
        self.assertEqual(pattern_match('q((<\x0b qe\x0cnE!\x08#};np\x08i>4bv A_vn2l5[\r=\x08fx^_|PR!RY<]8f;F|M#Pj`S\x0c0Z8z:@UKU5~a\\fZcBY7"dcZ(\x08iVM 2\r\tox7Hq', 'n2l'), [28])
    def test_case_2787(self):
        self.assertEqual(pattern_match('k1|=,L$b(I\nI$tV$BE\\\\\x0bJ5tGA=WOsYG6\n4\x0b2AY6Ul\x08<YSO(G\x08PX~X##r9?lQ;.x5F_6h/N[T\x0bvXa\\\x0cn;pS.w', 'b(I\nI'), [7])
    def test_case_2788(self):
        self.assertEqual(pattern_match("UZ%!uQ4)ibpJk\n\x0b?!\\~}ksxQfk;+$}#yIm4AOQ>t=BfA~lcL?{Ve7t}q{L\x08'$V'$U8B6[K+6$z|%", 'Ve7t}'), [50])
    def test_case_2789(self):
        self.assertEqual(pattern_match("'8*'k'Ll7!^}1y\tHj*ga/`(0I6!y'6|y-9^$N\\c+CA>\tpP\tG{;sr5^&=}DFD\x0b8R}pX;z4qvbSq'd|", '}1y\tH'), [11])
    def test_case_2790(self):
        self.assertEqual(pattern_match('!O\\]\njvM+sFRPabpL dw@n?Lchv;S\\r{&G#\x08K=)x?c? T#U\x0b6<!3RC]~FPoMkE\r3~0/ZRN;1e\ti*I\x08 p\x08}P.{\x0c<`q', '\njvM'), [4])
    def test_case_2791(self):
        self.assertEqual(pattern_match("c]\x08$[\x08@PXx\x0bq,h\\%\\6G64\x08F2v}v_uW_k~EdqtazP}Lt`\x08\n \x08%2f@EeT`%k_)4p8b]$T_]Jr>4opwjY2 PHAjI=<x=T'", '\x08\n \x08'), [44])
    def test_case_2792(self):
        self.assertEqual(pattern_match("BG1-bZ4[{>O&!N'UE]\r=%kVd27\n.\t~$P\toC$vlyBy2p9\rrSS!y)BqX)jC27\nOv~", '\toC$v'), [32])
    def test_case_2793(self):
        self.assertEqual(pattern_match("R4dE7u7wMO)cvHKg'~;mIixBm`P4ec}sU3dE$+vm'BH0B L<u*uH@l-WI^mG5C)RT]XU2Cevw=S,_&", "+vm'B"), [37])
    def test_case_2794(self):
        self.assertEqual(pattern_match('\rwDOEFtK!e@Jh.\x085,<hH\n7O[T9w5JTfw)Y\tm~l$EMp!8U@=zk4UUa\x0bp\x0b5"NuRv714\ru 5BZ;N XZh>F0":-', '\rwDO'), [0])
    def test_case_2795(self):
        self.assertEqual(pattern_match('M"2\n9H1@!]TzPy!/`mBdB-,\x08{\tD6z LY2bc!<6z1%L+@ec!2c>GK/#a\x0c NkUeQd', '#a\x0c N'), [53])
    def test_case_2796(self):
        self.assertEqual(pattern_match('^(\x0c#i^ZRZ~[!Z.1\r=NK7bXI\n\x0c+Sd@6~KR,\tTO7L.@e\r1S1;r=jnH7HRCq~ju\\ou;FL ]{k3j6lX)hlK', 'H7HR'), [51])
    def test_case_2797(self):
        self.assertEqual(pattern_match('niy)fZ3h-0P2nz8lK\\D^][\x0c\x0cAZ3F{\x0b;s.U\nL KYWfqmB1tH;=(T*Ezz\t', 'B1tH'), [43])
    def test_case_2798(self):
        self.assertEqual(pattern_match("M\x08cJ,{57j)TYYH+tygo9?0|.p6X4L/vxh))rl}1@Ly3.dDybdqgJak;:\r\x0c'!zj_#\t\nw>t!)", '@Ly3.'), [39])
    def test_case_2799(self):
        self.assertEqual(pattern_match("-2klQK&IIO}Br8=e\tc\x0b94*#'^T/M`&AaKo&QM\x0bS%x#\t1>XG`\\\t3a51rn%cgjP&N~`|}6FyG^<k\x0bn]K/", '\x0bS%x'), [37])
    def test_case_2800(self):
        self.assertEqual(pattern_match('CQF-Q/E9dRE?)b+,PL]sm(@Hq;;L:_\t<Q(69uy_aLmEE(2Lo]/+3uZd\x0cr%3l|Am__Eh$`\rXmfXo\x08\tT+', '/E9d'), [5])
    def test_case_2801(self):
        self.assertEqual(pattern_match('\x08}`+GA\'"9ANQ)$@Nw$QgU1!\'s\r\n\'Xi4Ei&=\x0bAo}qkWp3{M\x080\x0b K}=tOlyJ`U+\'p`Rv\\\x0ceZMR\tKx<%#\x08E', 'M\x080\x0b'), [45])
    def test_case_2802(self):
        self.assertEqual(pattern_match('0^8F.D%U\r"zF@D|8MpOZ<CGjia9!K2PM"!bs\r\n\t\rS\x08U(\\QQw*Lb:z8Ep]yRr\\T*k;9\x08e_yR+\tx:UIv+\nD', '"!bs'), [32])
    def test_case_2803(self):
        self.assertEqual(pattern_match('x.}_9#G1U\rjC)`k;aDXSXiI|K_WNM`q"`eLhag16<c48E\t:M&il=9Wledc\t{BM\x0bfDj\rT=', 'ag16<c'), [36])
    def test_case_2804(self):
        self.assertEqual(pattern_match('c\x08jP}zfy.FGOLtDPRuHuffPz5?_[2(lrIII\rVSH\x0cFC+]7TnS8\nr', '5?_[2('), [24])
    def test_case_2805(self):
        self.assertEqual(pattern_match("f1Dd,d$\x0b}p`^v\x0b*I4JF)[\\FO4\n#Qg3Mq>w`;Sm.sgP%F2/lQ\x08bxn0~\ty[l/g/77QI0\x0c;;t\x0c\rY[(`y+sIz)OS'Xy WPTSO7M", '(`y+s'), [74])
    def test_case_2806(self):
        self.assertEqual(pattern_match('zT}YMrBw\x08tC3@]dMY$1|m7q,C^gmS)\'HCnOw\x0c-+.|\x0cXX%(\\9P\'xu!hIPp[c\x08@D3!"!Yu\\0o', 'Bw\x08'), [6])
    def test_case_2807(self):
        self.assertEqual(pattern_match('<YDxl?0U*J`]KTj]dy\x0c$IrYvQ0:CSCWh\\4n;+md(na7G<hZh,;OQx/,@PLDtg6N!', 'dy\x0c$'), [16])
    def test_case_2808(self):
        self.assertEqual(pattern_match('i:8\x086d!<cz<zHbn#^m^t;#r,k{O`4\x0b4ck7<8;]\t<?+uW-RsE8[M-|(2ma\x0cf\'.u*#.n8BO4LJ{"*\tg=', 'J{"*\tg'), [71])
    def test_case_2809(self):
        self.assertEqual(pattern_match('#\r,5fsfRu}}q])o\\f5 Cw5)%V$Vxhg|(<]bp,EHg2k#UbWcMLOyR/z,K[:hEF\nn', ':hEF'), [57])
    def test_case_2810(self):
        self.assertEqual(pattern_match('rS3<=ri.^vE:+>=>Yu\':YG6x&\x0c-p*V\x08:\n[>{mY7l3ja(t{iC@|-E<C!P;"R3TkDLD-LLo+:![u\x08', 'P;"'), [55])
    def test_case_2811(self):
        self.assertEqual(pattern_match('1;c&"\rtpWtf\\n\x0c&z_k9&0V,\r-v\x080>`l8lHi\r5BXXEB+7tsI6.cF;^21@A;.Y(c/@@^\rZ\x0b9', '\x080>`l'), [26])
    def test_case_2812(self):
        self.assertEqual(pattern_match('QD|Fk\'"9?sj\n1*O@$FKUoj\x08d\x0b`^)u\x0c\rE^!J|D\r{NO]LDs\x08!]9C&p<:U5:5U.l%Q-I,Z`nIp`7wi', ')u\x0c\rE'), [27])
    def test_case_2813(self):
        self.assertEqual(pattern_match('9Dr,m9|}_u+s`D>|.-Bhkx/p^B6x6=k }j.k3zXMekWrWr*"]_l/L",u7qJ\\\x08+":J]U%n<y\x0cH? ou+', '\x0cH? o'), [71])
    def test_case_2814(self):
        self.assertEqual(pattern_match('+}DAQjU%5Y\'C*6HQ\x08blZm8_O)+=at-*vpJAGe ]jW~2]c_^+2%[B]^\\k"\\E-X\x0b/e', 'W~2'), [40])
    def test_case_2815(self):
        self.assertEqual(pattern_match('3588fb--U$ N4fb\x08@6cc]&vaj\'D.Pu`:xY%\x0bV\n~sLIqI~C8ioN?4mu7OD"1qD\x0b?Lua^P<{HL0hAF|', '4fb\x08@'), [12])
    def test_case_2816(self):
        self.assertEqual(pattern_match('L4XYDQ]S~@_\x0c$N@,O; BJ>K4`2oHJ:T^v/"&cEAHY>;GrZuB^i?)QzBDl+ 1b', '^v/"&'), [31])
    def test_case_2817(self):
        self.assertEqual(pattern_match('%O(_SW<(P+4C[{ETIE6{f?e:`JR\x0c#>6k\n&><`M :};z)8s`1{1T\r1>[2"G.=*.\x08`oTv?MEL%%S[P\r>AvywN^(Qs9nnvo&X', '><`M '), [34])
    def test_case_2818(self):
        self.assertEqual(pattern_match('\\$O?-#{#MG~E/^DpPd$<lo]+}n;.|\nZc\x0b\x0c0[SXHSN\x0ciag\x08~#g|{X9}V[N*4!SQe,9hQ".{"C\x08k`unNv\tq S d= 4l_(4X\rC/', 'O?-'), [2])
    def test_case_2819(self):
        self.assertEqual(pattern_match("8EUm\x0b:p/!qC2m7JX\x0b\x08a]A7@^Bw( ';hzOScTYa]YI[DOq)B}@8\rV%67Bu{Vu_=i8&A43?5g}RZw2 :3`I=:mkV\rY", "( ';h"), [26])
    def test_case_2820(self):
        self.assertEqual(pattern_match("lA4%fDx:Cpu'y<Vy5zpo0|o-C/9H=dzZQDFo[h'cQ\x0cEon|\x0b7JvuM0&??Wh", 'Eon|\x0b'), [42])
    def test_case_2821(self):
        self.assertEqual(pattern_match('Nqf=\n\x08Bz*YEbUb\tiw1"*xM/\x0c\\)Db=9RH\n pA}fW6&zJI+W-!&$r%"\x08_Fi\x0bM|<\'meP=)]=I', '+W-'), [44])
    def test_case_2822(self):
        self.assertEqual(pattern_match('RZnOh\x0b7=IsJR@\x0ckfE\r$V/D\x0c=-8CWrV$\rv\nuuAy1t"P)X[I2RhRqoL1ta`k.~\\e {e', 'qoL1t'), [50])
    def test_case_2823(self):
        self.assertEqual(pattern_match('q2! \r%\x08VHV)\t^@h|}\\78bn%{ucsj HNY[.C"L\x08:n\'S^Wwp8+Q^U1J\x0blma%buAJ:X', 'ma%'), [55])
    def test_case_2824(self):
        self.assertEqual(pattern_match("c9ZJ\rW>ko:ZJu_:O\x08QK_@Vt_E<zV@yg?.zeJ?E4-${\\o3C\nf%1$\\WNn'/*bI#qe\x08j^m=*\t_iY?", 'I#qe'), [59])
    def test_case_2825(self):
        self.assertEqual(pattern_match('bFSFc}fo}z7i\r\x0cg+Qh_y)4Vm\x0b3hk_A(N5Vc@C7<X\\Pv8i,\x0b<7lWtkI6m-x6}CWJG\r(4F', '\x0cg+Q'), [13])
    def test_case_2826(self):
        self.assertEqual(pattern_match(']f7Dh">\rI9\'s\'xJMN>e$jZUr!B:7=$meB;p#xr\tXRSi_u5:EL:5;,):D\r_mtZ| &:', "'s'x"), [10])
    def test_case_2827(self):
        self.assertEqual(pattern_match('L*Qb)`Av6O65oG,GKPo8e^9\n4,tI"45XHx2sUrPy.b?Eg]D\n^0tmJ-]SQd^FNjV5sO?QL', 'b)`Av6'), [3])
    def test_case_2828(self):
        self.assertEqual(pattern_match('fr!q,.t@\\ESi9oM\x0c`]"\x0bC3\'jYT&*t\x0824Zu\'D~aF&G:-\x0c\x0bw]{T6O|w3M}0NP(SVI3OdAft;4ZF1h]aoO', "'D~"), [34])
    def test_case_2829(self):
        self.assertEqual(pattern_match('Dch:PgR^"`,![\n-zpm57Yr^6h\tkw6\x0b:\x0c,L@@C7OZvHM\x0ctBJBF{F5V{9y7e,U:GHc0zL^;', ',L@'), [32])
    def test_case_2830(self):
        self.assertEqual(pattern_match('^yF"(6l~\\H]+ P?=Y[+\r\nozm\'s-@Eg(<v-Z:>H-\' |$YcMzi>oi \x0c}', '|$Y'), [41])
    def test_case_2831(self):
        self.assertEqual(pattern_match('[.K;_y;PN\r@7!v#f\rcH\x0cTm{tryY!MG7ua[?)kk)D\x0b.dQ]T@nwk9c9)d\x0ca-ZO`Ug6"yA/;nm`+l?r9MG>9>k&s6gy~T\n', 'ryY!'), [24])
    def test_case_2832(self):
        self.assertEqual(pattern_match('[M\x08bP|)O/KG\x0cWRAuv11(%"7tX\x0bj94\nEv[D0 6%L=HSJ&mQ+jUH/kP\x0bL\tX\x08HWHkC"^<P16|\nbD\x0cc]BG!o/DTbD', 'c]BG!'), [74])
    def test_case_2833(self):
        self.assertEqual(pattern_match('0f~VZx\x0c@%.E*ZR_E+o,oSM7R\rmn|mj.v*"s.\t_CS0O6K\x0bCQ26Gs94 \\.4x`l', '\x0bCQ2'), [44])
    def test_case_2834(self):
        self.assertEqual(pattern_match('~vumDdDn/#.m`W7I{\x0cyN/\x0b\nTZui~)"3Hr[5~*KIbEIg_\nE#KEtO>FC2c\\R4[q[{e/Zat', 'c\\R'), [55])
    def test_case_2835(self):
        self.assertEqual(pattern_match('lQq5+f6-ClRm/o mXB"RVr\'zWRI@|RI`\'qfZnPwcA4\x08\n!dTb!Hh3_C6fsW[UpFwGaBA|/Me_', 'Qq5+f6'), [1])
    def test_case_2836(self):
        self.assertEqual(pattern_match("M\x08z\rJ[&0A}fhwLG$\rcfV\rb>57P}+1S~YES5RFgmG:!=dPf!hAYI([^WzN6ZY:9FT^V+|Y8<;]!h?^*zYEg8pA*'4txrTuj9K&Cfa", '57P}+'), [23])
    def test_case_2837(self):
        self.assertEqual(pattern_match("k.sl87YWojp;Ld\x0bP4q,kE*u*_H\\_+'eb%4^{S{';m ,bh22 qy'i*8TK$4I\nD\n[ARe:}5m[@~0\x08G4aAU\x0b0", 'm[@~'), [69])
    def test_case_2838(self):
        self.assertEqual(pattern_match(')ZOb7mHqeBDQ#lzp<x3\\LdjKXB0WE`\x0c#tq,Io\x0cl24]\x08{f+1i%46dx08(zSOAzd{"7Dc\x0c1\n{,Pnzap3u', 'HqeBDQ'), [6])
    def test_case_2839(self):
        self.assertEqual(pattern_match("!o!v;*^y[*bLrL3r+\x08'U^0_0};8jUm^2Gsdkxxk3I'>>@wZ=1rQkGh|S", 'xk3'), [37])
    def test_case_2840(self):
        self.assertEqual(pattern_match(')\x0b2;I?pHVNb\x0bKm/jx_\x08p;P3\rpm{vas\r;^\ntub#d\x0c[E`GeFM}!EV&f<GZU/LUSL]/D', '\x0c[E`G'), [39])
    def test_case_2841(self):
        self.assertEqual(pattern_match('srHy7i.Tp0<P\x08<\\qK\x0bH\x0cY\x0c9pnLmh_T\r*Cj5[na0`:^lKC\nN>oeJIui#/', 'h_T\r*'), [27])
    def test_case_2842(self):
        self.assertEqual(pattern_match("5De`meX`tqHroYKu%kfKc](0'=guQ7!A'm](f\x08~aO77D\tM(}~340,w:qYp_{1>U[<\x0b|Kvv6", "A'm"), [31])
    def test_case_2843(self):
        self.assertEqual(pattern_match('tl#wH\x08iK5w (4cgX(yx\\7M~9B-$Cd;\tHFNT8?o_\r\nfE:TrNm5<\x0c;L9#t)@.ke$7+ 0\x0cc?8.O.b', 'tl#wH\x08'), [0])
    def test_case_2844(self):
        self.assertEqual(pattern_match("IC)VG?R1.y|d42WQwc*a+rB}({5\tDY;@U3\nSY0O1^@cWL\x0cj%#,*PH+'-Tz[=\r(o!\n\r8IwLd\x0b8|bQ~.Zsyf$:G;", "H+'"), [52])
    def test_case_2845(self):
        self.assertEqual(pattern_match('>a<ftys[xjYMc2\x08:*e4<W0}9/HS,=U>5I]MF5(}JZCj/9/}%\x0ck\tAKCIwU4x', '=U>5I'), [28])
    def test_case_2846(self):
        self.assertEqual(pattern_match('FvD3%U_:([-{p6R[do\taV%YS\x08UM9>\tI3lgBa1dpdkEnz\x0cUi\n(dz=Tk0\x0c-\t3', '(dz=Tk'), [48])
    def test_case_2847(self):
        self.assertEqual(pattern_match("+' !iw[}J{S/.Qv+nua(j28)@u\x0ca7\x08w(\thZxp2WmhuAh1h\nqG L\x08Y_MsnL4UB5)\x08'Ikd\nA", '_MsnL'), [53])
    def test_case_2848(self):
        self.assertEqual(pattern_match('.y\r7X"Y$41`Xt?.N%ui`Bk9kR~P",IjI=E:XW;5@\'3{p9Q1;j4(A}V2;\\Gj.kl}b1_ATj+D\rla', '_ATj+D'), [65])
    def test_case_2849(self):
        self.assertEqual(pattern_match("e7=aR\x0bE{;6yyOtQ}>D]\x0c=don)i\x0c\t/rnunT9:B+~?\x0cv*4fJ|k>xn'w28:/JH=~fB~z1k%$7IX\\??Q*?WkG<\x08}V`,4C H+gI[", '=don)'), [20])
    def test_case_2850(self):
        self.assertEqual(pattern_match('LvAaU$)H$u$zXb9j,\r[l.gay>qR8s9}ajnBn]AcTc)Ww<#=u@T]-<z"%L)\x0b5whZzAH+uFc}iUkfE$te1\'3uTbt-\n2-\nv*k @qX$b', 'ZzAH+'), [62])
    def test_case_2851(self):
        self.assertEqual(pattern_match('rI>\x0crmDL8T0RNM[u8+( S\x0c1Mz#_AnHL#QMZ/.1gg.jP0oriQvF*5o=r\rK?8@r<Hl<\\1@sqU)K7N\x08H', 'F*5o='), [49])
    def test_case_2852(self):
        self.assertEqual(pattern_match('nc6=.@M7+kSH@TC8\\\r{cXrV6Z\x0bBa/x^A\r/\tf5\\Xsk)3OFnvAkGP~r\\dN38rHxKib', '5\\X'), [36])
    def test_case_2853(self):
        self.assertEqual(pattern_match(",Z:?(>yD~nv<5#Rjv7q9<IK'Z\nJ`cN0=v,|FyI[>hO]xC \r+tgpa%Lbx5%I", 'v7q'), [16])
    def test_case_2854(self):
        self.assertEqual(pattern_match('vJ/ymkC^qx>lqm#zl\nh^YP\n;\t1fE>m[u2?Nsv{aTPEY$$hkA0=mi!(aq-LIVRE^UIoYTrC~4!RUI6QM]5U."ijAIX!"c[o!R\t5$', '?Nsv{'), [33])
    def test_case_2855(self):
        self.assertEqual(pattern_match('R:VW\rWA_jsj\niHHrJEFxU)Hjbe(n`k=L%0 7$$y#sb5|(XcR[7%NqSV', 'HHr'), [13])
    def test_case_2856(self):
        self.assertEqual(pattern_match(']#^)1Zcfy? soh_N|VQCNOK`3xvY\x08\n#*#)th $$&qzSC\\5"o%N6=g\rU3WV\x08G3lqf!\\,)074jQ|r\x0cq\x0bGcX2AFuExl?^Ku~`_b', 'qzSC\\'), [40])
    def test_case_2857(self):
        self.assertEqual(pattern_match('mxu!\'0f&`<h\r[c,\x08p2eRY#D<|{_P\nK]Tqf}WR@C\x0c96"T7X\x0b0=)BbKf>/jZ\no', '<h\r[c,'), [9])
    def test_case_2858(self):
        self.assertEqual(pattern_match('o)|/d<Tu(H$;fc7e.dR^ \tFa410gha\r1^"\rM=(p xc=}J@?5=#TfgoO3H+n-GH\x0c$I${NvAhv|X^\x0cC[:uD!', '=(p x'), [36])
    def test_case_2859(self):
        self.assertEqual(pattern_match('S@^yy96[:1hP"P.8Ko/OC4gH6;%Jx8Xy\x0c.Zu\'k`W/xGd;:Q0LvHW:=dw+S0zR\\z+msY`;w', 'hP"P.8'), [10])
    def test_case_2860(self):
        self.assertEqual(pattern_match("P\rKV(oXfE\t/U\x0cs}?'d\x0cnj<,?1v\\Hb66|D.xJyUv%\x08$[!4Zm>!&`Q)i:\n`|P(- `#1o;?n1$KSf-Qi,?Em7uT1\n:+gW0e+Iq*\rY6W", ',?Em'), [77])
    def test_case_2861(self):
        self.assertEqual(pattern_match('hZ||sJ431\rfg9MEp,ZKAX<N\rm9uFUw}t\nr\x0b`%B3\'y>E-f`$\no(&!]4\\\rQ!:$E?)I[G=\t6ft$e"\t6ua X#/;b9uAZ&', '9uFUw}'), [25])
    def test_case_2862(self):
        self.assertEqual(pattern_match("Kd'>RAK@^wrS^Q\x08eD-e'6861K\x0b&\n{fZY^'.@>=zD)o~B$\nXpOW6+4_5.;<?", '>RAK@'), [3])
    def test_case_2863(self):
        self.assertEqual(pattern_match('bMstuo2p>.k$g1Ju0 yascoF/36,k@;]R$8.y>$y~rqEzgV\x0c)Y\r#"\x0b]\rst.+?pq\r8,@5mN;27uU\x0bQ\x0c7\x08Kk\\5&vj*\t', 'mN;27u'), [68])
    def test_case_2864(self):
        self.assertEqual(pattern_match('~+WYqww<_sZzKL|^d!tcO0\tUWV*UwfL0_7eOK|9+4=0\te\rnuY:y3)qv\x0b,.Q?V\\.jUYNV_', '\rnuY'), [45])
    def test_case_2865(self):
        self.assertEqual(pattern_match('Ix;C`<$-;\nM_"_h;0jVk7dHOxma\x08R)Bsx\t"(_WaK_\rdch !p,Hy\n)9 a\\\nUgAnyx9c~~=cw9xDz2:\x0b"\x08FQ+rd=| u]W\n6', '\t"(_W'), [33])
    def test_case_2866(self):
        self.assertEqual(pattern_match("-{fWah lN%/\r-,is\nM(~JNG%1~o_@/DmQb+y'/x\\uU}\r$q(UxmWb/EgDVv=,~%$P/'n&g<cu`%`uh5wvH2{MfMrKpS8hFQ\n0#", '/x\\'), [37])
    def test_case_2867(self):
        self.assertEqual(pattern_match('44zGhqo8!)ll4~G-\n&VKv\'oznSo|SV4R-1\'aHL_o(\t$SI,>>3_yyNZtYE\x0co?N5kB!\t\r/p\x0b6}#y\x0br\t]\x08K)DrQy"3\tE\x08rQ)u', '\t]\x08K)'), [76])
    def test_case_2868(self):
        self.assertEqual(pattern_match('I\n|e~hr`"3^v;?#w~0\'Z`"f^T_z&wV|-YfdppM?_J&r:ZEVg#+^y346)\t', '"f^T'), [21])
    def test_case_2869(self):
        self.assertEqual(pattern_match("zvGEOW6$Gd'}fG,#v5W]&``\x0blbqoezd'5/\rm~Sdl]9]j+fo_'9\r\x08\r'ompxMB$8=uFz;0wsYH`\x0c{", '~Sdl]9'), [36])
    def test_case_2870(self):
        self.assertEqual(pattern_match(" l?!pF3diuKGp=&<zzl\x08zUy}DJS#_ihBYt8J@j$8+7%j)W\t-QB,g|i4'vsj-*Qyb$b'F2oZ-TY3OB\tr aT$|FF\x08|x? ", 'FF\x08'), [84])
    def test_case_2871(self):
        self.assertEqual(pattern_match("8\n3^y5\x0bO@%5ghe\t\x08Bw4Zy\nW8a,i`soH6WDW*'yH\x08Cq'`b(XXV\\3q5j19#a}dVT[e`Vfb9DP24`]ivlYZ\rtA_m\x0bEV^\t=hzrk`g\\", 'YZ\rtA'), [78])
    def test_case_2872(self):
        self.assertEqual(pattern_match("uu%41O,6P^a@E#_:|\ns'P-#f~B6${J|YaroaqK>|52!'zm< (x zCFihgf@5&{4<#Nt\\%2Fk=h\x08]>kva`?$oNlB*ZHE5j0\x0b", '41O'), [3])
    def test_case_2873(self):
        self.assertEqual(pattern_match('`G@0q*jV"&\\0WOEyZUd=}{=g,x\x0bs;\x0b\rCv\x0bNds&SEwK~yi$r \x08MNs) s)zw8\x08]OY@,', 'MNs'), [49])
    def test_case_2874(self):
        self.assertEqual(pattern_match('#K\x08M:W^~HpM$J"?ejcaMAj/fh\\{j$2<8(*$\x0bBY@:n_8:sC\'~h%)W*C`qN=6vwa!/\t]`noSMn4xr/Cl.(L3<', 'M$J'), [10])
    def test_case_2875(self):
        self.assertEqual(pattern_match('W[I~v]t:60x7\\\n\x0bGa\rI4P*6:t|reS:\nchn\x0bV~Ne|B(Um8Js(oNRef*-V9!WSQ\n', 'I4P'), [18])
    def test_case_2876(self):
        self.assertEqual(pattern_match('fzTf\'h)Kv{>qf-(m\\b4M$gQ5<BwO\x0b{wI?$Z8|DBgvcfC5\tR:CO<"u\rsI|KE",|6t^gG', '\tR:CO<'), [45])
    def test_case_2877(self):
        self.assertEqual(pattern_match('gAz=GU!XIo\x08vFPj{~\\!Y)9SzqY=2:.O.5VHB)$(< &:Gw;\x0bN.,\x08<ov\x08{PBn)rNMX%bxrHD\r,(.^1', 'zqY='), [23])
    def test_case_2878(self):
        self.assertEqual(pattern_match('v3/N#E/=!vX~D%i!>yA=cH>LvQX\x08"vKc\x0c/>\x0c.G[_RExaS?\r\rqD\x08C+*~7^|]l3B\'i,jm5K0T]b#]+$[MXv', 'ExaS?\r'), [41])
    def test_case_2879(self):
        self.assertEqual(pattern_match("O@t_/;wOQf78d\n5e$fnu)L@WG8 ]dJTE}hXx;TE;xcT~!HV2V\x0bhV$q/A'XRgK{>@\x0c o", 'hXx;T'), [33])
    def test_case_2880(self):
        self.assertEqual(pattern_match("A@evX9a{\x0b>H+z\r-M\to/`x1yz!\x0bCFh}-'4x.*u)J*{|<R4*\\Yq|rZd", '`x1'), [19])
    def test_case_2881(self):
        self.assertEqual(pattern_match("6\x0cF\rh\\_w4Tscnz47[ii=;]\x0cD\x0b5()]JS~=;QEN5hL|,)2\x08\t[96R'o`JTH&mFgL&SkJ$W]&oz^.o c", '$W]'), [65])
    def test_case_2882(self):
        self.assertEqual(pattern_match('m50\rrg+Hhsua6s+vAVTgZ+sk"WU\x0bPB9 t+!r$\'4\'@xQ"q5q9%x\r8soRM6}3_2wB\rw7E', 'AVTgZ'), [16])
    def test_case_2883(self):
        self.assertEqual(pattern_match('@\x08\'A\x0c\'[ pu|{N`gBCN)MQehG-dj[y.>m:!n%(<\x08C.%CPB>Zm=Vt>\x0b`FBimL"P', '%(<\x08C'), [35])
    def test_case_2884(self):
        self.assertEqual(pattern_match('laB}{O6U(Kr,6Gko@FacTe,\rSQ_&Ksb\x0b 7xpsV[XK~d1\x0b09h<kv\tren!e"=a5\\)\n>(dsK@9cFSAZh\\ml^\nj n2\x08a4?t\r', '\\)\n>'), [61])
    def test_case_2885(self):
        self.assertEqual(pattern_match('o*E9lj;l-eh\rs"ChqYgs}l5COsUQ1M4pl8~5[9,Z5c)pE2"#G>+y&\thTn$8>+J \tYu0{dF;m', '&\th'), [52])
    def test_case_2886(self):
        self.assertEqual(pattern_match('dD9FFi.\n<RH-c\ny/u[lgqECU\x0b42\x0cp}=DL\tQ.6IjNzt,X`hpxrLhKQK4*S@#DA', '[lgqEC'), [17])
    def test_case_2887(self):
        self.assertEqual(pattern_match('{-0Su~8*2Wi/k}HabD8#\n0)&ff\\spu=\rGyI{Xz/XP4E\\\x0cRR*+4\r.2/6wK\x0c|Rh~XSR |9,\tz/R', 'RR*+'), [45])
    def test_case_2888(self):
        self.assertEqual(pattern_match('!iqw&2VzapIO Rc<:{>(i8\x0b1*o Ita86zf^}MZ2Zp<YkK\x08E =j%;B\x0bNfdeV-&e\x08\nq\tlsH|3sdmUu\x0b\r\x0b\n.9r[r', 'V-&e\x08'), [58])
    def test_case_2889(self):
        self.assertEqual(pattern_match("ZT9]pK6gm*M.-Y<['%7.,M k=]JNVj'%Ln>?:Pe1U>\tUc2B=~O0m2KB\\?\x0b4^WDV,:;", 'c2B='), [44])
    def test_case_2890(self):
        self.assertEqual(pattern_match("#Gm\x0b~OcgC9'*as 0I\rGWkss;|-e\rT4v~?ljE9h?J$\ni?JdAJ\tl*v/O;o", '\rGW'), [17])
    def test_case_2891(self):
        self.assertEqual(pattern_match('|m`NH<[{/pB+\r/4_/U2\n>V*]]M\x0b_\n;tS-\\/=~[}trd^Pkk=&\tHWu', 'rd^'), [40])
    def test_case_2892(self):
        self.assertEqual(pattern_match('-6@hhf[gz(fyBvG<)~+8*~)BE,b\x0c2ye)ka~U6fFs~  Pm7uFG^n%MN7s,\ruaX\x08?|4:d?n*Rsyc3GHtxU|4y6<4t4U/Fu9', '4U/Fu'), [87])
    def test_case_2893(self):
        self.assertEqual(pattern_match('+dS\r`d1wcFm:3JWz8g$\ri`\\103Y4@=i"kn&=vT1vUVg^X5rq>Hs^3M&_<\t,jUC,lBkVJ\x082"j56-:0', 'T1vUVg'), [37])
    def test_case_2894(self):
        self.assertEqual(pattern_match('HW\n$65I\nMXmH`D?ivxe\x08$\x08qW+x\x0cyMytn\tLZR3|q.(T.5WeRu_\n`=fF=!Sx!\x0bm"8BIv\x0b\'/r\x0bZ>', 'LZR3|q'), [33])
    def test_case_2895(self):
        self.assertEqual(pattern_match('V%T|x}KQ\nyrS`NFvyJx=\\mvLV\nz9<}00I=1"YJCSk!*;JH\re[TXF\'>?}XI8/o', 'x=\\m'), [18])
    def test_case_2896(self):
        self.assertEqual(pattern_match('}."i$q p.SiF#;}r\'/*yRn.\'8\r\x08Sgn\rqU umXRh:+1=vy5\x0c)5<e@</*wiEU>)R>\'\x0c8I,+E', '\rqU u'), [30])
    def test_case_2897(self):
        self.assertEqual(pattern_match("cn'Z:J<!>Nh{Pah\nf%H:=#rKx#\tKsuf|TNp^\n #6397|X9Lrjf!H\x08I$G`(_Du3.fFc\x0bV", 'ah\nf%'), [13])
    def test_case_2898(self):
        self.assertEqual(pattern_match(' 7\t.Ivf"`f\t~<;)QR2fdttst\x0bD\x08LGyJQrha[:F-kaFQy \x0c\\X#H\ttj', ';)QR2'), [13])
    def test_case_2899(self):
        self.assertEqual(pattern_match('irxr$IA=?A_"-T/>f\\9.SvnC/$ZfV*A[:AVp"Oyr\'stK]skbC6mw"!<7\t&=]r%Cf~B', '\t&='), [56])
    def test_case_2900(self):
        self.assertEqual(pattern_match(')G/Q)\x0b(?];Q9\x0cr&szo.?jp-{qymAlqSRj/JTc\\KJqC43Pzx}~\'\x0cF>,C4SaWM,LV\x0c<lf~0"Dd\\v8>3VMqDK', '"Dd\\v8'), [69])
    def test_case_2901(self):
        self.assertEqual(pattern_match('SEAlxkn3"\x081fM\r\tyO,jRQv\tc%(.zzBF,/;KL\'?.\x08;C{$j\'ZsTrl=\'9h\x0cm1\x084a6_bkD!YJ?7Cx!\rY2', '.\x08;C'), [38])
    def test_case_2902(self):
        self.assertEqual(pattern_match('wPoq`|\n^ H56&|6}^;\t7ce^"+p>>MjS1y\x0c%/=R64O{69<Q-uVjFb7K3Ph1L/aJ~W6Ow]uq,yKXX>n6l#}($ZNzLB8\rio0P', 'Ph1L'), [55])
    def test_case_2903(self):
        self.assertEqual(pattern_match('f>.zYfH&50V~@\x0cr;&;v:D$"`c`J(5,Fz"e4p6KVBT"Ju\tN8k9l47p&', '(5,F'), [27])
    def test_case_2904(self):
        self.assertEqual(pattern_match('B9]\\qcil\x0b8w$[75C}tjCE-$pY{<:3.9P\\E-^^&F`n(}eI"!}l8k;t\x0c\x0bkO\\2#VY', '\\E-^^&'), [32])
    def test_case_2905(self):
        self.assertEqual(pattern_match('Sa6<|hFa3D"*-c:\\C~*\x0b\x08yY8{W_\'7{-C/3,)N<)PZLNQ@VPxA/_4~.j~OoOq;Wt3?8Jk KHY\x08+J\nZ\t/O1\x0c-+(D{El@X-cug?m', ';Wt3?8'), [60])
    def test_case_2906(self):
        self.assertEqual(pattern_match('88%0cM`Z`2ig^5xavIG^R<aHCF]PYo\\GpEm%t"?<Hz<yg!"_*mNkVaKiX,d\x08', '*mNkV'), [48])
    def test_case_2907(self):
        self.assertEqual(pattern_match("w&K6D\x08\\LxQ.p2)N|7L]\x0c>K^1y8kX~iGt6-pEYp.+tt\x08\\ky*9Z{75'^nk6\x08", 'X~iGt6'), [27])
    def test_case_2908(self):
        self.assertEqual(pattern_match(">\x0bm-]Nc77bQuq`!\\#tT(C{\x08\x08\nNYzT910^sR\x08\t\x0clE7\ntln\x0c\x0c[+>\x08e?\rw>t/+agbm\rV&DtVt6rlrSKob(<\x0cM)x\n5MRcj/'[(N3GrAA", 'R\x08\t\x0cl'), [34])
    def test_case_2909(self):
        self.assertEqual(pattern_match('aE2Z`R=r)6%U>~e;=o\nZrO\t"jqYcig!7pFPKsZ$ontG/T&wjnio', 'g!7pFP'), [29])
    def test_case_2910(self):
        self.assertEqual(pattern_match('h(We7+\rnp\x08UC&!.>!\x0c\\ZJR:]+c^:+D)1)ctW,MF@UYh\\Do\nA0\\}TO&hX3(#wQF}', 'C&!.>!'), [11])
    def test_case_2911(self):
        self.assertEqual(pattern_match('bF)#Q9\'k*meZ\'*Ow%V,|,I8p>QAv[Mx4w;P;DHx`f:OD[8+,gMN,M(\\]Yvh^\x0cb!mC;`\r\nZ/"&6{', '\\]Yv'), [54])
    def test_case_2912(self):
        self.assertEqual(pattern_match('YWM:E]mbTr\x0b+=<Ck6!crI=E}W2fTV:OCa{U=Zh$Z\x0c;sI,Y*zp5b#xX\\?)FOIEt(JEa07Ik%VECv<A3\t1Q\nvVo', ']mbTr\x0b'), [5])
    def test_case_2913(self):
        self.assertEqual(pattern_match('`[%\tm?&cKGLcpD\n5a&=6*kwq]I=x@+iH!ltA}3-zU&\r3{(o7CA^j_5wIqLYPP7\x085h~XP\x08w-~}\x0bV\\n#=/|ClKv', 'LcpD\n5'), [10])
    def test_case_2914(self):
        self.assertEqual(pattern_match("tFy9n}i-\nB.pg\x0c>vjlF' |L7@%D\\[B~g|!|k(;O4>+i$l;Iky}\x08Q\x0b\r+`>(.", '+i$'), [41])
    def test_case_2915(self):
        self.assertEqual(pattern_match('OKUvE]i/%[C^?T/+J5BYKm_1Nu+Lct/MU P,bPCxV20 :6^\nbE;ly^~UM\nLpvT_6*hK![e\x08', 'PCxV'), [37])
    def test_case_2916(self):
        self.assertEqual(pattern_match('K[UV\x0c[z)\x08\x08S 7xv|;GqkxpZpG+dbas|\x0b/}ubrxc)};RU>rB_"A*?Xr[v', '}ub'), [33])
    def test_case_2917(self):
        self.assertEqual(pattern_match('l=K\n|Y>zOQ:!sSu4\x0b<#gdr(8p\tEx~l\n8>z&%BT6q/X)8Qh/d^~/B<3]9X-}Mm', '<3]'), [52])
    def test_case_2918(self):
        self.assertEqual(pattern_match('t]m;pqA=!9;\x0bumw.zQW8BHJjU8hTUSM\rrX4<L,"K"0g@A\x0c/#tXrtAXU,Z,J$vDr\x0bw(\r80YGv]FkQE}Kj\x0bG,,z\n"tufDfd\x0b8\x083', 'W8B'), [18])
    def test_case_2919(self):
        self.assertEqual(pattern_match('sbh=\\Nkrme7}\t^3S~Tr$tr( \x0bYUKS4\x0cGu=eQW7v \x0cZg_(mn^Ivc4\nEda\\$\x08Fp+\n!@AnshHBxZk=\r\n;w7@^5', '}\t^3S~'), [11])
    def test_case_2920(self):
        self.assertEqual(pattern_match('op),=z&Tec)ss2%qZHTN\\z5?)\x08{lTT 10H-Sb&n7Dgln3PVx\\\tE\x0b45l`3k9', 'Vx\\'), [46])
    def test_case_2921(self):
        self.assertEqual(pattern_match('#~,!P\x0ci\x0bam_"2U\'w%w)F@:]Ss9)U?;`\r+Z1kp[Ya7W^F\x0bXcc7K.k2$H:\x08\r1Y7!"=ZHWdhoMpR<-$?C\x08/\r?9?Z=', "2U'w%"), [12])
    def test_case_2922(self):
        self.assertEqual(pattern_match("7gstYvmyP<!xYX\x08o\n`PNr5D&FYgYrDnL8){.oF!&{'\t,3/o;S){Wt\nPubohwdJSY=(rB", 'gYrD'), [26])
    def test_case_2923(self):
        self.assertEqual(pattern_match('f"O9k-`F,_\t/\n%lZ~npXuGm !w2.A?tn**U >\\zhsP)\t,|VHU&@n.\x0c^%\x08aawJWdaF', '^%\x08aaw'), [54])
    def test_case_2924(self):
        self.assertEqual(pattern_match('ZFS"5FmrhwO0T_u>YjZ|?v>X3rc+4qYO:=J:)6e|bxofaCSIR\n8b\rOiP>\\m{qg\x0bFVhm22lI|2j\'7[n NY)zrk06o', '>X3'), [22])
    def test_case_2925(self):
        self.assertEqual(pattern_match('`jv}=&@\nmU97g3^i3}\x0b\x08vCXg^BZo!-"\nT"U{a+B:(NpcsMuZ\n33_jn{5Dd8gsT\'>Y3n~', '33_'), [49])
    def test_case_2926(self):
        self.assertEqual(pattern_match('Qm:}Z-%?i![5T\x0b IV8IR2 M\x08^BI3lxB_T~n(\x08hgGu\\?!]bk<x2%#Zcg3%_P)v "Ba)O8]l[zC1!', 'V8IR2 '), [16])
    def test_case_2927(self):
        self.assertEqual(pattern_match('o{s$\x08li\x08BTvqH1|716qAu~w0p\rc-h+_f\\{V<|uiVO\tbNqN-*$fZz(>g[1eNz-ZRToz~&Q?H!HS', '1eNz'), [56])
    def test_case_2928(self):
        self.assertEqual(pattern_match("yU*#nb3^nGO4u:S\n_Q#*KJTuD&f>m+URukz>ICdTO}H'Qs{>_W)v^a.t4bvl*\\|*3MrLp\n]s%Y\rIr,HD?X1Th~rb", '^a.t4b'), [52])
    def test_case_2929(self):
        self.assertEqual(pattern_match('}T0b1+D/Y3;tELVX60k\x0bf6oT@I\x0c_zGdQ;5C<ep|+Mh\x0b8|nv\x08O_PrTUuC&u[7VoId[53^e2Z{&z- ,2;FL1?w0I{{yW\\<!1xv%^,', '3;tELV'), [9])
    def test_case_2930(self):
        self.assertEqual(pattern_match("S$/Ayr2v'^=V0h#i8!ua1*$SPP>/PNtEe$Z=r4?pk)}SCK8Z0a%Ipt92Z1T4bh)hhb", "v'^="), [7])
    def test_case_2931(self):
        self.assertEqual(pattern_match('N\r)E8DMnDb+]\tx"jM:yxW-,o[2s|/2Gxj"t!\x0c2MTSA_s=| %SA9q$Rtg~7\x0cj[', '| %S'), [45])
    def test_case_2932(self):
        self.assertEqual(pattern_match(',#=q!uw"h\'8ZO,g.6u#OPrk:/\tyyvl|v8Zg$88znI"8?N1&dh<B0\\*_', 'k:/\ty'), [22])
    def test_case_2933(self):
        self.assertEqual(pattern_match('Q\\W! qe^?TNCcT"Rtv:>N\nI;VN)UqAo\'QLhD-iR<Ig[5D\rsd\x0c%w(\r uYHBs[LR1\'G\nV\n7!lFo;', 'D-iR<I'), [35])
    def test_case_2934(self):
        self.assertEqual(pattern_match('O{tbUV!Ri7{f|aUNX\x08mLqz`Tt 2Evy5/sH}srt*gbvKW1rLI{GD\rx2zmkm-', 'Tt 2'), [23])
    def test_case_2935(self):
        self.assertEqual(pattern_match("/(^Y|(3~\x0cpE^EZQ0Sj=>$7;jBW7m<suzIM~NFh&SPj\t$N\x0c'kr\tL;\r\tL\x0c?WL6Hc\tlKb@|hiD0", 'Hc\tlKb'), [60])
    def test_case_2936(self):
        self.assertEqual(pattern_match('OYG^s=j>=T\x0bqNm^&[8,#zk1,}cc[:<*Y(\x0b|vT8x !FnR:tqu1a%VngQs}7~|T5$cfYHOR-o >}",', '8,#'), [17])
    def test_case_2937(self):
        self.assertEqual(pattern_match("0FyP=j.w;{'nj\rHy$Iw'o~|bsF\tF9)x)\t+BQS4o_]ITj[$1G%>K_57\x0cTJ,.*\\$,o\x0b&BeGw8`>YCZ\x0c>e", "y$Iw'o"), [15])
    def test_case_2938(self):
        self.assertEqual(pattern_match('D53bg H 8rzKSAf<7\x0cPxq^AxfNPy~D:v:\n =HD-MbXoJwhA"~)[h\r\x08G5T=!=$<Y9=a3_wzw\rNwr[\nvbEML', ' =HD-M'), [34])
    def test_case_2939(self):
        self.assertEqual(pattern_match('"\'~ .t[I"9DhDlBbixQY06*)PVFLpSOh\'}ga?_J#PHEnIBU|~\x08b;Z9TC--rXH5%/3S-I/', '#PH'), [39])
    def test_case_2940(self):
        self.assertEqual(pattern_match('-\'!"aS\x0b=B(+/FA{c76-)!Wec\x08*W*g1$bQaOj}Yy\x0bJr9mB{>00*!U>6z)H_`hqEYw\x0b4W\x0b6QJQ\rX*"SwZ4i\x08\x088xcdOQ:', '*g1$'), [27])
    def test_case_2941(self):
        self.assertEqual(pattern_match('4.jhl>:Op<Jxh%\x0b@\n7b"MrgG,W$4%95l\x08W\rlTV<^.#G[l\x0b,{0!Iyn OnC\\\x08I\'fj0/+64zsJFNG`0GE{6# 2s2hzqvk10xF', 'C\\\x08I'), [56])
    def test_case_2942(self):
        self.assertEqual(pattern_match('<|&/wE<#j6T;XT!9{rS""#,X.oQA$JK\r$n\x08\nZvB;|I&lM"MO0OlKK3(rK>\taO%\tqh', '\r$n\x08\nZ'), [31])
    def test_case_2943(self):
        self.assertEqual(pattern_match("E9sg jR|L6&~x'\x0cvb?GVdhSeg=k-#> ;PcYlnCzSk_)z.b1fC99)M(\tvVU{rOfD4G&[GP+!$", 'G&[G'), [64])
    def test_case_2944(self):
        self.assertEqual(pattern_match("=Y'De<f)=C\ntiK^C8=V9qUy4\r4C(owr.&=,TWr!eD9Gm[/i.aQP^\\#", 'eD9Gm'), [39])
    def test_case_2945(self):
        self.assertEqual(pattern_match('hi*HC\n\x0cKJhN`eDDc|`Wi)uB5w#?]Z@;\x0c ?&95\r6z?|{pwz;t5{\x08n[%f/tn`B/^o\n.{` nm>uN}', '5{\x08n[%'), [48])
    def test_case_2946(self):
        self.assertEqual(pattern_match('Q7N>.er"ou.Q=E*08qt?C]=\x08$4nR4lS"DJ>RQuz,J]u\\}(\nL,;UH \x0c1Tk~#=|XWz68HkxtHF `#q+ty-', '#=|XW'), [58])
    def test_case_2947(self):
        self.assertEqual(pattern_match('gE\x0c;@t-`\n-O#>x\x0c>=U\x08g2e~2IyZ7,|V"z>Ptx4n"iXl^ll4j[@ONve[^ZO\t', 'n"i'), [38])
    def test_case_2948(self):
        self.assertEqual(pattern_match('!bTD#x<zfQOy*\x08RJqQwk#C&TED\\W\tWKC]\\ofl]E=\tL~{U<d3-@g9a5`j624FL&JX\'\n^&\x0bCqhr"\tWUt:[pHVtW^V#V\r\x0b', "X'\n^&\x0b"), [63])
    def test_case_2949(self):
        self.assertEqual(pattern_match('9I9H\r9m6f62h\'f\']66j\tE-\t\x08!|D"Tl99@"bcZ\'|\x0c#,|eIy*<TjP;s!!5.FQz1\tkVk\t~', '6f62h'), [7])
    def test_case_2950(self):
        self.assertEqual(pattern_match('\nG)+AtSY\t#g\t\x0bN<q{(qkd![\x0bw[rVx[M^I^eU7sNc\\P I"+*M!FqbAfS,H\x0bsL"Um&75f}\t}E)m*v', '\x0bw['), [23])
    def test_case_2951(self):
        self.assertEqual(pattern_match('a%4uH\t0JJ\r;f\x0cuX/Vp2C, >z\n\n%fEeac@?\r/}W]\r U k\\GME \to4C+5D71`dxD+R;\\a*/n$h^sE3(c[\x08PXprqt)\x0cF2^qEmP', 'rqt)\x0c'), [83])
    def test_case_2952(self):
        self.assertEqual(pattern_match('ccJOfaH[ICR;@tlivf8iFBsm9pkbw^6U8oU@M4l3dlD=j\x08I?NS+#kIW \r}c!C&\r$qI*[;fEUx?=Qj/@A4|H^$QV%lETRRh?m.39', 'faH[IC'), [4])
    def test_case_2953(self):
        self.assertEqual(pattern_match("Vui3EWj G$bdz\x0bZdP{%pBQG7jkUytu\x0cL'{rYdq~k\nmNGx0w^[:", "\x0cL'{r"), [30])
    def test_case_2954(self):
        self.assertEqual(pattern_match("A'&)F@ yN@a\x08LXRQ\x0c;@J?fqN^m%k*[yCF604h\x0bIIFM(18B)!&#+Wpjq", "A'&)F@"), [0])
    def test_case_2955(self):
        self.assertEqual(pattern_match('-+cm]51+5eey*xH$W\'FXEQ#i<x>jYeh( m|om\x0c-p_IKO3g&\x08HaF\n\x083Z~;2jdcJ$\n24n<T-G"#\\d', '1+5'), [6])
    def test_case_2956(self):
        self.assertEqual(pattern_match('}]=dWoWRZv45t(>Eplzvqfa;<E6}[2;\n<y/\x0b0\x0b9:0GwC6\tqp:k mwXO e\nF:\tjPjP@oFrw3So#\\CUIxsu0ZaCX+m^cHHZ', 'ZaCX+m'), [82])
    def test_case_2957(self):
        self.assertEqual(pattern_match('iNl8.20N/lr`YWY2^\x0c<JvIO\\f&*i?9[.e2_`:2A-gV~H(A5lZVt.<e)Ak{zl@#/,q(>d9^YzgvFHrOLf$^aT)\r7jh3F{z', 'i?9'), [27])
    def test_case_2958(self):
        self.assertEqual(pattern_match('3+R_#LwrH-t|\'e ;$r:%Gx%T/uvpU}C,*\x08\\!Wn=r\r<2`w\x08 Z@6!7OW^J6X7|&W"%+"(7$>NB4\\V}8 :($:#v-f\tqf2oDe', '"(7'), [65])
    def test_case_2959(self):
        self.assertEqual(pattern_match('j<mp6)\\Yf\x0bnu| ?4YJQ#\'\';)\x08MtOH{1_dE\':r<1"9<D>($="b<b\\4a', '="b<'), [46])
    def test_case_2960(self):
        self.assertEqual(pattern_match(',L@j\x0b\\=N,?K5wn;iS[")\x0b>.S[{AwegzP",]RxHdb?/@"a8!2Zh', 'wegzP"'), [27])
    def test_case_2961(self):
        self.assertEqual(pattern_match('!#|+yiGHFA&!`3%H:$T,`Jsz8\x0by:)]CPpBx,=8)c qco7l[\x08BKU)A!5o/^pXdwC8|z0\nou+\x0c7>Dfv72RYTr174iI4/g"', ')A!5o/'), [51])
    def test_case_2962(self):
        self.assertEqual(pattern_match('\nG(nC;,e\nTuQ3wkyfs<i 4[eHJ|\ti-\rJu)X/){VpzFC5zfJ#Q\x0c"zYX86.&T`ubw]zd\tE4^\x0bTU-z]67QF\x08{V', ' 4['), [20])
    def test_case_2963(self):
        self.assertEqual(pattern_match('ooK-\x08*[*v[f*A\x0bUunm+v\tp5\tFkRKfzz,\rdA$8O_Q$<)k\nq@ygBli{_BF3\rF0uRD;MJY\n_T0pIl}y', 'zz,'), [29])
    def test_case_2964(self):
        self.assertEqual(pattern_match('\x0cy;U%+C\t1L=jr)lR6j,tl-soLn+O\x08\r Sb\x0c_m +}>~a86zMwktX8t&cG}7qX n', 'oLn+'), [23])
    def test_case_2965(self):
        self.assertEqual(pattern_match('Pt\r1\\>>i(E2v1uv\r\rOe7VJi.M55l!f0^Y0^$vDu\':9)p4NS$#2[e]h;!WU5~]JD"nu/_|t4M\'%\x0cR\'YFm>Tq;I', 'WU5~]J'), [56])
    def test_case_2966(self):
        self.assertEqual(pattern_match('ch\x0b-.4z[4=\rn~%8@uzaiXLJH/F N3NC3VZ?3}y<F\x0cp4{0{Z_9cBU\n5JW;IgE9]', '%8@uz'), [13])
    def test_case_2967(self):
        self.assertEqual(pattern_match('Ek>Ap=8uA{4J %s3o5\x0bC+ol}eOobd3pCATsn}4Kya(~UODL5 {\x0bU?d\x08OVl', '3o5\x0b'), [15])
    def test_case_2968(self):
        self.assertEqual(pattern_match('h,A7%\x08!N}0nIZ#:Jy}Cs<\x08jfvr^v8\trD\x0cqAdB?=z#!V+\x0b)oM|F', 'B?=z'), [36])
    def test_case_2969(self):
        self.assertEqual(pattern_match('/a_\x08F!)Z:h7A8\'R|"&8M\x0bprY@+#5kv.+ffB; q:&\x08mJ!H"5=5-7(G@661b5\rQ[`NhVS[h:dj0LGrK4YLus/', 'j0LGr'), [71])
    def test_case_2970(self):
        self.assertEqual(pattern_match('s{O<q^@3^2mVI~Q#U73\'fB\tY0ez=~y(p2 "geSalG>$"Ll)\'{2\\\x0b+<@};fX IbZq4`Pm Ee[1XuCo^]+9M|ho ', "'fB\tY"), [19])
    def test_case_2971(self):
        self.assertEqual(pattern_match('tE119n\ri%JP-=6y_:54gq=on\x08`}QS\tl8&8?Hc0LbNX5`icHy4lh;i\x0b`Q)O-', '\ri%JP-'), [6])
    def test_case_2972(self):
        self.assertEqual(pattern_match("\x08;wC.@\x0c P(m';{I]gq\t~\x0blK<lRkE-e!6](lDp;Y\x0bc^d*'SMxhnDI;#22:iI]aK}x|`S6@FW`kxD", 'K}x|'), [61])
    def test_case_2973(self):
        self.assertEqual(pattern_match('`%_69+|H<sMh0Z~uw)pupvbQIN)s%j/*Rf;tMl0`-CR({Tnd@!0\r>WHhhXwA', '0Z~uw'), [12])
    def test_case_2974(self):
        self.assertEqual(pattern_match('!\t<T-J`<|u:-0\n.U@xh(|?q\rK27La#2.0"8@dmcm7rL.MBQ6t[;4liSQ-ud?\r.V~m', '27La'), [25])
    def test_case_2975(self):
        self.assertEqual(pattern_match('oo2N8$UD""\x08ttIFvdE1a=4zi24j\x0cL\'y\x0bj:9(JM#V6/\tDo/h/<# /<', 'M#V6/\t'), [37])
    def test_case_2976(self):
        self.assertEqual(pattern_match('0Z\x08RrnhNoAf+]5edvLc_II\r+-Mx\tr`@]1!UQR$0of1hnh|G\x0cEUDUa!qK/jXm\x0clYJ!  =P/okYDGI2B=W)dE', 'Ua!q'), [51])
    def test_case_2977(self):
        self.assertEqual(pattern_match('vC<QHg\t.WF2$bFnzB\\Vl07!/eG3"b;gFv_=T@7x\r(9B92SN[H".`>', 'bFn'), [12])
    def test_case_2978(self):
        self.assertEqual(pattern_match("T_\te6\x0bP16UL7\rD?%4Kz+\nhTx*QHnlez2jS#ZY@K<=F'z(\tsbgx\x0c*4eh=9x~~DX+7I:~KSf,d:#``PD'%*", 'bgx\x0c*4'), [47])
    def test_case_2979(self):
        self.assertEqual(pattern_match('(m;STh/_u\\BCDZuTuPcuJI|#/forIv0.8]bm\tG\nht"\\1!B8P9\rok{pAgFDd@aA&:TX', '8P9\r'), [46])
    def test_case_2980(self):
        self.assertEqual(pattern_match('/KvTsL`j(zLaxLtRU@\nKIV.Mf7FnN=DmZ3_=\x0b!|^,r"&)EE8>JKtv%soO{qur[!I\x08DtT+u."/amj>5DhP_Ek', 'f7Fn'), [24])
    def test_case_2981(self):
        self.assertEqual(pattern_match("]F\\rYZr`S=p:T/.)\rxX12XR;1M$+:/|0DV{MDJ/+@PB*,{[0N\r->`\\S'2z S'Ct%6$)'", '->`\\'), [50])
    def test_case_2982(self):
        self.assertEqual(pattern_match('"1?j^%s@\\\'1mc=vTVVBqXoUk=]Y0}?=Pn/\x0bgpD^1af _<G$mg!=9~iJg;&!l\n]Q)bk`{(B\t', '"1?j'), [0])
    def test_case_2983(self):
        self.assertEqual(pattern_match('crs?*\'Hd@C\x08pX_YQEPm\x0bD@CW!c8m)I:r6X$\'\x08$fl6@Js}r\tbb)0&eh]j\x08BH~Q<P2Z9zr^`!PfmfP\x08GD1/zt:iykdl\\[z"S', 'GD1'), [77])
    def test_case_2984(self):
        self.assertEqual(pattern_match("Z#S\x0c[bma>d,Gu;~#B*Ue~0~L=e(C5'daUA\x0ch4\x0c3VXz$]1]a~ltA^L/5NY@bbisd-w\x0bV[WF1IqYtLE&:UCOhW", '\x0c3VX'), [37])
    def test_case_2985(self):
        self.assertEqual(pattern_match('%h~T\t1\r\tB%x\n"eKNCqNNmM9/"J#nl0$VF0=5.5$T`:veHGcec#Iga6g:,kDw#NCY0X&TwN\x089"5\\\tX/uC"KdV:D', 'N\x089"5\\'), [69])
    def test_case_2986(self):
        self.assertEqual(pattern_match('QLo}y.\x08?P\n\\Sz6(UB-e=Z_\'{kdTb1OM.N{6"J7QF\'|d^DvdCHI?hG\t=CE>IoX\t\x0cA', 'd^Dv'), [42])
    def test_case_2987(self):
        self.assertEqual(pattern_match('2So5c^\x0cMWfDHG#[{ul4\rC6.-fO5omTUio|5}aA.^kyqBh"H!(V;3/xVZtdj>Yu3Qp\r/|he$', '5omT'), [26])
    def test_case_2988(self):
        self.assertEqual(pattern_match('}}TLg<O\\!.[~!2p^/ExAy.)rx3\n@zYK,z<r!P.m5EMr|5NVg3\\J\n4NW[We?T^>h_[FQj&!<lg1oj4Qo~Zi\r;nv>qI{E4P', '5EMr'), [39])
    def test_case_2989(self):
        self.assertEqual(pattern_match(';|g\nmu8w\'*xEx*/`j;HR"\'Vf<7@Ko Cze\x08He#uon.7-\'W\tSxYop nkF_%&0Wn&_^', "w'*xEx"), [7])
    def test_case_2990(self):
        self.assertEqual(pattern_match('pW<#{)03~o~htt\nI|sNgmH4T48>S CPL]D[^*cV0SeR+>\\es{#0vb]q>2DCVF@njWO;ukSB*?*', 'L]D'), [31])
    def test_case_2991(self):
        self.assertEqual(pattern_match('XfGZ8O-h#M@qazv0E"8yFmd`=\\4>iuD_S>\nX/8fXT"8frS\tYIPc&Uee|[\x08\t\rh)qb\nA0C54)8\re ;hj%Y~?', 'b\nA0C5'), [63])
    def test_case_2992(self):
        self.assertEqual(pattern_match('$La^X"?\r0S\\z?i7e2Bo/N%?)QtGQ~@jts`wRM@B/n~<.w?u<;2Mf7[fgeK^40n#:;fz l2H>%qoa&$', ' l2H'), [67])
    def test_case_2993(self):
        self.assertEqual(pattern_match('[7M\x0b4D5tuTwg;2CB}QYBD9t6K/{s]huq6A81;pF-k/e^b\x08fkDtl$+ttQtJKbU[\rwguP8\x0b+Jf[8;Rm?EO7g.TK\nP', '/{s]'), [25])
    def test_case_2994(self):
        self.assertEqual(pattern_match(']u=6>t[x.0ODWE,jR>so*\x0b"Z/\x0bby,lhX\n\x0c/Dq8r0>n\r$-@f$?fy', '"Z/\x0b'), [22])
    def test_case_2995(self):
        self.assertEqual(pattern_match('*"Sf\\sN*R@=Z0m-Ddp6W\x0ba#!4e8_T335U0B3OFTNd/\nI\nBJ-1Y\x08&Mwb8GmgK+sZIPIh,r!\rsb\n', '@=Z0'), [9])
    def test_case_2996(self):
        self.assertEqual(pattern_match('@}/\\{{k`JfOwes\\:ckQX$19WJkwUAFg+4@=KH=gh"`:4R-X(EA\\G35l_.%"b3H|lDaT|\tUH>TaH1U&T.jpIB\x0crfbWwxq{[gY-', '\\G35'), [50])
    def test_case_2997(self):
        self.assertEqual(pattern_match('FB,pVg;O"Nb{l>z>Xdr:wEef,>;?WT5Ob;(Fh:XXZLn8Hg@:"9_ +&qf', 'Xdr:wE'), [16])
    def test_case_2998(self):
        self.assertEqual(pattern_match('V\nDy>LJJ+,Z|LbX&9/yn"P>&\\lD\\]$%{%9v)rkDK5>2rh^A$\'b\x08d+\t\tJ\\3=R!Wg3.:V}FnFV.)EO]Z[B*[\x08AG5G)qT\\d', '\t\tJ'), [53])
    def test_case_2999(self):
        self.assertEqual(pattern_match('\nt^pHeX[RCX^TCZ"3a\t,l@}3+*GDBDk%5ElV6?oB$tbg\n*;\x0c7x&{SSG^[4,rH/\n2[g]Y:9_(jG9%@{%Wwz(]', '%Wwz(]'), [78])

if __name__ == "__main__":
    unittest.main()
