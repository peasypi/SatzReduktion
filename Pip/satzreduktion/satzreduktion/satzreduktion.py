
"""Dokumentation zur Praktikumsaufgabe Satzreduktion."""


# -*- coding: utf-8 -*-


import re
import sys

from flair.data import Sentence
from flair.models import SequenceTagger


def main(text_input, output_textname):
    u"""Führt die Funktionen des Programms aus."""
    text_name = text_input
    text = eingabe_textdatei(text_name)
    tagged = ner_tagger(text)
    zeitpunkt_ersetzt = zeitpunkt_ersetzen(tagged)
    ner_reduziert = replace_ner(zeitpunkt_ersetzt)
    pos_tagged = pos_tagger(ner_reduziert)
    relativsatz_ersetzt = relativsaetze_ersetzen(pos_tagged)
    pp_entfernt = praepositionalphrasen_entfernen(relativsatz_ersetzt)
    pos_reduziert = pos_tags_entfernen(pp_entfernt)
    text_ausgabe("{}_reduziert.txt".format(output_textname), pos_reduziert)


def eingabe_textdatei(pfad):
    u"""
    Lädt die zu reduzierende Textdatei ein.

    :param pfad: Pfad zu der Textdatei
    :param data: Data speichert die Textdatei als String
    :return: eingelesene Textdatei als String
    """
    with open("{}".format(pfad), "r") as myfile:
        data = myfile.read().replace('\n', ' ')
    return data


def ner_tagger(data):
    u"""
    Lädt den NER-Tagger und tagged den gegebenen Text damit.

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


def pos_tagger(data):
    u"""
    Lädt den POS-Tagger und tagged den gegebenen Text damit.

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
    u"""
    Ersetzt Zeitpunkte im Text.

    :param text: Text wird auf von Zeitpunkte überprüft und dann durch
    irgendwann ersetzt
    :return: Text mit ersetzten Zeitpunkten
    """
    # ersetzt Zeitpunkte mit Am/An Tage, Datum, Tageszeiten und Feiertage
    text = re.sub(r"""
                  (\b(Am|An|am|an)\b)
                  \s(\b(\w|ä|ö|ü)*\b\s)?
                  ((\d{1,2}\.(\d{1,2}|(|\s)
                  (Januar|Februar|März|April|Mai|Juni|Juli|August|
                  September|Oktober|November|Dezember))
                  ((\s|\.)?\d{0,4}))(\.|\s)
                  |(Montag|Dienstag|Mittwoch|Donnerstag|Freitag|
                  Samstag|Sonntag|Sonnabend|Wochenende(n)?
                  |Wochen(anfang|anfängen)?)
                  (morgen|mittag|abend|nacht|vormittag|nachmittag)?(\.|\s)
                  |(Morgen|Mittag|Abend|Nacht|Vormittag|Nachmittag)\s
                  |(Weihachten|Jahresende|Ostern|Muttertag|Pfingsten
                  |Buß- und Bettag|Neujahr|Tag der Deutschen Einheit|
                  Tag der Arbeit|Christi Himmelfahrt|Dreikönigstag|
                  Karfreitag|\w*tag|Tag(en)?)(\.|\s))
                  """, "IRGENDWANN ", text, re.VERBOSE)
    # ersetzt Zeitpunkte mit Im/In Monate, Jahreszeiten, Jahre
    text = re.sub(r"""
                  (\b(Im|In|im|in)\b)\s
                  (\b\w*\b\s)*((\d{2}er)
                  |(Wochen)|(Zeit)
                  |(Januar|Februar|März|April|Mai|Juni|Juli|August|September
                  |Oktober|November|Dezember)|
                  (Frühling|Sommer|Herbst|Winter|Frühjahr))
                  (\s\d{1,4})?(\s|\.)
                  """, "IRGENDWANN ", text, re.VERBOSE)

    # ersetzt Zeitpunkt Uhrzeit oder Jahreszahl mit Um
    text = re.sub(r"""
                  (\b(Um|um|Punkt|punkt)\b)
                  \s(\d{1,4}|(\d{1,2}|
                  (eins|zwei|drei|vier|fünf|sechs|sieben|acht
                  |neun|zehn|elf|zwölf))
                  (:|h|\.)(\s)?(\d{1,2})?)+\s(Uhr)?
                  """, "IRGENDWANN ", text, re.VERBOSE)

    # ersetzt Zeitpunkt mit ab
    text = re.sub(r"""
                  (\b(Ab|ab)\b)\s
                  ((\d{1,2})?
                  (\.)?(\s)?
                  (Januar|Februar|März|April|Mai|Juni|Juli|August|
                  September|Oktober|November|Dezember)
                  (\d{1,4}\s)?|
                  (\b\w*\b\s)*
                  (Frühling|Sommer|Herbst|Winter|Jahre)
                  \s|(\d{4}\/\d{4}\s)|
                  (Jahre\s|
                  ((\d{1,2}(:|\.)?(\s)?(\d{1,2})?)+\s(Uhr\s)?)))
                  """, "IRGENDWANN ", text, re.VERBOSE)

    # ersetzt Zeitpunkte die mit "Anfang ..." eingeleitet werden
    text = re.sub(r"""
                  (\b(Anfang|anfang)\b)
                  (\s\b\w+\b\s)?
                  (\s
                  (Januar|Februar|März|April|Mai|Juni|Juli|August
                  |September|Oktober|November|Dezember)|
                  ((\d{2}er-|\w+)?(|\s)(Jahre(s)?|Woche)))\s
                  """, "IRGENDWANN ", text)
    # Temporale Adverbien
    text = re.sub(r"""
                  \b
                  (montags|dienstags|mittwochs|donnerstags|freitags|samstags
                  |sonntags|
                  abends|mittags|morgens|nachts)\b
                  """, "IRGENDWANN ", text, re.VERBOSE)
    # ersetzt Jahreszahlen und Daten die wie folgt aussehen dd.mm.yyyy|dd.mm.yy
    text = re.sub(r"""
                  (((Von|von)|
                  (Der|der))\s)?
                  (\d{4}|\d{2}\.\d{2}\.\d{2,4})(\.|\s)?
                  """, "IRGENDWANN ", text, re.VERBOSE)
    return text


