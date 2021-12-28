<h1 align="center">drf postgres

### Project Setup :

**Note :** *This project requires net connection to run because it is build using ElephantSQL (free PostgreSQL database hosting service).*
  
Prerequisites
1. python3
2. pip3


3. Clone the project.

    ```shell
    git clone https://github.com/shashank725/drf_postgres.git
    ```
    

4. Create a virtual environment with venv (install virtualenv, if its not installed) inside the project floder.
  
    ```shell
    cd drf_postgres
    ```
  
   #### For Linux/Mac OSX
    ```shell
    sudo apt-get install python3-venv
    python3 -m venv venv
    ```
  
   #### For Windows
    ```shell
    pip install virtualenv
    python -m venv venv
    ```


5. Activate the virtual environemnt.

    #### For Linux/Mac OSX
    ```shell
    source venv/bin/activate

    ```

    #### For Windows
    ```shell
    venv\Scripts\activate

    ```
   
6. Install the requirements.

    ```shell
    pip install -r requirements.txt
    ```
 

7. Run the development server

    ```
    python manage.py runserver

    ```
  
8. Head to server http://127.0.0.1:8000
  
  Admin
  Username : admin
  Password : admin
