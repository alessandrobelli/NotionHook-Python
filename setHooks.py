#!/usr/bin/env python3
def changeInFile(fileName,token,url):
	#read input file
	fin = open(fileName, "rt")
	#read file contents to string
	data = fin.read()
	#replace all occurrences of the required string
	data = data.replace('TOKEN', token)
	data = data.replace('URL', url)
	#close the input file
	fin.close()
	#open the input file in write mode
	fin = open(fileName, "wt")
	#overrite the input file with the resulting data
	fin.write(data)
	#close the file
	fin.close()
	

token = input("copy and paste your token and press enter \n")
url = input("copy and paste the url of your view and press enter \n")


changeInFile("commit-msg",token,url)
changeInFile("post-commit",token,url)

print("success!")


