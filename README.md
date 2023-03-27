# CarbonFootPrint

CarbonFootPrint is an important project because it helps raise awareness about the impact of our daily activities on the environment. The carbon footprint is a measure of the amount of carbon dioxide and other greenhouse gases that are released into the atmosphere as a result of our actions, such as driving a car, using electricity, and consuming food and goods.

By providing users with a way to calculate their carbon footprint, CarbonFootPrint encourages them to think about the impact of their actions and make changes to reduce their environmental impact. This can include making changes to their transportation habits, reducing energy consumption, and adopting more sustainable consumer choices.

The registration and login system allows users to track their progress over time and see how their carbon footprint changes as they make changes to their lifestyle. The evaluations provide feedback on their progress and encourage them to continue making changes.

Overall, CarbonFootPrint is an important project because it helps raise awareness about the impact of our daily activities on the environment and encourages individuals to take action to reduce their environmental impact.

## Installation

To run the application locally, follow these steps:

1. Clone the repository to your local machine:

```python
git clone https://github.com/UtshoDeyTech/NurtureMe.git
```


2. Navigate to the project directory:

```python
cd CarbonFootPrint
```

3. Install the required Python packages:

```python
pip install -r requirements.txt
```

4. Run the development server:


```python
python manage.py runserver
```


5. Navigate to `http://localhost:8000/` in your web browser to view the application.

## Usage

The CarbonFootPrint web application is easy to use and provides users with a clear and simple interface to calculate their carbon footprint.

When you first open the application, you will be prompted to register or log in. If you are a new user, click on the `Sign Up` link to create a new account. You will be asked to enter your name, email address, and create a password. After submitting the registration form, you will be directed to the login page.

Once you are logged in, you will be redirected to the home page, where you can view a list of available surveys. The home page also displays your username, your current survey score, and a list of your past evaluations.

To take a survey, click on the `Start Survey` button for the survey you wish to take. You will be directed to a page with a series of questions related to the topic of the survey. Answer the questions to the best of your ability, and then click the `Submit` button at the bottom of the page to view your survey score and a summary of your answers.

After completing a survey, you can view your survey scores and evaluations by clicking on the `Evaluation` link in the top navigation bar. This will take you to a page that displays a summary of your survey scores and a text box where you can enter additional comments or feedback.

In addition to taking surveys and viewing your scores, the CarbonFootPrint application also allows you to update your profile information, such as your name and email address. To do this, click on the "Profile" link in the top navigation bar and then click on the `Edit Profile` button.

Overall, the CarbonFootPrint web application provides users with an easy and effective way to calculate their carbon footprint and make changes to reduce their environmental impact.


## Project Structure

The project structure section describes the organization of the CarbonFootPrint Django application. It contains a high-level overview of the different components that make up the application and the purpose they serve.

The CarbonFootPrint project consists of a Django project, which is named `CarbonFootPrint`, and a single app named `base`. The CarbonFootPrint project is the highest-level component of the application, and it contains the `settings.py` file and the project-level `urls.py` file. The base app, on the other hand, is the primary functional component of the application, containing the `models`, `views`, and `templates` used to build the web application.

The `models.py` file in the base app defines the data models used by the application. These models include the `CustomUser`, `Room`, `Question`, `Option`, `BaseModel`, and `HomeQuestions` models. These models define the structure of the data that the application will store and manipulate, including information about users, surveys, and survey questions.

The `views.py` file in the base app defines the views used by the application. Views are the functions that handle HTTP requests and generate HTTP responses. The views defined in this file include `home()`, `room()`, `survey()`, `SignupPage()`, `LoginPage()`, and `LogoutPage()`. These views are responsible for rendering the appropriate templates and processing user input.

The `urls.py` file in the base app defines the URL patterns used by the application. URL patterns define the structure of the URLs used by the application and map those URLs to specific views.

The `templates` folder in the base app contains the HTML templates used to render the views. These templates define the structure and layout of the web pages that make up the application.

The static folder in the base app contains the static files used by the application. These files include CSS and JavaScript files, which are used to style the web pages and add interactivity to the application.

In summary, the project structure section provides a broad overview of the components that make up the CarbonFootPrint application, and how they work together to create a functional web application.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! If you have any suggestions or bug reports, please open an issue on GitHub.
