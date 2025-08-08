#!/bin/dash

# Adds the current directory (.) to the front of the search path.
# This makes it possible to run ./is_prime.sh just by typing is_prime.sh, without needing ./.
PATH=".:$PATH"

i=$1

if [ $# -ne 1 ]; then
    echo "bad input"
    exit 1
fi

for num in $(seq "$i"); do
    if is_prime.sh "$num" >/dev/null; then
        echo "$num" 
    fi
done