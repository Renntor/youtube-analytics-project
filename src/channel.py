import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб - канала"""
    # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
    api_key: str = os.environ.get('YT_API_KEY')

    # создать специальный объект для работы с API
    youtube = build('youtube', 'v3', developerKey = api_key)


    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала.
        Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

        self.title = self.youtube.channels().list \
            (id = self.channel_id, part = 'snippet,statistics').execute() \
            ['items'][0]['snippet']['title']

        self.description = self.youtube.channels().list \
            (id = self.channel_id, part = 'snippet,statistics').execute() \
            ['items'][0]['snippet']['description']

        self.url = 'https://www.youtube.com/channel/' + self.channel_id

        self.subscriber_count = self.youtube.channels().list \
            (id = self.channel_id, part = 'snippet,statistics').execute() \
            ['items'][0]['statistics']['subscriberCount']

        self.video_count = self.youtube.channels().list \
            (id = self.channel_id, part = 'snippet,statistics').execute() \
            ['items'][0]['statistics']['videoCount']

        self.view_count = self.youtube.channels().list \
            (id = self.channel_id, part = 'snippet,statistics').execute() \
            ['items'][0]['statistics']['viewCount']



    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.youtube.channels().list\
        (id = self.channel_id, part = 'snippet,statistics').execute()
        print(channel)


    def to_json(self, name: str) -> None:
        """
        Запись класса в файл
        """
        a = self.__dict__
        file = open(name, 'w')
        json.dump(a, file)
        file.close()



    @classmethod
    def get_service(cls):
        return cls.youtube


