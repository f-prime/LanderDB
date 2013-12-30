Usage
=====

    import landerdb
    
    db = landerdb.Connect("database")
    
    db.insert("table", {"data":"blah"}) # Inserts into the table "table"
    db.save()
    db.insert("table", {"data":"AHH"}) # For later
    db.save()
        
    db.insert("table", {"data":"dog", "rand":"cat"})
    db.save()

    data = db.find("table", {"data":"blah"})
    print data #Returns [{"data":"blah"}]


    data = db.find("table", {"data":"dog", "rand":"cat"})
    print data #Returns [{"data":"dog", "rand":"cat"}]

    data = db.find("table", "all") # Returns all data in a table
    print data # Returns [{"data":"blah"}, {"data":"blah"}]
    
    db.update("table", {"data":"dog"}, {"data":"cat", "rand":"dog"})
    db.save()    

