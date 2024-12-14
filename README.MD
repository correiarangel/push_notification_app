# Push Notification App (`R Notifications`)

**R Notifications** is a web application designed to create and test push notifications using the **OneSignal SDK**. It was developed as the final project for Harvard's **CS50: Introduction to Computer Science** course, promoted in Brazil by **Grupo Estudar**. This project was built using the **Flask framework** with **Python**, offering a simple and effective way for developers to test push notifications across different platforms. The application supports **desktop and tablet** environments via web browsers.

(Aplication Run...)[pushnotificationapp-production.up.railway.app]

## Version

- **1.0.0**

## Features

- Send and test push notifications.
- Built with Flask/Python for simplicity and scalability.
- Supports notifications using the **OneSignal SDK**.
- Open-source: The source code is publicly available for modification and redistribution (with proper credit).

## How to Set Up and Run the Application

### Prerequisites

- **Python** (version 3.8 or above)
- **pip** (Python package installer)
- **Git** (to clone the repository)
- A web browser (desktop or tablet)

### Installation Steps

```bash
# Clone the Repository
git clone https://github.com/username/push_notification_app.git
cd push_notification_app

# Set Up a Virtual Environment
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install Required Packages
pip install -r requirements.txt

# Configure OneSignal
# Create a OneSignal account and set up a project.
# Update the configuration file (config.py) with your OneSignal API key and app ID.

# Run the Application
flask run

# Access the Application
# The application will be accessible at:
# http://127.0.0.1:5000
```

### Testing Push Notifications

Open the web application in a browser. Enter the necessary details for your push notification (e.g., title, message, target audience) and test the notification by sending it directly through the application.

## About the Developer

**Marcos Fabiano Correia Rangel**
*"The only way to achieve the impossible is to believe it’s possible."*

### Academic Background

* **Postgraduate** : Mobile App Development (IFSP, 2020).
* **Undergraduate** : IT Management (Estácio Sá, 2016).
* **Technical** : IT Technician (ETEC, 2010).

### Social Media & Contact

* **LinkedIn** : [LinkedIn Profile](#)
* **GitHub** : [GitHub Profile](#)
* **Medium** : [Medium Profile](#)
* **Facebook** : [Facebook Profile](#)

## Acknowledgments

This project is a result of the **CS50: Introduction to Computer Science** course by Harvard University, facilitated in Brazil by  **Grupo Estudar** . Special thanks to the instructors and peers for the incredible learning journey. Feedback, suggestions, and constructive criticism are highly appreciated and can be shared through the contact channels listed above.

 (Aplication Run...)[pushnotificationapp-production.up.railway.app]
