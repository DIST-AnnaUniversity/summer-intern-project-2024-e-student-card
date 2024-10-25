#!C:/Python/python.exe
import pymysql, cgitb, cgi, os

print("Content-type: text/html\r\n\r\n")
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="summer_project")
cur = con.cursor()

form=cgi.FieldStorage()
Regno=form.getvalue("id")

q="""SELECT * FROM batch_details WHERE register_no='%s'"""%(Regno)
cur.execute(q)
res=cur.fetchone()

Name=res[3]
Phoneno=res[4]
EmailId=res[5]
FacultyName=res[6]

q="""SELECT photo FROM student_details WHERE register_no='%s'"""%(Regno)
cur.execute(q)
res=cur.fetchone()

if res:
    Photo = res[0]
else:
    Photo="image_dummy.jpeg"
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IST STUDENT RECORD</title>
    <link rel="icon" href="images/ist.png">
    <style>
        * {
            padding: 0;
            margin: 0;
            box-sizing: border-box;
        }

        body {
            font-family: Georgia, 'Times New Roman', Times, serif;
            word-spacing: 0.5rem;
            line-height: 1.5rem;
            margin: 0;
            background-color: #f0f0f0;
        }

        .header {
            background-color: rgb(36, 36, 87);
            color: white;
            display: flex;
            align-items: center;
            padding: 5px 20px;
            width: 100%;
        }

        .header img {
            width:10vw;
            height:auto;
            padding-left:30px;
            padding-right:30px;
        }

        .header h2 {
            color: white;
            text-align:center;

        }

        .main {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 70px; /* Adjust margin for header height */
            padding: 2rem;
        }

        .welcome {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-bottom: 2rem;
        }

        .welcome img {
            width: 200px;
            height: auto;
            border-radius: 10px;
        }

        .welcome p {
            font-size: 1.5rem;
            color: rgb(36, 36, 87);
            margin-top: 1rem;
            text-align: center;
        }

        .form-container {
            background-color: white;
            width: 100%;
            max-width: 800px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            padding: 2rem;
            box-sizing: border-box;
        }

        .form-container h2 {
            font-size: 1.5rem;
            color: rgb(36, 36, 87);
            margin-bottom: 1rem;
            border-bottom: 2px solid rgb(36, 36, 87);
            padding-bottom: 0.5rem;
            position: relative;
            cursor: pointer;
        }

        .form-container .button-group {
            display: none;
            margin-top: 1rem;
        }

        .form-container .button-group.active {
            display: block;
        }

        .form-container button {
            display: block;
            width: 100%;
            padding: 1rem;
            margin: 0.5rem 0;
            font-size: 1rem;
            color: white;
            background-color: rgb(36, 36, 87);
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .form-container button:hover {
            background-color: rgb(24, 24, 57);
        }
        
        .navbar {
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

    </style>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const headings = document.querySelectorAll('.form-container h2');

            headings.forEach(heading => {
                heading.addEventListener('click', () => {
                    const buttonGroup = heading.nextElementSibling;
                    buttonGroup.classList.toggle('active');
                });
            });
             if (window.history.replaceState) {
                window.history.replaceState(null, null, window.location.href);
            }
        });
    </script>
</head>
""")
print(f"""
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
        <a href="">Student Details</a>
    </nav>
    <div class="main">
        <div class="welcome">
            <img src="photos/{Photo}" alt="Welcome Image">
            <p>Welcome {Name}</p>
            <p>{Regno}</p>
        </div>
        <div class="form-container">
            <form method="post" enctype="multipart/form-data">
                <h2>Personal Details</h2>
                <div class="button-group">
                    <button type="submit" name="personal" value="personal">Personal Details</button>
                </div>
                <h2>Academic Details</h2>
                <div class="button-group">
                    <button type="submit" name="sem1" value="sem1">Semester 1</button>
                    <button type="submit" name="sem2" value="sem2">Semester 2</button>
                    <button type="submit" name="sem3" value="sem3">Semester 3</button>
                    <button type="submit" name="sem4" value="sem4">Semester 4</button>
                    <button type="submit" name="sem5" value="sem5">Semester 5</button>
                    <button type="submit" name="sem6" value="sem6">Semester 6</button>
                    <button type="submit" name="sem7" value="sem7">Semester 7</button>
                    <button type="submit" name="sem8" value="sem8">Semester 8</button>
                </div>
                <h2>Project Details</h2>
                <div class="button-group">
                    <button type="submit" name="project" value="project">Project Details</button>
                </div>
                <h2>Exit Student Details</h2>
                <div class="button-group">
                    <button type="submit" name="exit-placement" value="exit-placement">Placement</button>
                    <button type="submit" name="exit-exam" value="exit-exam">Exam</button>
                    <button type="submit" name="exit-higher" value="exit-higher">Higher Studies</button>
                    <button type="submit" name="exit-paper" value="exit-paper">Paper Published</button>
                    <button type="submit" name="exit-events" value="exit-events">Technical Events</button>
                </div>
            </form>
        </div>
    </div>
