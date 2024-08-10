# from math import cos, pi, radians

# function to find number of airships
def findAirships():
    thingsperDay = float(input("Things per day: "))
    tripsperDay = 11 # float(input("Trips per day: "))
    thingspertimetabledSlot = thingsperDay/tripsperDay
    thingaverageWeight = float(input("Average weight of thing: "))
    airshipweightLimit = float(input("Airship weight limit: "))

    """
    n is rounded up because if we need 1.4 
    airships, 1 is not enough and we cannot have 1.4
    therefore the lowest number of airships to match
    the demand is 2.
    """
    n = round(thingspertimetabledSlot*thingaverageWeight/airshipweightLimit + 0.5, 0)
    leftoverSpace = round((thingspertimetabledSlot*thingaverageWeight/(2*airshipweightLimit)*airshipweightLimit), 0)
    return (n, leftoverSpace)


while True:
    n, leftoverSpace = findAirships()
    print("You need", int(n), "airships and would have", leftoverSpace, "kilograms of spare space.")

