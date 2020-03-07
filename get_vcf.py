import json
import os
import requests
import pprint
import fileinput
import sys

URL = 'http://sbs:8100/'
# print(URL)



# Create session object, which can be used for all requests.
request_handle = requests.Session()

# Set up appropriate headers.
headers = {'Content-Type': 'application/json',
           'Accept': 'application/json'}

# Send the POST request, with your username & password, converted to json.
response = request_handle.post(os.path.join(URL, 'session'),
                               json={'username': 'USERNAME',
                                     'password': 'PASSWORD',
                                     },
                               headers=headers)

# Check that the response is OK.
if response.status_code == 200:
     # Add the authentication token to the headers.
     token = response.json().get('token')
     headers.update({'X-Token': token})
else:
     # View error messages.
     print (response.json())




for patient_name in fileinput.input():

    patient_name = patient_name.rstrip()
    response = request_handle.get(os.path.join(URL, 'somatic'), params={'patient': patient_name, 'production': True, 'analysis_type': 'strelka'}, headers=headers).json()

    print(response)

    # for library in response:
    #     for libcore in library['libcores']:


    # for foobar in response:
    #    keys = foobar.keys()
    #    for key in keys:
    #        print("\t".join([str(key), str(foobar[key])]))
    #
    #    print("\n")


