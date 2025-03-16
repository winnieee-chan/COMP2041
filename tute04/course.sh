#! /bin/dash

acc z5555555 |
grep -E '[A-Z]{4}[0-9]{4}.*Student' |
sed -E 's/^.*([A-Z]{4}[0-9]{4}).*$/\1/g'