from fasthtml import FastHTML
from app.templates import blog_list_template, create_post_template
from app.models import get_all_posts, create_post
from app.database import create_tables
import os

app = FastHTML()

# Define a route for static files
@app.route("/static/styles.css")
def static_file(filename):
    file_path = os.path.join("app", "static", filename)
    if os.path.isfile(file_path):
        with open(file_path, "rb") as file:
            content = file.read()
        # Set Content-Type based on file extension (e.g., "text/css" for CSS files)
        if filename.endswith(".css"):
            return content, {"Content-Type": "text/css"}
        elif filename.endswith(".js"):
            return content, {"Content-Type": "application/javascript"}
        elif filename.endswith(".png"):
            return content, {"Content-Type": "image/png"}
        # Add more content types as needed
    else:
        return "File not found", 404

# Create the database tables before starting the app
create_tables()

@app.route("/")
def index():
    posts = get_all_posts()
    return blog_list_template(posts)

@app.route("/create", methods=["GET"])
def create_post_get():
    return create_post_template()

# Define this as an async function to handle form data properly
@app.route("/create", methods=["POST"])
async def create_post_post(request):
    form_data = await request.form()  # Await for the form data
    title = form_data.get("title")
    content = form_data.get("content")
    create_post(title, content)
    return f"<h2>Post '{title}' created! <a href='/'>Go back</a></h2>"
