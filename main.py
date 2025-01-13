from flask import Flask, request, jsonify, send_from_directory
from exa_py import Exa

# Initialize Flask app
app = Flask(__name__, static_folder='web', static_url_path='')

exa = Exa('2fb28497-10f9-413a-b263-9ac04ffa085f')

@app.route('/')
def index():
    # Serve the HTML file
    return send_from_directory('web', 'index.html')
@app.route('/search', methods=['POST'])
def search():
    query = request.json.get('query')
    if not query:
        return jsonify({'error': 'No query provided'}), 400

    # Execute search for different sources
    instagram_results = exa.search(query, num_results=10, type='keyword', include_domains=['https://www.instagram.com/'])
    youtube_results = exa.search(query, num_results=10, type='keyword', include_domains=['https://www.youtube.com/'])
    tweets_results = exa.search(query, num_results=10, type='keyword', include_domains=['https://twitter.com/'])
    web_results = exa.search(query, num_results=10, type='keyword', include_domains=[])

    # Organize the results by category
    results = {
        'instagram': [{'title': result.title, 'url': result.url} for result in instagram_results.results],
        'youtube': [{'title': result.title, 'url': result.url} for result in youtube_results.results],
        'tweets': [{'title': result.title, 'url': result.url} for result in tweets_results.results],
        'webpages': [{'title': result.title, 'url': result.url} for result in web_results.results]
    }
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)

# @app.route('/')
# def index():
#     # Serve the HTML file
#     return send_from_directory('web', 'index.html')

# @app.route('/search', methods=['POST'])
# def search():
#     # Get the search query from the request
#     data = request.json
#     query = data.get('query')

#     if not query:
#         return jsonify({"error": "No query provided"}), 400

#     try:
#         # Perform the search using Exa
#         response = exa.search(
#             query,
#             num_results=5,
#             type='keyword',
#             include_domains=['https://www.instagram.com/'],
#         )

#         # Prepare the results to send back to the frontend
#         results = [
#             {"title": result.title, "url": result.url}
#             for result in response.results
#         ]
#         return jsonify(results)

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)


# response = exa.search(query, num_results = 10)

# response = exa.search(
#     'best pizza in brooklyn',
#     num_results = 5,
#     start_published_date = '2024-05-02',
#     category = 'tweet',
#     use_autoprompt = True,
# )

# Search from Instareels
# response = exa.search(
#     query,
#     num_results = 5,
#     type = 'keyword',
#     include_domains = ['https://www.instagram.com/'],
# )

# # print(response)

# for result in response.results:
#     print(f'Title: {result.title}')
#     print(f'URL: {result.url}')
#     print()