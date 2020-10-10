from locust import HttpUser, TaskSet, task, between

#def index(l):
    #l.client.get("/hello")

@task(2)
def index(self):
    self.client.get("/")

@task(1)
def profile(self):
    self.client.get("/hello")

class UserBehavior(TaskSet):
    tasks = {index: 1}
    


class WebsiteUser(HttpUser):
    tasks = UserBehavior
    wait_time = between(5.0, 9.0)