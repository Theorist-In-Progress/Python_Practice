from flask import Flask
'''
it creates an instance of the Flask class ,
which will be your WSGI application.
'''
### WSGI
app=Flask(__name__)
# as an argument we are giving the entry point of the application

@app.route("/")
def Welcome():
    return "welcome to the home page. This is amazing, absolute beauty of the course lies in its content"
# now whenever we hit this / along with our url , this function is going to get executed.
@app.route("/index")
def Index():
    return "welcome to the index page"

if __name__=="__main__":
    app.run(debug=True)
    # debug= True , if we change something in the route welcome func . suppose wrtie an extra line in return,
    # so basically this will show the real time updates in the code to the web page just by clicking refresh in webpage 

''' we can create any number of routes '''
