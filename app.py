from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import jwt
from functools import wraps

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/cricbuzz'
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(20), default='guest')

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_1 = db.Column(db.String(50), nullable=False)
    team_2 = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False)
    venue = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default='upcoming')

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    matches_played = db.Column(db.Integer, default=0)
    runs = db.Column(db.Integer, default=0)
    average = db.Column(db.Float, default=0.0)
    strike_rate = db.Column(db.Float, default=0.0)

# Decorator to authenticate and authorize admin users
def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization', None)
        if not token:
            return jsonify({'message': 'No token provided.'}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = User.query.filter_by(id=data['user_id']).first()
            if current_user.role != 'admin':
                return jsonify({'message': 'Unauthorized access.'}), 403
        except:
            return jsonify({'message': 'Invalid token.'}), 403
        return f(*args, **kwargs)
    return decorated

# API endpoints
@app.route('/api/admin/signup', methods=['POST'])
def admin_signup():
    # Implement admin user registration

@app.route('/api/admin/login', methods=['POST'])
def admin_login():
    # Implement admin user login and JWT token generation

@app.route('/api/matches', methods=['POST'])
@admin_required
def create_match():
    # Implement match creation by admin

@app.route('/api/matches', methods=['GET'])
def get_matches():
    # Implement fetching the list of all matches

@app.route('/api/matches/<int:match_id>', methods=['GET'])
def get_match_details(match_id):
    # Implement fetching the details of a specific match

@app.route('/api/teams/<int:team_id>/squad', methods=['POST'])
@admin_required
def add_player_to_squad(team_id):
    # Implement adding a player to a team's squad

@app.route('/api/players/<int:player_id>/stats', methods=['GET'])
def get_player_stats(player_id):
    # Implement fetching the player statistics

if __name__ == '__main__':
    app.run(debug=True)
