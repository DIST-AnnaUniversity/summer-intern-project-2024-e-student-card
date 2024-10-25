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
            </div>
""")


q = """SELECT * FROM student_details WHERE register_no='%s'""" % (Regno)
cur.execute(q)
personal_details = cur.fetchone()

q = """SELECT * FROM scholarship_details WHERE register_no='%s'""" % (Regno)
cur.execute(q)
scholarship= cur.fetchone()


if personal_details:
    print(f"""
             <img src="photos/{personal_details[1]}" alt="Welcome Image" style="width: 180px;height: auto; border-radius: 10px;margin-bottom: 10px">
            <p ><span style="color:red">Name:</span> {personal_details[2]}</p>
            <p ><span style="color:red">Register No:</span> {personal_details[3]}</p>
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
