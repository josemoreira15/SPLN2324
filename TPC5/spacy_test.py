import spacy

nlp = spacy.load('pt_core_news_lg')

text = "O Daniel e o André foram a Ponte de Lima a pé."
doc = nlp(text)
aux_ents = dict()

for ent in doc.ents:
    if ' ' in str(ent):
        rpc_ent = str(ent).replace(' ', '_')
        text = text.replace(str(ent), rpc_ent)
        aux_ents[rpc_ent] = ent.label_, ent.lemma_

doc = nlp(text)

tokens = [(str(token), token.pos_, token.lemma_) if str(token) not in aux_ents else (str(token).replace('_', ' '), aux_ents[str(token)][0], aux_ents[str(token)][1]) for token in doc]

 
print("TOKEN  ---  POS  ---  LEMMA")
print('-' * 27)
for token in tokens:
    print(f"{token[0]}  ---  {token[1]}  ---  {token[2]}")