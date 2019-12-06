from locust import HttpLocust, TaskSet


def login(user):
    """
    :param user: login function is created
    """
    user.client.post("/login/", {"username": "admin", "password": "admin"})


def index(user):
    """
    :param user: index function is created
    """
    user.client.get("/")


def forget(user):
    """
      :param user: index function is created
      """
    user.client.post("/forgotpassword", {"email": "sachinsanju04@gmail.com"})


class UserBehavior(TaskSet):
    tasks = {index: 2, forget: 5}

    def on_start(self):
        login(self)

    

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
