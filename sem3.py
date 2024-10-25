#!C:/Python/python.exe
import pymysql, cgitb, cgi, os

print("Content-type: text/html\r\n\r\n")
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="summer_project")
cur = con.cursor()

form = cgi.FieldStorage()
Regno = form.getvalue("id")

q = """SELECT * FROM sem3 WHERE register_no='%s'""" % (Regno);
cur.execute(q);
result = cur.fetchone();

if result is None:
    result = ["" for _ in range(56)]

print(f"""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Semester 3 </title>
    <link rel="icon" href="images/ist.png">
    <link rel="stylesheet" href="semstyle.css">
</head>
<body>
    <header>
        <section class="header">
            <div>
                <img class="ceg" src="images/ceg.png" alt="au_logo" width="200px" height="150px">
            </div>
            <div>
                <h2>DEPARTMENT OF INFORMATION SCIENCE AND TECHNOLOGY</h2>
            </div>
            <div>
                <img class="ist" src="images/ist.png" alt="ist_logo" width="200px" height="150px">
            </div>
        </section>
    </header>
    <nav class="navbar">
        <a href="home.py">Home</a><a id="sep" >--></a>
        <a href="student_main.py?id={Regno}">Student Details</a><a id="sep" >--></a>
        <a href="" >Semester 3</a>
    </nav>
    <h1 style=text-align:center;>Semester 3</h1>
    <h2 style=text-align:center;>Subject Details</h2>
    <div class="content">
        <form method="post" enctype="multipart/form-data">
            <table>
                <thead>
                    <tr>
                        <th>Subject</th>
                        <th>Code</th>
                        <th>Credit</th>
                        <th>Grade</th>
                        <th>if reappeared Year Passed</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><input type="text" name="subject1" placeholder="Enter Subject" value="{result[2]}" required></td>
                        <td><input type="text" name="code1" placeholder="Enter Code" value="{result[3]}" required></td>
                        <td><input type="number" name="credit1" placeholder="Enter credits" value="{result[4]}" required></td>
                        <td><input type="text" name="grade1" placeholder="Enter grade" value="{result[5]}" required></td>
                        <td><input type="date" name="year1" value="{result[6]}"></td>
                    </tr>
                    <tr>
                        <td><input type="text" name="subject2" placeholder="Enter Subject" value="{result[7]}" required></td>
                        <td><input type="text" name="code2" placeholder="Enter Code" value="{result[8]}" required></td>
                        <td><input type="number" name="credit2" placeholder="Enter credits" value="{result[9]}" required></td>
                        <td><input type="text" name="grade2" placeholder="Enter grade" value="{result[10]}" required></td>
                        <td><input type="date" name="year2" value="{result[11]}"></td>
                    </tr>
                    <tr>
                        <td><input type="text" name="subject3" placeholder="Enter Subject" value="{result[12]}" required></td>
                        <td><input type="text" name="code3" placeholder="Enter Code" value="{result[13]}" required></td>
                        <td><input type="number" name="credit3" placeholder="Enter credits" value="{result[14]}" required></td>
                        <td><input type="text" name="grade3" placeholder="Enter grade" value="{result[15]}" required></td>
                        <td><input type="date" name="year3" value="{result[16]}"></td>
                    </tr>
                    <tr>
                        <td><input type="text" name="subject4" placeholder="Enter Subject" value="{result[17]}" required></td>
                        <td><input type="text" name="code4" placeholder="Enter Code" value="{result[18]}" required></td>
                        <td><input type="number" name="credit4" placeholder="Enter credits" value="{result[19]}" required></td>
                        <td><input type="text" name="grade4" placeholder="Enter grade" value="{result[20]}" required></td>
                        <td><input type="date" name="year4" value="{result[21]}"></td>
                    </tr>
                    <tr>
                        <td><input type="text" name="subject5" placeholder="Enter Subject" value="{result[22]}" required></td>
                        <td><input type="text" name="code5" placeholder="Enter Code" value="{result[23]}" required></td>
                        <td><input type="number" name="credit5" placeholder="Enter credits" value="{result[24]}" required></td>
                        <td><input type="text" name="grade5" placeholder="Enter grade" value="{result[25]}" required></td>
                        <td><input type="date" name="year5" value="{result[26]}"></td>
                    </tr>
                    <tr>
                        <td><input type="text" name="subject6" placeholder="Enter Subject" value="{result[27]}" required></td>
                        <td><input type="text" name="code6" placeholder="Enter Code" value="{result[28]}" required></td>
                        <td><input type="number" name="credit6" placeholder="Enter credits" value="{result[29]}" required></td>
                        <td><input type="text" name="grade6" placeholder="Enter grade" value="{result[30]}" required></td>
                        <td><input type="date" name="year6" value="{result[31]}" ></td>
                    </tr>
                    <tr>
                        <td><input type="text" name="subject7" placeholder="Enter Subject" value="{result[32]}" required></td>
                        <td><input type="text" name="code7" placeholder="Enter Code" value="{result[33]}" required></td>
                        <td><input type="number" name="credit7" placeholder="Enter credits" value="{result[34]}" required></td>
                        <td><input type="text" name="grade7" placeholder="Enter grade" value="{result[35]}" required></td>
                        <td><input type="date" name="year7" value="{result[36]}"></td>
                    </tr>
                    <tr>
                        <td><input type="text" name="subject8" placeholder="Enter Subject" value="{result[37]}" required></td>
                        <td><input type="text" name="code8" placeholder="Enter Code" value="{result[38]}" required></td>
                        <td><input type="number" name="credit8" placeholder="Enter credits" value="{result[39]}" required></td>
                        <td><input type="text" name="grade8" placeholder="Enter grade" value="{result[40]}" required></td>
                        <td><input type="date" name="year8" value="{result[41]}"></td>
                    </tr>
                    <tr>
                        <td><input type="text" name="subject9" placeholder="Enter Subject" value="{result[42]}" ></td>
                        <td><input type="text" name="code9" placeholder="Enter Code" value="{result[43]}" ></td>
                        <td><input type="number" name="credit9" placeholder="Enter credits" value="{result[44]}" ></td>
                        <td><input type="text" name="grade9" placeholder="Enter grade" value="{result[45]}" ></td>
                        <td><input type="date" name="year9" value="{result[46]}"></td>
                    </tr>
                    <tr>
                        <td><input type="text" name="subject10" placeholder="Enter Subject" value="{result[47]}" ></td>
                        <td><input type="text" name="code10" placeholder="Enter Code" value="{result[48]}"></td>
                        <td><input type="number" name="credit10" placeholder="Enter credits" value="{result[49]}" ></td>
                        <td><input type="text" name="grade10" placeholder="Enter grade" value="{result[50]}" ></td>
                        <td><input type="date" name="year10" value="{result[51]}"></td>
                    </tr>
                </tbody>
            </table>
            <div class="summary">
                <label for="totalCredits">Total Credits:</label>
                <input type="number" id="totalCredits" name="totalCredits" value="{result[52]}" required>

                <label for="earnedCredits">Earned Credits:</label>
                <input type="number" id="earnedCredits" name="earnedCredits" value="{result[53]}" required>

                <label for="gpa">GPA:</label>
                <input type="number" step="0.01" id="gpa" name="gpa" value="{result[54]}" required>

                   <label for="marksheet">Marksheet :(eg:registerno.pdf)</label>
                <input type="file" id="marksheet" name="marksheet" accept=".pdf" value="{result[55]}" required>
            </div>
            <button type="submit" name="submit">Submit</button>
        </form>
    </div>
    <footer>

        <p><a href="https://www.instagram.com/yourdepartmentpage">
            <img src="images/instgram.jpeg" alt="instagram" width="30px" height="30px"></a>Follow in Instragram</p>
        <p>&copy; 2024 Information Technology. All rights reserved.</p>
    </footer>
</body>
</html>

""")

