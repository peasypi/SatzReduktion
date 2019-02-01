"""
Dokumentation zur Praktikumsaufgabe Satzreduktion

"""


# -*- coding: iso-8859-1 -*-

from flair.data import Sentence
from flair.models import SequenceTagger
import re


def main():
    """
    Führt die Funktionen des Programms aus
    """
    text = eingabe_Textdatei(input("Pfad des einzulesenden Textes: "))
    tagged = nerTagger(text)
    zeitpunkt_ersetzt = zeitpunkt_ersetzen(tagged)
    ner_reduziert = replaceNER(zeitpunkt_ersetzt)
    pos_tagged = posTagger(ner_reduziert)
    print(pos_tagged)
    relativsatz_ersetzt = relativsätze_ersetzen(pos_tagged)
    print(relativsatz_ersetzt)
    pos_reduziert = pos_tags_entfernen(relativsatz_ersetzt)
    print(pos_reduziert)
    text_ausgabe("Textdatei_reduziert.txt", pos_reduziert)



def eingabe_Textdatei(pfad):
    """
    Lädt die zu reduzierende Textdatei ein

    :param pfad: Pfad zu der Textdatei
    :param data: Data speichert die Textdatei als String
    """
    with open(pfad,"r") as myfile:
        data = myfile.read().replace('\n',' ')
    return data

def nerTagger(data):
    """
    Lädt den NER-Tagger und tagged den gegebenen Text damit

    :param data: Text als String eingelesen
    :param text_tagged_ner: Enthält den Text mit ner-Tags
    :return: Text mit NER Tags
    """

    # make a sentence
    sentence = Sentence(data, use_tokenizer=True)

    # load the NER tagger
    tagger = SequenceTagger.load('de-ner')

    # run NER over sentence
    tagger.predict(sentence)

    # save tagged sentence into a String
    text_tagged_ner = sentence.to_tagged_string()

    return text_tagged_ner

def posTagger(data):
    """
    Lädt den POS-Tagger und tagged den gegebenen Text damit

    :param data: Text als String eingelesen
    :param text_tagged_pos: Enthält den Text mit pos-Tags
    :return: Text mit POS Tags
    """

    # load model
    tagger = SequenceTagger.load('de-pos')

    # make German sentence
    sentence = Sentence(data,)

    # predict POS tags
    tagger.predict(sentence)

    # print sentence with predicted tags
    text_tagged_pos = sentence.to_tagged_string()

    return text_tagged_pos

def zeitpunkt_ersetzen(text):
    """
    Ersetzt Zeitpunkte im Text
    :param text: Text wird auf von Zeitpunkte überprüft und dann durch irgendwann ersetzt
    :return: Text mit ersetzten Zeitpunkten 
    """

    # ersetzt Zeitpunkte mit Am/An Tage, Datum, Tageszeiten und Feiertage
    text = re.sub(r"(\b(Am|An|am|an)\b)\s(\b(\w|ä|ö|ü)*\b\s)?((\d{1,2}\.(\d{1,2}|(|\s)(Januar|Februar|März|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember))((\s|\.)?\d{0,4}))(\.|\s)|(Montag|Dienstag|Mittwoch|Donnerstag|Freitag|Samstag|Sonntag|Sonnabend|Wochenende(n)?|Wochen(anfang|anfängen)?)(morgen|mittag|abend|nacht|vormittag|nachmittag)?(\.|\s)|(Morgen|Mittag|Abend|Nacht|Vormittag|Nachmittag)\s|(Weihachten|Jahresende|Ostern|Muttertag|Pfingsten|Buß- und Bettag|Neujahr|Tag der Deutschen Einheit|Tag der Arbeit|Christi Himmelfahrt|Dreikönigstag|Karfreitag|\w*tag|Tag(en)?)(\.|\s))", "IRGENDWANN ", text)
    
    # ersetzt Zeitpunkte mit Im/In Monate, Jahreszeiten, Jahre
    text = re.sub(r"(\b(Im|In|im|in)\b)\s(\b\w*\b\s)*((\d{2}er)|(Wochen)|(Zeit)|(Januar|Februar|März|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember)|(Frühling|Sommer|Herbst|Winter|Frühjahr))(\s\d{1,4})?(\s|\.)", "IRGENDWANN ", text)

    # ersetzt Zeitpunkt Uhrzeit oder Jahreszahl mit Um
    text = re.sub(r"(\b(Um|um|Punkt|punkt)\b)\s(\d{1,4}|(\d{1,2}|(eins|zwei|drei|vier|fünf|sechs|sieben|acht|neun|zehn|elf|zwölf))(:|h|\.)(\s)?(\d{1,2})?)+\s(Uhr)?", "IRGENDWANN ", text)

    # ersetzt Zeitpunkt mit ab
    text = re.sub(r"(\b(Ab|ab)\b)\s((\d{1,2})?(\.)?(\s)?(Januar|Februar|März|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember)\ (\d{1,4}\s)?|(\b\w*\b\s)*(Frühling|Sommer|Herbst|Winter|Jahre)\s|(\d{4}\/\d{4}\s)|(Jahre\s|((\d{1,2}(:|\.)?(\s)?(\d{1,2})?)+\s(Uhr\s)?)))","IRGENDWANN ", text)

    # ersetzt Zeitpunkte die mit "Anfang ..." eingeleitet werden
    text = re.sub(r"(\b(Anfang|anfang)\b)(\s\b\w+\b\s)?(\s(Januar|Februar|März|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember)|((\d{2}er-|\w+)?(|\s)(Jahre(s)?|Woche)))\s", "IRGENDWANN ", text)
    
    # Temporale Adverbien
    text = re.sub(r"\b(montags|dienstags|mittwochs|donnerstags|freitags|samstags|sonntags|abends|mittags|morgens|nachts)\b","IRGENDWANN ", text)
    
    # ersetzt Jahreszahlen und Daten die wie folgt aussehen dd.mm.yyyy|dd.mm.yy
    text = re.sub(r"(((Von|von)|(Der|der))\s)?(\d{4}|\d{2}\.\d{2}\.\d{2,4})(\.|\s)?", "IRGENDWANN ", text)
    
    return text


