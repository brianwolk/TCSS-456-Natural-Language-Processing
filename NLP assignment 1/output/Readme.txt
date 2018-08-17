Training: 'doyle-27.txt'
Testing: 'doyle-case-27.txt'

The bigram model without smoothing performed the worst, with the vast majority of 
sentences resulting in undefined (infinite) perplexity. This is expected because
the odds of a two word sequence never occuring in the test text is more likely
than a single word, though the unigram model without smoothing also performed 
quite poorly.

Smoothing helped the models' 'performance'', by making what would otherwise be
undefined perplexities into a real value. 