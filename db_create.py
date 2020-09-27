# db_create.py


from datetime import date

from project import db,bcrypt
from project.models import Task, User

# create the database and the db table
# db.create_all()

# # insert data
# db.session.add(
#     User("admin", "ad@min.com", "admin", "admin")
# )
# db.session.add(
#     Task("Finish this tutorial", date(2015, 3, 13), 10, date(2015, 2, 13), 1, 1)
# )
# db.session.add(
#     Task("Finish Real Python", date(2015, 3, 13), 10, date(2015, 2, 13), 1, 1)
# )

# # commit the changes
# db.session.commit()

db.create_all()

db.session.add(User("admin", "ad@min.com", bcrypt.generate_password_hash("admin"), "admin"))

# insert data
# db.session.add(
#     User("admin", "ad@min.com", "admin", "admin")
# )
# db.session.add(
#     Task("Finish this tutorial", date(2015, 3, 13), 10, date(2015, 2, 13), 1, 1)
# )
# db.session.add(
#     Task("Finish Real Python", date(2015, 3, 13), 10, date(2015, 2, 13), 1, 1)
# )

# commit the changes
db.session.commit()
