import os
import json
import csv

def load_json(folder_path):
    json_data = []

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.json'):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "r") as f:
                json_data.append(json.load(f))

    return json_data

folder_user = (r"C:\Users\user\OneDrive\Desktop\projects\AltschoolAssessment\events\users")

folder_card = (r"C:\Users\user\OneDrive\Desktop\projects\AltschoolAssessment\events\cards")

users = load_json(folder_user)
cards = load_json(folder_card)






users_list = []
for user in users:
     user_dict = {
        "type": user["metadata"]["type"],
        "event_at": user["metadata"]["event_at"],
        "event_id": user["metadata"]["event_id"],
        "id": user["payload"]["id"],
        "name": user["payload"]["name"],
        "address": user["payload"]["address"],
        "job": user["payload"]["job"],
        "score": user["payload"]["score"]
        }
     users_list.append(user_dict)




cards_list = []
for card in cards:
    if card["payload"].get("user_id") is not None:
        card_dict = {
            "id": card["payload"]["id"],
                "user_id": card["payload"]["user_id"],
                "created_by_name": card["payload"]["created_by_name"],
                "updated_at": card["payload"]["updated_at"],
                "created_at": card["payload"]["created_at"],
                "active": card["payload"]["active"],
                "type": card["metadata"]["type"],
                "event_at": card["metadata"]["event_at"],
                "event_id": card["metadata"]["event_id"]
                }
        cards_list.append(card_dict)







# data to csv
with open('users.csv','w',newline='') as csv_file:
    fieldnames = users_list[0].keys()
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(users_list)    

# cards_list to csv
with open('cards.csv','w',newline='') as csv_file:
    fieldnames = cards_list[0].keys()
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(cards_list)   
