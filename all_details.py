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

print()

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IST STUDENT RECORD</title>
    <link rel="icon" href="images/ist.png">
    <link rel="stylesheet" href="fetching.css" type="text/css">
    <script src="all_details.js"></script>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
            font-size: 16px;
        }

        th, td {
            text-align: left;
            padding: 12px;
            border: 1px solid #ddd;
        }

        th {
            background-color: #f2f2f2;
            color: #333;
        }

        td {
            background-color: #fff;
            color: #555;
        }

        table img {
            border-radius: 10px;
            width: 180px;
            height: auto;
            margin-bottom: 10px;
        }

        @media screen and (max-width: 768px) {
            table, th, td {
                display: block;
                width: 100%;
            }

            td {
                padding: 8px;
            }

            th {
                text-align: center;
            }
        }

        /* Button Styling */
        #prevButton, #nextButton {
            background-color: red; 
            color: white; 
            border: none;
            padding: 12px 24px;
            font-size: 18px; 
            cursor: pointer;
            margin: 20px; /* Added margin */
            border-radius: 8px;
            display: inline-block;
            text-align: center;
            transition: background-color 0.3s;
        }

        #prevButton:hover, #nextButton:hover {
            background-color: darkred;
            font-weight: bold;
        }

        .button-container {
            display: flex;
            justify-content: center; /* Center the buttons */
            align-items: center;
            padding: 10px;
        }

        .button-container #prevButton {
            margin-right: 10px; /* Space between buttons */
        }

        /* Additional Button for unlocking or freezing */
        #unlockButton, #freezebutton {
            background-color: red;
            border: none;
            color: white;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 10px 4px;
            cursor: pointer;
            border-radius: 5px;
            transition: background-color 0.3s;
        }

        #unlockButton:hover, #freezebutton:hover {
            background-color: darkred;
            font-weight: bolder;
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

        #sep:hover {
            background-color: rgb(24, 24, 57);
        }

        .navbar a:hover {
            background-color: red;
        }
    </style>
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
        <a href="home.py">Home</a><a id="sep">--></a>
        <a href="staff_main.py?id={Staffid}">Dashboard</a><a id="sep">--></a>
        <a href="#">{Regno}</a>
    </nav>
""")

# Logic to fetch previous and next register numbers
prev_id_query = "SELECT register_no FROM batch_details WHERE register_no < '%s' AND staffid='%s' ORDER BY register_no DESC LIMIT 1" % (Regno, Staffid)
next_id_query = "SELECT register_no FROM batch_details WHERE register_no > '%s' AND staffid='%s' ORDER BY register_no ASC LIMIT 1" % (Regno, Staffid)

cur.execute(prev_id_query)
prev_record = cur.fetchone()

cur.execute(next_id_query)
next_record = cur.fetchone()

prev_regno = prev_record[0] if prev_record else None
next_regno = next_record[0] if next_record else None

# Display the buttons for navigation
print(f"""
    <div class="button-container">
        <button id="prevButton" onclick="window.location.href='all_details.py?id={prev_regno}&staffid={Staffid}'" {'disabled' if not prev_regno else ''}>
            &#8592; Previous
        </button>
        <button id="nextButton" onclick="window.location.href='all_details.py?id={next_regno}&staffid={Staffid}'" {'disabled' if not next_regno else ''}>
            Next &#8594;
        </button>
    </div>

    <div class="wrapper"> 
        <div class="content">
        <form method="post">
