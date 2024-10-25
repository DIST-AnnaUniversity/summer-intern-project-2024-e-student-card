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
     body {
        font-family: Arial, sans-serif;
        background-color: #fbfdfd;
        margin: 0;
        padding: 0;
        display: flex;
        flex-direction: column;
        align-items: center;
        min-height: 100vh;
        overflow-x: hidden; /* Prevent horizontal scrolling */
        overflow-y: auto;
        position: relative;
    }

    .header {
        background-color: rgb(36, 36, 87);
        color: white;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 20px;
        width: 100%;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        position: relative;
        top: 0;
        left: 0;
        z-index: 1000;
    }

    .header h1 {
        color: white;
    }

    .header img {
        height: 60px;
    }

    .header p {
        flex-grow: 1;
        margin: 0;
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

    .main-content {
        padding-top: 100px; /* Adjusted padding to avoid overlap with fixed header */
        width: 100%;
        justify-content: center;
    }

    .container {
        width: 100%;
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
        font-size: 20px;
        padding-bottom: 100px;
        font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
    }
    table {
    width: 100%;
    border-collapse: collapse; /* Ensure borders are merged */
    margin-bottom: 20px;
}

th, td {
    padding: 10px;
    text-align: left;
    border: 1px solid #ddd; /* Add border to cells */
}

th {
    background-color: #f2f2f2;
    border-bottom: 2px solid #0a2949; /* Add border to the bottom of header cells */
}

td {
    border-bottom: 1px solid #ddd; /* Add border to the bottom of data cells */
}

td input {
    border: none;
    border-bottom: 2px solid #0a2949; /* Single-line underline */
    background-color: transparent;
    font-size: 16px;
    color: #333;
    padding: 8px 0; /* Adjust padding as needed */
    width: 100%;
    box-sizing: border-box;
}

td input:focus {
    border-bottom: 2px solid #4b5a6a; /* Change underline color on focus */
    outline: none;
}


    h1, h2 {
        text-align: center;
        margin-top: 20px;
    }

    form {
        margin-top: 20px;
    }

    .table-container {
        overflow-x: auto;
        margin-bottom: 20px;
    }

    table {
        width: 100%;
        color: #0a2949;
        border-collapse: collapse;
        margin-bottom: 20px;
    }

    th, td {
        padding: 10px;
        text-align: left;
    }

    th {
        background-color: #f2f2f2;
    }

    td input {
        border: none;
        border-bottom: 2px solid #0a2949;
        background-color: transparent;
        font-size: 16px;
        color: #333;
        padding: 10px 0;
        width: 100%;
    }

    td input:focus {
        border-bottom: 2px solid #4b5a6a;
        outline: none;
    }

    button[type="submit"] {
        padding: 12px 30px;
        background-color: #00796b;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s;
        font-size: 18px;
        margin-left: auto;
        margin-right: auto;
        display: block;
    }

    button[type="submit"]:hover {
        background-color: #004d40;
    }

    footer {
        text-align: center;
        padding: 2px;
        background-color: white;
        color: black;
        width: 100%;
        box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.3);
        font-size: 20px;
        position: relative;
        bottom: 0;
        left: 0;
    }

    footer a {
        color: black;
        text-decoration: none;
    }

    footer a:hover {
        text-decoration: underline;
    }
    

    @media (max-width: 768px) {
        .header {
            flex-direction: row;
            align-items: flex-start;
            padding: 15px;
        }

        .header img {
            height: 50px;
        }

        .container {
            padding: 15px;
        }

        th, td {
            font-size: 18px;
        }

        input[type="text"] {
            height: 40px;
            font-size: 18px;
        }

        button[type="submit"] {
            font-size: 16px;
            padding: 10px 20px;
        }
    }

    @media (max-width: 480px) {
        .header {
            padding: 10px;
        }

        .header img {
            height: 40px;
        }

        .container {
            padding: 10px;
        }

        th, td {
            font-size: 16px;
        }

        input[type="text"] {
            height: 35px;
            font-size: 16px;
        }

        button[type="submit"] {
            font-size: 14px;
            padding: 8px 16px;
        }

        h1, h2 {
            font-size: 18px;
        }
    }

    .navbar {
        width: 100vw;
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

    #sep:hover {
        background-color: rgb(24, 24, 57);
    }
    td input {
    border: none;
    border-bottom: 2px solid #0a2949; /* Single-line underline */
    background-color: transparent;
    font-size: 16px;
    color: #333;
    padding: 8px 0; /* Adjust padding as needed */
    width: 100%;
    box-sizing: border-box;
}

