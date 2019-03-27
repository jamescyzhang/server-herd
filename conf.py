# A configuration file for the Twisted Places proxy herd

# Google Places API key
API_KEY="AIzaSyCeKLnQ_GBbZUsKEoleKErpl3orNeZZAPw"
# Google Places Nearby API Endpoint
API_ENDPOINT="https://maps.googleapis.com/maps/api/place/nearbysearch/json?"

# TCP port numbers for each server instance (server ID: case sensitive)
# Please use the port numbers allocated by the TA.
PORT_NUM = {
    'Alice': 12860,
    'Bob': 12861,
    'Charlie': 12862,
    'David': 12863,
    'Erica': 12864
}

# Each Server can talk with other servers within the given 5, and we define
# a neighbor as a server another server can talk to. Note that this communication
# is bidirectional.
NEIGHBORS = {
	'Alice': ['Charlie', 'Erica'],
	'Bob': ['David', 'Erica'],
	'Charlie': ['David', 'Alice'],
	'Erica': ['Alice', 'Bob'],
	'David': ['Bob', 'Charlie']
}

PROJ_TAG="Fall 2018"
