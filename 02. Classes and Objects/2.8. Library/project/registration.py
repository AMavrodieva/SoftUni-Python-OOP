class Registration:
    def __init__(self):
        pass

    def add_user(self, user, library):
        if user in library.user_records:
            return f'User with id = {user.user_id} already registered in the library!'
        library.user_records.append(user)

    def remove_user(self, user, library):
        if user not in library.user_records:
            return f'We could not find such user to remove!'
        library.user_records.remove(user)

    def change_username(self, user_id: int, new_username: str, library):
        for user in library.user_records:
            if user.user_id == user_id and user.username != new_username:
                old_name = user.username
                user.username = new_username
                if old_name in library.rented_books:
                    library.rented_books[new_username] = library.rented_books[old_name]
                    library.rented_books.pop(new_username)
                return f'Username successfully changed to: {new_username} for user id: {user_id}'
            if user.user_id == user_id and user.username == new_username:
                return f'Please check again the provided username - ' \
                       f'it should be different than the username used so far!'
        return f'There is no user with id = {user_id}!'
