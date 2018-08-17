import nltk
f = open('Klingon_Train.txt', 'r')
line = f.readline()
sents = []

while line:
	if (len(line) > 1):
		sents.append(('<START>/<START> ' + line.strip('\n') + ' <END>/<END>').split())
	line = f.readline()

tags = [nltk.tag.str2tuple(word)[1] for sent in sents for word in sent]
bigrams = list(nltk.bigrams(tags))

tag_counts = {}
trans_counts = {}

for tag in tags:
	if tag in tag_counts:
		tag_counts[tag] = tag_counts.get(tag) + 1
	else:
		tag_counts[tag] = 1
		
for tup in bigrams:
	if tup in trans_counts:
		trans_counts[tup] = trans_counts.get(tup) + 1
	else:
		trans_counts[tup] = 1;

for t1 in tag_counts.keys():
	if t1 != '<END>':
		for t2 in tag_counts.keys():
			if t2 != '<START>':
				if (t1,t2) in trans_counts:
					trans_counts[(t1,t2)] = trans_counts.get((t1,t2)) / tag_counts.get(t1) + 0.1
				else:
					trans_counts[(t1,t2)] = 0.1
trans_counts.pop(('<START>', '<END>'), 0);
trans_counts.pop(('<END>', '<START>'), 0);

#print(trans_counts)