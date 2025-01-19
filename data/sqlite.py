from .models.user import User
import sqlite3
from hashlib import sha256
from pathlib import Path


class Connection:
    """
    Gerencia a conexão com o banco de dados SQLite.

    Implementa o padrão Singleton para garantir que apenas uma instância da conexão 
    exista. Esta classe fornece métodos para criar o banco de dados, adicionar 
    novos usuários e validar credenciais de usuários.

    Attributes:
        db_path (Path): O caminho do arquivo do banco de dados.
        _connection (sqlite3.Connection): A conexão ativa com o banco de dados.
    """
    _instance = None  # Atributo para o padrão Singleton

    def __new__(cls, *args, **kwargs):
        """
        Garante que apenas uma instância da classe seja criada.

        Returns:
            Connection: A instância única da classe.
        """
        if not cls._instance:
            cls._instance = super(Connection, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        """
        Inicializa o caminho do banco de dados, a conexão
        e cria o banco, caso não exista.

        O banco de dados está localizado no diretório 'data/storage/' e é chamado
        'database.db'.
        """
        self.db_path        = Path("data/storage/database.db")
        self._connection    = None
        self.create_database()

    def _connect(self):
        """
        Estabelece e retorna a conexão com o banco de dados.

        Returns:
            sqlite3.Connection: A conexão ativa com o banco de dados.
        """
        if not self._connection:
            self._connection = sqlite3.connect(self.db_path)
        return self._connection

    def create_database(self) -> None:
        """
        Cria o banco de dados e a tabela de usuários, caso ainda não existam.

        A tabela de usuários possui os seguintes campos:
        - id: Identificador único (INTEGER, PRIMARY KEY).
        - email: Endereço de email único (TEXT, NOT NULL).
        - password: Senha do usuário (TEXT, NOT NULL).
        """
        if not self.db_path.exists():
            # Cria o diretório, se necessário
            self.db_path.parent.mkdir(exist_ok=True, parents=True)

            conn    = self._connect()
            cursor  = conn.cursor()

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                )
            ''')

            conn.commit()

    def create_user(self, email: str, password: str) -> None:
        """
        Adiciona um novo usuário ao banco de dados.

        Args:
            email (str): O endereço de email do usuário.
            password (str): A senha do usuário.

        Raises:
            ValueError: Se os campos 'email' ou 'password' estiverem ausentes 
                        ou se o email já estiver registrado.
        """
        if not email or not password:
            raise ValueError("Missing fields: 'email' or 'password'!")

        conn = self._connect()
        cursor = conn.cursor()
        try:
            # Hash da senha
            hash_pass = sha256(password.encode()).hexdigest()

            cursor.execute(
                "INSERT INTO users (email, password) "
                "VALUES (?, ?)",
                (email, hash_pass)
            )

            conn.commit()
        except sqlite3.IntegrityError:
            raise ValueError(f"Email {email} is already registered!")
        except Exception as e:
            raise ValueError(str(e))

    def validate_user(self, email: str, password: str) -> User:
        """
        Valida as credenciais de um usuário.

        Args:
            email (str): O endereço de email do usuário.
            password (str): A senha do usuário.

        Returns:
            User: O objeto User correspondente ao email e senha fornecidos.

        Raises:
            ValueError: Se o email ou a senha forem inválidos.
        """
        conn        = self._connect()
        cursor      = conn.cursor()
        hash_pass   = sha256(password.encode()).hexdigest()  # Hash da senha

        cursor.execute(
            "SELECT email, password "
            "FROM users "
            "WHERE email = ? AND password = ?",
            (email, hash_pass)
        )

        result = cursor.fetchone()

        if result:
            return User(email = result[0], password = result[1])
        else:
            raise ValueError("Invalid username or password!")
