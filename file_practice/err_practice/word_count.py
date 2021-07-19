def count_words(filename):
    try:
        with open(filename) as file_project:
            contents = file_project.read()
    except FileNotFoundError:
        msg = "sorry, the file " + filename + " does not exist."
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) +
        " words.")

filename = 'D:\\pythonworkspace1\\vscode_python\\file_practice\\err_practice\\alice.txt'
count_words(filename)