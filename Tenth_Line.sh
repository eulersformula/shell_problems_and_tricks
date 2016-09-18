#How would you print just the 10th line of a file?

#For example, assume that file.txt has the following content:

#Line 1
#Line 2
#Line 3
#Line 4
#Line 5
#Line 6
#Line 7
#Line 8
#Line 9
#Line 10

#Your script should output the tenth line, which is:
#Line 10

#Notice: If the file contains less than 10 lines, what should you output

# Read from the file file.txt and output the tenth line to stdout.

#Method 1:
nl=$(wc -l file.txt | awk '{print $1}') #Notice that wc -l will output "nl file.txt"
if [ $nl -lt 10 ]; then
    echo ''
else
    head -10 file.txt | tail -1
fi
