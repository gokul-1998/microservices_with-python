
- How to find a file in a directory
    - `sudo find /snap -name k9s`

- to create a symbolic link.
    - `sudo ln -s /snap/k9s/155/bin/k9s /usr/local/bin/k9s`

- this will  find  all the `VIRTUAL` word in the output of grep command
    - `env|grep VIRTUAL `

- how to  set environment variables?
    - `export MYSQL_HOST=localhost`

- in mysql , the command to list all databases is
    - `show databases`

- to drop a database
    - `drop database <name>`

- to list all the  users in mysql
    - `select user from mysql.user;`

- to drop a user from database
    - `drop user auth_user@localhost;`

- how to findout which user has logged in currently
    - `select user();`

- to use a database
    - `use auth;`

- to show the tables
    - `show tables;`


- basic authorization
    - need basic in header
 
- jwt 
    - needs bearer in token

- check this out
    - https://docs.docker.com/engine/install/linux-postinstall/


- pymysql error resolution
    - `https://github.com/PyMySQL/mysqlclient#prerequisites`

- `kubectl scale deployment --replicas=6 service`

- 