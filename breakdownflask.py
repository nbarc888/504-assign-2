#additional resource for flask can be found below
    #https://flask.palletsprojects.com/en/stable/

from flask import Flask ### imports and downloads flask to be usable within script 

app = Flask(__name__) ### creates the instance for flask application 

# Home route
@app.route("/") #Decorator that associates the function 'home' with root URL
def home(): ###### generates the text in the webpage
    return """
Chiikawa (ちいかわ) - series also referred to as Nanka Chiisakute Kawaii Yatsu (なんか小さくてかわいいやつ; 'literally translated to: Something Small and Cute')

Japanese web series that follows the daily adventures of a small cute creature named Chiikawa and friends.

Series gained popularity in 2020's and growing popularity remains within the teenage to young adult demographic in East Asia

Web series also was granted an anime series of short 5-minute episodes that is currently ongoing.

The Chiikawa franchise is estimated to have exceeded 10 billion yen (68 million USD) in September 2025 -Kyodo News
    """
        

if __name__ == "__main__":
    # Run on all interfaces (so it's accessible via public IP), port 5003
    app.run(host="0.0.0.0", port=5003) # This block ensures the application runs when the script is executed directly