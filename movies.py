import shutil

def main():
    while True:
        print('********** My Movies Database **********')
        print('Menu:')
        print('1. List Movies')
        print('2. Add Movie')
        print('3. Delete Movie')
        print('4. Update Movie')
        print('5. Stats')
        print('6. Random Movie')
        print('7. Search Movie')
        print('8. Movies sorted by rating')
        print('9. Generate Website')
        print('0. Exit')
        choice = input('Enter choice (0-9): ')

        if choice == '1':
            movie_storage.list_movies()

        elif choice == '2':
            movie_name = input('Enter a movie name: ')
            movie_storage.add_movie(movie_name)
            print('Movie added successfully')

        elif choice == '3':
            movie_name = input('Enter a movie name: ')
            movie_storage.delete_movie(movie_name)

        elif choice == '4':
            movie_name = input('Enter a movie name: ')
            rating = float(input('Enter a new rating (between 1-10): '))
            movie_storage.update_movie(movie_name, rating)
            print('Movie updated successfully')

        elif choice == '5':
            movie_storage.stats()

        elif choice == '6':
            movie_storage.random_movie()

        elif choice == '7':
            search_query = input('Enter a movie name or part of a movie name: ')
            movie_storage.search_movie(search_query)

        elif choice == '8':
            movie_storage.movies_sorted_by_rating()

        elif choice == '9':
            generate_website()

        elif choice == '0':
            print('Bye!')
            break

        else:
            print('Invalid choice. Pick a number between 0-9')

def generate_website():
    template_file = "index_template.html"
    output_file = "index.html"

    with open(template_file, "r") as file:
        template = file.read()

    title = "My Movie App"
    movie_grid = generate_movie_grid()

    template = template.replace("__TEMPLATE_TITLE__", title)
    template = template.replace("__TEMPLATE_MOVIE_GRID__", movie_grid)

    with open(output_file, "w") as file:
        file.write(template)

    print("Website was generated successfully.")

def generate_movie_grid():
    movie_storage.load_movies_from_file()
    movies = movie_storage.movies

    movie_details = ""
    for movie in movies.values():
        movie_details += f"<li><strong>Title:</strong> {movie['Title']}</li>"
        movie_details += f"<li><strong>Rating:</strong> {movie['Rating']}</li>"
        movie_details += f"<li><strong>Year:</strong> {movie['Year']}</li>"
        movie_details += f"<li><strong>Poster:</strong> <img src='{movie['Poster']}'></li>"
        movie_details += "<br>"

    return movie_details

if __name__ == "__main__":
    main()


