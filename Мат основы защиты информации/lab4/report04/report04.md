---
# Front matter
lang: ru-RU
title: "Лабораторная работа №4"
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

Изучить применение языка Octave, познакомится с решением систем линейным уравнений с помощью Octave.

# Задание

 Разобраться со спецификой языка и выполнить операции. 

1. Метод Гаусса
2. Левое деление
3. LU-разложение
4. LUP-разложение


# Выполнение лабораторной работы

 Для начала работы с программой включим журналирование сессии командой diary on. Затем приступим к выполнению первого этапа - Метода Гаусса. Для начала заданим матрицу В и покажем как её можно просматривать поэлементно или всю строку. ( рис. [-@fig:001] )

![Вывод данных](image/1.png){ #fig:001 width=70% }

Теперь в явном виде реализуем метод Гаусса. Для начала добавим к третьей строке первую строку, умноженную на -1, а затем добавим к третьей строке вторую строку, умноженную на -1.5 (рис. [-@fig:002] ) 

![Метод Гаусса](image/2.png){ #fig:002 width=70% }

Теперь легко вычислить вектор, он будет равен х = (17/3 ; 17/3 ; -13/3) . Из последний строки можно вычислить х3: 0*х1 + 0*х2 + 3*х3 = -13. Затем подставляя получившееся значение х3 во вторую строку мы получаем х2 и так далее.

У Octave есть встроенная функция, которая позволяет сразу получить треугольный вид матрицы ( рис. [-@fig:003] )

![Треугольная матрица](image/3.png){ #fig:003 width=70% }

Мы можем поменять формат матрицы, чтобы отобразить больше разрядов и увидеть более точные вычисления ( рис. [-@fig:004] )

![Изменение формата](image/4.png){ #fig:004 width=70% }

Рассмотрим решение систем вида A*x = b, решим с помощью левого деления. Для начала разделим матрицу В на коэффициенты А и вектор значений b. Вычислим вектор х с помощью команды А/b  (рис. [-@fig:005] ) 

![Решение системы](image/5.png){ #fig:005 width=70% }

С помощью Octave покажем LU разложение матрицы ( рис. [-@fig:006] )

![LU разложение](image/6.png){ #fig:006 width=70% }

С помощью Octave покажем LUP разложение матрицы. Программа показывает сразу все необходимые нам матрицы (рис. [-@fig:007] )

![LUP разложение](image/7.png){ #fig:007 width=70% }




# Выводы

Изучила способы применения языка Octave, познакомилась с решением систем линейным уравнений с помощью Octave.



# Список литературы

Лабораторная работа №4

Лабораторная работа № 4. Введение в работу с Octave [Электронный ресурс]. 2019. URL:https://esystem.rudn.ru/pluginfile.php/2372904/mod_resource/content/3/004-gauss.pdf



