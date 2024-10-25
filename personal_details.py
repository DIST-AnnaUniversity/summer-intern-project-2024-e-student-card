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
        <tr><th>Mother Name:</th><td>{personal_details[20]}</td></tr>
        <tr><th>Mother Occupation:</th><td>{personal_details[21]}</td></tr>
        <tr><th>Mother Income:</th><td>{personal_details[22]}</td></tr>
        <tr><th>Address:</th><td>{personal_details[23]}</td></tr>
        <tr><th>Guardian Address:</th><td>{personal_details[24]}</td></tr>
        <tr><th>Guardian Phone No:</th><td>{personal_details[25]}</td></tr>
        <tr><th>Guardian Email ID:</th><td>{personal_details[26]}</td></tr>
    </table>
    """)


if not personal_details:
        print("<p>No personal details found for the given registration number.</p>")

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
