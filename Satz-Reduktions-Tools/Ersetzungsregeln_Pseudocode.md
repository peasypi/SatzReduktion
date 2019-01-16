´´´python

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
            ja: zu welchem Dictionary (?) Präpositionen gehört die Präposition? (z.B. Genitiv lokal, Dativ modal) -> Präpositionen kommen doppelt vor, daher ist es da sinnvoll, je nach TAG eine Prioritätenliste zu haben (z.B. Person nicht lokal oder temporal)
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
            ja: zu welchem Dictionary (?) Präpositionen gehört die Präposition? (z.B. Genitiv lokal, Dativ modal)
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
            ja: zu welchem Dictionary (?) Präpositionen gehört die Präposition? (z.B. Genitiv lokal, Dativ modal)
                je nachdem dann NE OHNE (!) Präposition mit dem passenden Wort ERSETZEN: irgendeine / irgendeiner Organisation (Präposition bleibt)
            nein: was ist es dann?
        Ist es irgendwas anderes? (Nomen, Verb, etc.)
            Ignorier das Wort davor, ersetze mit irgendeine Organisation

    