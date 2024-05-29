

# 🏃‍♂️ Exercise Tracker Application using NLP and Sheety APIs

Python-based tool that leverages NLP and Sheety APIs to help users log their physical activities and monitor their fitness progress. With this application, users can seamlessly track their exercises, calculate calories burned, and store their activity data in a structured format.

## ⭐ Key Features:

### NLP Integration:
- 🔗 Utilizes a Natural Language Processing (NLP) API to interpret and analyze exercise descriptions.
- 📊 Automatically calculates the calories burned based on the type and duration of the exercise.

### Customizable Tracking:
- ⚙️ Users can log various exercises with different types, durations, and intensities.
- 🎯 Flexibility to input any form of physical activity and get structured data in return.

### Automated Data Logging:
- 🗓️ Logs exercise details including duration, calories burned, date, and time to a Google Sheet using the Sheety API.
- 🔄 Automatic updates ensure all exercise data is recorded in real-time.

### Performance Analysis:
- 📊 Provides detailed records of exercises, enabling users to analyze their physical activity trends over time.
- 🔍 Offers insights into exercise frequency, calorie expenditure, and overall fitness progress.


## 🚀 How It Works:

### Setup:
- 🛠️ Install necessary Python packages (`requests` for API interactions).
- 🔑 Set up your NLP and Sheety API configurations.

### Configuration:
- ⚙️ Define your personal details (gender, weight, height, age) and API keys in the `config.py` file.
- 📈 Configure Sheety to connect your Google Sheet for data logging.

### Daily Tracking:
- 📅 Log daily exercises by entering the type and duration of the activity.
- 🔄 The application processes this input using the NLP API and sends the data to Sheety, updating the Google Sheet.

### Visualization:
- 👀 View your logged exercise data in the connected Google Sheet.
- 📊 Analyze performance trends and statistics using the visual insights provided by the Google Sheet graphs.

## 🏁 Getting Started:

### Installation:
1. ⬇️ Clone the repository and navigate to the project directory.
   ```bash
   git clone https://github.com/yourusername/exercise-tracker.git
   cd exercise-tracker
   ```
2. 📦 Install the required dependencies:
   ```bash
   pip install requests
   ```

### Configuration:
1. 🔑 Set up your API keys and personal details in `config.py`:
   ```python
   BASE_URL = "https://api.your_nlp_api.com"
   NATURAL_LANGUAGE_ENDPOINT = "/v2/natural_language_processing/exercise"
   URL = "https://api.sheety.co/your_project/sheet"
   APP_ID = "your_app_id"
   API_KEY = "your_api_key"
   GENDER = "your_gender"
   WEIGHT_KG = your_weight_in_kg
   HEIGHT_CM = your_height_in_cm
   AGE = your_age
   ```

### Usage:
1. 📝 Run the application:
   ```bash
   python main.py
   ```
2. 🏃‍♂️ Enter your exercise details when prompted:
   ```
   What exercise have you completed?
   ```



## Contributing
Contributions are welcome! Please create an issue or submit a pull request for any improvements or bug fixes.

## Contact
For any questions or inquiries, please contact [cjhester23@gmail.com].

