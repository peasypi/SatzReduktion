##
# Die folgenden Methoden sollen Named Entities eines getaggten Textes mit Reduktionswörtern austauschen. 
# Die getaggten Wörter, die ausgetauscht werden, sind: Organization, Person und Location 
##

##
# Die Funktion replaceNER(X) liest eine getaggte Datei ein, macht aus ihr eine Liste bestehend aus Strings, 
# ruft die jeweiligen Ersetzungs-Funktionen auf und fängt den 'letzten' Ersetzungsfall auf,
# abschließend wird der ersetzte Text in eine neue Datei geschrieben
# @param X Die einzulesende txt-Datei
def replaceNER(X):

        with open(X, 'r') as file, open('replacedText.txt','w') as newFile: 
            data = file.read()
            count = 0
        
            words = data.split()
            
            
            
            toReplace("IRGENDWO",praelist_irgendwo,count,words)
            toReplace("IRGENDWOHIN",praelist_irgendwohin,count,words)
            toReplace("IRGENDWOHER",praelist_irgendwoher,count,words)
            toReplace("IRGENEINE ORGANISATION",praelist_irgendeine,count,words)
            toReplace("IRGENEINER ORGANISATION",praelist_irgendeiner,count,words)
            toReplace("IRGENDWEM",praelist_irgendwem,count,words)
            toReplace("IRGENWEN",praelist_irgendwen,count,words)
            toReplace("IRGENDWER",praelist_irgendwer,count,words)
            
            for i in words:
            
                if '<S-LOC>' in words[count]:
                    words[count-1] = "IRGENDWO(HIN)/(HER)"
                    words[count] = "Reset"
                    if words[count-2] in artikel:
                        words[count-2] = "Reset"
                elif '<B-LOC>' in words[count]:
                    words[count-1] = "IRGENDWO(HIN)/(HER)"
                    words[count] = "Reset"
                    if words[count-2] in artikel:
                        words[count-2] = "Reset"
                elif '<S-ORG>' in words[count]:
                    words[count-1] = "IRGENDEINE/R ORGANISATION"
                    words[count] = "Reset"
                    if words[count-2] in artikel:
                        words[count-2] = "Reset"
                elif '<B-ORG>' in words[count]:
                    words[count-1] = "IRGENDEINE/R ORGANISATION"
                    words[count] = "Reset"
                    if words[count-2] in artikel:
                        words[count-2] = "Reset"
                elif '<S-PER>' in words[count]:
                    words[count-1] = "IRGENDWER"
                    words[count] = "Reset"
                    if words[count-2] in artikel:
                        words[count-2] = "Reset"
                elif '<B-PER>' in words[count]:
                    words[count-1] = "IRGENDWER"
                    words[count] = "Reset"
                    if words[count-2] in artikel:
                        words[count-2] = "Reset"
                
                count +=1

            count = 0
               
            for i in words:
                if "Reset" not in words[count]:
                    newFile.write(words[count])
                    newFile.write(' ')
                count += 1

##
# Die Funktion toReplace(ersetzung, praeposition, count, words) geht den getaggten Text Wort für Wort durch und                
# ruft, abhängig vom gefundenen Tag, die jeweilige Funktion zum Ersetzen auf
# wird kein Tag gefunden, wird der Count um 1 erhöht 
# wird ein I- oder E-Tag gefunden (Inside, End), wird das getaggte Wort auf "Reset" gesetzt 
# 
# @param ersetzung String: Das Wort, mit dem ersetzt werden soll (z.B. "irgendwo")
# @param praeposition Liste von Präpositionen, die jeweils einem Ersetzungswort zugeordnet werden kann 
# @param count Zähler (int), der anzeigt, an welcher Stelle im Text (words) sich die Iteration befindet
# @param words Getaggter Text als Liste 

