#!/usr/bin/python

from workflow.workflow import Settings

class Const(object):
    ITC = u"itc"
    NUMBER = u"num"
    DEFAULT_TEXT = u""
    DEFAULT_ITC = u"zh-t-i0-pinyin"
    DEFAULT_NUMBER_OF_RESULT = u'10'
    DEFAULT_CONFIG = {ITC: DEFAULT_ITC, NUMBER: DEFAULT_NUMBER_OF_RESULT}

    ICON_FILE_NAME = "icon.png"
    APPLICATION_CONFIG_FILE_NAME = "config/ime.config"

    @staticmethod
    def load_application_settings():
        return Settings(Const.APPLICATION_CONFIG_FILE_NAME, Const.DEFAULT_CONFIG)
