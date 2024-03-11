import time
import redis
from flask import Flask

app = Flask(__name__)
# 此处host是docker-compose.yaml配置文件中 redis的服务的名称
cache = redis.Redis(host='127.0.0.1', port=6379)


def get_hit_count():
    """利用redis统计访问次数"""
    retries = 5
    # 由于当redis重启时,可能会有短暂的无法访问redis
    # 循环的在作用默认重试5次
    while True:
        try:
            # redis的incr方法, 如果hits值存在自动+1, 否则新增该键,值为1
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as e:
            if retries == 0:
                raise e
            retries -= 1
            time.sleep(0.5)


@ app.route('/')
def main():
    count = get_hit_count()
    return "欢迎访问! 网站已累计访问{}次\n".format(count)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
