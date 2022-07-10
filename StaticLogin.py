import time
import webbrowser
from multiprocessing import Process
from threading import Timer, Thread
from tkinter import *


from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from flask import Flask, send_file, render_template, request, session,flash, request, redirect, url_for
from functools import partial

import os
import urllib.request
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 800 * 800


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def Static_LoginPortal(login_screen,username,password):
    if (username.get() == "test" and password.get() == "test"):
        text = Text(login_screen)
        text.insert(INSERT, "Login Successful !")
        print("Login Successful !")
        print(" Credentials !!!", username.get() and password.get())
        print("Your file will be downloaded shortly !")
        login_screen.destroy()
        Timer(1, open_download_portal).start();
        app.run(port=5000)  # Replace port number for your localhost here

    else:
        tkWindow = Tk()
        tkWindow.geometry('400x150')
        text = Text(tkWindow)
        text.insert(INSERT, "Invalid Credentials !!!")
        text.insert(END, "\nPlease enter valid credentials")
        text.pack()
        print("Invalid Credentials !!!", username.get())

    return

def Display_Screen():
    print("Im here")
    login_screen = Tk()  # create a GUI window

    login_screen.geometry("400x510")  # set the configuration of GUI window
    login_screen.title("Login Account")  # set the title of GUI window

    # create a Form label
    Label(login_screen,text="Login to Download the File", bg="white", width="300", height="2", font=('Arial', 14)).pack()
    Label(login_screen,text="").pack()

    username_verify = StringVar()
    password_verify = StringVar()
    Label(login_screen, text="Username").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()

    Label(login_screen, text="").pack()
    Label(login_screen, text="Password").pack()
    password__login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password__login_entry.pack()
    Label(login_screen, text="").pack()
    print("userName", username_login_entry)
    Button(login_screen,text="Sign In", height="2", width="30", command=partial(Static_LoginPortal,login_screen,username_verify,password_verify)).pack()
    Label(login_screen,text="").pack()

    Button(login_screen,text="Login with Linkedin", height="2", width="30", command=lambda:Linkedin_LoginPortal(login_screen, username_verify, password_verify)).pack()
    Label(login_screen,text="").pack()

    Button(login_screen,text="Login with GitHub", height="2", width="30", command=lambda:GitHUB_LoginPortal(login_screen, username_verify, password_verify)).pack()
    Label(login_screen,text="").pack()

    Button(login_screen,text="Login with Facebook", height="2", width="30", command= lambda:FB_LoginPortal(login_screen, username_verify, password_verify)).pack()
    Label(login_screen,text="").pack()

    Button(login_screen,text="Login with Google", height="2", width="30", command=lambda:GO_LoginPortal(login_screen, username_verify, password_verify)).pack()
    Label(login_screen,text="").pack()

    login_screen.mainloop()  # start the GUI


def GitHUB_LoginPortal(screen , usr, passwd):
    # place the chromedriver.exe in the same path as the project
    driver = webdriver.Chrome('./chromedriver')
    driver.get("https://www.github.com/login")

    # html ID of username in github page is "login_field"
    username_box = driver.find_element(By.ID,'login_field')
    username_box.send_keys(usr.get())

    # html ID of password in github page is "password"
    password_box = driver.find_element(By.ID,'password')
    password_box.send_keys(passwd.get())

    password_box.send_keys(Keys.RETURN)

    # wait for 5 seconds for login process
    time.sleep(5)

    try:
        # check for password box after 5sec waiting, if still present login failed
        login_check = driver.find_element(By.ID,'password')
        print("Invalid Credentials !!!")
        driver.close()
    except NoSuchElementException:
        print("Login Successful !")
        print("Your file will be downloaded shortly !")
        driver.close()
        screen.destroy()
        Timer(1, open_download_portal).start();
        app.run(port=5000)  # Replace port number for your localhost here

    driver.quit()

    return


def Linkedin_LoginPortal(screen , usr, passwd):
    # place the chromedriver.exe in the same path as the project
    driver = webdriver.Chrome('./chromedriver')
    driver.get("https://www.linkedin.com/")

    # html ID of username in linkedIn page is "session_key"
    username_box = driver.find_element(By.ID,'session_key')
    username_box.send_keys(usr.get())

    # html ID of password in linkedIn page is "session_password"
    password_box = driver.find_element(By.ID,'session_password')
    password_box.send_keys(passwd.get())

    password_box.send_keys(Keys.RETURN)

    # wait for 5 seconds for login process
    time.sleep(5)

    try:
        # check for password box after 5sec waiting, if still present login failed
        login_check = driver.find_element(By.ID,'password')
        print("Invalid Credentials !!!")
        driver.close()
    except NoSuchElementException:
        print("Login Successful !")
        print("Your file will be downloaded shortly !")
        driver.close()
        screen.destroy()
        Timer(1, open_download_portal).start();
        app.run(port=5000)  # Replace port number for your localhost here

    driver.quit()

    return


