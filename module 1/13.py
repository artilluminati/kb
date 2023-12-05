import random

films = {
    "Побег из Шоушенка": "Драма",
    "Зеленая миля": "Драма",
    "Властелин колец: Возвращение короля": "Фэнтези",
    "Интерстеллар": "Научная фантастика",
    "Бойцовский клуб": "Драма",
    "Звёздные войны: Эпизод IV – Новая надежда": "Фантастика",
    "Крестный отец": "Криминальный",
    "Матрица": "Фантастика",
    "Список Шиндлера": "Драма",
    "Бриллиантовая рука": "Комедия"
}



def film_recommendation(films, genre):
    genre_films = [film for film, film_genre in films.items() if film_genre.lower() == genre.lower()]
    if genre_films:
        recommended_film = random.choice(genre_films)
        return recommended_film
    else:
        return "Извините, фильмов в данном жанре нет."

genre = input("Введите жанр фильма: ")
recommendation = film_recommendation(films, genre)
print(recommendation)

