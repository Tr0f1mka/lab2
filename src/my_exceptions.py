class UndefinedFlagError(Exception):
    """
    Исключение неизвестного флага
    """
    pass


class TooFewPathsError(Exception):
    """
    Исключение малого количества путей
    """
    def __str__(self):
        return super().__str__()


class TooManyPathsError(Exception):
    """
    Исключение большого количества путей
    """
    pass


class LessRFlagError(Exception):
    """
    Исключение отсутствия флага rm
    """
    pass
