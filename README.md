# Django Template

![Project Logo](../src/static/django-logo-negative.png)

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)


## Configuration

Before running the project, you need to configure certain settings. Follow the instructions below:

1. Rename the `.env.example` file to `.env`:

   ```shell
   mv .env.example .env
   
2. #### Open the .env file in a text editor and provide the necessary values for the environment variables:
    SECRET_KEY=your_secret_key

    DEBUG=True

    DATABASE_URL=your_database_url


## Installation

You can choose either of the following methods to install and set up the project:

### Docker Installation

1. Make sure you have Docker installed on your system. Refer to the [Docker documentation](https://docs.docker.com/get-docker/) for installation instructions.


2. Clone the repository:
    ```
    git clone https://gitlab.com/nurbol0tt/django-clean-architecture.git
    ```
   2.1 Build the Docker image and start the container:
   ```
    cd my-project
   ```
   ```
    docker-compose up --build
   ```

3. Access the application at http://localhost:8000.
___


### Manual Installation

1. Clone the repository:
    ```
    git clone https://gitlab.com/nurbol0tt/django-clean-architecture.git
    ```

2. Create a virtual environment:
    ```
    cd my-project
    python -m venv env
    ```

3. Activate the virtual environment:
   * For Windows:
      ```
      .\env\Scripts\activate
      ```
   * For Unix/macOS:
      ```
      source env/bin/activate
      ```
     

4. Install the dependencies:
    ```
    poetry install
    ```

5. Perform database migrations:
   ```
   python manage.py migrate
   ```

6. Run the development server:

   ``` 
   python manage.py runserver
   ```
   
7. Access the application at http://localhost:8000.


# Usage

The Usage section provides guidance on how to use and interact with the project. It covers various aspects and features to help you make the most of the project's capabilities.

## Authentication

- [User Registration](user-registration.md): Learn how to register new users.
- [User Login](user-login.md): Understand the process of logging in to the application.
- [Password Reset](password-reset.md): Find out how to reset your password if you forget it.

## Views

- [Dashboard](dashboard.md): Explore the dashboard view and its functionalities.
- [Data Analysis](data-analysis.md): Learn how to perform data analysis using the project's built-in tools.
- [Report Generation](report-generation.md): Understand how to generate reports based on the collected data.

## API Reference

- [Endpoints](api-endpoints.md): View the available API endpoints and their functionalities.
- [Authentication](api-authentication.md): Learn how to authenticate API requests.

For more detailed instructions and examples, click on the links provided in each subsection above.


## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please feel free to contribute.

To contribute to the project, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make the necessary changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.

For more details, please refer to the [contribution guidelines](CONTRIBUTING.md).


## License

This project is licensed under the [MIT License](LICENSE).
