# program that reads in a string and makes each alternate character into an upper case character
# and each other alternate character into lower case character. 
# then using the same string, it makes each alternate word lowercase and uppercase.

sentence = input("Enter a sentence:")

new_sentence = " "
for i in range (len(sentence)):
    if i % 2 == 0: 
        new_sentence += sentence[i].upper()
    else: 
        new_sentence += sentence[i].lower()
print(new_sentence)

another_sentence = sentence.split(" ")
print(another_sentence)

another_new_sentence = " "
for i in range(0,len(another_sentence)):
    if i % 2 == 0:
        another_new_sentence = another_new_sentence + " " + another_sentence[i].lower()
    else: 
        another_new_sentence = another_new_sentence + " " + another_sentence[i].upper()
final_sentence = "".join(another_new_sentence)
print(final_sentence)
