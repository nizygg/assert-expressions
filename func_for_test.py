from typing import NoReturn, Union


def assert_expressions(
    all_expressions: tuple, func, print_result: bool = True
) -> Union[bool, NoReturn]:
    """There are two versions of doc(ru, en).:
    A function for automatically checking all variants of expressions.
    For correct operation,
    it is expected that the assert_expression will be passed
    the data is in the following form.
    all_expressions - expects a tuple of dictionaries, where each key is,
    this is a function parameter, and another key:
    expected_result is the value that the function should return
    a = (
        {
            "len_x": 4,
            "len_y": 3,
            "matrix_values": [(1, 2, 3), (0, 2, 6), (7, 4, 1), (2, 7, 0)],
            "x": 3,
            "y": 0,
            "expected_result": [7, 7],
        }
    ),
    func = function to be checked.
    Returns True if function do what expected
    Русский перевод.
    Функция для автоматической проверки всех вариантов выражений.
    Для корректной работы ожидается, что в assert_expressions будет переданы
    данные в следующей форме.
    all_expressions - ожидает кортеж из словарей, где каждый ключ,
    это параметр функции, и еще один ключ:
        expected_result - значение, которое функция должна вернуть
    a = (
        {
            "len_x": 4,
            "len_y": 3,
            "matrix_values": [(1, 2, 3), (0, 2, 6), (7, 4, 1), (2, 7, 0)],
            "x": 3,
            "y": 0,
            "expected_result": [7, 7],
        }
    ),
    func = функция, которая должна быть проверена.
    Возвращает True, если функция делает то, что ожидается от нее
    """
    try:
        expected_resultes = []
        for expression in all_expressions:
            expected_result = expression.__getitem__("expected_result")
            expected_resultes.append(expected_result)
            expression.__delitem__("expected_result")

        for i in range(len(all_expressions)):
            expression = all_expressions[i]
            function_res = func(**expression)
            result = (
                function_res == expected_resultes[i],
                function_res,
                expected_resultes[i],
            )
            assert result[
                0
            ], f"{expression} - returns {result[1]}, {result[2]} is required"
        if print_result:
            print("Function works currectly")
        return True
    except Exception:
        print(
            "You probably enter wrong parametrs. Check the standart\n",
            """
            a = (
            {
            "len_x": 4,
            "len_y": 3,
            "matrix_values": [(1, 2, 3), (0, 2, 6), (7, 4, 1), (2, 7, 0)],
            "x": 3,
            "y": 0,
            "expected_result": [7, 7],
            }
            ),
            func = function to be checked.
            examples = a + ...(other examples)
            assert_expression(examples, func)
            """,
        )
    return False
