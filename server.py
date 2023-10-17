import json
from urllib import request, parse
import random
import time
# ======================================================================
# This function sends a prompt workflow to the specified URL 
# (http://127.0.0.1:8188/prompt) and queues it on the ComfyUI server
# running at that address.
def queue_prompt(prompt_workflow):
    p = {"prompt": prompt_workflow}
    data = json.dumps(p).encode('utf-8')
    req =  request.Request("http://127.0.0.1:8188/prompt", data=data)
    return json.loads(request.urlopen(req).read())
# ======================================================================


prompt_workflow = json.load(open('workflow.json'))
print(queue_prompt(prompt_workflow))
time.sleep(25)

