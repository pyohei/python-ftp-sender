#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
File Walker

"""

import os
import re

class Walker:

    def __init__(self, dir):
        self.dir = dir
        self.cache = []
        self.patterns = []

    def set_patterns(self, patterns, ignore=True):
        p = _Pattern(patterns, ignore)
        self.patterns.append(p)

    def start(self, iscache=False):
        for dirpath, dirs, files in os.walk(self.dir):
            for f in files:
                fpath = os.path.join(dirpath, f)
                if not self.__is_notice(fpath):
                    continue
                if iscache:
                    self.cache.append(fpath)
                    print "chche"
                yield fpath

    def __is_notice(self, dirpath):
        for p in self.patterns:
            if not self.__is_target_pattern(p, dirpath):
                return False
        return True

    def __is_target_pattern(self, pattern, dirpath):
        " Pattern is so complex..."
        if not self.patterns:
            return True
        for t in pattern.patterns:
            if t.search(dirpath):
                if pattern.is_ignore:
                   return False
                return True
        if pattern.is_ignore:
            return True
        return False

    def back(self, num):
        if not num:
            raise ValueError("Should over 0")
        if not self.cache:
            raise KeyError("You do not set chache")
        if num > 0:
            num = 0 - num
        return self.cache[num]

class _Pattern:

    def __init__(self, patterns, ignore=True):
        self.patterns = [re.compile(i) for i in patterns]
        self.is_ignore = ignore

if __name__ == '__main__':
    print __file__
    full_path = os.path.abspath(__file__)
    paths = full_path.split("/")
    home = "/".join(paths[:6])
    walker = Walker(home)
    walker.set_patterns([".*py$"], False)
    walker.set_patterns([".*__init__.py"])
    #walker.set_patterns([".*pyc$",".*cgi$", "/\.git"])
    n = walker.start(iscache=True)
    print "---- sart ------"
    while True:
        try:
            i = 1
            print n.next()
            print "#####",walker.back(i)
            i +=1
        except StopIteration:
            print "end"
            break
    print "----- end from: %s ------" % home
