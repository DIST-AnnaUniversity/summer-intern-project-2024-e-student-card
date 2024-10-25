#!C:/Python/python.exe
import pymysql
import cgitb
import cgi
import smtplib
import random
import os

print("Content-Type: text/html\r\n\r\n")
cgitb.enable()

con = pymysql.connect(host="localhost", user="root", password="", database="summer_project")
cur = con.cursor()

form = cgi.FieldStorage()
Staffid= form.getvalue("staffid")
Email = form.getvalue("email")
Submit = form.getvalue("submit")
OtpSubmit = form.getvalue("otp_submit")
ResetSubmit = form.getvalue("reset_submit")
Otp = form.getvalue("otp")
NewPassword = form.getvalue("new_password")
ConfirmPassword = form.getvalue("confirm_password")
Randno = form.getvalue("randno")

# HTML structure
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <title>IST STUDENT RECORD</title>
    <meta name="view-port" content="width=device-width;initial=1.0">
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
            overflow-x: hidden;
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
            box-sizing: border-box;
        }
        .header img {
            height: 60px;
        }
        .registration-form {
            margin-left: 30vw;
            margin-top: 20vh;
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
""")

if Submit is not None:
    q = """SELECT * FROM staff_details WHERE email_id='%s' AND staffid='%s'""" % (Email, Staffid)
    cur.execute(q)
    res = cur.fetchall()
    con.commit()

    if res:
        q = """SELECT * FROM staff_login WHERE username='%s'""" % (Staffid)
        cur.execute(q)
        res = cur.fetchall()

        for row in res:
            Password = row[2]
            Name = row[1]

        fromaddress = 'mahimasj5868@gmail.com'
        ppassword = 'nbqo izhq vsyp cair'
        toaddress = Email
        subject = "Message From DEPARTMENT OF INFORMATION SCIENCE AND TECHNOLOGY!"
        Randno = random.randint(10000000, 99999999)
        body = "Hello {} ,\n\n OTP for IST STUDENT RECORD PAGE is {}".format(Name, Randno)
        msg = """Subject: {} \n\n {}""".format(subject, body)
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.starttls()
        server.login(fromaddress, ppassword)
        server.sendmail(fromaddress, toaddress, msg)
        server.quit()

        print("""
        <h2>Enter OTP</h2>
        <form action="" method="post" enctype="multipart/form-data">
            <label for="otp">Enter OTP :</label>
            <input type="text" id="otp" name="otp" required>
            <input type="hidden" name="staffid" value="{}">
            <input type="hidden" name="email" value="{}">
            <input type="hidden" name="randno" value="{}">
            <button type="submit" name="otp_submit">Submit OTP</button>
        </form>
        """.format(Staffid, Email, Randno))

    else:
        print("""
        <script>
        alert("Email not found");
        </script>
        """)

elif OtpSubmit is not None:
    if Otp == Randno:
        print("""
        <h2>Reset Password</h2>
        <form action="" method="post" enctype="multipart/form-data">
            <label for="new_password">New Password:</label>
            <input type="password" id="new_password" name="new_password" required>
            <label for="confirm_password">Confirm Password:</label>
            <input type="password" id="confirm_password" name="confirm_password" required>
            <input type="hidden" name="staffid" value="{}">
            <input type="hidden" name="email" value="{}">
            <button type="submit" name="reset_submit">Reset Password</button>
        </form>
        """.format(Staffid, Email))
    else:
        print("""
        <script>
        alert("Incorrect OTP");
        </script>
        """)

elif ResetSubmit is not None:
    if NewPassword == ConfirmPassword:
        q = """UPDATE staff_login SET password='%s' WHERE username='%s'""" % (NewPassword, Staffid)
        cur.execute(q)
        con.commit()
        print("""
        <script>
        alert("Password reset successfully");
        location.href="staff_login.py";
        </script>
        """)
    else:
        print("""
        <script>
        alert("Passwords do not match");
        </script>
        """)

else:
    print("""
    <h2>Change Password:</h2>
    <form action="" method="post" enctype="multipart/form-data">
        <label for="staffid">Enter Username :</label>
        <input type="text" id="staffid" name="staffid" required>
        <label for="email">Enter Email :</label>
        <input type="email" id="email" name="email" required>
        <button type="submit" name="submit">Submit</button>
    </form>
    """)

print("""
</div>
</body>
</html>
""")

con.close()
