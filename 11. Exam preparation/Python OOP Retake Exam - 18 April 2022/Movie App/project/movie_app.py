from project_unitest.user import User
from project_unitest.movie_specification.movie import Movie


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def check_user(self, username):
        for user in self.users_collection:
            if user.username == username:
                return True
        return False

    def check_movie(self, title):
        for movie in self.movies_collection:
            if movie.title == title:
                return True
        return False

    def register_user(self, username: str, age: int):
        if self.check_user(username):
            raise Exception("User already exists!")
        current_user = User(username, age)
        self.users_collection.append(current_user)
        return f'{username} registered successfully.'

    def upload_movie(self, username: str, movie: Movie):
        if not self.check_user(username):
            raise Exception("This user does not exist!")
        elif not movie.owner.username == username:
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')
        elif self.check_movie(movie.title):
            raise Exception("Movie already added to the collection!")
        else:
            for user in self.users_collection:
                if user.username == username:
                    user.movies_owned.append(movie)
                    self.movies_collection.append(movie)
                    return f'{username} successfully added {movie.title} movie.'

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if not movie.owner.username == username:
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')
        elif not self.check_movie(movie.title):
            raise Exception(f'The movie {movie.title} is not uploaded!')
        else:
            for element, value in kwargs.items():
                setattr(movie, element, value)
            return f'{username} successfully edited {movie.title} movie.'

    def delete_movie(self, username: str, movie: Movie):
        if not movie.owner.username == username:
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')
        elif not self.check_movie(movie.title):
            raise Exception(f'The movie {movie.title} is not uploaded!')
        else:
            self.movies_collection.pop(self.movies_collection.index(movie))
            for user in self.users_collection:
                if user.username == username:
                    user.movies_owned.pop(user.movies_owned.index(movie))
                    return f'{username} successfully deleted {movie.title} movie.'

    def check_if_user_liked_movie(self, username, movie_title):
        for user in self.users_collection:
            if user.username == username:
                for movie in user.movies_liked:
                    if movie.title == movie_title:
                        return True
                return False

    def like_movie(self, username: str, movie: Movie):
        if movie.owner.username == username:
            raise Exception(f'{username} is the owner of the movie {movie.title}!')
        elif self.check_if_user_liked_movie(username, movie.title):
            raise Exception(f'{username} already liked the movie {movie.title}!')
        else:
            for user in self.users_collection:
                if user.username == username:
                    user.movies_liked.append(movie)
                    movie.likes += 1
                    return f'{username} liked {movie.title} movie.'

    def dislike_movie(self, username: str, movie: Movie):
        if not self.check_if_user_liked_movie(username, movie.title):
            raise Exception(f'{username} has not liked the movie {movie.title}!')
        else:
            for user in self.users_collection:
                if user.username == username:
                    user.movies_liked.pop(user.movies_liked.index(movie))
                    movie.likes -= 1
                    return f'{username} disliked {movie.title} movie.'

    def display_movies(self):
        if len(self.movies_collection) == 0:
            return 'No movies found.'
        result_str = []
        for movie in sorted(self.movies_collection, key=lambda x: (-x.year, x.title)):
            result_str.append(movie.details())
        return '\n'.join(result_str)

    def __str__(self):
        users = ''
        movies = ''
        if len(self.users_collection) == 0:
            users += 'No users.'
        else:
            users += ", ".join([user.username for user in self.users_collection])
        if len(self.movies_collection) == 0:
            movies += 'No movies.'
        else:
            movies += ", ".join([movie.title for movie in self.movies_collection])
        return f'All users: {users}\nAll movies: {movies}'