def toReplace(ersetzung,praeposition,count,words):
    
    for i in words: 
        if '<S-LOC>' in words[count]:
            replaceLOC(ersetzung,praeposition,words,count) 
            count += 1
            continue
        elif '<B-LOC>' in words[count]:
            replaceLOC(ersetzung,praeposition,words,count)
            count += 1
            continue
        elif '<S-ORG>' in words[count]:
            replaceORGPER(ersetzung,praeposition,words,count)
            count += 1
            continue
        elif '<B-ORG>' in words[count]:
            replaceORGPER(ersetzung,praeposition,words,count)
            count += 1
            continue
        elif '<S-PER>' in words [count]:
            replaceORGPER(ersetzung,praeposition,words,count)
            count += 1
            continue
        elif '<B-PER>' in words[count]:
            replaceORGPER(ersetzung,praeposition,words,count)
            count += 1
            continue
        elif '<I-PER>' in words[count]:
            words[count] = "Reset"
            words[count-1] = "Reset"
            count += 1
            continue
        elif '<E-PER>' in words[count]:
            words[count] = "Reset"
            words[count-1] = "Reset"
            count += 1
            continue
        elif '<I-ORG>' in words[count]:
            words[count] = "Reset"
            words[count-1] = "Reset"
            count += 1
            continue
        elif '<E-ORG>' in words[count]:
            words[count] = "Reset"
            words[count-1] = "Reset"
            count += 1
            continue
        elif '<I-LOC>' in words[count]:
            words[count] = "Reset"
            words[count-1] = "Reset"
            count += 1
            continue
        elif '<E-LOC>' in words[count]:
            words[count] = "Reset"
            words[count-1] = "Reset"
            count += 1
            continue
            
        count += 1   
        continue
     
    count = 0

##
# Die Funktion replaceLOC(ersetzung,praeposition,words,count) wird aufgerufen, wenn ein LOCATION-Tag entdeckt wurde
# Sie überprüft, ob das Wort vor dem getaggten Wort (bzw. das Wort davor) in der entsprechenden Liste von Präpositionen enthalten ist
# ist dies der Fall, wird das TAG ersetzt und das getaggte Wort sowie die Präposition auf "Reset" gesetzt 
# (alle auf "Reset" gesetzten Worte werden nicht in die neue Datei mit eingeschrieben)
#
# @param ersetzung String: Das Wort, mit dem ersetzt werden soll (z.B. "irgendwo")
# @param praeposition Liste von Präpositionen, die jeweils einem Ersetzungswort zugeordnet werden kann 
# @param count Zähler (int), der anzeigt, an welcher Stelle im Text (words) sich die Iteration befindet
# @param words Getaggter Text als Liste 

def replaceLOC(ersetzung,praeposition,words,count):

    if words[count-2] in praeposition:
                            words[count] = ersetzung
                            words[count-1] = "Reset"
                            words[count-2] = "Reset"
                            
    elif words[count-3] in praeposition:
                            words[count] = ersetzung
                            words[count-1] = "Reset"
                            words[count-2] = "Reset"
                            words[count-3] = "Reset"
    else: 
                            pass

##
# Die Funktion replaceORGPER(ersetzung,praeposition,words,count) wird aufgerufen, wenn ein ORGANIZATION- oder ein PERSON-Tag entdeckt wurde
# siehe Funktion replaceLOC, der Unterschied ist, dass die überprüften Präpositionen nicht gelöscht werden, da sie grammatikalisch benötigt werden 
# 
# @param ersetzung String: Das Wort, mit dem ersetzt werden soll (z.B. "irgendwo")
# @param praeposition Liste von Präpositionen, die jeweils einem Ersetzungswort zugeordnet werden kann 
# @param count Zähler (int), der anzeigt, an welcher Stelle im Text (words) sich die Iteration befindet
# @param words Getaggter Text als Liste
                          
def replaceORGPER(ersetzung,praeposition,words,count): 

    if words[count-2] in praeposition:
                            words[count] = ersetzung
                            words[count-1] = "Reset"
    elif words[count-3] in praeposition:
                            words[count] = ersetzung
                            words[count-1] = "Reset"
                            words[count-2] = "Reset"
    else: 
                            pass
                            
# Listen mit Präpositionen, die grammatisch jeweils auf ein bestimmtes "Ersetzungswort" hinweisen 
                            
