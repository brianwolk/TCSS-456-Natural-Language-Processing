import nltk
import operator
test = '<START> tera\'ngan legh yaS <END>'
test_words = test.split()
from transition import trans_counts
from transition import tag_counts
from emission import dict

#bigrams = list(nltk.bigrams(test_words))
tags = list(tag_counts.keys())
T = len(tag_counts.keys())
W = len(test_words)
score = [[0 for x in range(W)] for y in range(T)]
backPtr = [[0 for x in range(W)] for y in range(T)]

#init step:
for t in range(1,6):
	if t != 4:
		score[t][1] = 1
		if (tags[0],tags[t]) in trans_counts.keys():
			score[t][1] = score[t][1] * trans_counts.get((tags[0], tags[t]))
		else:
			score[t][1] = score[t][1] * 0.1
		if test_words[1] in dict.keys():
			score[t][1] = score[t][1] * dict.get(test_words[1]).get(tags[t])
		else:
			score[t][1] = score[t][1] * 0.1
		backPtr[t][1] = 0;
#iter step:
for w in range(2, 5):
	for t in range(1,6):
		if t != 4:
			if test_words[w] in dict.keys():
				score[t][w] = score[t][w] * dict.get(test_words[w]).get(tags[t])
			else:
				score[t][w] = 0.1
			max = -1
			s = -1
			j_save = -1
			#get max:
			for j in range(1,6):
				if j != 4:
					if (tags[j],tags[t]) in trans_counts.keys():
						s = score[j][w - 1] * trans_counts.get((tags[j], tags[t]))
					else:
						s = score[j][w - 1] * 0.1
					if s > max:
						max = s
						j_save = j
			score[t][w] = score[t][w] * max
			backPtr[t][w] = j_save

#sequence identification:
max = -1
j_save = -1
for t in range(1,6):
		if t != 4:
			if score[t][4] > max:
				max = score[t][4]
				j_save = t

seq_stack = []
seq_stack.append(tags[ backPtr[j_save][4]])
seq_stack.append(tags[backPtr[backPtr[j_save][4]][3]])
seq_stack.append(tags[ backPtr[backPtr[ backPtr[j_save][4] ][3]][2]] )


#print(seq_stack)

print(''.join(test_words[t] + '/' + seq_stack.pop() + ' ' for t in range(1,4)))

#print(score)
#print(backPtr)


