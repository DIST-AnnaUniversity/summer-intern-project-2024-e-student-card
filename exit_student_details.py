#!C:/Python/python.exe
import pymysql
import cgitb
import cgi

print("Content-type: text/html\r\n\r\n")
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="summer_project")
cur = con.cursor()

form = cgi.FieldStorage()
Regno = form.getvalue("id")
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

print('<h1 style="text-align:center"> Exit Student Details</h1>')

if personal_details:
    print('<h2>Personal Details</h2>')
    print(f"""
             <img src="photos/{personal_details[1]}" alt="Welcome Image" style="width: 180px;height: auto; border-radius: 10px;margin-bottom: 10px">
            <p ><span style="color:red">Name:</span> {personal_details[2]}</p>
            <p ><span style="color:red">Register No:</span> {personal_details[3]}</p><br><hr>
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
