import unittest
from suffix_tree_matching import SuffixTree
from suffix_tree_matching import near_exact_pattern_matching as nepm

def near_exact_pattern_matching(text, pattern):
    return nepm(text, pattern)

class TestGeneratedCases(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(near_exact_pattern_matching('+OR^u 3E8Ir A81cj\x08.4@"#ZA5.kytE\nO{_\\l}w,V\x0be'H_'0\t+7V:$kv|qs\x0c[Qp@y.`\x0c\x0c|2Y\\!Fpd2<d[e3', '3(3*6 l'), [])
    def test_case_1(self):
        self.assertEqual(near_exact_pattern_matching('+#)F(}FDbH|A6Lug;`13!hM![P)Ko,L-;Lfq5HIZ4*EnH)> t'G}AC"-D*uzJ5E]6/B\t&\x0bA Sp3', 'Y?uu\tN\ttt{F TJ'), [])
    def test_case_2(self):
        self.assertEqual(near_exact_pattern_matching('gJ!? <\\y( XZw2g$){EpnC"yEc=6BJuy-$\\sW\\EiHhbbKkYmmYjto', 'cW(Z;{B]b'), [])
    def test_case_3(self):
        self.assertEqual(near_exact_pattern_matching('9C,k74|4)L3SRQ1H1!W/K'0KISrv(o)-T6^.O(y$M_-@\n!'v[S&h1~`h %>%*PZr<97/NPa9}wVQJ`>D&ib\x08Z:c9  T', 'q/e+~\x0cMQMTEj'), [])
    def test_case_4(self):
        self.assertEqual(near_exact_pattern_matching(' ;^sqVb{qTTU@&Gp]\x0c7d\n.y.F./@Yf!|lm"jT&z(.M\\^ %}(:R', '\x08\x0c-u$c5/xJ>p]\x0c'), [])
    def test_case_5(self):
        self.assertEqual(near_exact_pattern_matching('W1i3WR63hsi5\x0bG.4h?>,#Mx]sZ9'NBL|8b`;c___6v1xWsj4CpO,\x0b2w\x08v@\r(JYhJNN\\', 'M$<wbSnbzUr,<%'), [])
    def test_case_6(self):
        self.assertEqual(near_exact_pattern_matching('6-L&r0v6UVE/,d<rm EI\x08H.~3+^SuEV_?:Hx;IyR5ln\\rSM-$[{}K3raLdl\tY$$M!.OgeL.l%XXsvuO/', '~;V',H'), [])
    def test_case_7(self):
        self.assertEqual(near_exact_pattern_matching('Von.0JFMHb": :5WnOP)H6>~x,gAAzj9JaPd2NR7H{ (SU:GIlsX!,Au', 'U`dr+kbT'), [])
    def test_case_8(self):
        self.assertEqual(near_exact_pattern_matching('iLb*Ie\x08Un<#U{LxRgdc#v*jv`u_|a>aZCgQAc)jc\n@2r=MJ(IRbK\x0cr6DpraHi#MT\x0c)sIg=d\x0cE4J*YAowjFWcDe CVfx{hd', '1puo1th5}&'), [])
    def test_case_9(self):
        self.assertEqual(near_exact_pattern_matching('BEk>%uhr1VvK;4;e]_pIO"Z}pfZ]\\uk#\x0b\x0cb!AUNUe5TRr[9u8Cw!r', '.{L^@"8V02[+'), [])
    def test_case_10(self):
        self.assertEqual(near_exact_pattern_matching('&2'e:lfZz#eg\\'YG'"?^g1ZMjR\x0b\r;fl,'_\x082\x0c/ie\n>~{W8\x08VznPW`.{>\x0bX=B2a-D,Ql0u$yYc?PbVo x#Y[\x0brkxBu+"R;#B'?_@', ']'vX\\V'), [])
    def test_case_11(self):
        self.assertEqual(near_exact_pattern_matching('*,KNL\x0cA%IkjK@)v\r\x084eI^_^UcZP6\\52_\x0b}*nB!sx\x0cC0WedBM.*N)w:yM8', '}r^\x08@B0ABRjvr'), [])
    def test_case_12(self):
        self.assertEqual(near_exact_pattern_matching('!#W$KD_N2.1TB>TTdO.co&8yH\\HhG!Y1'v\\~-]_.5EUuAI\tL"Tjr&Mghp*^_pm0\x0c(\n=\x0bv z\x08\\ -u,5/i&[$\x0cr', 'B1]l#10qU-xf'), [])
    def test_case_13(self):
        self.assertEqual(near_exact_pattern_matching('\tOLj3j2X#Eu B$ 9Z~`QR@{R~T@e_a6WQQhF7[tm>v/=klI@Im$(td:weJOo\x0cZ"3T0sFP\nGi5`"T>i9p', ' x<XLD]HkI'), [])
    def test_case_14(self):
        self.assertEqual(near_exact_pattern_matching('^*))gmd#KFR\t*cx=\rlX\x0b!M^*a\rSVb6_+udx1# !VT.\\\x08j>nk.B#l_4We3nwX72P~J', 'oo@+>:eoc;qxr{?'), [])
    def test_case_15(self):
        self.assertEqual(near_exact_pattern_matching('I-U&>Pg\x0b(tK1:0I\t}*%pZnfe71h\\AQ!6UP,%n\x08?qeYJ_f}!k>uYb=9=_(c[6<bo\n!zgWO\rdi,pE\x0c\rSQE0bsh+j}1', 'P82[VkE'), [])
    def test_case_16(self):
        self.assertEqual(near_exact_pattern_matching('cY`Ue\x0b%+\x08s9/]U\x08;U;~;=#kfqs/3`X2H2|^m\rWU&G<Jq^qh"2SCEQrpk%Rx<J2-Uggag\t];2Zb=/g:d\nPk\\Q_,Oa1/n:<TsR@o`', 'eZ\n:$'), [])
    def test_case_17(self):
        self.assertEqual(near_exact_pattern_matching(''^Xe8$KOq7vo\tcS7x~ZO'N2\r+>{_23Gjt|Pbm-n<sBJD8LR0YpWA]oj7kv\t3Rv#C-|bVhFce3F,J\nkIvw8z3W', ']N]9YQ;\t@D'), [])
    def test_case_18(self):
        self.assertEqual(near_exact_pattern_matching('%(r>(5P$i[w4{(>k;(aUMG_\\3A0;J\x0bz\r8hhZ{wzuiM"Zt)%lhue9n;$#TD', '\x0b]k2 SrM<<oU|yu'), [])
    def test_case_19(self):
        self.assertEqual(near_exact_pattern_matching('\\i1\x0b kqK>:0\\6@d2\x08^\tSka%nQ(qi~R\tmS<T\x0bC7Gf+(lF3r\x08Z"nbX?H+\x0c\\pxY|Z<8BA.aGRO~;p,.E\\e)[`@`;\x0b\x0bW', '\x0cmZ.%A'), [])
    def test_case_20(self):
        self.assertEqual(near_exact_pattern_matching('_D}\rRT@B@Db3]0J6!m<,=6KolN"O\n\\02:#WY\x0b}C|veO_^&5KC~', '>DN%#'), [])
    def test_case_21(self):
        self.assertEqual(near_exact_pattern_matching('L0U1gnr,7H\nDO`Nve3q1Wo]i#\njQ2]+SM>PbMM/ 9\\F[j|kPtd*R] 3Z\tGf_\nE\nCss!tj:h&Pw3G4Bi\x0bP\n,z?^9', 'oR1K<*Y{'), [])
    def test_case_22(self):
        self.assertEqual(near_exact_pattern_matching('[X"skLNSD3\x08a (20D),Y[^Anc_=Vn*0U"~!QG7o+Vn{@UywgatvvHX_lAp7iq$Ri%', ' P6p:|o'), [])
    def test_case_23(self):
        self.assertEqual(near_exact_pattern_matching('Wlr]V(rmSGI~,t9uR[0\n/\n8Q(`${mL:ZPY=$kdc,I(aY\\3_6z!3\noG; `?Ki`<I-T?e|w5F :47Gwi:h_b \nbij[#_rbX`J', '$W0.6.n^$4e|6*'), [])
    def test_case_24(self):
        self.assertEqual(near_exact_pattern_matching('i\x0bG\x084\r)\tqrz4;2<rYRF\\2RS^EzPvP,9*~\r\rbix97{MgrvLH1PN q', '\tNEpD8'), [])
    def test_case_25(self):
        self.assertEqual(near_exact_pattern_matching('&/:1<J<w!fLtC>|#Au"L=[W`@S<iXVxi]*+yi}>b}\x0b-VhbyKx86G:if37_f]kv +7/1%b//]GN-SF5!5^&@{F4O', 'i)xO=g'), [])
    def test_case_26(self):
        self.assertEqual(near_exact_pattern_matching('Tm]0V88$Sh&cTP;&B82\x0c*5b&,;lsbH^,C\\0XdwXDM<[Z_u(v0`y_d8[K>i^!#S=C'-ej\x0bnY%/F5&\x0bUNCmfyk*P6t)qeA\nv&', 'pr~N1b5v.O+8-'), [])
    def test_case_27(self):
        self.assertEqual(near_exact_pattern_matching('%#eFEeW{\\|m>~USw,rqP9c<`_G[\t"\x08\\Q\t'=b!E3vk7Rf\x08+E&(I?=4eP$]g=vBpl6V5XAB->sPr?7^NfE$P${T@', 'N@]^{*H*zK'), [])
    def test_case_28(self):
        self.assertEqual(near_exact_pattern_matching('UJ_5{ovmH:.>AXu/G'`\\\x08t;.SjLBIl!\r\togb6-UDBBG\x0c%V`@KR()A^', '7b&2Z6{r1.C\x0co%Q'), [])
    def test_case_29(self):
        self.assertEqual(near_exact_pattern_matching('/)v2)W\r=\nC0c\t\tTuHZ}wlR`!lh3^k\\79!\n_cgF\\W0v[v#sP)5=i;J}{s\\"f$o,Bs$!_HOvDn;\raoje', '\\,m>)SW!;'), [])
    def test_case_30(self):
        self.assertEqual(near_exact_pattern_matching('!I2|;u`"A8fqWr-hJR<Fz\nG["Z+[\tiZ]u-{\re\\Jd>;VU&^nwhea[z\nZ8b.ORXTW7U^', 'qBxh0E.'), [])
    def test_case_31(self):
        self.assertEqual(near_exact_pattern_matching('EvqgpnLTR%BS-ccNEXwF\x0c*_Q9%4t8y8GMv.x\x0cjdR\x08b\\mwqo1Om}szA;8M_d"z`^>#'dZi|o3`)M"\t^u*7`8+\r^\\,,GlsE7I?o;(P', 'Nmmg.'), [])
    def test_case_32(self):
        self.assertEqual(near_exact_pattern_matching('l4#%vXq^?e\x0cZmIvE>& #rD4*tN|h0QA=;:\x0bYf\n\x0cQ:^+p~#X&.Q/\nb"k| lZ0a9|;&K/\nZiV(m', 'hiUk\x0b{]z-'), [])
    def test_case_33(self):
        self.assertEqual(near_exact_pattern_matching('c$5ljcph7v\r\t/x?7G\nq46c\\LF\n?Mt\rvY&.w?A~A8aXqiFXx\rH2\tU]wNfNs%OAwTMA&SEf7', '"\\AY[Ii~%'), [])
    def test_case_34(self):
        self.assertEqual(near_exact_pattern_matching('sd\nyP3"Qo5Q#-e=b53y>gZa\nAB\x0bdY52 \x08kF~lql\rS?ZrRxsTpve*/l/p\x0c4us3`=l\x08OWI#+h]\\U(m-0WEN12}\x0b_pu#0v /',}', '?:8A7\x0b'V4'), [])
    def test_case_35(self):
        self.assertEqual(near_exact_pattern_matching('I193tI}9sVbbg_8*sQ=M&ZsBWuG%Rv[L37lsYgI Y7@\x08b9SEu :y aF~"Xa_~Y8\x08d}dx8vY(;nk~~je(?73)|xC6bqyIK', '8\\AT;'), [])
    def test_case_36(self):
        self.assertEqual(near_exact_pattern_matching('LM$FNF4g4YJOm[L:i}ZLFdb^Bir2_Ge_+w\\@^q6"wp%qu7on|vg }u', '9#usA}dRb8'), [])
    def test_case_37(self):
        self.assertEqual(near_exact_pattern_matching('Mku+LGM7uwx3h\\DVfG6#a2r!.!({\r\nCyssWbaTLDe4kIUbN7z`r8UmT#/8F$', 'fOfgum0E=IO= '), [])
    def test_case_38(self):
        self.assertEqual(near_exact_pattern_matching('/tqQtTZM'oYK1ei=fVXFlO\x08\\pN_vbW;k6}I;3z\x0bM\tcPY!d<~>>WID\x0b-\nSO[*2*EQ1514\x08VV}x^;79Ov]\r', 'WYx!c'), [])
    def test_case_39(self):
        self.assertEqual(near_exact_pattern_matching('q-Sg\x0cRbe=kTimh %wDtS.4$YQKs"ZI\t<U~lvMx\x0cqCz$IjhfQx'Q\\to_L1yukzKz\t?h$MeTdSMi5]=tx\x08;4!4}ufj_[vM', '|xdl#>@/h'), [])
    def test_case_40(self):
        self.assertEqual(near_exact_pattern_matching('vAf7c>!]??EJGM>\x0cH/ZEEc0u[j$f!8@&,e03Td1@8E`If6W*J`Hysc*\x0b\t~h', '#$V\x08`a.jc]F\r'), [])
    def test_case_41(self):
        self.assertEqual(near_exact_pattern_matching('vM^E |X{sLkM8v;f]\roH/5x{/|`Z|}/n^P&vT:~\n:Q'n_Gbg,YdZjMk^1ACpSVAt%\n?', '^q._t8\x0b7){&pn]('), [])
    def test_case_42(self):
        self.assertEqual(near_exact_pattern_matching('"0\t5\rQ\r$a\r724}4-Qy558/gKoEx3-<.|vL1Re]B\\R/T^FEzFFd'zsj|"I$C#wP\x0b8(;l`:u9fgYC\rF\r)NdD', '-aetVV\x0bNK&k\x08'), [])
    def test_case_43(self):
        self.assertEqual(near_exact_pattern_matching('L\t(^@_`z1;I80^%4^\x08]5Bh+bt%~5Fj\x0b]1r)XwUT-weQ"p~wS\x0c\x0b>*<i+B', 'Hy%3MY2\rjK'), [])
    def test_case_44(self):
        self.assertEqual(near_exact_pattern_matching('K-/RR\t{:3 ~WYH%.X2[ oqC(C+"+s7>bS^rY}fJ;H:Jdn,[\n|M', ''55x>DXhye'), [])
    def test_case_45(self):
        self.assertEqual(near_exact_pattern_matching('k!Bq).\\["{J\nrK~nnh$XaE"4E3*nk,0`?i9;D4pkff]\x0bC&sW1MhTfFZMfi"f3/T!<g!X/?>xtgo\t*08+83}&U7Bv9!=o~\x0bYT', ' LEuTt\n\tf2m'), [])
    def test_case_46(self):
        self.assertEqual(near_exact_pattern_matching('L'>Lo8jy9H8(!^_Z{.'=\\JcQ{-0t&Wh$j/5e\x0bQqW\t59k/vz7#[KLF[+g'v){a.%\t(9uXUK'XW5D\x0b6\r6uq1hZ> bmMSm4ETp7\n`s<', '_50&\n-gH#n`h5W;'), [])
    def test_case_47(self):
        self.assertEqual(near_exact_pattern_matching('=]}1txS4VC|"U)dHQ^qOjZZuNC.FLAR/o]"`b.?Z#R0a\\u*\\Ocz@K7Ck(3`z<0f:\x08lI\x082{NIRt;jtKpGB"\\[n', 'Um_"Py^XY#|Xvy'), [])
    def test_case_48(self):
        self.assertEqual(near_exact_pattern_matching('El{lEA\nbJ}i.n\x0bmD>7ADtxjWm??RO32xEw&0"N>H~z\x0cd) ~rjlI\r41\x0bFI@q0T?[Bw[*NI;,0]${vBu0MF-]+9L:`+', 'xE;<dE\r&DosEZ'), [])
    def test_case_49(self):
        self.assertEqual(near_exact_pattern_matching('IyRcV}M&)?6MUY\\N* FL)FHkfySC?/@,xw(zWZB.oT|/O %"961"qSp}j3(r-j<Mzc\x0bC3^\\s>`0hkLVjt3``_0', '?^f[@>|P|^\x0c\n?y'), [])
    def test_case_50(self):
        self.assertEqual(near_exact_pattern_matching('cic\nJjC\\r:n0%\x0b1c3<Tu 18;CSi<k+"R^bcQ QvsXn{50=[Chzmp\r@nF2V;', '\x08Tnf g\n2xN'), [])
    def test_case_51(self):
        self.assertEqual(near_exact_pattern_matching('pj\x0b1;z?IY#p'x'_Z o\t\rrPP~uXp3J+8n~9VJ!R0>G!f0-hI{m\x08/z,\x0b?$FD"B_HWT\rB6P]8uiBSgMkiG\r}8^r}jL|'?]D$,`S', 'J%y=&-}O=W|>P'), [])
    def test_case_52(self):
        self.assertEqual(near_exact_pattern_matching(';I,>\x0cjB8*1OCC\tnxtiq@wkr\r?zHEaZ\x0bOl6EdH;uPNYyeg4uFp3ATiiIf4!Y!Ok F`1-6,ERB"\x0cw8Li', 'cO,"<pcO3Lyb'), [])
    def test_case_53(self):
        self.assertEqual(near_exact_pattern_matching('Y9|\n',n=A g0?r.PF>\nZ1hIo{ R17f\x0c`K5(\x0cC{2,&&h?:'e81vio~5,{P@ZH+UsG{( =H->^1{?fU>2pbsUk.\x08/gs+J3D\\', '$ *';\x0b'), [])
    def test_case_54(self):
        self.assertEqual(near_exact_pattern_matching('jI=gUH<i/ow\r"\\JO:M:MzUdti*hMQiM/,"UCO,`++^!"EbR1Aw,r>[j\t$WM^F=E\x0b\rrV[[~wC`L', '%ui\n$DAl'), [])
    def test_case_55(self):
        self.assertEqual(near_exact_pattern_matching('\x08T[H!2w8L)I\r:3[<l+$*:$hQ^6z39\n_+j[\x0bwA!Fxq_wNQ_:mr~8ZyW)s9.\n?$\x0c^(5Q\x08Q*1Lw-$wR L', '\x0cs!B0'), [])
    def test_case_56(self):
        self.assertEqual(near_exact_pattern_matching('g\x0c=n<px$oI*$P,3|**RY:Fy+5 0F{X0kye.r@`U?vWhjR=e}(TZc!L2C$='LCT$KI}i[O\x0c', 'g(5IP'), [])
    def test_case_57(self):
        self.assertEqual(near_exact_pattern_matching('+\t\x08Rl}n.\r, 27UWW|`i'M?+jA_oUk1jWMvI"\nRo.!Jq<ciAV03Vwcl\\6VOnwW\t5s%GCCJ`)>*RCRt|woddU2#J\\!"\x0cRM\n\ts\x08', 'm3ns/EO'), [])
    def test_case_58(self):
        self.assertEqual(near_exact_pattern_matching('G*t$h7!\rmFI[2mU|7,_Suu\x0b+;(jv-MBM;~f#hsF?m~Bpw\rAaEGw&%j*gY?ugdowBI!B\x0cSNf8L\tn\t/s6', 'H>b||t2!:Qq[LQQ'), [])
    def test_case_59(self):
        self.assertEqual(near_exact_pattern_matching('d6g\x0cMw",CbhshcNClT*o[47bIs[vP2K>Z&AB";\x0cyuf\x0cX~X}*b0$()@\\ JvJiG<43x4\rA!0oKQt9.yo0F~3h\x0bO~_4f\t\x08\x0b)', 'I}6jo1lStf qH'), [])
    def test_case_60(self):
        self.assertEqual(near_exact_pattern_matching('G6\x0b>+4<QgTL`f\x08cJ@\x0bg[>UnZv\r'i'(\n5:S*9bw``_,$_2O-56A+7%,T;)AcIla,Q=\x0c1"', '"Z@~x2'), [])
    def test_case_61(self):
        self.assertEqual(near_exact_pattern_matching('jw/5%2lVEc7Up9'wgo<i5:@\x08Ie DOCC\n4#/mP\r5L\t,B,i/Z{b\x08]?e\r!LPtV8e6ws5o.Ty"qM|.\n\x0c.8B:\x0cj9', '\rD\nRU'), [])
    def test_case_62(self):
        self.assertEqual(near_exact_pattern_matching(' S8x?E(CY0m/t?\n)b`},\x0b@[a7d@[jjA^l4&qEoZFh&\n5GTkT(|'>t!q@`IUx|eN,GxN8-s*4@\t', '3g2|m^&]F`_\t%'), [])
    def test_case_63(self):
        self.assertEqual(near_exact_pattern_matching('ZS6D% _Zu;AZrk`4]^>_Y'kkZ'Q,_vM\t&'dgbcl04nX\tb?),)zWqP]p'Md;5 Xtp491,]KuHs2>R#jxS?Po&|q tOf3D\n616\x0c?', '/0uQ+VxxO'), [])
    def test_case_64(self):
        self.assertEqual(near_exact_pattern_matching('t;dEF }NxWc0S8je+XMtm_.Ws_DW-t;a^7bpa?p3w<\\\rm]!TKN>\x0c+\tk}&\x0b8/lS^fk)Zn\x0b^J@c`+}$U6Xk\x0c\\Zg; ', 'vdggI\x0c'), [])
    def test_case_65(self):
        self.assertEqual(near_exact_pattern_matching('=,[b;'~V&GrYtQHN\tSxa[cTXi7IO\tQz/VppmMA~ql@S+@nfa7-(~W', ')ix)Akzm['), [])
    def test_case_66(self):
        self.assertEqual(near_exact_pattern_matching('<4(]{_$\\j\r\x08A:7DqTdTb8N\n,&#=9(Ca8g*m:\r'.jm"`7zuD9si\\8~k=v7}<k)[*}^hMeY\r!J|mL+3i\x08I\r', 'Fz<F=EL7Dg\r\\v'), [])
    def test_case_67(self):
        self.assertEqual(near_exact_pattern_matching('?C`0hmr'7"x/_H~FJpU}&Rgp[djm>Ks,pxUi_tzR\x08!|1&[Z^B|{b[w@\\0^kGZo$', 'i{Sz\x0b'), [])
    def test_case_68(self):
        self.assertEqual(near_exact_pattern_matching('VXr9O@%}`{e9`v@7s5/\x087 M<JOL3Jr`04syZ;zk\ryS%x9~b\rWLA9', ':+nYK\x0b5V'), [])
    def test_case_69(self):
        self.assertEqual(near_exact_pattern_matching('}9vI#)8*;5|]Iy:~PsU2d4+w\\'qkbF0Chh\n/YASXKe<'\tStPL*e^\x083J2)', 'S"!tGb\r`'), [])
    def test_case_70(self):
        self.assertEqual(near_exact_pattern_matching('%|3\x0cjdP1i0T\\^{Mxq\x08O{4r$TlsJID\t#'%y1ow0bKsA[36L3&8(', ' ,BH'N\t Jj'5kp'), [])
    def test_case_71(self):
        self.assertEqual(near_exact_pattern_matching('wPQ&cC\n;'Og<D6GuQY5L|BI<0,z#DkL\x0c3+eIQ"&\\Tl\x0b=EHF}bs=|/dB\\<\r,5+8PbDD', '/Q5DrQ#\tC['), [])
    def test_case_72(self):
        self.assertEqual(near_exact_pattern_matching(';_Rw7dMJwOi?aC\n#H NC1 ,\tGzYmh<16\tFFy}\nU]G g~\x0cW\x08(;ub\x0bYq*,1v6{\x0cx~\r=N[y.\\@s}nxUGwJu2N8Tf|pP0$-[2\x08I', 'I#i9#s'), [])
    def test_case_73(self):
        self.assertEqual(near_exact_pattern_matching('\tDJCY"BFJ_xfHaa9L=-\ncvPwa@\n&Won&\\:fV@q@qe\nQZe>5Si1e+hP?!(n\x088,Y\x0bR\n_yn>(."vG8R%1B|r-=:HB.<A\\}<J\x0c?6Hm1', 'ASgsA&eP!\nw5:l'), [])
    def test_case_74(self):
        self.assertEqual(near_exact_pattern_matching('\x08\tD<Mo?*Nh+\n!S,F/!b^SG\x0baHJji?5U~K'%)Q#SC~d]r\tCZ!X@?hc~wp_\rqvHUB_p4V+v^EU8\x0c./\x0b', 'EcJ)Nl'), [])
    def test_case_75(self):
        self.assertEqual(near_exact_pattern_matching('WSvar\x0c'w\x08*$|pe 9DM0>bvt(@0x`\x0b!cj_\n\x08 gTP|VR6~bo9`\rflh4p{Wr=$`-)BaW){S'$cwQk<~K"Z5KxV$Y[0Mu(F|t', 'lkGWJS'), [])
    def test_case_76(self):
        self.assertEqual(near_exact_pattern_matching('\x0bikAel_=fGd|o\x0c|M~~{l\rP\x0cJ'|nxy3P"Z-*^!3TEH[t+qYfswBV|j{%1c azHVc$2^H7'H(u$;N2n6zU{^J 3`]4\x0c', 'z48WS\r\x08:'), [])
    def test_case_77(self):
        self.assertEqual(near_exact_pattern_matching('/YC\x0bm^pJtoocg(NBnUy/.A\n2rbCbgxq]S2WT0s@O&rX?Uw[)|\\@|ks^6#', 'XuSp|R7`P*8c]3'), [])
    def test_case_78(self):
        self.assertEqual(near_exact_pattern_matching('\n;\x0cG'`93e5l =_]17[D>"\\,Fj%iQ^,57n_Zb'$QuOf(pIax\x0cl:', 'lcZC<\x08'), [])
    def test_case_79(self):
        self.assertEqual(near_exact_pattern_matching('Kdi_rWAtn:\x08K\x0b`]/}J\rDsm\t(?=C\x0c} y|v[?//KY*saflP>S*\r*upO', 'v,/\x0bV\x0b'), [])
    def test_case_80(self):
        self.assertEqual(near_exact_pattern_matching('vKM+4&b(]V5^icrClH\x08fV\\3x4K=sabA*agL1aT:='.\nQ/3('p$&Q', '!m/Tr'), [])
    def test_case_81(self):
        self.assertEqual(near_exact_pattern_matching('=9c`6X<}!\tC{pty_Kd\nef\t!eS=dTZ<kn$\x0bLI;{P\ty'Tf2\r$d-z5'\twLejFe}Pvt+sg>5:*udN', 'kT1v\x0b 5pV\n'g&S'), [])
    def test_case_82(self):
        self.assertEqual(near_exact_pattern_matching('\rc/0"u>X9.\x0c(01{_o0z;'nI\r^]swL^|)V]9_Hr`hR&EtPmX,Kq\x0cd$r`', 'Z/\x0cEQln'), [])
    def test_case_83(self):
        self.assertEqual(near_exact_pattern_matching('\x0bK,cR|=iZ4^uU qakM=5lj0>\r+^n`FHz6~5v9$YJQf|6l\\cj[&u<SU`qxFoY!Ay.&LP"0;T3}J:w', '[_1(L\x0c'm9+\r'), [])
    def test_case_84(self):
        self.assertEqual(near_exact_pattern_matching('7d| !Hg`$[b1\x08a(dMoU0y2SK[]vZ]>4Z#kKAF]E\nU$[4+[:/T@:pDr<{UD,'R-a\n,:0Jolzr)]+ja^}6Or`#l7X<H\x0c~3', '+Mb\x0b^R'), [])
    def test_case_85(self):
        self.assertEqual(near_exact_pattern_matching(':wKsT{(_oVxhI{F,#C:]*"R[-xgg8">GFn+~z2-\x0c#mw\n!K*Ii$Q>(bCC|', '>[\r5-i2\x08o9'), [])
    def test_case_86(self):
        self.assertEqual(near_exact_pattern_matching('b28)^\x0bHa>LYU@\x0b}(*%z[v.>Xijf6.&+lxkg;;~+\t.U(-{y6AVGas8=Bb<n7,2S\nn2!{f\t*;sTx\x08!y', '4L{2b!25'C4MZ('), [])
    def test_case_87(self):
        self.assertEqual(near_exact_pattern_matching('6:\\hhG!B\x08u.WF~\x0bS`{Qg3&D@0'r\x08mic~\x0b, z4sw>FKTebc:w1iRuYkU,{q3.qx!e!O-`wx}N', '\n,?4W<YvZ>.W(Mv'), [])
    def test_case_88(self):
        self.assertEqual(near_exact_pattern_matching('qJ7e#fY]O*r.TX(T\x0c:tM:/Y\x0co\rbV@:#kdMA9'+x2*4u]d6kMMm@!>f.s;eB~${\tlZHI/2-H#[wi]iq\x0b\\N1wTg\r+s+J', '*U~JJ;4P&mU'), [])
    def test_case_89(self):
        self.assertEqual(near_exact_pattern_matching('\tb7$7Qt+(.J\\"4B\x0c7fNIn,\\pN5Mc{53{o@htOB1\x0b\tl?ut&8"@,~=3d\rA0+gqr', 'hGqg0cq:'), [])
    def test_case_90(self):
        self.assertEqual(near_exact_pattern_matching('nm)[>`T)iI/J~iV@&\rzYA>oEhW,zG]w;X:s9?z%M,F+ ofSvn0\rU)y-u/{whbV@L9ykkl^Zol', '2|])i@('), [])
    def test_case_91(self):
        self.assertEqual(near_exact_pattern_matching('q|Y \x08ynk/F&\t;f[$hLb0?ZE;?7Ew}k>1!r@4p1M?`$'8oV4{\\077?QnN:la', 'u\\yrL!`=E'), [])
    def test_case_92(self):
        self.assertEqual(near_exact_pattern_matching('=f~,tsD+v`[KFk}'n^:?@P?|k-gdG9n58b^=T\\5~4`E[D2\tQb)%{u&nc]i~L#|8a>fz', 'ruV\tR&|1;osO7;{'), [])
    def test_case_93(self):
        self.assertEqual(near_exact_pattern_matching('1h~\\O\re48Y\t2D>v%>JwB8`a[#ZI\\_OU]jO#R2Cb<x'&+PmZ-7i=p\x08\nS)*O0O3x7wK@V)\x0ck!| \n*;U:fy86rE5"@=C;x\\KAR9\\CJ', '#X\x0b+'7X:ztTOa0.'), [])
    def test_case_94(self):
        self.assertEqual(near_exact_pattern_matching(')%;,t]j)J/\\UU+YEu\x08<cLC2G})"zcB^vf_OVnY0U#t>IU6uSW;9r}7j<\x0cYH9\x08PuwGm@ojk=\n]d[\x08\x08gkD@}dz{LF', 'q1-\x08^'), [])
    def test_case_95(self):
        self.assertEqual(near_exact_pattern_matching('+\x08\\]|{fG/5Kwq|\x0b~Yf4~*O-j`\t|!zXwjNAHk~\tnRp&i\x083\x08s\x08KU @`WW:=2p}\x0bR#', 'Io/ = @blG:\nN'), [])
    def test_case_96(self):
        self.assertEqual(near_exact_pattern_matching('ly\x0bKO;;dA@\rgwMW>_qi_u7_2oD@M'.jA4ZWcRm0r.7ZRML\tK>ttO0AH;5_z}z1a*N`(Sa', 'YmjBX#vv'), [])
    def test_case_97(self):
        self.assertEqual(near_exact_pattern_matching('6Aqv|8yQ!0+ah ,E\x08!5n,>&l/h\x0cE0y,S9NK@ix\x0cj@0Z9cA|!u#>Rj=`,v47rc/BO%vY3f}5nKj-wB`qb=Y_U}o\x08,h=Y', 'h0Y\n$#.A}#X\\Kc'), [])
    def test_case_98(self):
        self.assertEqual(near_exact_pattern_matching('jcOUA?~uY\x0b=9f&;@I4<OqM weX8.E@-GXb)DXT"WC^@u/68GS(.o]+3U\\THV*', '"mR!9H?+7F'), [])
    def test_case_99(self):
        self.assertEqual(near_exact_pattern_matching('\rN,/b<}5j!r.H`O!lO!\\\x0c^\x0cSh:CqiQ;\nXpVW~ _2\rTKm2"+/*s\x0b7', '8|Ku"'), [])