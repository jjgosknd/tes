"""Функции построения конкретных диаграмм для главы 2."""
from shapes import (rect, roundrect, ellipse, diamond, parallelogram, hexagon,
                    arrow, line, textbox, diagram, _emu_cm)


C = _emu_cm  # alias


# ==========================================================
# 1. Функциональная схема приложения
# ==========================================================
def diagram_functional_scheme():
    """Функциональная схема: блоки модулей и их связи."""
    parts = []
    # Заголовок
    parts.append(textbox(C(0.5), C(0.2), C(17), C(0.8),
                         "Функциональные модули мобильного приложения EduFlow",
                         font_size=11, bold=True, fill="", line_color=""))
    # Слой 1: Презентационный (UI Compose)
    parts.append(textbox(C(0.3), C(1.3), C(3), C(0.6),
                         "Презентация (Compose UI)", font_size=9, bold=True,
                         fill="DEEBF7", line_color="2E75B6"))
    # Экраны
    screens = [
        (0.5, 2.0, "Login"), (2.5, 2.0, "Register"),
        (4.5, 2.0, "Catalog"), (6.5, 2.0, "Course"),
        (8.5, 2.0, "Lesson"), (10.5, 2.0, "Quiz"),
        (12.5, 2.0, "MyCourses"), (14.5, 2.0, "Profile"),
    ]
    for x, y, name in screens:
        parts.append(rect(C(x), C(y), C(2), C(0.9), text=name,
                          fill="DEEBF7", line_color="2E75B6",
                          font_size=9, bold=True))

    # Слой 2: Бизнес-логика (ViewModel)
    parts.append(textbox(C(0.3), C(3.3), C(3), C(0.6),
                         "Бизнес-логика (ViewModel)", font_size=9, bold=True,
                         fill="FFF2CC", line_color="BF9000"))
    vms = [
        (0.5, 4.0, "LoginVM"), (2.5, 4.0, "RegisterVM"),
        (4.5, 4.0, "CatalogVM"), (6.5, 4.0, "CourseDetailsVM"),
        (8.5, 4.0, "LessonVM"), (10.5, 4.0, "LessonVM"),
        (12.5, 4.0, "MyCoursesVM"), (14.5, 4.0, "ProfileVM"),
    ]
    for x, y, name in vms:
        parts.append(rect(C(x), C(y), C(2), C(0.9), text=name,
                          fill="FFF2CC", line_color="BF9000",
                          font_size=8, bold=True))
        parts.append(arrow(C(x + 1), C(2.9), C(x + 1), C(4.0)))

    # Слой 3: Репозитории
    parts.append(textbox(C(0.3), C(5.3), C(3), C(0.6),
                         "Доступ к данным (Repository)", font_size=9,
                         bold=True, fill="E2EFDA", line_color="548235"))
    repos = [
        (0.5, 6.0, "AuthRepository", 4),
        (5.0, 6.0, "CatalogRepository", 4),
        (9.5, 6.0, "LearningRepository", 4),
        (14.0, 6.0, "CertificateRepo", 2.5),
    ]
    for x, y, name, w in repos:
        parts.append(rect(C(x), C(y), C(w), C(0.9), text=name,
                          fill="E2EFDA", line_color="548235",
                          font_size=9, bold=True))

    # Стрелки от ViewModel к репозиториям (упрощённо: общие пучки)
    for x in [0.5, 2.5]:  # Login/Register VM -> AuthRepo
        parts.append(arrow(C(x + 1), C(4.9), C(2.5), C(6.0)))
    for x in [4.5, 6.5]:  # Catalog/Course VM -> CatalogRepo
        parts.append(arrow(C(x + 1), C(4.9), C(7), C(6.0)))
    for x in [8.5, 10.5, 12.5]:  # Lesson/MyCourses VM -> LearningRepo
        parts.append(arrow(C(x + 1), C(4.9), C(11.5), C(6.0)))
    parts.append(arrow(C(15.5), C(4.9), C(15.25), C(6.0)))

    # Слой 4: Сетевой
    parts.append(rect(C(0.5), C(7.3), C(16), C(1),
                      text="Сетевой слой: Retrofit + OkHttp + AuthInterceptor + TokenAuthenticator",
                      fill="FCE4D6", line_color="C65911", font_size=10, bold=True))
    for x in [2.5, 7.0, 11.5, 15.25]:
        parts.append(arrow(C(x), C(6.9), C(x), C(7.3)))

    # Сервер
    parts.append(rect(C(0.5), C(8.7), C(16), C(0.9),
                      text="REST API сервера: /api/v1/auth, /catalog, /courses, /lessons, /me/*",
                      fill="D9E1F2", line_color="2E75B6", font_size=10, bold=True))
    parts.append(arrow(C(8.5), C(8.3), C(8.5), C(8.7)))
    parts.append(arrow(C(8.5), C(8.7), C(8.5), C(8.3), color="000000"))

    return diagram(17.5, 10, ''.join(parts), name="FunctionalScheme")


# ==========================================================
# 2. IDEF0 контекстная диаграмма
# ==========================================================
def diagram_idef0_context():
    parts = []
    # Центральный процесс
    parts.append(rect(C(6), C(4), C(6), C(2.5),
                      text="A0\nПрохождение онлайн\nкурса в мобильном\nприложении",
                      fill="DEEBF7", line_color="2E75B6", font_size=12, bold=True))
    # Входы (слева)
    parts.append(arrow(C(0.5), C(5), C(6), C(5)))
    parts.append(textbox(C(0.5), C(4.4), C(5.4), C(0.5),
                         "Учётные данные пользователя",
                         font_size=9, fill="", line_color=""))
    # Управление (сверху)
    parts.append(arrow(C(7), C(0.5), C(7), C(4)))
    parts.append(textbox(C(7), C(0.5), C(5.5), C(0.5),
                         "Структура каталога курсов",
                         font_size=9, fill="", line_color=""))
    parts.append(arrow(C(9), C(0.5), C(9), C(4)))
    parts.append(textbox(C(9), C(1.0), C(5.5), C(0.5),
                         "Учебный контент и тесты",
                         font_size=9, fill="", line_color=""))
    parts.append(arrow(C(11), C(0.5), C(11), C(4)))
    parts.append(textbox(C(11), C(1.5), C(5.5), C(0.5),
                         "Шаблон сертификата",
                         font_size=9, fill="", line_color=""))
    # Выходы (справа)
    parts.append(arrow(C(12), C(4.5), C(17), C(4.5)))
    parts.append(textbox(C(12.1), C(4.0), C(4.8), C(0.5),
                         "Прогресс прохождения",
                         font_size=9, fill="", line_color=""))
    parts.append(arrow(C(12), C(5.5), C(17), C(5.5)))
    parts.append(textbox(C(12.1), C(5.0), C(4.8), C(0.5),
                         "Результаты тестов",
                         font_size=9, fill="", line_color=""))
    parts.append(arrow(C(12), C(6.2), C(17), C(6.2)))
    parts.append(textbox(C(12.1), C(5.7), C(4.8), C(0.5),
                         "Сертификат (PDF)",
                         font_size=9, fill="", line_color=""))
    # Механизмы (снизу)
    parts.append(arrow(C(7), C(9), C(7), C(6.5)))
    parts.append(textbox(C(6.5), C(9), C(2.5), C(0.5),
                         "Android-устройство",
                         font_size=9, fill="", line_color=""))
    parts.append(arrow(C(9), C(9), C(9), C(6.5)))
    parts.append(textbox(C(8.5), C(9.4), C(3), C(0.5),
                         "REST API сервер",
                         font_size=9, fill="", line_color=""))
    parts.append(arrow(C(11), C(9), C(11), C(6.5)))
    parts.append(textbox(C(10.5), C(9), C(3), C(0.5),
                         "СУБД PostgreSQL",
                         font_size=9, fill="", line_color=""))
    return diagram(17.5, 10.5, ''.join(parts), name="IDEF0_Context")


