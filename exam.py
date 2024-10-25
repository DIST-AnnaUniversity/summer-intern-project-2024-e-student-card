#!C:/Python/python.exe
import pymysql, cgitb, cgi, os

print("Content-type: text/html\r\n\r\n")
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="summer_project")
cur = con.cursor()

form=cgi.FieldStorage()
Regno=form.getvalue("id")

print("""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Exit Form</title>
    <link rel="icon" href="images/ist.png">
    <link rel="stylesheet" href="examstyle.css">
    <style>
    
    body {
    font-family: 'Arial', sans-serif;
    background-color: #f2f3f4;
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    min-height: 100vh;
    overflow-x: hidden; /* Prevent horizontal scrolling */
    overflow-y: auto; 
}

.header {
    background-color: rgb(36, 36, 87);
    color: white;
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    padding: 1vw;
    text-align: center;
    height: 60px;
}
.heder h1{
    color:white;
}
.header img {
    height: 40px;
    width: auto;
    margin: 0 1vw; /
}

.header p {
    flex-grow: 1;
    margin: 1vw;
    text-shadow: 3px 3px black;
}

.ceg .ist {
    width: 30vw;
    height: auto;
}

.main {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-image: url("images/dept2.jpg");
    background-size: cover;
    width: 100vw;
}

.main div {
    background-color: black;
    color: white;
    width: 40vw;
    text-align: center;
    margin: 3vw 0;
    font-size: min(3vw, 20px);
    padding: 2vw;
    border-radius: 20px;
    outline: 3px solid white;
    outline-offset: 2px;
}

.main div:hover,
.main div:focus {
    background-color: red;
}

.main-content {
    padding-top: 30px;
    width: 100%;
    justify-content: center;
}


.main-content {
    padding-top: 130px;
    width: 100%;
    justify-content: center;
}

.form-container {
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    background-color: white;
    padding: 40px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
    max-width: 950px;
    width: 100%;
    margin: 20px auto 50px;
    font-size: 24px;
    margin-top: 20px;
}

.photo-section {
    flex: 2;
    padding: 10px;
}

.photo-section img {
    justify-content: center;
    max-width: 100%;
    height: 350px;
    padding-top: 69px;
    border-radius: 4px;
}

.form-info-section {
    flex: 2;
    padding: 20px;
    padding-left: 80px;
    color: white;
}

h1, h2 {
    text-align: center;
    margin-bottom: 20px;
    color: #0a2949;
}

.h {
    color: rgb(183, 46, 46);
    text-align: center;
    margin-bottom: 20px;
    color: #0a2949;
}

.form-group {
    display: flex;
    flex-direction: column;
    margin-bottom: 15px;
}

label {
    margin-bottom: 5px;
    font-weight: bold;
    color: black;
    font-size:18px;
}


/* Styling for date input */
.form-group input[type="date"] {
    appearance: none; /* Remove default browser styling */
    background-color: #fbf9f9;
    border: 1px solid #ccc;
    border-radius: 4px;
    padding: 10px;
    font-size: 16px;
    font-style: oblique;
    width: 100%;
    box-sizing: border-box;
    transition: border-color 0.3s, box-shadow 0.3s;
}

.form-group input[type="date"]:focus {
    border-color: #00796b;
    outline: none;
    box-shadow: 0 0 5px rgba(0, 121, 107, 0.5);
}

.form-group input[type="date"]::placeholder {
    color: #a9a9a9;
    font-style: italic;
}


.form-group input[type="date"]::-webkit-calendar-picker-indicator {
    cursor: pointer;
    filter: invert(0.5); /* Adjust the color of the calendar icon */
}

/* Adjusting the padding for the date input */
.form-group input[type="date"]::-webkit-inner-spin-button,
.form-group input[type="date"]::-webkit-clear-button {
    display: none; /* Remove default clear and spin buttons */
}

select {
    appearance: none; /* Remove default arrow */
    background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24"><path fill="none" stroke="%23000000" stroke-width="2" d="M12 5l-7 7 7 7 7-7z"/></svg>') no-repeat right 10px center;
    background-color: #fbf9f9; /* Change background color */
}

option {
    background-color: #ebe5e5; /* Background color of options */
    color: #000; /* Text color of options */
    padding: 15px;
    font-size: 17px;
    text-align: center; /* Padding inside options */
}

input, select {
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 13px;
    color:black;
}

button {
    padding: 10px 20px;
    background-color: #0a2949;
    color: black;
    border: none;
    border-radius: 4px;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.3s;
}

button:hover {
    background-color: #4b5a6a;
}

footer {
    text-align: center;
    padding: 20px;
    background-color: white;
    color: #F4A896;
    width: 100%;
    box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.1);
    font-size: 20px;
    margin-top: 70px;
}

footer a {
    color: white;
    text-decoration: none;
}

footer a:hover {
    text-decoration: underline;
}

/* Responsive Styles */

@media (max-width: 768px) {
    .header {
        flex-direction: row;
    }
    .header img {
        flex-direction: column;
        height: 80px;
    }
    .form-container {
        flex-direction:row;
        padding: 20px;
    }
    .form-group {
        flex-direction:column;
    }
    .photo-section, .form-info-section {
        width: 100%;
    }
}

@media (max-width: 480px) {
    .header {
        padding: 10px;
    }
    .form-container {
        padding: 10px;
    }
    button {
        width: 100%;
        font-size: 14px;
    }
    input, select {
        font-size: 14px;
    }
}
.navbar {
    width:100vw;
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
</head>
""")
print(f"""
<body>
    <header class="header">
        <div>
            <img class="ceg" src="images/ceg.png" alt="au_logo">
        </div>
        <div>
            <h2 style="color:white">DEPARTMENT OF INFORMATION SCIENCE AND TECHNOLOGY</h2>
        </div>
        <div>
            <img class="ist" src="images/ist.png" alt="ist_logo">
        </div>
    </header>
    <nav class="navbar">
        <a href="home.py">Home</a><a id="sep" >--></a>
        <a href="student_main.py?id={Regno}">Student Details</a><a id="sep" >--></a>
        <a href="" >Exam Details</a>
    </nav>
    <div class="main-content">
        <h1 style="text-align:center">EXIT DETAILS FORM</h1>
        <div class="form-container">
            <div class="photo-section">
                <img src="images/e1.jpg" alt="Placeholder">
            </div>
            <div class="form-info-section">
                <form method="post" enctype="multipart/form-data">
                    <section>
                        <h2>National/International Exam Details</h2>
                        <div class="form-group">
                            <label for="examType">Exam Type:</label>
                            <select id="examType" name="examType" required>
                                <option value="GRE">GRE</option>
                                <option value="TOEFL">TOEFL</option>
                                <option value="IELTS">IELTS</option>
                                <option value="GATE">GATE</option>
                                <option value="NET">NET</option>
                                <option value="UPSC">UPSC</option>
                                <option value="other">Other</option>
                            </select>
                        </div>
                    </section>
                    <section>
                        <h2>Certified Course (if any from courses ,edx,NPTEL etc )</h2>
                        <div class="form-group">
                            <label for="courseName">Course Name</label>
                            <input type="text" id="courseName" name="courseName">
                        </div>
                        <div class="form-group">
                            <label for="completionDate">Completion Date:</label>
                            <input type="date" id="completionDate" name="completionDate">
                        </div>
                    </section>
                    <button type="submit" name="submit">Submit</button>
                </form>
            </div>
        </div>
    </div>
    <footer>
        <p>&copy; 2024 Information Technology. All rights reserved.</p>
    </footer>
</body>
</html>

""")

ExamType=form.getvalue("examType")
CourseName=form.getvalue("courseName")
Completiondate=form.getvalue("completionDate")
Submit=form.getvalue("submit")

if Submit != None :

    q = """SELECT id FROM exam_details WHERE register_no='%s'""" % (Regno)
    cur.execute(q)
    rec = cur.fetchone()

    if rec != None:
        q = """UPDATE exam_details SET exam_type='%s',course_name='%s',completion_date='%s' WHERE register_no='%s'""" % (
        ExamType,CourseName,Completiondate,Regno)
        cur.execute(q)
        con.commit()

        print("""
                               <script>
                               alert("Exam_details Updated Successfully !!");
                               location.href='student_main.py?id=%s';
                               </script>
                               """ % Regno)

    else:
        q = """INSERT INTO exam_details(register_no,exam_type,course_name,completion_date) VALUES ('%s','%s','%s','%s')""" % (
            Regno,ExamType,CourseName,Completiondate)
        cur.execute(q)
        con.commit()

        print("""
                       <script>
                       alert("Exams_details Added Successfully !!");
                       location.href='student_main.py?id=%s';
                       </script>
                       """ % Regno)
