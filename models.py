from sqlalchemy import Column, Integer, String, Numeric, Boolean, DateTime, ForeignKey, BigInteger
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Boreholes(Base):
    __tablename__ = 'Boreholes'

    id = Column(BigInteger, primary_key=True)
    name = Column(String, nullable=False)
    length = Column(Numeric)
    depth = Column(Numeric)
    fissure_inside = Column(Boolean)

    files = relationship("Borehole", back_populates="files")

class Files(Base):
    __tablename__ = 'Files'

    id = Column(BigInteger, primary_key=True)
    name = Column(String, nullable=False)
    borehole_id = Column(BigInteger, ForeignKey('Boreholes.id'))
    part_of_file_id = Column(Integer)
    created_at = Column(DateTime)
    data = Column(JSONB)

    borehole = relationship("Files", back_populates="borehole")