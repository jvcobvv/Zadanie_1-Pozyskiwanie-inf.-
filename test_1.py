import unittest
from main import EmailExtractor

class EmailExtractorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.data = [
            # email, is_student, is_male, name, surname
            ["norbert.waszkowiak@wat.edu.pl", False, True, "Norbert", "Waszkowiak"],
            ["jan.kowalski@student.wat.edu.pl", True, True, "Jan", "Kowalski"],
            ["anna.nowak@student.wat.edu.pl", True, False, "Anna", "Nowak"],
            ["adrianna.abacka01@student.wat.edu.pl", True, False, "Adrianna", "Abacka"],
            ["katarzyna.babacka@wat.edu.pl", False, False, "Katarzyna", "Babacka"],

            ["jakub.pawlak02@student.wat.edu.pl", True, True, "Jakub", "Pawlak"],
            ["janusz.wojtkowski@wat.edu.pl", False, True, 'Janusz', 'Wojtkowski'],
            ["maria.wesolowska@student.wat.edu.pl", True, False, 'Maria', 'Wesolowska'],
            ["janusz.wojtkowskiwat.edu.pl", -1, -1, -1, -1],
            ["januszwojtkowski@wat.edu.pl", False, -1, -1, -1],
            ["janusz.wojtkowski@watedu.pl", -1, True, 'Janusz', 'Wojtkowski'],
            ["karolina.wojtkowska13@watedupl", -1, False, 'Karolina', 'Wojtkowska'],
            ["mortadelagazka@watedu.pl", -1, -1, -1, -1],
            ["marianmarciniak@watedupl", -1, -1, -1, -1],
            ["maria.sklodowska@gmail.com", -1, True, 'Maria', 'Sklodowska']
        ]

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