#Libraries Start
from tokenize import String
import requests
import json
#Libraries End


#Get Use Json Function Start
def GetData(js):
    data=json.loads(js)
    for item in data:
        print("id is ", item["Id"], " Title Is ",item["Title"]," Image Address is : ",item["Image"])
#Get Use Json Function End


#Catch Data Start
def Catch(data):
    with open("C:/Users/Rezafta/Desktop/python_request_test/catch.txt","w") as catch:
        catch.write("data")
        catch.close()
#Catch Data End


#Main Function Start
if __name__=="__main__":
    req = requests.get("https://rezafarazi.github.io/Online_Json_Api/sorapp_posts.json")
    all_text=req.text
    Catch(all_text)
    GetData(all_text)
#Main Function End


