import csv
from istorage import IStorage

class StorageCsv(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def list_movies(self):
        movies = {}
        with open(self.file_path, "r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                movie_title = row["title"]
                movie_info = {
                    "rating": float(row["rating"]),
                    "year": int(row["year"])
                }
                movies[movie_title] = movie_info
        return movies

    def add_movie(self, title, year, rating, poster):
        with open(self.file_path, "a", newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([title, str(rating), str(year)])

    def delete_movie(self, title):
        rows = []
        with open(self.file_path, "r") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row[0] != title:
                    rows.append(row)
        with open(self.file_path, "w", newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(rows)

    def update_movie(self, title, rating):
        rows = []
        with open(self.file_path, "r") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row[0] == title:
                    row[1] = str(rating)
                rows.append(row)
        with open(self.file_path, "w", newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(rows)
