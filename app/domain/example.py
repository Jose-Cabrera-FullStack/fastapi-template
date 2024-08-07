from itertools import cycle


class AppNameDomain:
    @staticmethod
    def parse_rut(rut: str) -> str:
        """Parse rut to format 12345678-9"""
        if "-" in rut:
            return rut

        reversed_digits = map(int, reversed(str(rut)))
        factors = cycle(range(2, 8))
        s = sum(d * f for d, f in zip(reversed_digits, factors))
        dv = (-s) % 11
        return f"{rut}-{dv}"


# Test function:function used by test template, only used for testing & template purposes (don't copy)


def error_for_test(data):
    return data["field2"] == 100
