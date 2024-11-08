from app.database import get_db

class BlogPost:
    def __init__(self, id: int, title: str, content: str):
        self.id = id
        self.title = title
        self.content = content

def get_all_posts():
    with get_db() as conn:
        cursor = conn.execute('SELECT id, title, content FROM blog_posts')
        rows = cursor.fetchall()
        return [BlogPost(id=row[0], title=row[1], content=row[2]) for row in rows]

def create_post(title: str, content: str):
    with get_db() as conn:
        conn.execute('INSERT INTO blog_posts (title, content) VALUES (?, ?)', (title, content))