# ==========================================================
# 3. IDEF0 декомпозиция первого уровня
# ==========================================================
def diagram_idef0_level1():
    parts = []
    # Пять процессов A1..A5
    procs = [
        (0.7, 2.5, 3.0, 1.8, "A1\nРегистрация и\nавторизация"),
        (4.3, 2.5, 3.0, 1.8, "A2\nПросмотр\nкаталога"),
        (7.9, 2.5, 3.0, 1.8, "A3\nПрохождение\nуроков"),
        (11.5, 2.5, 3.0, 1.8, "A4\nВыполнение\nтестов"),
        (4.5, 5.8, 3.0, 1.8, "A5\nВыдача\nсертификата"),
    ]
    for x, y, w, h, text in procs:
        parts.append(rect(C(x), C(y), C(w), C(h), text=text,
                          fill="DEEBF7", line_color="2E75B6",
                          font_size=11, bold=True))

    # Связи A1 -> A2 -> A3 -> A4 -> A5
    parts.append(arrow(C(3.7), C(3.4), C(4.3), C(3.4)))
    parts.append(arrow(C(7.3), C(3.4), C(7.9), C(3.4)))
    parts.append(arrow(C(10.9), C(3.4), C(11.5), C(3.4)))
    # A4 -> A5 (через изгиб)
    parts.append(arrow(C(13), C(4.3), C(13), C(5.5)))
    parts.append(arrow(C(13), C(5.5), C(7.5), C(5.5)))
    parts.append(arrow(C(7.5), C(5.5), C(7.5), C(5.8)))
    # A3 -> A4 повторно (циклическое прохождение)
    parts.append(arrow(C(9.4), C(4.3), C(9.4), C(5.0), dashed=True))
    parts.append(arrow(C(9.4), C(5.0), C(13), C(5.0), dashed=True))

    # Входы слева в A1
    parts.append(arrow(C(0), C(3.4), C(0.7), C(3.4)))
    parts.append(textbox(C(0), C(2.9), C(0.7), C(0.4),
                         "Email/пароль", font_size=8, fill="", line_color=""))

    # Выход справа из A4 — результаты
    parts.append(textbox(C(15), C(2.0), C(2.4), C(0.5),
                         "Прогресс/баллы", font_size=8, fill="", line_color=""))

    # Управление сверху
    for i, (x, _, w, _, _) in enumerate(procs):
        parts.append(arrow(C(x + w/2), C(0.8), C(x + w/2), C(2.5)))

    parts.append(textbox(C(0.7), C(0.4), C(3.0), C(0.4),
                         "Правила", font_size=8, fill="", line_color=""))
    parts.append(textbox(C(4.3), C(0.4), C(3.0), C(0.4),
                         "Каталог", font_size=8, fill="", line_color=""))
    parts.append(textbox(C(7.9), C(0.4), C(3.0), C(0.4),
                         "Контент", font_size=8, fill="", line_color=""))
    parts.append(textbox(C(11.5), C(0.4), C(3.0), C(0.4),
                         "Тесты", font_size=8, fill="", line_color=""))
    parts.append(textbox(C(4.5), C(7.7), C(3.0), C(0.4),
                         "Шаблон сертификата", font_size=8, fill="", line_color=""))

    # Механизмы снизу для каждого
    for x, _, w, _, _ in procs[:4]:
        parts.append(arrow(C(x + w/2), C(5.2), C(x + w/2), C(4.3)))
    parts.append(textbox(C(0.7), C(5.0), C(14.4), C(0.4),
                         "Мобильное приложение / REST API / БД",
                         font_size=8, fill="", line_color=""))

    return diagram(17.5, 8.5, ''.join(parts), name="IDEF0_Level1")


# ==========================================================
# 4. IDEF0 декомпозиция второго уровня (для A3 — Прохождение уроков)
# ==========================================================
def diagram_idef0_level2():
    parts = []
    procs = [
        (0.5, 2.0, 3.5, 1.7, "A3.1\nЗапись\nна курс"),
        (4.5, 2.0, 3.5, 1.7, "A3.2\nЗагрузка\nконтента урока"),
        (8.5, 2.0, 3.5, 1.7, "A3.3\nПросмотр\nматериала"),
        (12.5, 2.0, 4.5, 1.7, "A3.4\nОтметка\n«Урок пройден»"),
        (4.5, 5.0, 3.5, 1.7, "A3.5\nСохранение\nпрогресса"),
        (8.5, 5.0, 3.5, 1.7, "A3.6\nПереход\nк следующему уроку"),
    ]
    for x, y, w, h, text in procs:
        parts.append(rect(C(x), C(y), C(w), C(h), text=text,
                          fill="FFF2CC", line_color="BF9000",
                          font_size=10, bold=True))
    # Стрелки
    parts.append(arrow(C(4.0), C(2.85), C(4.5), C(2.85)))
    parts.append(arrow(C(8.0), C(2.85), C(8.5), C(2.85)))
    parts.append(arrow(C(12.0), C(2.85), C(12.5), C(2.85)))
    parts.append(arrow(C(14.5), C(3.7), C(14.5), C(4.5)))
    parts.append(arrow(C(14.5), C(4.5), C(6.25), C(4.5)))
    parts.append(arrow(C(6.25), C(4.5), C(6.25), C(5.0)))
    parts.append(arrow(C(8.0), C(5.85), C(8.5), C(5.85), dashed=False))
    parts.append(arrow(C(10.25), C(5.0), C(10.25), C(3.7), dashed=True))

    # Подписи входов/выходов
    parts.append(arrow(C(0), C(2.85), C(0.5), C(2.85)))
    parts.append(textbox(C(0), C(2.4), C(0.5), C(0.4),
                         "ID курса", font_size=8, fill="", line_color=""))

    parts.append(arrow(C(13), C(7.5), C(13), C(6.7)))
    parts.append(textbox(C(12), C(7.5), C(3), C(0.4),
                         "Курс пройден→A5", font_size=8, fill="", line_color=""))

    return diagram(17.5, 8, ''.join(parts), name="IDEF0_Level2")


