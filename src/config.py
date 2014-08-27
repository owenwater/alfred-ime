#!/usr/bin/python

import sys
from workflow.workflow import Settings
from workflow import Workflow

from const import Const

LOG = None

class ITCConfig(object):
    ITC_CONFIG_FILE_NAME = "config/itc.config"
    def __init__(self):
        self.langs = Settings(ITCConfig.ITC_CONFIG_FILE_NAME)

class ConfigSetter(object):
    def __init__(self, args):
        global LOG
        self.args = args.strip()
        self.settings = Const.load_application_settings()
        wf = Workflow()
        LOG = wf.logger

    def execute(self):
        key,value = self.args.split(Config.SEPARATOR)
        self.settings[key] = value
        self.settings.save()
        self.send_notification(key,value)

    def send_notification(self, key, value):
        notification = "Set {0} to {1}".format(key, value)
        LOG.info(notification)
        print notification


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


    def show_set_num_item(self, show_num):
        if show_num:
            self.wf.add_item(u"Default Number Of Words Loaded",
                             subtitle = "enter the number",
                             autocomplete = Config.NUM + ' ', 
                             icon = Const.ICON_FILE_NAME)

    def show_set_lang_item(self, show_lang):
        if show_lang:
            self.wf.add_item(u"Default Language",
                             subtitle = "select the language",
                             autocomplete = Config.LANG, 
                             icon = Const.ICON_FILE_NAME)

    def show_config_options(self, show_num = False, show_lang = False):
        if not (show_num or show_lang):
            #So something will showup at least
            show_num = True
            show_lang = True
        self.show_set_lang_item(show_lang)
        self.show_set_num_item(show_num)
        self.wf.send_feedback()

    def get_lang_input(self):
        itc_config = ITCConfig()
        for lang in itc_config.langs:
            self.wf.add_item(lang,
                             subtitle = itc_config.langs[lang],
                             arg = self.generate_arg(Const.ITC, itc_config.langs[lang]),
                             valid = True,
                             icon = Const.ICON_FILE_NAME)
        self.wf.send_feedback()


    def get_num_input(self, args):
        if len(args) == 0:
            self.show_config_options(show_num = True)
            self.wf.send_feedback()
            return

        number = args[0]
        if self.is_integer(number):
            self.wf.add_item(u"Set the default number of words loaded",
                         subtitle = number,
                         arg = self.generate_arg(Const.NUMBER, number),
                         valid = True,
                         icon = Const.ICON_FILE_NAME)
            self.wf.send_feedback()

    def handle_args(self):
        args = self.args.split()
        option = args[0]
        if option == Config.NUM:
            self.get_num_input(args[1:])
        elif option == Config.LANG:
            self.get_lang_input()
        else:
            show_lang = Config.LANG.startswith(option)
            show_num = Config.NUM.startswith(option)
            self.show_config_options(show_lang = show_lang, show_num = show_num)

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
        return key + Config.SEPARATOR + value

if __name__=="__main__":
    config = Config(' '.join(sys.argv[1:]))
    config.execute()
    #setter = ConfigSetter(' '.join(sys.argv[1:]))
    #setter.execute()
