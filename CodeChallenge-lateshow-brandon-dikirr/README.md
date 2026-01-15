# CodeChallenge-LateShow
-This project is a Flask REST API that models episodes of The Late Show, their guests, and guest appearances. It is built to be fully compatible with the provided Postman collection.

## Tech Stack

 .Python 3.10+

 .Flask

 .Flask-SQLAlchemy

 .Flask-Migrate

 .SQLAlchemy-Serializer

 .SQLite

## Database Models
.Episode
.Guest
.Appearance
.Relationships

 ## API Endpoints
GET /episodes

Returns a list of all episodes.

GET /episodes/:id

Returns a specific episode and its appearances.

DELETE /episodes/:id

Deletes an episode and all related appearances.

Success response: 204 No Content

GET /guests

Returns a list of all guests.

POST /appearances

Creates a new appearance.

## How to Run the Application
1️. Clone the Repository
2.Install Dependencies with Pipenv
3.Activate the Virtual Environment
4.Set Flask Environment Variables
5.Run Database Migrations
6.Seed the Database
7.Start the Server

## Author

 Brandon Dikirr

 ## License

 This project is licensed