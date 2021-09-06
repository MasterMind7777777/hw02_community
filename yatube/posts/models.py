from django.db import models
from django.contrib.auth import get_user_model

# Получаем модель пользователя.
User = get_user_model()


class Group(models.Model):
    """Модель сообществ в которые
       можно публиковать статьи"""
    # Название группы.
    title = models.CharField(max_length=200)
    # Читабельная ссылка.
    slug = models.SlugField(unique=True)
    # Описание.
    description = models.TextField()

    def __str__(self):
        """Значение выводимое при печати"""
        return self.title


class Post(models.Model):
    """Модель статьи в блоге."""
    # Текст статьи.
    text = models.TextField()
    # Дата публикации.
    pub_date = models.DateTimeField(auto_now_add=True)
    # Группа в которой будет опубликована статья(Опциолнално).
    group = models.ForeignKey(Group,
                              blank=True,
                              null=True,
                              on_delete=models.SET_NULL,)
    # Автор статьи.
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
