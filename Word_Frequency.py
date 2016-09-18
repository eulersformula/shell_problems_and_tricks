#Write a bash script to calculate the frequency of each word in a text file words.txt.

#For simplicity sake, you may assume:

#words.txt contains only lowercase characters and space ' ' characters.
#Each word must consist of lowercase characters only.
#Words are separated by one or more whitespace characters.
#For example, assume that words.txt has the following content:

#the day is sunny the the
#the sunny is is
#Your script should output the following, sorted by descending frequency:
#the 4
#is 3
#sunny 2
#day 1
#Note:
#Don't worry about handling ties, it is guaranteed that each word's frequency count is unique.

cat words.txt | tr -s ' ' | tr ' ' '\n' | awk 'NF' | sort | uniq -c | sort -r | awk '{print $2,$1}'

#Explanation:
#cat words.txt reads in the file. This can be replaced by "tr '\\n' ' ' < words.txt".
#tr(anslate) -s(queeze) ' ' will remove repetitive white spaces (this is not necessary actually).
#tr ' ' '\n' will break the words into lines
#uniq(ue) -c(ount) will count the number of unique lines by filtering out duplicated *adjacent* lines. This results in "count word" format for each unique word
#sort -r(everse) will reversely sort the lines according to the first column
#awk '{print $2,$1}' will reverse the columns
