## Description

A Flask app with deliberate SQL injection vulnerabilities. Exploit the database to bypass authentication and extract information on the DB to get the flag.

Points: **100**
Created by: @blind2k
Dependency: N/A
Attempts: N/A

## Challenge

DEADFACE is taunting us! We found their link! There was a breach!. How deep, and how for heaven’s sakes did they got in, we don’t know! Can you locate their backdoor string?

## Hints

1. How many DBs are there?

## Solution

1. Navigate to the root URL
2. Use `admin' -- `as the user name.
   1. Password is irrelevant
   2. Spaces before & after the “--” are critical

Once bypassed, user will be redirected to /dashboard.

![image.png](https://trello.com/1/cards/68cd9b565787c0e2659dcce7/attachments/68f13ed877a9f2be13f98f70/download/image.png)

To get the table names:

1. Change the tag with `id="database"` from `<select>` to `<input>`
2. Send `sqlite_master -- ` to the server to get the list of tables

To get the flag:

1. Repeat step 3
2. Send`general`-- as the database

## Flag

DEADFACE{you\_found\_the\_sqli\_01_flag!}