from flask import Flask,render_template 
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
if __name__=="__main__":
    app.run(debug=True)
    # debug= True , if we change something in the route welcome func . suppose wrtie an extra line in return,
    # so basically this will show the real time updates in the code to the web page just by clicking refresh in webpage 

''' we can create any number of routes '''