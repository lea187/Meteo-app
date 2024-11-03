from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/weather', methods=['POST'])
def get_weather_for_city():
    city = request.form['city']  # Récupérer la ville depuis le formulaire
    api_key = "02f5004a96321abd346684d5753e2604"  # Remplace par ta clé API OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    
    if data['cod'] == 200:
        # Récupérer les données météo
        weather_data = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
        return render_template('result.html', weather=weather_data)  # Rendre le template avec les données météo
    else:
        return render_template('result.html', weather=None)  # Gérer les erreurs en affichant un message

if __name__ == '__main__':
    app.run(debug=True)