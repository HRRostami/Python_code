sentence=input('please enter your sentence')
sentence_list=list(sentence)
dict_words={}
for i in sentence_list:
    count_words=sentence_list.count(i)
    dict_words[i] = count_words
print(dict_words)