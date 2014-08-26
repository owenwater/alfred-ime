#!/usr/bin/python

import sys
import math
from workflow.workflow import Settings
from workflow import Workflow
from main import IME

LOG = None

class ITCConfig(object):
    ITC_CONFIG_FILE_NAME = "itc.config"
    def __init__(self):
        self.langs = Settings(ITCConfig.ITC_CONFIG_FILE_NAME)

class ConfigSetter(object):
    def __init__(self, args):
        self.args = args.strip()
        self.settings = Settings(IME.APPLICATION_CONFIG_FILE_NAME, IME.DEFAULT_CONFIG)

    def execute():
        key,value = self.args.split(Config.SEPARATOR)
        settings[key] = value
        settings.save()


class Config(object):
    NUM = u"num"
    LANG = u"lang"

    SEPARATOR = ":" 

    def __init__(self, args):
        self.args = args.strip()

    def execute(self):
        global LOG
        wf = Workflow()
        LOG = wf.logger
        sys.exit(wf.run(self.main))


    def show_set_num_item(self):
        self.wf.add_item(u"Default Number Of Words Loaded",
                         subtitle = "enter the number",
                         autocomplete = Config.NUM, 
                         icon = IME.ICON_FILE_NAME)

    def show_set_lang_item(self):
        self.wf.add_item(u"Default Language",
                         subtitle = "select the language",
                         autocomplete = Config.LANG, 
                         icon = IME.ICON_FILE_NAME)

    def show_config_options(self):
        self.show_set_num_item()
        self.show_set_lang_item()
        self.wf.send_feedback()

    def get_lang_input(self):
        itc_config = ITCConfig()
        for lang in itc_config.langs:
            self.wf.add_item(lang,
                             subtitle = itc_config.langs[lang],
                             arg = self.generate_arg(Config.LANG, itc_config.langs[lang]),
                             valid = True,
                             icon = IME.ICON_FILE_NAME)

        self.wf.send_feedback()


    def get_num_input(self, args):
        if len(args) == 0:
            self.show_set_num_item()
            self.wf.send_feedback()
            return

        number = args[0]
        if self.is_integer(number):
            self.wf.add_item(u"Set the default number of words loaded",
                         subtitle = number,
                         arg = self.generate_arg(Config.NUM, number),
                         valid = True,
                         icon = IME.ICON_FILE_NAME)
            self.wf.send_feedback()

    def handle_args(self):
        args = self.args.split()
        option = args[0]
        if option == Config.NUM:
            self.get_num_input(args[1:])
        elif option == Config.LANG:
            self.get_lang_input()
        else:
            self.show_config_options()

    def main(self, wf):
        self.wf = wf

        if self.args == "":
            self.show_config_options()
        else:
            self.handle_args()
        
    def is_integer(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def generate_arg(self, key, value):
        key + Config.SEPARATOR + value

if __name__=="__main__":
    config = Config(' '.join(sys.argv[1:]))
    config.execute()
