print('Program for homework 1')
a = [1, 2, 3, 4, 5]
print('Ex.1 - We have this array: ' + str(a))
a.reverse()
print('Reverse of array is below:')
print(a)
print('')

a = [1, 1, 2, 2, 2, 2, 3, 3, 3]
b = 2
c = a.count(b)
print('Ex.2 - We have this array: ' + str(a))
print('We found variable ' + str(b) + ' only ' + str(c) + ' times')
print('')

a = 'ana are mere si nu are pere'
print('Ex.3 - We have the text: ' + a )
words = len(a.split())
print('This text has ' + str(words) + ' words')

