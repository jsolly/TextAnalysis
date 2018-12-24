# text_analysis
All this script does right now is assess the reading level of a text using the The Flesch Grade Level Readability Formula. See more details about the formula here:
http://readabilityformulas.com/flesch-grade-level-readability-formula.php

You can also get a 7 sentence summary of any text using the get_summary function. Woot woot.

#### Dependencies
You will probably need to install these packages
```
pip install nltk
pip install big-phoney
```

#### How to

In the main function at the bottom of reading_level.py you can put in your own text file and see what you get. Alternatively, you can do something like this:

```
text = "I love apples. Apples are so yummy! Also, this string should be WAYYYY longer for this to give any meaningful results."
text_stats = get_text_stats(text)
print (text_stats["Flesch-Kincaid-reading-level"] # Print out the Flesch Kinkaid Reading level
print (text_stats["summary"]) # Print out a summary of the text
```