def FB_LoginPortal(screen , usr, passwd):
    # place the chromedriver.exe in the same path as the project
    driver = webdriver.Chrome('./chromedriver')
    driver.get("https://www.facebook.com/")

    # html ID of username in facebook page is "email"
    username_box = driver.find_element(By.ID,'email')
    username_box.send_keys(usr.get())

    # html ID of password in facebook page is "pass"
    password_box = driver.find_element(By.ID,'pass')
    password_box.send_keys(passwd.get())

    password_box.send_keys(Keys.RETURN)

    # wait for 5 seconds for login process
    time.sleep(3)

    try:
        # check for password box after 5sec waiting, if still present login failed
        login_check = driver.find_element(By.ID,'pass')
        print("Invalid Credentials !!!")
        driver.close()
    except NoSuchElementException:
        print("Login Successful !")
        print("Your file will be downloaded shortly !")
        driver.close()
        screen.destroy()
        Timer(1, open_download_portal).start();
        app.run(port=5000)  # Replace port number for your localhost here

    driver.quit()

    return


# Google has security issue with browser automation
def GO_LoginPortal(screen , usr, passwd):
    # place the chromedriver.exe in the same path as the project
    driver = webdriver.Chrome('./chromedriver')
    driver.get("https://accounts.google.com/signin/v2/identifier?service=CPanel&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

    # html ID of username in google page is "identifierId"
    username_box = driver.find_element(By.ID,'identifierId')
    username_box.send_keys(usr.get())

    username_box.send_keys(Keys.RETURN)


    # html name of password in google page is "password"
    password_box = driver.find_element(By.ID,'password')
    password_box.send_keys(passwd.get())

    password_box.send_keys(Keys.RETURN)

    # wait for 5 seconds for login process
    time.sleep(5)

    try:
        # check for password box after 5sec waiting, if still present login failed
        login_check = driver.find_element(By.name,'password')
        print("Invalid Credentials !!!")
        driver.close()
    except NoSuchElementException:
        print("Login Successful !")
        print("Your file will be downloaded shortly !")
        driver.close()
        screen.destroy()
        Timer(1, open_download_portal).start();
        app.run(port=5000)  # Replace port number for your localhost here

    driver.quit()

    return


@app.route('/')
def upload_form():
    # place the download.html file in a new folder named "templates" in the project path
    return render_template('download.html')


@app.route('/download')
def download_file():
    # keep the file to be uploaded to the server and downloaded by user in the same path a project
    path = "your_file.txt"
    return send_file(path, as_attachment=True)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    Timer(1, Display_Screen).start()
    return "logged out successfully !! \n Login again through GUI window"


@app.route('/contactUs')
def contactus():
    # place the download.html file in a new folder named "templates" in the project path
    return render_template('ContactUs.html')


@app.route('/softwareEngineering')
def se():
    # place the download.html file in a new folder named "templates" in the project path
    return render_template('SoftwareEngineering.html')


@app.route('/flag', methods=['GET', 'POST'])
def flag():
    # place the download.html file in a new folder named "templates" in the project path
    path = 'static/uploads/'
    uploads = sorted(os.listdir(path), key=lambda x: os.path.getctime(path + x))  # Sorting as per image upload date and time
    print(uploads)
    # uploads = os.listdir('static/uploads')
    uploads = ['uploads/' + file for file in uploads]
    uploads.reverse()
    return render_template('FlagCopy.html',uploads=uploads)


def open_download_portal():
    webbrowser.open_new('http://127.0.0.1:5000/')


app.config['UPLOAD_PATH'] = 'static/uploads'
@app.route('/uploadSubmit', methods=['POST', 'GET'])
def upload_image():
    if request.method == 'POST':
        f = request.files['file']
        print(f.filename)
        # f.save(secure_filename(f.filename))
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        return redirect("/flag")


@app.route('/display/<filename>')
def display_image(filename):
    print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


def main():
    Display_Screen()


if __name__ == '__main__':
    main()