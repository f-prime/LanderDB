import db
q = db.Connect("test")
print q.find("users", {"b":6})

