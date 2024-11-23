---
# Front matter
lang: ru-RU
title: "Лабораторная работа №6"
subtitle: "Математические основы защиты информации и информационной безопасности"
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

Познакомиться с алгоритмом разбора числа на множители.

# Задание

Реализовать алгоритм, реализующий р-метод Полларда. 


# Выполнение лабораторной работы

 
Данная работа была выполнена на языке Julia. 

Для реализации теста Ферма была написана следующая программа (рис. [-@fig:001] ) :

![Программа реализации теста Ферма](image/1.png){ #fig:001 width=70% }

В данной программе: 

1-2 строки: подключение библиотек для случайного числа и для нахождения НОД

4: задание функции 

5-9: Задаём сжимающую функцию, в данном случае степенную. Со случайно выбранным числом делаем операцию а^В! mod n.  

10: находим НОД чисел а-1 и n 

11: проводим проверку условия, если числитель нетривиальный, то выводим его, в ином случае алгоритм необходимо повторить

18: задаём число, которое нужно разложить

19: запускаем функцию.

Мы можем видеть результат на (рис. [-@fig:001] ) . Программа работает верно.


# Выводы

Познакомилась с алгоритмом разбора числа на множители и реализовала алгоритм р-метод Полларда.

# Список литературы

Лабораторная работа №6

Разложение чисел на множители [Электронный ресурс]. URL: https://esystem.rudn.ru/mod/folder/view.php?id=1150978


