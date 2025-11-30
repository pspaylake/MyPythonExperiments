#!/bin/bash

# experiment.sh - Demonstrating piping in Bash

echo "=== Experiment: Bash Piping ==="

# 1. Generate a list of processes and filter them
echo "Processes containing 'bash':"
ps aux | grep bash | grep -v grep

# 2. Count the number of lines in a file
echo "Line count of /etc/passwd:"
cat /etc/passwd | wc -l

# 3. Sort and display unique words from a text
echo "Unique words from sample text:"
echo "apple orange banana apple grape orange" | tr ' ' '\n' | sort | uniq

# 4. Chain multiple pipes
echo "Top 5 most used shell commands in history:"
history | awk '{print $2}' | sort | uniq -c | sort -nr | head -5
