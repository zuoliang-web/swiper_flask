
from main import app
import json

def render_json(code=0,data=None):

    result = {
        'code':code,
        'data':data,
    }

    if app.debug:
        json_result = json.dumps(result,ensure_ascii=False,indent=4,sort_keys=True)
    else:
        json_result = json.dumps(result,ensure_ascii=False,separators=(',',':'))
    
    return json_result