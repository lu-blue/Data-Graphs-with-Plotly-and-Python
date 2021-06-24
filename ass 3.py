#FOR TEXT 0
#Task 1

f = open ("Text0.txt", encoding="utf-8")
text = f.read()

#removing punctuation from the middle of the sentences
new_text = text.replace('—', "— ")
#print (new_text)


count=new_text.count('!')-1
new_text2 = new_text.replace('!','',count)
#print (new_text2)


import re
x = re.sub(r'!+(?=.*\!)','',new_text2) 
x = x.rstrip("\n")
#print (x)

x1 = x.replace(',', "")
#print (x1)

#print("\n")

#splitting sentences by finding .!? into a list
def sent_tokenize(x1):
    sentences = re.split(r"[.!?]", x1)
    sentences = [sent.strip(" ") for sent in sentences]
    sentences = sentences[:-1]
    return sentences

#print (sent_tokenize(x1))

#print("\n")

#all sentences, from the longest to the shortest (by the number of words)
lst = sent_tokenize(x1)
lst.sort(key=lambda q: len(q.split()), reverse=True)
#print (lst)

#print ("\n")

#10 top frequency sentences 
all_sentences = lst
sentence_counter = {}
for sentence in all_sentences:
    if sentence in sentence_counter:
        sentence_counter[sentence] += 1
    else:
        sentence_counter[sentence] = 1

ten_top_sentences = sorted(sentence_counter, key = sentence_counter.get, reverse = True)

#print (ten_top_sentences[:10])

#print("\n")

#prints number of words in each of top 10 sentences 
top_sentences_length = [len(sentence.split()) for sentence in ten_top_sentences[:10]]
#print (top_sentences_length)

#list of integers from top_sentences_length into a list of strings
output = [str(x) for x in top_sentences_length]  
#print (output)

#print("\n")

ranking = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
#print (ranking)

#sentence ranking of top 10 sentences (prints both sentences and ranking)
sentence_indices = -1
sentences_and_ranks = [ten_top_sentences[:10][sentence_indices]]
for elements in ten_top_sentences[:10]:
	sentence_indices += 1
	#print (f'{sentence_indices+1}. {ten_top_sentences[:10][sentence_indices]}')

#print("\n")

#preparing for csv
header0 = "Length,Sentence,Book,Ranking\n"
#print (header0)
s_list1 = output
s_list2 = ten_top_sentences[:10]
s_list3 = ranking

newList0 = []
for n in range(0, len(s_list1)):
   newList0.append(s_list1[n] + "," + s_list2[n] + ",1," + s_list3[n] + "\n")
#print(*newList0, sep='\n')

#print ("\n")

#to make list to string
listToStr1 = ' '.join([str(elem) for elem in newList0]) 
#print (listToStr1)

#Task 2

#remove !?. even from the end of the sentences (needed for word frequency count later)
all_punct_strip = x.replace('.', "").replace('!', "").replace('?', "").replace('“', "").replace('”', "").replace('\n',' ').replace('\'','').replace('—', " ").replace(':', "").replace(';', "").replace(',', "").replace('(', "").replace(')', "").replace('\ufeffI', "")
#remove stopwords, case-insensitive way 
words=all_punct_strip.split()
f=open("stopwordlist.txt", encoding="utf-16")
stopwords = f.read()
new_words = [word for word in words if word.lower() not in stopwords]
#print (new_words)

#print("\n")

#making a no-stopwords list into a list of lowercase words 
lowlist = new_words
lowlist =[item.lower () for item in lowlist]
#print (lowlist)

replaced_sg = ['language' if wd == "languages" else wd for wd in lowlist]
replaced_sg0 = ['science' if wd == "sciences" else wd for wd in replaced_sg]
replaced_sg1 = ['plant' if wd == "plants" else wd for wd in replaced_sg0]
#print (replaced_sg1)

#print ("\n")

#top 10 frequent words
from collections import Counter
frequency_list = replaced_sg1
counts = Counter(frequency_list)
#print (counts)
#print ("The top 10 frequent words in this list are:\n")
#print (Counter(counts).most_common(10))

#print ("\n")

#converting list of tuples into a list of lists
mytuple = Counter(counts).most_common(10)
result = list(map(list, mytuple))
#print (result)

#makes a list of lists into a single list (joins lists) 
import itertools
single_list = list(itertools.chain.from_iterable(result)) 
#print(single_list)

#print ("\n")

#extracting only frequency lists (numbers)
indices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
extracted = [single_list[index] for index in indices]
#print (extracted)

#print ("\n")

#list of integers into a list of strings
outcome = [str(x) for x in extracted]  
#print (outcome)

#10 top frequency words without showing their count
words = replaced_sg1
word_counter = {}
for word in words:
    if word in word_counter:
        word_counter[word] += 1
    else:
        word_counter[word] = 1

ten_top_without_count = sorted(word_counter, key = word_counter.get, reverse = True)

#print (ten_top_without_count[:10])

#print ("\n")

#word count of top ten frequent words
word_length0 = [len(i) for i in ten_top_without_count[:10]]
#print (word_length)

#list of integers from word_length into a list of strings
outcome1 = [str(x) for x in word_length0]  
#print (outcome1)

#print ("\n")

#preparing for csv
header = "Keyword,Frequency,Length,Book\n"
#print (header)
List1 = ten_top_without_count[:10]
List2 = outcome
List3 = outcome1
#printing original lists
#print ("List1 : " + str(List1))


newList = []
for n in range(0, len(List1)):
   newList.append(List1[n] + "," + List2[n] + "," + List3[n] + ",1\n")
#print (newList)

#print ("\n")

listToStr3 = ' '.join(map(str, newList))
#print (listToStr3)


#FOR TEXT 2

