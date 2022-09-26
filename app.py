#Libraries Start
import requests
#Libraries End


#Main Function Start
if __name__=="__main__":
    req = requests.get("https://rezafarazi.github.io/Online_Json_Api/sorapp_posts.json")
    print(req.text)
#Main Function End