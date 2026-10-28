try:
    with open("input.txt", "r") as file:
        lines = file.readlines()

    line_count = len(lines)
    word_count = 0
    char_count = 0

    for line in lines:
        word_count += len(line.split())
        char_count += len(line)

    print("File Statistics")
    print("----------------")
    print("Line count:", line_count)
    print("Word count:", word_count)
    print("Character count:", char_count)

except FileNotFoundError:
    print("Error: The input.txt file was not found.")
