from collections import Counter, defaultdict

def read_file(filename):
    '''This function reads the contents of text file and returns
    the contents as string'''
    f = open(filename)
    fo = f.read()
    f.close()
    return fo

def clean_text(text):
    '''This function cleans the text and returns words as list'''
    text = text.lower().replace('[','').replace(']','').replace(']','')\
.replace(',','').replace('.','')\
.replace('"','').replace('!','').replace('*','')\
.replace('?','').replace(':','').replace("'",'')\
.replace('%','').replace("'",'').replace(";",'')
    return text.split()

def wordcount(words):
    '''
    This function calculates occurance of each alphabet in input word.
    Input:
        @param (word) (type: string)
    Output:
        returns dictionary where
            alphabet as key and count as value
        {alphabet:<count>, .......}
    '''
    alpha_count = {}
    stopwords = ['a', 'in']

    for alpha in words:
        if alpha not in stopwords:
            if alpha in alpha_count:
                alpha_count[alpha] += 1
            else:
                alpha_count[alpha] = 1
        else:
            pass
        # retuns a dictionary with count of each alphabet  
    return alpha_count


def wordcount_counter(words):
    '''This function calculates occurance of each word
    in input listof words. Uses Counter from collections library
    Input:
        @param (words) (type: list)
    Output:
        returns dictionary where
            alphabet as key and count as value
        {alphabet:<count>, .......}
    '''
    return Counter(words)

def wordcount_dd(words):
    word_count = defaultdict(int)

    for word in words:
        word_count[word] += 1

    return word_count

def word_count_err_handling(words):
    wordcount = {}

    for word in words:
        try:
            wordcount[word] += 1
        except KeyError:
            wordcount[word] = 1

    return wordcount