def relativsätze_ersetzen(text):
    text_wo_rel = re.sub(r",?\s<PUNCT>\s(die|der|das|den|dem|deren|denen|dessen|welcher|welches|welche|welchem|welchen|was|wenn|wenn|wo|wohin|woher|worüber|wofür|woran|mit|auf)(\s<\w{1,5}>)(\s\b\w+\b\s<\w{1,5}>)*\s\w+\s(<AUX>|<VERB>)\s(\,\s)?", "", text)
    return text_wo_rel


def pos_tags_entfernen(text):
    text_wo_pos_tags = re.sub(r"<\w{1,5}>\s", "", text)
    return text_wo_pos_tags


##
# Die folgenden Methoden sollen Named Entities eines getaggten Textes mit Reduktionswörtern austauschen. 
# Die getaggten Wörter, die ausgetauscht werden, sind: Organization, Person und Location 
##



def replaceNER(data):
    """ 
    Die Funktion replaceNER(X) liest eine getaggte Datei ein, macht aus ihr eine Liste bestehend aus Strings, 
    ruft die jeweiligen Ersetzungs-Funktionen auf und fängt den 'letzten' Ersetzungsfall auf, 
    abschließend wird der ersetzte Text in eine neue Datei geschrieben

    :param data: Die einzulesende txt-Datei
    :return: Text reduziert
    """

    
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
    neuerText = []
    for i in words:
        if "Reset" not in words[count]:
            neuerText.append(words[count])
            neuerText.append(' ')
        count += 1
    text = ''.join(neuerText)
        
    return text

def toReplace(ersetzung,praeposition,count,words):
    """Die Funktion toReplace(ersetzung, praeposition, count, words) geht den getaggten Text Wort für Wort durch und                
    ruft, abhängig vom gefundenen Tag, die jeweilige Funktion zum Ersetzen auf
    wird kein Tag gefunden, wird der Count um 1 erhöht 
    wird ein I- oder E-Tag gefunden (Inside, End), wird das getaggte Wort auf "Reset" gesetzt 

    :param ersetzung String: Das Wort, mit dem ersetzt werden soll (z.B. "irgendwo")
    :param praeposition Liste von Präpositionen, die jeweils einem Ersetzungswort zugeordnet werden kann 
    :param count Zähler (int), der anzeigt, an welcher Stelle im Text (words) sich die Iteration befindet
    :param words Getaggter Text als Liste 
    """
    
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


