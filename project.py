#!C:/Python/python.exe
import pymysql, cgitb, cgi, os

print("Content-type: text/html\r\n\r\n")
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="summer_project")
cur = con.cursor()


form = cgi.FieldStorage()
Regno = form.getvalue("id")


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
    font-family: 'Arial', sans-serif;
    background-color: #e9ecef;
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    min-height: 100vh;
    overflow-x: hidden; 
    overflow-y: auto;
    position: relative;
}

.header {
    background-color: #242457;
    color: white;
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    padding: 10px 2vw;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.header h2 {
    font-size: 1.5rem;
    margin: 0;
}

.header img {
    height: 50px;
    width: auto;
}

.navbar {
    background-color: #181839;
    overflow: hidden;
    text-align: left;
    width: 100%;
    padding: 0 10%;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.navbar a {
    color: white;
    padding: 14px 20px;
    text-decoration: none;
    font-size: 1rem;
    transition: background-color 0.3s;
}

.navbar a:hover {
    background-color: #343457;
    border-radius: 5px;
}

.main-content {
    padding-top: 50px;
    width: 90%;
    max-width: 1000px;
    margin: 0 auto;
}

.form-container {
    background-color: white;
    padding: 30px;
    border-radius: 8px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    margin-top: 30px;
    margin-bottom: 60px;
}

h1, h2 {
    text-align: center;
    color: #0a2949;
    margin-bottom: 20px;
}
h1 {
    text-align: center;
    color: #0a2949;
    margin-bottom: 20px;
    font-size: 2rem; /* Adjust the font size if needed */
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px; /* Space between text and image */
}

.project-icon {
    height: 30px; /* Adjust size as needed */
    width: auto;
    vertical-align: middle; /* Aligns the image with the text */
}

.form-row {
    display: flex;
    justify-content: space-between;
    margin-bottom: 20px;
}

.form-group {
    width: 48%;
    display: flex;
    flex-direction: column;
}

.form-group-full {
    width: 100%;
    display: flex;
    flex-direction: column;
    margin-bottom: 20px;
}

label {
    font-weight: bold;
    color: #0a2949;
    margin-bottom: 5px;
}

input, select, textarea {
    border: none;
    border-bottom: 2px solid #0a2949;
    background-color: transparent;
    font-size: 16px;
    color: #333;
    padding: 10px 0;
    transition: border-color 0.3s ease-in-out;
}

input:focus, select:focus, textarea:focus {
    border-bottom: 2px solid #4b5a6a;
    outline: none;
}



button {
    padding: 12px 24px;
    background-color: #0a2949;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 16px;
    cursor: pointer;
    margin-top: 20px;
    margin-left: 450px;
    transition: background-color 0.3s, transform 0.2s;
}

button:hover {
    background-color: #4b5a6a;
    transform: translateY(-2px);
}

footer {
    text-align: center;
    padding: 2px;
    background-color: #ebf0f4;
    color: rgb(10, 7, 7);
    width: 100%;
    box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.1);
    font-size: 16px;
    margin-top: auto;
}

@media (max-width: 768px) {
    .header img {
        height: 40px;
    }
    .header h2 {
        font-size: 1.2rem;
    }
    .form-container {
        padding: 20px;
    }
    .navbar a {
        font-size: 0.9rem;
    }
    .form-row {
        flex-direction: column;
    }
    .form-group {
        width: 100%;
        margin-bottom: 10px;
    }
}

@media (max-width: 480px) {
    .header {
        padding: 10px;
    }
    .form-container {
        padding: 15px;
    }
    button {
        width: 100%;
        font-size: 14px;
    }
    input, select {
        font-size: 14px;
    }
}

   </style>
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
        <a href="" >Project Details</a>
    </nav>
    <div class="main-content">
        <h1>
            <img src="images/projectpic.jpg" alt="Project Icon" class="project-icon">
            PROJECT DETAILS
        </h1>
        
        <div class="form-container">
            <div class="form-info-section">
                <form method="post" enctype="multipart/form-data">
                    <section>
                        <div class="form-row">
                            <div class="form-group">
                                <label for="projectTitle1">Summar Project Name: </label>
                                <input type="text" id="projectTitle1" name="projectTitle1" required>
                            </div>
                            <div class="form-group">
                                <label for="guideName1">Project Guide:</label>
                                <input type="text" id="guideName1" name="guideName1" required>
                            </div>
                        </div>
                        <div class="form-row">
                            <div class="form-group">
                                <label for="projectTitle2">Final Year Project Name:</label>
                                <input type="text" id="projectTitle2" name="projectTitle2">
                            </div>
                            <div class="form-group">
                                <label for="guideName2">Project Guide:</label>
                                <input type="text" id="guideName2" name="guideName2">
                            </div>
                        </div>
                        <div class="form-group-full">
                            <label for="otherProjects">Other Project Details :</label>
                            <textarea id="otherProjects" name="otherProjects" rows="4"></textarea>
                        </div>
                    </section>
                    <button type="submit" name="submit">Submit</button>
                </form>
            </div>
        </div>
    </div>
    <footer>
        <p style="color:black;">&copy; 2024 Information Technology. All rights reserved.</p>
    </footer>
</body>
</html>


""")


projectTitle1=form.getvalue("projectTitle1")
projectTitle2=form.getvalue("projectTitle2")
guideName1=form.getvalue("guideName1")
guideName2=form.getvalue("guideName2")
otherProjects=form.getvalue("otherProjects")
Submit=form.getvalue("submit")

if Submit != None :
    q="""SELECT id FROM project_details WHERE register_no='%s'"""%(Regno)
    cur.execute(q)
    rec = cur.fetchone()

    if rec != None :
        q="""UPDATE project_details SET project_title1='%s',guide_name1='%s',project_title2='%s',guide_name2='%s',other_projects='%s' WHERE register_no='%s'"""%(projectTitle1,guideName1,projectTitle2,guideName2,otherProjects,Regno)
        cur.execute(q)
        con.commit()

        print("""
                            <script>
                            alert("Project_details Updated Successfully !!");
                            location.href='student_main.py?id=%s';
                            </script>
                            """ % Regno)

    else:
        q = """INSERT INTO project_details(register_no,project_title1,guide_name1,project_title2,guide_name2,other_projects) VALUES ('%s','%s','%s','%s','%s','%s')""" % (
            Regno, projectTitle1, guideName1, projectTitle2, guideName2, otherProjects)
        cur.execute(q)
        con.commit()

        print("""
                    <script>
                    alert("Project_details Added Successfully !!");
                    location.href='student_main.py?id=%s';
                    </script>
                    """ % Regno)
