#!C:/Python/python.exe
import pymysql, cgitb, cgi, os

print("Content-type: text/html\r\n\r\n")
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="summer_project")
cur = con.cursor()

form = cgi.FieldStorage()
Staffid = form.getvalue("id")

# Fetch staff details
q = """SELECT * FROM staff_details WHERE staffid='%s'""" % (Staffid)
cur.execute(q)
res = cur.fetchone()

Name = res[2]
Phoneno = res[3]
EmailId = res[4]

# Fetch staff photo
q = """SELECT photo FROM staff_details WHERE staffid='%s'""" % (Staffid)
cur.execute(q)
res = cur.fetchone()

if res:
    Photo = res[0]
else:
    Photo = "image_dummy.jpeg"

# Fetch batch details
q = """SELECT DISTINCT batch FROM batch_details WHERE staffid='%s'""" % (Staffid)
cur.execute(q)
batches = cur.fetchall()

# Fetch students in selected batch
Batch = form.getvalue("batch")
students = []
if Batch:
    q = """SELECT register_no, name FROM batch_details WHERE batch='%s' AND staffid='%s'""" % (Batch, Staffid)
    cur.execute(q)
    students = cur.fetchall()

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
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            background-color: #f9f9f9;
        }

        .header {
            background-color: rgb(36, 36, 87);
            color: white;
            display: flex;
            align-items: center;
            padding: 5px 10px; /* Reduced padding to decrease height */
            width: 100%;
        }

        .header img {
            width: 5vw; /* Reduced width for the images in the header */
            height: auto;
            margin: 0 5vw; /* Adjusted margins */
        }

        .header h2 {
            flex: 1;
            text-align: center;
        }

        .main {
            display: flex;
            flex-direction: row;
        }

        .sidebar {
            width: 20%; /* Reduced width of the sidebar */
            height:auto;
            color: black;
            padding: 20px;
            text-align: center;
        }

        .sidebar h2 {
            color:black;
            margin-bottom: 20px;
        }

        .sidebar ul {
            list-style-type: none;
            padding: 0;
        }

        .sidebar ul li {
            margin-bottom: 15px;
        }

        .sidebar ul li a {
            color: #ffffff;
            text-decoration: none;
            padding: 10px 20px;
            border: 1px solid #ffffff;
            border-radius: 5px;
            display: block;
            transition: background-color 0.3s, color 0.3s;
        }

        .sidebar ul li a:hover {
            background-color: #ffffff;
            color: #003366;
        }

        .form-container {
            margin-top: 20px;
            
        }

        .form-container h1 {
            font-size: 1.4em;
            margin-bottom: 20px;
        }
        
        .form-container form label{
            font-size:1em;
        }
        .form-container form input{
            margin-bottom:15px;
            font-sie:1.5em;
            padding:10px;
        }
        
        .form-container form button {
            display: block;
            width: 100%;
            padding: 12px;
            margin-bottom: 15px;
            background-color: #003366;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1em;
            transition: background-color 0.3s, transform 0.3s;
        }

        .form-container form button a {
            color: white;
            text-decoration: none;
        }

        .form-container form button:hover {
            background-color: #002244;
            transform: scale(1.05);
        }

        .content {
            flex: 1;
            padding: 20px;
        }

        .content h2 {
            color: #003366;
            margin-bottom: 20px;
        }

        .welcome {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-bottom: 20px;
        }

        .welcome img {
            width: 180px;
            height: auto;
            border-radius: 10px;
            margin-bottom: 10px;
        }

        .welcome p {
            font-size: 1.3rem;
            color: #003366;
            margin-top: 5px;
            text-align: center;
        }

        .batch-list {
            margin-top: 20px;
        }

        .batch-list ul {
            list-style-type: none;
            padding: 0;
        }

        .batch-list ul li {
            margin-bottom: 15px;
        }

        .batch-list ul li a {
            color: #003366;
            text-decoration: none;
            padding: 12px 20px;
            display: block;
            border: 2px solid #003366;
            border-radius: 5px;
            background-color: #e6f0ff;
            transition: background-color 0.3s, color 0.3s;
        }

        .batch-list ul li a:hover {
            background-color: #003366;
            color: #ffffff;
        }

        .student-list {
            margin-top: 20px;
        }

        .student-list table {
            width: 100%;
            border-collapse: collapse;
        }

        .student-list table, .student-list th, .student-list td {
            border: 1px solid #ddd;
        }

        .student-list th, .student-list td {
            padding: 12px;
            text-align: left;
        }

        .student-list th {
            background-color: #003366;
            color: white;
        }

        .student-list td a {
            color: #003366;
            text-decoration: none;
        }

        .student-list td a:hover {
            text-decoration: underline;
        }

        .footer {
            background-color: rgb(36, 36, 87);
            color: white;
            padding: 15px;
            text-align: center;
        }

        .footer p {
            margin: 5px 0;
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
         .batch-dropdown {
        position: relative;
        display: block;
        width: 100%; /* Full width */
        margin-bottom: 20px;
    }

    .batch-dropdown button {
        width: 100%;
        padding: 15px;
        font-size: 1.2rem;
        background-color: #003366;
        color: white;
        border: none;
        cursor: pointer;
        text-align: left; /* Align text to left */
        transition: background-color 0.3s;
    }

    .batch-dropdown button:hover {
        background-color: #002244;
    }

    .batch-dropdown-content {
        display: none;
        position: absolute;
        top: 100%; /* Positioned below the button */
        left: 0;
        width: 100%; /* Full width of the parent button */
        background-color: white;
        box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.2);
        z-index: 1;
        border: 1px solid #ddd;
    }

    .batch-dropdown-content a {
        padding: 12px 20px;
        display: block;
        text-decoration: none;
        color: #003366;
        background-color: #e6f0ff;
        border-bottom: 1px solid #ddd;
    }

    .batch-dropdown-content a:hover {
        background-color: #003366;
        color: white;
    }

    .batch-dropdown.show .batch-dropdown-content {
        display: block;
    }
         
    </style>
