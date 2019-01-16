# Ersetzungsregeln: 

    Satz iterativ durchgehen, TAGs checken
        wurde ein TAG erkannt? 
            ja: ist das darauffolgende Wort auch getaggt?
            nein: welche NE? Abhängig davon in CASE 1, 2 oder 3 switchen. STOP
                ja: gehört die darauffolgende NE dazu? 
                    nein: als eigenen TAG behandeln, darauffolgende Wörter auf NEs checken (Vorgang erneut durchgehen)
                    ja: auf darauffolgendes Wort checke, ob zugehörige NE, als ein Wort behandeln, welche NE? Abhängig davon in CASE 1, 2 oder 3 switchen. STOP

## CASE 1: Person 
    Checke das Wort vor der getaggten NE
        Ist es ein Artikel ODER ein Demonstrativpronomen? (PoS)
            ja: behandele Artikel/Demonstrativpronomen und NEs als eins (alles wird später ersetzt) und checke das Wort davor
            nein: was ist es dann?
        Ist es eine Präposition? 
            ja: zu welcher Liste Präpositionen gehört die Präposition? (z.B. Genitiv lokal, Dativ modal) -> Präpositionen kommen doppelt vor, daher ist es da sinnvoll, je nach TAG eine Prioritätenliste zu haben (z.B. Person nicht lokal oder temporal)
                je nachdem dann NE mit Artikel und Präposition (!) mit dem passenden Wort ERSETZEN: irgendwer / jemand, irgendwem , etc.
            nein: was ist es dann?
        Ist es irgendwas anderes? (Nomen, Verb, etc.)
            Ignorier das Wort davor, ersetze mit irgendwer

## CASE 2: Location
    Checke das Wort vor der getaggten NE
        Ist es ein Artikel ODER ein Demonstrativpronomen? (PoS)
            ja: behandele Artikel/Demonstrativpronomen und NEs als eins (alles wird später ersetzt) und checke das Wort davor
            nein: was ist es dann?
        Ist es eine Präposition? 
            ja: zu welcher Liste Präpositionen gehört die Präposition? (z.B. Genitiv lokal, Dativ modal)
                je nachdem dann NE mit Artikel (etc.) und Präposition (!) mit dem passenden Wort ERSETZEN: irgendwo, irgendwohin , etc.
            nein: was ist es dann?
        Ist es irgendwas anderes? (Nomen, Verb, etc.)
            Ignorier das Wort davor, ersetze mit irgendwo
    

## CASE 3: Organization
    Checke das Wort vor der getaggten NE
        Ist es ein Artikel ODER ein Demonstrativpronomen? (PoS)
            ja: behandele Artikel/Demonstrativpronomen und NEs als eins (alles wird später ersetzt) und checke das Wort davor
            nein: was ist es dann?
        Ist es eine Präposition? 
            ja: zu welcher Liste Präpositionen gehört die Präposition? (z.B. Genitiv lokal, Dativ modal)
                je nachdem dann NE OHNE (!) Präposition mit dem passenden Wort ERSETZEN: irgendeine / irgendeiner Organisation (Präposition bleibt)
            nein: was ist es dann?
        Ist es irgendwas anderes? (Nomen, Verb, etc.)
            Ignorier das Wort davor, ersetze mit irgendeine Organisation

    

### Präpositionen

```python

# Wechselpräpositionen?

genitivLokal = ["abseits", "außer", "außerhalb", "ausgangs", "beidseits", "beiderseits", "diesseits", "eingangs", "entlang", "fern", "fernab", "inmitten", "innerhalb", "jenseits", "längs", "längsseits", "links", "nördlich", "nordöstlich", "nordwestlich", "oberhalb", "östlich", "rechts", "seitlich", "seitwärts", "südlich", "südöstlich", "südwestlich", "unfern", "unterhalb", "unweit", "vis-à-vis", "westlich", "weitab", "zunächst", "zuseiten"]

dativLokal = ["ab", "aus", "bei", "beim", "gegenüber", "nach", "nächst", "nahe", "vis-à-vis", "von", "vom", "zu", "zum", "zur"]

akkusativLokal = ["bis", "durch", "entlang", "gegen", "gen", "lang", "um", "ums"]

genitivModal = ["abzüglich", "anhand", "anstatt", "anstelle", "aufseiten", "ausschließlich", "ausweislich", "bar", "einbezüglich", "einschließlich", "exklusive", "hinsichtlich", "in puncto", "inklusive", "kraft", "laut", "minus", "mittels", "namens", "ob", "plus", "punkto", "rücksichtlich", "seitens", "statt", "unbeschadet", "uneingedenk", "unerachtet", "ungeachtet", "ungerechnet", "vermittels", "vermittelst", "vermöge", "voller", "vonseiten", "vorbehaltlich", "vorbehältlich", "vorgängig", "zufolge", "zugunsten", "zuhanden", "zulasten", "zuungunsten", "zuzüglich"]

dativModal = ["außer", "entgegen", "entsprechend", "gegenüber", "gemäß", "getreu", "gleich", "laut", "mit", "mitsamt", "nach", "nebst", "samt", "von", "vom", "zu", "zum", "zur", "zuwider"]

akkusativModal = ["betreffend", "bis auf", "contra", "für", "fürs", "gegen", "je", "kontra", "ohne", "per", "pro", "sonder", "versus", "via", "wider"]

genitivKausal = ["angesichts", "anlässlich", "aufgrund", "kraft", "ob", "behufs", "betreffs", "beziehentlich", "bezüglich", "dank", "eingedenk", "gelegentlich", "halber", "infolge", "mangels", "mithilfe", "trotz", "wegen", "willen", "zwecks"]

dativKausal = ["aus", "dank", "zu", "zulieb", "zuliebe"]

