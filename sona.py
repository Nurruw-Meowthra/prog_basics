#1. Sõne-tüüpi muutujate deklareerimine
first_name = "James"
last_name = "Bond"


#2. Sõnede kujundamine - names
full_name = first_name + " " + last_name
self_description_sentence = "My name is " + last_name + ", " + full_name


#3. Sõnede kujundamine - cake string
cake = "vahukoor \nmarjad \ntäidispõhi"
print(cake)


#4. Sõnede tükeldamine
original_string = "Programming is fun!"
backwards = original_string[::-1]
every_other = original_string[0::2]
first_word_reversed = original_string[10::-1]
print(first_word_reversed)