import sqlite3
import os
import utils

DB_FILE = "volunteer_hub.db"

def init_db():
    """Инициализация таблиц базы данных."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Таблица заявок (задач)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            category TEXT NOT NULL,
            volunteer TEXT DEFAULT 'Не назначен',
            status TEXT DEFAULT 'Открыта',
            created_at TEXT
        )
    ''')
    
    # Таблица волонтеров
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS volunteers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            skills TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

# --- Логика работы с задачами ---

def add_task(title, category):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    date_now = utils.get_current_date()
    cursor.execute(
        "INSERT INTO tasks (title, category, created_at) VALUES (?, ?, ?)", 
        (title, category, date_now)
    )
    conn.commit()
    conn.close()

def get_all_tasks(status_filter="Все"):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    if status_filter == "Все":
        cursor.execute("SELECT id, title, category, volunteer, status, created_at FROM tasks")
    else:
        cursor.execute("SELECT id, title, category, volunteer, status, created_at FROM tasks WHERE status = ?", (status_filter,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_task_status(task_id, new_status, volunteer_name=None):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    if volunteer_name:
        cursor.execute(
            "UPDATE tasks SET status = ?, volunteer = ? WHERE id = ?", 
            (new_status, volunteer_name, task_id)
        )
    else:
        cursor.execute(
            "UPDATE tasks SET status = ? WHERE id = ?", 
            (new_status, task_id)
        )
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

# --- Логика работы с волонтерами ---

def add_volunteer(name, phone, skills):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO volunteers (name, phone, skills) VALUES (?, ?, ?)", 
        (name, phone, skills)
    )
    conn.commit()
    conn.close()

def get_all_volunteers():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, phone, skills FROM volunteers")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_volunteer(vol_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM volunteers WHERE id = ?", (vol_id,))
    conn.commit()
    conn.close()
