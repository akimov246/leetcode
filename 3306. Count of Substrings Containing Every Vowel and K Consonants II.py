class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = 'aeiou'
        result = 0
        vowels_counter = {}
        consonants = 0
        for char in word:
            if char in vowels:
                vowels_counter[char] = vowels_counter.get(char, 0) + 1
            else:
                consonants += 1
        min_length = k + 5
        start = 0

        iteration = 0
        while len(word) - start >= min_length:
            v_counter = vowels_counter.copy()
            c_counter = consonants
            if c_counter == k:
                for vowel in vowels:
                    if not v_counter.get(vowel, 0):
                        break
                else:
                    result += 1

            for i in range(len(word) - 1, start - 1, -1):
                if c_counter < k:
                    break
                if len(word[iteration:i]) < min_length:
                    break
                if word[i] in vowels:
                    v_counter[word[i]] -= 1
                else:
                    c_counter -= 1
                if c_counter == k:
                    for vowel in vowels:
                        if not v_counter.get(vowel, 0):
                            break
                    else:
                        result += 1
            start += 1
            if word[iteration] in vowels:
                vowels_counter[word[iteration]] -= 1
            else:
                consonants -= 1
            iteration += 1

        return result



print(Solution().countOfSubstrings(word = "cskqpadcslipdmmeickecbjchhbkrchpplbrrkpnaouimgrgonacgiojjqjnebbjbkubdqudjeddskpeidnpfngfofseapuinhklesnpikkshhadgjgcdikeubplqaucaunmfhlkqambjchlrpflldgkggqcqhakmhobkoaprrlnfabgnhnmrhrbpckneerlomjllbhjqkbmpapnmdfauaklhkboafsjknfigoinuapajbqgeemepfjogmpudnlrscjpmhsmcfqbrlqmekmgmfarnkgiqdbirmdokhjuhhmdpoqcfqmklrehpcrefulqnjhnlagddjlpdreaspmqjbhgkiuubafunbqbhmpskfspmiddndefqgsemcjuuqlrghiogrkdpeiejjfeqoumiabqgnmffgqbhrdpnbbfrbunqcmndilammceojppijfprqmbfouicofokksrbfumjjfihninfurfhjloeeijdcqqcpupbmoapddimpdceaneanbpurjsehfjkjqucospcsjlliqcglpjjrmaluqisdmukafjeokimiehmsgrqrqlsgkkgpjgsupfmoddsikajpqpehhmlqnknnsdbdmhkrdmidjecgphuucanlhfqogbqgshlaoqaaofdnoejelrahehujiuluosbfrqmggdlqipjgbrqqhfbaaianljsbmmfbnqbsjfldrscfqilplhjfsbqeiijiudkuejejhiiblqumlelehhfullhsnicpdmgeojjljopmefjicngunpulfnflkkpsmoubdjonqijhbsjqncsebapurkbpenurgcgcolpkipbijbjhnkkgqspbbkreoboampnpqjdjejjjjrsuefjihrdcloquflgegrsariurrkqidjjsdmgmmefjjdiluahqkkqjcihirusefnudumlpklsmjobqnukpgohfnuakdhshqqbecimiqgnpcrkgkcknikjkkpjeagredphcjlasgleqbogfdrupfiicaknhfdfpardcdimghkeldnimqhgncpjggqpmcfrlpaleircsrojcnekqupsmnagebqsljuoshdapjegqqdllgqqnirfhdlprnfkauukqjmlohbmhsgflahllsfflpneuiookeeqnahurfhmehcprfddcceqmnoupffkrcgagrbusloqqredaeiqcrpdugafjudalgljqjsqgipnqignmqiidjiikfeojjhlknsjoiimijhkphemhkikidlceejaekksqfmrqoikdrqbklkhkoifuomrbuhpkiqepodbbsjagrgbmdmrcfkoucaocoiscicjmugledqipffdoscjbsqoofioqbkepelgeorngnrkpcsrajnrjdnpcuigrafbsfacmdhokfsbgcsmfoqmaokqhiofojojpduskfohdhejmmnfapbcdqjfipehdkqdmssrqppdedcpnubkckosfhefgdfhbdrnicrkpbnoknqrjpjdjankhlucjimfdumankbunkfeaembisqmucnokimbhliauhcnmignmjedgldddboklrbadumdekrmeknqnkhkrejrmsujofgjdjjsicideclurkbjmlabkihfhughgscorpollkmkodksrpbafmolhpjhoboicojqrsihqsmssibqedgdgffcnibuaerrqhjgfbliefadmkljppojpcohfbkkqgglodajauinglhaiqurjghnfqcukksjchkqjroorposglgofpgdilbfbmjogeafrmknjdgmimdsaibaiqqpschipcookpsffkejecbokhjojnkehcbdkpkgjshnokqouqegrmscejafsocckoijqrselndpcicooaeramsldnqeseniccgbuosmujmcqspchdlsajlirgfjcffdbireosrmaojlccnggffbouiqnulhodqssclseapidmnmukaomucfqrfpjcmefdjsbcdsmflqjkpcljdbqaerrrrasgdukflrclkkjenmukjeeggrbjjujojfqqablbrrlmgllncgjlceluhbahemqquuekbcplunhorbbkilshgpfrffnndilhgalsqdpdejkpijhlsbghjbkafmkoclkrparjfubmcbhmfpbhealbnlajorfrlshjaiiqdfsmgpfskqcrdffkpocfqrahbchfbgjeslkuidfcseqrcrmninsempqslaqapppmakducuoraenjuoghlhopcmfocnjlebrgqkdhsmqnjrooomnilhpgjgmhiiujsrkajksifjkqdrklkqlqfjnjjidiknolgecqhomjdkqaoenhajneurmdjcslmpofeaaljgmpacjqgfukocckmrucbhgamibdarmqrpdqoqcmlbudbafglrrsuogsrhkmuekrjsqncicidncgslbhsouoprpeeuflkipisispmhhfqqmsabeickirihronsiikdjjhnqqmmrhpooerdekarjcnjbumeimopndcskqibkrmoophhidlepsdkmgaafcmdsafsqjrlmcnfoaccgdsmasnuhokifqrnoidrjorarblbsgsjmpiqkdglprdiisahphqfckkqdilqhsurbksciadqorplufooujqlogknrhaplmbicrmmmssesinrmjakspjridigfiansldggagcdildnlnneueqjqdhrjsfujclbckqdeeloasqsgadiuoihmagsuodnghdleqgrrhkqnsjcgsukggqnelcnhoeqaiagclreckadumrgbpddronllrinosaaikmhkjpquemirckfpakolnbqhehhooamfkonppaooaffcesqqpejdrgaffedarsgufimukqhfbpsafqjdgrkidarfgbccpanuplsjpekkjgnrhkirmjlapmcnbjajralrurmglbdqcdlujklpkpmslluqcjguqojrpnohfhnnlmkqhdlrfcbhlorqrecdnmfpfgrplnsngugcqadskujnefgjaeajcpeelakgjelllieekekahngadqidjgcrkkkdsdpdujhpdhoimndloikdlioekukqksnnpelbhbfohurprgdkfmjlrfefdasrkpudsgghpnjqohdgdioufolppqubbajfpperpmsmhnbqneqjbgifgfocogpcchsreilhoklnmhhhkkrfqsdnrikmseorjpudoiuciqbmqsonijsbulunqasoikfboobejrnkhirrdoepenqdhnidgpmsbscuonnmmohoanmamngajdofkdcuocggluglhgmgmhonjbairhqgcijgrffkpcmuegkejujhjhirpfhebebilbjhngglsbgmbgabroofmqhkmkbnikqqcgqrmiluupkiuicaamumpfudlrggrfhcfbelkgqbcbrsbmjukoeljuggeieagkasboskkifrlgjrufrkqjlgpisnjrabinenpjqgqobbfiedoonehmlrihhsemjrcpnleoquaahkhiljfbuesncnslqkcdlmshmojgfrqpoedaeudiukhefclpibsslqhcclrodmrpjabadjbqiciohcselhsuhbjesmephgidhchplgmunibdeishjljddphopllhfsiobqfqimgpbfjcelifcfkfhemainpoaifhaagqabicssubsgknhquosojjajjuohcdonpsilrsghuirjgrcsgbkicqqcdffoeugqqiubrpuahofkneopbqdrsegibkqejlhprsdcagcqsppcqrjkaqdmhsoicqcdfplbgqgiqsjejnlangidhguacegiqiebjrdclphdjnjrdsoicgionlpbdpicfembulqqmnnqjldpfskgqaeblsrajfmlrrcdrrsfimeugepmmqunkeriehijbbopkfhfoneibpjufhdjdsdeighuqqscbjumparniqjdgjjjqsnsorbacniggplmnakhbudmncounlgbsuuegoonjgpcademomhmbkjpaeumbqnlrngffckbkpoccjlumbpnelrfrfomgmmkcraascpgmpbijqpnudcnqjmgnrdmqbnfeaudlklsmghlskbaqpdgjrbjgohqdkgqsqcuusuhokjcddufqunanlagdkuuagegncaflbnuaqnbjnfbugmfsihsndbhqhhnccacrhnbdfrcehfuuamqquhnnokrumnlrhspdbjdmqgdhcegdplsemdsolrdsmdrsaobeknsjjjgsiajholqdmriekjcqjpfoqesgofpanihuipjrbhinpkrqgpdjmljrsipecocsciqgegkfujliccpjaipsenpeiapccfmuqbjfeinrqscbrmflsfeoekkjnscsrgcnkoicbikafcgidjsklsbqlaqqkeesearnnaabslrorcjqihsfseirnjespupelmbiqdqpjrehjmhlfbcjrmiusqdcqiemobdogmrisgcfbcgicighmebaggsfmiabfpkihkiodrkfauchpldnhracapceeinqsbjfpjiraeceuikbecgqnnibpnsqpnbijafrkmfqpcojdbqscqadnhonhgnnojagisfinbjnkfijuiekqpnrmghridkikkgpjhdjnjgqerpsqorpbmeosbuiqkfqrblkkkbogkhlqsqsmahbqiogpnqoiglfbbcfqdusaruaaorauebeqnlkqniqruqmbeskulnpflkejqarkuebeefnqneumkbepmdfpebgkbphfudufdaufnhhericaibhnrcinpmeslsupcoomrnlfphjunioidfemoqpqadcgclommacsqngcaidhucpbrijbspnpaojcngjdjrirgajjligpakhfafnirsslmjkqonkhasijsafplcckolepfqemsjjlrcnlmjhjfgmebjhrmhb", k = 2581))