from django.core.management.base import BaseCommand
from films.models import Movie

class Command(BaseCommand):
    help = "Заполняет базу тестовыми фильмами"

    def handle(self, *args, **kwargs):
        movies = [
            {"title": "Интерстеллар", "description": "Научная фантастика о межзвёздных путешествиях", "review": "Глубокий фильм с шикарной музыкой."},
            {"title": "Начало", "description": "Мир снов и сознания", "review": "Гениальный сюжет, заставляет думать."},
            {"title": "Матрица", "description": "Выбор между реальностью и иллюзией", "review": "Классика, не теряет актуальности."},
            {"title": "Зелёная миля", "description": "История, пробивающая до слёз", "review": "Настоящее кино о человечности."},
            {"title": "Остров проклятых", "description": "Детектив с поворотом", "review": "Финал разрушает шаблоны мышления."},
            {"title": "Форрест Гамп", "description": "Жизнь как коробка конфет", "review": "Трогательный, мудрый и вдохновляющий."}
        ]

        for movie in movies:
            Movie.objects.get_or_create(**movie)

        self.stdout.write(self.style.SUCCESS("✅ База данных успешно заполнена"))
