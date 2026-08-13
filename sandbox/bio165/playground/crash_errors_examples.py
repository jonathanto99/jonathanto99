#! /usr/bin/env python

########## Indentation error example:

#var = "test"
#if var == "test":
#print("hi")

########## Invalid syntax error example:

#var = "test"
#if var == "test"
#   print("hi")

########## Invalid syntax error example:

#var = "test"
#if var = "test":
#	print("hi")

########## Invalid syntax error example:

#file = open("hello.txt", "r"

########## One more syntax error example:

#file = open("hello.txt", "r')

########## No such file or directory example:

#file = open("hello.txt", "r")

########## Attribute error example:

#file = open('test.vcf', 'r')
#line = file.readline()
#while line != "":
#	print(line)
#	line = line.readline()

########## Type Error example:

#age = 21
#print("I'm " + age + " years old")

########## Index Error example:

#list = [1, 2]
#print(list[2])
