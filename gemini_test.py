import requests


url = "http://chatai.my-blog.uz/webhook/2af2f0a6-7106-473c-96d9-f1df92562289"
url1="http://localhost:5678/webhook/2af2f0a6-7106-473c-96d9-f1df92562289"


while True:
    session=input("session_id kiriting : ")
    message = input("Savol kiriting : ")
    # message="Savdoga chiqarilgan lotlar soni qancha"
    payload = {
        "message":message,
        "session_id":session
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url,auth=("chemical-industry", "ChemicalPass@123"),  headers=headers,json=payload)




    print("Javob:", response.json()['answer'])

    print("Query:", response.json()['query'])
