from code02_searching.models.movie import Movie
from code02_searching.models.movie_collection import MovieCollection
from code02_searching.services.movie_reader import MovieReader
import os

def main():
    print(os.getcwd()) 
    # Membuat objek pembaca CSV
    reader = MovieReader("src/code02_searching/Trending_movies.csv")

    # Membaca CSV menjadi list object Movie
    movies = reader.read_movies()

    # Membuat koleksi movie
    collection = MovieCollection(movies)

    # Menampilkan semua movie
    collection.show_all()

    # Mencari film bahasa Inggris
    print("\nMovie English:")
    english_movies = collection.find_by_language("en")

    for movie in english_movies:
        print(movie)

    # Film dengan rating tertinggi
    print("\nHighest Rating:")
    highest = collection.get_highest_rating()
    print(highest)

if __name__ == "__main__":
    main()