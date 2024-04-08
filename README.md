# WorkIndia_Assignment
The steps to complete the task are:

1. Set up the Web Server and Database:
   i. Choose a suitable web server framework i.e. Python Flask.
   ii. Set up a MySQL database to store the required data.
2. Implement the Admin User Registration and Login:
   i. Create an endpoint for admin user registration, where the username, password, and email are captured.
   ii. Implement the login endpoint, where the username and password are validated, and a JWT access token is generated and returned upon successful login.
3. Implement the Match CRUD Operations:
   i. Create an endpoint to allow the admin user to add a new match, with details like team_1, team_2, date, and venue.
   ii. Implement an endpoint to fetch the list of all matches, which can be accessible by the guest user.
   iii. Create an endpoint to fetch the details of a specific match, which can be accessed by the guest user.
4. Implement the Team and Player Management:
   i. Create an endpoint to allow the admin user to add a player to a team's squad.
   ii. Implement an endpoint to fetch the player statistics, which can be accessed by the logged-in user.
5. Implement the Authorization and Authentication:
   i. Ensure that the admin-only endpoints (create match, add player) require the JWT access token in the Authorization header.
   ii. Implement the necessary middleware to validate the access token and authorize the user based on their role (admin or guest).
