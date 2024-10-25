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
    <style>
    body {
    font-family: Georgia, 'Times New Roman', Times, serif;
    background-color: #feffff;
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    min-height: 100vh;
    overflow-x: hidden; 
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

.form-container {
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    background-color: #ffffff;
    padding: 40px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.4);
    max-width: 1000px;
    width: 100%;
    margin: 20px auto;
    font-size: 24px;
    color: rgb(6, 6, 83);
    margin-top: 50px;
}

.photo-section {
    flex: 2;
    padding: 10px;
}

.photo-section img {
    justify-content: center;
    max-width: 100%;
    height: auto;
    padding-top: 69px;
    border-radius: 4px;
}

.form-info-section {
    flex: 2;
    padding: 20px 80px 20px 20px;
    color: white;
}

h1,
h2 {
    text-align: center;
    margin-bottom: 20px;
    color: #0a2949;
    padding-bottom: 20px;
}

.h {
    color: rgb(183, 46, 46);
    text-align: center;
    margin-bottom: 20px;
}

.form-group {
    display: flex;
    flex-direction: column;
    margin-bottom: 15px;
}

label {
    margin-bottom: 5px;
    font-weight: bold;
    color: #000000;
    padding-bottom: 10px;
}

input,
select {
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 6px;
    font-size: 18px;
    font-style: oblique;
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
    font-size: 18px;
    text-align: center; /* Padding inside options */
}

/* Button styles */
button {
    padding: 10px 20px;
    background-color: #0a2949;
    color: #F4A896;
    border: none;
    border-radius: 4px;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.3s;
}

button:hover {
    background-color: #4b5a6a;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 20px;
    background-color:#feffff;
    color: black;
    width: 100%;
    box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.1);
    font-size: 20px;
    margin-top: 70px;
}



/* Responsive Styles */

/* Tablets and smaller devices */
@media (max-width: 768px) {
    .header {
        flex-direction: row;
        align-items: flex-start;
        padding: 15px;
    }

    .header img {
        height: 30px; /* Adjust the height for smaller screens */
    }

    .main-content {
        padding-top: 30px;
    }

    .form-container {
        padding: 30px;
        font-size: 15px;
    }

    th,
    td {
        font-size: 18px;
    }

    input[type="text"] {
        height: 16px;
        font-size: 13px;
    }

    option {
        font-size: 14px;
    }

    button[type="submit"] {
        font-size: 15px;
        padding: 10px 20px;
    }

    select {
        font-size: 16px; /* Adjust select font size for tablets */
    }

    .photo-section {
        justify-content: center; /* Center the photo section */
        display: flex;
    }
}

/* Phones and smaller devices */
@media (max-width: 480px) {
    .header {
        padding: 20px;
    }

    .header img {
        height: 30px; /* Adjust the height for smaller screens */
    }

    .main-content {
        padding-top: 100px;
    }

    .form-container {
        padding: 20px;
        font-size: 15px;
        flex-direction: column; /* Stack the sections vertically */
        align-items: center; /* Center the content */
    }

    th,
    td {
        font-size: 16px;
    }

    input[type="text"] {
        height: 18px;
        font-size: 14px;
    }

    button[type="submit"] {
        font-size: 12px;
        padding: 8px 16px;
    }

    h1,
    h2 {
        font-size: 18px;
    }

    select {
        font-size: 16px; /* Adjust select font size for phones */
    }

    .photo-section {
        justify-content: center; /* Center the photo section */
        display: flex;
        margin-bottom: 20px; /* Add some space below the photo section */
    }

    .form-info-section {
        width: 100%; /* Make the form section full width */
        padding: 0 20px; /* Add padding to the form section */
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
            <h2 style="color:white";>DEPARTMENT OF INFORMATION SCIENCE AND TECHNOLOGY</h2>
        </div>
        <div>
            <img class="ist" src="images/ist.png" alt="ist_logo">
        </div>
    </header>
    <nav class="navbar">
        <a href="home.py">Home</a><a id="sep" >--></a>
        <a href="student_main.py?id={Regno}">Student Details</a><a id="sep" >--></a>
        <a href="" >Placement Details</a>
    </nav>
    <div class="main-content">
        <h1  style="text-align:center">EXIT DETAILS FORM</h1>
        <div class="form-container">
            <div class="photo-section">
                <img src="images/placement.png" alt="Placeholder">
            </div>
            
            <div class="form-info-section">
                <form method="post" enctype="multipart/form-data">
                    <h2>Placement Details</h2>
                    <div class="form-group">
                        <label for="companyName">Company Name:</label>
                        <input type="text" id="companyName" name="companyName" required>
                    </div>
                    <div class="form-group">
                        <label for="selectionType">Selection Type:</label>
                        <select id="selectionType" name="selectionType" required>
                            <option value="selectone">-- Select one --</option>
                            <option value="onCampus">On Campus</option>
                            <option value="offCampus">Off Campus</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="salaryPackage">Salary Package:</label>
                        <input type="text" id="salaryPackage" name="salaryPackage" required>
                    </div>
                    <div class="form-group">
                        <label for="jobType">Job Type:</label>
                        <select id="jobType" name="jobType" required>
                            <option value="selectone">-- Select one --</option>
                            <option value="productBased">Product Based</option>
                            <option value="serviceBased">Service Based</option>
                        </select>
                    </div>
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

CompanyName=form.getvalue("companyName")
SelectionType=form.getvalue("selectionType")
SalaryPackage=form.getvalue("salaryPackage")
JobType=form.getvalue("jobType")
Submit=form.getvalue("submit")

if Submit != None :

    q = """SELECT id FROM placement_details WHERE register_no='%s'""" % (Regno)
    cur.execute(q)
    rec = cur.fetchone()

    if rec != None:
        q = """UPDATE placement_details SET company_name='%s',selection_type='%s',salary_package='%s',job_type='%s' WHERE register_no='%s'""" % (CompanyName,SelectionType,SalaryPackage,JobType,Regno)
        cur.execute(q)
        con.commit()

        print("""
                                <script>
                                alert("Placement_details Updated Successfully !!");
                                location.href='student_main.py?id=%s';
                                </script>
                                """ % Regno)

    else:
        q = """INSERT INTO placement_details(register_no,company_name,selection_type,salary_package,job_type) VALUES ('%s','%s','%s','%s','%s')""" % (
            Regno,CompanyName,SelectionType,SalaryPackage,JobType)
        cur.execute(q)
        con.commit()

        print("""
                        <script>
                        alert("Placement_details Added Successfully !!");
                        location.href='student_main.py?id=%s';
                        </script>
                        """ % Regno)




