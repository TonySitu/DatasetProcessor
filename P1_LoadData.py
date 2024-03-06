def load_dataset() -> dict:
    map_genre = {}

    with open("google_books_dataset.csv", "r") as dataset_file:
        next(dataset_file)

        for line in dataset_file:
            map_book: dict[str, str | float | int] = {}
            book_details = line.strip("\n").split(",")
            map_book["title"] = book_details[0]
            map_book["author"] = book_details[1]
            map_book["rating"] = book_details[2]
            map_book["publisher"] = book_details[3]
            map_book["pages"] = int(book_details[4])
            map_book["language"] = book_details[6]

            if map_book["rating"] != "N/A":
                map_book["rating"] = float(map_book["rating"])

            book_genre = book_details[5]
            if book_genre not in map_genre:
                map_genre[book_genre] = []

            if map_book not in map_genre[book_genre]:
                map_genre[book_genre].append(map_book)

    return map_genre


def main():
    print(load_dataset())


if __name__ == "__main__":
    main()
