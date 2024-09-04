def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()


#inner_function() - Ошибка, так как функция находится в объемлющей видимости.
test_function()  # - Все работает