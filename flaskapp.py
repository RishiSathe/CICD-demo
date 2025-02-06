from flask import Flask

app = Flask(__name__)

@app.route('/')
def indexpage():
    return '''
    <html>
    <head>
        <style>
            body { 
                font-family: 'Arial', sans-serif; 
                background-color: #f7f9fc; /* Lightest blue */
                margin: 0;
                padding: 0;
                color: #333333; /* Dark gray for better contrast */
            }
            .container {
                width: 80%;
                margin: auto;
                padding: 40px;
                background-color: #ffffff; /* White */
                box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
                border-radius: 12px;
                margin-top: 50px;
                text-align: center;
            }
            h1 { 
                color: #4a90e2; /* Nice blue */
                font-size: 36px;
                margin-bottom: 20px;
            }
            p { 
                font-size: 18px; 
                color: #555555; /* Medium gray */
                line-height: 1.6;
            }
            .btn {
                display: inline-block;
                padding: 10px 20px;
                margin-top: 20px;
                font-size: 16px;
                color: #ffffff;
                background-color: #4a90e2; /* Button blue */
                text-decoration: none;
                border-radius: 8px;
                transition: background-color 0.3s ease;
            }
            .btn:hover {
                background-color: #357ab7; /* Darker blue */
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to Our Flask App</h1>
            <p>We're thrilled to have you here! Explore our features and enjoy your stay.</p>
            <a href="/nxtpg" class="btn">Go to Next Page</a>
        </div>
    </body>
    </html>
    '''

@app.route('/nxtpg')
def nextpage():
    return '''
    <html>
    <head>
        <style>
            body { 
                font-family: 'Arial', sans-serif; 
                background-color: #f7f9fc; /* Lightest blue */
                margin: 0;
                padding: 0;
                color: #333333; /* Dark gray for better contrast */
            }
            .container {
                width: 80%;
                margin: auto;
                padding: 40px;
                background-color: #ffffff; /* White */
                box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
                border-radius: 12px;
                margin-top: 50px;
                text-align: center;
            }
            h1 { 
                color: #32cd32; /* LimeGreen */
                font-size: 36px;
                margin-bottom: 20px;
            }
            p { 
                font-size: 18px; 
                color: #555555; /* Medium gray */
                line-height: 1.6;
            }
            .btn {
                display: inline-block;
                padding: 10px 20px;
                margin-top: 20px;
                font-size: 16px;
                color: #ffffff;
                background-color: #32cd32; /* Button green */
                text-decoration: none;
                border-radius: 8px;
                transition: background-color 0.3s ease;
            }
            .btn:hover {
                background-color: #228b22; /* Darker green */
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>You've Reached the Next Page</h1>
            <p>Congratulations! Keep exploring and enjoy the journey.</p>
            <a href="/" class="btn">Back to Home</a>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)