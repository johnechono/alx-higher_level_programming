# Python - Network #1

This project involved learning how to use the `urllib` and `requests` Python
libraries to send and receive HTTP messages to URL's. I practiced sending `GET`
and `POST` requests, fetching JSON resources, and interacting with API's (the
Star Wars API, GitHub API, and Twitter API).
and `POST` requests, fetching JSON resources, and interacting with API's (the GitHub API).

## Tasks :page_with_curl:

@@ -63,47 +62,15 @@ Star Wars API, GitHub API, and Twitter API).
  `[<id>] <name>`.
  * Uses `requests`.

* **9. Star Wars API #0**
  * [9-starwars.py](./9-starwars.py): Python script sends a search request to
  the Star Wars API `people` endpoint with a given string.
  * Usage: `./9-starwars.py <search string>`
	* Displays the total number and `name` of each result.
	* Uses `requests`.

* **10. My Github!**
* **9. My Github!**
  * [10-my_github.py](./10-my_github.py): Python script that takes GitHub
  credentials (username and password) and uses the Github API to display the
  corresponding ID.
  * Usage: `./10-my_github.py <username> <password>`
	* Uses `requests`.

* **11. Time for an interview!**
* **10. Time for an interview!**
  * [100-github_commits.py](./100-github_commits.py): Python script that lists
  the 10 most recent comments of a given GitHub repository using the GitHub API.
  * Usage: `./100-github_commits.py <repository name> <owner name>`
	* Uses `requests`.

* **12. Star Wars API #1**
  * [101-starwars.py](./101-starwars.py): Python script that sends a search
  request to the Star Wars API `people` endpoint with a given string.
  * Usage: `./101-starwars.py <search string>`
	* Displays the total number and `name` of each result.
	* Manages pagination to display all results.
	* Uses `requests`.

* **13. Star Wars API #2**
  * [102-starwars.py](./102-starwars.py): Python script that sends a search
  request to the Star Wars API `people` endpoint with a given string.
  * Usage: `./102-starwars.py <search string>`
	* Displays the total number and `name` of each result as well as the list of
  films associated with each character.
	* Manages pagination to display all results.
	* Uses `requests`.

* **14. Twitter Auth**
  * [103-search_twitter.py](./103-search_twitter.py): Python script that sends
  a search request to the Twitter API `search` endpoint with a given string.
  * Usage: `./103-search_twitter.py <consumer key> <consumer secret> <search string>`
	* Displays the the top 5 results in the format
  `[<Tweet ID>] <Tweet text> by <Tweet owner name>`.
  * Uses `requests`.
	* Uses `requests`.
