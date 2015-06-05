#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'eternnoir'

import os
from subprocess import Popen, PIPE


class MsBuild:
    def __init__(self, msBuildPath, debug=False):
        self.executePath = msBuildPath
        self.debug = debug

    def build(self, slnPath, *para):
        if not os.path.isfile(self.executePath):
            raise Exception("MsBuild.exe not found at " + self.executePath)
        p = Popen([self.executePath, slnPath, para], stdout=PIPE, stderr=PIPE)
        output, err = p.communicate()
        if self.debug:
            print(output)
        if p.returncode == 1:
            return False
        return True

    def build_release(self, slnPath):
        arg1 = '/t:Rebuild'
        arg2 = '/p:Configuration=Release'
        return self.build(slnPath, arg1, arg2)
