#!C:/Python/python.exe
import pymysql, cgitb, cgi, smtplib

print("Content-Type: text/html\r\n\r\n")
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="summer_project")
cur = con.cursor()

print("""
<!DOCTYPE html>
<html lang="en">
<head>
        <title>IST STUDENT RECORD</title>
        <meta name="view-port"  content="width=device-width;initial=1.0">
        <link rel="icon" href="images/ist.png">
    <style>
               body {
    font-family: Arial, sans-serif;
    margin: 0;
    background-color: #f0f0f0;
    background-size: cover;
    color: #e0e0e0;
    display: flex;
    flex-direction: column;
    min-height: 100vh;
    font-weight: bolder;
    overflow-x: hidden; /* Prevent horizontal scrolling */
}

.header {
    background-color:  rgb(36, 36, 87);
    color: white;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 20px;
    width: 100%;
    z-index: 1;
    box-sizing: border-box; /* Include padding and border in width */
}

.header img {
    height: 60px;
}

        .registration-form {
            margin-left:30vw;
            margin-top:20vh;
            background-color: white;
            padding: 20px;
            color: black;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 40vw;
        }
        .registration-form h2 {
            margin-bottom: 20px;
        }
        .registration-form label {
            display: block;
            margin-bottom: 5px;
        }
        .registration-form input {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        .registration-form button {
            width: 100%;
            padding: 10px;
            background-color: rgb(36, 36, 87);
            border: none;
            border-radius: 5px;
            color: white;
            font-size: 16px;
        }
        .registration-form button:hover {
            background-color: green;
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

<div class="registration-form">
    <h2>Forgot Password?</h2>
    <form action="#" method="post" enctype="multipart/form-data">
        <label for="regno">Enter Username :</label>
        <input type="text" id="regno" name="regno" required>
        <label for="email">Enter Email :</label>
        <input type="email" id="email" name="email" required>
        <button type="submit" name="submit">Submit</button>
    </form>
</div>

</body>
</html>
""")

form = cgi.FieldStorage()
Regno=form.getvalue("regno")
Email = form.getvalue("email")
Submit = form.getvalue("submit")

if Submit is not None:
    q = """SELECT * FROM student_details WHERE email_id='%s' AND register_no='%s'""" % (Email,Regno)
    cur.execute(q)
    res = cur.fetchall()
    con.commit()

    if res:
        q="""SELECT * FROM student_login WHERE username='%s'""" % (Regno)
        cur.execute(q)
        res = cur.fetchall()

        for row in res:
            Password = row[2]
            Name = row[1]


        fromaddress = 'mahimasj5868@gmail.com'
        ppassword = 'nbqo izhq vsyp cair'
        toaddress = Email
        subject = "Message From DEPARTMENT OF INFORMATION SCIENCE AND TECHNOLOGY ! "
        body = "Hello {} ,\n\n Your Password for IST STUDENT RECORD PAGE is {}".format(Name, Password)
        msg = """Subject: {} \n\n {}""".format(subject, body)
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.starttls()
        server.login(fromaddress, ppassword)
        server.sendmail(fromaddress, toaddress, msg)
        server.quit()

        print("""
        <script>
        alert("Mail sent successfully");
        location.href="student_login.py";
        </script>
        """)
    else:
        print("""
        <script>
        alert("Email not found");
        </script>
        """)
