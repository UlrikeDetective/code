def blog_list_template(posts):
    return f"""
    <html>
        <head><title>Blog Posts</title></head>
        <body>
            <h1>All Blog Posts</h1>
            <ul>
                {''.join([f'<li>{post.title}</li>' for post in posts])}
            </ul>
            <a href="/create">Create a new post</a>
        </body>
    </html>
    """

def create_post_template():
    return """
    <html>
        <head><title>Create Post</title></head>
        <body>
            <h1>Create a New Blog Post</h1>
            <form action="/create" method="post">
                <label for="title">Title:</label><br>
                <input type="text" id="title" name="title"><br>
                <label for="content">Content:</label><br>
                <textarea id="content" name="content"></textarea><br>
                <input type="submit" value="Submit">
            </form>
            <a href="/">Back to posts</a>
        </body>
    </html>
    """
