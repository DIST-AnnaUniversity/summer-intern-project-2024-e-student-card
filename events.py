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
    <title>Paper Publishing Details Form</title>
    <link rel="icon" href="images/ist.png">
    <style>
         @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

body {
    font-family: 'Roboto', sans-serif;
    background-color: #f4f4f9;
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    min-height: 100vh;
}

.header {
    background-color: rgb(36, 36, 87);
    color: white;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 30px;
    width: 100%;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    position: relative;
    top: 0;
    left: 0;
    z-index: 1000;
    overflow-x: hidden; /* Prevent horizontal scrolling */
    overflow-y: auto; 
}

.header img {
    height: 50px;
}

.header h2 {
    margin: 0;
}

.content {
    width: 100%;
    max-width: 800px;
    margin: 120px auto 20px;
    padding: 80px;
    margin-top: 30px;
    background-color: white;
    border-radius: 10px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
    font-weight: bold;
}

h1 {
    text-align: center;
    color: #333;
    margin-bottom: 20px;
    font-weight: 700;
}

.form-group {
    margin-bottom: 20px;
}

.form-group label {
    display: block;
    margin-bottom: 8px;
    font-weight: bold;
    color: #1e0c81;
    padding-bottom: 10px;
    font-size: larger;
    font-size: 22px;
}

.form-group input[type="text"],
.form-group input[type="date"] {
    width: 100%;
    padding: 12px;
    font-size: 16px;
    box-sizing: border-box;
    border: none;
    border-bottom: 2px solid #6d6969;
    background-color: transparent;
    transition: border-color 0.3s, box-shadow 0.3s;
    font-size: 20px;
}

.form-group input[type="text"]:focus,
.form-group input[type="date"]:focus {
    border-color: #3f51b5;
    box-shadow: 0 1px 0 #3f51b5;
    outline: none;
}

.form-group input[type="date"] {
    appearance: none;
    background-color: transparent;
    padding-right: 30px;
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="%233f51b5"><path d="M7 10l5 5 5-5z"/></svg>');
    background-repeat: no-repeat;
    background-position: right 10px center;
    background-size: 16px 16px;
}

.form-group input[type="date"]::-webkit-calendar-picker-indicator {
    position: absolute;
    right: 10px;
    top: 50%;
    transform: translateY(-50%);
    cursor: pointer;
    opacity: 0;
}

.submit-container {
    text-align: center;
    margin-top: 20px;
}

button[type="submit"] {
    padding: 12px 30px;
    background-color: #0a1971;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s, transform 0.3s;
    font-size: 18px;
}

button[type="submit"]:hover {
    background-color: #1b2987;
    transform: translateY(-3px);
}

footer {
    text-align: center;
    padding: 2px;
    background-color: white;
    color: black;
    width: 100%;
    box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.1);
    font-size: 16px;
    position: relative;
    bottom: 0;
    left: 0;
}

footer a {
    color: white;
    text-decoration: none;
}

footer a:hover {
    text-decoration: underline;
}

/* Media Queries */
@media (max-width: 1200px) {
    .content {
        max-width: 700px;
        padding: 15px;
    }
}

@media (max-width: 992px) {
    .header h2 {
        font-size: 1.2rem;
    }
    .content {
        margin: 100px auto 20px;
        max-width: 600px;
        padding: 15px;
    }
    button[type="submit"] {
        font-size: 16px;
        padding: 10px 20px;
    }
}

@media (max-width: 768px) {
    .header {
        flex-direction: column;
        align-items: flex-start;
    }
    .header img {
        height: 40px;
    }
    .header h2 {
        font-size: 1rem;
    }
    .content {
        margin: 90px auto 20px;
        padding: 10px;
    }
    .form-group input[type="text"],
    .form-group input[type="date"] {
        font-size: 14px;
        padding: 10px;
    }
    button[type="submit"] {
        font-size: 14px;
        padding: 8px 16px;
    }
}

