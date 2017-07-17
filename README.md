Web vulnerabilities 

1. SQL Injection
    a. Vulnerability: server.py is web server file - user POSTed variables are used in raw
    query to database
    b. Exploits: 
        - Submitting in password box: [pswd' or '1=1] will give access into
            application  b/c the SQL query becomes [SELECT * FROM users WHERE
            username='username' and password='pswd' or '1=1']
        - [pswd' union select * from users where '1=1]
        - 
