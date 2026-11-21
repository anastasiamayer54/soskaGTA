import os
from flask import Flask, render_template

base_dir = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(base_dir, 'templates'),
    static_folder=os.path.join(base_dir, 'static')
)

# Мультиплатформенная база данных нарезок (YouTube, VK, Rutube, Twitch, Direct MP4)
VIDEOS_DATA = [
    {
        "id": 1,
        "title": "Официальный Трейлер №1 GTA VI",
        "category": "trailers",
        "category_name": "Трейлер",
        "author": "Rockstar Games",
        "platform": "YouTube",
        "type": "iframe",
        "duration": "1:30",
        "views": "190M",
        "embed_url": "https://www.youtube.com/embed/QdBZY2fkU-0"
    },
    {
        "id": 2,
        "title": "Безумная погоня от вертолета и полиции",
        "category": "chases",
        "category_name": "Погони",
        "author": "ViceCityRacer",
        "platform": "Rutube",
        "type": "iframe",
        "duration": "0:45",
        "views": "120K",
        # Пример плеера Rutube
        "embed_url": "https://rutube.ru/play/embed/0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d/"
    },
    {
        "id": 3,
        "title": "Эпичный момент и перестрелка у пляжа",
        "category": "action",
        "category_name": "Перестрелки",
        "author": "VK_Gamer",
        "platform": "VK Видео",
        "type": "iframe",
        "duration": "0:50",
        "views": "85K",
        # Пример плеера VK
        "embed_url": "https://vk.com/video_ext.php?oid=-22822305&id=456239018&hash=a1b2c3d4e5f6"
    },
    {
        "id": 4,
        "title": "Реакция стримера на момент с машиной в GTA 6",
        "category": "stunts",
        "category_name": "Трюки",
        "author": "StreamerClip",
        "platform": "Twitch",
        "type": "iframe",
        "duration": "0:30",
        "views": "310K",
        # Пример плеера Twitch Clips
        "embed_url": "https://clips.twitch.tv/embed?clip=ATolerantKangarooPicoMause-example&parent=127.0.0.1"
    },
    {
        "id": 5,
        "title": "Прямая HD-нарезка физики катера на волнах",
        "category": "details",
        "category_name": "Детали",
        "author": "ViceCityClips",
        "platform": "Direct MP4",
        "type": "direct",
        "duration": "0:20",
        "views": "450K",
        # Прямая ссылка на MP4 файл
        "embed_url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4"
    },
    {
        "id": 6,
        "title": "Дрифт по ночному Ocean Drive",
        "category": "stunts",
        "category_name": "Трюки",
        "author": "NeonDrifter",
        "platform": "YouTube",
        "type": "iframe",
        "duration": "0:40",
        "views": "520K",
        "embed_url": "https://www.youtube.com/embed/f3Ssz32T_Gg"
    },
    {
        "id": 7,
        "title": "Ограбление магазина с Люсией",
        "category": "action",
        "category_name": "Перестрелки",
        "author": "LeonidaGamer",
        "platform": "Rutube",
        "type": "iframe",
        "duration": "1:05",
        "views": "210K",
        "embed_url": "https://rutube.ru/play/embed/0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d/"
    },
    {
        "id": 8,
        "title": "Побег от 5 звезд розыска",
        "category": "chases",
        "category_name": "Погони",
        "author": "PoliceEscape_VK",
        "platform": "VK Видео",
        "type": "iframe",
        "duration": "1:15",
        "views": "190K",
        "embed_url": "https://vk.com/video_ext.php?oid=-22822305&id=456239018&hash=a1b2c3d4e5f6"
    }
]

@app.route('/')
def index():
    return render_template('index.html', videos=VIDEOS_DATA)

if __name__ == '__main__':
    print("🚀 Сайт GTA 6 Vice City запущен на http://127.0.0.1:5000")
    app.run(debug=True, port=5000)