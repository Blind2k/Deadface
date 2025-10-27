## Description

Players will be given an endpoint. This endpoint will slowly  help the user to build the correct request packet to access the flag. The server will return a specific error that will hint which header is missing.

Points 50
Created by @blind2k
Dependency NA
Attempts NA

## Challenge

 DEADFACE is up to their old tricks again! We’ve stumbled on to one of their web servers but we can’t figure out how to access it. We are confident that the proper request will get you any thing from the server. Can you use your head and try to build the perfect packet that will reveal the FLAG

 Submit your answer as `deadface{flag_text}`

## Hints

1. Some HTTP librariesframeworksbinaries may block “LOGIN” as method.
2. “Delta-time error”
   1. Time has many names.
3. Do we need 2 bf
   1. Only between 0-40

## Solution

First, discover the method using OPTIONS. The “Allow” header will contain “LOGIN” as method.

`curl -X OPTIONS -v $URL`

Once the method is set to LOGIN, add a header according the response. It is possible to google “http request headers

- You are not agent smith
  - User-Agent smith
- Sorry. You are not in Germany!”
  - Location Germany
- Delta-time error”
  - Age 30
- “Origin should be local”
  - Origin [http127.1](http127.1 ‌)
- “XSS protection is ON!”
  - X-XSS-Protection 0
- “You are being tracked”
  - DNT null
- “We don't like frames here!”
  - X-Frame-Options DENY
- “NOOOO!!!! Old-school caching is enabled!!”
  - Pragma no-cache
- “Possible sniffing is happening right now!”
  - X-Content-Type-Options nosniff
- “Override is required to get the flag”
  - X-HTTP-Method-Override GET

## Final command

Burp

```
LOGIN  HTTP1.1
Host env02.deadface.io8001
Accept texthtml,applicationxhtml+xml,applicationxml;q=0.9,;q=0.8
Accept-Language en-US,en;q=0.5
Accept-Encoding gzip, deflate, br
Connection keep-alive
Upgrade-Insecure-Requests 1
Priority u=0, i
User-Agent smith
Content-Length 0
Location Germany
Age 30
Origin http127.1
X-XSS-Protection 0
DNT null
X-Frame-Options DENY
Pragma no-cache
X-Content-Type-Options nosniff
X-HTTP-Method-Override GET
```

```shell
curl --header 
-X LOGIN http127.0.0.18080 
-H User-Agent smith 
-H Location Germany 
-H Age 30 
-H Origin http127.1 
-H X-XSS-Protection 0 
-H DNT null 
-H X-Frame-Options DENY 
-H Pragma no-cache 
-H X-Content-Type-Options nosniff 
-H X-HTTP-Method-Override GET
```

## Flag

deadface{itsAllInMyHeaders}