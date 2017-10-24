# DropKick for LIFE (SERVER)
Dropkick for LIFE is for contributes to the reduction of suicide rate in the Republic of Korea.

This is Server Side App Source code

v0.1 -- 2017/10/25
Made of Django Framework (PYTHON3)

#Starting this APP
  1. pull this git 
  2. run "python3 manage.py runserver"

#Process

Input Korean Sentence at http://yourIPAddress:PORT(default:8000)/app/  

##[method - POST, req - 'send' Header]##

Then, It will take KONLPY process and Do morphological decomposition.

Finally, The original text, date time, and analysis result are saved in DB.
