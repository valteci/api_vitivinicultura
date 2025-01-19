class User:
    """
    Representa um usuário no sistema.

    Um usuário é identificado por seu email e senha. Ele precisa estar cadastrado
    e fazer login para acessar a API. A classe fornece métodos para manipulação 
    e acesso seguro aos atributos do usuário.

    Attributes:
        email (str): O endereço de email do usuário.
        password (str): A senha do usuário.
    """
    def __init__(self, email: str, password: str):
        """
        Inicializa uma nova instância da classe User.

        Args:
            email (str): O endereço de email do usuário.
            password (str): A senha do usuário.
        """
        self._email = email
        self._password = password

    @property
    def email(self) -> str:
        """
        Obtém o endereço de email do usuário.

        Returns:
            str: O email do usuário.
        """
        return self._email

    @property
    def password(self) -> str:
        """
        Obtém a senha do usuário.

        Returns:
            str: A senha do usuário.
        """
        return self._password

    @email.setter
    def email(self, email: str) -> None:
        """
        Define o endereço de email do usuário.

        Args:
            email (str): O novo endereço de email.
        """
        self._email = email

    @password.setter
    def password(self, password: str) -> None:
        """
        Define a senha do usuário.

        Args:
            password (str): A nova senha.
        """
        self._password = password
