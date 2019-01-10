# Satz-Reduktion

## Weiteres Vorgehen
* **Deadline 17.01.19**
* Pia, Marie und Nils arbeiten sich in **Flair** ein
* Marie fertigt F Test für Flair an
* Michael und Vera überlegen sich Regeln zur späteren Implementierung - 
  1. Person  -> irgendwer/irgendwem
  2. Ort -> irgendwo 
  3. Organisation -> ?


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

### SpaCy
* https://towardsdatascience.com/named-entity-recognition-with-nltk-and-spacy-8c4a7d88e7da

#### Named Entity Recognition with Tensorflow
* https://github.com/riedlma/sequence_tagging#named-entity-recognition-with-tensorflow 
* 

#### Listen zur Erweiterung der Tools
* https://de.wikipedia.org/wiki/Liste_der_gr%C3%B6%C3%9Ften_Unternehmen_in_Deutschland_(Wertsch%C3%B6pfung) - Liste der größten deutschen Unternehmen
* https://de.wikipedia.org/wiki/Liste_der_Gro%C3%9Fst%C3%A4dte_in_Deutschland - Liste der deutschen Großstädte
* https://de.wikipedia.org/wiki/Liste_der_h%C3%A4ufigsten_Familiennamen_in_Deutschland - Liste der häufigsten Familiennamen
* 

### Fragen
* Was unterscheidet beispielsweise I-MISC und O-MISC? I / O
* Wie sollen die NER-Tools verglichen werden? 
  1. Features des jeweiligen Tools überprüfen. Wie variabel ist es einzusetzen? Welche Funktionen bringt es mit sich?
* Gibt es ein Limit für das GIT? Kann ich es auch als Dropbox benutzen? 
> We recommend repositories be kept under 1GB each. This limit is easy to stay within if large files are kept out of the repository. If your repository exceeds 1GB, you might receive a polite email from GitHub Support requesting that you reduce the size of the repository to bring it back down.
* Kann man Regex nutzen für Datumsbestimmung?


### Mögliche Schwierigkeiten
* Satzstellung: Erkennung von Subjekt/Objekt Austausch durch Irgendwer/Irgendwem

### Flair
* https://github.com/zalandoresearch/flair