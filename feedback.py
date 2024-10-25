#!C:/Python/python.exe
import pymysql, cgitb, cgi,  smtplib

print("Content-type: text/html\r\n\r\n")
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="summer_project")
cur = con.cursor()

print("""
    <!DOCTYPE html>
<html>
    <head>
        <title>IST STUDENT RECORD</title>
        <meta name="view-port"  content="width=device-width;initial=1.0">
        <link rel="icon" href="images/ist.png">
        <link rel="stylesheet" href="login.css" type="text/css">
        <style>
            nav{
                position:relative;
            }
            .navbar {
            width:100vw;
            background-color: rgb(24, 24, 57);
            overflow: hidden;
            text-align: left;
        }

        .navbar a {
            display: inline-block;
            color: white;
            padding: 14px 20px;
            text-decoration: none;
            font-size: 1.2rem;
        }
        #sep:hover{
            background-color:rgb(24, 24, 57);
        }
        .navbar a:hover {
            background-color: red;
        }
            
.login-box {
   
    height: auto; /* Adjust according to header height */

}
        </style>
    </head>
    <body>
        <header>
            <section class="header">
                <div>
                    <img class="ceg" src="images/ceg.png" alt="au_logo" width="200px" height="150px">
                </div>
                <div>
                    <h2>DEPARTMENT OF INFORMATION SCIENCE AND TECHNOLOGY</h2>
                </div>
                <div>
                    <img class="ist" src="images/ist.png" alt="ist_logo" width="200px" height="150px">
                </div>
            </section>
        </header>
        <nav class="navbar">
            <a href="home.py">Home</a><a id="sep" >--></a>
            <a href="">Feed Back</a>
        </nav>
        <article>
            <section class="login-box">
                <div class="login-container">
                <div class="login">
                    <h2 style="color:red">FEEDBACK FORM</h2>
                    <form method="post" class="form" enctype="multipart/form-data">
                        <div class="regno">
                            <label for="regno">Register No :</label>
                            <input type="text" name="regno" id="regno" placeholder="Register no" required>
                        </div>
                        <div class="name">
                            <label for="name">Name :</label>
                            <input type="text" name="name"  id="name" placeholder="Name" required>
                        </div>
                        <div class="year">
                            <label for="year">Year :</label>
                            <input type="number" name="year" id="year" placeholder="Year" required>
                        </div>
                        <div class="feedback">
                            <label for="feedback">Feedback :</label>
                            <textarea rows='10' cols='55' name='feedback' placeholder="Enter Your feedback here!" required></textarea>
                        </div>
                        <div class="submit">
                            <button type="submit" id="submit" name="submit">SUBMIT</button>
                        </div>
                    </form>
                </div>
                </div>
            </section>
         
    </body>
</html>
""")

form=cgi.FieldStorage()
Regno=form.getvalue("regno")
Name=form.getvalue("name")
Year=form.getvalue("year")
Feedback=form.getvalue("feedback")
Submit=form.getvalue("submit")

if Submit != None :

    fromaddress = 'mahimasj5868@gmail.com'
    ppassword = 'nbqo izhq vsyp cair'
    toaddress = 'kikibot25@gmail.com'
    subject = "FEED BACK FROM IST STUDENT PAGE"
    body = "\nStudent Name : {}\nRegister No: {}\nYear :{}\nFeedback : {}   ".format(Name, Regno,Year,Feedback)
    msg = """Subject: {} \n\n {}""".format(subject, body)
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login(fromaddress, ppassword)
    server.sendmail(fromaddress, toaddress, msg)
    server.quit()

    print("""
            <script>
            alert("Thank You for Your Feedback");
            location.href="home.py";
            </script>
            """)


