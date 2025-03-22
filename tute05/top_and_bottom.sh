#! /bin/dash

file="$1"

# prints the file name, 
echo "$file"

# plus the first and 
head -n1 "$file"

# last lines of the file.
tail -n1 "$file"