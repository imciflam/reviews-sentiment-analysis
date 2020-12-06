from tensorflow.keras.preprocessing.text import Tokenizer
import pickle

def lstm(review):
    f = open('models/my_classifier.pickle', 'rb')
    model = pickle.load(f)
    print(review) 
    tok = Tokenizer()  

    testing_list = list()
    testing= "warning : anyone offended by blatant , leering machismo had better avoid this film .or lots of blood & guts , men against men and mano-et-mano stuff .in other words , it's a walter hill film !with a john milius script !i always picture these guys getting together and producing a movie between arm-wrestling matches .these films always contain male characters i have a very hard time identifying with , probably due to the likelihood that any meeting between them and me would result in my arm being ripped off and then my subsequent death by beating with said limb .and we got tough guys galore , here ; drug-running banditos by the dozens , all dirty and sweaty and pretty ill-tempered , overall ; a secret task force of army commandos who are in the area to cover-up ( supposedly ) any connection between the government and the drug runners ; and lots of shit-kicking texas dirt farmers who'd as soon shoot you between the eyes as look at you .in particular , we got nick nolte as one hard-ass texas ranger , powers boothe as the drug kingpin , michael ironsides as the leader of the secret army , and rip torn as the local sheriff .torn is the sympathetic figure of the group ; he smiles before shooting anyone .as to women . . .well , i've never seen jane fonda or meryl streep in a walter hill film , and at this rate , i doubt i ever will .women exist here to look good , comfort the man , and get argued over .gosh !just like the old days . . .frankly , this is a pretty good movie , if you can accept the premise and can take the macho stuff .the cinematography is excellent , the cast of characters is broad and has texture , the script is quite good , and the film lets you keep up with what's happening yourself , without spelling it out to you .i appreciate a film that makes me have to think to keep up .finally , there's lots of sam peckinpah slow-motion shoot-ups ."
    testing2 = "my final criticism of the film lies in its glamorous depiction of alcohol and alcoholism "
    testing3 = "this film brims with imagination , containing a lush imagery that shows the arcadia that is heaven and the bitterness and frightfulness that is hell"
    testing_list.append(re.sub("[^\w]", " ",  testing2).split())

    tok.fit_on_texts(testing_list)

    testing_list = tok.texts_to_sequences(testing_list)  

    print(tok.word_counts)
    print(tok.document_count)
    print(tok.word_index)
    print(tok.word_docs)
    print(testing_list[0])
    #pad sequences of integers
    from keras.preprocessing import sequence
    max_words = 2462
    testing_list = sequence.pad_sequences(testing_list, maxlen=max_words) 
    result = model.predict(testing_list)
    print(result)