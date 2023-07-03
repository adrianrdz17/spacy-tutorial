import spacy

with open('./data/alice.txt','r', encoding='utf-8') as f:
    text = f.read().replace('\n\n',' ').replace('\n', ' ')
    chapters = text.split('CHAPTER ')[1:]

chapter1 = chapters[0]

nlp = spacy.load('en_core_web_sm')
# utilizacion de la pesada
# nlp = spacy.load('en_core_web_trf')

doc = nlp(chapter1)
sentences = list(doc.sents)
sentence = sentences[1]

# nouns = []
# for token in sentence:
    # if token.pos_ == 'ADV':
        # nouns.append(token)

# print(nouns)

chunks = (list(doc.noun_chunks))
for chunk in chunks:
    if 'watch' in str(chunk):
        print(chunk)
