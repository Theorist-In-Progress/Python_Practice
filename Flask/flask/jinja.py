# building url dynamically 
# varibale rule and jinja 2 template engine
from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)
# as an argument we are giving the entry point of the application

@app.route("/")
def Welcome():
    return "<html><H1> welcome to the home page. This is amazing, absolute beauty of the course lies in its content </H1></html>"
# returing with HTML Tags, but its now a good pracitce to write like that its better to write a separate Html page
@app.route("/index")
def Index():
    return render_template('index.html')

@app.route("/Submit",methods=['GET','POST'])
def Submit():
    if request.method=='POST':
        name=request.form['name']    
        return f'hello {name}'
    return render_template('form.html')

##variable rule
@app.route("/Success/<int:score>")
def Success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
        ## now we will try to return our result to our html page 
    return render_template('result.html',results=res)
    # here we are passing our value to html page 
@app.route("/Successres/<int:score>")
def Successres(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    exp={'Score':score,'res':res}
        ## now we will try to return our result to our html page 
    return render_template('result1.html',results=exp)
## iF CONDITION 
@app.route("/Successif/<int:score>")
def Successif(score):
    

        ## now we will try to return our result to our html page 
    return render_template('result.html',results=score)

## building url dynamically
## so what we are trying to do over here is ..first we will get our result which will calculate our average result 
# if result is pass then it will route us to success page otherwise fail page 
@app.route("/fail/<int:score>")
def fail(score):
   
        ## now we will try to return our result to our html page 
    return render_template('result1.html',results=score)
@app.route('/getresults',methods=['POST','GET'])
def getresults():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['data_science'])
        total_score=(science+maths+c+data_science)/4
    else:
        return render_template('getresults.html')
    return redirect(url_for('Successres',score=total_score))
# so url_for helping to create dynamic url and redirect is for redirecting 






if __name__=="__main__":
    app.run(debug=True)