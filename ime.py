#!/usr/bin/python

import sys
from workflow import Workflow
from workflow import web

from const import Const

LOG = None

class Params:
    def __init__(self, (text, itc, num)):
        self.text = text
        self.itc = itc
        self.num = num
        self.ie = 'utf-8'
        self.oe = 'utf-8'
        self.app = 'alfred-ime'

class IME(object):
    URL = "https://inputtools.google.com/request"

    def __init__(self, args, default_num, default_itc):
        self.args = args
        self.default_num = default_num
        self.default_itc = default_itc

    def execute(self):
        global LOG
        wf = Workflow()
        LOG = wf.logger
        sys.exit(wf.run(self.main))

    def handle_args(self, args):
        text = Const.DEFAULT_TEXT
        num = self.default_num
        itc = self.default_itc

        args = args.strip().split()
        try:
            text = args[0]
            num = args[1]
        except IndexError:
            pass
        return text,itc,num

    def get_workitem_texts(self, text, result, matched_length):
        left_text = text[matched_length:]
        return result+left_text

    def is_success(self, json):
        return json[0] == 'SUCCESS'

    def parsing_json(self, json):
        content = json[1]
        text = content[0][0]
        results = content[0][1]
        meta_data = content[0][3]
        annotation_list = meta_data['annotation']
        if 'matched_length' in meta_data:
            matched_length_list = meta_data['matched_length']
        else:
            matched_length_list = [len(text)] * len(results)

        return text, results, annotation_list, matched_length_list
        

    def update_workflow_items(self, json):
        if not self.is_success(json):         
            self.wf.add_item(json[0])
            self.wf.send_feedback()
            return

        text, results, annotation_list, matched_length_list = self.parsing_json(json)

        for result, annotation, matched_length in zip(results, annotation_list, matched_length_list):
            workitem_text = self.get_workitem_texts(text, result, matched_length)
            self.wf.add_item(workitem_text,
                        subtitle = annotation, 
                        arg = workitem_text, 
                        autocomplete = workitem_text,
                        icon = Const.ICON_FILE_NAME,
                        valid = True)

        self.wf.send_feedback()

    def load_response(self, params):
        response = web.post(IME.URL, params=params.__dict__)
        response.raise_for_status()
        return response

    def main(self, wf):
        self.wf = wf

        params = Params(self.handle_args(self.args))

        response = self.load_response(params)
        self.update_workflow_items(response.json())

