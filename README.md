# [late update: since `Battlefield Play4Free` has shut down, this service is of no use anymore]
------
# Aurevoir - P4F JSON Fetcher

Since P4F's services are going down on July 14th, I quickly created my last mini-project for it. Aurevoir fetches majority of the well known JSON files that power the P4F Profile Pages.

###What is being fetched:
- Initial User Info - /profile/soldiers/...
- Profile Pages - /profile/stats/...
    - [%22GameEventStats%22]
    - [%22CoreStats%22]
    - [%22BadPlayerStats%22]
    - [%22GameModeStats%22]
    - [%22VehicleStats%22]
    - [%22MapStats%22]
    - [%22GameModeMapStats%22]
    - [%22RushMapStats%22]
    - Loadout - /profile/stats/loadout...

###How to use Aurevoir:
You can download the latest stable build in my GitHub repo, and place the two python files (Snitch.py and Kommunity.py) as well as this README file in whatever directory you wish. Run the Kommunity script by either running it through a python shell or double-clicking it in order to open the shell automatically.

The rest is very simple. The script will ask you for a P4F-supported language (EN, DE, PL, etc.) and then ask you for the nucleusID of your account, which you can find by going to your profile page and looking for the first 10-stringed number. This ID exposes your profileIDs (profileIDs are childrens of a nucleusID, usually containing the specific information of each character).

> battlefield.play4free.com/[language abbrevation]/profile/[nucleusID]/[profileID]

The resulting fetches will be placed in a zip file named after the first profileID captured (Not always the main soldier).

###Requirements:
- Machine that runs Python 3.4 or higher
- Internet connection (hopefully better than mine)
- A keyboard, maybe
- Doing this before the service shuts down  :-)

###Known Issues:
- Zip file is not named after main soldier, rather the first profileID's data presented in output
- Does not handle false language abbrevations and nucleusIDs gracefully
- WILL crash if the same data files are present (result of requesting the same account twice without removing either of them)
- Has not been tested on Mac or Linux distro
- Has not been tested to be ran multiple times at the same moment
- Does not gracefully handle network hiccups other than native exceptions

###To-Do:
- Capture my own profile data for gloating in the near future
- Maybe create a HTML generator to display JSON data all fancy-like
