#! /bin/dash






# If no exit status is given the program should print a warning
# If an exit status is given the program should print an error and exit the program

case "$#" in
    # Case 1: one argument
    # arg1 -> program name
    1)  
        program_name="$1"
        echo "$0: there's a warning for $program_name"
    ;;

    # Case 2: two arguments
    # arg1 -> exit code
    # arg2 -> program name
    2) 
        echo "$0: the $2 exit with $1"
    ;;

    *)
        echo "$0 usage: [program_name] | [exit_code] [program_name]"
        exit 1
    ;;
esac

exit 0