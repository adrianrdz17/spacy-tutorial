import spacy

with open('./data/alice.txt','r', encoding='utf-8') as f:
    text = f.read().replace('\n\n',' ').replace('\n', ' ')
    chapters = text.split('CHAPTER ')[1:]

chapter1 = chapters[0]

nlp = spacy.load('en_core_web_sm')

doc = nlp(chapter1)
sentences = list(doc.sents)
sentence = sentences[1]

# token.text nos permite acceder a la palabra como tal
# token.pos_ nos brinda el 'tipo' de elemento que es dicha palabra
for token in sentence:
    print(token.text, token.pos_)

