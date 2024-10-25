#!C:/Python/python.exe
import pymysql, cgitb, cgi, os

print("Content-type: text/html\r\n\r\n")
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="summer_project")
cur = con.cursor()


form=cgi.FieldStorage()
Regno=form.getvalue("id")

q="""SELECT * FROM batch_details WHERE register_no='%s'"""%(Regno)
cur.execute(q)
res=cur.fetchone()

Name=res[3]
Phoneno=res[4]
EmailId=res[5]
FacultyName=res[6]


print("""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IST STUDENT RECORD</title>
    <link rel="icon" href="images/ist.png">
    <link rel="stylesheet" href="studentstyle.css">
    <style>
    
    body {
    font-family: 'Merriweather', serif; /* A more formal serif font */
    word-spacing: 0.3rem;
    line-height: 1.8rem;
    margin: 0;
    background-color: #F4F4F9; /* A soft, neutral background */
}

.header {
    background-color: rgb(36, 36, 87); /* Deep, formal blue-gray */
    color: white;
    display: flex;
    align-items: center;
    padding: 10px 15px;
    width: 100%;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.header img {
    height: 50px;
    margin-right: 20px;
}

.header h2 {
    color: white;
    font-size: 25px; /* Formal, slightly larger text */
}

.wrapper {
    display: flex;
    flex: 1;
    flex-direction: column;
}

.content {
    padding: 40px;
    flex-grow: 1;
    //margin-top: 30px;
    margin-bottom: 80px; /* Ensure space for footer */
    background-color: white; /* Clean white background for content */
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    border-radius: 10px;
}

h1, h2 {
    color: #2C3E50; /* Consistent, formal text color */
}

h1 {
    font-size: 48px;
    margin-bottom: 30px;
    font-weight: 700; /* Bold and prominent */
}

h2 {
    font-size: 20px;
    margin-bottom: 20px;
    font-weight: 600; /* Slightly bold for emphasis */
}

.text {
    background-color: #ECEFF1; /* Light gray for contrast */
    border: 1px solid #CFD8DC; /* Subtle border */
    border-radius: 8px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    padding: 25px;
    color: #37474F; /* Deep gray text */
    text-align: center;
    font-family: 'Merriweather', serif;
    font-size: 20px;
}

form {
    max-width: 800px;
    margin: 0 auto;
    padding: 30px;
    background-color: white;
    border: 1px solid #DADFE1; /* Light gray border for a formal look */
    border-radius: 12px;
    box-shadow: 0 5px 25px rgba(0, 0, 0, 0.15);
    font-size: 18px;
    line-height: 1.8;
    display: flex;
    flex-direction: column;
    gap: 30px;
    color: #2C3E50;
}

.form-group {
    display: flex;
    flex-direction: column;
    margin-bottom: 5px;
    gap: 5px;
}

.form-group label {
    font-weight: 500;
    color: #2C3E50;
    text-align: left;
    font-size: 18px;
}

.form-group input, .form-group select {
    padding: 5spx;
    box-sizing: border-box;
    border: 1px solid #BDC3C7;
    background-color: #FAFAFA;
    color: #2C3E50;
    transition: border 0.3s, box-shadow 0.3s;
    font-size: 15px;
    width: 100%;
    border-radius: 8px;
}

.form-group input:focus, .form-group select:focus {
    border: 1px solid #2980B9;
    box-shadow: 0 0 8px rgba(41, 128, 185, 0.4); /* Soft focus shadow */
    outline: none;
}

.form-group textarea {
    padding: 15px;
    box-sizing: border-box;
    border: 1px solid #BDC3C7;
    border-radius: 8px;
    background-color: #FAFAFA;
    color: #2C3E50;
    transition: border 0.3s, box-shadow 0.3s;
    resize: vertical;
    min-height: 140px;
}

.form-group textarea:focus {
    border: 1px solid #2980B9;
    box-shadow: 0 0 8px rgba(41, 128, 185, 0.4);
    outline: none;
}

.design {
    display: flex;
    flex-wrap: wrap;
    gap: 10px; /* Reduced gap to 10px */
}

.design .form-group {
    flex: 1 1 calc(50% - 25px);
    min-width: 320px;
    margin-bottom:0px; /* Adjusted margin for better spacing */
}

button {
    padding: 15px ;
    background-color: rgb(36, 36, 87);
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 20px;
    font-weight: 600;
    cursor: pointer;
    transition: background-color 0.3s, box-shadow 0.3s;
}

button:hover {
    background-color: #21618C;
    box-shadow: 0 3px 15px rgba(0, 0, 0, 0.2); /* Added shadow on hover */
}

footer {
    text-align: center;
    padding: 2px;
    background-color:rgb(36, 36, 87); /* Darker footer for a formal look */
    color: #ECF0F1;
    width: 100%;
    box-shadow: 0 -4px 12px rgba(0, 0, 0, 0.1);
    font-size: 18px;
    position: relative;
    bottom: 0; /* Ensure it stays at the bottom */
}

footer a {
    color: #AED6F1;
    text-decoration: none;
}

footer a:hover {
    text-decoration: underline;
}

@media (max-width: 600px) {
    .header img {
        height: 40px;
    }

    .content {
        padding: 20px;
    }

    form {
        gap: 20px;
    }

    form button {
        padding: 12px 20px;
        font-size: 18px;
    }

    h1 {
        font-size: 40px;
    }

    h2 {
        font-size: 28px;
    }
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
        <a href="" >Personal Details</a>
    </nav>
    <div class="wrapper"> <!-- Added wrapper for flex layout -->
      
        <div class="wrapper">
        <div class="content">
            <h1 style="text-align:center">Student Information </h1>
            <form method="post" enctype="multipart/form-data">
                <h2 class="text">
                 <img src="images/std.png" alt="HTML tutorial" style="width:42px;height:42px;">
                     Student Details</h2>
                Student Details</h2>
                <div class="form-group">
                    <label for="photo">Photo:</label>
                    <input type="file" id="photo" name="photo" accept=".jpeg, .png, .jpg" required>
                </div>
                
                <div class="design">
                <div class="form-group">
                    <label for="name">Name:</label>
                    <input type="text" id="name" name="name" value="{Name}" readonly>
                </div>
            
                <div class="form-group">
                    <label for="regno">Register Number:</label>
                    <input type="text" id="regno" name="regno" value="{Regno}" readonly>
                </div>
                </div>
                 <div class="form-group">
                    <label for="phoneno">Phone Number:</label>
                    <input type="tel" id="phoneno" name="phoneno" value="{Phoneno}" readonly>
                </div>
            
                <div class="form-group">
                    <label for="email">Email ID:</label>
                    <input type="email" id="email" name="email" value="{EmailId}" readonly>
                </div>
            
                <div class="design">
                <div class="form-group">
                    <label for="dob">Date of Birth:</label>
                    <input type="date" id="dob" name="dob" required>
                </div>
            
                <div class="form-group">
                    <label for="sex">Sex:</label>
                    <select id="sex" name="sex" required>
                        <option value="male">Male</option>
                        <option value="female">Female</option>
                        <option value="other">Other</option>
                    </select>
                </div>
                </div>
                
                <div class="design">
                <div class="form-group">
                    <label for="bloodgroup">Blood Group:</label>
                    <input type="text" id="bloodgroup" name="bloodgroup" required>
                </div>
            
                <div class="form-group">
                    <label for="community">Community:</label>
                    <input type="text" id="community" name="community" required>
                </div>
                </div>
                
                <div class="design">
                <div class="form-group">
                    <label for="cutoff">Cutoff:</label>
                    <input type="number" id="cutoff" name="cutoff" required>
                </div>
            
                <div class="form-group"> 
                    <label for="admitted">Admitted On:</label>
                    <input type="date" id="admitted" name="admitted" required>
                </div>
               </div>
               
                <div class="form-group">
                    <label for="specialcategory">Special Category:</label>
                    <input type="text" id="specialcategory" name="specialcategory">
                </div>
                
                <div class="design">
                <div class="form-group">
                    <label for="scholarship">Scholarship:</label>
                    <input type="text" id="scholarship" name="scholarship">
                </div>
            
                <div class="form-group">
                    <label for="volunteer">Volunteer:</label>
                    <input type="text" id="volunteer" name="volunteer">
                </div>
                </div>
                
                <div class="form-group">
                    <label for="hosteller">Hosteller/Day Scholar:</label>
                    <input type="text" id="hosteller" name="hosteller">
                </div>
            
               
                <h2 class="text">
                <img src="images/teacher.png" alt="HTML tutorial" style="width:42px;height:42px;"></img>
                Faculty Details</h2>
            
                <div class="form-group">
                    <label for="facultyname">Faculty Name:</label>
                    <input type="text" id="facultyname" name="facultyname" value="{FacultyName}" readonly>
                </div>
            
                <h2 class="text">
                 <img src="images/parent.png" alt="HTML tutorial" style="width:42px;height:42px;"></img>
                Parent Details</h2>
                Parent Details</h2>
                 
                <div class="design"> 
                <div class="form-group">
                    <label for="dadname">Father's Name:</label>
                    <input type="text" id="dadname" name="dadname" required>
                </div>
            
                <div class="form-group">
                    <label for="dadoccupation">Father's Occupation:</label>
                    <input type="text" id="dadoccupation" name="dadoccupation" required>
                </div>
                </div>
                
                
                <div class="form-group">
                    <label for="dadincome">Father's Annual Income:</label>
                    <input type="number" id="dadincome" name="dadincome" required>
                </div>
                <div class="form-group">
                    <label for="fatherphoneno">Father's Phone Number:</label>
                    <input type="tel" id="fatherphoneno" name="fatherphoneno" required>
                </div>
                
             <div class="design"> 
                <div class="form-group">
                    <label for="momname">Mother's Name:</label>
                    <input type="text" id="momname" name="momname" required>
                </div>
            
                <div class="form-group">
                    <label for="momoccupation">Mother's Occupation:</label>
                    <input type="text" id="momoccupation" name="momoccupation" required>
                </div>
                </div>
                
            
                <div class="form-group">
                    <label for="momincome">Mother's Annual Income:</label>
                    <input type="number" id="momincome" name="momincome" required>
                </div>
                <div class="form-group">
                    <label for="motherphoneno">Mother's Phone Number:</label>
                    <input type="tel" id="motherphoneno" name="motherphoneno" required>
                </div>
                <div class="form-group">
                    <label for="currentaddress">Current Address:</label>
                    <textarea id="currentaddress" name="currentaddress" rows="4" required></textarea>
                </div>
                 <div class="form-group">
                    <label for="permanentaddress">Permanent Address:</label>
                    <textarea id="permanentaddress" name="permanentaddress" rows="4" required></textarea>
                </div>
                
                 <div class="design"> 
                <div class="form-group">
                    <label for="guardianaddress">Local Guardian's Address:</label>
                    <textarea id="guardianaddress" name="guardianaddress" rows="4" required></textarea>
                </div>
                
                <div class="form-group">
                    <label for="guardianphoneno">Guardian's Phone Number:</label>
                    <input type="tel" id="guardianphoneno" name="guardianphoneno" required>
                </div>
                </div>
                
                <div class="form-group">
                    <label for="guardianemail">Guardian's Email ID:</label>
                    <input type="email" id="guardianemail" name="guardianemail" required>
                </div>
                <div>
                     <label for="tenthmarksheet">10th Marksheet :(eg:registerno.pdf)</label>
                    <input type="file" id="tenthmarksheet" name="tenthmarksheet" accept=".pdf" required>
                </div>
                <div>
                     <label for="twelthmarksheet">12th Marksheet :(eg:registerno.pdf)</label>
                    <input type="file" id="twelthmarksheet" name="twelthmarksheet" accept=".pdf" required>
                </div>
                <button type="submit" name="submit">Submit</button>

            </form>            
        </div>
    </div>
   
    <footer>
        
        <p>&copy; 2024 Information Technology. All rights reserved.</p>
    </footer>
</body>
</html>

""")

