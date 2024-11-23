---
# Front matter
lang: ru-RU
title: "Лабораторная работа №6"
subtitle: "Научное программирование"
author: "Колчева Юлия Вячеславовна"

# Formatting
toc-title: "Содержание"
toc: true # Table of contents
toc_depth: 2
lof: true # List of figures
lot: true # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4paper
documentclass: scrreprt
polyglossia-lang: russian
polyglossia-otherlangs: english
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase
indent: true
pdf-engine: lualatex
header-includes:
  - \linepenalty=10 # the penalty added to the badness of each line within a paragraph (no associated penalty node) Increasing the value makes tex try to have fewer lines in the paragraph.
  - \interlinepenalty=0 # value of the penalty (node) added after each line of a paragraph.
  - \hyphenpenalty=50 # the penalty for line breaking at an automatically inserted hyphen
  - \exhyphenpenalty=50 # the penalty for line breaking at an explicit hyphen
  - \binoppenalty=700 # the penalty for breaking a line at a binary operator
  - \relpenalty=500 # the penalty for breaking a line at a relation
  - \clubpenalty=150 # extra penalty for breaking after first line of a paragraph
  - \widowpenalty=150 # extra penalty for breaking before last line of a paragraph
  - \displaywidowpenalty=50 # extra penalty for breaking before last line before a display math
  - \brokenpenalty=100 # extra penalty for page breaking after a hyphenated line
  - \predisplaypenalty=10000 # penalty for breaking before a display
  - \postdisplaypenalty=0 # penalty for breaking after a display
  - \floatingpenalty = 20000 # penalty for splitting an insertion (can only be split footnote in standard LaTeX)
  - \raggedbottom # or \flushbottom
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Изучение языка Octave, знакомство с методами работы с последовательностями, пределами, рядами. 

# Задание

 Разобраться со спецификой языка и выполнить операции. 

1. Пределы
2. Частичные суммы
3. Суммы ряда
4. Вычисление интегралов
5. Аппроксимирование суммами


# Выполнение лабораторной работы

 Для начала работы с программой включим журналирование сессии командой diary on. Затем приступим к выполнению первого этапа - работе с пределами. Определеим анонимную функцию, создадим индекчную переменную от 0 до 9 ( рис. [-@fig:001] )

![Вывод данных](image/1.png){ #fig:001 width=70% }

Возьмём степени 10, которые будцт входными значениями и оценим нашу функцию. Результат: предел сходится к значению 2.718 (рис. [-@fig:002] ) 

![Программа](image/2.png){ #fig:002 width=70% }

Теперь определим частичные суммы ряда.

Для начала определим индексный вектор, а затем вычислим члены. Чтобы узнать частичные суммы, остаётся только дописать команду sum. Напишем это в цикле ( рис. [-@fig:003] )

![Программа](image/3.png){ #fig:003 width=70% }

Нарисуем получившееся ( рис. [-@fig:004] )

![программа](image/4.png){ #fig:004 width=70% }

Получили такой рисунок  (рис. [-@fig:005] ) 

![График](image/5.png){ #fig:005 width=70% }

Теперь переходим к суммам ряда. Это сделать проще всего. Вычислим сумму первых 1000 членов гармонического ряда. Определим эти члены и посчитаем сумму ( рис. [-@fig:006] )

![Код](image/6.png){ #fig:006 width=70% }

Переходим к разделу интегрирования. Для начала вычислим интерграл при помощи функции guad. Определим функцию и применим её (рис. [-@fig:007] )

![Программа](image/7.png){ #fig:007 width=70% }

И последний раздел: аппроксимирование суммами. Сделаем это двумя способами: циклами и с помощью векторов. Для этого напишем два варианта кода  (рис. [-@fig:008] ) (рис. [-@fig:009] )

![Вариант 1](image/8.png){ #fig:008 width=70% }

![Вариант 2](image/9.png){ #fig:009 width=70% }

Запустим их и сверим результаты (рис. [-@fig:010] )

![Выводы](image/10.png){ #fig:010 width=70% }

Как можем заметить, второй файл с векторизацией работает куда быстрее. А это значит, что лучше всего вместо циклов использовать операции над векторами. 

На этом лабораторная работа закончена.


# Выводы

Познакомилась с методами работы с последовательностями, пределами, рядами.



# Список литературы

Лабораторная работа №6

Лабораторная работа № 6. Введение в работу с Octave [Электронный ресурс]. 2019. URL:https://esystem.rudn.ru/pluginfile.php/2372908/mod_resource/content/2/README.pdf



