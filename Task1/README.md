Name of the project: Invitations

Name of the app used: list_friends

URLs used:

	/admin: Admin login.
			Login credentials - Username: Madhu 
				            Password: randompassword

	/list_friends/: Dummy site. Prompts you to go to input.

	/list_friends/input/: Has a text field and a button. User can input latitude, longitude and distance divided by a space

	/list_friends/input/result: Automatically redirected to this page once the button in /list_friends/input is
				    pressed. Shows list of people who are within the necessary distance sorted based on user_id.

	Note: The latitude/longitude distance conversion to km has been done using the following calculation:
		  latitude: 1 deg = 110.574 km
		  longitude: 1 deg = 111.320*cos(latitude) km

		  Source: https://stackoverflow.com/questions/1253499/simple-calculations-for-working-with-lat-lon-km-distance

Other notes:

1) I used python manage.py shell to input values into the database. I stored the JSON file contents in a variable called "everything" and used the following code:

from list_friend.models import Friend

everything = [{....},{....},......]

for person in everything:
	a=Friend(name=person["name"],latitude=person["latitude"],longitude=person["longitude"],user_id=person["user_id"])
	a.save()

2) sudo fuser -k 8000/tcp is a useful command to kill all processes on port 8000


Further work:
* Create three seperate text fields for latitude, longitude, distance.
* Use a cleaner way to move between different views.
