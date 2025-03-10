#!/bin/dash


for file in *.c
do
    echo "$file includes:"
    sed -En 's/^#include ["<](.*)[">]$/    \1/p' "$file" 
done

# W09B:
# for file in *.c; do
#     # echo "$file"
#     cat "$file" | sed -En 's/^.* [<](.*)[>]$/\1/p'
# done

# H09A
# for file in *.c; do
#     echo "$file"
#     grep -E '^#include' "$file" | sed -E 's/^#include [<"](.*)[>"]/\1/'
# done

# F13B
# for name in *.c; do
#     sed -En 's/#include [\<"](.*)[\>"]/\1/gp' "$name"
# done