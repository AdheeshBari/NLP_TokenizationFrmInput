import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
if __name__ == "__main__":
    user_input = input("Enter some text: ")
    sentence_tokens = sent_tokenize(user_input)
    word_tokens = word_tokenize(user_input)
    print("Sentence Tokens:", sentence_tokens)
    print("Word Tokens:", word_tokens)
# Output  
# Enter some text: Hi, how are you? I am fine. 
# Sentence Tokens: ['Hi, how are you?', 'I am fine.']
# Word Tokens: ['Hi', ',', 'how', 'are', 'you', '?', 'I', 'am', 'fine', '.']