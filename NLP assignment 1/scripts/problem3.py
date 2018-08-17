import nltk
import random
FILE1 = ['doyle-27.txt']#, 
FILE2 = ['doyle-case-27.txt']

for doc in FILE1:
	with open(doc, 'r') as file:
		text = ''.join(file.readlines()).lower().split()
		####Set up dictionary with single word counts
		dict1 = {}
		dict_of_dicts = {}
		totalWords = 0;
		for word in text:
			dict1[word] = 0.1;
			dict_of_dicts[word] = {};
		for word in text:
			dict1[word] = dict1[word] + 1
		####Set up dictionary with bigram counts
		bigrams1 = list(nltk.bigrams(text))
		vocab_size = 0;
		for big in bigrams1:
			if big[1] not in dict_of_dicts[big[0]]:
				vocab_size = vocab_size + 1
				dict_of_dicts[big[0]][big[1]] = 0.1;				
		for big in bigrams1:
			dict_of_dicts[big[0]][big[1]] = dict_of_dicts[big[0]][big[1]] + 1;
		for prev in dict1:
			for curr in dict_of_dicts[prev]:
				dict_of_dicts[prev][curr] = dict_of_dicts[prev][curr] / (dict1[prev])#* vocab_size)
		for i in range(100):
			#print('V =' + str(0.1*vocab_size))
			key1 = random.choice(list(dict_of_dicts.keys()))
			key2 = random.choice(list(dict_of_dicts[key1].keys()))
			#print('p(' + str(key2) + '|' + str(key1) + ') = ' + str(dict_of_dicts[key1][key2]))
#print(bigrams1[2][0])
#print(dict_of_dicts)
for doc in FILE2:
	with open(doc, 'r') as file:
		allLines = file.readlines()
		i = 0
		endIndex = 100
		lines100 = []
		while (i < endIndex):
			if len(allLines[i]) > 1:
				lines100.append(allLines[i].lower().split())
			else:
				endIndex = endIndex + 1
			i = i + 1

		for j in range(100):
			sent_bigrams = nltk.bigrams(lines100[j])
			sent_length = 1;
			sent_prob = 1;
			for big in sent_bigrams:
				sent_length = sent_length + 1
				if(big[0] in dict1.keys() and big[1] in dict1.keys()):
					if big[1] in dict_of_dicts[big[0]].keys():
						sent_prob *= dict_of_dicts[big[0]][big[1]]
					else:
						sent_prob *= 0.1 / dict1[big[0]];
				else:
					if(big[0] in dict1.keys()):
						sent_prob *= 0.1 / dict1[big[0]];
					else:
						sent_prob *= 0.1 / 0.1
			perplexity = 1 / (pow(sent_prob, 1.0/sent_length))
			print(str(perplexity))
