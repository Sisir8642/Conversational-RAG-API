import redis
#here we have used redis, and the data saved in the ram for the period of program execution
r = redis.Redis(host="localhost", port=6379, decode_responses=True)

def save_message(user_id, message):
    r.rpush(user_id, message)

def get_history(user_id):
    return r.lrange(user_id, 0, -1)
