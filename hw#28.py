# Условие:
# Создать программу, которая запрашивает у пользователя произвольную строку символов.
# Далее программа ее шифрует и выводит на экран в зашифрованном виде.
# Шифрование происходит путем замены каждого символа символом, который
# находится на 5 позиций правее в предопределенной таблице шифрования.
# Таблица шифрования задается программистом в виде одномерного списка символов.
# Если при выборе символа для шифровки таблица шифрования заканчивается, то
# циклически переходить к ее началу.


s=str(input('Random string is:'))
lst=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
     's','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9',
     ' ','!','-','%','@','(',')','=','+','-',':''?''.',',']

new_string=[]
for i in range(len(s)):
    symbol=s[i]
    symbol_index_lst=lst.index(symbol.lower())
    new_index_lst = symbol_index_lst + 5
    if new_index_lst<len(lst):
        new_symbol = lst[new_index_lst]
        new_string+=new_symbol
    else:
        new_index_lst1=new_index_lst%len(lst)
        new_symbol1 = lst[new_index_lst1]
        new_string+=new_symbol1
string=''.join(new_string)
print('Encrypted string is:', string)