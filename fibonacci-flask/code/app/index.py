import copy,time
from datetime import datetime
from flask import Flask ,request, json
from werkzeug.exceptions import HTTPException
from DB_Handler import DB_Handler
from Fibonacci_Sum import Fibonacci_Sum

app = Flask(__name__)

   
@app.route('/')
def landing():
    response = app.response_class()
    response.content_type = "application/json"
    response.data = json.dumps({"message":"Please use the /health or /fib/{number} with GET requests as endpoints."})
    return (response)

@app.route('/fib/<num>', methods=['GET'])
def fibonacci_sum(num):
    ts = datetime.fromtimestamp(time.time())
    ip = request.remote_addr
    status=200
    url = request.url
    response = app.response_class()
    res = Fibonacci_Sum.calculate(int(num))
    try:
        db_resp = DB_Handler.add_to_db(ts,ip,url,status)
        if (db_resp is None):
            response.data = json.dumps(res)
            response.code = "200"
            response.content_type = "application/json"

        else:
            response.data = json.dumps({
                "code": 1122,
                "name": "error_message",
                "description": db_resp,
            })    
            
    except BaseException as e:
        response.data = json.dumps({
        "code": 1234,
        "name": "error_message",
        "description": str(e),
    })

    finally:
               
        return (response)   

@app.route('/health', methods=['GET'])
def health_check():
    
    response = app.response_class()
    response.content_type = "application/json"
    try:
        DB_Handler.get_db_connection()
        response.data = json.dumps({
                "code": 1111,
                "name": "api_health",
                "message": "API is working fine",
            }) 
    except Exception as e:
        response.data = json.dumps({
        "code": 4444,
        "name": "api_health",
        "message": str(e),
    })   
    finally:
        return response
   
@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    DB_Handler.add_to_db(datetime.fromtimestamp(time.time()), request.remote_addr, request.url, e.code)
    return response

if __name__ == '__main__':
   app.run(host='0.0.0.0')
