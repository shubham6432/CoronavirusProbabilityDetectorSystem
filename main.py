from flask import Flask, render_template,request
app = Flask(__name__)
import pickle


# open a file, where you stored the pickled data
file = open('model.pkl', 'rb')

# dump information to that file
clf = pickle.load(file)
file.close()

@app.route('/' , methods =["GET", "POST"])

def hello_world():
    if request.method == "POST" :
        myDict = request.form

        Fever = int(myDict['Fever'])
        Age  = int(myDict['Age'])
        BodyPain = int(myDict['BodyPain'])
        RunnyNose = int(myDict['RunnyNose'])
        DiffBreath =int(myDict['DiffBreath'])

        inputfeature =[Fever, BodyPain, Age, RunnyNose, DiffBreath]
        infprob = clf.predict_proba([inputfeature])[0][1]
        print(infprob)
        return render_template("show.html", inf=round(infprob*100))
    return render_template("index.html")
    #return 'Hello, World!' + str(infprob)


if __name__ ==  "__main__":

    app.run(debug = True)