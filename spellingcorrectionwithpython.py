# Spelling Correction with Python By Sharad Khare
# Now in this section, I will take you through how to create a program for the task of Spelling correction with Python programming language:

from textblob import TextBlob
words = ["Data Scence", "Mahine learnin", "Dicionary"]
corrected_words = []
for i in words:
    corrected_words.append(TextBlob(i))
    print("Wrong words : ", words)
    print("Corrected Words are : ")
    for i in corrected_words:
        print(i.correct(), end=" ")