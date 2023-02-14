import random
again, wincnt, failcnt = 'д', 0, 0   # Полстянов проект игра висеkица.
def getword():
    lst = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'работа', 'слово', 'место',    # список взят из открытого источника
    'вопрос', 'лицо', 'глаз', 'страна', 'друг', 'сторона', 'дом', 'случай', 'ребенок', 'голова',
    'система', 'вид', 'конец', 'отношение', 'город', 'часть', 'женщина', 'проблема', 'земля',
    'решение', 'власть', 'машина', 'закон', 'час', 'образ', 'отец', 'история', 'нога', 'вода',
    'война', 'возможность', 'компания', 'результат', 'дверь', 'народ', 'область', 'число',
    'голос', 'развитие', 'группа', 'жена', 'процесс', 'условие', 'книга', 'ночь', 'суд', 'деньга',
    'уровень', 'начало', 'государство', 'стол', 'средство', 'связь', 'имя', 'президент', 'форма',
    'путь', 'организация', 'качество', 'действие', 'статья', 'общество', 'ситуация', 'деятельность',
    'школа', 'душа', 'дорога', 'язык', 'взгляд', 'момент', 'минута', 'месяц', 'порядок', 'цель',
    'программа', 'муж', 'помощь', 'мысль', 'вечер', 'орган', 'правительство', 'рынок', 'предприятие',
    'партия', 'роль', 'смысл', 'мама', 'мера', 'улица', 'состояние', 'задача', 'информация', 'театр',
    'внимание', 'производство', 'квартира', 'труд', 'тело', 'письмо', 'центр', 'утро', 'мать', 'комната',
    'семья', 'сын', 'смерть', 'положение', 'интерес', 'федерация', 'век', 'идея', 'управление', 'автор',
    'окно', 'ответ', 'совет', 'разговор', 'мужчина', 'ряд', 'счет', 'мнение', 'цена', 'точка', 'план',
    'проект', 'глава', 'материал', 'основа', 'причина', 'движение', 'культура', 'сердце', 'рубль', 'наука',
    'документ', 'неделя', 'вещь', 'чувство', 'правило', 'служба', 'газета', 'срок', 'институт', 'ход',
    'стена', 'директор', 'плечо', 'опыт', 'встреча', 'принцип', 'событие', 'структура', 'количество', 'товарищ',
    'создание', 'значение', 'объект', 'гражданин', 'очередь', 'период', 'образование', 'состав', 'пример',
    'лес', 'исследование', 'девушка', 'данные', 'палец', 'судьба', 'тип', 'метод', 'политика', 'армия', 'брат',
    'представитель', 'борьба', 'использование', 'шаг', 'игра', 'участие', 'территория', 'край', 'размер', 'номер',
    'район', 'население', 'банк', 'начальник', 'класс', 'зал', 'изменение', 'большинство', 'характер', 'кровь',
    'направление', 'позиция', 'герой', 'течение', 'девочка', 'искусство', 'гость', 'воздух', 'мальчик', 'фильм',
    'договор', 'регион', 'выбор', 'свобода', 'врач', 'экономика', 'небо', 'факт', 'церковь', 'завод', 'фирма',
    'бизнес', 'союз', 'деньги', 'специалист', 'род', 'команда', 'руководитель', 'спина', 'дух', 'музыка',
    'способ', 'хозяин', 'поле', 'доллар', 'память', 'природа', 'дерево', 'оценка', 'объем', 'картина',
    'процент', 'требование', 'писатель', 'сцена', 'анализ', 'основание', 'повод', 'вариант', 'берег',
    'модель', 'степень', 'самолет', 'телефон', 'граница', 'песня', 'половина', 'министр', 'угол', 'зрение',
    'предмет', 'литература', 'операция', 'двор', 'спектакль', 'руководство', 'солнце', 'автомобиль', 'родитель',
    'участник', 'журнал', 'база', 'пространство', 'защита', 'название', 'стих', 'море', 'удар', 'знание',
    'солдат', 'миллион', 'строительство', 'технология', 'председатель', 'сон', 'сознание', 'бумага', 'реформа',
    'оружие', 'линия', 'текст', 'выход', 'ребята', 'магазин', 'соответствие', 'участок', 'услуга', 'поэт',
    'предложение', 'желание', 'пара', 'успех', 'среда', 'возраст', 'комплекс', 'бюджет', 'представление',
    'площадь', 'генерал', 'господин', 'дочь', 'понятие', 'кабинет', 'безопасность', 'фонд', 'сфера', 'папа',
    'сотрудник', 'продукция', 'будущее', 'продукт', 'содержание', 'художник', 'республика', 'сумма', 'контроль',
    'парень', 'ветер', 'хозяйство', 'помочь', 'курс', 'губа', 'река', 'грудь', 'огонь', 'нос', 'волос', 'ухо',
    'отсутствие', 'радость', 'сад', 'подготовка', 'необходимость', 'доктор', 'лето', 'камень', 'здание',
    'капитан', 'собака', 'итог', 'рис', 'техника', 'элемент', 'источник', 'деревня', 'депутат', 'проведение',
    'рот', 'масса', 'комиссия', 'цвет', 'рассказ', 'функция', 'определение', 'мужик', 'обеспечение',
    'обстоятельство', 'работник', 'разработка', 'лист', 'звезда', 'гора', 'применение', 'победа', 'товар',
    'воля', 'зона', 'предел', 'целое', 'личность', 'офицер', 'влияние', 'поддержка', 'ответственность']
    return random.choice(lst)
