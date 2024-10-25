#!C:/Python/python.exe
import pymysql, cgitb, cgi, os

print("Content-type: text/html\r\n\r\n")
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="summer_project")
cur = con.cursor()

print("""
     <!DOCTYPE html>
<html>
<head>
    <title>IST STUDENT RECORD</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" href="images/ist.png">
    <link rel="stylesheet" href="login.css" type="text/css">
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
    <article>
        <section class="login-box">
            <div class="login-container">
                <div class="login-image">
                    <img src="images/login_photo2.gif" alt="Login Image">
                </div>
                <div class="login">
                    <h2>STAFF LOGIN</h2>
                    <form method="post" class="form" enctype="multipart/form-data">
                        <div class="username">
                            <label for="username">User Name:</label>
                            <input type="text" name="username" id="username" placeholder="staffid" required>
                        </div>
                        <div class="password">
                            <label for="password">Password:</label>
                            <input type="password" name="password" id="password" placeholder="password" required>
                        </div>
                        <div class="forgot">
                            <p><a href="staff_change.py">Change password?</a></p>
                            <p><a href="staff_forgot.py">Forgot password?</a></p>
                        </div>
                        <div class="submit">
                            <button type="submit" id="submit" name="submit">LOGIN</button>
                        </div>
                    </form>
                </div>
            </div>
        </section>
    </article>
</body>
</html>
""")

form=cgi.FieldStorage()
Username=form.getvalue("username")
Password=form.getvalue("password")
Submit=form.getvalue("submit")

if Submit != None :

    q="""SELECT id FROM staff_login WHERE username='%s' AND password='%s'"""%(Username,Password)
    cur.execute(q)
    rec = cur.fetchone()

    if rec != None:
        print("""
                    <script>
                    alert("logged in successfully");
                    location.href ='staff_main.py?id=%s';
                    </script>
                    """ % Username)

    else:
        print("""
                    <script>
                    alert("Invalid username and password ");
                    </script>
                    """)



