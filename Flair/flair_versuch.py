from flair.data import Sentence
from flair.models import SequenceTagger

#Versuch 1 - Textdatei als String? 
#file = open('/home/pia/Uni/5.Semester/Textmining/saetze_clean.txt', 'r')
#saetze = ''
#for line in file:
#    saetze = line.rstrip()
#file.close()

#Versuch 2 - Textdatei als String?
#with open('/home/pia/Uni/5.Semester/Textmining/saetze_clean.txt',"r") as myfile:
#   data = myfile.read().replace('\n','')


satz = "George Washington las die Washington Post in Washington ."

# make a sentence
sentence = Sentence(satz)

#load the NER tagger
tagger = SequenceTagger.load('ner')

#run NER over sentence
tagger.predict(sentence)

print(sentence)
print('The following NER tags are found:')

#iterate over entities and print
for entity in sentence.get_spans('ner'):
    print(entity)