# ==========================================================
# 5. DFD первого уровня (нотация Гейна-Сарсона)
# ==========================================================
def diagram_dfd_level1():
    parts = []
    # Внешние сущности (квадраты с тенью)
    parts.append(rect(C(0.3), C(2.0), C(2.5), C(1.2),
                      text="Учащийся", fill="F2F2F2",
                      line_color="000000", font_size=10, bold=True))
    parts.append(rect(C(0.3), C(7.0), C(2.5), C(1.2),
                      text="Преподаватель\n(админ-панель)", fill="F2F2F2",
                      line_color="000000", font_size=9, bold=True))

    # Процессы (скруглённые) — нумерованные
    procs = [
        (4.0, 1.0, "1\nАутентификация"),
        (4.0, 3.5, "2\nКаталог"),
        (4.0, 6.0, "3\nПрохождение урока"),
        (10.0, 1.0, "4\nТестирование"),
        (10.0, 3.5, "5\nПрогресс"),
        (10.0, 6.0, "6\nСертификат"),
    ]
    for x, y, text in procs:
        parts.append(roundrect(C(x), C(y), C(3.5), C(1.2), text=text,
                               fill="DEEBF7", line_color="2E75B6",
                               font_size=10, bold=True))

    # Хранилища (открытые прямоугольники сверху-снизу)
    stores = [
        (14.5, 1.0, "D1 Пользователи"),
        (14.5, 3.5, "D2 Курсы"),
        (14.5, 6.0, "D3 Прогресс"),
        (14.5, 7.5, "D4 Сертификаты"),
    ]
    for x, y, text in stores:
        parts.append(rect(C(x), C(y), C(3), C(0.8), text=text,
                          fill="FFF2CC", line_color="BF9000",
                          font_size=9, bold=True))

    # Связи: учащийся <-> процессы
    parts.append(arrow(C(2.8), C(2.6), C(4.0), C(1.6)))  # Уч -> 1
    parts.append(arrow(C(4.0), C(1.4), C(2.8), C(2.4), dashed=False))  # 1 -> Уч (ответ)
    parts.append(arrow(C(2.8), C(2.6), C(4.0), C(4.1)))  # Уч -> 2
    parts.append(arrow(C(2.8), C(2.6), C(4.0), C(6.6)))  # Уч -> 3
    parts.append(arrow(C(2.8), C(2.6), C(10.0), C(1.6)))  # Уч -> 4 (тесты)

    # Преподаватель -> 2 (наполняет каталог)
    parts.append(arrow(C(2.8), C(7.6), C(4.0), C(4.1)))

    # Процессы -> хранилища
    parts.append(arrow(C(7.5), C(1.6), C(14.5), C(1.4)))  # 1 -> D1
    parts.append(arrow(C(7.5), C(4.1), C(14.5), C(3.9)))  # 2 -> D2
    parts.append(arrow(C(7.5), C(6.6), C(14.5), C(6.4)))  # 3 -> D3
    parts.append(arrow(C(13.5), C(4.1), C(14.5), C(3.9)))  # 5 -> D2
    parts.append(arrow(C(13.5), C(6.6), C(14.5), C(7.9)))  # 6 -> D4

    # Связи между процессами
    parts.append(arrow(C(7.5), C(6.6), C(10.0), C(4.1)))  # 3 -> 5 (отметка прогресса)
    parts.append(arrow(C(11.75), C(2.2), C(11.75), C(3.5)))  # 4 -> 5 (результат теста)
    parts.append(arrow(C(11.75), C(4.7), C(11.75), C(6.0)))  # 5 -> 6 (после 100% выдать сертификат)

    return diagram(17.5, 9, ''.join(parts), name="DFD_Level1")


# ==========================================================
# 6. ER-диаграмма базы данных
# ==========================================================
def diagram_er():
    parts = []
    entities = [
        # x, y, w, h, name, fields
        (0.3, 0.4, 3.5, 3.6, "users",
         "PK id BIGINT\n— email VARCHAR\n— password_hash VARCHAR\n— full_name VARCHAR\n— role user_role\n— created_at TIMESTAMP"),
        (4.5, 0.4, 3.5, 2.5, "categories",
         "PK id BIGINT\n— name VARCHAR\n— slug VARCHAR\n— icon_url VARCHAR"),
        (8.7, 0.4, 4.0, 4.6, "courses",
         "PK id BIGINT\nFK category_id\n— title VARCHAR\n— description TEXT\n— level prog_level\n— author VARCHAR\n— cover_url VARCHAR\n— duration_min INT\n— is_published BOOL"),
        (13.4, 0.4, 4.0, 3.6, "modules",
         "PK id BIGINT\nFK course_id\n— title VARCHAR\n— position INT"),
        (13.4, 4.5, 4.0, 4.0, "lessons",
         "PK id BIGINT\nFK module_id\n— title VARCHAR\n— content_md TEXT\n— video_url VARCHAR\n— position INT\n— duration_min INT"),
        (8.7, 5.5, 4.0, 4.0, "quiz_questions",
         "PK id BIGINT\nFK lesson_id\n— question TEXT\n— options JSONB\n— correct_idx INT"),
        (4.5, 3.5, 3.5, 2.5, "enrollments",
         "PK id BIGINT\nFK user_id\nFK course_id\n— enrolled_at TIMESTAMP"),
        (0.3, 4.5, 3.5, 2.5, "lesson_progress",
         "PK id BIGINT\nFK user_id\nFK lesson_id\n— completed_at TIMESTAMP"),
        (4.5, 6.5, 3.5, 3.0, "certificates",
         "PK id BIGINT\nFK user_id\nFK course_id\n— issued_at TIMESTAMP\n— certificate_no VARCHAR\n— pdf_url VARCHAR"),
        (0.3, 8.0, 3.5, 1.5, "refresh_tokens",
         "PK id BIGINT\nFK user_id\n— token_hash VARCHAR\n— expires_at TIMESTAMP"),
    ]
    for x, y, w, h, name, fields in entities:
        # Заголовок
        parts.append(rect(C(x), C(y), C(w), C(0.6), text=name,
                          fill="2E75B6", line_color="2E75B6",
                          font_size=10, bold=True, font_color="FFFFFF"))
        # Тело
        parts.append(rect(C(x), C(y + 0.6), C(w), C(h - 0.6), text=fields,
                          fill="FFFFFF", line_color="2E75B6",
                          font_size=8, bold=False, text_align="l"))

    # Связи
    # users 1—N enrollments
    parts.append(line(C(3.8), C(2.2), C(4.5), C(4.7)))
    # courses 1—N enrollments
    parts.append(line(C(8.7), C(2.7), C(8.0), C(4.7)))
    # users 1—N lesson_progress
    parts.append(line(C(2.0), C(4.0), C(2.0), C(4.5)))
    # courses 1—N modules
    parts.append(line(C(12.7), C(2.7), C(13.4), C(2.7)))
    # modules 1—N lessons
    parts.append(line(C(15.4), C(4.0), C(15.4), C(4.5)))
    # lessons 1—N quiz_questions
    parts.append(line(C(13.4), C(7.5), C(12.7), C(7.5)))
    # lesson_progress N—1 lessons
    parts.append(line(C(3.8), C(5.7), C(13.4), C(6.0)))
    # certificates N—1 users
    parts.append(line(C(4.5), C(7.5), C(2.0), C(7.0)))
    # certificates N—1 courses
    parts.append(line(C(8.0), C(7.5), C(10.7), C(5.0)))
    # categories 1—N courses
    parts.append(line(C(8.0), C(1.6), C(8.7), C(1.6)))
    # users 1—N refresh_tokens
    parts.append(line(C(2.0), C(4.0), C(2.0), C(8.0)))

    return diagram(17.5, 10, ''.join(parts), name="ER_Diagram")


