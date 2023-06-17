class MovieApp:
    def __init__(self, storage):
        self._storage = storage

    def _command_list_movies(self):
        movies = self._storage.list_movies()
        # Implement the logic to display the list of movies
        ...

    def _command_movie_stats(self):
        # Implement the logic to display movie statistics
        ...

    def _generate_website(self):
        # Implement the logic to generate the website
        ...

    def run(self):
        while True:
            print("********** My Movies Database **********")
            print("Menu:")
            print("1. List Movies")
            print("2. Movie Stats")
            print("3. Generate Website")
            print("0. Exit")
            choice = input("Enter choice (0-3): ")

            if choice == "1":
                self._command_list_movies()
            elif choice == "2":
                self._command_movie_stats()
            elif choice == "3":
                self._generate_website()
            elif choice == "0":
                print("Bye!")
                break
            else:
                print("Invalid choice. Pick a number between 0-3")
