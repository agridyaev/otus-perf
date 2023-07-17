import time

def hello_world(user):
    user.client.get("/")


def view_items(user):
    for id_ in range(10):
        resp = user.client.get(f"/item?id={id_}", name="/item")
        # resp = user.client.get(f"/item?id={id_}")
        assert "<html><body><h1>hi!</h1></body></html>" in resp.text
        time.sleep(1)


def view_errors(user):
    raise Exception("Error")
