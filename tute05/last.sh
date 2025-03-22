#! /bin/dash

counter=0
z0=0
z1=0
z2=0
z3=0
z4=0
z5=0
z6=0
z7=0
z8=0
z9=0
class=0

# `read -r` reads each line and splits it into four parts:
# loggin: Username
# tty: Typically represents the terminal or session.
# address: IP address, hostname, or similar.
# other: Catches any additional data.

# When you use the read command with multiple variables, the shell 
# splits each input line into words based on the Internal Field Separator 
# (IFS), which by default includes spaces, tabs, and newlines.
while read -r loggin tty address other; do
    
    case "$address" in
        *uniwide*)
            counter=$((counter + 1))
            ;;
    esac
    case "$loggin" in
        z0*) z0=$((z0+ 1)) ;;
        z1*) z1=$((z1+ 1)) ;;
        z2*) z2=$((z2+ 1)) ;;
        z3*) z3=$((z3+ 1)) ;;
        z4*) z4=$((z4+ 1)) ;;
        z5*) z5=$((z5+ 1)) ;;
        z6*) z6=$((z6+ 1)) ;;
        z7*) z7=$((z7+ 1)) ;;
        z8*) z8=$((z8+ 1)) ;;
        z9*) z9=$((z9+ 1)) ;;
        *) class=$((class+ 1)) ;;
    esac
done < last.log

echo "$counter uniwide loggins"
echo "z0: $z0, z1: $z1, z2: $z2, z3: $z3, z4: $z4, z5: $z5, z6: $z6, z7: $z7, z8: $z8, z9: $z9"
echo "class: $class"