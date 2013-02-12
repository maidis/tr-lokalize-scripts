# -*- coding: utf-8 -*-
import os,sys
import time
import Lokalize
import Project
import Editor

def lookup():
    if not Editor.isValid(): return

    word = Editor.currentEntryId().split('\n', 1)[-1]
    if not word: return

    os.system("kioclient exec 'http://translate.google.com.tr/#en/tr/%s'" % word)

lookup()