# ==========================================================
# 7. Диаграмма классов мобильного клиента (UML)
# ==========================================================
def diagram_class():
    parts = []
    # Слой UI/Compose (Screens) - голубые
    classes = [
        # x,y,w,h, name, body, fill
        (0.3, 0.3, 3.5, 1.6, "<<screen>>\nLoginScreen",
         "+ Render(state)\n+ onSubmit()", "DEEBF7", "2E75B6"),
        (4.3, 0.3, 3.5, 1.6, "<<screen>>\nCatalogScreen",
         "+ Render(state)\n+ onCourseClick()", "DEEBF7", "2E75B6"),
        (8.3, 0.3, 3.5, 1.6, "<<screen>>\nCourseDetailsScreen",
         "+ Render(state)\n+ onEnroll()", "DEEBF7", "2E75B6"),
        (12.3, 0.3, 3.5, 1.6, "<<screen>>\nLessonScreen",
         "+ Render(state)\n+ onComplete()", "DEEBF7", "2E75B6"),

        # ViewModel - жёлтые
        (0.3, 2.2, 3.5, 1.8, "LoginViewModel",
         "- repo: AuthRepository\n+ submit(email, pwd)", "FFF2CC", "BF9000"),
        (4.3, 2.2, 3.5, 1.8, "CatalogViewModel",
         "- repo: CatalogRepo\n+ load()\n+ filter(cat)", "FFF2CC", "BF9000"),
        (8.3, 2.2, 3.5, 1.8, "CourseDetailsViewModel",
         "- repo: CatalogRepo\n+ load(id)\n+ enroll()", "FFF2CC", "BF9000"),
        (12.3, 2.2, 3.5, 1.8, "LessonViewModel",
         "- repo: LearningRepo\n+ load(id)\n+ complete()\n+ submitQuiz()", "FFF2CC", "BF9000"),

        # Repository - зелёные
        (0.3, 4.4, 3.5, 1.8, "AuthRepository",
         "+ login()\n+ register()\n+ logout()\n+ refresh()", "E2EFDA", "548235"),
        (4.3, 4.4, 3.5, 1.8, "CatalogRepository",
         "+ categories()\n+ courses(filter)\n+ courseById(id)", "E2EFDA", "548235"),
        (8.3, 4.4, 3.5, 1.8, "LearningRepository",
         "+ enroll(courseId)\n+ lesson(id)\n+ complete(id)\n+ submitQuiz()\n+ myCourses()", "E2EFDA", "548235"),
        (12.3, 4.4, 3.5, 1.8, "CertificateRepository",
         "+ listMine()\n+ downloadPdf(id)", "E2EFDA", "548235"),

        # API/Network - красноватые
        (0.3, 6.6, 3.5, 1.5, "AuthApi (Retrofit)",
         "@POST(\"login\")\n@POST(\"register\")\n@POST(\"refresh\")", "FCE4D6", "C65911"),
        (4.3, 6.6, 7.5, 1.5, "EduFlowApi (Retrofit)",
         "@GET categories, courses, course/{id}\n@POST courses/{id}/enroll\n@GET lessons/{id}\n@POST lessons/{id}/complete, /quiz\n@GET me/courses, /certificates", "FCE4D6", "C65911"),
        (12.3, 6.6, 3.5, 1.5, "TokenStore",
         "+ save(pair)\n+ access()\n+ refresh()\n+ clear()", "FCE4D6", "C65911"),
    ]
    for x, y, w, h, name, body, fill, line_color in classes:
        # шапка
        parts.append(rect(C(x), C(y), C(w), C(0.6), text=name,
                          fill=line_color, line_color=line_color,
                          font_size=9, bold=True, font_color="FFFFFF"))
        parts.append(rect(C(x), C(y + 0.6), C(w), C(h - 0.6), text=body,
                          fill=fill, line_color=line_color,
                          font_size=8, text_align="l"))

    # связи: каждый Screen -> VM (по вертикали)
    for x in [0.3, 4.3, 8.3, 12.3]:
        cx = x + 1.75
        parts.append(arrow(C(cx), C(1.9), C(cx), C(2.2)))
        parts.append(arrow(C(cx), C(4.0), C(cx), C(4.4)))
    # repo -> api (упрощённо: один пучок)
    parts.append(arrow(C(2.0), C(6.2), C(2.0), C(6.6)))
    parts.append(arrow(C(6.0), C(6.2), C(6.0), C(6.6)))
    parts.append(arrow(C(10.0), C(6.2), C(8.0), C(6.6)))
    parts.append(arrow(C(14.0), C(6.2), C(8.0), C(6.6)))
    # AuthApi <- TokenStore (зависимость)
    parts.append(arrow(C(12.3), C(7.4), C(3.8), C(7.4), dashed=True))

    return diagram(17.5, 9, ''.join(parts), name="ClassDiagram")


# ==========================================================
# 8. Диаграмма вариантов использования (Use Case)
# ==========================================================
def diagram_use_case():
    parts = []
    # Системная граница
    parts.append(rect(C(4.5), C(0.5), C(10.5), C(9), text="",
                      fill="", line_color="2E75B6", line_width=12700))
    parts.append(textbox(C(4.5), C(0.5), C(10.5), C(0.5),
                         "Мобильное приложение EduFlow", font_size=11, bold=True,
                         fill="", line_color=""))
    # Актёры (упрощённая фигурка)
    actors = [
        (0.3, 1.2, "Учащийся"),
        (15.3, 1.2, "Сервер\n(REST API)"),
        (0.3, 7.0, "Преподаватель\n(админ-панель)"),
    ]
    for x, y, name in actors:
        # head
        parts.append(ellipse(C(x + 0.6), C(y), C(0.5), C(0.5),
                             fill="FFFFFF", line_color="000000"))
        # body lines (упрощённо — просто прямоугольник на месте тела)
        parts.append(line(C(x + 0.85), C(y + 0.5), C(x + 0.85), C(y + 1.2)))
        parts.append(line(C(x + 0.4), C(y + 0.7), C(x + 1.3), C(y + 0.7)))
        parts.append(line(C(x + 0.85), C(y + 1.2), C(x + 0.4), C(y + 1.6)))
        parts.append(line(C(x + 0.85), C(y + 1.2), C(x + 1.3), C(y + 1.6)))
        parts.append(textbox(C(x), C(y + 1.7), C(2.0), C(0.7),
                             name, font_size=9, bold=True,
                             fill="", line_color=""))

    # Use cases
    use_cases = [
        (5.5, 1.2, "Зарегистрироваться"),
        (5.5, 2.0, "Авторизоваться"),
        (5.5, 2.8, "Просмотреть каталог"),
        (5.5, 3.6, "Фильтровать по категории"),
        (5.5, 4.4, "Открыть курс"),
        (5.5, 5.2, "Записаться на курс"),
        (10.5, 1.2, "Открыть урок"),
        (10.5, 2.0, "Просмотреть видео"),
        (10.5, 2.8, "Пройти тест"),
        (10.5, 3.6, "Отметить «Пройдено»"),
        (10.5, 4.4, "Просмотреть «Мои курсы»"),
        (10.5, 5.2, "Просмотреть профиль"),
        (8.0, 6.0, "Получить сертификат"),
        (8.0, 6.8, "Скачать PDF сертификата"),
        (8.0, 7.6, "Выйти из аккаунта"),
        (5.5, 6.0, "Управлять курсами"),
        (5.5, 6.8, "Управлять учётками"),
    ]
    for x, y, name in use_cases:
        parts.append(ellipse(C(x), C(y), C(4.3), C(0.7), text=name,
                             fill="FFF2CC", line_color="BF9000",
                             font_size=8, bold=False))

    # Связи учащегося с use case (упрощённо — линии)
    for ux, uy in [(5.5, 1.2), (5.5, 2.0), (5.5, 2.8), (5.5, 3.6), (5.5, 4.4),
                   (5.5, 5.2), (10.5, 1.2), (10.5, 2.0), (10.5, 2.8), (10.5, 3.6),
                   (10.5, 4.4), (10.5, 5.2), (8.0, 6.0), (8.0, 6.8), (8.0, 7.6)]:
        parts.append(line(C(1.5), C(2.4), C(ux), C(uy + 0.35), width=6350))

    # Связи преподавателя
    for ux, uy in [(5.5, 6.0), (5.5, 6.8)]:
        parts.append(line(C(1.5), C(8.2), C(ux), C(uy + 0.35), width=6350))

    # Связи сервера (правый) — со всеми
    for ux, uy in [(5.5, 1.2), (5.5, 2.0), (10.5, 1.2), (10.5, 2.0), (10.5, 2.8),
                   (8.0, 6.0), (8.0, 6.8)]:
        parts.append(line(C(ux + 4.3), C(uy + 0.35), C(15.6), C(2.4), width=6350))

    return diagram(17.5, 10, ''.join(parts), name="UseCase")


