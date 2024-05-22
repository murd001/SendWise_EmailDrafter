import csv
from flask import Flask, render_template, request
from sendMail import send_email

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        smtp_password = request.form['smtp_password']
        sender_email = request.form['sender_email']
        subject = request.form['subject']
        html_body = request.form['html_body']

        if 'recipients_filename' in request.files:
            recipients_file = request.files['recipients_filename']

            if recipients_file.filename != '':
                recipients_filename = 'Send Wise/uploads/' + recipients_file.filename
                recipients_file.save(recipients_filename)  # Save uploaded file

                # Send email using sendMail function
                send_email(sender_email, smtp_password, subject, html_body, recipients_filename)

                return render_template('index.html', preview_html=html_body)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
