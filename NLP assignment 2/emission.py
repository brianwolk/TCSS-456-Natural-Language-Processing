import nltk
import operator

f = open('Klingon_Train.txt', 'r')
words = f.read().split()
tuples = [nltk.tag.str2tuple(word) for word in words]
# N V PRO CONJ
dict = {}
for tup in tuples:
	if tup[0] in dict:
		dict.get(tup[0])[tup[1]] = dict.get(tup[0]).get(tup[1]) + 1
	else:
		dict[tup[0]] = {'N' : 0, 'V' : 0, 'PRO' : 0, 'CONJ' : 0}
		dict[tup[0]][tup[1]] = 1;

for entry in dict:
	occurances = 0;
	dict2 = dict.get(entry);
	for tag in dict2:
		occurances = dict2.get(tag) + occurances
	for tag in dict2:
		dict2[tag] = (dict2[tag] / occurances) + 0.1

#print(sorted(dict.items(), key=operator.itemgetter(0)))

