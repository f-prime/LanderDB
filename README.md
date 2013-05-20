Usage
=====

    import landerdb
    
    db = landerdb.Connect("database")
    
    db.insert("table", {"data":"blah"}) # Inserts into the table "table"
    db.insert("table", {"data":"AHH"}) # For later
 
    data = db.find("table", {"data":"blah"})
    print data #Returns [{"data":"blah"}]

    
    data = db.find("table", "all") # Returns all data in a table
    print data # Returns [{"data":"blah"}, {"data":"blah"}]
    

