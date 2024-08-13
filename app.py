from flask import Flask, render_template, request

app = Flask(__name__)

# Function to determine the appropriate club based on distance and lie
def recommend_club(distance, lie):
    if lie == "fairway":
        if distance > 265:
            return "Driver"
        elif 220 <= distance <= 265:
            return "3-Wood"
        elif 200 <= distance < 220:
            return "5-Hybrid"
        elif 187 <= distance <= 200:
            return "5-Iron"
        elif 175 <= distance < 187:
            return "6-Iron"
        elif 160 <= distance < 175:
            return "7-Iron"
        elif 150 <= distance < 160:
            return "8-Iron"
        elif 143 <= distance < 150:
            return "9-Iron"
        elif 110 <= distance < 143:
            return "Pitching Wedge"
        elif 100 <= distance < 110:
            return "Approach Wedge - 52"
        elif 85 <= distance < 100:
            return "Sand Wedge - 56"
        else:
            return "Lob Wedge - 60"
    elif lie == "rough":
        if distance > 200:
            return "3-Wood"
        elif 150 <= distance <= 200:
            return "5-Iron"
        elif 120 <= distance < 150:
            return "7-Iron"
        elif 100 <= distance < 120:
            return "8-Iron"
        else:
            return "Sand Wedge"
    elif lie == "sand":
        if distance > 100:
            return "7-Iron"
        else:
            return "Sand Wedge"
    else:
        return "Putter"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        distance = int(request.form['distance'])
        lie = request.form['lie']
        club = recommend_club(distance, lie)
        return f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Recommended Club</title>
            <style>
                body {{
                    font-family: 'Arial', sans-serif;
                    background-color: #f0f2f5;
                    margin: 0;
                    padding: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }}
                .container {{
                    background-color: #fff;
                    padding: 30px;
                    border-radius: 10px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    text-align: center;
                    max-width: 400px;
                    width: 100%;
                }}
                h1 {{
                    color: #333;
                    margin-bottom: 20px;
                }}
                a {{
                    display: inline-block;
                    margin-top: 20px;
                    text-decoration: none;
                    color: #007bff;
                }}
                a:hover {{
                    text-decoration: underline;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Your Recommended Club is: {club}</h1>
                <a href="/">Try Again</a>
            </div>
        </body>
        </html>
        '''
    except Exception as e:
        return f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Error</title>
            <style>
                body {{
                    font-family: 'Arial', sans-serif;
                    background-color: #f0f2f5;
                    margin: 0;
                    padding: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }}
                .container {{
                    background-color: #fff;
                    padding: 30px;
                    border-radius: 10px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    text-align: center;
                    max-width: 400px;
                    width: 100%;
                }}
                h1 {{
                    color: #333;
                    margin-bottom: 20px;
                }}
                a {{
                    display: inline-block;
                    margin-top: 20px;
                    text-decoration: none;
                    color: #007bff;
                }}
                a:hover {{
                    text-decoration: underline;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>An error occurred: {str(e)}</h1>
                <a href="/">Try Again</a>
            </div>
        </body>
        </html>
        '''

@app.route('/track_score', methods=['POST'])
def track_score():
    scores = [int(request.form[f'hole{i}']) for i in range(1, 19)]
    total_score = sum(scores)
    return f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Total Score</title>
        <style>
            body {{
                font-family: 'Arial', sans-serif;
                background-color: #f0f2f5;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }}
