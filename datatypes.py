import arrow


class BingTime(str):
    """
    Convert the time format of Bing Wallpaper API to `arrow.Arrow`.
    """

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, str):
            raise TypeError("string required")
        m = arrow.get(v, ["YYYYMMDD", "YYYYMMDDHHmm"])
        return cls(m)

    def __repr__(self):
        return f"BingTime({super().__repr__()})"