td input:focus {
    border-bottom: 2px solid #4b5a6a; /* Change underline color on focus */
    outline: none;
}

    .navbar a:hover {
        background-color: red;
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
            <h2>DEPARTMENT OF INFORMATION SCIENCE AND TECHNOLOGY</h2>
        </div>
        <div>
            <img class="ist" src="images/ist.png" alt="ist_logo">
        </div>
    </header>
    <nav class="navbar">
        <a href="home.py">Home</a><a id="sep" >--></a>
        <a href="student_main.py?id={Regno}">Student Details</a><a id="sep" >--></a>
        <a href="" >Paper Published Details</a>
    </nav>
    <div class="container">
        <form method="post" enctype="multipart/form-data">
            
        <h1>Paper Publishing Details</h1>
            <table>
                <thead>
                    <tr>
                        <th>Authors</th>
                        <th>Title</th>
                        <th>Journal Name</th>
                        <th>Month Year</th>
                        <th>DOI Link</th>
                        <th>Indexed in SCI-E / SCI / Scopus</th>
                    </tr>
                </thead>
                <h2>Paper Published in SCI-E/SCI/Scopus/WOS Indexed Journals</h2>
                <tbody>
                    <tr>
                        <td><input type="text" name="authors1"></td>
                        <td><input type="text" name="title1"></td>
                        <td><input type="text" name="journal_name1"></td>
                        <td><input type="text" name="month_year1"></td>
                        <td><input type="text" name="doi_link1"></td>
                        <td><input type="text" name="indexed1"></td>
                    </tr>
                    <tr>
                        <td><input type="text" name="authors2"></td>
                        <td><input type="text" name="title2"></td>
                        <td><input type="text" name="journal_name2"></td>
                        <td><input type="text" name="month_year2"></td>
                        <td><input type="text" name="doi_link2"></td>
                        <td><input type="text" name="indexed2"></td>
                    </tr>
                    <tr>
                        <td><input type="text" name="authors3"></td>
                        <td><input type="text" name="title3"></td>
                        <td><input type="text" name="journal_name3"></td>
                        <td><input type="text" name="month_year3"></td>
                        <td><input type="text" name="doi_link3"></td>
                        <td><input type="text" name="indexed3"></td>
                    </tr>
                </tbody>
            </table>

            <h2> Paper Published in National / International Conference / Workshop / Symposium</h2>
            <table>
              <thead>
                    <tr>
                        <th>Authors</th>
                        <th>Title</th>
                        <th>Journal Name</th>
                        <th>Month Year</th>
                        <th>DOI Link</th>
                        <th>Indexed in SCI-E / SCI / Scopus</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><input type="text" name="conference_authors1"></td>
                        <td><input type="text" name="conference_title1"></td>
                        <td><input type="text" name="conference_name1"></td>
                        <td><input type="text" name="conference_month_year1"></td>
                        <td><input type="text" name="conference_doi_link1"></td>
                        <td><input type="text" name="conference_indexed1"></td>
                    </tr>
                    <tr>
                        <td><input type="text" name="conference_authors2"></td>
                        <td><input type="text" name="conference_title2"></td>
                        <td><input type="text" name="conference_name2"></td>
                        <td><input type="text" name="conference_month_year2"></td>
                        <td><input type="text" name="conference_doi_link2"></td>
                        <td><input type="text" name="conference_indexed2"></td>
                    </tr>
                    <tr>
                        <td><input type="text" name="conference_authors3"></td>
                        <td><input type="text" name="conference_title3"></td>
                        <td><input type="text" name="conference_name3"></td>
                        <td><input type="text" name="conference_month_year3"></td>
                        <td><input type="text" name="conference_doi_link3"></td>
                        <td><input type="text" name="conference_indexed3"></td>
                    </tr>
                </tbody>
            </table>
            <div class="submit-container">
                <button type="submit" name="submit">Submit</button>
            </div>
              
        </form>
    </div>

    <footer>
        <p>&copy; 2024 Information Technology. All rights reserved.</p>
    </footer>
</body>
</html>

""")

Author1=form.getvalue("authors1")
Title1=form.getvalue("title1")
JournalName1=form.getvalue("journal_name1")
MonthYear1=form.getvalue("month_year1")
DoiLink1=form.getvalue("doi_link1")
Indexed1=form.getvalue("indexed1")

Author2=form.getvalue("authors2")
Title2=form.getvalue("title2")
JournalName2=form.getvalue("journal_name2")
MonthYear2=form.getvalue("month_year2")
DoiLink2=form.getvalue("doi_link2")
Indexed2=form.getvalue("indexed2")

Author3=form.getvalue("authors3")
Title3=form.getvalue("title3")
JournalName3=form.getvalue("journal_name3")
MonthYear3=form.getvalue("month_year3")
DoiLink3=form.getvalue("doi_link3")
Indexed3=form.getvalue("indexed3")

ConferenceAuthors1=form.getvalue("conference_authors1")
ConferenceTitle1=form.getvalue("conference_title1")
ConferenceName1=form.getvalue("conference_name1")
ConferenceMonthYear1=form.getvalue("conference_month_year1")
ConferenceDoiLink1=form.getvalue("conference_doi_link1")
ConferenceIndexed1=form.getvalue("conference_indexed1")

ConferenceAuthors2=form.getvalue("conference_authors2")
ConferenceTitle2=form.getvalue("conference_title2")
ConferenceName2=form.getvalue("conference_name2")
ConferenceMonthYear2=form.getvalue("conference_month_year2")
ConferenceDoiLink2=form.getvalue("conference_doi_link2")
ConferenceIndexed2=form.getvalue("conference_indexed2")

ConferenceAuthors3=form.getvalue("conference_authors3")
ConferenceTitle3=form.getvalue("conference_title3")
ConferenceName3=form.getvalue("conference_name3")
ConferenceMonthYear3=form.getvalue("conference_month_year3")
ConferenceDoiLink3=form.getvalue("conference_doi_link3")
ConferenceIndexed3=form.getvalue("conference_indexed3")

Submit=form.getvalue("submit")


if Submit != None :

    q = """SELECT id FROM paper_published_details WHERE register_no='%s'""" % (Regno)
    cur.execute(q)
    rec = cur.fetchone()

    if rec != None:
        q = """UPDATE paper_published_details SET author1='%s',title1='%s',journal_name1='%s',month_year1='%s',doi_link1='%s',indexed1='%s',author2='%s',title2='%s',journal_name2='%s',month_year2='%s',doi_link2='%s',indexed2='%s',author3='%s',title3='%s',journal_name3='%s',month_year3='%s',doi_link3='%s',indexed3='%s',conference_author1='%s',conference_title1='%s',conference_name1='%s',conference_month_year1='%s',conference_doi_link1='%s',conference_indexed1='%s',conference_author2='%s',conference_title2='%s',conference_name2='%s',conference_month_year2='%s',conference_doi_link2='%s',conference_indexed2='%s',conference_author3='%s',conference_title3='%s',conference_name3='%s',conference_month_year3='%s',conference_doi_link3='%s',conference_indexed3='%s' WHERE register_no='%s'""" % (
            Author1, Title1, JournalName1, MonthYear1, DoiLink1, Indexed1, Author2, Title2, JournalName2, MonthYear2,
            DoiLink2, Indexed2, Author3, Title3, JournalName3, MonthYear3, DoiLink3, Indexed3, ConferenceAuthors1,
            ConferenceTitle1, ConferenceName1, ConferenceMonthYear1, ConferenceDoiLink1, ConferenceIndexed1,
            ConferenceAuthors2, ConferenceTitle2, ConferenceName2, ConferenceMonthYear2, ConferenceDoiLink2,
            ConferenceIndexed2, ConferenceAuthors3, ConferenceTitle3, ConferenceName3, ConferenceMonthYear3,
            ConferenceDoiLink3, ConferenceIndexed3,Regno)
        cur.execute(q)
        con.commit()

        print("""
                                       <script>
                                       alert("Paper_published_details Updated Successfully !!");
                                       location.href='student_main.py?id=%s';
                                       </script>
                                       """ % Regno)

    else:
        q = """INSERT INTO paper_published_details(register_no,author1,title1,journal_name1,month_year1,doi_link1,indexed1,author2,title2,journal_name2,month_year2,doi_link2,indexed2,author3,title3,journal_name3,month_year3,doi_link3,indexed3,conference_author1,conference_title1,conference_name1,conference_month_year1,conference_doi_link1,conference_indexed1,conference_author2,conference_title2,conference_name2,conference_month_year2,conference_doi_link2,conference_indexed2,conference_author3,conference_title3,conference_name3,conference_month_year3,conference_doi_link3,conference_indexed3) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (
            Regno,Author1,Title1,JournalName1,MonthYear1,DoiLink1,Indexed1,Author2,Title2,JournalName2,MonthYear2,DoiLink2,Indexed2,Author3,Title3,JournalName3,MonthYear3,DoiLink3,Indexed3,ConferenceAuthors1,ConferenceTitle1,ConferenceName1,ConferenceMonthYear1,ConferenceDoiLink1,ConferenceIndexed1,ConferenceAuthors2,ConferenceTitle2,ConferenceName2,ConferenceMonthYear2,ConferenceDoiLink2,ConferenceIndexed2,ConferenceAuthors3,ConferenceTitle3,ConferenceName3,ConferenceMonthYear3,ConferenceDoiLink3,ConferenceIndexed3)
        cur.execute(q)
        con.commit()

        print("""
                               <script>
                               alert("Paper_published_details Added Successfully !!");
                               location.href='student_main.py?id=%s';
                               </script>
                               """ % Regno)

