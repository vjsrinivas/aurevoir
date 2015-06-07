__author__ = 'Vijaysrinivas Rajagopal'

from datetime import datetime
import urllib.request, urllib.error, json


class JSONFetcher:
    def __init__(self, nucleusid):
        self.language = "en"  # By default
        self.baseurl = "http://battlefield.play4free.com/"
        self.datecreated = str(datetime.now())
        self.nucleusid = nucleusid
        self.profileid = []

    def grabgeneric(self, url):
        """
        Retrieves data from a source and stores it in self.rawdata as a string for later parsing by jsonparse()
        :param url: Used to direct http.client for retrieval
        :return complete data or -1 (Error):
        """
        try:
            c = urllib.request.urlopen(url)
            return c.read().decode("utf-8")
        except (urllib.error.HTTPError, urllib.error.URLError, urllib.error.URLError, Exception) as e:
            print(e)
            return -1

    def jsonparse(self, rawdata):
        """
        Parses string data from self.rawdata into an array in self.jsondata.
        Call self.jsondata just like you would with a normal array
        :return Nothing:
        """
        try:
            return json.loads(rawdata)
        except(TypeError, KeyError, ValueError, Exception) as e:
            print(e)

    def grabStarter(self):
        url = self.baseurl + self.language + "/profile/soldiers/" + self.nucleusid
        interim = self.jsonparse(self.grabgeneric(url))
        for x in interim['data']:
            self.profileid.append(x['id'])
        return interim['data']

    def grabloadout(self, index):
        url = self.baseurl + self.language + "/profile/loadout/" + str(self.nucleusid) + "/" + str(self.profileid[index])
        interim = self.jsonparse(self.grabgeneric(url))
        return interim

    def grabMeat(self, index, type):
        url = "{0}{1}/profile/stats/{2}/{3}?g=[\"{4}\"]".format(self.baseurl, self.language, self.nucleusid,
                                                                self.profileid[index], type)
        return self.jsonparse(self.grabgeneric(url))


import zipfile
import os
import shutil


class FileAway:
    def __init__(self):
        self.filename = ""

    def WriteLeiter(self, jsoninput, datatype):
        datatype = "{0}_{1}.json".format(self.filename, datatype)
        with open(datatype, 'w') as outfile:
            json.dump(jsoninput, outfile)
        try:
            os.makedirs(str(self.filename))
        except OSError:
            return 1
        return 0

    def zipcreate(self, file, content):
        with zipfile.ZipFile("{0}.zip".format(file), 'w') as zipper:
            zipper.write("./Profile_SoldierInfo.json")
            for x in content:
                zipper.write("./{0}/{0}_CoreStats.json".format(x))
                zipper.write("./{0}/{0}_BadPlayerStats.json".format(x))
                zipper.write("./{0}/{0}_GameEventStats.json".format(x))
                zipper.write("./{0}/{0}_GameModeStats.json".format(x))
                zipper.write("./{0}/{0}_RushMapStats.json".format(x))
                zipper.write("./{0}/{0}_WeaponStats.json".format(x))
                zipper.write("./{0}/{0}_VehicleStats.json".format(x))
                zipper.write("./{0}/{0}_MapStats.json".format(x))
                zipper.write("./{0}/{0}_GameModeMapStats.json".format(x))
                zipper.write("./{0}/{0}_Loadout.json".format(x))
                shutil.rmtree("./{0}".format(x))
            zipper.write("./log.txt")
            os.remove("log.txt")
            os.remove("Profile_SoldierInfo.json")
        return 0
