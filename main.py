#!/usr/bin/python

import sys
from workflow import Workflow
from workflow import web

arg = ""
defaultLang = 'zh-t-i0-pinyin'
defaultNumberOfResult = 10

itcConfigFileName = "itc.config"
iconFileName = "icon.png"


LOG = None

class Params:
    def __init__(self):
        self.ie = 'utf-8'
        self.oe = 'utf-8'
        self.app = 'alfred-ime'

def handle_args(args):
    args = args.strip().split()
    text = ''
    num = defaultNumberOfResult
    lang = defaultLang
    try:
        text = args[0]
        num = args[1]
        lang = args[2]
    except IndexError:
        pass
    return text,num,lang

def get_workitem_text(text, result, matched_length):
    left_text = text[matched_length:]
    return result+left_text

def update_workflow_items(json, wf):
    if json[0] != 'SUCCESS':
        wf.add_item(json[0])
        wf.send_feedback()
        return
    content = json[1]
    text = content[0][0]
    results = content[0][1]
    meta_data = content[0][3]

    for index, result in enumerate(results):
        annotation = meta_data['annotation'][index]
        matched_length = len(text)
        if 'matched_length' in meta_data:
            matched_length = meta_data['matched_length'][index]
        workitem_text = get_workitem_text(text, result, matched_length)
        wf.add_item(workitem_text,
                    subtitle = annotation, 
                    arg = workitem_text, 
                    autocomplete = workitem_text,
                    uid = str(index),
                    icon = iconFileName,
                    valid = True)
    wf.send_feedback()



def main(wf):
    text,num,itc = handle_args(arg)
    params = Params()
    params.text = text
    params.itc = itc
    params.num = num
    
    url = "https://inputtools.google.com/request"
    response = web.post(url, params=params.__dict__)
    response.raise_for_status()
    
    update_workflow_items(response.json(), wf)

def start():
    global LOG
    wf = Workflow()
    LOG = wf.logger
    sys.exit(wf.run(main))


if __name__=="__main__":
    start()
