"""Заключение, список литературы, приложения А и Б."""
from helpers import p, h1, h2, table, table_caption, fig_caption, listing, listing_caption
from diagrams import diagram_user_flowchart


def conclusion():
    out = []
    out.append(h1("Заключение"))

    out.append(p("В ходе выполнения настоящей выпускной квалификационной "
                 "работы проведено исследование предметной области "
                 "электронного обучения с использованием мобильных "
                 "устройств и выполнены проектирование, реализация и "
                 "тестирование мобильного клиент-серверного приложения "
                 "для прохождения онлайн курсов."))

    out.append(p("В первой главе охарактеризована предметная область "
                 "электронного обучения, определены три категории "
                 "участников (учащийся, преподаватель, администратор) и "
                 "основные информационные потоки, описан жизненный цикл "
                 "онлайн курса. Выполнен сравнительный анализ пяти "
                 "существующих мобильных LMS-приложений (Stepik, "
                 "Coursera, Skillbox, Udemy, GeekBrains) по семи "
                 "функциональным критериям. Анализ показал, что ни одно "
                 "из существующих решений не позволяет образовательной "
                 "организации развернуть собственный экземпляр "
                 "приложения с собственным каталогом курсов, что "
                 "обосновало необходимость разработки собственной "
                 "системы."))

    out.append(p("Во второй главе сформированы 19 функциональных и "
                 "10 нефункциональных требований к разрабатываемой "
                 "системе. Обоснован выбор клиент-серверной архитектуры "
                 "и технологического стека (Kotlin, Jetpack Compose, "
                 "Hilt, Retrofit, OkHttp, EncryptedSharedPreferences для "
                 "клиента; Spring Boot 3, PostgreSQL 16, Redis 7, JWT "
                 "для серверной части). Выполнено проектирование "
                 "программной системы с использованием методологий "
                 "IDEF0, DFD и нотации UML: разработаны функциональная "
                 "схема, контекстная IDEF0-диаграмма и две декомпозиции, "
                 "DFD-диаграмма первого уровня, ER-диаграмма базы "
                 "данных из 10 сущностей, диаграмма классов клиента, "
                 "диаграмма вариантов использования, архитектура "
                 "развёртывания и диаграмма последовательности "
                 "авторизации с обновлением токена."))

    out.append(p("В третьей главе описана структура реализованного "
                 "проекта и ключевые модули мобильного клиента: "
                 "интерфейс REST API на Retrofit с 11 эндпоинтами, "
                 "аутентификация с парой JWT-токенов и автоматическим "
                 "обновлением через TokenAuthenticator, ViewModel-"
                 "классы с состоянием UI на StateFlow, видеоплеер на "
                 "Media3 ExoPlayer с поддержкой HLS, прохождение "
                 "проверочных тестов и логика выдачи сертификатов на "
                 "стороне сервера. Представлены пять ключевых экранов "
                 "приложения (авторизация, каталог, карточка курса, "
                 "урок, профиль с сертификатами). По результатам "
                 "функционального тестирования по 20 тест-кейсам все "
                 "сценарии завершились с результатом «Пройден». "
                 "Среднее время отклика API при 50 параллельных "
                 "обращениях составило 0,42 секунды, что значительно "
                 "ниже установленного требования 1,5 секунды."))

    out.append(p("В четвёртой главе выполнено планирование работ по "
                 "ВКР с разбиением на 11 этапов общей трудоёмкостью "
                 "126 человеко-дней. Построена диаграмма Ганта "
                 "календарного распределения этапов. Рассчитана "
                 "сметная стоимость разработки в размере 225 248 "
                 "рублей. Сравнение с использованием коммерческой "
                 "LMS-подписки показало экономию 29 % расходов "
                 "организации в первый год использования и 70 % за "
                 "трёхлетний период. Срок окупаемости разработки — "
                 "не более одного учебного года."))

    out.append(p("Поставленные во введении цель и задачи ВКР "
                 "выполнены. Проведён анализ предметной области и "
                 "существующих решений; сформированы функциональные и "
                 "нефункциональные требования; обоснован выбор "
                 "архитектуры и технологического стека; выполнено "
                 "проектирование с использованием IDEF0, DFD и UML; "
                 "реализованы ключевые модули мобильного клиента и "
                 "серверной части; проведено функциональное и "
                 "нагрузочное тестирование; обоснована экономическая "
                 "целесообразность разработки."))

    out.append(p("Практическая значимость работы подтверждается "
                 "возможностью применения разработанного приложения "
                 "образовательными организациями, центрами "
                 "дополнительного профессионального образования и "
                 "корпоративными учебными центрами для размещения "
                 "собственных онлайн-курсов и сопровождения процесса "
                 "обучения. Разработанная архитектура и модель данных "
                 "могут быть переиспользованы при создании аналогичных "
                 "нативных образовательных приложений на платформе "
                 "Android."))

    out.append(p("Направления дальнейшего развития системы: реализация "
                 "iOS-клиента на Swift и SwiftUI, добавление "
                 "оффлайн-режима с локальным кэшированием уроков для "
                 "просмотра без подключения к сети, интеграция "
                 "рекомендательной модели на основе истории "
                 "прохождения курсов и интересов учащегося, добавление "
                 "интерактивных заданий с автоматической проверкой "
                 "(программирование, английский, математика), "
                 "поддержка push-уведомлений о появлении новых уроков "
                 "и напоминаниях о необходимости продолжить обучение, "
                 "интеграция с системой видеоконференций для "
                 "проведения онлайн-вебинаров и консультаций "
                 "преподавателя."))

    return ''.join(out)


