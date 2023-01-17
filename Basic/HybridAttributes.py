from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method

Base = declarative_base()

class Interval(Base):
    __tablename__ = 'interval'

    id = Column(Integer, primary_key=True)
    start = Column(Integer, nullable=False)
    end = Column(Integer, nullable=False)

    def __init__(self, start, end):
        self.start = start
        self.end = end

    @hybrid_property
    def length(self):
        return self.end - self.start

    @length.setter
    def updatelength(self, value):
        self.end = self.start + value

    @hybrid_method
    def contains(self, point):
        return (self.start <= point) & (point <= self.end)

    @hybrid_method
    def intersects(self, other):
        return self.contains(other.start) | self.contains(other.end)

first = Interval(3, 9)
print(first.length)
print(Interval.length.expression)

print(first.contains(6))
print(first.contains(13))
print(first.intersects(Interval(7, 18)))
print(first.intersects(Interval(25, 29)))

