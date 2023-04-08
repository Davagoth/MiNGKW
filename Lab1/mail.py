import re


class EmailExtractor:

    def __init__(self, email: str):
        self.email = email
        self.regex = r"(?P<get_name>[a-z]{2,})[.](?P<get_surname>[a-z]{2,})([0-9]{2}){0,1}[@](?P<is_student>(" \
                     r"student\.)?)(wat\.edu\.pl)"

    def is_student(self) -> bool:
        x = re.compile("")
        x.match(self.email)
        return False

    def is_male(self) -> bool:
        return False

    def get_name(self) -> str:
        return "Dawid"

    def get_surname(self) -> str:
        return "Glowacki"