# ==========================================================
# 9. Архитектура развёртывания (deployment diagram)
# ==========================================================
def diagram_deployment():
    parts = []
    # Узел: смартфон
    parts.append(rect(C(0.3), C(0.3), C(5.0), C(5.5), text="",
                      fill="F2F2F2", line_color="000000"))
    parts.append(textbox(C(0.3), C(0.3), C(5.0), C(0.6),
                         "Узел: Android-смартфон",
                         font_size=10, bold=True, fill="", line_color=""))
    # Артефакты внутри
    parts.append(rect(C(0.7), C(1.1), C(4.2), C(1.0), text="EduFlow.apk",
                      fill="DEEBF7", line_color="2E75B6", font_size=10, bold=True))
    parts.append(rect(C(0.7), C(2.3), C(4.2), C(1.0), text="EncryptedSharedPrefs",
                      fill="DEEBF7", line_color="2E75B6", font_size=10, bold=True))
    parts.append(rect(C(0.7), C(3.5), C(4.2), C(1.0), text="DataStore (Settings)",
                      fill="DEEBF7", line_color="2E75B6", font_size=10, bold=True))

    # Узел: API-сервер
    parts.append(rect(C(6.5), C(0.3), C(5.0), C(5.5), text="",
                      fill="F2F2F2", line_color="000000"))
    parts.append(textbox(C(6.5), C(0.3), C(5.0), C(0.6),
                         "Узел: API-сервер (Linux, Docker)",
                         font_size=10, bold=True, fill="", line_color=""))
    parts.append(rect(C(7.0), C(1.1), C(4.0), C(1.0), text="Spring Boot 3 (JAR)",
                      fill="FFF2CC", line_color="BF9000", font_size=10, bold=True))
    parts.append(rect(C(7.0), C(2.3), C(4.0), C(1.0), text="Nginx (reverse proxy)",
                      fill="FFF2CC", line_color="BF9000", font_size=10, bold=True))
    parts.append(rect(C(7.0), C(3.5), C(4.0), C(1.0), text="Storage (S3-совместимый)",
                      fill="FFF2CC", line_color="BF9000", font_size=10, bold=True))

    # Узел: СУБД
    parts.append(rect(C(12.7), C(0.3), C(4.5), C(5.5), text="",
                      fill="F2F2F2", line_color="000000"))
    parts.append(textbox(C(12.7), C(0.3), C(4.5), C(0.6),
                         "Узел: БД (Linux, Docker)",
                         font_size=10, bold=True, fill="", line_color=""))
    parts.append(rect(C(13.0), C(1.1), C(3.9), C(1.0), text="PostgreSQL 16",
                      fill="E2EFDA", line_color="548235", font_size=10, bold=True))
    parts.append(rect(C(13.0), C(2.3), C(3.9), C(1.0), text="Redis 7\n(сессии/кэш)",
                      fill="E2EFDA", line_color="548235", font_size=9, bold=True))

    # Связи
    parts.append(arrow(C(4.9), C(1.6), C(7.0), C(1.6)))
    parts.append(textbox(C(5.0), C(1.0), C(2.0), C(0.5),
                         "HTTPS / REST", font_size=9, fill="", line_color=""))
    parts.append(arrow(C(11.0), C(1.6), C(13.0), C(1.6)))
    parts.append(textbox(C(11.1), C(1.0), C(2.0), C(0.5),
                         "JDBC", font_size=9, fill="", line_color=""))
    parts.append(arrow(C(11.0), C(2.8), C(13.0), C(2.8)))
    parts.append(textbox(C(11.1), C(3.4), C(2.0), C(0.5),
                         "TCP/Redis proto", font_size=9, fill="", line_color=""))

    return diagram(17.5, 6.5, ''.join(parts), name="Deployment")


# ==========================================================
# 10. Диаграмма последовательности — авторизация и обновление токена
# ==========================================================
def diagram_seq_auth():
    parts = []
    # Жизненные линии
    actors = [
        (1.0, "Учащийся"),
        (4.0, "LoginScreen"),
        (7.0, "AuthRepository"),
        (10.0, "AuthApi"),
        (13.0, "TokenStore"),
        (16.0, "Сервер"),
    ]
    for x, name in actors:
        parts.append(rect(C(x - 1), C(0.2), C(2), C(0.7), text=name,
                          fill="DEEBF7", line_color="2E75B6",
                          font_size=9, bold=True))
        # пунктирная линия жизни
        parts.append(line(C(x), C(0.9), C(x), C(9.0), color="888888"))

    # Сообщения
    msgs = [
        (1.0, 4.0, 1.5, "ввод email/password"),
        (4.0, 7.0, 2.0, "submit(email, pwd)"),
        (7.0, 10.0, 2.5, "login(req)"),
        (10.0, 16.0, 3.0, "POST /auth/login"),
        (16.0, 10.0, 3.5, "200 {access, refresh, user}"),
        (10.0, 7.0, 4.0, "AuthResponse"),
        (7.0, 13.0, 4.5, "save(tokens)"),
        (13.0, 7.0, 5.0, "ok"),
        (7.0, 4.0, 5.5, "Result.Success"),
        (4.0, 1.0, 6.0, "переход в Catalog"),
        (4.0, 7.0, 7.0, "...позже: GET /courses (401)"),
        (7.0, 13.0, 7.5, "refresh()"),
        (13.0, 10.0, 8.0, "POST /auth/refresh"),
        (10.0, 7.0, 8.5, "новый access"),
    ]
    for x1, x2, y, text in msgs:
        parts.append(arrow(C(x1), C(y), C(x2), C(y)))
        # подпись
        midx = min(x1, x2)
        w = abs(x2 - x1)
        parts.append(textbox(C(midx), C(y - 0.4), C(max(w, 1.5)), C(0.3),
                             text, font_size=8, fill="", line_color=""))

    return diagram(17.5, 10, ''.join(parts), name="SeqAuth")


