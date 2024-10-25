#!C:/Python/python.exe
import pymysql
import cgitb
import cgi

print("Content-type: text/html\r\n\r\n")
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="summer_project")
cur = con.cursor()

form=cgi.FieldStorage()
Regno=form.getvalue("id")
Staffid=form.getvalue("staffid")

# HTML structure
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IST STUDENT RECORD</title>
    <link rel="icon" href="images/ist.png">
    <link rel="stylesheet" href="fetching.css" type="text/css">
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
                <h1>DEPARTMENT OF INFORMATION SCIENCE AND TECHNOLOGY</h1>
            </div>
            <div>
                <img class="ist" src="images/ist.png" alt="ist_logo" width="200px" height="150px">
            </div>
        </section>
    </header>
    <nav class="navbar">
        <a href="home.py">Home</a><a id="sep" >--></a>
        <a href="staff_main.py?id={Staffid}">Dashboard</a><a id="sep" >--></a>
        <a href="">{Regno}  </a>
    </nav>
    <div class="wrapper"> 

        <div class="content">
            
""")

q = """SELECT * FROM student_details WHERE register_no='%s'""" % (Regno)
cur.execute(q)
personal_details = cur.fetchone()

q = """SELECT * FROM sem1 WHERE register_no='%s'""" % (Regno)
cur.execute(q)
sem1 = cur.fetchone()

q = """SELECT * FROM sem2 WHERE register_no='%s'""" % (Regno)
cur.execute(q)
sem2 = cur.fetchone()

q = """SELECT * FROM sem3 WHERE register_no='%s'""" % (Regno)
cur.execute(q)
sem3 = cur.fetchone()

q = """SELECT * FROM sem4 WHERE register_no='%s'""" % (Regno)
cur.execute(q)
sem4 = cur.fetchone()

q = """SELECT * FROM sem5 WHERE register_no='%s'""" % (Regno)
cur.execute(q)
sem5 = cur.fetchone()

q = """SELECT * FROM sem6 WHERE register_no='%s'""" % (Regno)
cur.execute(q)
sem6 = cur.fetchone()

q = """SELECT * FROM sem7 WHERE register_no='%s'""" % (Regno)
cur.execute(q)
sem7 = cur.fetchone()

q = """SELECT * FROM sem8 WHERE register_no='%s'""" % (Regno)
cur.execute(q)
sem8 = cur.fetchone()

if personal_details:
    print(f"""
             <img src="photos/{personal_details[1]}" alt="Welcome Image" style="width: 180px;height: auto; border-radius: 10px;margin-bottom: 10px">
            <p ><span style="color:red">Name:</span> {personal_details[2]}</p>
            <p ><span style="color:red">Register No:</span> {personal_details[3]}</p>
            """)

if sem1:
    print(""" <br><br><hr><br<br>""")
    print('<h2>Academic Details </h2><br><h2> Semester 1</h2>')
    print("""
            <table>
                <tr>
                    <th>Subject</th>
                    <th>Code</th>
                    <th>Credit</th>
                    <th>Grade</th>
                    <th>Reappear/Passed Year</th>
                </tr>
        """)

    print(f"""
                <tr>
                    <td>{sem1[2]}</td>
                    <td>{sem1[3]}</td>
                    <td>{sem1[4]}</td>
                    <td>{sem1[5]}</td>
                    <td>{sem1[6]}</td>
                </tr>
                <tr>
                    <td>{sem1[7]}</td>
                    <td>{sem1[8]}</td>
                    <td>{sem1[9]}</td>
                    <td>{sem1[10]}</td>
                    <td>{sem1[11]}</td>
                </tr>
                <tr>
                    <td>{sem1[12]}</td>
                    <td>{sem1[13]}</td>
                    <td>{sem1[14]}</td>
                    <td>{sem1[15]}</td>
                    <td>{sem1[16]}</td>
                </tr>
                <tr>
                    <td>{sem1[17]}</td>
                    <td>{sem1[18]}</td>
                    <td>{sem1[19]}</td>
                    <td>{sem1[20]}</td>
                    <td>{sem1[21]}</td>
                </tr>
                <tr>
                    <td>{sem1[22]}</td>
                    <td>{sem1[23]}</td>
                    <td>{sem1[24]}</td>
                    <td>{sem1[25]}</td>
                    <td>{sem1[26]}</td>
                </tr>
                <tr>
                    <td>{sem1[27]}</td>
                    <td>{sem1[28]}</td>
                    <td>{sem1[29]}</td>
                    <td>{sem1[30]}</td>
                    <td>{sem1[31]}</td>
                </tr>
                <tr>
                    <td>{sem1[32]}</td>
                    <td>{sem1[33]}</td>
                    <td>{sem1[34]}</td>
                    <td>{sem1[35]}</td>
                    <td>{sem1[36]}</td>
                </tr>
                <tr>
                    <td>{sem1[37]}</td>
                    <td>{sem1[38]}</td>
                    <td>{sem1[39]}</td>
                    <td>{sem1[40]}</td>
                    <td>{sem1[41]}</td>
                </tr>
                <tr>
                    <td>{sem1[42]}</td>
                    <td>{sem1[43]}</td>
                    <td>{sem1[44]}</td>
                    <td>{sem1[45]}</td>
                    <td>{sem1[46]}</td>
                </tr>
                <tr>
                    <td>{sem1[47]}</td>
                    <td>{sem1[48]}</td>
                    <td>{sem1[49]}</td>
                    <td>{sem1[50]}</td>
                    <td>{sem1[51]}</td>
                </tr>
            """)
    print("</table>")

    print(f"""<br>
        <p> Total Credits : {sem1[52]}<br>
         Earned Credits : {sem1[53]}<br>
        Gpa : {sem1[54]}<br><hr>
        """)
if sem2:
    print(""" <br><br><hr><br<br>""")
    print('<h2>Semester 2</h2>')
    print("""
            <table>
                <tr>
                    <th>Subject</th>
                    <th>Code</th>
                    <th>Credit</th>
                    <th>Grade</th>
                    <th>Reappear/Passed Year</th>
                </tr>
        """)

    print(f"""
                <tr>
                    <td>{sem2[2]}</td>
                    <td>{sem2[3]}</td>
                    <td>{sem2[4]}</td>
                    <td>{sem2[5]}</td>
                    <td>{sem2[6]}</td>
                </tr>
                <tr>
                    <td>{sem2[7]}</td>
                    <td>{sem2[8]}</td>
                    <td>{sem2[9]}</td>
                    <td>{sem2[10]}</td>
                    <td>{sem2[11]}</td>
                </tr>
                <tr>
                    <td>{sem2[12]}</td>
                    <td>{sem2[13]}</td>
                    <td>{sem2[14]}</td>
                    <td>{sem2[15]}</td>
                    <td>{sem2[16]}</td>
                </tr>
                <tr>
                    <td>{sem2[17]}</td>
                    <td>{sem2[18]}</td>
                    <td>{sem2[19]}</td>
                    <td>{sem2[20]}</td>
                    <td>{sem2[21]}</td>
                </tr>
                <tr>
                    <td>{sem2[22]}</td>
                    <td>{sem2[23]}</td>
                    <td>{sem2[24]}</td>
                    <td>{sem2[25]}</td>
                    <td>{sem2[26]}</td>
                </tr>
                <tr>
                    <td>{sem2[27]}</td>
                    <td>{sem2[28]}</td>
                    <td>{sem2[29]}</td>
                    <td>{sem2[30]}</td>
                    <td>{sem2[31]}</td>
                </tr>
                <tr>
                    <td>{sem2[32]}</td>
                    <td>{sem2[33]}</td>
                    <td>{sem2[34]}</td>
                    <td>{sem2[35]}</td>
                    <td>{sem2[36]}</td>
                </tr>
                <tr>
                    <td>{sem2[37]}</td>
                    <td>{sem2[38]}</td>
                    <td>{sem2[39]}</td>
                    <td>{sem2[40]}</td>
                    <td>{sem2[41]}</td>
                </tr>
                <tr>
                    <td>{sem2[42]}</td>
                    <td>{sem2[43]}</td>
                    <td>{sem2[44]}</td>
                    <td>{sem2[45]}</td>
                    <td>{sem2[46]}</td>
                </tr>
                <tr>
                    <td>{sem2[47]}</td>
                    <td>{sem2[48]}</td>
                    <td>{sem2[49]}</td>
                    <td>{sem2[50]}</td>
                    <td>{sem2[51]}</td>
                </tr>
            """)
    print("</table>")

    print(f"""<br>
        <p> Total Credits : {sem2[52]}<br>
         Earned Credits : {sem2[53]}<br>
        Gpa : {sem2[54]}<br><hr>
        """)
if sem3:
    print(""" <br><br><hr><br<br>""")
    print('<h2>Semester 3</h2>')
    print("""
            <table>
                <tr>
                    <th>Subject</th>
                    <th>Code</th>
                    <th>Credit</th>
                    <th>Grade</th>
                    <th>Reappear/Passed Year</th>
                </tr>
        """)

    print(f"""
                <tr>
                    <td>{sem3[2]}</td>
                    <td>{sem3[3]}</td>
                    <td>{sem3[4]}</td>
                    <td>{sem3[5]}</td>
                    <td>{sem3[6]}</td>
                </tr>
                <tr>
                    <td>{sem3[7]}</td>
                    <td>{sem3[8]}</td>
                    <td>{sem3[9]}</td>
                    <td>{sem3[10]}</td>
                    <td>{sem3[11]}</td>
                </tr>
                <tr>
                    <td>{sem3[12]}</td>
                    <td>{sem3[13]}</td>
                    <td>{sem3[14]}</td>
                    <td>{sem3[15]}</td>
                    <td>{sem3[16]}</td>
                </tr>
                <tr>
                    <td>{sem3[17]}</td>
                    <td>{sem3[18]}</td>
                    <td>{sem3[19]}</td>
                    <td>{sem3[20]}</td>
                    <td>{sem3[21]}</td>
                </tr>
                <tr>
                    <td>{sem3[22]}</td>
                    <td>{sem3[23]}</td>
                    <td>{sem3[24]}</td>
                    <td>{sem3[25]}</td>
                    <td>{sem3[26]}</td>
                </tr>
                <tr>
                    <td>{sem3[27]}</td>
                    <td>{sem3[28]}</td>
                    <td>{sem3[29]}</td>
                    <td>{sem3[30]}</td>
                    <td>{sem3[31]}</td>
                </tr>
                <tr>
                    <td>{sem3[32]}</td>
                    <td>{sem3[33]}</td>
                    <td>{sem3[34]}</td>
                    <td>{sem3[35]}</td>
                    <td>{sem3[36]}</td>
                </tr>
                <tr>
                    <td>{sem3[37]}</td>
                    <td>{sem3[38]}</td>
                    <td>{sem3[39]}</td>
                    <td>{sem3[40]}</td>
                    <td>{sem3[41]}</td>
                </tr>
                <tr>
                    <td>{sem3[42]}</td>
                    <td>{sem3[43]}</td>
                    <td>{sem3[44]}</td>
                    <td>{sem3[45]}</td>
                    <td>{sem3[46]}</td>
                </tr>
                <tr>
                    <td>{sem3[47]}</td>
                    <td>{sem3[48]}</td>
                    <td>{sem3[49]}</td>
                    <td>{sem3[50]}</td>
                    <td>{sem3[51]}</td>
                </tr>
            """)
    print("</table>")

    print(f"""<br>
        <p> Total Credits : {sem3[52]}<br>
         Earned Credits : {sem3[53]}<br>
        Gpa : {sem3[54]}<br><hr>
        """)
if sem4:
    print(""" <br><br><hr><br<br>""")
    print('<h2>Semester 4</h2>')
    print("""
            <table>
                <tr>
                    <th>Subject</th>
                    <th>Code</th>
                    <th>Credit</th>
                    <th>Grade</th>
                    <th>Reappear/Passed Year</th>
                </tr>
        """)

    print(f"""
                <tr>
                    <td>{sem4[2]}</td>
                    <td>{sem4[3]}</td>
                    <td>{sem4[4]}</td>
                    <td>{sem4[5]}</td>
                    <td>{sem4[6]}</td>
                </tr>
                <tr>
                    <td>{sem4[7]}</td>
                    <td>{sem4[8]}</td>
                    <td>{sem4[9]}</td>
                    <td>{sem4[10]}</td>
                    <td>{sem4[11]}</td>
                </tr>
                <tr>
                    <td>{sem4[12]}</td>
                    <td>{sem4[13]}</td>
                    <td>{sem4[14]}</td>
                    <td>{sem4[15]}</td>
                    <td>{sem4[16]}</td>
                </tr>
                <tr>
                    <td>{sem4[17]}</td>
                    <td>{sem4[18]}</td>
                    <td>{sem4[19]}</td>
                    <td>{sem4[20]}</td>
                    <td>{sem4[21]}</td>
                </tr>
                <tr>
                    <td>{sem4[22]}</td>
                    <td>{sem4[23]}</td>
                    <td>{sem4[24]}</td>
                    <td>{sem4[25]}</td>
                    <td>{sem4[26]}</td>
                </tr>
                <tr>
                    <td>{sem4[27]}</td>
                    <td>{sem4[28]}</td>
                    <td>{sem4[29]}</td>
                    <td>{sem4[30]}</td>
                    <td>{sem4[31]}</td>
                </tr>
                <tr>
                    <td>{sem4[32]}</td>
                    <td>{sem4[33]}</td>
                    <td>{sem4[34]}</td>
                    <td>{sem4[35]}</td>
                    <td>{sem4[36]}</td>
                </tr>
                <tr>
                    <td>{sem4[37]}</td>
                    <td>{sem4[38]}</td>
                    <td>{sem4[39]}</td>
                    <td>{sem4[40]}</td>
                    <td>{sem4[41]}</td>
                </tr>
                <tr>
                    <td>{sem4[42]}</td>
                    <td>{sem4[43]}</td>
                    <td>{sem4[44]}</td>
                    <td>{sem4[45]}</td>
                    <td>{sem4[46]}</td>
                </tr>
                <tr>
                    <td>{sem4[47]}</td>
                    <td>{sem4[48]}</td>
                    <td>{sem4[49]}</td>
                    <td>{sem4[50]}</td>
                    <td>{sem4[51]}</td>
                </tr>
            """)
    print("</table>")

    print(f"""<br>
        <p> Total Credits : {sem4[52]}<br>
         Earned Credits : {sem4[53]}<br>
        Gpa : {sem4[54]}<br><hr>
        """)
if sem5:
    print(""" <br><br><hr><br<br>""")
    print('<h2>Semester 5</h2>')
    print("""
            <table>
                <tr>
                    <th>Subject</th>
                    <th>Code</th>
                    <th>Credit</th>
                    <th>Grade</th>
                    <th>Reappear/Passed Year</th>
                </tr>
        """)

    print(f"""
                <tr>
                    <td>{sem5[2]}</td>
                    <td>{sem5[3]}</td>
                    <td>{sem5[4]}</td>
                    <td>{sem5[5]}</td>
                    <td>{sem5[6]}</td>
                </tr>
                <tr>
                    <td>{sem5[7]}</td>
                    <td>{sem5[8]}</td>
                    <td>{sem5[9]}</td>
                    <td>{sem5[10]}</td>
                    <td>{sem5[11]}</td>
                </tr>
                <tr>
                    <td>{sem5[12]}</td>
                    <td>{sem5[13]}</td>
                    <td>{sem5[14]}</td>
                    <td>{sem5[15]}</td>
                    <td>{sem5[16]}</td>
                </tr>
                <tr>
                    <td>{sem5[17]}</td>
                    <td>{sem5[18]}</td>
                    <td>{sem5[19]}</td>
                    <td>{sem5[20]}</td>
                    <td>{sem5[21]}</td>
                </tr>
                <tr>
                    <td>{sem5[22]}</td>
                    <td>{sem5[23]}</td>
                    <td>{sem5[24]}</td>
                    <td>{sem5[25]}</td>
                    <td>{sem5[26]}</td>
                </tr>
                <tr>
                    <td>{sem5[27]}</td>
                    <td>{sem5[28]}</td>
                    <td>{sem5[29]}</td>
                    <td>{sem5[30]}</td>
                    <td>{sem5[31]}</td>
                </tr>
                <tr>
                    <td>{sem5[32]}</td>
                    <td>{sem5[33]}</td>
                    <td>{sem5[34]}</td>
                    <td>{sem5[35]}</td>
                    <td>{sem5[36]}</td>
                </tr>
                <tr>
                    <td>{sem5[37]}</td>
                    <td>{sem5[38]}</td>
                    <td>{sem5[39]}</td>
                    <td>{sem5[40]}</td>
                    <td>{sem5[41]}</td>
                </tr>
                <tr>
                    <td>{sem5[42]}</td>
                    <td>{sem5[43]}</td>
                    <td>{sem5[44]}</td>
                    <td>{sem5[45]}</td>
                    <td>{sem5[46]}</td>
                </tr>
                <tr>
                    <td>{sem5[47]}</td>
                    <td>{sem5[48]}</td>
                    <td>{sem5[49]}</td>
                    <td>{sem5[50]}</td>
                    <td>{sem5[51]}</td>
                </tr>
            """)
    print("</table>")

    print(f"""<br>
        <p> Total Credits : {sem5[52]}<br>
         Earned Credits : {sem5[53]}<br>
        Gpa : {sem5[54]}<br><hr>
        """)
if sem6:
    print(""" <br><br><hr><br<br>""")
    print('<h2>Semester 6</h2>')
    print("""
            <table>
                <tr>
                    <th>Subject</th>
                    <th>Code</th>
                    <th>Credit</th>
                    <th>Grade</th>
                    <th>Reappear/Passed Year</th>
                </tr>
        """)

    print(f"""
                <tr>
                    <td>{sem6[2]}</td>
                    <td>{sem6[3]}</td>
                    <td>{sem6[4]}</td>
                    <td>{sem6[5]}</td>
                    <td>{sem6[6]}</td>
                </tr>
                <tr>
                    <td>{sem6[7]}</td>
                    <td>{sem6[8]}</td>
                    <td>{sem6[9]}</td>
                    <td>{sem6[10]}</td>
                    <td>{sem6[11]}</td>
                </tr>
                <tr>
                    <td>{sem6[12]}</td>
                    <td>{sem6[13]}</td>
                    <td>{sem6[14]}</td>
                    <td>{sem6[15]}</td>
                    <td>{sem6[16]}</td>
                </tr>
                <tr>
                    <td>{sem6[17]}</td>
                    <td>{sem6[18]}</td>
                    <td>{sem6[19]}</td>
                    <td>{sem6[20]}</td>
                    <td>{sem6[21]}</td>
                </tr>
                <tr>
                    <td>{sem6[22]}</td>
                    <td>{sem6[23]}</td>
                    <td>{sem6[24]}</td>
                    <td>{sem6[25]}</td>
                    <td>{sem6[26]}</td>
                </tr>
                <tr>
                    <td>{sem6[27]}</td>
                    <td>{sem6[28]}</td>
                    <td>{sem6[29]}</td>
                    <td>{sem6[30]}</td>
                    <td>{sem6[31]}</td>
                </tr>
                <tr>
                    <td>{sem6[32]}</td>
                    <td>{sem6[33]}</td>
                    <td>{sem6[34]}</td>
                    <td>{sem6[35]}</td>
                    <td>{sem6[36]}</td>
                </tr>
                <tr>
                    <td>{sem6[37]}</td>
                    <td>{sem6[38]}</td>
                    <td>{sem6[39]}</td>
                    <td>{sem6[40]}</td>
                    <td>{sem6[41]}</td>
                </tr>
                <tr>
                    <td>{sem6[42]}</td>
                    <td>{sem6[43]}</td>
                    <td>{sem6[44]}</td>
                    <td>{sem6[45]}</td>
                    <td>{sem6[46]}</td>
                </tr>
                <tr>
                    <td>{sem6[47]}</td>
                    <td>{sem6[48]}</td>
                    <td>{sem6[49]}</td>
                    <td>{sem6[50]}</td>
                    <td>{sem6[51]}</td>
                </tr>
            """)
    print("</table>")

    print(f"""<br>
        <p> Total Credits : {sem6[52]}<br>
         Earned Credits : {sem6[53]}<br>
        Gpa : {sem6[54]}<br><hr>
        """)
if sem7:
    print(""" <br><br><hr><br<br>""")
    print('<h2>Semester 7</h2>')
    print("""
            <table>
                <tr>
                    <th>Subject</th>
                    <th>Code</th>
                    <th>Credit</th>
                    <th>Grade</th>
                    <th>Reappear/Passed Year</th>
                </tr>
        """)

    print(f"""
                <tr>
                    <td>{sem7[2]}</td>
                    <td>{sem7[3]}</td>
                    <td>{sem7[4]}</td>
                    <td>{sem7[5]}</td>
                    <td>{sem7[6]}</td>
                </tr>
                <tr>
                    <td>{sem7[7]}</td>
                    <td>{sem7[8]}</td>
                    <td>{sem7[9]}</td>
                    <td>{sem7[10]}</td>
                    <td>{sem7[11]}</td>
                </tr>
                <tr>
                    <td>{sem7[12]}</td>
                    <td>{sem7[13]}</td>
                    <td>{sem7[14]}</td>
                    <td>{sem7[15]}</td>
                    <td>{sem7[16]}</td>
                </tr>
                <tr>
                    <td>{sem7[17]}</td>
                    <td>{sem7[18]}</td>
                    <td>{sem7[19]}</td>
                    <td>{sem7[20]}</td>
                    <td>{sem7[21]}</td>
                </tr>
                <tr>
                    <td>{sem7[22]}</td>
                    <td>{sem7[23]}</td>
                    <td>{sem7[24]}</td>
                    <td>{sem7[25]}</td>
                    <td>{sem7[26]}</td>
                </tr>
                <tr>
                    <td>{sem7[27]}</td>
                    <td>{sem7[28]}</td>
                    <td>{sem7[29]}</td>
                    <td>{sem7[30]}</td>
                    <td>{sem7[31]}</td>
                </tr>
                <tr>
                    <td>{sem7[32]}</td>
                    <td>{sem7[33]}</td>
                    <td>{sem7[34]}</td>
                    <td>{sem7[35]}</td>
                    <td>{sem7[36]}</td>
                </tr>
                <tr>
                    <td>{sem7[37]}</td>
                    <td>{sem7[38]}</td>
                    <td>{sem7[39]}</td>
                    <td>{sem7[40]}</td>
                    <td>{sem7[41]}</td>
                </tr>
                <tr>
                    <td>{sem7[42]}</td>
                    <td>{sem7[43]}</td>
                    <td>{sem7[44]}</td>
                    <td>{sem7[45]}</td>
                    <td>{sem7[46]}</td>
                </tr>
                <tr>
                    <td>{sem7[47]}</td>
                    <td>{sem7[48]}</td>
                    <td>{sem7[49]}</td>
                    <td>{sem7[50]}</td>
                    <td>{sem7[51]}</td>
                </tr>
            """)
    print("</table>")

    print(f"""<br>
        <p> Total Credits : {sem7[52]}<br>
         Earned Credits : {sem7[53]}<br>
        Gpa : {sem7[54]}<br><hr>
        """)
if sem8:
    print(""" <br><br><hr><br<br>""")
    print('<h2>Semester 8</h2>')
    print("""
            <table>
                <tr>
                    <th>Subject</th>
                    <th>Code</th>
                    <th>Credit</th>
                    <th>Grade</th>
                    <th>Reappear/Passed Year</th>
                </tr>
        """)

    print(f"""
                <tr>
                    <td>{sem8[2]}</td>
                    <td>{sem8[3]}</td>
                    <td>{sem8[4]}</td>
                    <td>{sem8[5]}</td>
                    <td>{sem8[6]}</td>
                </tr>
                <tr>
                    <td>{sem8[7]}</td>
                    <td>{sem8[8]}</td>
                    <td>{sem8[9]}</td>
                    <td>{sem8[10]}</td>
                    <td>{sem8[11]}</td>
                </tr>
                <tr>
                    <td>{sem8[12]}</td>
                    <td>{sem8[13]}</td>
                    <td>{sem8[14]}</td>
                    <td>{sem8[15]}</td>
                    <td>{sem8[16]}</td>
                </tr>
                <tr>
                    <td>{sem8[17]}</td>
                    <td>{sem8[18]}</td>
                    <td>{sem8[19]}</td>
                    <td>{sem8[20]}</td>
                    <td>{sem8[21]}</td>
                </tr>
                <tr>
                    <td>{sem8[22]}</td>
                    <td>{sem8[23]}</td>
                    <td>{sem8[24]}</td>
                    <td>{sem8[25]}</td>
                    <td>{sem8[26]}</td>
                </tr>
                <tr>
                    <td>{sem8[27]}</td>
                    <td>{sem8[28]}</td>
                    <td>{sem8[29]}</td>
                    <td>{sem8[30]}</td>
                    <td>{sem8[31]}</td>
                </tr>
                <tr>
                    <td>{sem8[32]}</td>
                    <td>{sem8[33]}</td>
                    <td>{sem8[34]}</td>
                    <td>{sem8[35]}</td>
                    <td>{sem8[36]}</td>
                </tr>
                <tr>
                    <td>{sem8[37]}</td>
                    <td>{sem8[38]}</td>
                    <td>{sem8[39]}</td>
                    <td>{sem8[40]}</td>
                    <td>{sem8[41]}</td>
                </tr>
                <tr>
                    <td>{sem8[42]}</td>
                    <td>{sem8[43]}</td>
                    <td>{sem8[44]}</td>
                    <td>{sem8[45]}</td>
                    <td>{sem8[46]}</td>
                </tr>
                <tr>
                    <td>{sem8[47]}</td>
                    <td>{sem8[48]}</td>
                    <td>{sem8[49]}</td>
                    <td>{sem8[50]}</td>
                    <td>{sem8[51]}</td>
                </tr>
            """)
    print("</table>")

    print(f"""<br>
        <p> Total Credits : {sem8[52]}<br>
         Earned Credits : {sem8[53]}<br>
        Gpa : {sem8[54]}<br><hr>
        """)


print("""
        </div>
    </div>
    <footer>
        <p><a href="https://www.instagram.com/yourdepartmentpage">
            <img src="images/instgram.jpeg" alt="instagram" width="30px" height="30px"></a>Follow on Instagram</p>
        <p>&copy; 2024 Information Technology. All rights reserved.</p>
    </footer>
</body>
</html>
""")

# Close database connection
cur.close()
con.close()
