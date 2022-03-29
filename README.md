### Requirements ,Packages used and Installation
Download and install Python, for this tutorial I'll be using Python 3.8.5, make sure to check the box Add Python to PATH on the installation setup screen
 
### Installation
          
Navigate to your current project directory for this case it will be **CLINICA**. <br>
          
### 1 .Create an environment
          
Depending on your operating system,make a virtual environment to avoid messing with your machine's primary dependencies
          
**Windows**
          
```

cd CLINICA
py -3 -m venv venv

```
### 2 .Activate the environment
          
**Windows** 

```venv\Scripts\activate```
          

### 3 .Install the requirements

Applies for windows/macOS/Linux

```pip install -r requirements.txt```
  
### 4. Run the application 

**On windows**
```
set FLASK_APP=main
flask run
