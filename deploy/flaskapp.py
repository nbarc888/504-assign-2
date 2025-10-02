from flask import Flask

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return """
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <title>AHI 504 Flask VM Demo</title>
        <style>
          body {
            font-family: Arial, sans-serif;
            background-color: #3d4247;
            color: #EFF0EF;
            text-align: center;
            margin: 50px;
          }
          h1 {
            color: #28d73b;
          }
          p {
            font-size: 1.2em;
          }
          .footer {
            margin-top: 40px;
            font-size: 0.9em;
            color: #777;
          }
        </style>
      </head>
      <body>
        <h1> Flask is Running on Your Cloud VM! ✔️ </h1>
        <p>
          Congratulations — you’ve deployed a Python Flask app on port 5003.<br>
          Flask setup successfully deployed!
        </p>
        <div class="footer">
          <p>AHI 504 — Cloud Foundations for Health Informatics</p>
        </div>
        <h2> About Me </h2>
        
          <p> Hello! My name is Nina, and I am excited to be part of this course. </p>
          <p> I have a background in Nursing, and I am looking forward to learning more about cloud computing and its applications in health informatics. </p>
          <p> In my free time, I enjoy drawing and gaming. </p>
          <p> I am eager to collaborate with my classmates and gain hands-on experience in this field :D . </p>
      
      </body>
    </html>
    """
        


if __name__ == "__main__":
    # Run on all interfaces (so it's accessible via public IP), port 5003
    app.run(host="0.0.0.0", port=5003)
