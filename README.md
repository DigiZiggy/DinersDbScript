**Project title**

Program that creates SQLite database with two related tables, inserts data and has two queries.

**Project description**

There are 8 diners in different buildings of TalTech:
https://www.ttu.ee/students/university-facilities/canteen/
but IT College diner:
https://www.itcollege.ee/tudengile/oppehoone/kohvik/
is not in this list for unknown reason.

There are 4 service providers in total: Rahva Toit, Baltic Restaurants Estonia AS, TTÜ Sport and Bitstop Kohvik OÜ.
There are different opening hours for every canteen.

Task:
1) Create SQLite database DINERS, with two related tables CANTEEN and PROVIDER
Table CANTEEN fields: ID, ProviderID, Name, Location,  time_open, time_closed (weekday doesn't matter). (NB Changed 21.04.2019)
Table Provider fields: ID, ProviderName. (NB Changed 21.04.2019)
If you want, you may add some additional fields, but not necessary.

2) Insert IT College canteen data by separate statement, other canteens as one list.

3) Create query for canteens which are open 16.15-18.00
4) Create query for canteens which are serviced by Rahva Toit

Additional Information: 
Python 3 (Python 2 is not necessary). Tests and GUI are not necessary.

Add documentation and comments.
You may use direct SQL or SQLAlchemy (or other ORM).


**Code Example**

Create “home base” for the actual database
```angular2
engine = create_engine('sqlite:///DINERS.db', echo=True)
```

Open connection with database with base class from which all mapped classes should inherit
```angular2
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
```

Add data into database one by one for each database table
```angular2
add_separate_records()
```

Add data into database by bulk for each database table
```angular2
add_records_in_list()
```

Query to find canteens opened between 16.15-18.00
```
select_records_by_opening()
```

Query to find canteens who's provider is Rahva Toit
```angular2
select_records_by_provider()
```

Close database connection
```angular2
closeconn()
```

**How to use?**

Go into the Diners_Database folder
```angular2
cd Diners_Database
```

Make sure SQLAlchemy library is installed
```angular2
pip install SQLAlchemy
```

Run the image overlay generator
```angular2
python3 dbDiners.py
```

**License**

MIT © Sigrid Närep