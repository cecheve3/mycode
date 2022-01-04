#!/usr/bin/env python3

char_name= input("Which character do you want to know about? (Flash, Batman, Superman): ")

char_stat= input("What stats do you want to know about? (strength, speed, intelligence): ")

super_dic= {"flash":{"speed": "fastest", "intelligence": "lowest", "strength": "lowest"}, "batman":{"speed": "slowest", "intelligence": "Highest", "strength": "Money"}, "superman":{"speed": "fast", "intelligence": "average", "strength": "strongest"}}

print(super_dic[char_name.lower()][char_stat.lower()])

 

