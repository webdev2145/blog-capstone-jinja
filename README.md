README

This project was done as part of my participation in the 100 Days of Code Challenge

Python and Jinja was used to generate dynamic content for the webpages

Functionality:
import requests
URL = 'https://api.npoint.io/5abcca6f4e39b4955965'
Angela Yu from App Brewery created the data for the posts

I used a class to keep the main.py file clutter free
class Post:

    def __init__(self):
        # URL = 'https://api.npoint.io/5abcca6f4e39b4955965'
        self.responses = requests.get(url=URL)
        self.posts = self.responses.json()

The index page list the title and subtitle of available blog posts

Dynamically generated contents for the index page:
<div class="wrapper">
    <div class="top">
        <div class="title"><h1>My Blog</h1></div>
    </div>
    <br>
    {% for post in posts: %}
        <div class="content">
            <div class="card">
                <h2>{{ post['title'] }}</h2>
                <p class="text">{{ post['subtitle'] }} </p>
                <a href="{{ url_for('get_blog', post_id=post['id']) }}">Read</a>
            </div>
        </div>
    {% endfor %}

</div>

call for individual posts and contents
I passed the id received from the link and the Posts object posts var
@app.route('/post/<int:post_id>')
def get_blog(post_id):
    return render_template('post.html', posts=my_posts.posts, id=post_id)

The body of the post is displayed after clicking the read link on the index page:

<div class="wrapper">
    <div class="top">
        <div class="title"><h1>My Blog</h1></div>
    </div>

        <div class="content">
            <div class="card">
                {% for post in posts: %}
                    {% if post['id'] == id: %}
                        <h2>{{ post['title'] }}</h2>
                        <p>{{ post['body'] }}</p>
                    {% else: %}
                        {{ continue }}
                    {% endif %}
                {% endfor %}
            </div>
        </div>

</div>