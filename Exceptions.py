# Exceptions
try:
#    1/0
    pass
except Exception as e:
    print(dir(e))
    print(e)
else:
    print('else reached when no exception raised')
finally:
    print('always executed')