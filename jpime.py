#!/usr/bin/python

from ime import IME
from data import jp_t_jp
from const import Const

LOG = None

class JPIME(IME):
    MAX_LENGTH = 4
    ONE_CHARACTER = 1
    def get_character(self, text, index):
        for length in range(JPIME.MAX_LENGTH,0,-1):
            str = text[index:index+length]
            if str in jp_t_jp.mapping:
                return jp_t_jp.mapping[str], length
        return text[index], JPIME.ONE_CHARACTER

    def parse_text(self, text):
        index = 0
        result = ""
        while index < len(text):
            str, length = self.get_character(text, index)
            result += str
            index += length
        return result
            

    def handle_args(self, args):

        args = unicode(args, "utf-8")
        text, itc, num = super(JPIME, self).handle_args(args)
        parsed_text = self.parse_text(text)
        LOG.debug(parsed_text)
        self.wf.add_item(parsed_text,
                         subtitle = text,
                         arg = parsed_text,
                         autocomplete = parsed_text,
                         icon = Const.ICON_FILE_NAME,
                         valid = True)
        return text, itc, num

    def init_log(self, wf):
        global LOG
        LOG = wf.logger

