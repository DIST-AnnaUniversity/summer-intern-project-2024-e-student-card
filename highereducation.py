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
    /*<link rel="stylesheet" href="higereducationstyle.css">*/
    <style>
    
    body {
    font-family: 'Arial', sans-serif;
    background-color: #ffffff;
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
    position:relative;
}

.header h1 {
    color: white;
}

.header img {
    height: 40px;
    width: auto;
    margin: 0 1vw;
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


.form-container {
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    background-color: #ffffff;
    padding: 40px;
    margin:50px;
    border-radius: 8px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.8); /* Enhanced shadow */
    max-width: 1200px;
    width: 100%;
    font-size: 24px;
    color: black;

}

.photo-section {
    flex: 2;
    padding: 10px;
}

.photo-section img {
    max-width: 100%;
    height:400px;
    border-radius: 4px;
    padding-top:100px;
    padding-bottom: 100px;
}

.form-info-section {
    flex: 2;
    padding: 30px;
    padding-left: 6px;
    color: black; /* Changed to black for consistency */
}

h1, h2 {
    text-align: center;
    margin-bottom: 20px;
}

.form-group {
    display: flex;
    flex-direction: column;
    margin-bottom: 15px;
}

label {
    color: black;
    margin-bottom: 5px;
    font-weight: bold;
}

input, select {
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 10px;
    font-size: 16px;
}

button {
    padding: 10px 20px;
    background-color:#0b3869;
    color: #e9dfdd;
    border: none;
    border-radius: 4px;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.3s, transform 0.3s;
}

button:hover {
    background-color: #4b5a6a;
    transform: scale(1.05); /* Slight scale effect on hover */
}

footer {
    text-align: center;
    padding: 20px;
    background-color: white;
    color: black;
    width: 100%;
    box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.3);
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

@media (max-width: 768px) {
    .header {
        flex-direction: row;
        font-size:12px;
    }
    .header img {
        flex-direction: column;
        height: 40px;
    }
    .form-container {
        flex-direction:row;
        padding: 10px;
        font-size:16px;
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
    .h1{
    font-size:20px;
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
        <a href="" >Higher Education Details</a>
    </nav>
    <div class="main-content">
        <h1 style="text-align:center">EXIT DETAILS FORM </h1>

        <h1 style="text-align:center"> Higher Education Details(if Selected/Admitted ):ME./M.Tech/M.S</h1>

        <div class="form-container">
            <div class="photo-section">
                <img src="images/h1.png" alt="Placeholder">
            </div>
            <div class="form-info-section">
                <form method="post" enctype="multipart/form-data">
                    <section>
                        <h2>Higher Education Details</h2>
                        <div class="form-group">
                            <label for="universityApplied">Number of Universities Applied:</label>
                            <input type="number" id="universityApplied" name="universityApplied" required>
                        </div>
                        <div class="form-group">
                            <label for="universityAdmitted">University Admitted:</label>
                            <input type="text" id="universityAdmitted" name="universityAdmitted" required>
                        </div>
                        <div class="form-group">
                            <label for="admissionYear">Year of Admission:</label>
                            <input type="number" id="admissionYear" name="admissionYear" required>
                        </div>
                        <div class="form-group">
                            <label for="specialization">Specialization:</label>
                            <input type="text" id="specialization" name="specialization" required>
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

UniversityApplied=form.getvalue("universityApplied")
UniversityAdmitted=form.getvalue("universityAdmitted")
AdmissionYear=form.getvalue("admissionYear")
Specialization=form.getvalue("specialization")
Submit=form.getvalue("submit")

if Submit != None :

    q = """SELECT id FROM higher_studies_details WHERE register_no='%s'""" % (Regno)
    cur.execute(q)
    rec = cur.fetchone()

    if rec != None:
        q = """UPDATE higher_studies_details SET university_applied='%s',university_admitted='%s',admission_year='%s',specialization='%s' WHERE register_no='%s'""" % (
            UniversityApplied,UniversityAdmitted,AdmissionYear,Specialization,Regno)
        cur.execute(q)
        con.commit()

        print("""
                                   <script>
                                   alert("Higher_Education_details Updated Successfully !!");
                                   location.href='student_main.py?id=%s';
                                   </script>
                                   """ % Regno)

    else:
        q = """INSERT INTO higher_studies_details(register_no,university_applied,university_admitted,admission_year,specialization) VALUES ('%s','%s','%s','%s','%s')""" % (
            Regno,UniversityApplied,UniversityAdmitted,AdmissionYear,Specialization)
        cur.execute(q)
        con.commit()

        print("""
                           <script>
                           alert("Higher_Education_details Added Successfully !!");
                           location.href='student_main.py?id=%s';
                           </script>
                           """ % Regno)