""")

# Continue with the rest of your form and content logic...


# form=cgi.FieldStorage()
# Regno=form.getvalue("id");
# Staffid=form.getvalue("staffid")
#
#
#
# # HTML structure
# print("""
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>IST STUDENT RECORD</title>
#     <link rel="icon" href="images/ist.png">
#     <link rel="stylesheet" href="fetching.css" type="text/css">
#     <script src="all_details.js"></script>
#     <style>
#
#     table {
#     width: 100%;
#     border-collapse: collapse;
#     margin-bottom: 20px;
#     font-size: 16px;
# }
#
# th, td {
#     text-align: left;
#     padding: 12px;
#     border: 1px solid #ddd;
# }
#
# th {
#     background-color: #f2f2f2;
#     color: #333;
# }
#
# td {
#     background-color: #fff;
#     color: #555;
# }
#
# table img {
#     border-radius: 10px;
#     width: 180px;
#     height: auto;
#     margin-bottom: 10px;
# }
#
# @media screen and (max-width: 768px) {
#     table, th, td {
#         display: block;
#         width: 100%;
#     }
#
#     td {
#         padding: 8px;
#     }
#
#     th {
#         text-align: center;
#     }
# }
#
#
#     #unlockButton,#freezebutton{
#     background-color: red;
#     border: none;
#     color: white;
#     padding: 10px 20px;
#     text-align: center;
#     text-decoration: none;
#     display: inline-block;
#     font-size: 16px;
#     margin: 10px 4px;
#     cursor: pointer;
#     border-radius: 5px;
#     transition: background-color 0.3s;
# }
#
# #unlockButton:hover ,#freezebutton:hover{
#     background-color:red;
#     font-weight:bolder;
# }
#
# .navbar {
#     background-color: rgb(24, 24, 57);
#     overflow: hidden;
#     text-align: left;
# }
#
# .navbar a {
#     display: inline-block;
#     color: white;
#     padding: 14px 20px;
#     text-decoration: none;
#     font-size: 1.2rem;
# }
# #sep:hover{
#     background-color:rgb(24, 24, 57);
# }
# .navbar a:hover {
#     background-color: red;
# }
#     </style>
# </head>
# """)
# print(f"""
# <body>
#     <header>
#         <section class="header">
#             <div>
#                 <img class="ceg" src="images/ceg.png" alt="au_logo" width="200px" height="150px">
#             </div>
#             <div>
#                 <h1>DEPARTMENT OF INFORMATION SCIENCE AND TECHNOLOGY</h1>
#             </div>
#             <div>
#                 <img class="ist" src="images/ist.png" alt="ist_logo" width="200px" height="150px">
#             </div>
#         </section>
#     </header>
#     <nav class="navbar">
#         <a href="home.py">Home</a><a id="sep" >--></a>
#         <a href="staff_main.py?id={Staffid}">Dashboard</a><a id="sep" >--></a>
#         <a href="">{Regno}  </a>
#     </nav>
#
#     <div class="wrapper">
#
#         <div class="content">
#         <form method="post">
#
# """)

# Fetch personal details from the database
q = """SELECT * FROM student_details WHERE register_no='%s'""" % (Regno)
cur.execute(q)
personal_details = cur.fetchone()

q = """SELECT * FROM scholarship_details WHERE register_no='%s'""" % (Regno)
cur.execute(q)
scholarship = cur.fetchone()

# Fetch academic details from the database
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

q = """SELECT * FROM project_details WHERE register_no='%s'""" % (Regno)
cur.execute(q)
project = cur.fetchone()

q = """SELECT * FROM placement_details WHERE register_no='%s'""" % (Regno)
cur.execute(q)
placement = cur.fetchone()

q = """SELECT * FROM exam_details WHERE register_no='%s'""" % (Regno)
cur.execute(q)
exam = cur.fetchone()

q = """SELECT * FROM higher_studies_details WHERE register_no='%s'""" % (Regno)
cur.execute(q)
higherstudies = cur.fetchone()

q = """SELECT * FROM paper_published_details WHERE register_no='%s'""" % (Regno)
cur.execute(q)
paper = cur.fetchone()

q = """SELECT * FROM events_details WHERE register_no='%s'""" % (Regno)
cur.execute(q)
event = cur.fetchone()

