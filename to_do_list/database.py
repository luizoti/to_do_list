"""Modulo with database models and settings."""

from enum import Enum

from sqlalchemy import (
    create_engine,
    Integer,
    Column,
    DateTime,
    String,
    Boolean
)
from sqlalchemy.orm import declarative_base, sessionmaker

from to_do_list.settings import DATABASE_URL

Base = declarative_base()
engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()

def session_clear(exception=None):
    """Clear season if active."""
    session.close_all()
    if exception and session.is_active:
        session.rollback()

session_clear()


class TaskStates(Enum):
    """Task states."""
    PENDENTE = 0
    CONCLUIDA = 1 # noqa
    EM_PROGRESSO = 2

class TaskPrioritys(Enum):
    """Task prioritys."""
    BAIXA = 0
    MEDIA = 1
    ALTA = 2

class Tasks(Base):
    __tablename__ = "Tasks"
    id = Column(Integer, primary_key=True, autoincrement=True, name="ID da task")
    created_at = Column(DateTime, nullable=False, name="Data de Criação")
    title = Column(String, nullable=False, name="Titulo")
    description = Column(String, nullable=False, name="Descrição")
    priority = Column(Integer, nullable=False, name="Prioridade")
    completion_date = Column(DateTime, nullable=False, name="Data de conclusão")
    category = Column(String, nullable=False, name="Categoria")
    order = Column(Integer, nullable=False, name="Ordem")
    concluded = Column(Boolean, nullable=False, name="Concluída")

Base.metadata.create_all(engine)
