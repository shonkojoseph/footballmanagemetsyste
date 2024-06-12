from __init__ import CONN, CURSOR

class Player:

    all = {}

    def __init__(self, name, position, age=None, nationality=None, id=None):
        self.id = id
        self.name = name
        self.position = position
        self.age = age
        self.nationality = nationality

    def __repr__(self):
        return f"<Player {self.name} ({self.position}) - Age: {self.age}, Nationality: {self.nationality}>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE players (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                position TEXT NOT NULL,
                age INTEGER,
                nationality TEXT
            )
        """

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS players;
        """

        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO players (
                name, position, age, nationality
            ) VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(
            sql,
            (
                self.name,
                self.position,
                self.age,
                self.nationality,
            ),
        )
        CONN.commit()
        self.id = CURSOR.lastrowid

        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, position, age=None, nationality=None):
        player = cls(name, position, age, nationality)
        player.save()
        return player

    @classmethod
    def instance_from_db(cls, row):
        player = cls.all.get(row[0])

        if player:
            player.name = row[1]
            player.position = row[2]
            player.age = row[3]
            player.nationality = row[4]

        else:
            player = cls(
                row[1],
                row[2],
                row[3],
                row[4]
            )

            player.id = row[0]

            cls.all[player.id] = player

        return player 

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * FROM players WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()

        if row:
            return cls.instance_from_db(row)

        return None
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM players
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
   
    def update(self):
        sql = """
            UPDATE players SET name = ?, position = ?, age = ?, nationality = ?
            WHERE id = ?
        """

        CURSOR.execute(
            sql,
            (
                self.name,
                self.position,
                self.age,
                self.nationality,
                self.id,
            ),
        )

        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM players
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()
