# ipsum_file = open('files/ipsum.txt')


# # for line in ipsum_file:
# #     print(line.rstrip())

# The seek sets the cursor at a starting point. The zero is the beginning of the file
# # ipsum_file.seek(0)

# # lines = ipsum_file.readlines()
# # print(lines)


# When a file is read like this it must be closed.

#  Start at the 50th character in the file
# ipsum_file.seek(50)

#  Sets file_text = to the 50th to 100th character in the file
# file_text = ipsum_file.read(100)
# print(file_text)
# ipsum_file.close()

def sequence_filter(line):
    return ">" not in line


# When the file is read like this there is no need to close the file after its done.
with open('files/dna_sequence.txt') as dna_file:
    lines = dna_file.readlines()
    print(list(filter(sequence_filter, lines)))