# ==========================================================
# 11. Главный экран Catalog (макет)
# ==========================================================
def diagram_screen_catalog():
    parts = []
    # Рамка телефона
    parts.append(roundrect(C(5), C(0.3), C(7), C(13), text="",
                           fill="FFFFFF", line_color="000000", line_width=25400))
    # TopBar
    parts.append(rect(C(5.2), C(0.6), C(6.6), C(0.9), text="EduFlow",
                      fill="2E75B6", line_color="2E75B6",
                      font_size=11, bold=True, font_color="FFFFFF"))
    # Search bar
    parts.append(roundrect(C(5.4), C(1.7), C(6.2), C(0.7), text="🔍 Поиск курсов",
                           fill="F2F2F2", line_color="BFBFBF",
                           font_size=9, text_align="l"))
    # Категории — chips
    cats = ["Все", "IT", "Дизайн", "Бизнес", "Языки"]
    cx = 5.4
    for i, c in enumerate(cats):
        fill = "2E75B6" if i == 1 else "F2F2F2"
        fc = "FFFFFF" if i == 1 else "000000"
        parts.append(roundrect(C(cx), C(2.6), C(1.1), C(0.6), text=c,
                               fill=fill, line_color=fill,
                               font_size=8, font_color=fc))
        cx += 1.2
    # Список курсов (4 карточки)
    courses = [
        ("Kotlin для Android", "Иван Петров", "16 ч • Начальный"),
        ("UI/UX-дизайн", "Анна Смирнова", "20 ч • Средний"),
        ("Управление проектами", "Олег Иванов", "12 ч • Начальный"),
        ("Английский A2→B1", "Maria Lee", "30 ч • Средний"),
    ]
    y = 3.5
    for title, author, info in courses:
        parts.append(roundrect(C(5.4), C(y), C(6.2), C(2.0), text="",
                               fill="FFFFFF", line_color="BFBFBF"))
        # Обложка слева
        parts.append(rect(C(5.6), C(y + 0.2), C(1.6), C(1.6), text="",
                          fill="DEEBF7", line_color="2E75B6"))
        # Текст
        parts.append(textbox(C(7.4), C(y + 0.2), C(4.0), C(0.5),
                             title, font_size=10, bold=True,
                             fill="", line_color="", text_align="l"))
        parts.append(textbox(C(7.4), C(y + 0.8), C(4.0), C(0.5),
                             author, font_size=8,
                             fill="", line_color="", text_align="l"))
        parts.append(textbox(C(7.4), C(y + 1.4), C(4.0), C(0.4),
                             info, font_size=8,
                             fill="", line_color="", text_align="l"))
        y += 2.2

    # BottomBar
    parts.append(rect(C(5.2), C(12.0), C(6.6), C(1.0), text="",
                      fill="F2F2F2", line_color="BFBFBF"))
    tabs = ["Каталог", "Мои курсы", "Профиль"]
    tx = 5.5
    for i, t in enumerate(tabs):
        col = "2E75B6" if i == 0 else "595959"
        weight = True if i == 0 else False
        parts.append(textbox(C(tx), C(12.2), C(2), C(0.7),
                             t, font_size=9, bold=weight, font_color=col,
                             fill="", line_color=""))
        tx += 2.1
    return diagram(17, 14, ''.join(parts), name="Screen_Catalog")


# ==========================================================
# 12. Экран курса (Course Details)
# ==========================================================
def diagram_screen_course():
    parts = []
    parts.append(roundrect(C(5), C(0.3), C(7), C(13), text="",
                           fill="FFFFFF", line_color="000000", line_width=25400))
    # Topbar с кнопкой назад
    parts.append(rect(C(5.2), C(0.6), C(6.6), C(0.9), text="← Курс",
                      fill="2E75B6", line_color="2E75B6",
                      font_size=11, bold=True, font_color="FFFFFF",
                      text_align="l"))
    # Обложка
    parts.append(rect(C(5.4), C(1.7), C(6.2), C(2.5), text="",
                      fill="DEEBF7", line_color="2E75B6"))
    # Заголовок
    parts.append(textbox(C(5.4), C(4.4), C(6.2), C(0.6),
                         "Kotlin для Android-разработки",
                         font_size=11, bold=True,
                         fill="", line_color="", text_align="l"))
    parts.append(textbox(C(5.4), C(5.0), C(6.2), C(0.5),
                         "Иван Петров • 16 ч • Начальный",
                         font_size=9, fill="", line_color="", text_align="l"))
    # Кнопка
    parts.append(roundrect(C(5.4), C(5.7), C(6.2), C(0.8),
                           text="Записаться",
                           fill="2E75B6", line_color="2E75B6",
                           font_size=11, bold=True, font_color="FFFFFF"))
    # Программа
    parts.append(textbox(C(5.4), C(6.8), C(6.2), C(0.5),
                         "Программа курса",
                         font_size=10, bold=True,
                         fill="", line_color="", text_align="l"))
    # Модуль 1
    parts.append(textbox(C(5.4), C(7.4), C(6.2), C(0.5),
                         "Модуль 1. Основы Kotlin",
                         font_size=9, bold=True,
                         fill="", line_color="", text_align="l"))
    lessons1 = ["1.1 Введение", "1.2 Переменные и типы", "1.3 Функции"]
    for i, l in enumerate(lessons1):
        parts.append(textbox(C(5.6), C(7.9 + i * 0.5), C(6.0), C(0.4),
                             "• " + l, font_size=9,
                             fill="", line_color="", text_align="l"))
    # Модуль 2
    parts.append(textbox(C(5.4), C(9.5), C(6.2), C(0.5),
                         "Модуль 2. Android и Compose",
                         font_size=9, bold=True,
                         fill="", line_color="", text_align="l"))
    lessons2 = ["2.1 Настройка проекта", "2.2 Compose UI", "2.3 Навигация"]
    for i, l in enumerate(lessons2):
        parts.append(textbox(C(5.6), C(10.0 + i * 0.5), C(6.0), C(0.4),
                             "• " + l, font_size=9,
                             fill="", line_color="", text_align="l"))
    # Bottom
    parts.append(rect(C(5.2), C(12.0), C(6.6), C(1.0), text="",
                      fill="F2F2F2", line_color="BFBFBF"))
    return diagram(17, 14, ''.join(parts), name="Screen_Course")


# ==========================================================
# 13. Экран урока (Lesson)
# ==========================================================
def diagram_screen_lesson():
    parts = []
    parts.append(roundrect(C(5), C(0.3), C(7), C(13), text="",
                           fill="FFFFFF", line_color="000000", line_width=25400))
    parts.append(rect(C(5.2), C(0.6), C(6.6), C(0.9), text="← Урок 1.2",
                      fill="2E75B6", line_color="2E75B6",
                      font_size=11, bold=True, font_color="FFFFFF",
                      text_align="l"))
    # Видео-плеер
    parts.append(rect(C(5.4), C(1.7), C(6.2), C(3.5), text="▶  ВИДЕО",
                      fill="000000", line_color="000000",
                      font_size=14, bold=True, font_color="FFFFFF"))
    # Заголовок урока
    parts.append(textbox(C(5.4), C(5.4), C(6.2), C(0.6),
                         "Переменные и типы данных",
                         font_size=11, bold=True,
                         fill="", line_color="", text_align="l"))
    # Текст
    parts.append(textbox(C(5.4), C(6.0), C(6.2), C(2.5),
                         "В Kotlin переменные объявляются\nс помощью val (неизменяемые)\nи var (изменяемые). Базовые типы:\nInt, Long, Double, String, Boolean.\nСистема типов — статическая, с\nвыводом типа.",
                         font_size=9,
                         fill="", line_color="", text_align="l"))
    # Тест
    parts.append(textbox(C(5.4), C(8.6), C(6.2), C(0.5),
                         "Проверка знаний",
                         font_size=10, bold=True,
                         fill="", line_color="", text_align="l"))
    parts.append(textbox(C(5.4), C(9.1), C(6.2), C(0.5),
                         "Какое ключевое слово создаёт\nнеизменяемую переменную?",
                         font_size=9,
                         fill="", line_color="", text_align="l"))
    options = ["○ var", "● val", "○ const", "○ let"]
    for i, o in enumerate(options):
        parts.append(textbox(C(5.6), C(10.0 + i * 0.4), C(6.0), C(0.4),
                             o, font_size=9,
                             fill="", line_color="", text_align="l"))
    # Кнопка отметить пройденным
    parts.append(roundrect(C(5.4), C(11.6), C(6.2), C(0.7),
                           text="Отметить пройденным",
                           fill="2E75B6", line_color="2E75B6",
                           font_size=10, bold=True, font_color="FFFFFF"))
    return diagram(17, 14, ''.join(parts), name="Screen_Lesson")


