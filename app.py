from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")

def hello_world():

    return "<p>Hello, World!</p>"



@app.route("/Formulario",methods=["GET","POST"])

def formulario():

    if request.method == "POST":

        a = int (request.form["datoA"])

        b = int (request.form["datoB"])
        
        c = int (request.form["datoC"])

        #print(int(A)+int(B))

        R1 = (-b + ((b**2) - 4 *a*c)**(1/2)) / (2*a)
        R2 = (-b - ((b**2) - 4 *a*c)**(1/2)) / (2*a)

        

        return render_template("Formulario.html",c=c,a=a,b=b,R1=R1,R2=R2)

    return render_template("Formulario.html")



if __name__=="__main__":

    app.run()