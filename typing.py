#!/usr/bin/env python
#-*- coding:utf-8 -*-

''' A typing practice toy '''

__author__ = "at"

from sys import argv
from getch import getch
from puts import puts
import string

def typing(text):
	if len(text) == 0: return
	count = 0
	lines = [ i[j:j+40] for i in text.split('\n') for j in range(0, len(i), 40)]
	for line in lines:
		print line
		pos = 0
		while pos < min(40, len(line)):
			try:
				ch = getch()
			except KeyboardInterrupt:
				puts("\n[Done] %d Error\n" % count, puts.purple)
				exit()
			if ch == '\n': break
			if ch == line[pos]:
				puts(ch, puts.green)
				pos += 1
			elif ch in string.printable:
				puts(ch, puts.red)
				count += 1
				pos += 1
		print ""
	puts("\n[Done] %d Error\n" % count, puts.purple)


def main():
	script, filename = argv
	print "filename is", filename
	with open(filename, "rt") as f:
		text = f.read()
		typing(text)


if __name__ == "__main__":
	main()
