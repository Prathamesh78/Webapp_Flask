# Webapp_Flask

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```
   
2. Navigate to the project directory:
   ```bash
   cd your-repository
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Set the Flask app environment variable:

   - For Windows:
     ```cmd
     set FLASK_APP=sample
     ```

   - For macOS/Linux:
     ```bash
     export FLASK_APP=sample
     ```

2. Run the Flask application:

   ```bash
   python -m flask run
   ```

## Setting up the CI/CD Pipeline with GitHub Actions

### The CI/CD pipeline is configured using GitHub Actions to automatically run tests on every push to the repository and deploy the application to Heroku if the tests pass.

### To set up the CI/CD pipeline for your own repository, follow these steps:

    1. Fork this repository to your GitHub account.

    2. Log in to Heroku or sign up for a new account if you don't have one.

    3. Create a new Heroku app from the Heroku dashboard.

    4. Generate an API key on Heroku:
    * Go to Account Settings.
    * Under the API Key section, click on "Generate API Key" and copy the API key.

    5. Add the Heroku API key as a secret in your GitHub repository:
    * Go to your repository on GitHub.
    * Navigate to Settings > Secrets.
    * Click on "New repository secret" and add a secret named HEROKU_API_KEY with the value of your Heroku API key.

    6. Configure the main.yml workflow file in the .github/workflows directory:
    * Update the heroku_app_name variable with the name of your Heroku app.
    * Update the heroku_email variable with the email associated with your Heroku account.

    7. Commit and push the changes to your GitHub repository.

    8. GitHub Actions will automatically run the CI/CD pipeline on every push to the repository. You can view the workflow runs in the "Actions" tab of your repository.

    9. Once the pipeline is successful, your Flask application will be deployed to Heroku, and you can access it using the provided Heroku app URL.
