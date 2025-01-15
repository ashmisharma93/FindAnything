# FindAnything
This repo consists a basic project on creating a Search Engine Website using Exa API.
Exa is an API that is used to search the content that best matches with the user's input unlike Google which matches the keywords from the user's input and the available web content.
Exa uses LLM model (Large Language Models) which is an artificial intelligence model that interprets and translates human-like text in various languages.
This project enables users to retrieve links based on their query from a variety of sources, including YouTube links, Instagram reels, X posts, and webpages.
 
The main.py file serves as the backend logic for your custom search engine. Here's what it does step by step:

Primary Functionality of main.py:
1) Sets up the Flask Web Server:
It initializes a Flask application that runs a web server, handling HTTP requests from the front end (HTML, CSS, and JavaScript files).
It serves the index.html file when the user visits the root route (/).

2) Handles Search Queries:
It listens for search requests sent from the front-end form (via JavaScript).
Upon receiving a search query, it interacts with the Exa API or any other search API to fetch relevant results for the query.

3) Processes API Results:
It structures the results received from APIs into sections (Instagram, YouTube, tweets, and general web links).
The results are returned to the front end as a JSON response.

4) Facilitates Communication Between Front End and API:
Acts as a middleman between the front-end interface (what the user interacts with) and the external services (like Exa or other APIs).
Converts user inputs into API requests and processes the responses to provide meaningful outputs to the user.


Project Structure: web Folder
The web folder contains the front-end files that power the user interface of the search engine website. Here's a breakdown:

1) index.html

Acts as the main entry point for the search engine website.
Structure includes:
 - A search bar for user queries.
 - Sections to display categorized results (e.g., Instagram, YouTube, tweets, and webpages).
 - A visually appealing header with the title "Find Anything".
 
2) styles.css
   
Provides the styling for the website to ensure it is aesthetically pleasing and user-friendly.
Key features:
 - Elegant fonts, smooth transitions, and a gradient background.
 - Custom styling for search results sections and hover effects.
 - Integration of the "Birthstone" font for an elegant touch.
   
3) script.js

Contains the JavaScript logic to dynamically interact with the backend and display results.
Key functionalities:
 - Sends the search query from the front end to the backend (main.py) via an API call.
 - Processes and updates the categorized results dynamically without refreshing the page.
 - Handles errors gracefully to improve user experience.