# ==========================================================
# 14. Экран профиля и сертификатов
# ==========================================================
def diagram_screen_profile():
    parts = []
    parts.append(roundrect(C(5), C(0.3), C(7), C(13), text="",
                           fill="FFFFFF", line_color="000000", line_width=25400))
    parts.append(rect(C(5.2), C(0.6), C(6.6), C(0.9), text="Профиль",
                      fill="2E75B6", line_color="2E75B6",
                      font_size=11, bold=True, font_color="FFFFFF"))
    # Аватар
    parts.append(ellipse(C(7.5), C(1.8), C(2), C(2), text="",
                         fill="DEEBF7", line_color="2E75B6"))
    # Имя
    parts.append(textbox(C(5.4), C(4.0), C(6.2), C(0.6),
                         "Соловьёв Георгий",
                         font_size=11, bold=True,
                         fill="", line_color="", text_align="ctr"))
    parts.append(textbox(C(5.4), C(4.6), C(6.2), C(0.5),
                         "g.solovyev@example.com\nРоль: Студент",
                         font_size=9,
                         fill="", line_color="", text_align="ctr"))
    # Сертификаты
    parts.append(textbox(C(5.4), C(5.7), C(6.2), C(0.5),
                         "Мои сертификаты",
                         font_size=10, bold=True,
                         fill="", line_color="", text_align="l"))
    # Список (3 карточки)
    certs = [
        ("Kotlin для Android", "Выдан: 12.04.2026"),
        ("UI/UX-дизайн", "Выдан: 02.03.2026"),
    ]
    y = 6.3
    for title, info in certs:
        parts.append(roundrect(C(5.4), C(y), C(6.2), C(1.4), text="",
                               fill="FFFFFF", line_color="BFBFBF"))
        parts.append(rect(C(5.6), C(y + 0.2), C(0.9), C(1.0), text="📄",
                          fill="FFF2CC", line_color="BF9000",
                          font_size=14, bold=True))
        parts.append(textbox(C(6.7), C(y + 0.2), C(4.7), C(0.5),
                             title, font_size=10, bold=True,
                             fill="", line_color="", text_align="l"))
        parts.append(textbox(C(6.7), C(y + 0.7), C(4.7), C(0.4),
                             info, font_size=8,
                             fill="", line_color="", text_align="l"))
        # Кнопка PDF
        parts.append(roundrect(C(6.7), C(y + 1.0), C(2.2), C(0.4),
                               text="Открыть PDF",
                               fill="2E75B6", line_color="2E75B6",
                               font_size=8, bold=True, font_color="FFFFFF"))
        y += 1.6
    # Кнопка выхода
    parts.append(roundrect(C(5.4), C(10.5), C(6.2), C(0.8),
                           text="Выйти из аккаунта",
                           fill="C00000", line_color="C00000",
                           font_size=11, bold=True, font_color="FFFFFF"))
    return diagram(17, 14, ''.join(parts), name="Screen_Profile")


# ==========================================================
# 15. Экран авторизации (Login)
# ==========================================================
def diagram_screen_login():
    parts = []
    parts.append(roundrect(C(5), C(0.3), C(7), C(13), text="",
                           fill="FFFFFF", line_color="000000", line_width=25400))
    # Логотип
    parts.append(textbox(C(5), C(2.0), C(7), C(1.2),
                         "EduFlow",
                         font_size=22, bold=True, font_color="2E75B6",
                         fill="", line_color=""))
    parts.append(textbox(C(5), C(3.2), C(7), C(0.6),
                         "Вход в EduFlow",
                         font_size=11,
                         fill="", line_color=""))
    # Поля
    parts.append(roundrect(C(5.6), C(4.5), C(5.8), C(1.0), text="Email",
                           fill="FFFFFF", line_color="BFBFBF",
                           font_size=10, text_align="l"))
    parts.append(roundrect(C(5.6), C(5.7), C(5.8), C(1.0), text="Пароль",
                           fill="FFFFFF", line_color="BFBFBF",
                           font_size=10, text_align="l"))
    # Кнопка
    parts.append(roundrect(C(5.6), C(7.0), C(5.8), C(1.0),
                           text="Войти",
                           fill="2E75B6", line_color="2E75B6",
                           font_size=12, bold=True, font_color="FFFFFF"))
    # Ссылка регистрации
    parts.append(textbox(C(5), C(8.3), C(7), C(0.5),
                         "У меня ещё нет аккаунта",
                         font_size=10, font_color="2E75B6",
                         fill="", line_color=""))
    return diagram(17, 14, ''.join(parts), name="Screen_Login")


# ==========================================================
# 16. Диаграмма Ганта
# ==========================================================
def diagram_gantt():
    """Простая диаграмма Ганта."""
    parts = []
    # Подписи дней
    parts.append(textbox(C(0), C(0.2), C(5.5), C(0.5),
                         "Этап", font_size=10, bold=True,
                         fill="", line_color="", text_align="l"))
    # Шкала времени (12 столбцов = 12 недель)
    for w in range(12):
        x = 5.7 + w * 0.95
        parts.append(textbox(C(x), C(0.2), C(0.95), C(0.5),
                             f"Н{w + 1}", font_size=8, bold=True,
                             fill="", line_color=""))

    # Этапы (ярлык, неделя начала, длительность в неделях, цвет)
    stages = [
        ("Анализ предметной области", 0, 2, "DEEBF7", "2E75B6"),
        ("Анализ аналогов", 1, 1, "DEEBF7", "2E75B6"),
        ("Формирование требований", 2, 1, "DEEBF7", "2E75B6"),
        ("Проектирование архитектуры и БД", 2, 2, "FFF2CC", "BF9000"),
        ("Проектирование UI", 3, 2, "FFF2CC", "BF9000"),
        ("Реализация серверной части", 4, 4, "E2EFDA", "548235"),
        ("Реализация мобильного клиента", 5, 5, "E2EFDA", "548235"),
        ("Интеграция и отладка", 9, 1, "FCE4D6", "C65911"),
        ("Функциональное тестирование", 9, 2, "FCE4D6", "C65911"),
        ("Подготовка ВКР", 6, 5, "F2F2F2", "808080"),
        ("Защита ВКР", 11, 1, "FFD7D7", "C00000"),
    ]
    y = 0.9
    for label, start, dur, fill, line_color in stages:
        # Подпись
        parts.append(textbox(C(0), C(y + 0.05), C(5.5), C(0.4),
                             label, font_size=9,
                             fill="", line_color="", text_align="l"))
        # Полоса
        bx = 5.7 + start * 0.95
        bw = dur * 0.95
        parts.append(rect(C(bx), C(y), C(bw), C(0.4), text="",
                          fill=fill, line_color=line_color))
        y += 0.55
    # Нижняя ось
    parts.append(line(C(5.7), C(y + 0.1), C(5.7 + 12 * 0.95), C(y + 0.1)))
    return diagram(17.5, y + 0.5, ''.join(parts), name="Gantt")


