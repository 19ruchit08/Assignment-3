from flask import Flask, request, jsonify

app = Flask(_name_)

# Route to return student number
@app.route('/')
def home():
    return jsonify({"student_number": "200554055"})

# Route to handle Dialogflow webhook requests
@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    
    # Extract intent name from the request
    intent = req.get('queryResult', {}).get('intent', {}).get('displayName', '')

    # Example of handling different intents and generating responses
      if intent_name == 'elaborate':
        fulfillment_text = "Which concept would you like me to explain?"
      if intent_name == 'Mathmatics':
        fulfillment_text = "Sure! For Mathematics, try practicing problems daily, focus on understanding the concepts, and use visual aids like graphs "
      if intent_name == 'GetStudentNumber':
        fulfillment_text = "Your student number is 123456789."
    else:
        fulfillment_text = "Sorry, I didn't understand that."


    # Return the response in the required format
    return jsonify({
        "fulfillmentText": response_text
    })

if _name_ == '_main_':
    app.run(debug=True)