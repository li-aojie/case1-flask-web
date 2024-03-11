# flask web app v1.0
# 搭建一个基于flask的web项目,实现了简单的访问统计
# 第一步: 获取一个镜像: python3.6
FROM python:alpine3.6
# 第二部: 拷贝项目代码到镜像中 ADD(自动尝试解压缩，不建议)/COPY
COPY ./flask-web-code /code
# 第三部: 安装项目的依赖环境: 第三方模块 flaks reids
# 切换工作目录用WORKDIR，类似于cd命令
WORKDIR /code
RUN pip install -r requirements.txt
# 第四部: 配置项目的启动 CMD参数 python app.py
CMD ["python", "app.py"]
