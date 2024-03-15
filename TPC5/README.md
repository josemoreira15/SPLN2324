**Problema**

Apresentação dos diferentes *tokens* de um texto, juntamente com a sua POS (*part of speech*) e o seu *lemma*.

**Solução**

A solução abordada passa pelas seguintes etapas:
* criação da variável **nlp = spacy.load('pt_core_news_lg')**
* utilização da variável no texto de *input*, criando a variável *doc*
* anaálise das entidades presentes em *doc*
* para as entidades que possuem espaços, substituição das mesmas, no texto de *input*, pela entidade com '_' no lugar de ' ', com o objetivo de salvaguardar as mesmas
* utilização de um dicionário para guardar as entidades, o seu *label_* e o seu *lemma_*
* utilização, novamente, da nlp para criação de novo *doc*
* tokenização do novo *doc*, reescrevendo as entidades (retirando os '_'), preenchendo com os *label_* e *lemma_* guardados