import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3

# Функция, позволяющая проговаривать слова
# Принимает параметр "Слова" и прогроваривает их
def talk(words):
	print(words)  # Дополнительно выводим на экран
	engine = pyttsx3.init()
	engine.say(words)
	engine.runAndWait()

# Вызов функции и передача строки
# именно эта строка будет проговорена компьютером
talk("Слушаю, босс")

""" 
	Функция command() служит для отслеживания микрофона.
	Вызывая функцию мы будет слушать что скажет пользователь,
	при этом для прослушивания будет использован микрофон.
	Получение данные будут сконвертированы в строку и далее
	будет происходить их проверка.
"""
def command():
	# Создаем объект на основе библиотеки
	# speech_recognition и вызываем метод для определения данных
	r = sr.Recognizer()

	# Начинаем прослушивать микрофон и записываем данные в source
	with sr.Microphone() as source:
		# Просто вывод, чтобы мы знали когда говорить
		print("Говорите")
		# Устанавливаем паузу, чтобы прослушивание
		# началось лишь по прошествию 1 секунды
		r.pause_threshold = 1
		# используем adjust_for_ambient_noise для удаления
		# посторонних шумов из аудио дорожки
		r.adjust_for_ambient_noise(source, duration=1)
		# Полученные данные записываем в переменную audio
		# пока мы получили лишь mp3 звук
		audio = r.listen(source)

	try: # Обрабатываем все при помощи исключений
		""" 
		Распознаем данные из mp3 дорожки.
		Указываем что отслеживаемый язык русский.
		Благодаря lower() приводим все в нижний регистр.
		Теперь мы получили данные в формате строки,
		которые спокойно можем проверить в условиях
		"""
		zadanie = r.recognize_google(audio, language="ru-RU").lower()
		# Просто отображаем текст что сказал пользователь
		print("Вы сказали: " + zadanie)
	# Если не смогли распознать текст, то будет вызвана эта ошибка
	except sr.UnknownValueError:
		# Здесь просто проговариваем слова "Я вас не поняла"
		# и вызываем снова функцию command() для
		# получения текста от пользователя
		# talk("Я вас не поняла")
		zadanie = command()

	# В конце функции возвращаем текст задания
	# или же повторный вызов функции
	return zadanie

# Данная функция служит для проверки текста,
# что сказал пользователь (zadanie - текст от пользователя)
def makeSomething(zadanie):
	if 'стоп' in zadanie:
		talk('Прощайте, босс')
		sys.exit()
	elif 'открой мой сайт' in zadanie:
		talk('Уже открываю')
		url = 'https://dragonswealth.ru/'
		webbrowser.open(url)
	elif 'как тебя зовут' in zadanie:
		talk('Меня зовут Пятница')
	elif 'открой youtube' in zadanie:
		talk('Уже открываю ютубчик')
		url = 'https://www.youtube.com/'
		webbrowser.open(url)
	elif 'включи музыку' in zadanie:
		talk('Звук поставим на всю и соседи не спят')
		url = 'https://radio.yandex.ru/user/thebreadenergy86'
		webbrowser.open(url)
	elif 'мне плохо' in zadanie:
		talk('Послушай меня, дружочек')
		url = 'https://youtu.be/YJhN81WAXuc?t=113'
		webbrowser.open(url)
# Вызов функции для проверки текста будет
# осуществляться постоянно, поэтому здесь
# прописан бесконечный цикл while
while True:
	makeSomething(command())
