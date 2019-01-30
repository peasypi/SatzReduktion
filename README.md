# Satz-Reduktion

### Weiteres Vorgehen

#### Deadline 30.01.19
* Präsentation fertigstellen
  1. Wer hält den Vortag?
  2. Ersetzungsquote + Zeit pro 1000 Sätzw
  3. Git aufräumen
  4. Gute/Schlechte Sätze als Beispiele für Präsentationsfolie
  5. Probleme erklären 
* Report schreiben
  


#### Deadline 24.01.19
* Vera schreibt Programm für Person- und Organisationsersetzung
* Pia bereitet die Präsentation vor
* Marie beginnt den Report zu schreiben
* Nils schreibt Programm für Zeitersetzung


#### Deadline 17.01.19
* Pia, Marie und Nils arbeiten sich in **Flair** ein
* Marie fertigt F Test für Flair an
* Michael und Vera überlegen sich Regeln zur späteren Implementierung - 
  1. Person  -> irgendwer/irgendwem
  2. Ort -> irgendwo 
  3. Organisation -> ?
* F-Test nochmal mit allen Tools durchgehen?
* Definition: Named-entity recognition:
>**Named-entity recognition (NER)** oder **Eigennamenerkennung** ist eine Aufgabe in der Informationsextraktion und bezeichnet die automatische Identifikation und Klassifikation von Eigennamen. Ein Eigenname ist eine Folge von Wörtern, die eine **real existierende Entität** beschreibt, wie z. B. ein Firmenname

**&rarr;** falscher F-Test da Nicht-Named-Entities als richtig gezählt? (zB. Schule, Straße,...)

### Abschlusspräsentation
* Link: https://docs.google.com/presentation/d/19WAhtyTvoAB8iPGCoNefRfwEbIxNPLxk3taE54hK8e0/edit?usp=sharing


### Report
* Link: https://docs.google.com/document/d/1m9werGLU5DkYnpZEeW0IBM7NSdT4p7RdLhDkV0neTqM/edit?usp=sharing 

### Beschreibung
Reduktion / Vereinfachung von Sätze, z. B.: Ersetzung von
* Zeitangaben durch irgendwann
* Ortsangaben durch irgendwo (/ da / dort)
* Personen etc. durch irgendwer (/ jemand)
* irgendwem, irgendwas, ...

### Aufgaben
1. Definieren sinnvoller Ersetzungsschritte, -regeln und Abbruchkriterien
2. Erkennung typischer Ersetzungsmuster
3. Ansätze zur Vereinfachung von Teilsätzen, Relativsätze?
4. Evaluierung der Reduktion (Genauigkeit, Schwachstellen, Lösungsansätze)

### Betreuer
Erik Körner, koerner@informatik.uni-leipzig.de (Raum P906)

### Hinweise
* Anforderungen laut: http://asv.informatik.uni-leipzig.de/de/courses/257 
* Projekt-/Zeitplan (Gruppenmitglieder, Emails, Matrikelnr., Aufgaben, Aufgabenaufteilung, vorläufige Zeitplan, mögliche Zwischenergebnisse/-ziele)
* Sauberer Code, Ziel: Verständlichkeit für andere
* Accounts werden nach Anfrage erstellt, Details in extra Email

### Links

#### Stanford NER-Tool
* https://nlp.stanford.edu/software/CRF-NER.shtml
* https://mareikeschumacher.de/tutorial-wie-ich-stanford-ner-mit-deutschen-classifiern-installiere-und-nutze/ 
* https://nlpado.de/~sebastian/software/ner_german.shtml 

#### GermaNER
* https://github.com/tudarmstadt-lt/GermaNER 
* https://github.com/MaviccPRP/ger_ner_evals 

#### SpaCy
* https://towardsdatascience.com/named-entity-recognition-with-nltk-and-spacy-8c4a7d88e7da

#### Flair
* https://github.com/zalandoresearch/flair

#### Verzeichnisse Zeiten, Präpositionen usw. 
* [Verzeichnis deutscher Präpositionen](https://de.wiktionary.org/wiki/Verzeichnis:Deutsch/Pr%C3%A4positionen)

#### Listen zur Erweiterung der Tools
* https://de.wikipedia.org/wiki/Liste_der_gr%C3%B6%C3%9Ften_Unternehmen_in_Deutschland_(Wertsch%C3%B6pfung) - Liste der größten deutschen Unternehmen
* https://de.wikipedia.org/wiki/Liste_der_Gro%C3%9Fst%C3%A4dte_in_Deutschland - Liste der deutschen Großstädte
* https://de.wikipedia.org/wiki/Liste_der_h%C3%A4ufigsten_Familiennamen_in_Deutschland - Liste der häufigsten Familiennamen

### Fragen
* Was unterscheidet beispielsweise I-MISC und O-MISC? I / O
> Beginning, Inside, End, Single (jeweils Anfangsbuchstaben) bei flair
* Wie sollen die NER-Tools verglichen werden? 
>  1. Features des jeweiligen Tools überprüfen. Wie variabel ist es einzusetzen? Welche Funktionen bringt es mit sich?
>  2. standardisiert (F-Test)
* Gibt es ein Limit für das GIT? Kann ich es auch als Dropbox benutzen? 
> We recommend repositories be kept under 1GB each. This limit is easy to stay within if large files are kept out of the repository. If your repository exceeds 1GB, you might receive a polite email from GitHub Support requesting that you reduce the size of the repository to bring it back down.
* Kann man Regex nutzen für Datumsbestimmung?


### Mögliche Schwierigkeiten
* Satzstellung: Erkennung von Subjekt/Objekt Austausch durch Irgendwer/Irgendwem

