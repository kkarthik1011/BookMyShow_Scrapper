import requests
from bs4 import BeautifulSoup
import re
import time
import smtplib, ssl

run = True
old_text_out = ""
while run :
    req_eng_2d = requests.get("https://in.bookmyshow.com/buytickets/spider-man-no-way-home-hyderabad/movie-hyd-ET00310790-MT/20211216")
    req_eng_3d = requests.get("https://in.bookmyshow.com/buytickets/spider-man-no-way-home-hyderabad/movie-hyd-ET00319080-MT/20211216")

    soup_eng_2d = BeautifulSoup(req_eng_2d.content , "html.parser")
    soup_eng_3d = BeautifulSoup(req_eng_3d.content , "html.parser")

    text_2d = soup_eng_2d.prettify()
    text_3d = soup_eng_3d.prettify()
    # initializing substring
    test_sub = 'data-name="'

    f = open("BMS.txt",'w')

    # print("Locations with English : 2D")
    f.write("Locations with English : 2D")
    f.write('\n')
    # using re.finditer()
    # All occurrences of substring in string
    res_2d = [i.start() for i in re.finditer(test_sub, text_2d)]
    res_2d = res_2d[9:]

    for start in res_2d:
        count = 0
        flag = 0
        while flag < 2:
            # print(text_2d[start+10+count],end="")
            f.write(text_2d[start+10+count])
            if text_2d[start+10+count] == '"' : flag +=1
            count += 1
        # print("")
        f.write('\n')
    # print("")
    f.write('\n')
    # print("Locations with English : 3D")
    f.write("Locations with English : 3D")

    test_sub = ',"name":"'

    # using re.finditer()
    # All occurrences of substring in string
    res_3d = [i.start() for i in re.finditer(test_sub, text_3d)]
    res_3d = res_3d[9:]

    for start in res_3d:
        count = 0
        flag = 0
        while flag < 2:
            # print(text_2d[start + 10 + count], end="")
            f.write(text_2d[start + 10 + count])
            if text_2d[start + 10 +count] == '"': flag += 1
            count += 1
        # print("")
        f.write("\n")
    # print("")
    f.write("\n")

    f.close()

    r = open("BMS.txt" ,'r')
    text_out = r.readlines()

    if old_text_out != text_out:
        sender_email = "python.king1011@gmail.com"
        receiver_email = "kkarthik1011@gmail.com, rahulguptab2210@gmail.com, dannychayt@gmail.com"
        message = """\
        Subject: Update In Tickets

        This message is sent from Python.
        
        """
        port = 465  # For SSL
        password = "pythonking"

        # Create a secure SSL context
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login("python.king1011@gmail.com", password)
            # TODO: Send email here
            server.sendmail(sender_email, receiver_email, message+str(text_out))

    old_text_out = text_out
    print(text_out)
    time.sleep(120)
