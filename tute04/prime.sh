#!/bin/dash

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