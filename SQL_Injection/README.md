1. hi
    i. hello
    ii. hola
2. bonjour


# SQL Injection #

## This vulnerability occurs when unparsed user input is used for SQL queries ##


### Web vulnerabilities ###

#### SQL Injection ####
1. Using SQL injection to gain permission access where username/password
are required.

#### Vulnerability ####

login_server.py is a web server file - user input is POSTed and used as
raw SQL query to database

#### Exploits ####
i. Submitting in password box: [pswd' or '1=1] will give access into
application b/c the SQL query becomes [SELECT * FROM users WHERE
username='username' and passwords='pswd' or '1=1']

ii. [pswd' UNION SELECT * FROM users WHERE '1=1]

iii. Blind SQL Injection can be used to gain login access by figuring out
the user password. This works by understanding which queries result in
the server responding with true or false values. For example, a password
can be recovered from a database by querying the server for each letter
in the string. 
More specifically, as a test the following was submitted
to the password box in the login page [pswd' or
substring('ab',1,1)='a' and '1=1] this asks the server if 'a' is the
first character in the string 'ab'. Based on access/denial to the
login, we know if that query is true or false. This was then used to
check for the letters in the password by submitting [pswd' or
substring(password,1,1)='d' and '1=1]. In this case we knew the
username, however, so an attack must be found to do this without
knowing this info. But, there are circumstances where usernames are
leaked without passwords.
Using this technique, I wrote an automated hack to check for each
letter one at a time until the entire password is recovered. This file
can be found in blind_sql.py.

2.
#### Vulnerability ####
id_content_server.py returns pages based on ids - SQL injection can be used
to view more pages than permitted

#### Exploits ####
    i. Can get server to display more pages than allowed by one id by submitting [3 or 1=1] as
       url param
    ii. Similarly using a union, we can get more than one page at a time
       [1 union select page_content from page where id=2]
