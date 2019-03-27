import re

cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models (original order)"""
    
    jeeps = ""
    numJeeps = len(cars['Jeep'])
    iCounter = 0

    for jeep in cars['Jeep']:
        iCounter += 1
        jeeps += jeep
        if(iCounter < numJeeps):
            jeeps += ", "
    
    print(jeeps)

    return jeeps

def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    returnList = list()
    
    for make in cars:
        returnList.append(cars[make][0])
    
    print(returnList)

    return returnList
    


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    
    matchesList = list()
    
    for models in cars.values():
        for model in models:
            if(re.search(grep, model, re.I)):
                matchesList.append(model)
    
    print(matchesList)

    return matchesList


def sort_car_models(cars=cars):
    """sort the car models (values) and return the resulting cars dict"""
    for _ in cars.keys():
        cars[_] = sorted(cars[_])
    
    print(cars)

    return cars


"""
get_all_jeeps()
get_first_model_each_manufacturer()
"""
sort_car_models()