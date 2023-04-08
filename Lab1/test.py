import unittest

from mail import EmailExtractor


class EmailExtractorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.data = [
            # email, is_student, is_male, name, surname
            ["norbert.waszkowiak@wat.edu.pl", False, True, "Norbert", "Waszkowiak"],
            ["jan.kowalski@student.wat.edu.pl", True, True, "Jan", "Kowalski"],
            ["anna.nowak@student.wat.edu.pl", True, False, "Anna", "Nowak"],
            ["adrianna.abacka01@student.wat.edu.pl", True, False, "Adrianna", "Abacka"],
            ["katarzyna.babacka@wat.edu.pl", False, False, "Katarzyna", "Babacka"],
            ["dawid.glowacki@student.wat.edu.pl", True, True, "Dawid", "Głowacki"],
            ["agata.agatowska@wat.edu.pl", False, False, "Agata", "Agatowska"],
            ["bernadeta.bartojewska@student.wat.edu.pl", True, False, "Bernadeta", "Bartojewska"],
            ["aleksandra.baz@wat.edu.pl", False, False, "Aleksandra", "Baź"],
            ["dominik.dobrowolski02@student.wat.edu.pl", True, True, "Dominik", "Dobrowolski"],
            ["eustachy.polski@wat.edu.pl", False, True, "Eustachy", "Polski"],
            ["krystyna.krawczyk@student.wat.edu.pl", True, False, "Krystyna", "Krawczyk"],
            ["dominika.dobosz@wat.edu.pl", False, False, "Dominika", "Dobosz"],
            ["pawel.pawlowski01@student.wat.edu.pl", True, True, "Pawel", "Pawlowski"],
            ["oliwier.guliwer@wat.edu.pl", False, True, "Oliwier", "Guliwer"]]

    def test_is_student(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                is_student = x[1]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(is_student, extractor.is_student())

    def test_is_male(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                name = x[2]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(name, extractor.is_male())

    def test_get_name(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                name = x[3]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(name, extractor.get_name())

    def test_get_surname(self):
        for x in self.data:
            with self.subTest():
                # given
                email = x[0]
                surname = x[4]
                # then
                extractor = EmailExtractor(email)
                # expect
                self.assertEqual(surname, extractor.get_surname())


if __name__ == '__main__':
    unittest.main()