#
# Name=form.getvalue("name")
# Regno=form.getvalue("regno")
Dob=form.getvalue("dob")
Sex=form.getvalue("sex")
BloodGroup=form.getvalue("bloodgroup")
Community=form.getvalue("community")
Cutoff=form.getvalue("cutoff")
AdmittedOn=form.getvalue("admitted")
SpecialCategory=form.getvalue("specialcategory")
Scholarship=form.getvalue("scholarship")
Volunteer=form.getvalue("volunteer")
Stay=form.getvalue("hosteller")
# Phoneno=form.getvalue("phoneno")
# EmailId=form.getvalue("email")
# FacultyName=form.getvalue("facultyname")
FatherName=form.getvalue("dadname")
FatherOccupation=form.getvalue("dadoccupation")
FatherIncome=form.getvalue("dadincome")
FatherPhoneno=form.getvalue("fatherphoneno")
MotherName=form.getvalue("momname")
MotherOccupation=form.getvalue("momoccupation")
MotherIncome=form.getvalue("momincome")
MotherPhoneno=form.getvalue("motherphoneno")
CurrentAddress=form.getvalue("currentaddress")
PermanentAddress=form.getvalue("permanentaddress")
GuardianAddress=form.getvalue("guardianaddress")
GuardianPhoneno=form.getvalue("guardianphoneno")
GuardianEmailId=form.getvalue("guardianemail")
Submit=form.getvalue("submit")


