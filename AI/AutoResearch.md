**AutoResearch** от Андрея Карпатого — ==это проект с открытым исходным кодом, который автоматизирует научный метод в машинном обучении и других задачах, превращая его в автономный цикл «исследователь-ИИ»==. [[1](https://habr.com/ru/news/1008390/), [2](https://vc.ru/ai/2798012-autoresearch-ii-dlya-optimizatsii-protsessov-vo-sne)]

Основной смысл заключается в том, чтобы передать ИИ-агенту (например, Claude или Codex) задачу по улучшению кода или модели, предоставив ему возможность самостоятельно проводить сотни экспериментов, сохраняя только те, которые улучшают метрики. [[1](https://www.youtube.com/watch?v=5-ekc3eXNvs&t=10), [2](https://www.ixbt.com/news/2026/03/11/ii-nachal-sam-provodit-nauchnye-jeksperimenty-platforma-autoresearch-ot-andreja-karpaty-sama-avtomatiziruet-uluchshenie.html)]

В чём смысл AutoResearch

1. **Автономный цикл (Loop):** ИИ сам формулирует гипотезу, вносит изменения в код, запускает обучение/эксперимент, оценивает результат и решает, оставить изменения или откатиться к предыдущей версии.
2. **Исключение человека:** Исследователь не вмешивается в процесс. Вы настраиваете среду, запускаете её, и за ночь ИИ может провести сотни экспериментов.
3. **Фиксированный бюджет и метрика:** Каждый эксперимент ограничен по времени (например, 5 минут), что делает результаты сравнимыми. ИИ ориентируется на один четкий показатель (например, минимальная ошибка валидации), что исключает субъективность.
4. **«Умный» поиск улучшений:** Это не просто перебор параметров, а понимание кода агентом. Агент меняет архитектуру нейросети, оптимизаторы или гиперпараметры, используя свои знания. [[1](https://github.com/karpathy/autoresearch), [2](https://www.youtube.com/watch?v=bc4NrE0cOE0), [3](https://www.datacamp.com/es/tutorial/guide-to-autoresearch), [4](https://vc.ru/ai/2798012-autoresearch-ii-dlya-optimizatsii-protsessov-vo-sne), [6](https://www.ixbt.com/news/2026/03/11/ii-nachal-sam-provodit-nauchnye-jeksperimenty-platforma-autoresearch-ot-andreja-karpaty-sama-avtomatiziruet-uluchshenie.html)]

Как это устроено (3 ключевых файла)

- `program.md` — файл, в котором вы (человек) определяете цель, ограничения и направления исследований.
- `train.py` — файл, который редактирует ИИ (содержит модель и логику обучения).
- `prepare.py` — файл, который ИИ **не может** менять. Он готовит данные и считает метрику (оценку). [[1](https://www.reddit.com/r/LocalLLaMA/comments/1rowp28/karpathy_autoresearch/?tl=ru), [2](https://www.youtube.com/watch?v=uBWuKh1nZ2Y), [3](https://github.com/karpathy/autoresearch)]

Как это можно использовать

Autoresearch можно применять там, где можно четко измерить результат:

- **Оптимизация ML-моделей:** Карпатый изначально создал его для улучшения тренировки маленьких GPT-моделей. Агент может находить лучшие архитектуры или гиперпараметры.
- **Оптимизация кода:** Улучшение работы алгоритмов, скриптов обработки данных, поиск багов.
- **Маркетинг и контент (за пределами ML):** Можно настроить агент для изменения текста писем (cold email), структуры посадочных страниц или SEO-заголовков, если есть система оценки конверсии.
- **Автоматизация ИИ-агентов:** Применение для «самоулучшения» (Self-improving AI) — когда агент, генерирующий код, сам же анализирует свои ошибки и улучшает свой промпт или логику. [[1](https://www.youtube.com/watch?v=DqjJNGheOvg&t=15), [2](https://www.mindstudio.ai/blog/karpathy-autoresearch-pattern-marketing-automation), [4](https://vc.ru/ai/2798012-autoresearch-ii-dlya-optimizatsii-protsessov-vo-sne), [5](https://www.datacamp.com/es/tutorial/guide-to-autoresearch)]

Как запустить

1. **Скачать репозиторий:** `karpathy/autoresearch` с GitHub.
2. **Настроить окружение:** Нужна видеокарта NVIDIA и установленный `uv` (пакетный менеджер Python).
3. **Запустить агента:** Подключить Claude/Codex к репозиторию и дать инструкцию: «Посмотри `program.md` и начни эксперименты». [[1](https://github.com/karpathy/autoresearch)]