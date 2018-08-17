import nltk
FILE1 = ['doyle-27.txt']#, 
FILE2 = ['doyle-case-27.txt']

for doc in FILE1:
	with open(doc, 'r') as file:
		text = ''.join(file.readlines()).lower().split()
		dict1 = {}
		totalWords = 0;
		for word in text:
			dict1[word] = 0;
		for word in text:
			dict1[word] = dict1[word] + 1
			totalWords = totalWords + 1
		for entry in dict1:
			dict1[entry] = dict1[entry] / totalWords

#print(dict1)
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
			sent_length = 0;
			sent_prob = 1;
			for word in lines100[j]:
				sent_length = sent_length + 1
				if word in dict1.keys():
					sent_prob *= dict1[word]
				else:
					sent_prob = 0;
			if (sent_prob == 0):
				print('UNDEFINED')
			else:
				perplexity = 1 / (pow(sent_prob, 1.0/sent_length))
				print(str(perplexity))
		
				
			
			
		
			