</head>
<body>
    <header>
        <section class="header">
            <div>
                <img class="ceg" src="images/ceg.png" alt="au_logo">
            </div>
            <div>
                <h2>DEPARTMENT OF INFORMATION SCIENCE AND TECHNOLOGY</h2>
            </div>
            <div>
                <img class="ist" src="images/ist.png" alt="ist_logo">
            </div>
        </section>
    </header>
    <nav class="navbar">
        <a href="home.py">Home</a><a id="sep" >--></a>
        <a href="">Dashboard</a>
    </nav>
    <div class="main">
        <div class="sidebar">
            <div class="form-container">
                <h1>SEARCH STUDENT DETAILS HERE!</h1>
                <form method="post" enctype="multipart/form-data">
                    <label for="regno">Register No:</label>
                    <input type="text" name="regno" id="regno" placeholder="Enter Register No" required>
                    <button type="submit" name="alldetails">Get All Details</button>
                    <button type="submit" name="personaldetails">Get Personal Details</button>
                    <button type="submit" name="academicdetails">Get Academic Details</button>
                    <button type="submit" name="scholarshipdetails">Get Scholarship Details</button>
                    <button type="submit" name="exitdetails">Get Exit Student Details</button>
                </form>
            </div>
        </div>
""")
print(f"""
        <div class="content">
            <div class="welcome">
                <img src="staff_photos/{Photo}" alt="Welcome Image">
                <p>Welcome {Name}</p>
                <p>{Staffid}</p>
            </div>
            <div class="batch-list">
                <h2>Batches</h2>
                <ul>
""")
# for batch in batches:
#     print(f"""<li><a href="?id={Staffid}&batch={batch[0]}">{batch[0]}</a></li>""")
# print(f"""
#                 </ul>
#             </div>
#             <div class="student-list">
#                 <h2>Batch: {Batch if Batch else 'Select a batch'}</h2>
# """)
# if Batch and students:
#     print("""
#                 <h2>Students</h2>
#                 <table>
#                     <thead>
#                         <tr>
#                             <th>Register No</th>
#                             <th>Name</th>
#                         </tr>
#                     </thead>
#                     <tbody>
#     """)
#     for student in students:
#         print(f"""
#                         <tr>
#                             <td><a href="all_details.py?id={student[0]}&staffid={Staffid}">{student[0]}</a></td>
#                             <td>{student[1]}</td>
#                         </tr>
#         """)

# Loop through batches and create dropdowns for student list and batch analysis
for batch in batches:
    print(f"""
    <li>
        <div class="batch-dropdown">
        <button onclick="toggleDropdown()">Batch {batch[0]}</button>
        <div class="batch-dropdown-content">
            <a href="?id={Staffid}&batch={batch[0]}">Student List</a>
            <a href="analysis.py?id={Staffid}&batch={batch[0]}">Batch Analysis</a>
        </div>
    </div>
    </li>
    """)

print(f"""
                </ul>
            </div>
""")

# If students are fetched, display the student list
if students:
    print(f"""
            <div class="student-list">
                <h2>Student List for Batch {Batch}</h2>
                <table>
                    <thead>
                        <tr>
                            <th>Register No</th>
                            <th>Name</th>
                        </tr>
                    </thead>
                    <tbody>
    """)
    for student in students:
        print(f"""
                        <tr>
                            <td><a href="all_details.py?id={student[0]}&staffid={Staffid}">{student[0]}</a></td>
                            <td>{student[1]}</td>
                        </tr>
        """)
    print("""
                    </tbody>
                </table>
    """)
elif Batch:
    print("<p>No students found for this batch.</p>")
else:
    print("<p>Select a batch to view students.</p>")
print("""
            </div>
        </div>
    </div>
    <footer class="footer">
        <p>&copy; 2024 IST Department. All rights reserved.</p>
    </footer>
    <script>
        function toggleDropdown() {
        var dropdown = document.querySelector(".batch-dropdown");
        dropdown.classList.toggle("show");
    }

    // Close the dropdown if clicked outside
    window.onclick = function(event) {
        if (!event.target.matches('.batch-dropdown button')) {
            var dropdowns = document.getElementsByClassName("batch-dropdown-content");
            for (var i = 0; i < dropdowns.length; i++) {
                var openDropdown = dropdowns[i];
                if (openDropdown.style.display === "block") {
                    openDropdown.style.display = "none";
                }
            }
        }
    }
    </script>
</body>
</html>
""")

Regno=form.getvalue("regno")
All=form.getvalue("alldetails")
Personal=form.getvalue("personaldetails")
Academics=form.getvalue("academicdetails")
Scholarship=form.getvalue("scholarshipdetails")
Exit=form.getvalue("exitdetails")

if All != None :
    print(f"""
    <script>
    location.href='all_details.py?id={Regno}&staffid={Staffid}';
    </script>
    """)

if Personal != None :
    print(f"""
    <script>
    location.href='personal_details.py?id={Regno}&staffid={Staffid}';
    </script>
    """)
if Academics != None :
    print(f"""
    <script>
    location.href='academic_details.py?id={Regno}&staffid={Staffid}';
    </script>
    """)
if Scholarship != None :
    print(f"""
    <script>
    location.href='scholarship_details.py?id={Regno}&staffid={Staffid}';
    </script>
    """)
if Exit != None :
    print(f"""
    <script>
    location.href='exit_student_details.py?id={Regno}&staffid={Staffid}';
    </script>
    """)


