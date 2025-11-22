import unittest
from main import Recomendation


class TestFuncs(unittest.TestCase):
    def test_rec(self):
        self.assertEqual(Recomendation().rec_film([1, 2, 3]), ['Человек паук', 'Унесенные призраками', 'Терминатор', 'Джанго освобожденный', 'Волк с Уолл-стрит', 'Гладиатор', 'Побез из шоушенга', 'Брат 2', 'Зеленая книга', 'Джентельмены', 'Властелин колец', 'Леон', 'Криминальное чтиво', 'Форрест гамп', 'Брат', 'Гнев человеческий', 'Зеленая миля'])
        self.assertEqual(Recomendation("films1.txt", "users1.txt").rec_film([2, 4]), ['Дюна', 'Мстители: Финал'])


if __name__ == "__main__":
    unittest.main()