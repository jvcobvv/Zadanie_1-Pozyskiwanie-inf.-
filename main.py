class EmailExtractor():
    def __init__(self, email):
        self.email = email

    def is_student(self):
        x = self.email.count('@')
        if x == 0:
            return -1
        mail = self.email.split('@')
        x = mail[1].count('.')
        if x < 2:
            return -1
        koncowka = mail[1].split('.')
        if len(koncowka) == 4 and koncowka[0] == 'student':
            return True
        else:
            return False

    def is_male(self):
        x = self.email.count('@')
        if x == 0:
            return -1
        mail = self.email.split('@')
        x = mail[0].count('.')
        if x == 0:
            return -1
        koncowka = mail[0].split('.')
        if koncowka[0][len(koncowka[0]) - 1] == 'a':
            return False
        else:
            return True

    def get_name(self):
        x = self.email.count('@')
        if x == 0:
            return -1
        mail = self.email.split('@')
        x = mail[0].count('.')
        if x == 0:
            return -1
        koncowka = mail[0].split('.')
        text = koncowka[0][0].upper() + koncowka[0][1:]
        return text

    def get_surname(self):
        x = self.email.count('@')
        if x == 0:
            return -1
        mail = self.email.split('@')
        x = mail[0].count('.')
        if x == 0:
            return -1
        koncowka = mail[0].split('.')
        if koncowka[1][len(koncowka[1]) - 1].isnumeric():
            return koncowka[1][0].upper() + koncowka[1][1:(len(koncowka[1]) - 2)]
        else:
            return koncowka[1][0].upper() + koncowka[1][1:]

emailik = EmailExtractor("norbert.waszkowiak@student.wat.edu.pl")
print(emailik.is_student())