def relativsaetze_ersetzen(text):
    u"""
    Ersetzt Relativsätze.

    :param text: Text wird der Funktion übergeben
    :return: Text ohne Relativsätze
    """
    text_wo_rel = re.sub(r"""
                         ,?\s<PUNCT>\s
                         (die|der|das|den|dem|deren|denen|dessen
                         |welcher|welches|welche|welchem|welchen|was|wenn
                         |wo|wohin|woher|worüber|wofür|woran|mit|auf)
                         (\s<\w{1,5}>)(\s\b\w*\b\s<\w{1,5}>)*\s\w+\s
                         (<AUX>|<VERB>)\s(\,\s)?
                         """, "", text, re.VERBOSE)
    return text_wo_rel


def pos_tags_entfernen(text):
    u"""
    Entfernt POS-Tags und noch vorhandene MISC-Tags.

    :param text: Text wird der Funktion übergeben
    :return: Text ohne jegliche Tags
    """
    text_wo_pos_tags = re.sub(r"\s?<\w{1,5}(-MISC)?>\s?", " ", text)
    return text_wo_pos_tags


def praepositionalphrasen_entfernen(text):
    u"""
    Entfernt Präpositionalphrasen.

    :param text: Text wird der Funktion übergeben
    :return: Text ohne Präpositionalphrasen
    """
    for word in text.split():
        if word in (praelist_kausal or praelist_modal):
            adp = word
            text = re.sub(r"""
                          {0}\s<ADP>(\s\b\w+\b\s<\w{{1,5}}>\s\b\w+\b\s){{0,3}}
                          <NOUN>""".format(adp),
                          "{0} IRGENDETWAS".format(adp), text, re.VERBOSE)
    return text

