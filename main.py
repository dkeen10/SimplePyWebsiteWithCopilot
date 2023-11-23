# Create a simple web server using Flask

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

# HTML string for the webpage
# Use CSS for styling
#Provide a form where users can enter a username and password
html = """
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="description" content="Simple Web Server">
        <meta name="author" content="Jorge Garcia">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {
                font-family: Arial, Helvetica, sans-serif;
            }
            h1 {
                text-align: center;
            }
            p {
                text-align: center;
            }
            form {
                text-align: center;
            }
            label {
                font-weight: bold;
            }
        </style>
        <title>Simple Web Server</title>
    </head>
    <body>
        <h1>Simple Web Server</h1>
        <p>This is a simple web server.</p>
        <form>
            <label for="username">Username:</label><br>
            <input type="text" id="username" name="username"><br>
            <label for="password">Password:</label><br>
            <input type="password" id="password" name="password"><br><br>
            <input type="submit" value="Submit">
    </body>
</html>
"""


# Create an instance of the Flask class
app = Flask(__name__)

# Create a simple endpoint for the home page
@app.route('/') 
def home():
    return html

#Run the app
if __name__ == '__main__':
    app.run(debug=True)
