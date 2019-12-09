# Homer MarkovText
Text Generation through Markov Chains

This is a custom Markov chain text engine that generates passages like Homer!

<H1> Training Data </H1>
There are some data sets that have been provided in there which have been scoured from the web.  What's included:
1. Homer's Illiad
2. Homer's Oddysey

<H1> Generating a Dictionary </H1>
To generate a dictionary file, you'll need to run the genMarkovDict.py script as follows:

<BR><code>python genMarkovDict.py -k (the order of the markov chain; i.e. do you generate one word at a time or pairs of words) -i (input file with wild card) -d (output dictionary file) </code>

For example, the following generates a dictionary of order 2 where the text was generated using two words at a time:
<BR><code>python genMarkovDict.py -k 2 -i "Data - Obama\*.*" -d homerdict.txt </code>

<H1> Generating Text </H1>
To generate the actual text, you'll need to run the genMarkovText.py script as follows:

<code>python genMarkovText.py -w (maximum number of words in sentence) -n (number of sentences to generate) -d (source dictionary file) </code>

For example, the following creates 5 generated text sentences with each one having a maximum of 20 words (if the end of sentence is found, then it will only go up to that last word)
<BR><code>python genMarkovText.py -w 20 -n 5 -d homerdict.txt </code>
  
Special thanks to Pubs Abayasiri for open sourcing their code and making this as easy as possible!

