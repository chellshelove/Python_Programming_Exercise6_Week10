class Movie:
    def __init__(self, title, director, score):
        self.title = title
        self.director = director
        self.score = score

    def __str__(self):
        return f"Title: {self.title}, Director: {self.director}, Score: {self.score}"


# List of 5 movies
movies = [
    Movie("Inception", "Christopher Nolan", 8.8),
    Movie("Pulp Fiction", "Quentin Tarantino", 8.9),
    Movie("Parasite", "Bong Joon-ho", 8.6),
    Movie("The Grand Budapest Hotel", "Wes Anderson", 8.1),
    Movie("The Shape of Water", "Guillermo del Toro", 7.3)
]


# Get the director's name from the user
director_name = input("Enter the director's name: ")

# Filter movies by the specified director
director_movies = [movie for movie in movies if movie.director == director_name]

# Check if the director has movies in the list
if director_movies:
    # Find the highest-scoring movie of the director
    highest_scoring_movie = max(director_movies, key=lambda movie: movie.score)
    print("Highest-scoring movie by", director_name + ":")
    print(highest_scoring_movie)
else:
    # Print error message if no movies found for the director
    print(f"No movies found for director {director_name}.")