@media (max-width: 576px) {
    .header {
        padding: 10px 20px;
    }
    .header img {
        height: 30px;
    }
    .header h2 {
        font-size: 0.9rem;
    }
    .content {
        margin: 80px auto 20px;
        padding: 10px;
    }
    h1 {
        font-size: 1.5rem;
    }
    .form-group input[type="text"],
    .form-group input[type="date"] {
        font-size: 12px;
        padding: 8px;
    }
    button[type="submit"] {
        font-size: 12px;
        padding: 6px 12px;
    }
    footer {
        font-size: 14px;
    }
}
/* Dropdown styling */
.form-group select {
    width: 100%;
    padding: 12px;
    font-size: 16px;
    box-sizing: border-box;
    border: none;
    border-bottom: 2px solid #6d6969;
    background-color: transparent;
    transition: border-color 0.3s, box-shadow 0.3s;
    font-size: 20px;
    cursor: pointer;
}

.form-group select:focus {
    border-color: #3f51b5;
    box-shadow: 0 1px 0 #3f51b5;
    outline: none;
    background-color: #f0f0f0;
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
            <h2>DEPARTMENT OF INFORMATION SCIENCE AND TECHNOLOGY</h2>
        </div>
        <div>
            <img class="ist" src="images/ist.png" alt="ist_logo">
        </div>
    </header>
    <nav class="navbar">
        <a href="home.py">Home</a><a id="sep" >--></a>
        <a href="student_main.py?id={Regno}">Student Details</a><a id="sep" >--></a>
        <a href="" >Events Details</a>
    </nav>
    <h1 style="margin-top:140px;">Technical Events Organized / Participated</h1>
    <main class="content">
        

        <form method="post" enctype="multipart/form-data">
        <div class="form-group">
    <label for="event_type">Event Type:</label>
    <select id="event_type" name="event_type">
    <option value="participated">-- select one --</option>
        <option value="organized">Organized</option>
        <option value="participated">Participated</option>
    </select>
</div>

            <div class="form-group">
                <label for="event_name">Name of the Event:</label>
                <input type="text" id="event_name" name="event_name">
            </div>
            <div class="form-group">
                <label for="institution_organized">Institution Organized:</label>
                <input type="text" id="institution_organized" name="institution_organized">
            </div>
            <div class="form-group">
                <label for="college_university">College / University State / National / International:</label>
                <input type="text" id="college_university" name="college_university">
            </div>
            <div class="form-group">
                <label for="role">Role:</label>
                <input type="text" id="role" name="role">
            </div>
            <div class="form-group">
                <label for="date_duration">Date / Duration:</label>
                <input type="text" id="date_duration" name="date_duration">
            </div>
            <div class="form-group">
                <label for="awards">Awards if any:</label>
                <input type="text" id="awards" name="awards">
            </div>
            <div class="submit-container">
                <button type="submit" name="submit">Submit</button>
            </div>
        </form>
    </main>
    
    <footer>
        <p>&copy; 2024 Information Technology. All rights reserved.</p>
    </footer>
</body>
</html>
   



""")

EventName=form.getvalue("event_name")
Institution=form.getvalue("institution_organized")
College=form.getvalue("college_university")
Role=form.getvalue("role")
DateDuration=form.getvalue("date_duration")
Awards=form.getvalue("awards")
Submit=form.getvalue("submit")



if Submit != None :

    q = """SELECT id FROM events_details WHERE register_no='%s'""" % (Regno)
    cur.execute(q)
    rec = cur.fetchone()

    if rec != None:
        q = """UPDATE events_details SET event_name='%s',institution_organized='%s',college_university='%s',role='%s',date_duration='%s',awards='%s' WHERE register_no='%s'""" % (
            EventName,Institution,College,Role,DateDuration,Awards,Regno)
        cur.execute(q)
        con.commit()

        print("""
                                   <script>
                                   alert("Technical_Events_details Updated Successfully !!");
                                   location.href='student_main.py?id=%s';
                                   </script>
                                   """ % Regno)

    else:
        q = """INSERT INTO events_details(register_no,event_name,institution_organized,college_university,role,date_duration,awards) VALUES ('%s','%s','%s','%s','%s','%s','%s')""" % (
            Regno,EventName,Institution,College,Role,DateDuration,Awards)
        cur.execute(q)
        con.commit()

        print("""
                           <script>
                           alert("Technical_Events_details Added Successfully !!");
                           location.href='student_main.py?id=%s';
                           </script>
                           """ % Regno)