##
# Die folgenden Methoden sollen Named Entities eines getaggten Textes mit
# Reduktionswörtern austauschen.
# Die getaggten Wörter, die ausgetauscht werden, sind:
# Organization, Person und Location
##


def replace_ner(data):
    u"""
    Ersetzt NER Tags.

    Die Funktion liest eine getaggte Datei ein,
    macht aus ihr eine Liste bestehend aus Strings,
    ruft die jeweiligen Ersetzungs-Funktionen auf und
    fängt den 'letzten' Ersetzungsfall auf,
    abschließend wird der ersetzte Text in eine neue Datei geschrieben.

    :param data: Die einzulesende txt-Datei
    :return: Text reduziert
    """
    count = 0
    words = data.split()

    to_replace("IRGENDWO", praelist_irgendwo, count, words)
    to_replace("IRGENDWOHIN", praelist_irgendwohin, count, words)
    to_replace("IRGENDWOHER", praelist_irgendwoher, count, words)
    to_replace("IRGENEINE ORGANISATION", praelist_irgendeine, count, words)
    to_replace("IRGENEINER ORGANISATION", praelist_irgendeiner, count, words)
    to_replace("IRGENDWEM", praelist_irgendwem, count, words)
    to_replace("IRGENWEN", praelist_irgendwen, count, words)
    to_replace("IRGENDWER", praelist_irgendwer, count, words)

    for i in words:

        if '<S-LOC>' in words[count]:
            words[count - 1] = "IRGENDWO(HIN)/(HER)"
            words[count] = "Reset"
            if words[count - 2].lower() in artikel:
                words[count - 2] = "Reset"
        elif '<B-LOC>' in words[count]:
            words[count - 1] = "IRGENDWO(HIN)/(HER)"
            words[count] = "Reset"
            if words[count - 2].lower() in artikel:
                words[count - 2] = "Reset"
        elif '<S-ORG>' in words[count]:
            words[count - 1] = "IRGENDEINE/R ORGANISATION"
            words[count] = "Reset"
            if words[count - 2].lower() in artikel:
                words[count - 2] = "Reset"
        elif '<B-ORG>' in words[count]:
            words[count - 1] = "IRGENDEINE/R ORGANISATION"
            words[count] = "Reset"
            if words[count - 2].lower() in artikel:
                words[count - 2] = "Reset"
        elif '<S-PER>' in words[count]:
            words[count - 1] = "IRGENDWER"
            words[count] = "Reset"
            if words[count - 2].lower() in artikel:
                words[count - 2] = "Reset"
        elif '<B-PER>' in words[count]:
            words[count - 1] = "IRGENDWER"
            words[count] = "Reset"
            if words[count - 2].lower() in artikel:
                words[count - 2] = "Reset"
        count += 1

    text = ' '.join([w for w in words if w != "Reset"])

    return text


