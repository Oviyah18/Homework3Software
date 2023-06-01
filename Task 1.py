#TASK 1 PART A
data = """JUMP Amal
JUMP Belle
JUMP Charlie
JUMP Dylan
JOIN Evelyn
JUMP Frankie
JUMP Gloria
JOIN Helen
JOIN Iman
JOIN Joey
JOIN Kimberley
JUMP Lauren
JOIN Marie
JUMP Nuria
JUMP Odette
JUMP Priyanka
JOIN Quinn
JOIN Romily
JOIN Sofia
JUMP Theresa
JUMP Una
JUMP Violet
JOIN Wanda
JUMP Xanthe
JOIN Yvonne
JOIN Zara"""

with open('hw3_q1.txt', 'w') as file:
    file.write(data)

from collections import deque

# Create an empty deque to represent the queue
queue = deque()

# Read the input file
with open('hw3_q1.txt', 'r') as file:
    for line in file:
        # Split the line into words
        words = line.strip().split()
        command, name = words[0], words[1]

        if command == 'JUMP':
            # Add the person to the front of the queue
            queue.appendleft(name)
        elif command == 'JOIN':
            # Add the person to the back of the queue
            queue.append(name)

# Print the final order of the queue
print(list(queue))

""" PART B
# ASSUMPTIONS:
1. Input file has a fixed format with JOIN/JUMP followed my a only name for each line.
2. Assume that the file already exists
3. File opens successfully
4. No leading or trailing spaces for the data in the file
"""
