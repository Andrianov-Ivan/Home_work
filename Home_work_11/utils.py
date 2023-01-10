import json

"""Функция, которая загрузит данные из файла"""


def load_candidates():
    with open('candidates.json', 'r', encoding='utf-8') as f:  # открываем файл на чтение
        candidates = json.load(f)  # загружаем из файла данные
        return candidates


"""Функция, которая покажет всех кандидатов"""


def get_all():
    return load_candidates()


"""Функция, которая вернет кандидата по id"""


def get_candidates_by_id(id):
    for candidate in load_candidates():
        if candidate['id'] == id:
            return candidate
    return


"""Функция, которая вернет кандидата по имени"""


def get_candidates_by_name(name):
    candidates = []
    for candidate in load_candidates():
        if name.lower() in candidate['name'].lower():
            candidates.append(candidate)

    return candidates



"""Функция, которая вернет кандидатов по навыку"""


def get_candidates_by_skill(skill):
    candidates = []
    for candidate in load_candidates():
        skills = candidate["skills"].lower().split(', ')
        if skill in skills:
            candidates.append(candidate)
    return candidates
