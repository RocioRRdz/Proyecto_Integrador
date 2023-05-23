## pip install requests   Fuente: https://pypi.org/project/requests/
import requests

url_base = "http://localhost:3000/api/v1-sensors/sensors"

def getAll_sensorInfo():
    #Get
    print("\nGET ALL SENSOR INFO: ")
    url = url_base + "/"
    response = requests.get(url)
    result = response.json()
    print(result) #diccionario ...
    print(response.status_code)

    #print("Table Info:")
    #for register in result:
        #for key in register:
            #print("Attribute: ", key, " Value: ", register[key])
        #print("\n")
###############################################################################################################################
def getAll_sensorRecords():
    # Get
    print("\nGET ALL RECORDS: ")
    url = url_base + "/records"
    response = requests.get(url)
    result = response.json()
    print(result)  # diccionario ...
    print(response.status_code)

    #print("Table Info:")
    #for register in result:
        #for key in register:
            #print("Attribute: ", key, " Value: ", register[key])
        #print("\n")
###############################################################################################################################
def getByID(id):
    #Get with parameters
    print("\nGET with parameters: ")
    url = url_base + "/{}".format(id)
    response = requests.get(url)
    result = response.json()
    print(result)  # diccionario ...
    print(response.status_code)

    #print("Value of Device: ", response.json())
    #print(response.status_code)
###############################################################################################################################
def insertRecord_wPost(id_sensor, current_value):
    #Post
    print("\nINSERT SENSOR RECORD:")
    #import json
    #Id_sensor = id_sensor
    #Current_value = current_value
    url = url_base + "/records"
    #headers =  {"Content-Type":"application/json"}
    general = {
        "Id_sensor": id_sensor,
        "Current_value": current_value
    }
    response = requests.post(url, json=general)
    result = response.json()
    print(result)
    print(response.status_code)
###############################################################################################################################
def insertNewSensor_wPost(name, id_owner, id_type):
    #Post
    print("\nINSERT NEW SENSOR: ")
    #Name = name
    #Id_owner = id_owner
    #Id_type = id_type
    url = url_base + "/"
    general = {
        "Name": name,
        "Id_owner": id_owner,
        "Id_type": id_type
    }
    response = requests.post(url, json=general)
    result = response.json()
    print(result)
    print(response.status_code)
###############################################################################################################################
def updateSensor_wPatch(id,name):
    # Post
    print("\nUPDATE SENSOR: ")
    #import json
    #Name = name
    url = url_base + "/{}"+format(id)
    #headers = {"Content-Type": "application/json"}
    general = {
        "Name": name
    }
    #response = requests.patch(url, data=json.dumps(body), headers=headers, verify=False)
    response = requests.patch(url, json=general)
    result = response.json()
    print(result)
    print(response.status_code)
###############################################################################################################################
def deleteSensor(id):
    #Delete
    print("\nDELETE SENSOR: ")
    url = url_base + "/{}".format(id)
    response = requests.delete(url)
    result = response.json() #It may not use because if "delete" returns void
    print(result)
    print(response.status_code)
###############################################################################################################################


#getAll_sensorInfo()
#getAll_sensorRecords()
#getByID(1)
#insertRecord_wPost(1, 10.5)
#insertNewSensor_wPost("Sensor1", 1)
#updateSensor_wPatch(1, "New Names")
#deleteSensor(1)






