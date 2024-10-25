#!C:/Python/python.exe
import pymysql
import cgitb
import cgi
import os
import random
import pandas as pd
import smtplib
import json

print("Content-type: text/html\r\n\r\n")
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="summer_project")
cur = con.cursor()


def insert_data_to_db(data):
    try:
        query = "INSERT INTO batch_details (batch,register_no,name,phoneno,email,facultyadvisor,staffid) VALUES (%s,%s, %s, %s, %s, %s, %s)"
        q = "INSERT INTO student_login(username,password) VALUES (%s, %s)"

        for index, row in data.iterrows():
            cur.execute(query,
                        (Batch, row['REGNO'], row['NAME'], row['PHONE NO'], row['EMAIL ID'], row['FACULTY ADVISOR'],row['STAFF ID']))
            Randno = random.randint(10000000, 99999999)
            cur.execute(q, (row['REGNO'], Randno))

            fromaddress = 'mahimasj5868@gmail.com'
            ppassword = 'nbqo izhq vsyp cair'
            toaddress = row['EMAIL ID']
            subject = "Message From DEPARTMENT OF INFORMATION SCIENCE AND TECHNOLOGY!"
            body = "Hello {},\n\nYour Registration process of IST STUDENT RECORD Successfully Completed!\n\nYour Username and Password is Given Below:\n\nUsername: {}\nPassword: {}".format(
                row['NAME'], row['REGNO'], Randno)
            msg = "Subject: {}\n\n{}".format(subject, body)
            server = smtplib.SMTP("smtp.gmail.com:587")
            server.starttls()
            server.login(fromaddress, ppassword)
            server.sendmail(fromaddress, toaddress, msg)
            server.quit()
        con.commit()
        return True, None
    except Exception as e:
        return False, str(e)


print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Dashboard</title>
    <link rel="icon" href="images/ist.png">
    <link rel="stylesheet" href="dashboard.css">
    <script defer src="dashboard.js"></script>
</head>
<body>
    <header class="header">
        <h1>Admin Dashboard</h1>
    </header>
    <div class="sidebar">
        <button onclick="showSection('batchSection')">Batch Information</button>
        <button onclick="showSection('staffSection')">Staff Registration</button>
        <button onclick="showSection('analysisSection')">Batch Analysis</button>
        <button><a href="https://1drv.ms/x/c/629f9c16aa1c4346/ESERzW9sYy1ItckK4gyjd8YBv_2FkzEnfHOZvK4p-Gdifw?e=1xvMGa" style="text-decoration:none;color:white">Sample Excel</a></button>
    </div>
    <main class="main-content">
        <section id="batchSection" class="form-container">
            <h2>Upload Batch Information</h2>
            <form id="uploadForm" action="" method="post" enctype="multipart/form-data">
                <div class="form-group">
                    <label for="batch">Batch:</label>
                    <select name="batch" id="batch" required>
                        <!-- Options will be populated by JavaScript -->
                    </select>
                </div>
                <div class="form-group">
                    <label for="file">Upload Excel File:</label>
                    <input type="file" name="file" id="file" accept=".xlsx, .xls" required>
                </div>
                <div class="form-group">
                    <button type="submit" name="submit">Upload</button>
                </div>
            </form>
        </section>
        <section id="staffSection" class="form-container" style="display: none;">
            <h2>Staff Registration</h2>
            <form id="staffForm" action="" method="post" enctype="multipart/form-data">
                <div class="form-group">
                    <label for="staffid">Staff ID:</label>
                    <input type="text" name="staffid" id="staffid" required>
                </div>
                <div class="form-group">
                    <label for="staffname">Name:</label>
                    <input type="text" name="staffname" id="staffname" required>
                </div>
                <div class="form-group">
                    <label for="phoneno">Phone No:</label>
                    <input type="tel" name="phoneno" id="phoneno" required>
                </div>
                <div class="form-group">
                    <label for="email">Email:</label>
                    <input type="email" name="email" id="email" required>
                </div>
                <div class="form-group">
                    <label for="photo">Photo:</label>
                    <input type="file" name="photo" id="photo" accept=".jpeg, .png, .jpg" required>
                </div>
                <div class="form-group">
                    <button type="submit" name="register">Register</button>
                </div>
            </form>
        </section>
        <section id="batchSection" class="form-container">
            <h2>Batch Analysis:</h2>
            <form id="uploadForm" action="" method="post" enctype="multipart/form-data">
                <div class="form-group">
                    <label for="batchanalyse">Batch:</label>
                    <input type="text" name="batchanalyse" id="batchanalyse" placeholder="Enter batch (eg: 2026)" >
                </div>
                <div class="form-group">
                    <button type="submit" name="analyse">Analyse</button>
                </div>
            </form>
        </section>
    </main>