def to_replace(ersetzung, praeposition, count, words):
    u"""
    Hilfsfunktion.

    Die Funktion to_replace(ersetzung, praeposition, count, words)
    geht den getaggten Text Wort für Wort durch und
    ruft, abhängig vom gefundenen Tag, die jeweilige Funktion zum Ersetzen auf
    wird kein Tag gefunden, wird der Count um 1 erhöht
    wird ein I- oder E-Tag gefunden (Inside, End),
    wird das getaggte Wort auf "Reset" gesetzt

    :param ersetzung String: Das Wort, mit dem ersetzt werden soll
    (z.B. "irgendwo")
    :param praeposition Liste von Präpositionen,
    die jeweils einem Ersetzungswort zugeordnet werden kann
    :param count Zähler (int), der anzeigt, an welcher Stelle im Text (words)
     sich die Iteration befindet
    :param words Getaggter Text als Liste
    """
    for i in words:
        if '<S-LOC>' in words[count]:
            replace_loc(ersetzung, praeposition, words, count)
            count += 1
            continue
        elif '<B-LOC>' in words[count]:
            replace_loc(ersetzung, praeposition, words, count)
            count += 1
            continue
        elif '<S-ORG>' in words[count]:
            replace_org_per(ersetzung, praeposition, words, count)
            count += 1
            continue
        elif '<B-ORG>' in words[count]:
            replace_org_per(ersetzung, praeposition, words, count)
            count += 1
            continue
        elif '<S-PER>' in words[count]:
            replace_org_per(ersetzung, praeposition, words, count)
            count += 1
            continue
        elif '<B-PER>' in words[count]:
            replace_org_per(ersetzung, praeposition, words, count)
            count += 1
            continue
        elif '<I-PER>' in words[count]:
            words[count] = "Reset"
            words[count - 1] = "Reset"
            count += 1
            continue
        elif '<E-PER>' in words[count]:
            words[count] = "Reset"
            words[count - 1] = "Reset"
            count += 1
            continue
        elif '<I-ORG>' in words[count]:
            words[count] = "Reset"
            words[count - 1] = "Reset"
            count += 1
            continue
        elif '<E-ORG>' in words[count]:
            words[count] = "Reset"
            words[count - 1] = "Reset"
            count += 1
            continue
        elif '<I-LOC>' in words[count]:
            words[count] = "Reset"
            words[count - 1] = "Reset"
            count += 1
            continue
        elif '<E-LOC>' in words[count]:
            words[count] = "Reset"
            words[count - 1] = "Reset"
            count += 1
            continue

        count += 1
        continue
    count = 0


def replace_loc(ersetzung, praeposition, words, count):
    u"""
    Funktion ersetzt Locations.

    Die Funktion replace_loc(ersetzung,praeposition,words,count)
    wird aufgerufen, wenn ein LOCATION-Tag entdeckt wurde
    Sie überprüft, ob das Wort vor dem getaggten Wort (bzw. das Wort davor)
    in der entsprechenden Liste von Präpositionen enthalten ist
    ist dies der Fall, wird das TAG ersetzt und das getaggte Wort
    sowie die Präposition auf "Reset" gesetzt
    (alle auf "Reset" gesetzten Worte
    werden nicht in die neue Datei mit eingeschrieben)
    :param ersetzung String: Das Wort, mit dem ersetzt werden soll
    (z.B. "irgendwo")
    :param praeposition: Liste von Präpositionen,
    die jeweils einem Ersetzungswort zugeordnet werden kann
    :param count Zähler (int),
    der anzeigt, an welcher Stelle im Text (words) sich die Iteration befindet
    :param words: Getaggter Text als Liste
    """
    if words[count - 2].lower() in praeposition:
                            words[count] = ersetzung
                            words[count - 1] = "Reset"
                            words[count - 2] = "Reset"

    elif words[count - 3].lower() in praeposition:
                            words[count] = ersetzung
                            words[count - 1] = "Reset"
                            words[count - 2] = "Reset"
                            words[count - 3] = "Reset"

    elif words[count - 2].lower() in praelist_wechsel:
                            words[count] = "IRGENDWO(HIN)/(HER)"
                            words[count - 1] = "Reset"
                            words[count - 2] = "Reset"

    elif words[count - 3].lower() in praelist_wechsel:
                            words[count] = "IRGENDWO(HIN)/(HER)"
                            words[count - 1] = "Reset"
                            words[count - 2] = "Reset"
                            words[count - 3] = "Reset"
    else:
                            pass


def replace_org_per(ersetzung, praeposition, words, count):
    u"""
    Funktion ersetzt Personen und Organisationen.

    Die Funktion replace_org_per(ersetzung,praeposition,words,count)
    wird aufgerufen, wenn ein ORGANIZATION- oder ein PERSON-Tag entdeckt wurde
    siehe Funktion replace_loc, der Unterschied ist,
    dass die überprüften Präpositionen nicht gelöscht werden,
    da sie grammatikalisch benötigt werden

    :param ersetzung String: Das Wort, mit dem ersetzt werden soll
    (z.B. "irgendwo")
    :param praeposition: Liste von Präpositionen,
    die jeweils einem Ersetzungswort zugeordnet werden kann
    :param count: Zähler (int),
    der anzeigt, an welcher Stelle im Text (words) sich die Iteration befindet
    :param words: Getaggter Text als Liste
    """
    if words[count - 2].lower() in praeposition:
                            words[count] = ersetzung
                            words[count - 1] = "Reset"
    elif words[count - 3].lower() in praeposition:
                            words[count] = ersetzung
                            words[count - 1] = "Reset"
                            words[count - 2] = "Reset"
    else:
                            pass

