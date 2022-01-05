#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas"                                            , "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

NE_planimals= farms[0]["agriculture"]
W_planimals= farms[1]["agriculture"]
SE_planimals= farms[2]["agriculture"]

print("choose between the following farms: ")
for farm in farms:
        print("-",farm["name"])

choice= input(">").lower()

if choice == "ne farm":
     for keys in NE_planimals:
         print(keys)
        

elif choice == "w farm":
     for keys in W_planimals:
         print(keys)
        

elif choice == "se farm": 
     for keys in SE_planimals:
         print(keys)
      


