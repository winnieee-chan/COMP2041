#! /bin/dash

# get zids
mlalias cs2041.fri13-strings |
grep -E 'z[0-9]{7}@' |
cut -d'@' -f1 |
sed -E 's/ //g' |

xargs acc | # pass arguments

# get courses with given zid
grep -E '[A-Z]{4}[0-9]{4}.*Student' |
sed -E 's/^.*([A-Z]{4}[0-9]{4}).*$/\1/g' |
sort |
uniq -c