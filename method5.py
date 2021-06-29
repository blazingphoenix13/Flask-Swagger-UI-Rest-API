from flask import render_template
import connexion

# Create the application instance
app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger1.yml')

# Create a URL route in our application for "/"
@app.route('/')
def home():
    return render_template('home1.html')

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


# Epoints to check
# localhost:5000    -> home1.html
# localhost:5000/api/people    -> displays all people (first_name,last_name,timestamp)
# localhost:5000/api/people/last_name    -> displays person with given last_name
# localhost:5000/api/ui    -> displays all REST API methods using Swagger UI
#  
