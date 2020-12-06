import pickle
import nltk 


def format_sentence(sent):
  return({word: True for word in nltk.word_tokenize(sent)})


def nbc(review):
    f = open('models/my_classifier.pickle', 'rb')
    classifier = pickle.load(f)
    f.close() 
    guess = classifier.classify(format_sentence(review))
    print(guess)
    print(review)