from flaskblog import app, db

if __name__ == '__main__':
    with app.app_context():
        # Create all the tables if they don't exist
        db.create_all()

    # Run the Flask app in debug mode
    app.run(debug=True, host="0.0.0.0")
