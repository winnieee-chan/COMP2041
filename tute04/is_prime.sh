#/bin/dash

# INPUT n
n=$1

# IF n == 1
#     echo "number is not prime"
#     exit 1
if [ "$n" -eq 1 ]; then
    echo "number is not prime"
    exit 1
fi

# i = 2
# WHILE i*i <= n
#     IF n % i == 0
#         echo "number is not prime"
#         exit 1
#     ELSE
# 			  i = i + 1
i=2
while [ $((i * i)) -le "$n" ]; do
    if [ $((n % i)) -eq 0 ]; then
        echo "number is not prime"
        exit 1
    fi
    i=$((i + 1))
done

# echo "number is prime"
# exit 0
echo "number is prime"
exit 0


