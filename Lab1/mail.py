import re


class EmailExtractor:

    def __int__(self, mail: str):
        self.email = mail

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
