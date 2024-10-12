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
from sqlalchemy.exc import SQLAlchemyError
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
    CONCLUIDA = 1  # noqa
    EM_PROGRESSO = 2


class TaskPrioritys(Enum):
    """Task prioritys."""
    BAIXA = 0
    MEDIA = 1
    ALTA = 2


class Tasks(Base):
    __tablename__ = "Tasks"
    id = Column(Integer, primary_key=True, name="id", comment="ID da task")
    created_at = Column(DateTime, nullable=False, name="created_at", comment="Data de Criação")
    title = Column(String, nullable=False, name="title", comment="Titulo")
    description = Column(String, nullable=False, name="description", comment="Descrição")
    priority = Column(Integer, nullable=False, name="priority", comment="Prioridade")
    completion_date = Column(DateTime, nullable=False, name="completion_date", comment="Data de conclusão")
    category = Column(String, nullable=False, name="category", comment="Categoria")
    order = Column(Integer, nullable=False, name="order", comment="Ordem")
    concluded = Column(Boolean, nullable=False, name="concluded", comment="Concluída")


Base.metadata.create_all(engine)


class TasksManager:
    """Manager for handling database operations on a model."""

    model = Tasks  # Atributo de classe a ser definido nos modelos concretos

    @classmethod
    def _to_dict(cls, obj):
        """Convert SQLAlchemy object to dictionary."""
        return {column.name: getattr(obj, column.name) for column in obj.__table__.columns}

    @classmethod
    def create(cls, **kwargs):
        """Create a new instance of the model and return it as a dict."""
        try:
            obj = cls.model(**kwargs)
            session.add(obj)
            session.commit()
            return cls._to_dict(obj)
        except SQLAlchemyError as e:
            session.rollback()
            return {"success": False, "message": str(e)}

    @classmethod
    def update(cls, obj_id, **kwargs):
        """Update an existing instance of the model and return it as a dict."""
        try:
            obj = session.query(cls.model).filter_by(id=obj_id).first()
            if not obj:
                return {"success": False, "message": "Object not found."}

            for key, value in kwargs.items():
                setattr(obj, key, value)

            session.commit()
            return cls._to_dict(obj)
        except SQLAlchemyError as e:
            session.rollback()
            return {"success": False, "message": str(e)}

    @classmethod
    def delete(cls, obj_id):
        """Delete an existing instance of the model."""
        try:
            obj = session.query(cls.model).filter_by(id=obj_id).first()
            if not obj:
                return {"success": False, "message": "Object not found."}
            session.delete(obj)
            session.commit()
            return {"success": True, "message": "Object deleted successfully."}
        except SQLAlchemyError as e:
            session.rollback()
            return {"success": False, "message": str(e)}

    @classmethod
    def get(cls, obj_id):
        """Retrieve a single instance of the model by ID and return it as a dict."""
        try:
            obj = session.query(cls.model).filter_by(id=obj_id).first()
            if obj:
                return cls._to_dict(obj)
            return {}
        except SQLAlchemyError as e:
            return {"success": False, "message": str(e)}

    @classmethod
    def all(cls):
        """Retrieve all instances of the model and return them as a list of dicts."""
        try:
            objects = session.query(cls.model).all()
            return [cls._to_dict(obj) for obj in objects]
        except SQLAlchemyError as e:
            return {"success": False, "message": str(e)}

    @classmethod
    def filter(cls, **filters):
        """Filter instances of the model based on given filters and return them as a list of dicts."""
        try:
            objects = session.query(cls.model).filter_by(**filters).all()
            return [cls._to_dict(obj) for obj in objects]
        except SQLAlchemyError as e:
            return {"success": False, "message": str(e)}