</body>
</html>
""")

form = cgi.FieldStorage()
Batch = form.getvalue("batch")
Submit = form.getvalue("submit")
Register = form.getvalue("register")
staffid = form.getvalue("staffid")
staffname = form.getvalue("staffname")
phoneno = form.getvalue("phoneno")
email = form.getvalue("email")
analyse=form.getvalue("analyse")


if Submit is not None:
    q = "SELECT * FROM batch_details WHERE batch='%s'" % (Batch)
    cur.execute(q)
    res = cur.fetchone()

    if res is None:
        file_item = form['file']

        if file_item.filename:
            fn = os.path.basename(file_item.filename)
            file_path = os.path.join("excel", fn)

            with open(file_path, 'wb') as f:
                f.write(file_item.file.read())

            try:
                record = pd.read_excel(file_path)
                success, error = insert_data_to_db(record)
                if success:
                    print(
                        f"""<script>alert("Successfully uploaded batch {Batch} details and processed the file: {fn}")</script>""")
                else:
                    print(f"""<script>alert("Error inserting data into the database: {error}")</script>""")
            except Exception as e:
                print(f"""<script>alert("Error reading the file: {e}")</script>""")
        else:
            print("<p>No file was uploaded</p>")
    else:
        print(f"""<script>alert("Batch {Batch} details already feeded!");</script>""")

if Register is not None:

    photo = form["photo"]
    fn = os.path.basename(photo.filename)
    open("staff_photos/" + fn, "wb").write(photo.file.read())

    try:
        query = "INSERT INTO staff_details (staffid, staff_name, phoneno, email_id, photo) VALUES (%s, %s, %s, %s, %s)"
        cur.execute(query, (staffid, staffname, phoneno, email, fn))  # Use filename here

        q = "INSERT INTO staff_login(username, password) VALUES (%s, %s)"
        Randnumber = random.randint(10000000, 99999999)
        cur.execute(q, (staffid, Randnumber))

        fromaddress = 'mahimasj5868@gmail.com'
        ppassword = 'nbqo izhq vsyp cair'
        toaddress = email
        subject = "Message From DEPARTMENT OF INFORMATION SCIENCE AND TECHNOLOGY!"
        body = "Hello {},\n\nYour Registration process of IST STUDENT RECORD Successfully Completed!\n\nYour Username and Password is Given Below:\n\nUsername: {}\nPassword: {}".format(
            staffname, staffid, Randnumber)
        msg = "Subject: {}\n\n{}".format(subject, body)

        server = smtplib.SMTP("smtp.gmail.com:587")
        server.starttls()
        server.login(fromaddress, ppassword)
        server.sendmail(fromaddress, toaddress, msg)
        server.quit()

        con.commit()
        print(f"""<script>alert("Successfully registered staff: {staffname}")</script>""")
    except Exception as e:
        print(f"""<script>alert("Error inserting staff data: {e}")</script>""")
    finally:
        cur.close()
        con.close()

if analyse is not None :
    batch = form.getvalue("batchanalyse")
    #
    # # Fetch the list of students for the given batch and staff
    # cur.execute("SELECT register_no FROM batch_details WHERE batch=%s", (batch))
    # students = cur.fetchall()
    #
    # total_students = len(students)
    # arrear_students = 0
    #
    # # List of semester tables to check
    # semesters = ['sem1', 'sem2', 'sem3', 'sem4', 'sem5', 'sem6', 'sem7', 'sem8']
    #
    # for student in students:
    #     register_no = student[0]
    #     has_arrear = False
    #
    #     # Check each semester for arrear ('U' grade)
    #     for semester in semesters:
    #         query = f"SELECT grade1, grade2, grade3, grade4, grade5, grade6, grade7, grade8, grade9, grade10 FROM {semester} WHERE register_no=%s"
    #         cur.execute(query, (register_no,))
    #         grades = cur.fetchone()
    #
    #         if grades:
    #             # If any grade is 'U', mark student as having arrear
    #             if 'U' in grades:
    #                 has_arrear = True
    #                 break
    #
    #     if has_arrear:
    #         arrear_students += 1
    #
    # # Calculate percentages
    # if total_students > 0:
    #     pass_percentage = ((total_students - arrear_students) / total_students) * 100
    #     arrear_percentage = (arrear_students / total_students) * 100
    # else:
    #     pass_percentage = arrear_percentage = 0
    #
    #
    #
    # # Data to be used in the chart
    # data = {
    #     'labels': ['Pass Percentage', 'Arrear Percentage'],
    #     'datasets': [{
    #         'data': [pass_percentage, arrear_percentage],
    #         'backgroundColor': ['#4CAF50', '#FF6347']
    #     }]
    # }
    #
    # # HTML and JS for displaying the chart
    # print(f"""
    # <!DOCTYPE html>
    # <html lang="en">
    # <head>
    #     <meta charset="UTF-8">
    #     <meta name="viewport" content="width=device-width, initial-scale=1.0">
    #     <title>Batch Analysis</title>
    #     <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    #     <style>
    #
    #         .chart-container {{
    #             width: 30%;
    #             margin: 0 auto;
    #         }}
    #     </style>
    # </head>
    # <body>
    #     <h1>Batch Analysis for {batch}</h1>
    #     <div class="chart-container">
    #         <canvas id="batchAnalysisChart"></canvas>
    #     </div>
    #     <script>
    #         const data = {json.dumps(data)};
    #         const config = {{
    #             type: 'pie',
    #             data: data,
    #             options: {{
    #                 responsive: true,
    #                 plugins: {{
    #                     legend: {{
    #                         position: 'top',
    #                     }},
    #                     tooltip: {{
    #                         callbacks: {{
    #                             label: function(tooltipItem) {{
    #                                 return tooltipItem.label + ': ' + tooltipItem.raw.toFixed(2) + '%';
    #                             }}
    #                         }}
    #                     }}
    #                 }}
    #             }}
    #         }};
    #
    #         const myChart = new Chart(
    #             document.getElementById('batchAnalysisChart'),
    #             config
    #         );
    #     </script>
    # """)
    # cur.close()
    # con.close()

    print(f"""
        <script>
        location.href='overall_analysis.py?batch={batch}';
        </script>
        """)

