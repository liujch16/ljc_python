file_name = 'D:\\pythonworkspace1\\vscode_python\\file_practice\\err_practice\\alice.txt'

try:
    with open(file_name) as f_obj:
        ontents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + file_name + " does not exist."
    print(msg)
else:
    words = ontents.split()
    num_words = len(words)
    print("The file " + file_name + " has about " + str(num_words) + " words.")