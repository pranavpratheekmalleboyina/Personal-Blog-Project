# Personal-Blog-Project
This is a small blog project that I have built using the Django framework

## Scripts

Here are some scripts that you can run regarding the posts and the users.

`user.py`
``` python
from blog.models import Post
from django.contrib.auth.models import User
#you can run the following lines to get a hang of the concept.
User.objects.all() #to get all the users added so far
User.objects.first() #to get just the first 
User.objects.filter(name='username')
User.objects.filter(name='username').first()
user = User.objects.filter(name='username').first()
# you can create a small , sample post in the following way.
post1 = Post(title='title_name',
             content= 'content',
             author = user)
post1.save() # saves the post             
```

`post.py`
``` python
from blog.models import Post
from django.contrib.auth.models import User
user = User.objects.filter(name='username').first()
post2 = Post(title='title_name',
             content= 'content',
             author = user)
post2.save()
Post.objects.all() # to get all the posts created so far
user.post_set # gets all the posts of a particular use 
user.post_set.create(
             title='title_name',
             content= 'content',
             author = user
)
```

