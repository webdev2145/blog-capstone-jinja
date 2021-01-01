from flask import Flask, render_template
import post


app = Flask(__name__)

my_posts = post.Post()

@app.route('/')
def home():

    return render_template("index.html", posts=my_posts.posts)


@app.route('/post/<int:post_id>')
def get_blog(post_id):
    return render_template('post.html', posts=my_posts.posts, id=post_id)


if __name__ == "__main__":
    app.run(debug=True)
