from flask import Flask, render_template
import json
import auth

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def main():
  # Return the content view
  return render_template("index.html", output="""
  <p>To see a blog's posts, enter the blog name in the URL:</p>
  <pre><code>https://anonblr.cleberg.io/blog_name</code></pre>
  <p>(WIP) To see multiple blogs, add a <code>+</code> sign between the blogs:</p>
  <pre><code>https://anonblr.cleberg.io/blog_one+blog_two</code></pre>
  <br>
  <a href="/funnytwittertweets">Example &rarr;</a>
  """)

@app.route("/<blog>")
def blogroll(blog):
  # Authenticate with Tumblr
  client = auth.login()

  # TODO: Create method to check if the URL contains multiple blogs

  # Return blog posts
  # TODO: Create a better method of checking post types so the following logic 
  # can use the correct JSON object more effectively
  output = str()
  data = client.posts(blog)
  for post in data["posts"]:
    try:
      output = f"{output}<div class='post'>{post['body']}</div>"
    except:
      print(f"Error: `body` not found in post `{post['id']}`. Looking for photos instead.")
      try:
        photo_set = str()
        photos = post['photos']
        for photo in photos:
          photo_set = photo_set + f"<img src={photo['original_size']['url']}>" + "<br>"
        output = output + photo_set
      except:
        print(f"Error: `photos` not found in post {post['id']}.")

  return render_template("index.html", output=output)
