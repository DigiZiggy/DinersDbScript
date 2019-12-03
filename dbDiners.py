# encoding: utf-8
"""
Program that creates SQLite database DINERS, with two related tables CANTEEN and PROVIDER,
inserts one canteens data by separate statement, other canteens as one list,
followed by two queries.

:author: Sigrid Närep
"""
from sqlalchemy import Column, Integer, String, ForeignKey, Time, select, func, and_
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime, time

engine = create_engine('sqlite:///DINERS.db', echo=True)

Base = declarative_base()


class Provider(Base):
    __tablename__ = 'PROVIDER'
    ID = Column(Integer, primary_key=True)
    ProviderName = Column(String)

    def __init__(self, ProviderName=None):
        self.ProviderName = ProviderName


class Canteen(Base):
    __tablename__ = 'CANTEEN'
    ID = Column(Integer, primary_key=True)
    ProviderID = Column(Integer, ForeignKey('PROVIDER.ID'))

    Name = Column(String)
    Location = Column(String)
    time_open = Column(Time)
    time_closed = Column(Time)
    print("Tables created successfully")

    def __init__(self, ProviderID=None, Name=None, Location=None, time_open=None, time_closed=None):
        self.ProviderID = ProviderID
        self.Name = Name
        self.Location = Location
        self.time_open = time_open
        self.time_closed = time_closed


def add_separate_records():
    """
    Insert IT College canteen data by separate statement

    """
    c1 = Provider(ProviderName='bitStop')
    c2 = Canteen(ProviderID=1, Name='bitStop KOHVIK', Location='Raja 4C, Tallinn',
                 time_open=datetime.strptime('09:30', '%H:%M').time(),
                 time_closed=datetime.strptime('16:00', '%H:%M').time())

    session.add(c1)
    session.add(c2)

    session.commit()
    print("Records created successfully")


def add_records_in_list():
    """
    Insert other canteens data as one list

    """
    session.add_all([
        Provider(ProviderName='Rahva Toit'),
        Provider(ProviderName='Baltic Restaurants Estonia AS'),
        Provider(ProviderName='TTÜ Sport OÜ'),
        Canteen(ProviderID=2, Name='Economics- and social science building canteen',
                Location='Akadeemia tee 3, SOC- building', time_open=datetime.strptime('08:30', '%H:%M').time(),
                time_closed=datetime.strptime('18:30', '%H:%M').time()),
        Canteen(ProviderID=2, Name='Libary canteen', Location='Akadeemia tee 1/Ehitajate tee 7',
                time_open=datetime.strptime('08:30', '%H:%M').time(),
                time_closed=datetime.strptime('19:00', '%H:%M').time()),
        Canteen(ProviderID=3, Name='Main building Deli cafe', Location='Ehitajate tee 5, U01 building',
                time_open=datetime.strptime('09:00', '%H:%M').time(),
                time_closed=datetime.strptime('16:30', '%H:%M').time()),
        Canteen(ProviderID=3, Name='Main building Daily lunch restaurant', Location='Ehitajate tee 5, U01 building',
                time_open=datetime.strptime('09:00', '%H:%M').time(),
                time_closed=datetime.strptime('16:30', '%H:%M').time()),
        Canteen(ProviderID=2, Name='U06 building canteen', Location='Ehitajate tee 5, Tallinn',
                time_open=datetime.strptime('09:00', '%H:%M').time(),
                time_closed=datetime.strptime('16:00', '%H:%M').time()),
        Canteen(ProviderID=3, Name='Natural Science building canteen', Location='Akadeemia tee 15, SCI building',
                time_open=datetime.strptime('09:00', '%H:%M').time(),
                time_closed=datetime.strptime('16:00', '%H:%M').time()),
        Canteen(ProviderID=3, Name='ICT building canteen', Location='Raja 15/Mäepealse 1',
                time_open=datetime.strptime('09:00', '%H:%M').time(),
                time_closed=datetime.strptime('16:00', '%H:%M').time()),
        Canteen(ProviderID=4, Name='Sports building canteen', Location='Männiliiva 7, S01 building',
                time_open=datetime.strptime('11:00', '%H:%M').time(),
                time_closed=datetime.strptime('20:00', '%H:%M').time())
    ])
    session.commit()
    print("Records created successfully")


def select_records_by_opening():
    """
    Query for canteens which are open 16.15-18.00

    """
    query = select([Canteen]).where(and_(func.time(Canteen.time_open) <= func.time('16:15'),
        func.time(Canteen.time_closed) >= func.time('18:00')))
    execution = session.execute(query)

    # printing out the resulting canteen names
    for canteen in execution:
        print(canteen.Name)


def select_records_by_provider():
    """
    Query for canteens which are serviced by Rahva Toit

    """
    print("Canteens serviced by Rahva Toit:")
    for p, c in session.query(Provider, Canteen).filter(Provider.ProviderName == 'Rahva Toit')\
            .filter(Canteen.ProviderID == 2).all():

        # printing out the resulting canteen names
        print(c.Name)


def closeconn():
    """
    close database connection
    """
    session.close()
    print("Connection closed")


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    add_separate_records()
    add_records_in_list()
    select_records_by_opening()
    select_records_by_provider()
    closeconn()
