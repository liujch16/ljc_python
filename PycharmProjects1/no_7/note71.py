#使用input()函数来获得用户提供的参数，其后的括号为向用户提供的额说明或提示
message = input('Tell me something, and I will repeat it back to you: ')
print(message)

#提示超过一行时，将提示存储到一个变量中再将变量传递给input()函数
prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is you first name? "

name = input(prompt)
print("\nHello, " + name + "!")