f = open ("Text2.txt", encoding="utf-8")
text = f.read()

#removing punctuation from the middle of the sentences
new_text = text.replace('—', "— ")
#print (new_text)


count=new_text.count('!')-1
new_text2 = new_text.replace('!','',count)
#print (new_text2)


import re
x = re.sub(r'!+(?=.*\!)','',new_text2) 
x = x.rstrip("\n")
#print (x)

x1 = x.replace(',', "")
#print (x1)

#print("\n")

#splitting sentences by finding .!? into a list
def sent_tokenize(x1):
    sentences = re.split(r"[.!?]", x1)
    sentences = [sent.strip(" ") for sent in sentences]
    sentences = sentences[:-1]
    return sentences

#print (sent_tokenize(x1))

#print("\n")


#all sentences, from the longest to the shortest (by the number of words)
lst = sent_tokenize(x1)
lst.sort(key=lambda q: len(q.split()), reverse=True)
#print (lst)

#print ("\n")

#10 top frequency sentences 
all_sentences = lst
sentence_counter = {}
for sentence in all_sentences:
    if sentence in sentence_counter:
        sentence_counter[sentence] += 1
    else:
        sentence_counter[sentence] = 1

ten_top_sentences = sorted(sentence_counter, key = sentence_counter.get, reverse = True)

#print (ten_top_sentences[:10])

#print("\n")

#prints number of words in each of top 10 sentences 
top_sentences_length = [len(sentence.split()) for sentence in ten_top_sentences[:10]]
#print (top_sentences_length)

#list of integers from top_sentences_length into a list of strings
output = [str(x) for x in top_sentences_length]  
#print (output)

#print("\n")

ranking = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
#print (ranking)

#sentence ranking of top 10 sentences
sentence_indices = -1
sentences_and_ranks = [ten_top_sentences[:10][sentence_indices]]
for elements in ten_top_sentences[:10]:
	sentence_indices += 1
	#print (f'{sentence_indices+1}. {ten_top_sentences[:10][sentence_indices]}')

#print("\n")

#preparing for csv
#header0 = "length, sentence, book, ranking"
#print (header0)
s_list1 = output
s_list2 = ten_top_sentences[:10]
s_list3 = ranking

newList1 = []
for n in range(0, len(s_list1)):
   newList1.append(s_list1[n] + "," + s_list2[n] + ",2," + s_list3[n] + "\n")
#print (*newList1, sep='\n')

listToStr2 = ' '.join(map(str, newList1))
#print (listToStr2)

#Task 2

#remove !?. even from the end of the sentences (needed for word frequency count later)
all_punct_strip = x.replace('.', "").replace('!', "").replace('?', "").replace('“', "").replace('”', "").replace('\n',' ').replace('\'','').replace('—', " ").replace(':', "").replace(';', "").replace(',', "").replace('(', "").replace(')', "").replace('\ufeffI', "")

#remove stopwords, case-insensitive way 
words=all_punct_strip.split()
f=open("stopwordlist.txt", encoding="utf-16")
stopwords = f.read()
new_words = [word for word in words if word.lower() not in stopwords]
#print (new_words)

#print("\n")

#making a no-stopwords list into a list of lowercase words 
lowlist = new_words
lowlist =[item.lower () for item in lowlist]
#print (lowlist)

replaced_sg2 = ['sound' if wd == "sounds" else wd for wd in lowlist]
replaced_sg3 = ['organ' if wd == "organs" else wd for wd in replaced_sg2]
replaced_sg4 = ['word' if wd == "words" else wd for wd in replaced_sg3]
#print (replaced_sg4)

#print ("\n")

#top 10 frequent words
from collections import Counter
frequency_list = replaced_sg4
counts = Counter(frequency_list)
#print (counts)
#print ("The top 10 frequent words in this list are:\n")
#print (Counter(counts).most_common(10))

#print ("\n")

#converting list of tuples into a list of lists
mytuple = Counter(counts).most_common(10)
result = list(map(list, mytuple))
#print (result)

#also makes a list of lists into a single list (joins lists) 
import itertools
single_list = list(itertools.chain.from_iterable(result)) 
#print(single_list)

#print ("\n")

#extracting only frequency lists (numbers)
indices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
extracted = [single_list[index] for index in indices]
#print (extracted)

#print ("\n")

#list of integers into a list of strings
outcome = [str(x) for x in extracted]  
#print (outcome)

#10 top frequency words without showing their count
words = replaced_sg4
word_counter = {}
for word in words:
    if word in word_counter:
        word_counter[word] += 1
    else:
        word_counter[word] = 1

ten_top_without_count = sorted(word_counter, key = word_counter.get, reverse = True)

#print (ten_top_without_count[:10])

#print ("\n")

#word count of top ten frequent words
word_length = [len(i) for i in ten_top_without_count[:10]]
#print (word_length)

#list of integers from word_length into a list of strings
outcome1 = [str(x) for x in word_length]  
#print (outcome1)

#print ("\n")

#preparing for csv
#header = "keyword, frequency, length, book\n"
#print (header)
List1 = ten_top_without_count[:10]
List2 = outcome
List3 = outcome1

newList4 = []
for n in range(0, len(List1)):
   newList4.append(List1[n] + "," + List2[n] + "," + List3[n] + ",2\n")
#print (newList4)

#print ("\n")

listToStr4 = ' '.join(map(str, newList4))
#print (listToStr4)

#extracting data to a csv file after we create it first
fw = open ("Keywords_All.csv", "w+") 
fw.write(header)
fw.write(listToStr3)
fw.write(listToStr4)

fw = open ("Sentences_All.csv", "w+") 
fw.write(header0)
fw.write(listToStr1)
fw.write(listToStr2)



















