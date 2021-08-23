# Fibonacci-using-Flask-Docker

The API is written using Flask framework with Python 3.8 and MySQL. The starting point of the API is the index.py class which is written in Flask. It exposes 3 endpoints to the user to get data, which are: “/fib/{number}”, “/health” & “/”. The index.py script imports DB_Handler and Fibonacci_Sum classes from DB_Handler.py and Fibonacci_Sum.py scripts respectively which are in the same folder as index.py. The DB_Handler class holds the properties to connect to the database and handles the database functions such as getting the database connection and inserting the request logs to the database table. The Fibonacci_Sum class does all the processing to find all the possible combinations of the smaller Fibonacci numbers that add up to that number. It first finds all the Fibonacci numbers that are smaller than the given number and then using 2 lists recursively calculates all the possible combinations and returns a list of all these combinations.
All the endpoints return data in JSON, if there are errors like there is no database connection or the insert fails or any HTTP error, the error messages are returned as JSON and the API itself doesn’t fail. The error codes associated with the messages are self-assumed.
The API is containerized, and a separate MySQL container is used. A docker-compose file is written to run the whole service.
To run the docker-compose, go the fibonacci-flask folder which contains the docker-compose.yaml file and run docker-compose up command. You can use the API with the IP of the host running the docker-compose on port 5000.
Brief explanation of endpoints:
•	/
If the user accesses only the IP of the Flask server, the decorator with (/) handler is used and the function landing gets called which returns the message in JSON to the user to use  /fib/{number} & /health endpoints to acquire data.

•	/fib/{number}
This endpoint returns data when a GET call is made to it with a number to calculate the combinations for. As soon as the call is made to it, a timestamp is saved which is used in logging the requests made to it. Then, the combinations are calculated and after that a call is made to the database to log the metadata about the request. The metadata saved consists of the timestamp when the request is received, the IP of the requestor, a status code and path of the request. On success, the combinations calculated are returned to the user and in case of a failure from the database side the error message is returned.

•	/health
This endpoint returns the condition of the API. If the database is available it returns a unique code and shows the message that API is working fine, otherwise the error message with an unique error code is returned.
When you open the fibonacci-flask folder you find 2 folders (code,db) and a docker-compose.yaml file. 
The “code” folder contains another folder “app” which contains all the python scripts, a Dockerfile which creates the image for our flask server and is required by the docker-compose.yaml file, and a requirements.txt file that is used by the Dockerfile to install the required python modules using pip.
The “db” folder contains an initialize.sql file that is required by the docker-compose.yaml file to create the database and tables when the MySQL container is run for the first time.
