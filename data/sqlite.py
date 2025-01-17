from .models.user import User
import sqlite3
from pathlib import Path


class Connection:
    _instance = None  # Atributo para o singleton

    def __new__(cls, *args, **kwargs):
        """Implementação do padrão Singleton"""
        if not cls._instance:
            cls._instance = super(Connection, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        """Inicializa o caminho do banco de dados."""
        self.db_path = Path("data/storage/database.db")
        self._connection = None

    def _connect(self):
        """Estabelece uma conexão com o banco de dados."""
        if not self._connection:
            self._connection = sqlite3.connect(self.db_path)
        return self._connection

    def create_database(self) -> None:
        """Cria o banco de dados e a tabela de usuários, caso não exista."""
        if not self.db_path.exists():
            self.db_path.parent.mkdir(exist_ok=True, parents=True)  # Garante que o diretório existe
            conn = self._connect()
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                )
            ''')
            conn.commit()

    def create_user(self, email: str, password: str) -> None:
        """Adiciona um novo usuário ao banco de dados."""
        conn = self._connect()
        cursor = conn.cursor()
        if email == None or password == None:
            raise ValueError(
                f'Erro: campos "email" ou "password" faltando!'
            )


        try:
            cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
            conn.commit()
        except sqlite3.IntegrityError:
            raise ValueError(f"Email {email} já cadastrado!")
        except Exception as e:
            raise ValueError(str(e))

    def validate_user(self, email: str, password: str) -> User:
        """Busca um usuário pelo email."""
        conn = self._connect()
        cursor = conn.cursor()
        hash_passw = password
        cursor.execute("SELECT email, password FROM users WHERE email = ? and password = ?", (email, hash_passw))
        result = cursor.fetchone()

        if result:
            return User(email=result[0], password=result[1])
        else:
            raise ValueError(f"Invalid username or password!")
