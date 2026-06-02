import os
import csv
from datetime import datetime

def validate_text(text, min_length=3):
    """Проверка текста: не пустой ли он и достаточной ли длины."""
    if not text or len(text.strip()) < min_length:
        return False
    return True

def validate_phone(phone_str):
    """
    Очищает строку от лишних символов и проверяет длину номера.
    Возвращает кортеж: (статус_проверки, очищенный_номер).
    """
    cleaned = ''.join(filter(str.isdigit, phone_str))
    if 10 <= len(cleaned) <= 12:
        # Форматируем номер для красоты
        return True, f"+{cleaned}" if len(cleaned) > 10 else cleaned
    return False, ""

def get_current_date():
    """Возвращает текущую дату в строковом формате."""
    return datetime.now().strftime("%Y-%m-%d %H:%M")

def export_to_csv(data, filename="Volunteer_Report.csv"):
    """
    Экспортирует переданные данные (список кортежей) в CSV файл.
    Пытается сохранить на Рабочий стол через модуль os.
    """
    try:
        # Пытаемся найти путь к рабочему столу
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        filepath = os.path.join(desktop, filename)
    except Exception:
        # Если не вышло (например, на Linux/Mac), сохраняем в папку со скриптом
        filepath = filename

    try:
        with open(filepath, mode='w', encoding='utf-8-sig', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(["ID", "Описание задачи", "Категория", "Ответственный", "Статус", "Дата создания"])
            for row in data:
                writer.writerow(row)
        return True, filepath
    except Exception as e:
        return False, str(e)
