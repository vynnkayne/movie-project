import json
import requests

movies = {}  # Dictionary to store the movies data

def load_movies_from_file():
    global movies
    with open("movies.json", "r") as file:
        movies = json.load(file)

def save_movies():
    with open('movies.json', 'w') as file:
        json.dump(movies, file)

def list_movies():
    load_movies_from_file()
    for movie_title, movie_details in movies.items():
        print_movie_details(movie_details)

def add_movie(movie_title):
    API_KEY = "18abac91"
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&t={movie_title}"
    response = requests.get(url)
    data = response.json()
    if data['Response'] == 'True':
        movie = {
            'Title': data['Title'],
            'Rating': float(data['imdbRating']),
            'Year': int(data['Year']),
            'Poster': data['Poster']
        }
        movies[movie_title] = movie  # Update the dictionary with the correct key
        save_movies()  # Save the updated movies data
        print('Movie added successfully')
    else:
        print('Movie not found')

def delete_movie(movie_title):
    if movie_title in movies:
        del movies[movie_title]
        save_movies()
        print('Movie deleted successfully')
    else:
        print('Movie not found')

def update_movie(title, rating):
    if title in movies:
        movies[title]['rating'] = rating
        save_movies()
        print('Movie updated successfully')
    else:
        print('Movie not found')

def stats():
    load_movies_from_file()
    num_movies = len(movies)
    print('Total movies:', num_movies)
    highest_rated_movie = max(movies.values(), key=lambda x: x['Rating'])
    lowest_rated_movie = min(movies.values(), key=lambda x: x['Rating'])
    print('Highest rated movie:', highest_rated_movie['Title'])
    print('Lowest rated movie:', lowest_rated_movie['Title'])
    ratings = [movie['Rating'] for movie in movies.values()]
    avg_rating = sum(ratings) / num_movies
    print('Average rating:', avg_rating)
    sorted_movies = sorted(movies.values(), key=lambda x: x['Rating'], reverse=True)
    print('Movies sorted by rating:')
    for movie in sorted_movies:
        print_movie_details(movie)

def random_movie():
    load_movies_from_file()
    import random
    if movies:
        random_movie = random.choice(list(movies.values()))
        print('Random movie:')
        print_movie_details(random_movie)
    else:
        print('No movies in the database')

def search_movie(title):
    load_movies_from_file()
    found_movies = []
    for movie in movies.values():
        if title.lower() in movie['Title'].lower():
            found_movies.append(movie)

    if found_movies:
        print(f"{len(found_movies)} movie(s) found:")
        for movie in found_movies:
            print_movie_details(movie)
    else:
        print('No matching movies found')

def movies_sorted_by_rating():
    load_movies_from_file()
    sorted_movies = sorted(movies.values(), key=lambda x: x['Rating'], reverse=True)
    print('Movies sorted by rating:')
    for movie in sorted_movies:
        print_movie_details(movie)

def print_movie_details(movie):
    print(f"Title: {movie['title']}")
    print(f"Rating: {movie['rating']}")
    print(f"Year: {movie['year']}")
    print(f"Poster URL: {movie['poster']}")
    print(f"Plot: {movie['plot']}")
    print(f"Director: {movie['director']}")
    print(f"Actors: {movie['actors']}")

    # Display the movie poster
    if 'poster' in movie and movie['poster']:
        print("\nPoster:")
        print_movie_poster(movie['poster'])

def get_movie_details(movie_title):
    api_key = '18abac91'
    url = f"http://www.omdbapi.com/?apikey={api_key}&t={movie_title}"
    response = requests.get(url)
    if response.status_code == 200:
        movie_data = response.json()
        if movie_data['Response'] == 'True':
            title = movie_data['Title']
            rating = float(movie_data['imdbRating'])
            year = int(movie_data['Year'])
            return {'title': title, 'rating': rating, 'year': year}
        else:
            print('Movie not found')
    else:
        print('Error occurred while fetching movie details')

def print_movie_poster(poster_url):
    try:
        response = requests.get(poster_url)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        img.show()
    except (requests.exceptions.RequestException, IOError) as e:
        print("Error displaying movie poster:", e)
