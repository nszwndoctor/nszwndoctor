from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

#we could do these two on one line, how?
in_file = open(from_file, encoding='gbk', errors='ignore')

# GBK编码错误 UnicodeDecodeError: 'gbk' codec can't decode 
# byte 0xff in position 0: illegal multibyte sequence
# 使用encoding='gbk', errors='ignore' 忽略
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RERUEN to continue, CTRL-C to abort. ")
input()
out_file = open(to_file,'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()
