import shelve
import os

# # file_wr=""
# try:
#     file_wr=open('record.txt','xt')
#     print(type(file_wr))
#     text="""Write to an Existing File
#     To write to an existing file, you must add a parameter to the open() function:
#     "a" - Append - will append to the end of the file
#     "w" - Write - will overwrite any existing content"""
#     print(text, file=file_wr)
#     file_wr.write(text)
#     file_wr.close()
# except FileExistsError:
#     print("record.txt already exists!")
# # finally:
# #  read, readline(), readlines()
#
# file_r=open("record.txt","rt")
# text=file_r.read()
# file_r.close()
# print(text)
# print(len(text))
#
# file_r=open("record.txt","rt")
# count_symbol=50
# text1=''
# while True:
#     fragment=file_r.read(count_symbol)
#     if not fragment:
#         break
#     text1+=fragment
#     print(len(fragment))
# print("row=",file_r.read())
# print("row=",file_r.read())
# file_r.close()
# print(text1)
#
# print("*"*30)
# file_r=open("record.txt","rt")
# text2=""
# line=file_r.readline()
# while line:
#     text2 += line
#     line = file_r.readline()
# file_r.close()
# print(text2)
#
#
# text3=""
# file_r=open("record.txt","rt")
# for line in file_r:
#     text3+=line
#
# file_r.close()
# print(text2)
#
#
# text4=""
# file_r=open("record.txt","rt")
# lines=file_r.readlines()
# print(lines)
# file_r.close()
# text5="".join(lines)
# print(text5)
#
# for line in lines:
#     text4+=line
# print(text4)
#
# # binary files
#
# text3=""
# bindata=bytes(range(0,256))
# # file_b_w=open("binary.dat","wb")
# # file_b_w.write(bindata)
# # # file_b_r.write(bytes(text,encoding="UTF-8"))
# # file_b_w.close()
#
#
# file_b_w=open("binary.dat","wb")
# len_data=len(bindata)
# setByte=0
# step=50
# while setByte<len_data:
#     rez=file_b_w.write(bindata[setByte:setByte+step])
#     print(rez)
#     setByte+=step
# file_b_w.close()
#
# file_b_r=open("binary.dat","rb")
# print(file_b_r.read())
# file_b_r.close()
#
# # tell seek
# file_b_r=open("binary.dat","rb")
# # print(file_b_r.tell())
# # print(file_b_r.seek(90))
# print(chr(97))
# print(file_b_r.seek(250,0))
# print(file_b_r.tell())
# print(file_b_r.seek(4,1))
# print(file_b_r.tell())
# print(chr(165))
# file_b_r.close()
#
#
# with open("binary.dat","rb") as fread:
#     text=fread.read()
#     print(text)

"""
   ['Python', 'Guido van Rossum'],
    ['Scala', 'Martin Odersky'],
    ['PHP', 'Rasmus Lerdorf'],
    ['Ruby', 'Yukihiro Matsumoto'],
    ['C', 'Dennis Ritchie'],
"""

filename = "shelve_ex"

with shelve.open(filename, 'c') as shelve_wr:
    shelve_wr['Python'] = 'Guido van Rossum'
    shelve_wr['Scala'] = 'Martin Odersky'
    shelve_wr['C'] = 'Dennis Ritchie'

with shelve.open(filename, 'r') as shelve_r:
    key="Scala"
    if key in shelve_r:
        print(shelve_r[key])
    # print(shelve_r['Python'])
    # print(shelve_r['Scala'])

with shelve.open(filename, 'r') as shelve_r:
    value=shelve_r.get("C","None")
    print(value)

with shelve.open(filename, 'r') as shelve_r:
    for key in shelve_r:
        print(key," ",shelve_r[key])


with shelve.open(filename, 'r') as shelve_r:
    for avtor in shelve_r.values():
        print(avtor)

with shelve.open(filename, 'c') as shelve_wandr:
    shelve_wandr["C"]="Ritchie"


with shelve.open(filename, 'r') as shelve_r:
    for avtor in shelve_r.values():
        print(avtor)


# os.mkdir("example1")
# os.mkdir("D://Example1")
# os.mkdir("D://Example1/exam")
if os.path.exists("D://Example1/exam/f2.txt"):
    os.rename("D://Example1/exam/f2.txt","D://Example1/exam/f1.txt")
else:
    print("ERROR")


# filename="D://Example1/exam/f1.txt"
with open("listSt.txt",'rt') as fileR:
    # rez=fileR.read()
    rez=fileR.readlines()

print(rez)
with open("listSt.txt",'wt') as fileW:
    for row in rez:
        print(row.rstrip("\n"))
        listInfo=row.rstrip("\n").split()
        print(listInfo)
        if int(listInfo[1])>7:
            listInfo[0]=listInfo[0].upper()
        print(listInfo)
        fileW.write(f"{listInfo[0]} {listInfo[1]} \n")

print(rez)
