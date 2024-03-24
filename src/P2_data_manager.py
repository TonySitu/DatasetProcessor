from P1_load_data import load_dataset


def get_books_by_category(map_genre: dict, genre: str) -> int:
    """
    Function returns the number of books associated by the defined
    genre given a dictionary that contains book details.

    :param map_genre: dictionary that contains keys of genres
    :param genre: genre to be counted
    :return: the number of books of defined genre
    """
    number_of_books = 0
    specified_genre_map = {}
    for book_dict in map_genre[genre]:
        number_of_books += 1
        specified_genre_map["Book {}".format(number_of_books)] = f"{book_dict['title']} by {book_dict['author']}"

    print("The genre", genre, "has", number_of_books, "books. This is the list of books:")
    for book_num, book in specified_genre_map.items():
        print(f"{book_num}: {book}")

    return number_of_books


def get_books_by_rating(map_genre: dict, rating: float) -> int:
    """
    Function returns number of books associated by the defined rating
    given a dictionary that contains book details

    :param rating: the rating of a book to find
    :param map_genre: dictionary that contains keys of genres
    :return:
    """
    def _rating_is_within_range(target_rating: float, given_rating) -> bool:
        """
        Function returns true if given rating is within a 0.5 difference of the
        target rating, and false otherwise.

        :param target_rating: the rating to be compared to
        :param given_rating: the rating that was given
        :return: true if given rating is within a 0.5 difference of target rating
        """
        return abs(given_rating - target_rating) <= 0.5

    number_of_books = 0
    specified_rating_map = {}
    title_pool = set()

    for book_list in map_genre.values():
        for book in book_list:
            if book["title"] not in title_pool and dict["rating"] != "N/A":     # dear god the nesting
                title_pool.add(book["title"])
                if _rating_is_within_range(rating, book["rating"]):
                    number_of_books += 1
                    title_pool.add(map_genre["title"])
                    specified_rating_map[f"Book {number_of_books}"] = f"{book['title']} by {book['author']}"

    print("There are", number_of_books, "books whose rating is between", str(rating-0.5), "and", str(rating+0.5),
          "This is the list of books:")

    for book_number, book_details, in specified_rating_map.items():
        print(f"{book_number}: {book_details}")

    return number_of_books

