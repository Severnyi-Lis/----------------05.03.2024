'''У Татьяны 5 яблок, а у Олега 8. Сколько всего?
Решение: всего 5+8=13 яблок.
Ответ: 13 яблок'''

tania = 5
oleg = 8
summa= tania+oleg
tr='У Татьяны'
s='яблок'
l= 'а у Олега'
f= 'Решение: всего 5 + 8 ='
w = 'Ответ: '
table_row = '%s %i %s %s %i '  # шаблон строки - подстановка по порядку
ttt='%s %i %s'
rrr='%s %i %s'
print(table_row % (  # % - знак подстановки в строку
    tr,       
    tania,
    s,
    l,
    oleg
))
print(ttt % (
    f,
    summa,
    s
))
print(rrr % (
    w,
    summa,
    s
))
