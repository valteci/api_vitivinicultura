class User:
    def __init__(self, email: str, password: str):
        self._email     = email
        self._password  = password

    @property
    def email(self) -> str:
        return self._email
    
    @property
    def password(self) -> str:
        return self._password
    
    @email.setter
    def email(self, email: str) -> None:
        self._email = email

    @password.setter
    def password(self, password: str) -> None:
        self._password = password