from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comments.db'
db = SQLAlchemy(app)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    comment = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Comment('{self.name}', '{self.email}', '{self.comment}')"

db.create_all()

@app.route("/comments", methods=["GET", "POST"])
def comments():
  if request.method == "POST":
    name = request.form["name"]
    email = request.form["email"]
    comment = request.form["comment"]
    # Store the comment in the database
    new_comment = Comment(name=name, email=email, comment=comment)
    db.session.add(new_comment)
    db.session.commit()
    return "Success"
  else:
    # Get the comments from the database
    comments = Comment.query.all()
    return jsonify([{'name': c.name, 'comment': c.comment} for c in comments])

if __name__ == "__main__":
  app.run()
