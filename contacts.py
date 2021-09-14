from flask import Flask,jsonify,request

app = Flask(__name__)
contacts = [
    {
        "ID":1,"Contact":"9856321478","Name":"Maheerr",
    },
    {
        "ID":2,"Contact":"9876543210","Name":"Payel mam",
    },
]

@app.route("/add-contact",methods=["POST"])
def addContact():
    if not request.json:
        return jsonify({
            "status":"error","message":"please provide the data"
        },400)
    contact = {
        "ID":contacts[-1]["ID"]+1,"Contact":request.json["Contact"],"Name":request.json.get("Name",""),
    }        
    contacts.append(contact)
    return jsonify({
            "status":"success","message":"task added successfully"
        },200) 


@app.route("/get-contact")
def get_contacts():
    return jsonify({
        "data":contacts
    })

if(__name__=="__main__"):
    app.run(debug=True)