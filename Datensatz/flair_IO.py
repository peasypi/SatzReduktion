from flair.data import Sentence
from flair.models import SequenceTagger

# convert text file into String
with open(r'/home/pia/Uni/5.Semester/Textmining/Satz-Reduktion/satz-reduktion/Datensatz/Saetze_clean_flair.txt',"r") as myfile:
   data = myfile.read().replace('\n',' ')


# make a sentence
sentence = Sentence(data)

#load the NER tagger
tagger = SequenceTagger.load('de-ner')

#run NER over sentence
tagger.predict(sentence)

#save tagged sentence into a String
tagged = sentence.to_tagged_string()

# save String into text file
file = open('/home/pia/Uni/5.Semester/Textmining/Satz-Reduktion/satz-reduktion/Datensatz/saetze_clean_getagged_flair.txt','w')
file.writelines(tagged)

print(sentence)
print('The following NER tags are found:')

#iterate over entities and print spans
for entity in sentence.get_spans('ner'):
    print(entity)
