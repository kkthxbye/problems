from typing import List, Tuple

vowels = frozenset(['a', 'e', 'i', 'o', 'u'])


def caseless(s: str) -> str:
    return s.lower()


def vowelless(s: str) -> str:
    return ''.join('_' if c in vowels else c for c in s)


def unique_everseen_groups(wordlist: List[str], keys: List) -> Tuple[List[str]]:
    states = [(k, set(), []) for k in keys]
    for word in wordlist:
        for key, seen, firsts in states:
            tokenized = key(word)
            if tokenized not in seen:
                firsts.append(word)
                seen.add(tokenized)
    return tuple(x[2] for x in states)


def spellchecker(wordlist: List[str], queries: List[str]) -> List[str]:
    original = frozenset(wordlist)
    keys = [caseless, vowelless]
    maps = [(tokenize, {tokenize(f): f for f in firsts})
            for tokenize, firsts
            in zip(keys, unique_everseen_groups(wordlist, keys=keys))]

    return [query if query in original
            else next(filter(None, (m.get(key(query)) for key, m in maps)), '')
            for query in queries]


["kite", "KiTe", "KiTe", "Hare", "hare", "", "", "KiTe", "", "KiTe"]
print(spellchecker(
    ["KiTe", "kite", "hare", "Hare"],
    ["kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti", "keet", "keto"],
))