praelist_irgendwo = ["in","um", "ums", "ab", "bei", "beim", "gegenüber", "nächst", "nahe", "vis-à-vis", "abseits", "außer", "außerhalb", "ausgangs", "beidseits", "beiderseits", "diesseits", "eingangs", "entlang", "fern", "fernab", "inmitten", "innerhalb", "jenseits", "längs", "längsseits", "links", "nördlich", "nordöstlich", "nordwestlich", "oberhalb", "östlich", "rechts", "seitlich", "seitwärts", "südlich", "südöstlich", "südwestlich", "unfern", "unterhalb", "unweit", "vis-à-vis", "westlich", "weitab", "zunächst", "zuseiten","In","Um", "Ums", "Ab", "Bei", "Beim", "Gegenüber", "Nächst", "Nahe", "Vis-à-vis", "Abseits", "Außer", "Außerhalb", "Ausgangs", "Beidseits", "Beiderseits", "Diesseits", "Eingangs", "Entlang", "Fern", "Fernab", "Inmitten", "Innerhalb", "Jenseits", "Längs", "Längsseits", "Links", "Nördlich", "Nordöstlich", "Nordwestlich", "Oberhalb", "Östlich", "Rechts", "Seitlich", "Seitwärts", "Südlich", "Südöstlich", "Südwestlich", "Unfern", "Unterhalb", "Unweit", "Vis-à-vis", "Westlich", "Weitab", "Zunächst", "Zuseiten"]
praelist_irgendwohin = ["nach", "zu", "zum", "zur", "bis", "durch", "entlang", "gegen", "gen", "lang","Nach", "Zu", "Zum", "Zur", "Bis", "Durch", "Entlang", "Gegen", "Gen", "Lang"]
praelist_irgendwoher = ["aus", "von", "vom","Aus", "Von", "Vom"]

praelist_irgendeine = ["um","Um","ums","Ums","Ab", "ab", "bei", "beim", "Bei","Beim","Gegenüber","gegenüber", "Nächst","nächst", "nahe","Nahe", "vis-à-vis","Vis-à-vis", "Abseits","abseits", "außer", "Außer","Außerhalb","außerhalb", "Ausgangs","ausgangs", "Beidseits","beidseits", "Beiderseits","beiderseits", "diesseits", "Diesseits","eingangs", "Eingangs","Entlang","entlang", "Fern","fern", "Fernab","fernab", "Inmitten","inmitten","Innerhalb", "innerhalb", "Jenseits","jenseits", "Längs","längs", "Längsseits","längsseits", "Links","links", "Nördlich","nördlich", "Nordöstlich","nordöstlich", "nordwestlich","Nordwestlich", "oberhalb", "Oberhalb","östlich", "Östlich","Rechts","rechts", "Seitlich","seitlich", "seitwärts","Seitwärts","Südlich", "südlich", "Südöstlich","südöstlich", "südwestlich","Südwestlich", "unfern", "Unfern","unterhalb", "Unterhalb","unweit", "Unweit","Westlich", "westlich", "weitab","Weitab","Zunächst", "zunächst", "zuseiten", "Zuseiten"]
praelist_irgendeiner = ["aus", "von", "vom", "nach", "zu", "zum", "zur", "bis", "durch", "entlang", "gegen", "gen", "lang","Aus", "Von", "Vom", "Nach", "Zu", "Zum", "Zur", "Bis", "Durch", "Entlang", "Gegen", "Gen", "Lang"]        

praelist_irgendwer = []
praelist_irgendwem = ["Mit","mit","Bei","bei","Zu","zu","von","Von"]
praelist_irgendwen = ["auf","Auf","An", "an","für","Für"]

# Artikelliste: 
artikel = ["der","Der","die","Die","das","Das","ein","Ein","Eine","eine","des", "Des","Dem","dem","den", "Den","Eines","eines","einer","Einer","einem","Einem"]

# Aufruf: 
replaceNER("Datensatz_saetze_clean_getagged_flair.txt")                            