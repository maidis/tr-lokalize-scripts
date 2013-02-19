# -*- coding: utf-8 -*-
import os,sys
import time
import Lokalize
import Project
import Editor

def lookup():
    if not Editor.isValid(): return

    word = Editor.selectionInTarget()
    if not word: word = Editor.selectionInSource()
    if not word: return

    os.system("kioclient exec 'http://tureng.com/search/%s'" % word)

lookup()
