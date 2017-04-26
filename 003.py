#!/bin/usr/bin
# -*- coding:UTF-8 -*-
import random

s = int(random.uniform(1, 10))
m = int(input('input:'))
while m != s:
    if m > s:
        print 'too big'
        m = int(input('input'))
    if m < s:
        print 'too little'
        m = int(input('input:'))
    if m == s:
        print 'ok!'
        break
