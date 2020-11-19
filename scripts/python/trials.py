import stanza

from stanza.server import CoreNLPClient
stanza.install_corenlp()
# start a CoreNLP client
with CoreNLPClient(annotators=['tokenize','ssplit','ner', 'coref']) as client:
    # run annotation over input
    ann = client.annotate('The developer spoke to the doctor and told her the truth.')
    # access all entities
    for sent in ann.sentence:
        print(sent.mentions)
    # access coreference annotations
    print(ann.corefChain)

stanza.download('en') # download English model
nlp = stanza.Pipeline('en') # initialize English neural pipeline
doc = nlp("The developer spoke to the doctor and told her the truth.") # run annotation over a sentence

for sen in doc.sentences:
    print('######ents######')
    print(sen.ents)
    print('######dependencies######')
    print(sen.dependencies)
    print('*********************')