Subject1 = form.getvalue("subject1")
Code1 = form.getvalue("code1")
Credit1 = form.getvalue("credit1")
Grade1 = form.getvalue("grade1")
Year1 = form.getvalue("year1")

Subject2 = form.getvalue("subject2")
Code2 = form.getvalue("code2")
Credit2 = form.getvalue("credit2")
Grade2 = form.getvalue("grade2")
Year2 = form.getvalue("year2")

Subject3 = form.getvalue("subject3")
Code3 = form.getvalue("code3")
Credit3 = form.getvalue("credit3")
Grade3 = form.getvalue("grade3")
Year3 = form.getvalue("year3")

Subject4 = form.getvalue("subject4")
Code4 = form.getvalue("code4")
Credit4 = form.getvalue("credit4")
Grade4 = form.getvalue("grade4")
Year4 = form.getvalue("year4")

Subject5 = form.getvalue("subject5")
Code5 = form.getvalue("code5")
Credit5 = form.getvalue("credit5")
Grade5 = form.getvalue("grade5")
Year5 = form.getvalue("year5")

Subject6 = form.getvalue("subject6")
Code6 = form.getvalue("code6")
Credit6 = form.getvalue("credit6")
Grade6 = form.getvalue("grade6")
Year6 = form.getvalue("year6")

Subject7 = form.getvalue("subject7")
Code7 = form.getvalue("code7")
Credit7 = form.getvalue("credit7")
Grade7 = form.getvalue("grade7")
Year7 = form.getvalue("year7")

Subject8 = form.getvalue("subject8")
Code8 = form.getvalue("code8")
Credit8 = form.getvalue("credit8")
Grade8 = form.getvalue("grade8")
Year8 = form.getvalue("year8")

Subject9 = form.getvalue("subject9")
Code9 = form.getvalue("code9")
Credit9 = form.getvalue("credit9")
Grade9 = form.getvalue("grade9")
Year9 = form.getvalue("year9")

