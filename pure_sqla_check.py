# -*- encoding: utf-8 -*-
import random
from sqlalchemy import Column, ForeignKey, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)

    def __str__(self):
        return self.username


class Genre(Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __str__(self):
        return self.name


class Magazine(Base):
    __tablename__ = 'magazines'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'))
    genre_id = Column(Integer, ForeignKey('genres.id'))

    author = relationship(User,
                          backref=backref('magazines',
                                          order_by=id,
                                          lazy='joined'))
    genre = relationship(Genre,
                         backref=backref('magazines',
                                         order_by=id,
                                         lazy='joined'))


class WorkType(Base):
    __tablename__ = 'work_types'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __str__(self):
        return self.name


class WorkEvent(Base):
    __tablename__ = 'work_events'
    id = Column(Integer, primary_key=True)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    work_type_id = Column(Integer, ForeignKey('work_types.id'))
    work_type = relationship(WorkType,
                             backref=backref('work_events'), order_by=id,
                             lazy='joined')


class AuthorRate(Base):
    __tablename__ = 'author_rates'
    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    work_type_id = Column(Integer, ForeignKey('work_types.id'))
    author_id = Column(Integer, ForeignKey('users.id'))
    work_type = relationship(WorkType,
                             backref=backref('author_rates'), order_by=id,
                             lazy='joined')

    author = relationship(User,
                          backref=backref('author_rates'),
                          order_by=id, lazy='joined')

    def __str__(self):
        return str(self.amount)


def check():
    engine = create_engine('postgres://flask:flask@localhost:5432/flask',
                           echo=True)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for i in range(5):
        some_key = str(random.randint(1000000, 9000000))
        work_type = WorkType(name='work_type' + some_key)
        session.add(work_type)
        for j in range(8):
            some_other_key = str(random.randint(1000000, 9000000))
            user = User(username='user' + some_key + some_other_key)
            session.add(user)
            rate = AuthorRate(
                amount=1 + random.random(),
                work_type=work_type,
                author=user)
            session.add(rate)
    session.commit()
    print('========')
    rates = session.query(AuthorRate)
    print(rates)
    rates = rates.limit(10)
    print('+++++++')
    print(rates)
    print('=========')
    rates = rates.offset(0)
    print('*********')
    for rate in rates:
        print('{0} {1} {2} {3}'.format(rate.id, rate.amount,
                                       rate.work_type, rate.author))
    print('********')


if __name__ == '__main__':
    check()
