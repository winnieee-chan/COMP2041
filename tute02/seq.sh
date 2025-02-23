#!/bin/dash

start=1
inc=1
end=1

if [ "$#" -eq 1 ]; then
    end="$1"
elif [ "$#" -eq 2 ]; then
    start="$1"ls
    end="$2"
else
    start="$1"
    inc="$2"
    end="$3"
fi
echo $1 $2 $3


i="$start"
while [ "$i" -le "$end" ]; do
    echo "$i"
    i=$((i + inc))
done