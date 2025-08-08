#!/usr/bin/env python3

import argparse

# Create an ArgumentParser object with a description
parser = argparse.ArgumentParser(description='A program to demonstrate different action items')

# Add a positional argument 'name' of type str (required)
parser.add_argument('name', type=str, help='Your name')

# Add an optional argument '--age' of type int
parser.add_argument('--age', type=int, help='Your age')

# Add an optional argument '--hobbies' that appends multiple values to a list
parser.add_argument('--hobbies', action='append', help='Your hobbies')

# Add an optional argument '--verbose' or '-v' that counts the number of times it's provided
parser.add_argument('--verbose', '-v', action='count', default=0, help='Verbosity level')

# Add an optional flag '--developer' that sets the value to True when present
parser.add_argument('--developer', action='store_true', help='Are you a developer?')

# Add an optional argument '--language' with a limited set of valid choices
parser.add_argument('--language', choices=['python', 'java', 'c++'], help='Preferred programming language')

# Parse the command-line arguments
args = parser.parse_args()

# Print the parsed argument values
print(f'Name: {args.name}')
print(f'Age: {args.age}')
print(f'Hobbies: {args.hobbies}')
print(f'Verbosity level: {args.verbose}')
print(f'Developer: {args.developer}')
print(f'Preferred language: {args.language}')

# Example usage
# ./script.py Alice --age 30 --hobbies chess --hobbies coding -vv --developer --language python
