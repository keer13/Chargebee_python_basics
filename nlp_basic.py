#Tokenization --- splits sentence into words
import nltk
from nltk.tokenize import word_tokenize
nltk.download("punkt")
nltk.download("punkt_tab")
text="hii have a great day my sweetiee"
token=word_tokenize(text)
print(token)


# Stop Words Removal --- removes common unnecessary words
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
text = "hii have a great day my sweetiee"
words = word_tokenize (text)
stop_words = set(stopwords.words("english"))
filtered_words = [word for word in words if word.lower() not in stop_words]
print("original:",text)
print("filtered:","".join(filtered_words))

# Stemming --- reduces words to root form (not always meaningful)
from nltk.stem import PorterStemmer
stemmer=PorterStemmer()
words=["running","runner","easily","fairly"]
stemmed_words=[stemmer.stem(word)for word in words]
print("Stemmed words:",stemmed_words)


# Lemmatization --- converts words to proper base form using grammar
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
nltk.download("wordnet")
lemmatizer = WordNetLemmatizer()
words = ["running","eating","best","fairly"]
lemmatized_words = [lemmatizer.lemmatize(word,pos=wordnet.VERB)for word in words]
print("lemmatized_words:",lemmatized_words)

# POS Tagging --- assigns grammatical tags to each word
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
nltk.download("averaged_perceptron_tagger_eng")
sentence = "hii have a great day my sweetiee."
tokens= word_tokenize(sentence)
tagged=pos_tag(tokens)
print(tagged)

# Syntax / Parsing --- evaluates or processes expression structure
exp = "5+7*13"
result=eval(exp)
print(result)


# Lowercasing --- converts all text to lowercase
text = "hii have a great day my sweetiee"
lowercase_text = text.lower()
print(lowercase_text)

# Special Character Removal --- removes unwanted symbols
import re
def remove(text):
    return re.sub(r'[^A-Za-z0-9\s]',"",text)
i = "hello!@@#$$& world"
c = remove(i)
print(c)
