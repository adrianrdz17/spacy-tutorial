import spacy
import textacy

with open('./data/alice.txt','r', encoding='utf-8') as f:
    text = f.read().replace('\n\n',' ').replace('\n', ' ')
    chapters = text.split('CHAPTER ')[1:]

chapter1 = chapters[0]

nlp = spacy.load('en_core_web_sm')

doc = nlp(chapter1)
sentences = list(doc.sents)
sentence = sentences[1]

# En esta seccion se definen el tipo de patrones que queremos obtener de nuestro texto a analizar
# POS is for Part Of Speech
patterns = [{'POS': 'VERB'}]
# patterns = [{"POS": "ADV"}, {"POS": "VERB"}]
# patterns = [{"POS": "VERB"}, {"POS": "ADV"}]
# Notese que podemos anidar nuestros distintos patrones como un arreglo de objetos
# patterns = [[{"POS": "NOUN"},{"POS": "VERB"}, {"POS": "ADV"}], [{"POS": "VERB"}, {"POS": "ADV"}], [{"POS": "ADV"}, {"POS": "VERB"}]]

# Este codigo es distinto al del video
verb_phrases = textacy.extract.matches.token_matches(doc, patterns)

for verb_phrase in verb_phrases:
    print(verb_phrase)