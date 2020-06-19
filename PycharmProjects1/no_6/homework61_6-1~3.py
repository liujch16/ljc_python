#6-1、6-2、6-3
'''6-1使用一个字典来存储一个人的信息，包括名、姓、年龄和居住的城市，包含键first_name、last_name、age和city，并将其答应出来
   6-2使用一个字典来存储一些人喜欢的数字，将人名用做字典中的键，将数字作为值存储到字典中，打印每个人的人名与数字
   6-3模拟字典，打印一个词汇并在其后附上含义'''
##6-1
infomation = {'first_name': 'Lau','last_name': 'jinchen', 'age': '21', 'city': 'nanjing'}

print(infomation['first_name'],infomation['last_name'],infomation['age'])
##6-2
infomation_0 = {'Li': '1','Lau': '0','Cen': '9'}

print("Li: " + infomation_0['Li'],"Lau: " + infomation_0['Lau'])
