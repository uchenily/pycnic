import hug
import json

@hug.get('/json')
def json_get():
    return { "message": "Hello, World!" }

app = __hug_wsgi__ 
