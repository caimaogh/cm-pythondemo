#!/usr/bin/env python2
# -*- coding: utf-8 -*-

class Grandfa(object):
    def first_name(self):
        print 'Black'

class Father(Grandfa):
    def first_name(self):
        print 'II Black'

class Mom(object):
    def second_name(self):
        print 'White'

class Tom(Father, Mom):
   print 'Tom'

my = Tom()
print my.second_name()
print my.first_name()