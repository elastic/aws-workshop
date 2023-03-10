import requests
import time
import logging
import random
import threading

def generate_random_ip():
    # Generate a random IP address in the form xxx.xxx.xxx.xxx
    # where xxx is a number between 0 and 255
    return ".".join([str(random.randint(0, 255)) for _ in range(4)])

def execute_request(data, headers):
    logging.warning("starting!")
    response = requests.post("http://localhost:5002/add-item", json=data, headers=headers)
    logging.warning(response)

n = 0

while True:
    # Make a POST request to the specified URL
    print(n)
    n = n+1
    number = "%05d" % random.randint(0,10)
    data = {"item": { "name": "test" + str(number)}, "id": 1 }
    headers = {'X-Real-IP': generate_random_ip()}
    
    x = threading.Thread(target=execute_request, args=(data,headers))
    x.start()
    
    # create spike every N seconds for specific country
    if(n > 300):
        print("spike starting")
        n = 0
        headers = {'X-Real-IP': "213.30.114.42"}
        data = {"item": { "name": "hack0r", "id": n }}
        for x in range(100):
            x = threading.Thread(target=execute_request, args=(data,headers))
            x.start()
        print("spike done")
    time.sleep(1)