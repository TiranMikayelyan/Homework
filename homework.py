# xndir150 axper pahanjy chgitem chisht em haskacel te che
# with open('text.txt', 'r') as file:
#     res = file.readlines()
#     res = res[::-1]
#     print(res[0:10])

#xndir152 chi exel
# def num(filename):
#     try:
#         with open(filename, 'r') as file:
#             res = file.read()
#         mydict = {i:res.count(i) for i in res}
#         return res
#     except FileNotFoundError:   
#         return "No File"
# print(num(input('enter a file name:')))


# xndir155
# def func(file_name):
#     try:
#         with open(file_name, 'r') as file:
#             res = file.read()
#         res = res.replace('\n', ' ')
#         res = res.split(' ')
#         mydict = {i:res.count(i) for i in res}
#         return mydict
#     except FileNotFoundError:
#         print('File not found')
# print(func(input('Enter file name:')))

#xndir156 isklyucheniaya asum et chgitem incha
# sum = 0
# while True:
#     tiv = input("Greq tiv: ")
#     try:
#         if tiv == '':
#             print(sum)
#             break
#         else:
#             tiv = float(tiv)
#             sum += tiv
#         print(sum)
#     except ValueError:
#         print("Enter True Value[float]")

#xndir157 chem haskacel

#xndir158 chgitem chishta te che
# def func(filename):
#     try:
#         with open(filename, 'r') as file:
#             res = file.read()
#         res = res.replace('#', '')
#         return res
#     except FileNotFoundError:
#         return 'No file'
# print(func(input('enter file name:')))

# xndir159 chi stacvel
#xndir160 lav chi vichaky
#xndir161 eli vata

#xndir162 asa vor senca)
# def func(name):
#     try:
#         with open(name,'r') as file:
#             res = file.read()
#         res = res.replace('\n', '')
#         mydict = {i:round((res.count(i) / 26) * 100, 2) for i in res}
#         return mydict
#     except FileNotFoundError:
#         print("file not found")
# print(func(input('enter file name: ')))

#xndir163 chi linum
# def func(name1, name2):
#     try:
#         with open(name1,'r') as file:
#             res = file.read()
#         res = res.replace('\n', ' ')
#         res = res.split(' ')
#         mydict = {i:res.count(i) for i in res}
#         with open(name2,'r') as file:
#             res1 = file.read()
#         res1 = res1.replace('\n', '')
#         res1 = res1.split(' ')
#         mydict1 = {j:res.count(j) for j in res}
#         return max(mydict),max(mydict1)
        
#     except FileNotFoundError:
#         print("file not found")
# print(func(input('enter file name1:'), input('enter file name2')))


#xndir164 chgitem 
#xndir165 eli chgitem
#axper el jamanak chexav myusneri vra erkar mtacem mijankyalnery xangarum en 
