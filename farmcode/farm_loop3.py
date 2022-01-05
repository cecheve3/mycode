#!/usr/bin/env python3


farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas"                                           , "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

trash= ["carrots", "celery"]

NE_Farm= farms[0]["agriculture"] 
W_Farm= farms[1]["agriculture"]
SE_Farm= farms[2]["agriculture"]


print("choose: ")
for farm in farms:
    print("-",farm["name"])
choice= input(">").lower()

if choice == "ne farm":
    for keys in NE_Farm:
        print(keys)

elif choice == "w farm":
    for keys in W_Farm:
        print(keys)

elif choice == "se farm":
    for keys in SE_Farm:
        if keys not in trash:
            print(keys)