# ==========================================================
# 17. Структура сметной стоимости (круговая, упрощённо как столбчатая)
# ==========================================================
def diagram_cost_structure():
    """Столбчатая диаграмма распределения затрат."""
    parts = []
    items = [
        ("Зарплата разработчика", 138600, "2E75B6"),
        ("Страховые взносы (30,2 %)", 41857, "BF9000"),
        ("Накладные расходы (20 %)", 36091, "548235"),
        ("Амортизация оборудования", 6300, "C65911"),
        ("ПО и сервисы", 2400, "808080"),
    ]
    total = sum(v for _, v, _ in items)
    # Заголовок
    parts.append(textbox(C(0), C(0.2), C(17), C(0.6),
                         f"Структура сметной стоимости разработки, итого {total:,} ₽".replace(",", " "),
                         font_size=11, bold=True,
                         fill="", line_color=""))
    # Столбцы
    max_w = 12.0  # макс ширина бара в см
    y = 1.2
    for name, value, color in items:
        share = value / total
        bar_w = share * max_w
        # подпись слева
        parts.append(textbox(C(0), C(y), C(4.5), C(0.6),
                             name, font_size=9,
                             fill="", line_color="", text_align="l"))
        # столбец
        parts.append(rect(C(4.7), C(y + 0.05), C(bar_w), C(0.5), text="",
                          fill=color, line_color=color))
        # значение
        parts.append(textbox(C(4.7 + bar_w + 0.1), C(y), C(4.5), C(0.6),
                             f"{value:,} ₽ ({share * 100:.1f} %)".replace(",", " "),
                             font_size=9,
                             fill="", line_color="", text_align="l"))
        y += 0.85
    return diagram(17, y + 0.3, ''.join(parts), name="CostStructure")


# ==========================================================
# 18. Блок-схема пользовательского сценария (для приложения Б)
# ==========================================================
def diagram_user_flowchart():
    parts = []
    # Старт
    parts.append(ellipse(C(7), C(0.2), C(3), C(0.8), text="Старт",
                         fill="E2EFDA", line_color="548235",
                         font_size=10, bold=True))
    parts.append(arrow(C(8.5), C(1.0), C(8.5), C(1.5)))

    # Запуск приложения
    parts.append(rect(C(6), C(1.5), C(5), C(0.8),
                      text="Запуск приложения",
                      fill="DEEBF7", line_color="2E75B6",
                      font_size=10))
    parts.append(arrow(C(8.5), C(2.3), C(8.5), C(2.8)))

    # Решение: токен есть?
    parts.append(diamond(C(6), C(2.8), C(5), C(1.4),
                         text="Токен сохранён?",
                         fill="FFF2CC", line_color="BF9000",
                         font_size=10, bold=True))
    parts.append(arrow(C(11), C(3.5), C(13), C(3.5)))
    parts.append(textbox(C(11), C(3.0), C(2), C(0.4),
                         "Да", font_size=9, fill="", line_color=""))
    parts.append(arrow(C(8.5), C(4.2), C(8.5), C(4.7)))
    parts.append(textbox(C(8.7), C(4.2), C(1), C(0.4),
                         "Нет", font_size=9, fill="", line_color=""))

    # Авторизация
    parts.append(rect(C(6), C(4.7), C(5), C(0.8),
                      text="Авторизация / Регистрация",
                      fill="DEEBF7", line_color="2E75B6",
                      font_size=10))
    parts.append(arrow(C(8.5), C(5.5), C(8.5), C(6.0)))

    # Каталог (правая ветка)
    parts.append(rect(C(13), C(3.1), C(4), C(0.8),
                      text="Авто-вход",
                      fill="E2EFDA", line_color="548235",
                      font_size=10))
    parts.append(arrow(C(15), C(3.9), C(15), C(6.0)))
    parts.append(arrow(C(15), C(6.0), C(11), C(6.4)))

    # Каталог
    parts.append(rect(C(6), C(6.0), C(5), C(0.8),
                      text="Просмотр каталога",
                      fill="DEEBF7", line_color="2E75B6",
                      font_size=10))
    parts.append(arrow(C(8.5), C(6.8), C(8.5), C(7.3)))

    # Решение: записан?
    parts.append(diamond(C(6), C(7.3), C(5), C(1.4),
                         text="Записан\nна курс?",
                         fill="FFF2CC", line_color="BF9000",
                         font_size=10, bold=True))
    parts.append(arrow(C(6), C(8.0), C(2.5), C(8.0)))
    parts.append(textbox(C(3), C(7.5), C(2.5), C(0.4),
                         "Нет", font_size=9, fill="", line_color=""))
    parts.append(arrow(C(8.5), C(8.7), C(8.5), C(9.2)))
    parts.append(textbox(C(8.7), C(8.7), C(1), C(0.4),
                         "Да", font_size=9, fill="", line_color=""))

    # Запись на курс
    parts.append(rect(C(0.5), C(7.6), C(5), C(0.8),
                      text="Запись на курс",
                      fill="DEEBF7", line_color="2E75B6",
                      font_size=10))
    parts.append(arrow(C(3), C(8.4), C(3), C(9.2)))
    parts.append(arrow(C(3), C(9.2), C(6), C(9.6)))

    # Прохождение урока
    parts.append(rect(C(6), C(9.2), C(5), C(0.8),
                      text="Прохождение урока",
                      fill="DEEBF7", line_color="2E75B6",
                      font_size=10))
    parts.append(arrow(C(8.5), C(10.0), C(8.5), C(10.5)))

    # Тест
    parts.append(rect(C(6), C(10.5), C(5), C(0.8),
                      text="Прохождение теста",
                      fill="DEEBF7", line_color="2E75B6",
                      font_size=10))
    parts.append(arrow(C(8.5), C(11.3), C(8.5), C(11.8)))

    # Тест пройден?
    parts.append(diamond(C(6), C(11.8), C(5), C(1.4),
                         text="Тест пройден?",
                         fill="FFF2CC", line_color="BF9000",
                         font_size=10, bold=True))
    parts.append(arrow(C(11), C(12.5), C(13), C(12.5)))
    parts.append(textbox(C(11), C(12.0), C(2), C(0.4),
                         "Да", font_size=9, fill="", line_color=""))
    parts.append(arrow(C(8.5), C(13.2), C(8.5), C(13.7)))
    parts.append(textbox(C(8.7), C(13.2), C(2), C(0.4),
                         "Нет, ещё уроки", font_size=8,
                         fill="", line_color=""))
    # Цикл — назад на урок
    parts.append(arrow(C(6), C(14), C(2), C(14)))
    parts.append(line(C(2), C(14), C(2), C(9.6)))
    parts.append(arrow(C(2), C(9.6), C(6), C(9.6)))

    # Все уроки пройдены — сертификат
    parts.append(rect(C(13), C(12.1), C(4), C(0.8),
                      text="Выдача сертификата",
                      fill="E2EFDA", line_color="548235",
                      font_size=10))
    parts.append(arrow(C(15), C(12.9), C(15), C(13.7)))

    # Конец
    parts.append(ellipse(C(13.5), C(13.7), C(3), C(0.8), text="Конец",
                         fill="E2EFDA", line_color="548235",
                         font_size=10, bold=True))

    return diagram(17.5, 14.8, ''.join(parts), name="UserFlowchart")
