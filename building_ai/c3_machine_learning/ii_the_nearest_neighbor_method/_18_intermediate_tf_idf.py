"""
Exercise 17 (intermediate): TF-IDF

Modify the following program to print out the tf-idf values for each document and each word. The following code
calculates the tf and df values, so you'll just need to combine them according to the correct formula. There are
three documents (sentences) and a total of eight terms (unique words), so the output should be three lists of eight
tf-idf values each."""

# DATA BLOCK

text = '''he really really loves coffee
my sister dislikes coffee
my sister loves tea'''


import math


def main(text):
    # split the text first into lines and then into lists of words
    docs = [line.split() for line in text.splitlines()]

    N = len(docs)

    # create the vocabulary: the list of words that appear at least once
    vocabulary = list(set(text.split()))

    df = {}
    tf = {}
    for word in vocabulary:
        # tf: number of occurrences of word w in document divided by document length
        # note: tf[word] will be a list containing the tf of each word for each document
        # for example tf['he'][0] contains the term frequence of the word 'he' in the first
        # document
        tf[word] = [doc.count(word)/len(doc) for doc in docs]

        # df: number of documents containing word w
        df[word] = sum([word in doc for doc in docs])/N

    # loop through documents to calculate the tf-idf values
    for doc_index, doc in enumerate(docs):
        tfidf = []
        for word in vocabulary:
            # ADD THE CORRECT FORMULA HERE. Remember to use the base 10 logarithm: math.log(x, 10)
            tfidf.append(None)

        print(tfidf)


main(text)
