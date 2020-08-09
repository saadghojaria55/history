import sqlite3 
conn = sqlite3.connect("C:/Users/LENOVO/AppData/Local/Google/Chrome/User Data/Default/History") 
  
# point out at the cursor 
c1 = conn.cursor() 
id = 0  
   
result = True
while result: 
      
    result = False
    ids = [] 
    for rows in c1.execute("SELECT id,url FROM urls WHERE url LIKE '%geeksforgeeks%'"): 
          
        print(rows) 
          
        id = rows[0] 
          
        ids.append((id,)) 
    c1.executemany('DELETE from urls WHERE id = ?',ids) 
    conn.commit() 
      
conn.close() 
