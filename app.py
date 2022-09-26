#Libraries Start
import requests
import json
#Libraries End


#Get Use Json Function Start
def GetData(js):
    data=json.loads(js)
    for item in data:
        print("id is ", item["Id"], " Title Is ",item["Title"]," Image Address is : ",item["Image"])
#Get Use Json Function End


#Main Function Start
if __name__=="__main__":
    req = requests.get("https://rezafarazi.github.io/Online_Json_Api/sorapp_posts.json")
    all_text=req.text
    GetData(all_text)
#Main Function End


