from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = {}
users = {}

task_id = 1
user_id = 1


# -----------------------
# GET ENDPOINTS
# -----------------------

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)


@app.route("/tasks/<int:id>", methods=["GET"])
def get_task(id):
    if id in tasks:
        return jsonify(tasks[id])
    return jsonify({"error": "Task not found"}), 404


# -----------------------
# POST ENDPOINTS
# -----------------------

@app.route("/tasks", methods=["POST"])
def create_task():
    global task_id

    data = request.json

    new_task = {
        "id": task_id,
        "title": data["title"],
        "completed": False
    }

    tasks[task_id] = new_task
    task_id += 1

    return jsonify(new_task)


@app.route("/users", methods=["POST"])
def create_user():
    global user_id

    data = request.json

    new_user = {
        "id": user_id,
        "name": data["name"],
        "email": data["email"]
    }

    users[user_id] = new_user
    user_id += 1

    return jsonify(new_user)


# -----------------------
# PUT ENDPOINTS
# -----------------------

@app.route("/tasks/<int:id>", methods=["PUT"])
def replace_task(id):

    if id not in tasks:
        return jsonify({"error": "Task not found"}), 404

    data = request.json

    tasks[id] = {
        "id": id,
        "title": data["title"],
        "completed": data["completed"]
    }

    return jsonify(tasks[id])


@app.route("/users/<int:id>", methods=["PUT"])
def replace_user(id):

    if id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.json

    users[id] = {
        "id": id,
        "name": data["name"],
        "email": data["email"]
    }

    return jsonify(users[id])


# -----------------------
# PATCH ENDPOINTS
# -----------------------

@app.route("/tasks/<int:id>/complete", methods=["PATCH"])
def complete_task(id):

    if id not in tasks:
        return jsonify({"error": "Task not found"}), 404

    tasks[id]["completed"] = True

    return jsonify(tasks[id])


@app.route("/users/<int:id>/email", methods=["PATCH"])
def update_email(id):

    if id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.json

    users[id]["email"] = data["email"]

    return jsonify(users[id])


# -----------------------
# DELETE ENDPOINTS
# -----------------------

@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):

    if id not in tasks:
        return jsonify({"error": "Task not found"}), 404

    deleted = tasks.pop(id)

    return jsonify({"deleted": deleted})


@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):

    if id not in users:
        return jsonify({"error": "User not found"}), 404

    deleted = users.pop(id)

    return jsonify({"deleted": deleted})


if __name__ == "__main__":
    app.run(debug=True)