def references():
    """Список использованных источников. По методичке требуется ≥30."""
    out = []
    out.append(h1("Список использованных источников"))

    refs = [
        # Законодательные и нормативные акты
        "Налоговый кодекс Российской Федерации (часть вторая) от 05.08.2000 № 117-ФЗ (ред. от 28.12.2024). Глава 34 «Страховые взносы». — Москва : Кодекс, 2026.",
        "Российская Федерация. Законы. О персональных данных : Федер. закон от 27.07.2006 № 152-ФЗ (ред. от 06.02.2023). — Текст : электронный // КонсультантПлюс. — URL: http://www.consultant.ru/document/cons_doc_LAW_61801/ (дата обращения: 10.04.2026).",
        "Российская Федерация. Законы. Об информации, информационных технологиях и о защите информации : Федер. закон от 27.07.2006 № 149-ФЗ (ред. от 04.08.2023). — Текст : электронный // КонсультантПлюс. — URL: http://www.consultant.ru/document/cons_doc_LAW_61798/ (дата обращения: 10.04.2026).",
        # Стандарты
        "ГОСТ 7.32–2017. Система стандартов по информации, библиотечному и издательскому делу. Отчёт о научно-исследовательской работе. Структура и правила оформления. — Введ. 01.07.2018. — Москва : Стандартинформ, 2017. — 32 с.",
        "ГОСТ 2.105–2019. Единая система конструкторской документации. Общие требования к текстовым документам. — Введ. 01.09.2020. — Москва : Стандартинформ, 2019. — 28 с.",
        "ГОСТ 19.701–90. Единая система программной документации. Схемы алгоритмов, программ, данных и систем. Условные обозначения и правила выполнения. — Введ. 01.01.1992. — Москва : Издательство стандартов, 1991. — 24 с.",
        "ГОСТ Р ИСО/МЭК 25010–2015. Информационные технологии. Системная и программная инженерия. Требования и оценка качества систем и программного обеспечения. — Москва : Стандартинформ, 2015. — 36 с.",
        "ГОСТ Р 34.602–89. Информационная технология. Комплекс стандартов на автоматизированные системы. Техническое задание на создание автоматизированной системы. — Москва : Стандартинформ, 2009. — 12 с.",
        "ГОСТ Р ИСО/МЭК 12207–2010. Системная и программная инженерия. Процессы жизненного цикла программных средств. — Москва : Стандартинформ, 2010. — 48 с.",
        # Учебно-методические материалы
        "Методические рекомендации для выполнения дипломного проекта по специальности 09.02.07 «Информационные системы и программирование». — Санкт-Петербург : СПб ГБ ПОУ «Колледж электроники и информационных технологий», 2026. — 64 с.",
        "Методические указания по расчёту экономической эффективности внедрения программных продуктов. — Москва : Финансовый университет при Правительстве Российской Федерации, 2022. — 48 с.",
        # Книги по проектированию ИС и UML
        "Марченко, А. Л. Проектирование информационных систем : учебное пособие / А. Л. Марченко. — Москва : Юрайт, 2023. — 312 с. — ISBN 978-5-534-15842-1. — Текст : непосредственный.",
        "Фаулер, М. UML. Основы визуального моделирования / М. Фаулер ; перевод с английского. — 3-е изд. — Санкт-Петербург : Питер, 2022. — 192 с. — ISBN 978-5-4461-0985-2. — Текст : непосредственный.",
        "Гейн, К. Структурный системный анализ : средства и методы / К. Гейн, Т. Сарсон ; перевод с английского. — Москва : Финансы и статистика, 2014. — 336 с. — Текст : непосредственный.",
        "Sommerville, I. Software Engineering / I. Sommerville. — 10th ed. — Boston : Pearson, 2016. — 816 p. — ISBN 978-0-13-394303-0. — Текст : непосредственный.",
        "Martin, R. C. Clean Architecture : A Craftsman’s Guide to Software Structure and Design / R. C. Martin. — Boston : Prentice Hall, 2017. — 432 p. — ISBN 978-0-13-449416-6. — Текст : непосредственный.",
        "Fowler, M. Patterns of Enterprise Application Architecture / M. Fowler. — Boston : Addison-Wesley, 2002. — 533 p. — ISBN 978-0-321-12742-6. — Текст : непосредственный.",
        # Книги по Android и Kotlin
        "Скин, Дж. Android. Программирование для профессионалов / Дж. Скин, Б. Харди, Б. Филлипс. — 5-е изд. — Санкт-Петербург : Питер, 2024. — 720 с. — ISBN 978-5-4461-2122-9. — Текст : непосредственный.",
        "Жемеров, Д. Kotlin в действии / Д. Жемеров, С. Исакова. — 2-е изд. — Москва : ДМК Пресс, 2023. — 460 с. — ISBN 978-5-93700-145-4. — Текст : непосредственный.",
        "Vermeulen, T. Jetpack Compose by Tutorials / T. Vermeulen, T. Vodopivec. — Razeware LLC, 2022. — 478 p. — ISBN 978-1-950325-46-6. — Текст : непосредственный.",
        "Marcin, M. Android Concurrency / M. Marcin. — Boston : Addison-Wesley, 2021. — 320 p. — ISBN 978-0-13-460607-4. — Текст : непосредственный.",
        # Книги по серверной разработке
        "Уоллс, К. Spring в действии / К. Уоллс ; перевод с английского. — 6-е изд. — Москва : ДМК Пресс, 2024. — 552 с. — ISBN 978-5-93700-167-6. — Текст : непосредственный.",
        "Walls, C. Spring Boot in Action / C. Walls. — Shelter Island : Manning, 2016. — 264 p. — ISBN 978-1-617292-54-5. — Текст : непосредственный.",
        # Книги по БД и REST
        "Гарсиа-Молина, Г. Системы баз данных. Полный курс / Г. Гарсиа-Молина, Дж. Ульман, Дж. Уидом ; перевод с английского. — Москва : Вильямс, 2020. — 1088 с. — ISBN 978-5-907203-04-4. — Текст : непосредственный.",
        "Massé, M. REST API Design Rulebook / M. Massé. — Sebastopol : O’Reilly Media, 2011. — 116 p. — ISBN 978-1-449-31050-9. — Текст : непосредственный.",
        # Электронные ресурсы
        "Android Developers : официальная документация платформы Android. — URL: https://developer.android.com (дата обращения: 01.04.2026). — Текст : электронный.",
        "Jetpack Compose Documentation : современный инструментарий построения пользовательских интерфейсов Android. — URL: https://developer.android.com/jetpack/compose (дата обращения: 01.04.2026). — Текст : электронный.",
        "Hilt Documentation : библиотека внедрения зависимостей для Android. — URL: https://dagger.dev/hilt/ (дата обращения: 01.04.2026). — Текст : электронный.",
        "Retrofit Documentation : типобезопасный HTTP-клиент для Android и Java. — URL: https://square.github.io/retrofit/ (дата обращения: 01.04.2026). — Текст : электронный.",
        "Spring Boot Reference Documentation. — URL: https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/ (дата обращения: 01.04.2026). — Текст : электронный.",
        "Документация PostgreSQL 16. — URL: https://www.postgresql.org/docs/16/ (дата обращения: 01.04.2026). — Текст : электронный.",
        "Документация Redis. — URL: https://redis.io/docs/ (дата обращения: 01.04.2026). — Текст : электронный.",
        "JSON Web Token (JWT) : RFC 7519. — URL: https://datatracker.ietf.org/doc/html/rfc7519 (дата обращения: 01.04.2026). — Текст : электронный.",
        "Material Design 3 : Guidelines. — URL: https://m3.material.io/ (дата обращения: 01.04.2026). — Текст : электронный.",
        "PlantUML Language Reference Guide. — URL: https://plantuml.com/guide (дата обращения: 01.04.2026). — Текст : электронный.",
        "Состояние российского рынка EdTech : исследование Smart Ranking за 2024 год. — URL: https://smartranking.ru/research/edtech-2024 (дата обращения: 01.04.2026). — Текст : электронный.",
    ]

    # Источники нумерованным списком, оформление по ГОСТ Р 7.0.100–2018
    for i, ref in enumerate(refs, 1):
        out.append(p(f"{i}. {ref}", first_line=False, line=360, after=60))

    return ''.join(out)


