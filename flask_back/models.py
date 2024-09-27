from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class GenderEnum(Enum):
    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'

class Users(Base):
    __tablename__ = "wixi_team"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(20), nullable=False)
    surname = Column(String(20), nullable=False)
    dob = Column(DateTime(timezone=True), nullable=False)
    email = Column(String(20), nullable=False, unique=True)
    mobile = Column(String(20), nullable=False)
    department = Column(String(12), nullable=False)
    id_number = Column(Integer, nullable=False, unique=True)
    gender = Column(Enum(GenderEnum), nullable=False)
    location = Column(String(40), nullable=False)
    start_date = Column(DateTime(timezone=True), nullable=False, default=func.now())
    end_date = Column(DateTime(timezone=True), nullable=True)

    @property
    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "surname": self.surname,
            "department": self.department
        }