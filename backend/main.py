from flask import request, jsonify
from config import app, db
from models import Contact

# create new route, specifiy which route to go to, specify which methods are valid 
@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()  # gets all contacts from DB
    json_contacts = list(map(lambda x: x.to_jason(), contacts))  # objects -> jsons
    return jsonify({"contacts": json_contacts})

@app.route("/create_contact", methods=["POST"])
def create_contact():
    

if __name__ == "__main__":
    with app.app_context():
        db.create_all
    
    app.run(debug=True)