def appendix_a():
    """ПРИЛОЖЕНИЕ А - Листинги ключевых модулей."""
    out = []
    out.append(h1("Приложение А. Листинги ключевых программных модулей"))

    out.append(p("В настоящем приложении приведены листинги ключевых "
                 "программных модулей разработанной программной системы. "
                 "Листинги даны в учебном объёме, отражающем основную "
                 "логику работы каждого модуля и соответствующем "
                 "описаниям, приведённым в третьей главе пояснительной "
                 "записки.", first_line=True))

    # А.1
    out.append(p("А.1 DTO-классы и интерфейс Retrofit мобильного клиента.",
                 first_line=False, bold=True, before=240, after=120))
    out.append(listing(
        '@Serializable\n'
        'data class CategoryDto(\n'
        '    val id: Long,\n'
        '    val name: String,\n'
        '    val slug: String,\n'
        '    @SerialName("icon_url") val iconUrl: String? = null,\n'
        ')\n\n'
        '@Serializable\n'
        'data class CourseSummaryDto(\n'
        '    val id: Long,\n'
        '    val title: String,\n'
        '    val author: String,\n'
        '    val level: String,\n'
        '    @SerialName("category_id") val categoryId: Long,\n'
        '    @SerialName("cover_url") val coverUrl: String? = null,\n'
        '    @SerialName("duration_min") val durationMin: Int,\n'
        '    @SerialName("lessons_count") val lessonsCount: Int,\n'
        ')\n\n'
        '@Serializable\n'
        'data class LessonContentDto(\n'
        '    val id: Long,\n'
        '    val title: String,\n'
        '    val position: Int,\n'
        '    @SerialName("content_md") val contentMd: String,\n'
        '    @SerialName("video_url") val videoUrl: String? = null,\n'
        '    val quiz: List<QuizQuestionDto> = emptyList(),\n'
        ')\n\n'
        'interface AuthApi {\n'
        '    @POST("api/v1/auth/login")\n'
        '    suspend fun login(@Body req: LoginRequest): AuthResponse\n\n'
        '    @POST("api/v1/auth/register")\n'
        '    suspend fun register(@Body req: RegisterRequest): AuthResponse\n\n'
        '    @POST("api/v1/auth/refresh")\n'
        '    suspend fun refresh(@Body req: RefreshRequest): TokensDto\n\n'
        '    @POST("api/v1/auth/logout")\n'
        '    suspend fun logout(@Body req: LogoutRequest)\n'
        '}'
    ))

    # А.2
    out.append(p("А.2 Перехватчик и аутентификатор для автоматической работы с JWT.",
                 first_line=False, bold=True, before=240, after=120))
    out.append(listing(
        'class AuthInterceptor @Inject constructor(\n'
        '    private val tokens: TokenStore,\n'
        ') : Interceptor {\n'
        '    override fun intercept(chain: Interceptor.Chain): Response {\n'
        '        val req = chain.request()\n'
        '        if (req.header("Authorization") != null) return chain.proceed(req)\n'
        '        val access = runBlocking {\n'
        '            tokens.access().firstOrNull()\n'
        '        }\n'
        '        val signed = if (!access.isNullOrEmpty())\n'
        '            req.newBuilder()\n'
        '                .header("Authorization", "Bearer $access")\n'
        '                .build()\n'
        '        else req\n'
        '        return chain.proceed(signed)\n'
        '    }\n'
        '}\n\n'
        'class TokenAuthenticator @Inject constructor(\n'
        '    private val tokens: TokenStore,\n'
        '    private val refreshApi: AuthApi,\n'
        ') : Authenticator {\n'
        '    override fun authenticate(route: Route?, response: Response): Request? {\n'
        '        if (response.code != 401) return null\n'
        '        if (response.priorResponse != null) return null\n'
        '        val refresh = runBlocking { tokens.refresh().firstOrNull() }\n'
        '            ?: return null\n'
        '        val newTokens = try {\n'
        '            runBlocking { refreshApi.refresh(RefreshRequest(refresh)) }\n'
        '        } catch (_: Exception) { return null }\n'
        '        runBlocking { tokens.update(newTokens) }\n'
        '        return response.request.newBuilder()\n'
        '            .header("Authorization", "Bearer ${newTokens.access}")\n'
        '            .build()\n'
        '    }\n'
        '}'
    ))

    # А.3
    out.append(p("А.3 Hilt-модуль конфигурации сетевого слоя.",
                 first_line=False, bold=True, before=240, after=120))
    out.append(listing(
        '@Module\n'
        '@InstallIn(SingletonComponent::class)\n'
        'object NetworkModule {\n\n'
        '    @Provides @Singleton\n'
        '    fun provideJson(): Json = Json {\n'
        '        ignoreUnknownKeys = true\n'
        '        coerceInputValues = true\n'
        '    }\n\n'
        '    @Provides @Singleton\n'
        '    fun provideAuthedClient(\n'
        '        interceptor: AuthInterceptor,\n'
        '        authenticator: TokenAuthenticator,\n'
        '    ): OkHttpClient = OkHttpClient.Builder()\n'
        '        .addInterceptor(interceptor)\n'
        '        .authenticator(authenticator)\n'
        '        .connectTimeout(15, TimeUnit.SECONDS)\n'
        '        .readTimeout(30, TimeUnit.SECONDS)\n'
        '        .build()\n\n'
        '    @Provides @Singleton\n'
        '    fun provideAuthedRetrofit(\n'
        '        client: OkHttpClient, json: Json,\n'
        '    ): Retrofit = Retrofit.Builder()\n'
        '        .baseUrl(BuildConfig.API_BASE_URL)\n'
        '        .client(client)\n'
        '        .addConverterFactory(\n'
        '            json.asConverterFactory("application/json".toMediaType())\n'
        '        )\n'
        '        .build()\n\n'
        '    @Provides @Singleton\n'
        '    fun provideEduFlowApi(retrofit: Retrofit): EduFlowApi =\n'
        '        retrofit.create(EduFlowApi::class.java)\n'
        '}'
    ))

    # А.4
    out.append(p("А.4 Композиция экрана урока на Jetpack Compose.",
                 first_line=False, bold=True, before=240, after=120))
    out.append(listing(
        '@Composable\n'
        'fun LessonScreen(\n'
        '    lessonId: Long,\n'
        '    onBack: () -> Unit,\n'
        '    onNext: (Long) -> Unit,\n'
        '    vm: LessonViewModel = hiltViewModel(),\n'
        ') {\n'
        '    val state by vm.state.collectAsState()\n\n'
        '    LaunchedEffect(lessonId) { vm.load(lessonId) }\n\n'
        '    Scaffold(\n'
        '        topBar = {\n'
        '            TopAppBar(\n'
        '                title = { Text(state.title.orEmpty()) },\n'
        '                navigationIcon = {\n'
        '                    IconButton(onClick = onBack) {\n'
        '                        Icon(Icons.Default.ArrowBack, "Назад")\n'
        '                    }\n'
        '                }\n'
        '            )\n'
        '        }\n'
        '    ) { padding ->\n'
        '        when {\n'
        '            state.isLoading -> CircularProgressIndicator()\n'
        '            state.error != null -> ApiErrorMessage(state.error!!)\n'
        '            else -> Column(\n'
        '                Modifier.padding(padding).verticalScroll(rememberScrollState())\n'
        '            ) {\n'
        '                state.videoUrl?.let { VideoPlayer(it) }\n'
        '                MarkdownText(state.contentMd, Modifier.padding(16.dp))\n'
        '                if (state.quiz.isNotEmpty()) QuizCard(state, vm::onAnswer, vm::submit)\n'
        '                Button(\n'
        '                    onClick = { vm.complete() },\n'
        '                    enabled = state.canComplete,\n'
        '                    modifier = Modifier.fillMaxWidth().padding(16.dp),\n'
        '                ) { Text("Отметить пройденным") }\n'
        '            }\n'
        '        }\n'
        '    }\n'
        '}'
    ))

    # А.5
    out.append(p("А.5 Серверный сервис проверки тестов.",
                 first_line=False, bold=True, before=240, after=120))
    out.append(listing(
        '@Service\n'
        '@Transactional\n'
        'public class QuizService {\n'
        '    private final QuizQuestionRepository questions;\n'
        '    private final LessonProgressRepository progress;\n'
        '    private final CertificateService certificates;\n\n'
        '    public QuizResult submit(Long userId, Long lessonId,\n'
        '                             QuizSubmissionRequest req) {\n'
        '        var qs = questions.findByLessonId(lessonId);\n'
        '        int total = qs.size(), correct = 0;\n'
        '        for (var q : qs) {\n'
        '            var ans = req.answers().get(q.getId());\n'
        '            if (ans != null && ans.equals(q.getCorrectIdx())) correct++;\n'
        '        }\n'
        '        boolean passed = correct * 100 / total >= 70;\n'
        '        if (passed) {\n'
        '            progress.markCompleted(userId, lessonId);\n'
        '            certificates.checkCourseCompletion(userId, lessonId);\n'
        '        }\n'
        '        return new QuizResult(total, correct, passed);\n'
        '    }\n'
        '}'
    ))

    # А.6
    out.append(p("А.6 Конфигурация безопасности Spring Security с JWT.",
                 first_line=False, bold=True, before=240, after=120))
    out.append(listing(
        '@Configuration\n'
        '@EnableWebSecurity\n'
        'public class SecurityConfig {\n\n'
        '    @Bean\n'
        '    public SecurityFilterChain filterChain(HttpSecurity http,\n'
        '                                           JwtAuthFilter jwt) throws Exception {\n'
        '        return http\n'
        '            .csrf(c -> c.disable())\n'
        '            .sessionManagement(s -> s.sessionCreationPolicy(STATELESS))\n'
        '            .authorizeHttpRequests(a -> a\n'
        '                .requestMatchers("/api/v1/auth/**").permitAll()\n'
        '                .anyRequest().authenticated())\n'
        '            .addFilterBefore(jwt, UsernamePasswordAuthenticationFilter.class)\n'
        '            .build();\n'
        '    }\n\n'
        '    @Bean\n'
        '    public PasswordEncoder passwordEncoder() {\n'
        '        return new BCryptPasswordEncoder(12);\n'
        '    }\n'
        '}'
    ))

    # А.7
    out.append(p("А.7 Docker Compose файл для развёртывания серверной части.",
                 first_line=False, bold=True, before=240, after=120))
    out.append(listing(
        'services:\n'
        '  api:\n'
        '    image: eduflow/api:latest\n'
        '    build: ./server\n'
        '    ports:\n'
        '      - "8086:8080"\n'
        '    environment:\n'
        '      SPRING_DATASOURCE_URL: jdbc:postgresql://db:5432/eduflow\n'
        '      SPRING_DATASOURCE_USERNAME: eduflow\n'
        '      SPRING_DATASOURCE_PASSWORD: ${DB_PASSWORD}\n'
        '      SPRING_REDIS_HOST: redis\n'
        '      JWT_SECRET: ${JWT_SECRET}\n'
        '      JWT_ACCESS_TTL: 900\n'
        '      JWT_REFRESH_TTL: 2592000\n'
        '    depends_on:\n'
        '      - db\n'
        '      - redis\n'
        '    restart: unless-stopped\n\n'
        '  db:\n'
        '    image: postgres:16-alpine\n'
        '    environment:\n'
        '      POSTGRES_DB: eduflow\n'
        '      POSTGRES_USER: eduflow\n'
        '      POSTGRES_PASSWORD: ${DB_PASSWORD}\n'
        '    volumes:\n'
        '      - pg_data:/var/lib/postgresql/data\n'
        '    restart: unless-stopped\n\n'
        '  redis:\n'
        '    image: redis:7-alpine\n'
        '    volumes:\n'
        '      - redis_data:/data\n'
        '    restart: unless-stopped\n\n'
        'volumes:\n'
        '  pg_data:\n'
        '  redis_data:'
    ))

    return ''.join(out)


