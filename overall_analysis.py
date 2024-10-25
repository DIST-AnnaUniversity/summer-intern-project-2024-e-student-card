#!C:/Python/python.exe
import pymysql, cgitb, cgi
import json

# Set content type for the response
print("Content-type: text/html\r\n\r\n")
cgitb.enable()  # Enable CGI error reporting

# Connect to the MySQL database
con = pymysql.connect(host="localhost", user="root", password="", database="summer_project")
cur = con.cursor()

# Retrieve form data
form = cgi.FieldStorage()
batch = form.getvalue("batch")

# Fetch the list of students for the specified batch
cur.execute("SELECT register_no FROM batch_details WHERE batch=%s", (batch,))
students = cur.fetchall()  # Get all registered student numbers

# Calculate the total number of students in the batch
total_students = len(students)  # Total students
arrear_students = 0  # Initialize arrear student count
pass_students = 0  # Initialize pass student count

# List of semester tables to check for grades
semesters = ['sem1', 'sem2', 'sem3', 'sem4', 'sem5', 'sem6', 'sem7', 'sem8']

# Iterate through each student to check for arrears
for student in students:
    register_no = student[0]  # Get the student's register number
    has_arrear = False  # Flag to check if the student has any arrears

    # Check grades for each semester
    for semester in semesters:
        # Query to fetch grades for the current semester
        query = f"SELECT grade1, grade2, grade3, grade4, grade5, grade6, grade7, grade8, grade9, grade10 FROM {semester} WHERE register_no=%s"
        cur.execute(query, (register_no,))
        grades = cur.fetchone()  # Get grades for the student

        if grades:
            # If any grade is 'U', mark student as having an arrear
            if 'U' in grades:
                has_arrear = True
                break  # No need to check further semesters if an arrear is found

    # If the student has an arrear, increment the arrear count
    if has_arrear:
        arrear_students += 1  # Count this student as an arrear student
    else:
        pass_students += 1  # Count this student as a pass student

# Calculate percentages for pass and arrear
if total_students > 0:
    pass_percentage = ((total_students - arrear_students) / total_students) * 100  # Calculate pass percentage
    arrear_percentage = (arrear_students / total_students) * 100  # Calculate arrear percentage
else:
    pass_percentage = arrear_percentage = 0  # Handle division by zero

# Close the database connection
con.close()

# Prepare data for the pie chart
data = {
    'labels': ['Pass Percentage', 'Arrear Percentage'],
    'datasets': [{
        'data': [pass_percentage, arrear_percentage],  # Data for the chart
        'backgroundColor': ['#4CAF50', '#FF6347']  # Colors for each segment
    }]
}

# HTML and JS for displaying the chart
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
        .chart-container {{
            width: 30%;
            margin: 0 auto;  /* Center the chart container */
        }}
        .stats {{
            text-align: center;  /* Center the text */
            margin: 20px 0;  /* Add margin for spacing */
            font-family: Arial, sans-serif;  /* Set font */
            font-size: 1.2em;  /* Set font size */
            color: #333;  /* Darker text color */
        }}
        .stats p {{
            margin: 5px 0;  /* Space between paragraphs */
            padding: 10px;  /* Add padding around the text */
            border-radius: 5px;  /* Rounded corners */
        }}
        .pass {{
            background-color: #4CAF50;  /* Green background for pass */
            color: white;  /* White text */
        }}
        .arrear {{
            background-color: #FF6347;  /* Red background for arrear */
            color: white;  /* White text */
        }}
        .total {{
            background-color: #2196F3;  /* Blue background for total */
            color: white;  /* White text */
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
        <a href="admin_main.py">Dashboard</a><a id="sep">--></a>
        <a href="#">Analysis</a>
    </nav>
    <h1>Batch Analysis for {batch}</h1>
    <div class="stats">
        <p class="total">Total Students: {total_students}</p>
        <p class="pass">Total Pass Students: {pass_students}</p>
        <p class="arrear">Total Arrear Students: {arrear_students}</p>
        <p class="pass">Overall Pass Percentage: {pass_percentage:.2f}%</p>
        <p class="arrear">Overall Arrear Percentage: {arrear_percentage:.2f}%</p>
    </div>
    <div class="chart-container">
        <canvas id="batchAnalysisChart"></canvas>  <!-- Canvas element for Chart.js -->
    </div>
    <script>
        const data = {json.dumps(data)};  // Convert data to JSON format
        const config = {{
            type: 'pie',  // Type of chart
            data: data,  // Data to be used
            options: {{
                responsive: true,  // Make the chart responsive
                plugins: {{
                    legend: {{
                        position: 'top',  // Position of the legend
                    }},
                    tooltip: {{
                        callbacks: {{
                            label: function(tooltipItem) {{
                                // Format tooltip label to show percentage with two decimal places
                                return tooltipItem.label + ': ' + tooltipItem.raw.toFixed(2) + '%';
                            }}
                        }}
                    }}
                }}
            }}
        }};

        const myChart = new Chart(
            document.getElementById('batchAnalysisChart'),  // Reference to the canvas element
            config  // Configuration for the chart
        );
    </script>
</body>
</html>
""")
