import re


class EmailExtractor:

    def __init__(self, email: str):
        self.email = email
        self.regex = r'(?P<get_name>[a-z]{2,})[.](?P<get_surname>[a-z]{2,})([0-9]{2})?[@](?P<is_student>(' \
                     r'student\.)?)(?P<is_wat>(wat\.edu\.pl){1})'

    def is_student(self) -> bool:
        match = re.search(self.regex, self.email)
        if match.group('is_student') == 'student.':
            return True
        else:
            return False

    def is_male(self) -> bool:
        match = re.search(self.regex, self.email)
        match2 = re.search(r'[a-z]+a$', match.group('get_name'))
        if match2:
            return False
        else:
            return True

    def get_name(self) -> str:
        match = re.search(self.regex, self.email)
        return match.group('get_name')

    def get_surname(self) -> str:
        match = re.search(self.regex, self.email)
        return match.group('get_surname')
