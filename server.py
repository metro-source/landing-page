import smtplib
import flask

app = flask.Flask(__name__)

@app.route("/api/sendmail", methods=["POST"])
def sendmail():
    params = flask.request.json
    
    with smtplib.SMTP("localhost") as smtp:
        message = "From: MetroVPN Mailer <mailer@vpn.metrodev.io>\r\nTo: contact@metrodev.io\r\n\r\n"
        message += params['name']+" "+params['email']+"\n"+params['msg']

        smtp.sendmail("mailer@vpn.metrodev.io", ["contact@metrodev.io"], message)

    response = flask.jsonify(status="Email sent 😎")

    return response