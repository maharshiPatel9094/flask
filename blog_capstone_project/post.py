import requests
import os 
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("URL")

class Post:
    def __init__(self):
        response = requests.get(url)
        all_posts = response.json()
        self.posts = all_posts #give all the posts
        
    # get the post by id 
    def get_post(self,id):
        for post in self.posts:
            if post["id"] == id:
                # print(post)
                return post
    
    
# test run
if __name__ == "__main__":
    post_manager = Post()
    post_manager.get_post(2)