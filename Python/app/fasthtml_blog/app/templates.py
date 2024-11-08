def blog_list_template(posts):
    return f"""
    <html>
        <head>
            <title>Blog Posts</title>
            <link rel="stylesheet" href="/static/styles.css">
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Cutive+Mono&family=Pacifico&display=swap" rel="stylesheet">
        </head>
        <body>
            <h1>All Blog Posts</h1>
            <ul>
                {''.join([f'<li>{post.title}</li>' for post in posts])}
            </ul>
            <div style="text-align: left;">
                <a href="/create">Create a new post</a>
            </div>
        </body>
    </html>
    """


def create_post_template():
    return """
    <html>
        <head>
            <title>Create Post</title>
            <link rel="stylesheet" href="/static/styles.css">
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Cutive+Mono&family=Pacifico&display=swap" rel="stylesheet">
        </head>
        <body>
            <h1>Create a New Blog Post</h1>
            <form action="/create" method="post">
                <label for="title">Title:</label>
                <input type="text" id="title" name="title">
                
                <label for="content">Content:</label>
                <textarea id="content" name="content"></textarea>
                
                <input type="submit" value="Submit">
            </form>
            <a href="/">Back to posts</a>
        </body>
    </html>
    """

