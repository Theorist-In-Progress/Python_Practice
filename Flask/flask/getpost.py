from flask import Flask,render_template,request
# render_template is responsible for redirecting to html page
'''
it creates an instance of the Flask class ,
which will be your WSGI application.
'''
### WSGI
app=Flask(__name__)
# as an argument we are giving the entry point of the application

@app.route("/")
def Welcome():
    return "<html><H1> welcome to the home page. This is amazing, absolute beauty of the course lies in its content </H1></html>"
# returing with HTML Tags, but its now a good pracitce to write like that its better to write a separate Html page
@app.route("/index")
def Index():
    return render_template('index.html')
## Important when render_template is redirecting it is going to look inside a praticular folder called as templates,
#  which is inside of  our main folder.
@app.route('/about')
# all these routes use http verb called get 
def about():
    return render_template('about.html')

@app.route("/form",methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']    
        # we are passing the name in method here because in html we have set id='name' to retrive that entire information 
        return f'hello {name}'
    return render_template('form.html')
@app.route("/Submit",methods=['GET','POST'])
def Submit():
    return render_template('index.html')
        # we are passing the name in method here because in html we have set id='name' to retrive that entire information 

    
if __name__=="__main__":
    app.run(debug=True)
    # debug= True , if we change something in the route welcome func . suppose wrtie an extra line in return,
    # so basically this will show the real time updates in the code to the web page just by clicking refresh in webpage 



''' User visits /form in the browser (GET request)
The browser sends a GET request to /form.
Flask runs the form() function.
Since the method is GET, it executes:
Flask renders and sends the form.html page (the HTML form) to the user.
2. User fills out the form and clicks Submit (POST request)
The browser sends a POST request to /form with the form data (e.g., name=Alice).
Flask runs the form() function again.
Now, request.method is 'POST', so it executes:
request.form['name'] gets the value the user entered in the text box (because the input’s name="name" in HTML).
Flask returns a response like hello Alice.
Background flow:
GET /form
→ Flask sends the HTML form to the browser.

User submits form
→ Browser sends POST request with form data.

POST /form
→ Flask retrieves the submitted data and sends a personalized response.

Key points:

The name attribute in <input name="name"> matches the key used in request.form['name'].
The id attribute is for HTML/JS; the name attribute is for form data submission.
Flask handles both GET (show form) and POST (process form) in the same route.'''