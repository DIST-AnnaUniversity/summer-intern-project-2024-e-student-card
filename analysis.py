#!C:/Python/python.exe
import pymysql, cgitb, cgi
import json

print("Content-type: text/html\r\n\r\n")
cgitb.enable()

# Connect to database
con = pymysql.connect(host="localhost", user="root", password="", database="summer_project")
cur = con.cursor()

form = cgi.FieldStorage()
staffid = form.getvalue("id")
batch = form.getvalue("batch")

# Fetch the list of students for the given batch and staff
cur.execute("SELECT register_no FROM batch_details WHERE staffid=%s AND batch=%s", (staffid, batch))
students = cur.fetchall()

total_students = len(students)
overall_arrear_students = 0
overall_pass_students = 0

# List of semester tables to check
semesters = ['sem1', 'sem2', 'sem3', 'sem4', 'sem5', 'sem6', 'sem7', 'sem8']

# Data for each semester's arrear and pass counts
sem_wise_pass = []
sem_wise_arrears = []

# Store the details for each semester analysis
sem_analysis_details = []

for semester in semesters:
    sem_arrear_students = 0
    sem_pass_students = 0
    arrear_register_nos = []  # List to store register numbers with arrears

    for student in students:
        register_no = student[0]

        query = f"SELECT grade1, grade2, grade3, grade4, grade5, grade6, grade7, grade8, grade9, grade10 FROM {semester} WHERE register_no=%s"
        cur.execute(query, (register_no,))
        grades = cur.fetchone()

        if grades:
            # Count arrears and passes based on grades
            if 'U' in grades:
                sem_arrear_students += 1
                arrear_register_nos.append(register_no)  # Add register_no to arrear list
            else:
                sem_pass_students += 1

    sem_wise_arrears.append(sem_arrear_students)
    sem_wise_pass.append(sem_pass_students)

    # Update overall arrear and pass counts
    overall_arrear_students += sem_arrear_students
    overall_pass_students += sem_pass_students

    # Add semester analysis details including arrear students for display
    sem_analysis_details.append({
        'semester': semester.capitalize(),
        'pass': sem_pass_students,
        'arrears': sem_arrear_students,
        'arrear_students': arrear_register_nos  # Include arrear students
    })

# Calculate overall percentages
if total_students > 0:
    pass_percentage = ((total_students - overall_arrear_students) / total_students) * 100
    arrear_percentage = (overall_arrear_students / total_students) * 100
else:
    pass_percentage = arrear_percentage = 0

# Close the database connection
con.close()

# Data to be used in the chart for semester-wise analysis
semester_data = {
    'labels': ['Sem1', 'Sem2', 'Sem3', 'Sem4', 'Sem5', 'Sem6', 'Sem7', 'Sem8'],
    'datasets': [
        {
            'label': 'Pass',
            'data': sem_wise_pass,
            'backgroundColor': '#4CAF50'
        },
        {
            'label': 'Arrears',
            'data': sem_wise_arrears,
            'backgroundColor': '#FF6347'
        }
    ]
}

# HTML and JS for displaying the charts
print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IST STUDENT RECORD</title>
    <link rel="icon" href="images/ist.png">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link rel="stylesheet" href="fetching.css" type="text/css">
    <style>
        .chart-container1 {{
            width: 30%;
            margin: 0 auto;
        }}
        .chart-container2 {{
            width: 60%;
            margin: 0 auto;
        }}
        .navbar {{
            background-color: rgb(24, 24, 57);
            overflow: hidden;
            text-align: left;
        }}

        .navbar a {{
            display: inline-block;
            color: white;
            padding: 14px 20px;
            text-decoration: none;
            font-size: 1.2rem;
        }}

        #sep:hover {{
            background-color: rgb(24, 24, 57);
        }}

        .navbar a:hover {{
            background-color: red;
        }}

        .analysis-info {{
            text-align: center;
            margin-top: 20px;
            font-size: 1.2rem;
        }}

        .semester-analysis {{
            text-align: center;
            margin-top: 30px;
        }}

        table {{
            margin: 20px auto;
            border-collapse: collapse;
            font-size: 1.1rem;
        }}

        table, th, td {{
            border: 1px solid black;
            padding: 10px;
        }}

        th {{
            background-color: rgb(24, 24, 57);
            color: white;
        }}
    </style>