</body>
</html>

""")

Sem1=form.getvalue("sem1")
Sem2=form.getvalue("sem2")
Sem3=form.getvalue("sem3")
Sem4=form.getvalue("sem4")
Sem5=form.getvalue("sem5")
Sem6=form.getvalue("sem6")
Sem7=form.getvalue("sem7")
Sem8=form.getvalue("sem8")

Personal=form.getvalue("personal")
Project=form.getvalue("project")
Placement=form.getvalue("exit-placement")
Exam=form.getvalue("exit-exam")
HigherStudies=form.getvalue("exit-higher")
Paper=form.getvalue("exit-paper")
Events=form.getvalue("exit-events")

if Sem1:
    q="SELECT id from sem1 WHERE register_no='%s'" % (Regno)
    cur.execute(q)
    rec = cur.fetchone()
    if rec:
        q="""SELECT status FROM sem1 WHERE register_no='%s'"""%(Regno)
        cur.execute(q)
        res= cur.fetchone()

        if res[0] == "UNLOCK":
            print("""
                    <script>
                    location.href='sem1.py?id=%s';
                    </script>
                    """ % Regno)
        else:
            print("""
                   <script>
                   alert("Semester 1 details already filled!! For further information contact department office!!")
                   </script>
                   """)

    else:
        print("""
        <script>
        location.href='sem1.py?id=%s';
        </script>
        """ % Regno)

elif Sem2:
    q = "SELECT id from sem2 WHERE register_no='%s'" % (Regno)
    cur.execute(q)
    rec = cur.fetchone()
    if rec:
        q = """SELECT status FROM sem2 WHERE register_no='%s'""" % (Regno)
        cur.execute(q)
        res = cur.fetchone()

        if res[0] == "UNLOCK":
            print("""
                            <script>
                            location.href='sem2.py?id=%s';
                            </script>
                            """ % Regno)
        else:
            print("""
                           <script>
                           alert("Semester 2 details already filled!! For further information contact department office!!")
                           </script>
                           """)

    else:
        print("""
        <script>
        location.href='sem2.py?id=%s';
        </script>
        """ % Regno)

elif Sem3:
    q = "SELECT id from sem3 WHERE register_no='%s'" % (Regno)
    cur.execute(q)
    rec = cur.fetchone()
    if rec:
        q = """SELECT status FROM sem3 WHERE register_no='%s'""" % (Regno)
        cur.execute(q)
        res = cur.fetchone()

        if res[0] == "UNLOCK":
            print("""
                            <script>
                            location.href='sem3.py?id=%s';
                            </script>
                            """ % Regno)
        else:
            print("""
                           <script>
                           alert("Semester 3 details already filled!! For further information contact department office!!")
                           </script>
                           """)

    else:
        print("""
        <script>
        location.href='sem3.py?id=%s';
        </script>
        """ % Regno)

elif Sem4:
    q = "SELECT id from sem4 WHERE register_no='%s'" % (Regno)
    cur.execute(q)
    rec = cur.fetchone()
    if rec:
        q = """SELECT status FROM sem4 WHERE register_no='%s'""" % (Regno)
        cur.execute(q)
        res = cur.fetchone()

        if res[0] == "UNLOCK":
            print("""
                            <script>
                            location.href='sem4.py?id=%s';
                            </script>
                            """ % Regno)
        else:
            print("""
                           <script>
                           alert("Semester 4 details already filled!! For further information contact department office!!")
                           </script>
                           """)

    else:
        print("""
        <script>
        location.href='sem4.py?id=%s';
        </script>
        """ % Regno)

elif Sem5:
    q = "SELECT id from sem5 WHERE register_no='%s'" % (Regno)
    cur.execute(q)
    rec = cur.fetchone()
    if rec:
        q = """SELECT status FROM sem5 WHERE register_no='%s'""" % (Regno)
        cur.execute(q)
        res = cur.fetchone()

        if res[0] == "UNLOCK":
            print("""
                            <script>
                            location.href='sem5.py?id=%s';
                            </script>
                            """ % Regno)
        else:
            print("""
                           <script>
                           alert("Semester 5 details already filled!! For further information contact department office!!")
                           </script>
                           """)

    else:
        print("""
        <script>
        location.href='sem5.py?id=%s';
        </script>
        """ % Regno)

elif Sem6:
    q = "SELECT id from sem6 WHERE register_no='%s'" % (Regno)
    cur.execute(q)
    rec = cur.fetchone()
    if rec:
        q = """SELECT status FROM sem6 WHERE register_no='%s'""" % (Regno)
        cur.execute(q)
        res = cur.fetchone()

        if res[0] == "UNLOCK":
            print("""
                            <script>
                            location.href='sem6.py?id=%s';
                            </script>
                            """ % Regno)
        else:
            print("""
                           <script>
                           alert("Semester 6 details already filled!! For further information contact department office!!")
                           </script>
                           """)

    else:
        print("""
        <script>
        location.href='sem6.py?id=%s';
        </script>
        """ % Regno)

elif Sem7:
    q = "SELECT id from sem7 WHERE register_no='%s'" % (Regno)
    cur.execute(q)
    rec = cur.fetchone()
    if rec:
        q = """SELECT status FROM sem7 WHERE register_no='%s'""" % (Regno)
        cur.execute(q)
        res = cur.fetchone()

        if res[0] == "UNLOCK":
            print("""
                            <script>
                            location.href='sem7.py?id=%s';
                            </script>
                            """ % Regno)
        else:
            print("""
                           <script>
                           alert("Semester 7 details already filled!! For further information contact department office!!")
                           </script>
                           """)

    else:
        print("""
        <script>
        location.href='sem7.py?id=%s';
        </script>
        """ % Regno)

elif Sem8:
    q = "SELECT id from sem8 WHERE register_no='%s'" % (Regno)
    cur.execute(q)
    rec = cur.fetchone()
    if rec:
        q = """SELECT status FROM sem8 WHERE register_no='%s'""" % (Regno)
        cur.execute(q)
        res = cur.fetchone()

        if res[0] == "UNLOCK":
            print("""
                            <script>
                            location.href='sem8.py?id=%s';
                            </script>
                            """ % Regno)
        else:
            print("""
                           <script>
                           alert("Semester 8 details already filled!! For further information contact department office!!")
                           </script>
                           """)

    else:
        print("""
        <script>
        location.href='sem8.py?id=%s';
        </script>
        """ % Regno)

elif Project:
    print("""
    <script>
    location.href='project.py?id=%s';
    </script>
    """ % Regno)

elif Placement:
    print("""
    <script>
    location.href='details.py?id=%s';
    </script>
    """ % Regno)

elif Exam:
    print("""
    <script>
    location.href='exam.py?id=%s';
    </script>
    """ % Regno)

elif HigherStudies:
    print("""
    <script>
    location.href='highereducation.py?id=%s';
    </script>
    """ % Regno)

elif Paper:
    print("""
    <script>
    location.href='paperpublished.py?id=%s';
    </script>
    """ % Regno)

elif Events:
    print("""
    <script>
    location.href='events.py?id=%s';
    </script>
    """ % Regno)

elif Personal:
    q = "SELECT id from student_details WHERE register_no='%s'" % (Regno)
    cur.execute(q)
    rec = cur.fetchone()
    if rec:
        print("""
           <script>
           alert("Personal details already filled!! For further information contact department office!!")
           </script>
           """)
    else:
        print("""
           <script>
           location.href='student.py?id=%s';
           </script>
           """ % Regno)
