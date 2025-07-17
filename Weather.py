<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Weather App</title>
  <link rel="stylesheet" href="style.css">
  <style>
    body {
      text-align: center;
      font-family: Arial;
      padding: 50px;
      background-color: #FF0000; /* Fixed double hash */
    }

    input, button {
      padding: 10px;
      margin: 10px;
      font-size: 16px;
    }
  </style>
</head>
<body>
  <h1>Weather App</h1>

  <input type="text" id="city" placeholder="Enter city name">      
  <button onclick="getWeather()">Get Weather</button>

  <div id="result"></div>

  <script>
    // units = metric means the temperature will be shown in celsius
    function getWeather() {
      const city = document.getElementById('city').value;
      const apiKey = "YOUR_API_KEY";
      const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

      fetch(url)
        .then(response => response.json()) // The response will be in raw format.
        // response.json() tells the browser to convert the response into JSON format (a format we can read easily in JavaScript)
        .then(data => {
          const temp = data.main.temp; // data is the json object we got from the weather API
          // Inside it, there is a part called main (which has temperature, pressure, humidity etc.)
          // main.temp means: "get the temperature from main section"
          // Examples: If the API gives
          // "main": {
          //   "temp": 30.15,
          //   "pressure": 1005,
          //   "humidity": 70
          // }
          const desc = data.weather[0].description;
          // data.weather is a list of weather conditions
          // [0] means we are taking the first weather condition from the list
          // .description gives short text like "clear sky" or "rain"
          // Examples: If the API gives
          // "weather": [
          //   {
          //     "main": "Clear",
          //     "description": "clear sky"
          //   }
          // ]
          document.getElementById('result').innerHTML =
            `<p>Temperature: ${temp}°C</p><p>Description: ${desc}</p>`;
          console.log("Temperature:", temp);
          console.log("Description:", desc);
        })
        .catch(error => {
          document.getElementById('result').innerHTML = "City not found or API error.";
        });
    }
  </script>
</body>
</html>
