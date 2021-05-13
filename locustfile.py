import time
from locust import HttpUser, task, between, constant, constant_pacing


class QuickStartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def hello_world(self):
        self.client.get("/")

    @task(2)
    def view_items(self):
        for id_ in range(10):
            resp = self.client.get(f"/item?id={id_}", name="/item")
            # resp = self.client.get(f"/item?id={id_}")
            assert "<html><body><h1>hi!</h1></body></html>" in resp.text
            time.sleep(1)

    @task(3)
    def view_errors(self):
        raise Exception("Error")

    def on_start(self):
        print("on start")
        # self.client.post("/login", json={"username": "foo", "password": "bar"})

    def on_stop(self):
        print("on stop")