def replaceLOC(ersetzung,praeposition,words,count):
    """
    Die Funktion replaceLOC(ersetzung,praeposition,words,count) wird aufgerufen, wenn ein LOCATION-Tag entdeckt wurde
    Sie überprüft, ob das Wort vor dem getaggten Wort (bzw. das Wort davor) in der entsprechenden Liste von Präpositionen enthalten ist
    ist dies der Fall, wird das TAG ersetzt und das getaggte Wort sowie die Präposition auf "Reset" gesetzt 
    (alle auf "Reset" gesetzten Worte werden nicht in die neue Datei mit eingeschrieben)

    :param ersetzung String: Das Wort, mit dem ersetzt werden soll (z.B. "irgendwo")
    :param praeposition Liste von Präpositionen, die jeweils einem Ersetzungswort zugeordnet werden kann 
    :param count Zähler (int), der anzeigt, an welcher Stelle im Text (words) sich die Iteration befindet
    :param words Getaggter Text als Liste 
    """
    
    if words[count-2] in praeposition:
                            words[count] = ersetzung
                            words[count-1] = "Reset"
                            words[count-2] = "Reset"
                            
    elif words[count-3] in praeposition:
                            words[count] = ersetzung
                            words[count-1] = "Reset"
                            words[count-2] = "Reset"
                            words[count-3] = "Reset"
    
    elif words[count-2] in praelist_wechsel:
                            words[count] = "IRGENDWO(HIN)/(HER)"
                            words[count-1] = "Reset"
                            words[count-2] = "Reset"
                            
    elif words[count-3] in praelist_wechsel:
                            words[count] = "IRGENDWO(HIN)/(HER)"
                            words[count-1] = "Reset"
                            words[count-2] = "Reset"
                            words[count-3] = "Reset"                        
    else: 
                            pass

                          
def replaceORGPER(ersetzung,praeposition,words,count): 
    """
    Die Funktion replaceORGPER(ersetzung,praeposition,words,count) wird aufgerufen, wenn ein ORGANIZATION- oder ein PERSON-Tag entdeckt wurde
    siehe Funktion replaceLOC, der Unterschied ist, dass die überprüften Präpositionen nicht gelöscht werden, da sie grammatikalisch benötigt werden 

    :param ersetzung String: Das Wort, mit dem ersetzt werden soll (z.B. "irgendwo")
    :param praeposition: Liste von Präpositionen, die jeweils einem Ersetzungswort zugeordnet werden kann 
    :param count: Zähler (int), der anzeigt, an welcher Stelle im Text (words) sich die Iteration befindet
    :param words: Getaggter Text als Liste
    """

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
praelist_wechsel = ["am","Am","an","An","auf","Auf","hinter","Hinter","in","In","neben","Neben","Über","über","unter","Unter","Vor","vor","zwischen","Zwischen","im","Im"]

praelist_irgendeine = ["um","Um","ums","Ums","Ab", "ab", "bei", "beim", "Bei","Beim","Gegenüber","gegenüber", "Nächst","nächst", "nahe","Nahe", "vis-à-vis","Vis-à-vis", "Abseits","abseits", "außer", "Außer","Außerhalb","außerhalb", "Ausgangs","ausgangs", "Beidseits","beidseits", "Beiderseits","beiderseits", "diesseits", "Diesseits","eingangs", "Eingangs","Entlang","entlang", "Fern","fern", "Fernab","fernab", "Inmitten","inmitten","Innerhalb", "innerhalb", "Jenseits","jenseits", "Längs","längs", "Längsseits","längsseits", "Links","links", "Nördlich","nördlich", "Nordöstlich","nordöstlich", "nordwestlich","Nordwestlich", "oberhalb", "Oberhalb","östlich", "Östlich","Rechts","rechts", "Seitlich","seitlich", "seitwärts","Seitwärts","Südlich", "südlich", "Südöstlich","südöstlich", "südwestlich","Südwestlich", "unfern", "Unfern","unterhalb", "Unterhalb","unweit", "Unweit","Westlich", "westlich", "weitab","Weitab","Zunächst", "zunächst", "zuseiten", "Zuseiten"]
praelist_irgendeiner = ["aus", "von", "vom", "nach", "zu", "zum", "zur", "bis", "durch", "entlang", "gegen", "gen", "lang","Aus", "Von", "Vom", "Nach", "Zu", "Zum", "Zur", "Bis", "Durch", "Entlang", "Gegen", "Gen", "Lang"]        

praelist_irgendwer = []
praelist_irgendwem = ["Mit","mit","Bei","bei","Zu","zu","von","Von"]
praelist_irgendwen = ["auf","Auf","An", "an","für","Für"]

# Artikelliste: 
artikel = ["der","Der","die","Die","das","Das","ein","Ein","Eine","eine","des", "Des","Dem","dem","den", "Den","Eines","eines","einer","Einer","einem","Einem"]


def text_ausgabe(neue_Textdatei, ersetzter_Text):
    """
    Speichert den Output in einer neuen Textdatei

    :param neue_Textdatei: Name der neuen Textdatei
    """

    with open(neue_Textdatei,'w') as file:
        file.write(ersetzter_Text)


if __name__ == '__main__':
    main()