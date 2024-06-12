from __init__ import CONN, CURSOR

class Team:

    all = {}

    def __init__(self, name, coach, stadium, id=None):
        self.id = id
        self.name = name
        self.coach = coach
        self.stadium = stadium

    def __repr__(self):
        return f"<Team {self.name} - Coach: {self.coach}, Stadium: {self.stadium}>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE teams (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                coach TEXT NOT NULL,
                stadium TEXT NOT NULL
            )
        """

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS teams;
        """

        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO teams (
                name, coach, stadium
            ) VALUES (?, ?, ?)
        """

        CURSOR.execute(
            sql,
            (
                self.name,
                self.coach,
                self.stadium
            ),
        )
        CONN.commit()
        self.id = CURSOR.lastrowid

        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, coach, stadium):
        team = cls(name, coach, stadium)
        team.save()
        return team

    @classmethod
    def instance_from_db(cls, row):
        team = cls.all.get(row[0])

        if team:
            team.name = row[1]
            team.coach = row[2]
            team.stadium = row[3]

        else:
            team = cls(
                row[1],
                row[2],
                row[3]
            )

            team.id = row[0]

            cls.all[team.id] = team

        return team

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * FROM teams WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()

        if row:
            return cls.instance_from_db(row)

        return None
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM teams
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
   
    def update(self):
        sql = """
            UPDATE teams SET name = ?, coach = ?, stadium = ?
            WHERE id = ?
        """

        CURSOR.execute(
            sql,
            (
                self.name,
                self.coach,
                self.stadium,
                self.id,
            ),
        )

        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM teams
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

