__author__ = 'Vijaysrinivas Rajagopal'

import os
from Snitch import JSONFetcher
from Snitch import FileAway
import  json


print("Small tool for retrieving your noobis- er, I mean, lasting memories of Battlefield Play4Free in the form of "
      "profile page data\n Created by: Medic_Alert\n\n Instructions: Type in either your nucleus ID"
      "for bulk download of every soldier in an account. Data will be downloaded in JSON format; logs will be created as"
      "well, and both will be zipped into a .rar file for any later retrieval.")
language = input("What language do you want your data to be encoded in? (ex. en for english):")
datagiven = input("Please type in nucleusID:")
instancer = JSONFetcher(datagiven)
instancer.language = language
uno = instancer.grabStarter()
writer = FileAway()
i = 0

with open("log.txt", "w") as rotter:
    z = 0
    for y in instancer.profileid:
        rotter.write("{0} = {1}\n".format(y, uno[z]['name']))
        z += 1

for x in instancer.profileid:
    writer.filename = x
    writer.WriteLeiter(instancer.grabMeat(i, "CoreStats"), "CoreStats")
    os.rename("./{0}_CoreStats.json".format(str(x)), "./{0}/{0}_CoreStats.json".format(str(x)))
    writer.WriteLeiter(instancer.grabMeat(i, "BadPlayerStats"), "BadPlayerStats")
    os.rename("./{0}_BadPlayerStats.json".format(str(x)), "./{0}/{0}_BadPlayerStats.json".format(str(x)))
    writer.WriteLeiter(instancer.grabMeat(i, "GameEventStats"), "GameEventStats")
    os.rename("./{0}_GameEventStats.json".format(str(x)), "./{0}/{0}_GameEventStats.json".format(str(x)))
    writer.WriteLeiter(instancer.grabMeat(i, "GameModeStats"), "GameModeStats")
    os.rename("./{0}_GameModeStats.json".format(str(x)), "./{0}/{0}_GameModeStats.json".format(str(x)))
    writer.WriteLeiter(instancer.grabMeat(i, "RushMapStats"), "RushMapStats")
    os.rename("./{0}_RushMapStats.json".format(str(x)), "./{0}/{0}_RushMapStats.json".format(str(x)))
    writer.WriteLeiter(instancer.grabMeat(i, "WeaponStats"), "WeaponStats")
    os.rename("./{0}_WeaponStats.json".format(str(x)), "./{0}/{0}_WeaponStats.json".format(str(x)))
    writer.WriteLeiter(instancer.grabMeat(i, "VehicleStats"), "VehicleStats")
    os.rename("./{0}_VehicleStats.json".format(str(x)), "./{0}/{0}_VehicleStats.json".format(str(x)))
    writer.WriteLeiter(instancer.grabMeat(i, "MapStats"), "MapStats")
    os.rename("./{0}_MapStats.json".format(str(x)), "./{0}/{0}_MapStats.json".format(str(x)))
    writer.WriteLeiter(instancer.grabMeat(i, "GameModeMapStats"), "GameModeMapStats")
    os.rename("./{0}_GameModeMapStats.json".format(str(x)), "./{0}/{0}_GameModeMapStats.json".format(str(x)))
    writer.WriteLeiter(instancer.grabloadout(i), "Loadout")
    os.rename("./{0}_Loadout.json".format(str(x)), "./{0}/{0}_Loadout.json".format(str(x)))
    i += 1

with open("Profile_SoldierInfo.json", 'w') as outfile:
    json.dump(uno, outfile)

writer.zipcreate(uno[0]['name'], instancer.profileid)

input("Enter any input to exit")