</head>
<body>
    <section class="header">
        <div>
            <img class="ceg" src="images/ceg.png" alt="au_logo" width="200px" height="150px">
        </div>
        <div>
            <h1>DEPARTMENT OF INFORMATION SCIENCE AND TECHNOLOGY</h1>
        </div>
        <div>
            <img class="ist" src="images/ist.png" alt="ist_logo" width="200px" height="150px">
        </div>
    </section>
    <nav class="navbar">
        <a href="home.py">Home</a><a id="sep">--></a>
        <a href="staff_main.py?id={staffid}">Dashboard</a><a id="sep">--></a>
        <a href="#">Analysis</a>
    </nav>
    <h1>Batch Analysis for {batch}</h1>

    <!-- Analysis Information Section -->
    <div class="analysis-info">
        <p>Total Students: {total_students}</p>
        <p>Total Pass Students: {total_students - overall_arrear_students}</p>
        <p>Total Arrear Students: {overall_arrear_students}</p>
        <p>Overall Pass Percentage: {pass_percentage:.2f}%</p>
        <p>Overall Arrear Percentage: {arrear_percentage:.2f}%</p>
    </div>

    <div class="chart-container1">
        <canvas id="overallChart"></canvas>
    </div>

    <!-- Semester-wise Analysis Section -->
    <h2 class="semester-analysis">Semester-wise Analysis</h2>
    <table>
    <tr>
        <th>Semester</th>
        <th>Pass Count</th>
        <th>Arrear Count</th>
        <th>Arrear Students (Register Nos)</th>
    </tr>
    {''.join([f"<tr><td>{sem['semester']}</td><td>{sem['pass']}</td><td>{sem['arrears']}</td><td>{', '.join(map(str, sem['arrear_students']))}</td></tr>" for sem in sem_analysis_details])}
</table>


    <div class="chart-container2">
        <canvas id="semWiseChart"></canvas>
    </div>

    <script>
        // Overall pass and arrear percentage pie chart
        const overallData = {{
            labels: ['Pass Percentage', 'Arrear Percentage'],
            datasets: [{{
                data: [{pass_percentage}, {arrear_percentage}],
                backgroundColor: ['#4CAF50', '#FF6347']
            }}]
        }};
        const overallConfig = {{
            type: 'pie',
            data: overallData,
            options: {{
                responsive: true,
                plugins: {{
                    legend: {{
                        position: 'top',
                    }},
                    tooltip: {{
                        callbacks: {{
                            label: function(tooltipItem) {{
                                return tooltipItem.label + ': ' + tooltipItem.raw.toFixed(2) + '%';
                            }}
                        }}
                    }}
                }}
            }}
        }};
        const overallChart = new Chart(
            document.getElementById('overallChart'),
            overallConfig
        );

        // Semester-wise bar chart
        const semWiseData = {json.dumps(semester_data)};
        const semWiseConfig = {{
            type: 'bar',
            data: semWiseData,
            options: {{
                responsive: true,
                plugins: {{
                    legend: {{
                        position: 'top',
                    }},
                    title: {{
                        display: true,
                        text: 'Semester-wise Pass and Arrear Count'
                    }},
                }},
                scales: {{
                    y: {{
                        beginAtZero: true
                    }}
                }}
            }}
        }};
        const semWiseChart = new Chart(
            document.getElementById('semWiseChart'),
            semWiseConfig
        );
    </script>
</body>
</html>
""")
