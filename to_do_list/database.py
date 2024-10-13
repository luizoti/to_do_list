"""Modulo with database models and settings."""

from sqlalchemy import (
    create_engine,
    Integer,
    Column,
    DateTime,
    String
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


class Tasks(Base):
    __tablename__ = "Tasks"
    id = Column(Integer, primary_key=True, name="id", comment="ID da task")
    created_at = Column(DateTime, nullable=False, name="created_at", comment="Data de Criação")
    title = Column(String, nullable=False, name="title", comment="Titulo")
    priority = Column(Integer, nullable=False, name="priority", comment="Prioridade")
    completion_date = Column(DateTime, nullable=False, name="completion_date", comment="Data de conclusão")
    order = Column(Integer, nullable=False, name="order", comment="Ordem")
    status = Column(Integer, nullable=False, name="status", comment="Status")


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

            if "order" in kwargs:
                current_task = session.query(Tasks).filter_by(id=obj_id).first()
                next_task = session.query(Tasks).filter_by(order=kwargs["order"]).first()
                next_task.order = current_task.order
                current_task.order = kwargs["order"]
            else:
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
            objects = session.query(cls.model).order_by(cls.model.order).all()
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
