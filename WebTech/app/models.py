from app import db


class Income(db.Model):
    income_id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float)
    desc = db.Column(db.String(500), index=True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '{} {} {} {}'.format(self.income_id,
                                    self.amount,
                                    self.desc,
                                    self.user_id)


class Expenditure(db.Model):
    expenditure_id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float)
    desc = db.Column(db.String(500), index=True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '{} {} {} {}'.format(self.expenditure_id,
                                    self.amount,
                                    self.desc,
                                    self.user_id)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    goal = db.Column(db.Float)
    incomes = db.relationship('Income',
                              backref='user',
                              lazy='dynamic')
    expenditures = db.relationship('Expenditure',
                                   backref='user',
                                   lazy='dynamic')

    def __repr__(self):
        return '{} {}'.format(self.id, self.goal)
