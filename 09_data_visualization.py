import spacy
from spacy import displacy

with open('./data/alice.txt','r', encoding='utf-8') as f:
    text = f.read().replace('\n\n',' ').replace('\n', ' ')
    chapters = text.split('CHAPTER ')[1:]

chapter1 = chapters[0]

nlp = spacy.load('en_core_web_sm')

doc = nlp(chapter1)
sentences = list(doc.sents)
sentence = sentences[6]

# Personalizando la visualizacion
colors = {"PERSON": "linear-gradient(90deg, #aa9cfc, #fc9ce7)"}
options = {"ents": ["PERSON"], "colors": colors}

# html = displacy.render(sentence, style='dep')
html = displacy.render(doc, style='ent', options=options)

with open('data_vis.html', 'w') as f:
    f.write(html)