if personal_details:
    print('<h2>Personal Details</h2>')
    print(f"""
    <table>
        <tr><td colspan="2" style="text-align: center;"><img src="photos/{personal_details[1]}" alt="Welcome Image"></td></tr>
        <tr><th>Name:</th><td>{personal_details[2]}</td></tr>
        <tr><th>Register No:</th><td>{personal_details[3]}</td></tr>
        <tr><th>DOB:</th><td>{personal_details[4]}</td></tr>
        <tr><th>Sex:</th><td>{personal_details[5]}</td></tr>
        <tr><th>Blood Group:</th><td>{personal_details[6]}</td></tr>
        <tr><th>Community:</th><td>{personal_details[7]}</td></tr>
        <tr><th>Cutoff:</th><td>{personal_details[8]}</td></tr>
        <tr><th>Admitted On:</th><td>{personal_details[9]}</td></tr>
        <tr><th>Special Category:</th><td>{personal_details[10]}</td></tr>
        <tr><th>Scholarship:</th><td>{personal_details[11]}</td></tr>
        <tr><th>Volunteer:</th><td>{personal_details[12]}</td></tr>
        <tr><th>Hosteller/Day Scholar:</th><td>{personal_details[13]}</td></tr>
        <tr><th>Phone No:</th><td>{personal_details[14]}</td></tr>
        <tr><th>Email ID:</th><td>{personal_details[15]}</td></tr>
        <tr><th>Faculty Name:</th><td>{personal_details[16]}</td></tr>
        <tr><th>Father Name:</th><td>{personal_details[17]}</td></tr>
        <tr><th>Father Occupation:</th><td>{personal_details[18]}</td></tr>
        <tr><th>Father Income:</th><td>{personal_details[19]}</td></tr>
        <tr><th>Father Phone no:</th><td>{personal_details[20]}</td></tr>
        <tr><th>Mother Name:</th><td>{personal_details[21]}</td></tr>
        <tr><th>Mother Occupation:</th><td>{personal_details[22]}</td></tr>
        <tr><th>Mother Income:</th><td>{personal_details[23]}</td></tr>
        <tr><th>Mother Phone no:</th><td>{personal_details[24]}</td></tr>
        <tr><th>Current Address:</th><td>{personal_details[25]}</td></tr>
        <tr><th>Permanent Address:</th><td>{personal_details[26]}</td></tr>
        <tr><th>Guardian Address:</th><td>{personal_details[27]}</td></tr>
        <tr><th>Guardian Phone No:</th><td>{personal_details[28]}</td></tr>
        <tr><th>Guardian Email ID:</th><td>{personal_details[29]}</td></tr>
    </table>
    """)

