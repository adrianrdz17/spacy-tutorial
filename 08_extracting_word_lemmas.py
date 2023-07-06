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

# Un lemma es la forma base o canónica de una palabra. En lingüística y procesamiento de lenguaje natural, se utiliza el concepto de lematización para reducir las diferentes formas flexionadas de una palabra a su forma base.

# Aqui obtengo los verbos de la oracion y sus formas en infinitvo
# for word in sentence:
    # if word.pos_ == 'VERB':
        # print(word, word.lemma_)

# Aqui obtengo los sustantivos de la oracion y sus formas en singular (eso me parece)
for word in sentence:
    if word.pos_ == 'NOUN':
        print(word, word.lemma_)