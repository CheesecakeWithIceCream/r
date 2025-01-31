totalMiles = 0
totaljourneycost = 0
journeyStage = ["A","B","C"]
costjourneystage = []
startMiles = int(input("What is the mileage at the start of the journey?: "))
nochargingStations = int(input("How many charging stations were visited"))
for x in range(nochargingStations):
    currentMiles = int(input("Enter current mileage: "))
    kwrating = int(input("Enter kw rating"))
    while kwrating != 7 and !=22 and !=50:
        print("Please input a valid kw rating")
        kwrating = int(input("Enter kw rating"))
    if kwrating == 7:
        pricePerMile = 0
    elif kwrating == 22:
        pricePerMile == 0.005
    else:
        pricePerMile = 0.01
    milesTravelled = currentMiles - startMiles
    startMiles = currentMiles
    journeystage = pricePerMile * milesTravelled
    costjourneystage.append(journeystage)
    
for x in range(nochargingStations):
    print(journeyStage[index])
    print(costjourneystage)
    totaljourneycost += costjourneystage[index]
    totalMiles += milesTravelled
print(round(totaljourneycost, 2))
print("You have travelled", totalMiles)
    

