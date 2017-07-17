Web vulnerabilities <br />
<br /> 
1. SQL Injection <br />
    a. Vulnerability: server.py is web server file - user POSTed variables are used in raw <br />
    query to database <br />
    b. Exploits: <br />
        - Submitting in password box: [pswd' or '1=1] will give access into <br/>
            application  b/c the SQL query becomes [SELECT * FROM users WHERE<br/>
            username='username' and password='pswd' or '1=1'] <br />
        - [pswd' union select * from users where '1=1] <br />
        - 
