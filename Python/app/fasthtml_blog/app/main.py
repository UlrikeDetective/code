from fasthtml import FastHTML
from app.templates import blog_list_template, create_post_template
from app.models import get_all_posts, create_post
from app.database import create_tables
import os
from starlette.responses import FileResponse

app = FastHTML()

@app.route("/static/{filename}")
async def static_file(request, filename: str):
    file_path = os.path.join("app", "static", filename)
    if os.path.isfile(file_path):
        return FileResponse(file_path)
    else:
        return FileResponse(status_code=404)

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
    form_data = await request.form()
    title = form_data.get("title")
    content = form_data.get("content")
    create_post(title, content)
    
    # Return HTML with CSS class for styling
    return f"""
    <html>
        <head>
            <link rel="stylesheet" href="/static/styles.css">
        </head>
        <body>
            <div class="success-message">
                <h2>Post '{title}' created!</h2>
                <a href="/">Go back</a>
            </div>
        </body>
    </html>
    """
