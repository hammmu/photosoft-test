import json
from urllib import request, parse
import random

# ======================================================================
# This function sends a prompt workflow to the specified URL 
# (http://127.0.0.1:8188/prompt) and queues it on the ComfyUI server
# running at that address.
def queue_prompt(prompt_workflow):
    p = {"prompt": prompt_workflow}
    data = json.dumps(p).encode('utf-8')
    req =  request.Request("http://127.0.0.1:8188/prompt", data=data)
    request.urlopen(req)    
# ======================================================================

# read workflow api data from file and convert it into dictionary 
# assign to var prompt_workflow
prompt_workflow = json.load(open('workflow.json'))
try:
    queue_prompt(prompt_workflow)
catch Exception as e:
    print(e)