if Submit != None :
    import os
    import pymysql

    if Submit is not None:
        # Retrieve and save the uploaded photo
        Photo = form["photo"]
        fn = os.path.basename(Photo.filename)

        # Save the photo file in the specified directory
        with open("photos/" + fn, "wb") as f:
            f.write(Photo.file.read())

        Marksheet1 = form["tenthmarksheet"]

        file_path = os.path.join("tenth_marksheet/", os.path.basename(Marksheet1.filename))
        with open(file_path, "wb") as f:
            f.write(Marksheet1.file.read())

        Marksheet2 = form["twelthmarksheet"]

        file_path = os.path.join("twelth_marksheet/", os.path.basename(Marksheet2.filename))
        with open(file_path, "wb") as f:
            f.write(Marksheet2.file.read())

        # Prepare the SQL query using parameterized format
        q = """
            INSERT INTO student_details (
                photo, name, register_no, dob, sex, blood_group, community, cutoff, 
                admitted_on, special_category, scholarship, volunteer, hosteller_dayscholar,
                phone_no, email_id, faculty_name, father_name, father_occupation, father_income,father_phone_no,
                mother_name, mother_occupation, mother_income,mother_phone_no, current_address,permanent_address, guardian_address,
                guardian_phone_no, guardian_email_id,10th_marksheet,12th_marksheet
            ) VALUES (%s,%s,%s,%s,%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # Gather the form data into a tuple
        values = (
            fn, Name, Regno, Dob, Sex, BloodGroup, Community, Cutoff, AdmittedOn,
            SpecialCategory, Scholarship, Volunteer, Stay, Phoneno, EmailId,
            FacultyName, FatherName, FatherOccupation, FatherIncome,FatherPhoneno,MotherName,
            MotherOccupation, MotherIncome,MotherPhoneno, CurrentAddress,PermanentAddress, GuardianAddress, GuardianPhoneno,
            GuardianEmailId,Marksheet1,Marksheet2
        )

        # Execute the query with parameterized values
        cur.execute(q, values)
        con.commit()

        # Success alert and redirection
        print(f"""
        <script>
        alert("Personal details filled Successfully !!");
        location.href="student_main.py?id={Regno}";
        </script>
        """)

    # Photo = form["photo"]
    # fn = os.path.basename(Photo.filename)
    # open("photos/" + fn, "wb").write(Photo.file.read())
    #
    # q="""INSERT INTO student_details(photo,name,register_no,dob,sex,blood_group,community,cutoff,admitted_on,special_category,scholarship,volunteer,hosteller_dayscholar,phone_no,email_id,faculty_name,father_name,father_occupation,father_income,mother_name,mother_occupation,mother_income,address,guardian_address,guardian_phone_no,guardian_email_id) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""%(Photo,Name,Regno,Dob,Sex,BloodGroup,Community,Cutoff,AdmittedOn,SpecialCategory,Scholarship,Volunteer,Stay,Phoneno,EmailId,FacultyName,FatherName,FatherOccupation,FatherIncome,MotherName,MotherOccupation,MotherIncome,Address,GuardianAddress,GuardianPhoneno,GuardianEmailId)
    # cur.execute(q)
    # con.commit()
    # # q = """INSERT INTO student_details(
    # #     photo, name, register_no, dob, sex, blood_group, community, cutoff,
    # #     admitted_on, special_category, scholarship, volunteer, hosteller_dayscholar,
    # #     phone_no, email_id, faculty_name, father_name, father_occupation,
    # #     father_income, mother_name, mother_occupation, mother_income,
    # #     address, guardian_address, guardian_phone_no, guardian_email_id
    # # ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    # #
    # # values = (Photo, Name, Regno, Dob, Sex, BloodGroup, Community, Cutoff, AdmittedOn,
    # #           SpecialCategory, Scholarship, Volunteer, Stay, Phoneno, EmailId,
    # #           FacultyName, FatherName, FatherOccupation, FatherIncome, MotherName,
    # #           MotherOccupation, MotherIncome, Address, GuardianAddress, GuardianPhoneno,
    # #           GuardianEmailId)
    # #
    # # cur.execute(q, values)
    #
    # print("""
    # <script>
    # alert("Personal details filled Successfully !!");
    # location.href="student_main.py?id=%s";
    # </script>
    # """%Regno)