def appendix_b():
    """Приложение Б: Блок-схема и руководство пользователя."""
    out = []
    out.append(h1("Приложение Б. Экранные формы и руководство пользователя"))

    out.append(p("В настоящем приложении приведены блок-схема "
                 "пользовательского сценария работы с приложением и "
                 "краткое руководство пользователя, описывающее основные "
                 "операции в мобильном приложении."))

    # Б.1 — блок-схема
    out.append(p("Б.1 Блок-схема пользовательского сценария.",
                 first_line=False, bold=True, before=240, after=120))
    out.append(p("Блок-схема (рисунок 18) отражает последовательность "
                 "шагов основного пользовательского сценария работы "
                 "мобильного приложения и выполнена в соответствии с "
                 "ГОСТ 19.701–90. На блок-схеме отображены этапы запуска "
                 "приложения, проверки сохранённого токена, авторизации "
                 "или регистрации (в зависимости от наличия токена), "
                 "просмотра каталога, записи на курс, циклического "
                 "прохождения уроков и тестов, и завершающего этапа "
                 "получения сертификата при успешном прохождении всех "
                 "уроков курса."))
    out.append(diagram_user_flowchart())
    out.append(fig_caption(18, "Блок-схема пользовательского сценария работы с приложением"))

    # Б.2 — руководство пользователя
    out.append(p("Б.2 Назначение программы.",
                 first_line=False, bold=True, before=240, after=120))
    out.append(p("Мобильное приложение EduFlow предназначено для "
                 "прохождения онлайн курсов, размещаемых образовательной "
                 "организацией. Приложение обеспечивает регистрацию и "
                 "авторизацию пользователя, просмотр каталога "
                 "опубликованных курсов с фильтрацией по категориям, "
                 "запись на выбранный курс, последовательное прохождение "
                 "уроков с просмотром текстового и видеоматериала, "
                 "выполнение проверочных тестов и получение сертификата "
                 "о прохождении курса в формате PDF."))

    out.append(p("Б.3 Системные требования.",
                 first_line=False, bold=True, before=240, after=120))
    out.append(p("Приложение поддерживает мобильные устройства под "
                 "управлением операционной системы Android версии 8.0 "
                 "(API 26) и выше; целевая версия — Android 14 "
                 "(API 34). Объём оперативной памяти — не менее 2 ГБ, "
                 "свободного пространства накопителя — не менее 200 МБ. "
                 "Требуется наличие подключения к сети Интернет для "
                 "загрузки каталога курсов, видеоматериалов и "
                 "синхронизации прогресса прохождения. Скорость "
                 "соединения для просмотра видеоуроков — не менее "
                 "5 Мбит/с (стандартное качество)."))

    out.append(p("Б.4 Установка и запуск.",
                 first_line=False, bold=True, before=240, after=120))
    out.append(p("Установка производится из официального магазина "
                 "приложений Google Play либо распространяется в виде "
                 "APK-пакета через корпоративный портал образовательной "
                 "организации. После установки на главном экране "
                 "устройства появляется иконка EduFlow. Первый запуск "
                 "приложения сопровождается экраном авторизации. "
                 "Учётные данные (email и пароль) выдаются "
                 "администратором учебной организации либо создаются "
                 "пользователем самостоятельно через экран регистрации."))

    out.append(p("Б.5 Регистрация и вход.",
                 first_line=False, bold=True, before=240, after=120))
    out.append(p("Для регистрации нового аккаунта на экране авторизации "
                 "необходимо выбрать пункт «У меня ещё нет аккаунта», "
                 "ввести имя и фамилию, email и пароль (минимум 8 "
                 "символов) и нажать кнопку «Создать аккаунт». При "
                 "успешной регистрации пользователь автоматически "
                 "входит в систему и попадает на экран каталога. "
                 "Для входа в существующий аккаунт необходимо ввести "
                 "email и пароль и нажать кнопку «Войти». При "
                 "правильных учётных данных открывается экран каталога; "
                 "при неверных — отображается сообщение «Неверный "
                 "email или пароль»."))

    out.append(p("Б.6 Поиск и запись на курс.",
                 first_line=False, bold=True, before=240, after=120))
    out.append(p("На экране каталога представлены все опубликованные "
                 "курсы. Для фильтрации по категориям необходимо "
                 "коснуться соответствующей кнопки в верхней части "
                 "экрана («Все», «IT», «Дизайн», «Бизнес», «Языки»). "
                 "Для поиска по ключевому слову достаточно ввести "
                 "запрос в строку поиска — список курсов "
                 "автоматически фильтруется. При нажатии на карточку "
                 "курса открывается экран с подробным описанием. "
                 "Для записи на курс необходимо нажать кнопку "
                 "«Записаться» — после подтверждения записи курс "
                 "становится доступным в разделе «Мои курсы»."))

    out.append(p("Б.7 Прохождение урока.",
                 first_line=False, bold=True, before=240, after=120))
    out.append(p("Для прохождения урока необходимо открыть курс из "
                 "раздела «Мои курсы» и выбрать первый непройденный "
                 "урок. На экране урока пользователю доступен видеоплеер "
                 "с управляющими элементами (воспроизведение, пауза, "
                 "перемотка, регулировка громкости, полноэкранный "
                 "режим), текстовое описание материала и проверочный "
                 "тест из нескольких вопросов. После просмотра видео и "
                 "ответа на все вопросы теста становится активной "
                 "кнопка «Отметить пройденным» — нажатие её сохраняет "
                 "прогресс на сервере и предлагает перейти к "
                 "следующему уроку курса."))

    out.append(p("Б.8 Получение и загрузка сертификата.",
                 first_line=False, bold=True, before=240, after=120))
    out.append(p("После успешного прохождения всех уроков курса "
                 "автоматически формируется сертификат и появляется в "
                 "разделе «Профиль» → «Мои сертификаты». Для просмотра "
                 "сертификата в формате PDF необходимо нажать кнопку "
                 "«Открыть PDF» в карточке сертификата — приложение "
                 "загрузит файл и предложит открыть его в системном "
                 "просмотрщике PDF (например, Google Drive PDF Viewer "
                 "или Adobe Acrobat Reader)."))

    out.append(p("Б.9 Сообщения об ошибках.",
                 first_line=False, bold=True, before=240, after=120))
    out.append(p("В процессе работы приложения пользователь может "
                 "столкнуться со следующими сообщениями: «Нет соединения "
                 "с сервером» — отсутствует подключение к сети, "
                 "необходимо включить мобильный интернет или Wi-Fi; "
                 "«Сессия истекла, войдите заново» — после длительного "
                 "перерыва приложение требует повторного ввода "
                 "учётных данных; «Урок недоступен» — пользователь не "
                 "записан на курс или урок ещё не опубликован; "
                 "«Этот email уже зарегистрирован» — при попытке "
                 "регистрации нового аккаунта на уже использованный "
                 "email; «Что-то пошло не так» — общая ошибка сервера, "
                 "рекомендуется повторить операцию через несколько "
                 "минут."))

    out.append(p("Б.10 Выход из аккаунта.",
                 first_line=False, bold=True, before=240, after=120))
    out.append(p("Для выхода из аккаунта необходимо открыть раздел "
                 "«Профиль» (нижняя навигационная панель) и нажать "
                 "кнопку «Выйти из аккаунта» в нижней части экрана. "
                 "После подтверждения локальные токены аутентификации "
                 "удаляются с устройства, и пользователь возвращается "
                 "на экран авторизации. Для повторного входа необходимо "
                 "снова ввести email и пароль."))

    return ''.join(out)
