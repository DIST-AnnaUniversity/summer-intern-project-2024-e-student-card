#!C:/Python/python.exe
import pymysql, cgitb, cgi, os

print("Content-type: text/html\r\n\r\n")
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="summer_project")
cur = con.cursor()

print("""
    <!DOCTYPE html>
<html>
    <head>
        <title>IST STUDENT RECORD</title>
        <meta name="view-port"  content="width=device-width;initial=1.0">
        <link rel="icon" href="images/ist.png">
        <link rel="stylesheet" href="home.css" type="text/css">
        <style>
            .nav div a:hover, .dropdown:hover .dropbtn {
    background-color: red;
    color: white;
}

.dropdown {
    position: relative;
    display: inline-block; 
}


.dropdown-content {
    display: none;
    position: absolute;
    background-color: #f9f9f9;
    min-width: 130px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 1;
}

.dropdown-content a {
    color: black;
    padding: 12px 10px;
    text-decoration: none;
    display: none;
}

.dropdown-content a:active{
    background-color: red;
    color: white;
}

.dropdown-content a:hover {
    background-color: red;
}

.dropdown:hover .dropdown-content a {
    display: block;
}

        </style>
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
        <nav>
            <section class="nav">
                <div><a href="home.py">Home</a></div>
                <div><a href="#about">About</a></div>
                <div><a href="#services">Services</a></div>
                <div><a href="#contact">Contact</a></div>
               <div class="dropdown">
                    <a href="" style="color:white">Login</a>
                    <div class="dropdown-content">
                        <a href="student_login.py">Student</a>
                        <a href="staff_login.py">Staff</a>
                        <a href="admin_login.py">Admin</a>
                    </div>
                </div>
                <div><a href="feedback.py">Feedback</a></div>
            </section>
        </nav>
        <article>
            <section class="about" id="about">
                    <div class="vision">
                        <img src="images/dept.jpeg" alt="ist dept" width="200px" height="150px"> 
                        <h1>OUR VISION :</h1>
                        <p>To educate students with conceptual knowledge and technical skills in the field of Information Technology with moral and ethical values to achieve excellence in academic, industry and research centric environments.</p>
                    </div>
                    <div class="mission">
                        <img src="images/dept.jpeg" alt="ist dept" width="200px" height="150px"> 
                        <h1>OUR MISSION :</h1>
                        <p>To inculcate in students a firm foundation in theory and practice of IT skills coupled with the thought process for disruptive innovation and research methodologies, to keep pace with emerging technologies. To provide a conducive environment for all academic, administrative, and interdisciplinary research activities using state-of-the-art technologies. To stimulate the growth of graduates and doctorates, who will enter the workforce as productive IT engineers, researchers, and entrepreneurs with necessary soft skills, and continue higher professional education with competence in the global market. To enable seamless collaboration with the IT industry and Government for consultancy and sponsored research. To cater to cross-cultural, multinational, and demographic diversity of students. To educate the students on the social, ethical, and moral values needed to make significant contributions to society.</p>
                    </div>
            </section>
            <h1 class="servi"> OUR SERVICES !!</h1>
            <section class="services" id="services">
                <!-- <h1 class="servi"> OUR SERVICES !!</h1> -->
                <div class="student">
                    <figure>
                        <a href="student_login.py"><img src="images/student.jpeg" alt="student" width="200px" height="150px"></a>
                        <figcaption><a href="student_login.py">Student Section</a></figcaption>
                    </figure>
                </div>
                <div class="staff">
                    <figure>
                        <a href="staff_login.py"><img src="images/staff.png" alt="staff" width="200px" height="150px"></a>
                        <figcaption><a href="staff_login.py">Staff Section</a></figcaption>
                    </figure>
                </div>
            </section>
            <section class="contact" id="contact">
                <div class="con-info">
                    <h2>Contact Us</h2><br>
                    <p>Email Id:ista@auist.net <br>
                    Phone No:044-22358812 </p>
                </div>
                <div class="links">
                <div>
                    <a href="https://www.instagram.com/ista__ceg/"><img src="images/instgram.jpeg" alt="instgram" width="200px" height="150px"></a>
                    <p><a href="https://www.instagram.com/ista__ceg/">https://www.instagram.com/ista__ceg/</a></p>
                </div>
                <div>
                    <a href="ista@auist.net"><img src="images/mail.jpeg" alt="mail" width="200px" height="150px"></a>
                    <p><a href="ista@auist.net">ista@auist.net</a></p>
                </div>
                <div>
                    <a href="https://www.linkedin.com/company/ista-ceg/mycompany/"><img src="images/linkedin.png" alt="linkedin" width="200px" height="150px"></a>
                    <p><a href="https://www.linkedin.com/company/ista-ceg/mycompany/">https://www.linkedin.com/company/ista-ceg/mycompany/</a></p>
                </div>
                </div>
            </section>
        </article>
        <footer>
            <section class="footer">
                <p>&copy;2024 , IST DEPT</p>
            </section>
        </footer>
    </body>
</html>
""")
