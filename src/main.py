#!/usr/bin/python

from workflow.workflow import Settings
from ime import IME
from const import Const
    
class IMESelector(object):
    JP_ITC = "ja-t-ja-hira-i0-und"

    def __init__(self):
        settings = Settings(Const.APPLICATION_CONFIG_FILE_NAME, Const.DEFAULT_CONFIG)
        self.itc = settings[Const.ITC]
        self.num = settings[Const.NUMBER]

    def getIME(self, args):
        if self.itc == IMESelector.JP_ITC:
            from jpime import JPIME
            return JPIME(args, self.num, self.itc)
        return IME(args, self.num, self.itc)
