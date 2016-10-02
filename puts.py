#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Put a charactor on screen in different kinds of color

class _Puts:
    """ Put a single character to standard output. """
    def __init__(self):
        self.default = "0"
        self.black = "30"
        self.black_b = "40"
        self.red = "31"
        self.red_b = "41"
        self.green = "32"
        self.green_b = "42"
        self.yellow = "33"
        self.yellow_b = "43"
        self.blue = "34"
        self.blue_b = "44"
        self.purple = "35"
        self.purple_b = "45"
        self.cyan = "36"
        self.cyan_b = "46"
        self.white = "37"
        self.white_b = "47"


    def __call__(self, s, color):
        import sys
        sys.stdout.write(color and "\33[" + color + "m" + s + "\33[0m" or s)


puts = _Puts()
