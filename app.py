import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
os.system("cls||clear") # Limpar terminal.

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
        self.ra = ra
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha

    

# Criando tabela no banco de dados.
Base.metadata.create_all(bind=MEU_BANCO) # Comando para criação de tabelas.

#CRUD
def create():
        
    print("Solicitando dados para o usuário.")
    inserir_ra = input("Digite seu R.A.: ")
    inserir_nome = input("Digite seu nome: ")
    inserir_sobrenome = input("Digite seu sobrenome: ")
    inserir_email = input("Digite seu e-mail: ")
    inserir_senha = input("Digite sua senha: ")

    aluno = Aluno(ra=inserir_ra,nome=inserir_nome,sobrenome=inserir_sobrenome,email=inserir_email, senha=inserir_senha)
    session.add(aluno)
    session.commit()
    
def readAll():
    print("\nExibindo dados de todos os alunos.")
    lista_alunos = session.query(Aluno).all()

    for aluno in lista_alunos:
        print(f"{aluno.id} - {aluno.ra} - {aluno.nome} - {aluno.sobrenome} - {aluno.email} - {aluno.senha}")

def readOne():
    print("Consultado os dados de apenas um aluno")
    email_aluno = input("Digite o e-mail do aluno: ")

    aluno = session.query(Aluno).filter_by(email = email_aluno).first()

    if aluno:
        print(f"{aluno.id} - {aluno.nome} - {aluno.email} - {aluno.senha}")
    else:
        print("Aluno não encontrado.")
    
def update():
    print("\nAtualizando dados de todos os alunos.")
    email_aluno = input("Digite o e-mail do aluno que será atualizado: ")

    aluno = session.query(Aluno).filter_by(email = email_aluno).first()

    if aluno:
        aluno.ra = input("Digite seu R.A: ")
        aluno.none = input("Digite seu nome: ")
        aluno.sobrenome = input("Digite seu Sobrenome: ")
        aluno.email  = input("Digite seu e-mail: ")
        aluno.senha = input("Digite sua senha: ")

        session.commit()
    else:

        print("Aluno não encontrado. ")
    
def delete():
    print("\nExcluido os dados de um aluno.")
    email_aluno = input("Digite o e-mail do aluno que será excluído: ")

    aluno = session.query(Aluno).filter_by(email = email_aluno).first()

    if aluno:
        session.delete(aluno)
        session.commit()
        print(f"Cliente {aluno.nome} excluido com sucesso!")
    else:
        print("Aluno não encontrado. ")

create()
readAll()
update()
readAll()
delete()
readAll()
readOne()

session.close