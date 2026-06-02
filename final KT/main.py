import tkinter as tk
from tkinter import ttk, messagebox
import os
import database as db
import utils

class VolunteerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("ДоброКорг v2.0 — Координация социальных проектов")
        self.geometry("900x650")
        self.minsize(800, 500)
        
        # Проверяем и создаем БД через os и базу
        if not os.path.exists(db.DB_FILE):
            db.init_db()
            
        self.setup_ui()
        self.refresh_all_data()

    def setup_ui(self):
        """Настройка главного окна, меню и вкладок"""
        self.style = ttk.Style()
        self.style.theme_use("clam")
        
        self.build_menu()
        
        # Создаем менеджер вкладок
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Фреймы для вкладок
        self.tab_tasks = ttk.Frame(self.notebook)
        self.tab_add_task = ttk.Frame(self.notebook)
        self.tab_volunteers = ttk.Frame(self.notebook)
        self.tab_dashboard = ttk.Frame(self.notebook)
        
        # Добавляем вкладки в блокнот
        self.notebook.add(self.tab_tasks, text="📋 База заявок")
        self.notebook.add(self.tab_add_task, text="➕ Новая заявка")
        self.notebook.add(self.tab_volunteers, text="👥 Волонтеры")
        self.notebook.add(self.tab_dashboard, text="📊 Статистика")
        
        # Собираем интерфейс каждой вкладки
        self.build_tasks_tab()
        self.build_add_task_tab()
        self.build_volunteers_tab()
        self.build_dashboard_tab()

    def build_menu(self):
        """Создание верхнего меню (Файл, Помощь)"""
        menubar = tk.Menu(self)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Экспорт заявок в CSV", command=self.export_data)
        file_menu.add_separator()
        file_menu.add_command(label="Выход", command=self.on_exit)
        menubar.add_cascade(label="Файл", menu=file_menu)
        
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="О программе", command=self.show_about)
        menubar.add_cascade(label="Помощь", menu=help_menu)
        
        self.config(menu=menubar)

    def build_tasks_tab(self):
        """Сборка вкладки управления задачами"""
        # Панель инструментов
        toolbar = ttk.Frame(self.tab_tasks, padding=10)
        toolbar.pack(fill="x")
        
        ttk.Label(toolbar, text="Фильтр:").pack(side="left", padx=5)
        self.cmb_filter = ttk.Combobox(toolbar, values=["Все", "Открыта", "В процессе", "Завершена"], state="readonly")
        self.cmb_filter.current(0)
        self.cmb_filter.pack(side="left", padx=5)
        self.cmb_filter.bind("<<ComboboxSelected>>", lambda e: self.refresh_tasks())
        
        ttk.Button(toolbar, text="🔄 Обновить", command=self.refresh_tasks).pack(side="left", padx=15)
        
        # Кнопки действий
        ttk.Button(toolbar, text="❌ Удалить", command=self.handle_delete_task).pack(side="right", padx=5)
        ttk.Button(toolbar, text="✅ Завершить", command=self.handle_complete_task).pack(side="right", padx=5)
        
        # Таблица задач
        columns = ("id", "title", "category", "volunteer", "status", "date")
        self.tree_tasks = ttk.Treeview(self.tab_tasks, columns=columns, show="headings", height=15)
        
        headings = [("id", "ID", 40), ("title", "Описание задачи", 300), 
                    ("category", "Категория", 120), ("volunteer", "Ответственный", 120), 
                    ("status", "Статус", 100), ("date", "Дата создания", 120)]
                    
        for col, text, width in headings:
            self.tree_tasks.heading(col, text=text)
            self.tree_tasks.column(col, width=width, anchor="center" if col != "title" else "w")
            
        scroll_y = ttk.Scrollbar(self.tab_tasks, orient="vertical", command=self.tree_tasks.yview)
        self.tree_tasks.configure(yscrollcommand=scroll_y.set)
        
        self.tree_tasks.pack(fill="both", expand=True, padx=10, pady=5)
        scroll_y.pack(side="right", fill="y")
        
        # Панель назначения
        assign_panel = ttk.Frame(self.tab_tasks, padding=10)
        assign_panel.pack(fill="x")
        
        ttk.Label(assign_panel, text="Назначить волонтера (имя):").pack(side="left", padx=5)
        self.ent_assign_vol = ttk.Entry(assign_panel, width=25)
        self.ent_assign_vol.pack(side="left", padx=5)
        ttk.Button(assign_panel, text="Назначить на задачу", command=self.handle_assign).pack(side="left", padx=5)

    def build_add_task_tab(self):
        """Сборка вкладки создания новой заявки"""
        form = ttk.LabelFrame(self.tab_add_task, text=" Детали новой заявки ", padding=20)
        form.pack(padx=30, pady=30, fill="both")
        
        ttk.Label(form, text="Описание проблемы (что нужно сделать):").grid(row=0, column=0, sticky="w", pady=5)
        self.txt_desc = tk.Text(form, height=4, width=60)
        self.txt_desc.grid(row=1, column=0, columnspan=2, sticky="we", pady=5)
        
        ttk.Label(form, text="Категория помощи:").grid(row=2, column=0, sticky="w", pady=10)
        self.cmb_category = ttk.Combobox(form, values=["Доставка продуктов", "Помощь приютам", "Уборка/Субботник", "Техническая помощь", "Медицина", "Другое"], width=30)
        self.cmb_category.current(0)
        self.cmb_category.grid(row=2, column=1, sticky="w", pady=10)
        
        btn_save = ttk.Button(form, text="Сохранить заявку", command=self.handle_add_task)
        btn_save.grid(row=3, column=0, columnspan=2, pady=20)

    def build_volunteers_tab(self):
        """Сборка вкладки базы волонтеров"""
        # Левая часть - форма добавления
        left_frame = ttk.LabelFrame(self.tab_volunteers, text=" Регистрация волонтера ", padding=10)
        left_frame.pack(side="left", fill="y", padx=10, pady=10)
        
        ttk.Label(left_frame, text="ФИО:").pack(anchor="w", pady=2)
        self.ent_vol_name = ttk.Entry(left_frame, width=30)
        self.ent_vol_name.pack(pady=5)
        
        ttk.Label(left_frame, text="Телефон:").pack(anchor="w", pady=2)
        self.ent_vol_phone = ttk.Entry(left_frame, width=30)
        self.ent_vol_phone.pack(pady=5)
        
        ttk.Label(left_frame, text="Навыки/Инвентарь:").pack(anchor="w", pady=2)
        self.ent_vol_skills = ttk.Entry(left_frame, width=30)
        self.ent_vol_skills.pack(pady=5)
        
        ttk.Button(left_frame, text="Добавить в базу", command=self.handle_add_vol).pack(pady=15)
        
        # Правая часть - таблица
        right_frame = ttk.Frame(self.tab_volunteers, padding=10)
        right_frame.pack(side="right", fill="both", expand=True)
        
        columns = ("id", "name", "phone", "skills")
        self.tree_vols = ttk.Treeview(right_frame, columns=columns, show="headings")
        
        self.tree_vols.heading("id", text="ID")
        self.tree_vols.heading("name", text="ФИО")
        self.tree_vols.heading("phone", text="Контакт")
        self.tree_vols.heading("skills", text="Специализация")
        
        self.tree_vols.column("id", width=40, anchor="center")
        self.tree_vols.column("name", width=150)
        self.tree_vols.column("phone", width=120, anchor="center")
        self.tree_vols.column("skills", width=150)
        
        self.tree_vols.pack(fill="both", expand=True, pady=5)
        ttk.Button(right_frame, text="Удалить выбранного", command=self.handle_delete_vol).pack(anchor="e")

    def build_dashboard_tab(self):
        """Сборка вкладки статистики"""
        frame = ttk.Frame(self.tab_dashboard, padding=30)
        frame.pack(fill="both", expand=True)
        
        ttk.Label(frame, text="Сводка по проекту", font=("Helvetica", 16, "bold")).pack(pady=20)
        
        self.lbl_total = ttk.Label(frame, text="Всего заявок: 0", font=("Helvetica", 12))
        self.lbl_total.pack(pady=5)
        self.lbl_open = ttk.Label(frame, text="Ожидают помощи: 0", font=("Helvetica", 12))
        self.lbl_open.pack(pady=5)
        self.lbl_proc = ttk.Label(frame, text="В работе: 0", font=("Helvetica", 12))
        self.lbl_proc.pack(pady=5)
        self.lbl_done = ttk.Label(frame, text="Успешно завершено: 0", font=("Helvetica", 12))
        self.lbl_done.pack(pady=5)

    # --- Обработчики событий (Логика приложения) ---

    def refresh_tasks(self):
        """Обновление таблицы заявок"""
        for item in self.tree_tasks.get_children():
            self.tree_tasks.delete(item)
            
        status_filter = self.cmb_filter.get()
        rows = db.get_all_tasks(status_filter)
        
        for row in rows:
            self.tree_tasks.insert("", "end", values=row)
            
        self.update_dashboard()

    def refresh_volunteers(self):
        """Обновление таблицы волонтеров"""
        for item in self.tree_vols.get_children():
            self.tree_vols.delete(item)
        for row in db.get_all_volunteers():
            self.tree_vols.insert("", "end", values=row)

    def refresh_all_data(self):
        self.refresh_tasks()
        self.refresh_volunteers()

    def update_dashboard(self):
        """Пересчет счетчиков статистики"""
        all_tasks = db.get_all_tasks("Все")
        total = len(all_tasks)
        opened = sum(1 for t in all_tasks if t[4] == "Открыта")
        proc = sum(1 for t in all_tasks if t[4] == "В процессе")
        done = sum(1 for t in all_tasks if t[4] == "Завершена")
        
        self.lbl_total.config(text=f"Всего заявок: {total}")
        self.lbl_open.config(text=f"Ожидают помощи (Открыта): {opened}")
        self.lbl_proc.config(text=f"В работе (В процессе): {proc}")
        self.lbl_done.config(text=f"Успешно завершено: {done}")

    def handle_add_task(self):
        desc = self.txt_desc.get("1.0", "end-1c")
        cat = self.cmb_category.get()
        
        if not utils.validate_text(desc, 5):
            messagebox.showerror("Ошибка", "Описание задачи слишком короткое!")
            return
            
        db.add_task(desc, cat)
        messagebox.showinfo("Успех", "Заявка добавлена в базу!")
        self.txt_desc.delete("1.0", "end")
        self.refresh_all_data()
        self.notebook.select(self.tab_tasks)

    def handle_add_vol(self):
        name = self.ent_vol_name.get().strip()
        phone = self.ent_vol_phone.get().strip()
        skills = self.ent_vol_skills.get().strip() or "Нет"
        
        if not utils.validate_text(name):
            messagebox.showerror("Ошибка", "Введите корректное ФИО!")
            return
            
        is_valid_phone, clean_phone = utils.validate_phone(phone)
        if not is_valid_phone:
            messagebox.showerror("Ошибка", "Некорректный номер телефона!")
            return
            
        db.add_volunteer(name, clean_phone, skills)
        self.ent_vol_name.delete(0, "end")
        self.ent_vol_phone.delete(0, "end")
        self.ent_vol_skills.delete(0, "end")
        self.refresh_volunteers()
        messagebox.showinfo("Готово", "Волонтер зарегистрирован!")

    def get_selected_task_id(self):
        selected = self.tree_tasks.selection()
        if not selected:
            messagebox.showwarning("Внимание", "Выберите задачу в таблице!")
            return None
        return self.tree_tasks.item(selected)["values"][0]

    def handle_assign(self):
        task_id = self.get_selected_task_id()
        if not task_id: return
        
        vol_name = self.ent_assign_vol.get().strip()
        if not utils.validate_text(vol_name, 2):
            messagebox.showerror("Ошибка", "Введите имя ответственного!")
            return
            
        db.update_task_status(task_id, "В процессе", vol_name)
        self.ent_assign_vol.delete(0, "end")
        self.refresh_tasks()
        messagebox.showinfo("Статус", "Волонтер назначен на задачу!")

    def handle_complete_task(self):
        task_id = self.get_selected_task_id()
        if not task_id: return
        if messagebox.askyesno("Подтверждение", "Отметить задачу как завершенную?"):
            db.update_task_status(task_id, "Завершена")
            self.refresh_tasks()

    def handle_delete_task(self):
        task_id = self.get_selected_task_id()
        if not task_id: return
        if messagebox.askyesno("Удаление", "Вы точно хотите удалить эту заявку?"):
            db.delete_task(task_id)
            self.refresh_tasks()

    def handle_delete_vol(self):
        selected = self.tree_vols.selection()
        if not selected:
            messagebox.showwarning("Внимание", "Выберите волонтера в таблице!")
            return
        vol_id = self.tree_vols.item(selected)["values"][0]
        if messagebox.askyesno("Удаление", "Удалить профиль волонтера?"):
            db.delete_volunteer(vol_id)
            self.refresh_volunteers()

    def export_data(self):
        data = db.get_all_tasks("Все")
        success, path = utils.export_to_csv(data)
        if success:
            messagebox.showinfo("Экспорт", f"Данные успешно выгружены:\n{path}")
        else:
            messagebox.showerror("Ошибка экспорта", path)

    def show_about(self):
        text = "Проект 'ДоброКорг'\n\nСистема для координации волонтерской помощи.\nРазработана на Python (Tkinter + SQLite3)."
        messagebox.showinfo("О программе", text)

    def on_exit(self):
        if messagebox.askyesno("Выход", "Вы уверены, что хотите закрыть программу?"):
            self.destroy()

if __name__ == "__main__":
    app = VolunteerApp()
    app.mainloop()