Subject10 = form.getvalue("subject10")
Code10 = form.getvalue("code10")
Credit10 = form.getvalue("credit10")
Grade10 = form.getvalue("grade10")
Year10 = form.getvalue("year10")

TotalCredits = form.getvalue("totalCredits")
EarnedCredits = form.getvalue("earnedCredits")
Gpa = form.getvalue("gpa")
Submit = form.getvalue("submit")

if Submit != None:
    q = """SELECT * FROM sem3 WHERE register_no='%s'""" % (Regno);
    cur.execute(q);
    res = cur.fetchone();
    if (res == None):
        Marksheet = form["marksheet"]
        # fn = os.path.basename(Marksheet.filename)
        # open("semester3_marksheet/" + fn, "wb").write(Marksheet.file.read())

        file_path = os.path.join("semester3_marksheet/", os.path.basename(Marksheet.filename))
        with open(file_path, "wb") as f:
            f.write(Marksheet.file.read())

        q = """INSERT INTO sem3(register_no,subject1,code1,credit1,grade1,reappear_passed_year1,subject2,code2,credit2,grade2,reappear_passed_year2,subject3,code3,credit3,grade3,reappear_passed_year3,subject4,code4,credit4,grade4,reappear_passed_year4,subject5,code5,credit5,grade5,reappear_passed_year5,subject6,code6,credit6,grade6,reappear_passed_year6,subject7,code7,credit7,grade7,reappear_passed_year7,subject8,code8,credit8,grade8,reappear_passed_year8,subject9,code9,credit9,grade9,reappear_passed_year9,subject10,code10,credit10,grade10,reappear_passed_year10,total_credits,earned_credits,gpa,marksheet,status,authorized)
             VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (
            Regno, Subject1, Code1, Credit1, Grade1, Year1, Subject2, Code2, Credit2, Grade2, Year2, Subject3, Code3,
            Credit3, Grade3, Year3, Subject4, Code4, Credit4, Grade4, Year4, Subject5, Code5, Credit5, Grade5, Year5,
            Subject6, Code6, Credit6, Grade6, Year6, Subject7, Code7, Credit7, Grade7, Year7, Subject8, Code8, Credit8,
            Grade8, Year8, Subject9, Code9, Credit9, Grade9, Year9, Subject10, Code10, Credit10, Grade10, Year10,
            TotalCredits, EarnedCredits, Gpa, file_path, "LOCK","NO")
        cur.execute(q)
        con.commit()

        print("""
            <script>
             alert("Semester 3 Form Filled Successfully !");
             location.href='student_main.py?id=%s'
            </script>    
            """ % Regno)
    if (res != None):
        Marksheet = form["marksheet"]
        # fn = os.path.basename(Marksheet.filename)
        # open("semester1_marksheet/" + fn, "wb").write(Marksheet.file.read())

        file_path = os.path.join("semester3_marksheet/", os.path.basename(Marksheet.filename))
        with open(file_path, "wb") as f:
            f.write(Marksheet.file.read())

        q = """UPDATE sem3 SET subject1='%s',code1='%s',credit1='%s',grade1='%s',reappear_passed_year1='%s',subject2='%s',code2='%s',credit2='%s',grade2='%s',reappear_passed_year2='%s',subject3='%s',code3='%s',credit3='%s',grade3='%s',reappear_passed_year3='%s',subject4='%s',code4='%s',credit4='%s',grade4='%s',reappear_passed_year4='%s',subject5='%s',code5='%s',credit5='%s',grade5='%s',reappear_passed_year5='%s',subject6='%s',code6='%s',credit6='%s',grade6='%s',
        reappear_passed_year6='%s',subject7='%s',code7='%s',credit7='%s',grade7='%s',reappear_passed_year7='%s',subject8='%s',code8='%s',credit8='%s',grade8='%s',reappear_passed_year8='%s',subject9='%s',code9='%s',credit9='%s',grade9='%s',reappear_passed_year9='%s',subject10='%s',code10='%s',credit10='%s',grade10='%s',reappear_passed_year10='%s',total_credits='%s',earned_credits='%s',gpa='%s',marksheet='%s',status='%s' WHERE register_no='%s'""" % (
        Subject1, Code1, Credit1, Grade1, Year1, Subject2, Code2, Credit2, Grade2, Year2, Subject3, Code3,
        Credit3, Grade3, Year3, Subject4, Code4, Credit4, Grade4, Year4, Subject5, Code5, Credit5, Grade5, Year5,
        Subject6, Code6, Credit6, Grade6, Year6, Subject7, Code7, Credit7, Grade7, Year7, Subject8, Code8, Credit8,
        Grade8, Year8, Subject9, Code9, Credit9, Grade9, Year9, Subject10, Code10, Credit10, Grade10, Year10,
        TotalCredits, EarnedCredits, Gpa, file_path, "LOCK", Regno)

        cur.execute(q)
        con.commit()

        print("""
                    <script>
                     alert("Semester 3 Form Updates Successfully !");
                     location.href='student_main.py?id=%s'
                    </script>    
                    """ % Regno)