def hanger(tries):
    stages = [
        f'''
        
       (x . x)
         (x)
----ooO-------- {name}-
|                     |
|  П О Р А Ж Е Н И Е  |
|                     |
| Слово: {wrdcmpl}
|                     |
'---------------ooO---'
  Слово из {len(word)} букв. 
       /  ^  \  
      (__/ \__)  
        ''',
        f'''
        
        (‘～ )
         (_ )
----ooO-------- {name}-
|                     |
|      1 попытка      |
|                     |
| Слово: {wrdcmpl}
|                     |
'---------------ooO---'
  Слово из {len(word)} букв.
       /  ^  \  
      (__/ \__)  
Введенные ранее буквы: {gsdltrs}
        ''',
        f'''
        
        (◕‿◕)
         ( )
----ooO-------- {name}-
|                     |
|      2 попытки      |
|                     |
| Слово: {wrdcmpl}
|                     |
'---------------ooO---'
  Слово из {len(word)} букв.
       /  ^  \  
      (__/ \__)  
Введенные ранее буквы: {gsdltrs}
        ''',
        f'''
        
      (　￣д￣)
        ( _ )
----ooO-------- {name}-
|                     |
|      3 попытки      |
|                     |
| Слово: {wrdcmpl}
|                     |
'---------------ooO---'
  Слово из {len(word)} букв.
       /  ^  \  
      (__/ \__)  
Введенные ранее буквы: {gsdltrs}
        ''',
        f'''
        
       (￣ヘ￣)
         ( _)
----ooO-------- {name}-
|                     |
|      4 попытки      |
|                     |
| Слово: {wrdcmpl}
|                     |
'---------------ooO---'
  Слово из {len(word)} букв.
       /  ^  \  
      (__/ \__)  
Введенные ранее буквы: {gsdltrs}
        ''',
        f'''
        
      ( ˘ ､ ˘ )
        ( ^ )
----ooO-------- {name}-
|                     |
|      5 попыток      |
|                     |
| Слово: {wrdcmpl}
|                     |
'---------------ooO---'
  Слово из {len(word)} букв.
       /  ^  \  
      (__/ \__)  
Введенные ранее буквы: {gsdltrs}
        ''',
        f'''
       (ー_ー )
         (_)
----ooO-------- {name}-
|                     |
|      6 попыток      |
|                     |
| Слово: {wrdcmpl}
|                     |
'---------------ooO---'
  Слово из {len(word)} букв.
       /  ^  \  
      (__/ \__)  

      ''',
        f'''
        
       (()‿())
        ( _ )
----ooO-------- {name}-
|                     |
|     П О Б Е Д А     |
|                     |
| Слово: {wrdcmpl}
|                     |
'---------------ooO---'
  Слово из {len(word)} букв.
       /  ^  \  
      (__/ \__)  
      '''
    ]
    return stages[tries]
def dmbprtct(npt):
    if not npt.isalpha():
        print(f'{name}, Надо было вводить букву или слово.')
    elif len(npt) > 1:
        if npt in gsdwrds:
            print(f'{name}, такое слово уже было.')
        else:
            gsdwrds.append(npt)
            return True
    elif len(npt) == 1:
        if npt in gsdltrs:
            print(f'{name}, такая буква уже была.')
        else:
            gsdltrs.append(npt)
            return True
def play(word):
    global wincnt, failcnt, wrdcmpl
    tries = 6  # количество попыток
    while 7 > tries > 0:
        print(hanger(tries))
        npt = input().upper()
        if npt == 'GOD':
            print(word)
            tries = 6
        elif dmbprtct(npt):
            if npt == word:
                tries = 7
                wrdcmpl = word
                print(hanger(tries))
                print(f'Твоя победа {name}.\n\n')
                wincnt += 1
                break
            elif len(npt) > 1 and npt != word:
                if tries > 3:
                    tries -= 3
                else:
                    tries = 0
                    print(hanger(tries))
                    break
            elif npt not in word:
                tries -= 1
                print('Буквы', npt, 'в слове нет!')
            elif npt in word:
                print('Буква', npt, 'в слове есть!')
                wlist = list(wrdcmpl)
                indices = [i for i in range(len(word)) if word[i] == npt]
                for index in indices:
                    wlist[index] = npt
                wrdcmpl = ''.join(wlist)
                if '-' not in wrdcmpl:
                    wrdcmpl = word
                    tries = 7
                    print(hanger(tries))
                    print('Твоя победа.\n\n')
                    wincnt += 1
                    break
        # elif dmbprtct(npt) == False:
        #     continue
    else:
        print(hanger(tries))
        failcnt += 1
        print('Тара-пара-пам поражение!\n\n')
name = input('Как тебя зовут?(Читрежим=god): ')
while True:
    if again.lower() in 'д да ок хорошо конечно ага давай yes sure ok common yea yeah yep real go':
        gsdltrs = []  # список названных букв
        gsdwrds = []
        word = getword().upper()
        if name.lower() == 'god':
            print(word,word,word,word,word,word,word,word,word,word, sep='\n\t\t\t')
        wrdcmpl = '-' * len(word)  # переменная кодирующая слово -А---А-
        print(
            f'\n\nПриветствую тебя {name}, давай играть в "Виселицу"!. \n\n'
            f'Правила игры: 0 попыток - поражение.\n'
            f' От тебя требуется ввести или слово или букву.\n '
            f'Все 1000 слов на русском. Игра не чувствительна к регистру.\n'
            f'Неправильный ввод буквы -1 попытка.\n'
            f'Неправильный ввод слова -3 попытки)\n'
            f'Ты держишь плакат на котором все данные. Удержи!')
        play(word)
        print(f'\nПобед: {wincnt}. Поражений: {failcnt}.')
        again = input('Играем еще раз? (попробуй разные ответы):')
    elif again.lower() in 'нет н неа но не_хочу все хватит no nah nope n отстань прекратить закончить заткнись stop end':
        print('Пока пока и возвращайся снова')
        break
    else:
        continue