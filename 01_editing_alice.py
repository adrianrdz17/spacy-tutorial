import spacy

# es importante indicar el encoding para que el archivo no presente errores
with open('./data/alice.txt','r', encoding='utf-8') as f:
    text = f.read().replace('\n\n',' ').replace('\n', ' ')
    chapters = text.split('CHAPTER ')[1:]

chapter1 = chapters[0]

nlp = spacy.load('en_core_web_sm')

doc = nlp(chapter1)
sentences = list(doc.sents)
sentence = sentences[2]
# print(sentence)

ents = sentence.ents
print(ents)