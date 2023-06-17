from istorage import IStorage
import json

class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path
        self.movies = {}
        self.load_movies_from_file()

    def load_movies_from_file(self):
        with open(self.file_path, "r") as file:
            self.movies = json.load(file)

    def save_movies(self):
        with open(self.file_path, "w") as file:
            json.dump(self.movies, file)

    def list_movies(self):
        return self.movies

    def add_movie(self, title, year, rating, poster):
        movie = {
            'Title': title,
            'Rating': rating,
            'Year': year,
            'Poster': poster
        }
        self.movies[title] = movie
        self.save_movies()

    def delete_movie(self, title):
        if title in self.movies:
            del self.movies[title]
            self.save_movies()

    def update_movie(self, title, notes):
        if title in self.movies:
            self.movies[title]['notes'] = notes
            self.save_movies()
