import requests
import json
import random


class SocBot():
    number_of_users = 0
    max_post_per_user = 0
    max_likes_per_user = 0
    user_tokens = []

    def __init__(self, path):
        with open(path, 'r') as f:
            data = f.readlines()
        self.number_of_users = int(data[0])
        self.max_post_per_user = int(data[1])
        self.max_likes_per_user = int(data[2])


    def sign_up_users(self):
        for i in range(0, self.number_of_users):
            name = "user" + str(i)
            email = "user" + str(i) + "@gmail.com"
            password = "password" + str(i)
            r = requests.post('http://localhost:8000/users/', data={"username": name, "email": email, "password": password})
            self.user_tokens.append(json.loads(r.text)["token"])


    def create_posts(self):
        users = json.loads(requests.get("http://localhost:8000/users/").text)
        users_id = []
        for u in users:
            users_id.append(int(u["id"]))
        for i in range(0, len(users_id)):
            post_numbers = random.randint(1, self.max_post_per_user + 1)
            for u in users_id:
                for j in range(0, post_numbers):
                    title = str(u) + "title#" + str(j)
                    description = str(u) + "description#" + str(j)
                    r = requests.post('http://localhost:8000/posts/', data={"user": u, "title": title, "description": description})
                users_id.remove(u)


    def likes(self):
        users = self.user_tokens
        if len(users) > 0:
            posts = json.loads(requests.get("http://localhost:8000/posts/").text)
            posts_id = []
            for p in posts:
                posts_id.append(int(p["id"]))
            for i in range(0, len(users)):
                #post_to_like = random.choice(posts_id)
                for u in users:
                    likes_number = random.randint(1, self.max_likes_per_user + 1)
                    for j in range(0, likes_number):
                        post_to_like = random.choice(posts_id)
                        r = requests.post("http://localhost:8000/likes/" + str(post_to_like) + "/", data={"token": u})
                    users.remove(u)



bot = SocBot("config.txt")
bot.sign_up_users()
bot.create_posts()
bot.likes()
