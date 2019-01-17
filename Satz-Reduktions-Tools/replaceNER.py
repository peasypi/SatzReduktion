def tobeReplaced(tag,praelist,irgend,count,words):

    for i in words:
        
        ort = count-1
        vorOrt = count-2
        vorvorOrt = count-3

        if tag in words[count]:

            if words[vorOrt] in praelist:
                words[vorOrt] = irgend
                words[ort] = "Reset"
                words[count] = "Reset"
                continue

            if words[vorOrt] in artlist:
                if words[vorvorOrt] in praelist:
                                    words[vorvorOrt] = irgend
                                    words[count] = "Reset"
                                    words[ort] = "Reset"
                                    words[vorOrt] = "Reset"
                                    continue
            
        count += 1
            


def replaceNER(X):

    with open(X, 'r') as file, open('replacedText.txt','w') as newFile: 
        data = file.readlines()

        
        count = 0
        
        for line in data:
            words = line.split()
        

        tobeReplaced('<S-LOC>',praelist_irgendwo,"IRGENDWO",count,words)
        tobeReplaced('<S-LOC>',praelist_irgendwohin,"IRGENDWOHIN",count,words)
        tobeReplaced('<S-LOC>',praelist_irgendwoher,"IRGENDWOHER",count,words)
        
        for i in words:
            if '<S-LOC>' in words[count]:
                words[count-1] = "IRGENDWO"
                words[count] = "Reset"
            count +=1

        count = 0
            

        for i in words:
            if "Reset" not in words[count]:
                newFile.write(words[count])
                newFile.write(' ')
            count += 1



artlist = ["der","Der","die","Die","das","Das","ein","eine","des","dem","den","eines","einer","einem"]

praelist_irgendwo = ["in","um", "ums", "ab", "bei", "beim", "gegenüber", "nächst", "nahe", "vis-à-vis", "abseits", "außer", "außerhalb", "ausgangs", "beidseits", "beiderseits", "diesseits", "eingangs", "entlang", "fern", "fernab", "inmitten", "innerhalb", "jenseits", "längs", "längsseits", "links", "nördlich", "nordöstlich", "nordwestlich", "oberhalb", "östlich", "rechts", "seitlich", "seitwärts", "südlich", "südöstlich", "südwestlich", "unfern", "unterhalb", "unweit", "vis-à-vis", "westlich", "weitab", "zunächst", "zuseiten"]
praelist_irgendwohin = ["nach", "zu", "zum", "zur", "bis", "durch", "entlang", "gegen", "gen", "lang"]
praelist_irgendwoher = ["aus", "von", "vom"]


praelist_genitivlokal = ["abseits", "außer", "außerhalb", "ausgangs", "beidseits", "beiderseits", "diesseits", "eingangs", "entlang",
             "fern", "fernab", "inmitten", "innerhalb", "jenseits", "längs", "längsseits", "links", "nördlich", "nordöstlich", 
             "nordwestlich", "oberhalb", "östlich", "rechts", "seitlich", "seitwärts", "südlich", "südöstlich", "südwestlich", 
             "unfern", "unterhalb", "unweit", "vis-à-vis", "westlich", "weitab", "zuseiten"]

praelist_dativlokal = ["ab", "aus", "bei", "beim", "gegenüber", "nach", "nächst", "nahe", "vis-à-vis", "von", "vom", "zu", "zum", "zur"]

praelist_akkusativLokal = ["bis", "durch", "entlang", "gegen", "gen", "lang", "um", "ums"]

praelist_genitivModal = ["abzüglich", "anhand", "anstatt", "anstelle", "aufseiten", "ausschließlich", "ausweislich", "bar", "einbezüglich",
                         "einschließlich", "exklusive", "hinsichtlich", "in puncto", "inklusive", "kraft", "laut", "minus", "mittels",
                         "namens", "ob", "plus", "punkto", "rücksichtlich", "seitens", "statt", "unbeschadet", "uneingedenk", "unerachtet",
                          "ungeachtet", "ungerechnet", "vermittels", "vermittelst", "vermöge", "voller", "vonseiten", "vorbehaltlich",
                           "vorbehältlich", "vorgängig", "zufolge", "zugunsten", "zuhanden", "zulasten", "zuungunsten", "zuzüglich"]

prelist_dativModal = ["außer", "entgegen", "entsprechend", "gegenüber", "gemäß", "getreu", "gleich", "laut", "mit", "mitsamt", "nach",
                     "nebst", "samt", "von", "vom", "zu", "zum", "zur", "zuwider"]

praelist_akkusativModal = ["betreffend", "bis auf", "contra", "für", "fürs", "gegen", "je", "kontra", "ohne", "per", "pro", "sonder",
                         "versus", "via", "wider"]

praelist_genitivKausal = ["angesichts", "anlässlich", "aufgrund", "kraft", "ob", "behufs", "betreffs", "beziehentlich", "bezüglich",
                         "dank", "eingedenk", "gelegentlich", "halber", "infolge", "mangels", "mithilfe", "trotz", "wegen", "willen",
                          "zwecks"]

praelist_dativKausal = ["aus", "dank", "zu", "zulieb", "zuliebe"]

parelist_akkusativKausal = ["durch" ,"für"]

praelist_akkusativKausal = ["durch" ,"für"]

praelist_datAkkKausal = ["auf", "vor"]

datAkkModal = ["auf", "in", "neben", "unter"]

datAkkLokal = ["an", "am", "ans", "auf", "aufs", "hinter", "hinterm", "hintern", "hinters", "in", "im", "ins", "neben", "über", "überm",
                 "übern", "übers", "unter", "unterm", "untern", "unters", "vor", "vorm", "vorn", "vors", "zwischen"]


replaceNER("saetze_clean_getagged_flair.txt")
    