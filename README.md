Web vulnerabilities <br />
<br /> 
1. SQL Injection <br />
    a.<br/> 
    Vulnerability: server.py is web server file - user POSTed variables are used in raw <br />
    query to database <br />
    Exploits: <br />
        - Submitting in password box: [pswd' or '1=1] will give access into <br/>
            application  b/c the SQL query becomes [SELECT * FROM users WHERE<br/>
            username='username' and password='pswd' or '1=1'] <br />
        - [pswd' union select * from users where '1=1] <br />
        - Specific information can be learned about contents of password if <br/>
            objective is to steal this info (and not just gain login access). <br/>
            This was achieved through blind sql injection by understanding the <br/>
            response of the server to true or false queries. If this <br/>
            difference can be established, then it is a matter of including the <br/>
            'question' we are unsure of and using the server's response as the <br/>
            'answer'. More specifically, as a test the following was submitted
            <br/>
            to the password box in the login page [pswd' or
            substring('ab',1,1)='a' and '1=1] this asks the server if 'a' is the
            <br/>
            first character in the string 'ab'. Based on access/denial to the
            <br/>
            login, we know if that query is true or false. This was then used to
            <br/>
            check for the letters in the password by submitting [pswd' or
            <br/>
            substring(password,1,1)='d' and '1=1]. In this case we knew the
            <br/>
            username, however, so an attack must be found to do this without
            <br/>
            knowing this info. But, there are circumstances where usernames are
            <br/>
            leaked without passwords.
            <br/>
        - TODO: 1. how to find column names 
            <br/>
                2. automate finding password with script and third attack
            <br/>
                3. timing attack
            <br/>

    b.<br/>
    Vulnerability: id_content_server.py returns pages based on ids
    Exploits: <br/>
        - Can get server to display more pages than allowed by one id by submitting [3 or 1=1] as
            url param <br/>
        - Similarly using a union, we can get more than one page at a time: <br/>
            [1 union select page_content from page where id=2] <br/>
