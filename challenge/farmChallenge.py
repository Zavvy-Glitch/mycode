#!/usr/bin/python3

""" TLG Cohort D23 | CChea
    Practice looping data """


def main():

    # farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
    #     {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
    #     {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

    farms = [{"name": "Southwest Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "Northeast Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "East Farm", "agriculture": ["bananas", "apples", "oranges"]},
         {"name": "West Farm", "agriculture": ["pigs", "chickens", "llamas"]}]


    undesirables = ["carrots", "celery"]

    #NE_animals = farms[0]["agriculture"]

    #for i in NE_animals:
    #    print(i)

    for farm in farms:
        print("-->", farm["name"])
    selection = input("Choose which farm to take an animal from\n")

    for farm in farms:
        if farm["name"].lower() == selection.lower():
            for animal in farm["agriculture"]:
                if animal not in undesirables:
                    print(animal)

main()