if scholarship:
    print(""" <br><br><hr><br<br>""")
    print('<h2>Scholarship Details <br><br> </h2>')
    print("""
                   <table>
                       <tr>
                           <th>Year</th>
                           <th>Name</th>
                           <th>Amount Received</th>
                       </tr>
               """)

    print(f"""
                       <tr>
                           <td>{scholarship[2]}</td>
                           <td>{scholarship[3]}</td>
                           <td>{scholarship[4]}</td>
                       </tr>
                       <tr>
                           <td>{scholarship[5]}</td>
                           <td>{scholarship[6]}</td>
                           <td>{scholarship[7]}</td>
                       </tr>
                       <tr>
                           <td>{scholarship[8]}</td>
                           <td>{scholarship[9]}</td>
                           <td>{scholarship[10]}</td>
                       </tr>
                       <tr>
                           <td>{scholarship[11]}</td>
                           <td>{scholarship[12]}</td>
                           <td>{scholarship[13]}</td>
                       </tr>

                   """)
    print("</table>")

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
    if(sem1[56]=="LOCK"):
        but="Click To UNLOCK"
        val="LOCK"
    else:
        val="UNLOCK"
        but="UNLOCKED"

    if (sem1[57] == "NO"):
        but2 = "Click To AUTHORIZE"
        val2 = "NO"
    else:
        val2 = "YES"
        but2 = "AUTHORIZED"

    print(f"""<br>
       <p> Total Credits : {sem1[52]}<br>
        Earned Credits : {sem1[53]}<br>
       Gpa : {sem1[54]}<br><hr>
       <embed src="{sem1[55]}" type="application/pdf" width="100%" height="600px" />
       <button id="unlockButton" value="{val}" name="sem1" type="submit">{but}</button>
       <button id="freezebutton" value="{val2}" name="sem1_f" type="submit">{but2}</button>
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
    if (sem2[56] == "LOCK"):
        but = "Click To UNLOCK"
        val = "LOCK"
    else:
        val = "UNLOCK"
        but = "UNLOCKED"

    if (sem2[57] == "NO"):
        but2 = "Click To AUTHORIZE"
        val2 = "NO"
    else:
        val2 = "YES"
        but2 = "AUTHORIZED"

    print(f"""<br>
       <p> Total Credits : {sem2[52]}<br>
        Earned Credits : {sem2[53]}<br>
       Gpa : {sem2[54]}<br><hr>
       <embed src="{sem2[55]}" type="application/pdf" width="100%" height="600px" />
        <button id="unlockButton" value="{val}" name="sem2" type="submit">{but}</button>
        <button id="freezebutton" value="{val2}" name="sem2_f" type="submit">{but2}</button>
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

    if (sem3[56] == "LOCK"):
        but = "Click To UNLOCK"
        val = "LOCK"
    else:
        val = "UNLOCK"
        but = "UNLOCKED"

    if (sem3[57] == "NO"):
        but2 = "Click To AUTHORIZE"
        val2 = "NO"
    else:
        val2 = "YES"
        but2 = "AUTHORIZED"

    print(f"""<br>
       <p> Total Credits : {sem3[52]}<br>
        Earned Credits : {sem3[53]}<br>
       Gpa : {sem3[54]}<br><hr>
       <embed src="{sem3[55]}" type="application/pdf" width="100%" height="600px" />
        <button id="unlockButton" value="{val}" name="sem3" type="submit">{but}</button>
        <button id="freezebutton" value="{val2}" name="sem3_f" type="submit">{but2}</button>
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
    if (sem4[56] == "LOCK"):
        but = "Click To UNLOCK"
        val = "LOCK"
    else:
        val = "UNLOCK"
        but = "UNLOCKED"

    if (sem4[57] == "NO"):
        but2 = "Click To AUTHORIZE"
        val2 = "NO"
    else:
        val2 = "YES"
        but2 = "AUTHORIZED"

    print(f"""<br>
       <p> Total Credits : {sem4[52]}<br>
        Earned Credits : {sem4[53]}<br>
       Gpa : {sem4[54]}<br><hr>
       <embed src="{sem4[55]}" type="application/pdf" width="100%" height="600px" />
        <button id="unlockButton" value="{val}" name="sem4" type="submit">{but}</button>
        <button id="freezebutton" value="{val2}" name="sem4_f" type="submit">{but2}</button>
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
    if (sem5[56] == "LOCK"):
        but = "Click To UNLOCK"
        val = "LOCK"
    else:
        val = "UNLOCK"
        but = "UNLOCKED"

    if (sem5[57] == "NO"):
        but2 = "Click To AUTHORIZE"
        val2 = "NO"
    else:
        val2 = "YES"
        but2 = "AUTHORIZED"

    print(f"""<br>
       <p> Total Credits : {sem5[52]}<br>
        Earned Credits : {sem5[53]}<br>
       Gpa : {sem5[54]}<br><hr>
       <embed src="{sem5[55]}" type="application/pdf" width="100%" height="600px" />
        <button id="unlockButton" value="{val}" name="sem5" type="submit">{but}</button>
        <button id="freezebutton" value="{val2}" name="sem5_f" type="submit">{but2}</button>
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

    if (sem6[56] == "LOCK"):
        but = "Click To UNLOCK"
        val = "LOCK"
    else:
        val = "UNLOCK"
        but = "UNLOCKED"

    if (sem6[57] == "NO"):
        but2 = "Click To AUTHORIZE"
        val2 = "NO"
    else:
        val2 = "YES"
        but2 = "AUTHORIZED"

    print(f"""<br>
       <p> Total Credits : {sem6[52]}<br>
        Earned Credits : {sem6[53]}<br>
       Gpa : {sem6[54]}<br><hr>
       <embed src="{sem6[55]}" type="application/pdf" width="100%" height="600px" />
        <button id="unlockButton" value="{val}" name="sem6" type="submit">{but}</button>
        <button id="freezebutton" value="{val2}" name="sem6_f" type="submit">{but2}</button>
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

    if (sem7[56] == "LOCK"):
        but = "Click To UNLOCK"
        val = "LOCK"
    else:
        val = "UNLOCK"
        but = "UNLOCKED"

    if (sem7[57] == "NO"):
        but2 = "Click To AUTHORIZE"
        val2 = "NO"
    else:
        val2 = "YES"
        but2 = "AUTHORIZED"

    print(f"""<br>
       <p> Total Credits : {sem7[52]}<br>
        Earned Credits : {sem7[53]}<br>
       Gpa : {sem7[54]}<br><hr>
       <embed src="{sem7[55]}" type="application/pdf" width="100%" height="600px" />
        <button id="unlockButton" value="{val}" name="sem7" type="submit">{but}</button>
        <button id="freezebutton" value="{val2}" name="sem7_f" type="submit">{but2}</button>
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
    if (sem8[56] == "LOCK"):
        but = "Click To UNLOCK"
        val="LOCK"
    else:
        val="UNLOCK"
        but = "UNLOCKED"

    if (sem8[57] == "NO"):
        but2 = "Click To AUTHORIZE"
        val2 = "NO"
    else:
        val2 = "YES"
        but2 = "AUTHORIZED"

    print(f"""<br>
       <p> Total Credits : {sem8[52]}<br>
        Earned Credits : {sem8[53]}<br>
       Gpa : {sem8[54]}<br><hr>
       <embed src="{sem8[55]}" type="application/pdf" width="100%" height="600px" />
       <button id="unlockButton" value="{val}" name="sem8" type="submit">{but}</button>
       <button id="freezebutton" value="{val2}" name="sem8_f" type="submit">{but2}</button>
       """)

if project:
    print(f"""
       <h2> Project Details : </h2>
       <h3>PROJECT 1</h3>
       <p> <span style = "color:red"> Title : </span> {project[2]} </p>
       <p> <span style = "color:red"> Guide : </span> {project[3]} </p>
       <h3>PROJECT 2</h3>
       <p> <span style = "color:red"> Title : </span> {project[4]} </p>
       <p> <span style = "color:red"> Guide : </span> {project[5]} </p>
       <p> <span style = "color:red"> Other Projects : </span> {project[6]} </p><br><hr>
       """)

if placement:
    print(f"""
               <h2> Placement Details : </h2>
               <p> <span style = "color:red"> Company Name : </span> {placement[2]} </p>
               <p> <span style = "color:red"> Selection Type : </span> {placement[3]} </p>
               <p> <span style = "color:red"> Salary Package : </span> {placement[4]} </p>
               <p> <span style = "color:red"> Job Type: </span> {placement[5]} </p><br><hr>
               """)

if exam:
    print(f"""
                       <h2> National/International Exam Details : </h2>
                       <p> <span style = "color:red"> Exam Name : </span> {exam[2]} </p>
                       <h3>Certified Courses :</h3>
                       <p> <span style = "color:red"> Course Name : </span> {exam[3]} </p>
                       <p> <span style = "color:red"> Completion Date : </span> {exam[4]} </p><br><hr>
                       """)
if higherstudies:
    print(f"""
                               <h2> Higher Education Details : </h2>
                               <p> <span style = "color:red"> No.of Universities applied : </span> {higherstudies[2]} </p>
                               <p> <span style = "color:red"> University Admitted : </span> {higherstudies[3]} </p>
                               <p> <span style = "color:red"> Year of Admission : </span> {higherstudies[4]} </p>
                               <p> <span style = "color:red"> Specialization : </span> {higherstudies[5]} </p><br><hr>
                               """)

if paper:
    print('<h2>Paper Published Details</h2>')
    print("No.of Paper Published in SCI-E/SCI/Scopus/WOS indexed Journals")
    print("""
                  <table>
                      <tr>
                          <th>Authors</th>
                          <th>Title</th>
                          <th>Journal Name</th>
                          <th>Month Year</th>
                          <th>DOI Link</th>
                          <th>Indexed in SCI-E/SCI scopus</th>
                      </tr>
              """)

    print(f"""
                      <tr>
                          <td>{paper[2]}</td>
                          <td>{paper[3]}</td>
                          <td>{paper[4]}</td>
                          <td>{paper[5]}</td>
                          <td>{paper[6]}</td>
                          <td>{paper[7]}</td>
                      </tr>
                      <tr>
                          <td>{paper[8]}</td>
                          <td>{paper[9]}</td>
                          <td>{paper[10]}</td>
                          <td>{paper[11]}</td>
                          <td>{paper[12]}</td>
                          <td>{paper[13]}</td>
                      </tr>
                      <tr>
                          <td>{paper[14]}</td>
                          <td>{paper[15]}</td>
                          <td>{paper[16]}</td>
                          <td>{paper[17]}</td>
                          <td>{paper[18]}</td>
                          <td>{paper[19]}</td>
                      </tr>

                  """)
    print("</table>")
    print("No.of Paper Published in National/International Conference/Workshop/Symposium")
    print("""
                          <table>
                              <tr>
                                  <th>Authors</th>
                                  <th>Title</th>
                                  <th>Journal Name</th>
                                  <th>Month Year</th>
                                  <th>DOI Link</th>
                                  <th>Indexed in SCI-E/SCI scopus</th>
                              </tr>
                      """)

    print(f"""
                              <tr>
                                  <td>{paper[20]}</td>
                                  <td>{paper[21]}</td>
                                  <td>{paper[22]}</td>
                                  <td>{paper[23]}</td>
                                  <td>{paper[24]}</td>
                                  <td>{paper[25]}</td>
                              </tr>
                              <tr>
                                  <td>{paper[26]}</td>
                                  <td>{paper[27]}</td>
                                  <td>{paper[28]}</td>
                                  <td>{paper[29]}</td>
                                  <td>{paper[30]}</td>
                                  <td>{paper[31]}</td>
                              </tr>
                              <tr>
                                  <td>{paper[32]}</td>
                                  <td>{paper[33]}</td>
                                  <td>{paper[34]}</td>
                                  <td>{paper[35]}</td>
                                  <td>{paper[36]}</td>
                                  <td>{paper[37]}</td>
                              </tr>

                          """)
    print("</table><br><hr>")

if event:
    print(f"""
                                      <h2> Technical Events Organized/Participateed/Presented : </h2>
                                      <p> <span style = "color:red"> Name Of the Event : </span> {event[2]} </p>
                                      <p> <span style = "color:red"> Institution Organized : </span> {event[3]} </p>
                                      <p> <span style = "color:red"> College/University/State/National/International : </span> {event[4]} </p>
                                      <p> <span style = "color:red"> Role : </span> {event[5]} </p>
                                      <p> <span style = "color:red"> Date/Duration : </span> {event[6]} </p>
                                      <p> <span style = "color:red"> Awards If Any : </span> {event[7]} </p><br><hr>
                                      """)

# if not personal_details:
#     print("<p>No personal details found for the given registration number.</p>")
# if not sem1:
#     print("<p>No SEMESTER 1 academic details found for the given registration number.</p>")
# if not sem2:
#     print("<p>No SEMESTER 2 academic details found for the given registration number.</p>")
# if not sem3:
#     print("<p>No SEMESTER 3 academic details found for the given registration number.</p>")
# if not sem4:
#     print("<p>No SEMESTER 4 academic details found for the given registration number.</p>")
# if not sem5:
#     print("<p>No SEMESTER 5 academic details found for the given registration number.</p>")
# if not sem6:
#     print("<p>No SEMESTER 6 academic details found for the given registration number.</p>")
# if not sem7:
#     print("<p>No SEMESTER 7 academic details found for the given registration number.</p>")
# if not sem8:
#     print("<p>No SEMESTER 8 academic details found for the given registration number.</p>")




print("""
        </div>
        <div class="button-container">
        <button id="prevButton" onclick="window.location.href='student_record.py?id={prev_regno}&staffid={Staffid}'" {'disabled' if not prev_regno else ''}>
            &#8592; Previous
        </button>
        <button id="nextButton" onclick="window.location.href='student_record.py?id={next_regno}&staffid={Staffid}'" {'disabled' if not next_regno else ''}>
            Next &#8594;
        </button>
    </div>
        </form>
    </div>
    <footer>
        <p><a href="https://www.instagram.com/yourdepartmentpage">
            <img src="images/instgram.jpeg" alt="instagram" width="30px" height="30px"></a>Follow on Instagram</p>
        <p>&copy; 2024 Information Technology. All rights reserved.</p>
    </footer>
</body>
</html>
""")


sem1_button=form.getvalue("sem1")
sem2_button=form.getvalue("sem2")
sem3_button=form.getvalue("sem3")
sem4_button=form.getvalue("sem4")
sem5_button=form.getvalue("sem5")
sem6_button=form.getvalue("sem6")
sem7_button=form.getvalue("sem7")
sem8_button=form.getvalue("sem8")

if sem1_button == "LOCK" :
    q="""UPDATE sem1 SET status='%s' WHERE register_no='%s'"""%("UNLOCK",Regno)
    cur.execute(q)
    con.commit()
    print(f"""
    <script>
    changeButtonContent();
    alert("Unlocked Successfully!");
    location.href='all_details.py?id={Regno}';
    </script>
    """)
if sem2_button == "LOCK" :
    q="""UPDATE sem2 SET status='%s' WHERE register_no='%s'"""%("UNLOCK",Regno)
    cur.execute(q)
    con.commit()
    print(f"""
    <script>
    changeButtonContent();
    alert("Unlocked Successfully!");
    location.href='all_details.py?id={Regno}';
    </script>
    """)

if sem3_button == "LOCK" :
    q="""UPDATE sem3 SET status='%s' WHERE register_no='%s'"""%("UNLOCK",Regno)
    cur.execute(q)
    con.commit()
    print(f"""
    <script>
    changeButtonContent();
    alert("Unlocked Successfully!");
    location.href='all_details.py?id={Regno}';
    </script>
    """)
if sem4_button == "LOCK" :
    q="""UPDATE sem4 SET status='%s' WHERE register_no='%s'"""%("UNLOCK",Regno)
    cur.execute(q)
    con.commit()
    print(f"""
    <script>
    changeButtonContent();
    alert("Unlocked Successfully!");
    location.href='all_details.py?id={Regno}';
    </script>
    """)
if sem5_button == "LOCK" :
    q="""UPDATE sem5 SET status='%s' WHERE register_no='%s'"""%("UNLOCK",Regno)
    cur.execute(q)
    con.commit()
    print(f"""
    <script>
    changeButtonContent();
    alert("Unlocked Successfully!");
    location.href='all_details.py?id={Regno}';
    </script>
    """)
if sem6_button == "LOCK" :
    q="""UPDATE sem6 SET status='%s' WHERE register_no='%s'"""%("UNLOCK",Regno)
    cur.execute(q)
    con.commit()
    print(f"""
    <script>
    changeButtonContent();
    alert("Unlocked Successfully!");
    location.href='all_details.py?id={Regno}';
    </script>
    """)
if sem7_button == "LOCK" :
    q="""UPDATE sem7 SET status='%s' WHERE register_no='%s'"""%("UNLOCK",Regno)
    cur.execute(q)
    con.commit()
    print(f"""
    <script>
    changeButtonContent();
    alert("Unlocked Successfully!");
    location.href='all_details.py?id={Regno}';
    </script>
    """)
if sem8_button == "LOCK" :
    q="""UPDATE sem8 SET status='%s' WHERE register_no='%s'"""%("UNLOCK",Regno)
    cur.execute(q)
    con.commit()
    print(f"""
    <script>
    changeButtonContent();
    alert("Unlocked Successfully!");
    location.href='all_details.py?id={Regno}&staffid={Staffid}';
    </script>
    """)

sem1_fbutton=form.getvalue("sem1_f")
sem2_fbutton=form.getvalue("sem2_f")
sem3_fbutton=form.getvalue("sem3_f")
sem4_fbutton=form.getvalue("sem4_f")
sem5_fbutton=form.getvalue("sem5_f")
sem6_fbutton=form.getvalue("sem6_f")
sem7_fbutton=form.getvalue("sem7_f")
sem8_fbutton=form.getvalue("sem8_f")

if sem1_fbutton == "NO" :
    q="""UPDATE sem1 SET authorized='%s' WHERE register_no='%s'"""%("YES",Regno)
    cur.execute(q)
    con.commit()
    print(f"""
   <script>
        if (confirm('Are you sure you want to AUTHORIZE SEMESTER 1 RESULT?')) {{
            alert("Authorized Successfully!");
            document.getElementById('freezebutton').innerText = 'AUTHORIZED';
            document.getElementById('freezebutton').style.backgroundColor = 'green';
            setTimeout(function() {{
                location.href = 'all_details.py?id={Regno}';
            }}, 1000);  // Delay redirect for 1 second
        }} else {{
            alert("Authorization Cancelled.");
        }}
    </script>
    """)

if sem2_fbutton == "NO" :
    q="""UPDATE sem2 SET authorized='%s' WHERE register_no='%s'"""%("YES",Regno)
    cur.execute(q)
    con.commit()
    print(f"""
    <script>
        if (confirm('Are you sure you want to AUTHORIZE SEMESTER 2 RESULT?')) {{
            alert("Authorized Successfully!");
            document.getElementById('freezebutton').innerText = 'AUTHORIZED';
            document.getElementById('freezebutton').style.backgroundColor = 'green';
            setTimeout(function() {{
                location.href = 'all_details.py?id={Regno}';
            }}, 1000);  // Delay redirect for 1 second
        }} else {{
            alert("Authorization Cancelled.");
        }}
    </script>
    """)

if sem3_fbutton == "NO" :
    q="""UPDATE sem3 SET authorized='%s' WHERE register_no='%s'"""%("YES",Regno)
    cur.execute(q)
    con.commit()
    print(f"""
    <script>
        if (confirm('Are you sure you want to AUTHORIZE SEMESTER 3 RESULT?')) {{
            alert("Authorized Successfully!");
            document.getElementById('freezebutton').innerText = 'AUTHORIZED';
            document.getElementById('freezebutton').style.backgroundColor = 'green';
            setTimeout(function() {{
                location.href = 'all_details.py?id={Regno}';
            }}, 1000);  // Delay redirect for 1 second
        }} else {{
            alert("Authorization Cancelled.");
        }}
    </script>
    """)

if sem4_fbutton == "NO" :
    q="""UPDATE sem4 SET authorized='%s' WHERE register_no='%s'"""%("YES",Regno)
    cur.execute(q)
    con.commit()
    print(f"""
    <script>
        if (confirm('Are you sure you want to AUTHORIZE SEMESTER 4 RESULT?')) {{
            alert("Authorized Successfully!");
            document.getElementById('freezebutton').innerText = 'AUTHORIZED';
            document.getElementById('freezebutton').style.backgroundColor = 'green';
            setTimeout(function() {{
                location.href = 'all_details.py?id={Regno}';
            }}, 1000);  // Delay redirect for 1 second
        }} else {{
            alert("Authorization Cancelled.");
        }}
    </script>
    """)

if sem5_fbutton == "NO" :
    q="""UPDATE sem5 SET authorized='%s' WHERE register_no='%s'"""%("YES",Regno)
    cur.execute(q)
    con.commit()
    print(f"""
   <script>
        if (confirm('Are you sure you want to AUTHORIZE SEMESTER 5 RESULT?')) {{
            alert("Authorized Successfully!");
            document.getElementById('freezebutton').innerText = 'AUTHORIZED';
            document.getElementById('freezebutton').style.backgroundColor = 'green';
            setTimeout(function() {{
                location.href = 'all_details.py?id={Regno}';
            }}, 1000);  // Delay redirect for 1 second
        }} else {{
            alert("Authorization Cancelled.");
        }}
    </script>
    """)

if sem6_fbutton == "NO" :
    q="""UPDATE sem6 SET authorized='%s' WHERE register_no='%s'"""%("YES",Regno)
    cur.execute(q)
    con.commit()
    print(f"""
    <script>
        if (confirm('Are you sure you want to AUTHORIZE SEMESTER 6 RESULT?')) {{
            alert("Authorized Successfully!");
            document.getElementById('freezebutton').innerText = 'AUTHORIZED';
            document.getElementById('freezebutton').style.backgroundColor = 'green';
            setTimeout(function() {{
                location.href = 'all_details.py?id={Regno}';
            }}, 1000);  // Delay redirect for 1 second
        }} else {{
            alert("Authorization Cancelled.");
        }}
    </script>
    """)

if sem7_fbutton == "NO" :
    q="""UPDATE sem7 SET authorized='%s' WHERE register_no='%s'"""%("YES",Regno)
    cur.execute(q)
    con.commit()
    print(f"""
    <script>
        if (confirm('Are you sure you want to AUTHORIZE SEMESTER 7 RESULT?')) {{
            alert("Authorized Successfully!");
            document.getElementById('freezebutton').innerText = 'AUTHORIZED';
            document.getElementById('freezebutton').style.backgroundColor = 'green';
            setTimeout(function() {{
                location.href = 'all_details.py?id={Regno}';
            }}, 1000);  // Delay redirect for 1 second
        }} else {{
            alert("Authorization Cancelled.");
        }}
    </script>
    """)

if sem8_fbutton == "NO" :
    q="""UPDATE sem8 SET authorized='%s' WHERE register_no='%s'"""%("YES",Regno)
    cur.execute(q)
    con.commit()
    print(f"""
    <script>
        if (confirm('Are you sure you want to AUTHORIZE SEMESTER 8 RESULT?')) {{
            alert("Authorized Successfully!");
            document.getElementById('freezebutton').innerText = 'AUTHORIZED';
            document.getElementById('freezebutton').style.backgroundColor = 'green';
            setTimeout(function() {{
                location.href = 'all_details.py?id={Regno}';
            }}, 1000);  // Delay redirect for 1 second
        }} else {{
            alert("Authorization Cancelled.");
        }}
    </script>
    """)

# Close database connection
cur.close()
con.close()
