#!/usr/bin/env dash

# ==============================================================================
# my-print
# Test the my-print command.
#
# Written by: Winnie Chan <chi.chan1@student.unsw.edu.au>
# Date: 2025-03-19
# For COMP2041/9044 tute05
# ==============================================================================

# Add the current directory to PATH so that my-print can be executed after a cd.
PATH="$PATH:$(pwd)"

# Create a temporary directory for the test.
test_dir="$(mktemp -d)"
cd "$test_dir" || exit 1

# Create temporary files to hold expected and actual output.
expected_stdout="$(mktemp)"
expected_stderr="$(mktemp)"
actual_stdout="$(mktemp)"
actual_stderr="$(mktemp)"

# Clean up temporary files and directories when the test is done.
trap 'rm -rf "$test_dir" "$expected_stdout" "$expected_stderr" "$actual_stdout" "$actual_stderr"' INT HUP QUIT TERM EXIT


# ----------------------------------------------------------------------
# Test 1: Call my-print with a valid argument.
#
# Expected:
#   - stdout should be the argument echoed.
#   - exit code should be 0.
#   - no output on stderr.
# ----------------------------------------------------------------------
echo "hello" > "$expected_stdout"
my-print hello > "$actual_stdout" 2> "$actual_stderr"
exit_code=$?

if [ "$exit_code" -ne 0 ]; then
    echo "Test 1 failed: expected exit code 0, got $exit_code"
    exit 1
fi

if ! diff "$expected_stdout" "$actual_stdout" >/dev/null 2>&1; then
    echo "Test 1 failed: stdout differs"
    diff "$expected_stdout" "$actual_stdout"
    exit 1
fi

if [ -s "$actual_stderr" ]; then
    echo "Test 1 failed: stderr is not empty"
    cat "$actual_stderr"
    exit 1
fi

# ----------------------------------------------------------------------
# Test 2: Call my-print without any argument.
#
# Expected:
#   - no output on stdout.
#   - a usage message (containing the word "Usage:") on stderr.
#   - exit code should be 1.
# ----------------------------------------------------------------------
my-print > "$actual_stdout" 2> "$actual_stderr"
exit_code=$?

if [ "$exit_code" -ne 1 ]; then
    echo "Test 2 failed: expected exit code 1, got $exit_code"
    exit 1
fi

if [ -s "$actual_stdout" ]; then
    echo "Test 2 failed: expected no output on stdout, got:"
    cat "$actual_stdout"
    exit 1
fi

if ! grep -q "Usage:" "$actual_stderr"; then
    echo "Test 2 failed: usage message not found in stderr"
    exit 1
fi

echo "All tests passed."