# Listen mit Präpositionen, die grammatisch jeweils auf ein bestimmtes
# "Ersetzungswort" hinweisen

praelist_irgendwo = [
    "in", "um", "ums", "ab", "bei", "beim", "gegenüber", "nächst", "nahe",
    "vis-à-vis", "abseits", "außer", "außerhalb", "ausgangs", "beidseits",
    "beiderseits", "diesseits", "eingangs", "entlang", "fern", "fernab",
    "inmitten", "innerhalb", "jenseits", "längs", "längsseits", "links",
    "nördlich", "nordöstlich", "nordwestlich", "oberhalb", "östlich", "rechts",
    "seitlich", "seitwärts", "südlich", "südöstlich", "südwestlich", "unfern",
    "unterhalb", "unweit", "vis-à-vis", "westlich", "weitab", "zunächst",
    "zuseiten"
]
praelist_irgendwohin = [
    "nach", "zu", "zum", "zur", "bis", "durch", "entlang", "gegen", "gen",
    "lang"
]
praelist_irgendwoher = ["aus", "von", "vom"]
praelist_wechsel = [
    "am", "an", "auf", "hinter", "in", "In",
    "neben", "über", "unter", "Vor",
    "vor", "zwischen", "im"
]

praelist_irgendeine = [
    "um", "ums", "ab", "bei", "beim",
    "gegenüber", "nächst", "nahe", "vis-à-vis", "abseits",
    "außer", "außerhalb", "ausgangs", "beidseits", "beiderseits",
    "diesseits", "eingangs", "entlang", "fern", "fernab",
    "inmitten", "innerhalb", "jenseits", "längs", "längsseits",
    "links", "nördlich", "nordöstlich", "nordwestlich", "oberhalb",
    "östlich", "rechts", "seitlich", "seitwärts", "südlich",
    "südöstlich", "südwestlich", "unfern", "unterhalb", "unweit",
    "westlich", "weitab", "zunächst", "zuseiten"
]
praelist_irgendeiner = [
    "aus", "von", "vom", "nach", "zu",
    "zum", "zur", "bis", "durch", "entlang",
    "gegen", "gen", "lang"
]

praelist_irgendwer = []
praelist_irgendwem = ["mit", "bei", "zu", "von"]
praelist_irgendwen = ["auf", "an", "für"]

praelist_kausal = [
    "angesichts",
    "anlässlich",
    "aufgrund",
    "ob",
    "betreffs",
    "bezüglich",
    "dank",
    "mangels",
    "trotz",
    "wegen",
    "zwecks",
    "unter",
    "durch",
    "für"
]
praelist_modal = [
    "abzüglich",
    "anhand",
    "anstatt",
    "anstelle",
    "exklusive",
    "hinsichtlich",
    "in puncto",
    "inklusive",
    "minus",
    "mittels",
    "seitens",
    "statt",
    "vorbehaltlich",
    "zufolge",
    "zugunsten",
    "zuhanden",
    "zulasten",
    "zuungunsten",
    "zuzüglich"
    "um"
]

# Artikelliste:
artikel = [
    "der", "die", "das", "ein",
    "eine", "des", "dem", "den",
    "eines", "einer", "einem"
]


def text_ausgabe(neue_textdatei, ersetzter_text):
    u"""
    Speichert den Output in einer neuen Textdatei.

    :param neue_textdatei: Name der neuen Textdatei
    """
    with open(neue_textdatei, 'w') as file:
        file.write(ersetzter_text)


if __name__ == '__main__':
    main()
