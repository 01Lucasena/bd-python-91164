import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados.

MEU_BANCO = create_engine("sqlite:///meubanco.db")

# Criando conexão com banco de dados.
Session = sessionmaker(bind=MEU_BANCO)
session = Session()

# Criando tabela.

Base = declarative_base()

class Aluno(Base):
    __tablename__ = "alunos"

    # Definindo campos da tabela.
    id = Column("id", Integer, primary_key=True, autoincrement=True) # Autoincremento de banco de dados.
    ra = Column("ra", String)
    nome = Column("nome", String)
    sobrenome = Column("sobrenome", String)
    email = Column("email", String)
    senha = Column("senha", String)

    # Definindo atributos de classe.
    def __init__(self,ra: str, nome: str, sobrenome: str, email: str, senha: str):
        self
        self.nome = nome
        self.email = email
        self.senha = senha

# Criando tabela no banco de dados.
Base.metadata.create_all(bind=MEU_BANCO) # Comando para criação de tabelas.