punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(strOriginal):
    for char in punctuation_chars:
        strChanged=strOriginal.replace(char,'')
        strOriginal=strChanged
    return strOriginal

def get_pos(str_sent):
    count=0
    for word in str_sent.split():
        wordPunctuated=strip_punctuation(word)
        for pos_word in positive_words:
            if wordPunctuated.lower()==pos_word:
                count=count+1
    return count

def get_neg(str_sent):
    count=0
    for word in str_sent.split():
        wordPunctuated=strip_punctuation(word)
        for neg_word in negative_words:
            if wordPunctuated.lower()==neg_word:
                count=count+1
    return count
#number of retweets, number of replies, positive score, negative score, net score for
#each tweet
with open('project_twitter_data.csv') as csv_f:
    lines=csv_f.read().splitlines()
    csv_f.close()

each_line_splitted=[line.split(',') for line in lines[1:]]
header_str="'Number of Retweets','Number of replies','Positive score','Negative score','Net score'\n"
#print(header_str)
str2=header_str
for item in each_line_splitted:
    p=get_pos(item[0])
    n=get_neg(item[0])
    #print('{},{},{},{},{}\n'.format(item[1],item[2],p,n,p-n))
    str1='{},{},{},{},{}\n'.format(item[1],item[2],p,n,p-n)
    str2=str2+str1
print(str2)