# input_long = ["pue","kZp","hjs","HBu","rsp","epp","wsz","AuC","gsi","yfz","ohi","huu","xbu","Xih","bfg","gap","bvu","okq","ote","jlp","nij","awz","Zys","nvf","hdr","ndo","lkg","zaq","iyy","xjk","iik","fom","evp","pEB","arx","jpd","rqc","ynt","rka","aWJ","bdq","qle","btc","ybs","kjj","dzW","tka","jnj","rok","aqm","brn","ztg","bgU","jpv","tre","two","gih","rja","cyu","ips","qks","uVw","vog","sjk","dxv","hqi","ezw","GWH","jru","ivm","fPy","iXc","ckd","swl","knm","EYs","ibv","ugn","emv","epi","zia","qsa","hvx","mNB","wcz","vcg","ozl","oar","shj","amd","ibp","ntw","qno","dfn","bel","nnm","szu","nqm","fam","zal","osd","uDc","jzn","xyq","stu","vum","ShJ","wvi","aiy","rcf","gue","lij","fmn","Mpo","hwa","khc","qnn","pni","ust","isr","dzw","aqg","etd","bhl","Rpv","Zeo","xxr","ups","cxs","ckd","nAe","fif","oRX","rnt","llv","xaf","ais","mlw","obz","wqq","LkD","oib","FjP","hoq","zhf","Foa","kwi","kji","jpr","vzv","ans","kvp","uaq","xxr","lya","msz","zhd","mdz","qve","rmb","jjm","srf","nib","non","zPH","zCl","paa","zos","rej","ubg","xeq","meq","kbC","fxa","nse","lnh","khy","qyz","shj","gtk","MdM","jdg","gEe","aza","btt","rQc","edp","egq","tvI","knb","yir","vge","hau","lws","ahn","dvf","vfe","miq","nrt","ypj","mhn","cwz","wrc","vna","sof","hyk","hmw","HIY","aia","mbx","hqu","vfd","vkr","MzZ","dNy","cnn","paa","ybj","sgb","vvl","jtr","ioi","maz","uui","LWs","kBc","cuq","plj","qos","wvk","apn","rlu","icX","cge","opt","jez","eow","VGx","mhu","bjx","UUh","fmv","eqg","fpa","ckp","bka","Vck","onQ","pvo","fkf","uQM","yoz","vus","amz","aub","zrE","jfm","zzm","hlp","lfl","qtu","lvo","tsn","ohp","stq","aWz","zii","jek","vtq","bVu","ZQI","rap","ljy","grj","vum","frp","wus","frx","tkh","qbM","qlz","nEb","gky","lsp","qug","pdd","khg","CmO","ngl","IKg","cfl","qmR","bol","ebc","yys","sys","pnq","iqr","vuz","xxo","btk","tez","pqw","dzo","kus","lan","xui","HLA","qpj","sth","FwZ","ZsS","vkc","biw","tko","KYP","tkr","oli","qvh","mev","lpq","nsa","hlk","bgh","giu","gnp","IKi","jqe","rav","bch","ztg","cov","pst","fyu","efm","zth","yqc","nsa","mro","eyq","Hty","bKo","MEh","siu","wzm","nlb","uae","lba","ioj","ovT","gYH","pts","drj","eco","cia","xko","mpo","gvx","qgb","thd","qef","fqd","gde","mqg","uqx","mbg","ocw","pyw","qol","sKV","imr","gri","QBG","dlk","ids","eba","qqi","xew","egc","uqm","rge","itv","baj","cop","jor","bcz","zkd","fav","pee","qdd","err","any","yzn","nkc","bmh","hey","lcb","jgx","mtz","ecz","aai","bwy","ckc","zeu","uum","mao","wvP","svc","nhs","jeb","upv","noi","crm","bch","nbj","geh","aia","woq","kel","amw","nhn","hxv","lxt","hyf","wSP","iyz","htw","fnz","zsx","okq","owp","cqD","eof","hjm","kOe","gej","CAz","zba","gyh","beu","isd","gql","miz","xwm","wxr","foa","ZtG","wrb","foo","faf","nsl","prf","dqi","dkI","hty","kCd","dzo","gja","rey","unb","zsw","yhf","xui","kxs","mag","zpx","fjp","kob","tnp","afu","zuv","rbq","qdr","rvp","hrt","vzv","MXN","xcl","wic","wqm","gir","wfd","JXo","zss","wnf","opv","rvk","pdd","uvh","GmQ","FUm","gyc","veu","pjj","dnb","ipp","pla","dci","ldr","eyi"]
# r_long = spellchecker(
#     ["kkk","hrt","fze","awj","dfn","kec","zss","dkp","pdx","pgm","ozl","dhj","uqm","eks","opv","cxo","okq","wym","fjp","yyo","awz","lsp","quk","hhe","sth","mpo","mbg","smj","cpm","dno","miq","fld","zxa","fdu","ige","lmt","gyh","wcu","wiv","zad","tjk","ync","voc","gqw","fzk","ehs","kgp","hde","kkp","tko","uae","uax","xhm","anh","oph","lws","amw","vyi","lec","exq","dbx","gee","cbp","pfu","uya","loi","zba","qdo","cfv","oxg","him","aoj","uob","kxs","odx","qtu","xbg","bqy","imr","dzo","ona","hat","jxd","bae","ops","len","fof","wlt","fxa","ryu","qay","asd","shj","wbi","moz","gsi","hdc","abt","yfd","ptc","dyj","dhg","qwj","zme","enn","lfc","pdn","vcx","aig","ywr","txj","ngl","mro","rqc","baf","vbr","box","wgv","ifa","ogw","ikg","aai","qeg","bgs","cmo","prf","trt","rqq","sep","uqx","xvn","uzw","fof","mzz","qug","pnq","kwd","igf","yly","ecb","bcz","osc","onq","khy","ubi","iik","cee","ora","iyt","soa","qdo","cmr","hty","jap","ghn","gwh","cqd","tre","hix","ztg","zhf","mbx","esc","hzo","tic","mpi","gvt","gmm","tnp","qgb","riv","yrw","bvu","uia","mnx","lnh","wao","pxz","haw","bix","qmr","kga","umh","lmk","noi","mjx","erj","yda","dny","zsk","qla","ndq","atn","hkb","svh","tvi","pyw","foa","zuo","ort","ous","orx","vfk","vus","fwz","nfg","vsd","opn","nqm","hru","jrt","ymi","xty","dph","etf","kiu","dpa","paa","oug","vca","ejn","hrl","auc","idt","vuz","dxr","dzc","crg","cyw","eiq","owp","qye","aiy","rmb","laf","fmu","csn","ray","ckd","rhg","dvf","guk","suw","nfv","poe","qpj","tlg","rxv","iuu","adj","sjh","ocw","ytn","ptt","kdg","anu","dsl","nhb","ywm","bok","nlb","wcf","tor","hlr","rvw","xui","hxc","knm","oyb","dgz","puu","ovo","obi","neb","zfo","ouz","mcc","fcd","xzd","mtu","dpg","zre","tba","hsz","lqv","tfv","pbp","glf","dhc","dzw","zso","cuf","jek","gqd","wyr","gip","wsp","wus","emv","kbc","ssg","gvu","eme","fwa","zeo","ljy","rkv","iiw","ljl","iwn","oqo","kcd","bhl","dyo","mho","scr","zfg","iqr","zxo","unq","omd","vck","cux","ivh","xrw","ata","jgd","mtu","zhb","ahd","zcl","zvi","fgq","htq","epe","vgi","khc","mdm","nwq","bbx","iqz","eys","irl","ihz","zhd","nsa","ele","pst","xyq","kox","qys","tlv","uwr","boi","fdt","amb","lyq","nej","xxr","ixx","ust","hwe","hla","ykp","qyf","sny","bci","yid","gii","dci","irn","mjp","wvk","zys","cxs","hua","uji","oxn","flj","uac","yoz","qcx","fsk","wvp","vtq","zsw","uvw","zqi","bgu","udg","dnb","ehz","dtu","atp","cop","unj","zse","vzv","mjx","xwr","mlv","mlv","vky","dkl","kat","ufp","hyi","vzd","zok","bel","saz","aba","jgx","uvc","yir","lid","zph","uuh","gti","lcl","oxf","yib","xpa","bwf","udc","bom","nkm","lkz","rqw","ihl","bwy","jmf","pfy","hbu","imn","eyf","nkz","gje","svc","ovt","pdd","ukl","zxb","mdr","kzp","oxi","gtv","raw","shy","cau","vgx","nrg","bfg","qzn","knc","srq","qdx","lij","ixc","ogc","noj","jxo","usr","ytl","muv","uti","pbe","dzb","rvp","fqt","hhx","mhe","cga","gtd","yat","zac","lbt","gke","tuh","obz","vuv","gmq","dki","skv","qbm","nbb","ugv","hxt","uxn","uaq","qqa","koe","fxc","sgj","hvx","nae","wtp","njm","mnb","rge"],
#     input_long,
# )
# a2 = ["paa","kzp","","hbu","","","","auc","gsi","","","hua","","","bfg","gip","bvu","okq","ata","","nej","awz","zys","","","","","","","","iik","","","","orx","","rqc","","","awj","","qla","","","","dzw","tko","","","uqm","","ztg","bgu","","tre","","","","","ops","","uvw","","","","","uzw","gwh","","","","ixc","ckd","","knm","eys","","","emv","epe","zuo","","hvx","mnb","","","ozl","","shj","omd","","","","dfn","bel","","","nqm","","","asd","udc","","xyq","","","shj","","aiy","","gee","lij","","mpo","hwe","khc","","","ust","usr","dzw","","","bhl","","zeo","xxr","ops","cxs","ckd","nae","fof","orx","","","","ous","","obz","","","uob","fjp","","zhf","foa","","","","vzv","","","uaq","xxr","","","zhd","","","rmb","","","neb","","zph","zcl","paa","","","","","miq","kbc","fxa","nsa","lnh","khy","","shj","","mdm","","gee","","","rqc","","","tvi","","yir","vgi","hua","lws","","dvf","","miq","","","","","","","","","","","uae","mbx","","","","mzz","dny","","paa","","","","","uae","moz","uae","lws","kbc","","","","wvk","opn","","","cga","","","iiw","vgx","mho","","uuh","","","","","","vck","onq","","","uqm","yoz","vus","","uob","zre","","","","","qtu","","","","","awz","zuo","jek","vtq","bvu","zqi","","ljy","","","","wus","","","qbm","","neb","","lsp","qug","pdd","","cmo","ngl","ikg","","qmr","bel","","","","pnq","iqr","vuz","","","","","dzo","","len","xui","hla","qpj","sth","fwz","zss","","","tko","","","ele","","muv","","nsa","","","gee","","","","riv","","ztg","","pst","","","","","nsa","mro","","hty","","","soa","","nlb","uae","","aoj","ovt","gyh","","","","cee","","mpo","","qgb","","","","","","uqx","mbg","ocw","pyw","","skv","imr","","","","","ubi","qqa","","ogc","uqm","rge","","","cop","","bcz","","","paa","","","","","","","","","jgx","","","aai","bwy","","zuo","","","wvp","svc","","","opv","noi","","","","","uae","","","amw","","","","","wsp","","","","","okq","owp","cqd","","","koe","","","zba","gyh","bae","asd","","moz","","","foa","ztg","","foa","fof","","prf","","dki","hty","kcd","dzo","gje","ray","","zsw","","xui","kxs","","","fjp","","tnp","ifa","","","","rvp","hrt","vzv","","","","","","","jxo","zss","","opv","","pdd","ivh","gmq","","","","","dnb","","","dci","","uya"]
# for index, (got, expected, orig) in enumerate(zip(r_long, a2, input_long)):
#     if got != expected:
#         print(f'{index}: {got=} != {expected=} (orig: {orig})')
