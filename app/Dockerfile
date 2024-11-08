FROM python:3.11

WORKDIR /app

# install app dependencies
# COPY requirements.txt ./
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

# copy in source code
EXPOSE 3306

#setup app user so container doesn't run as root user thanks docker docs
RUN useradd app
USER app

# CMD [ "python", "./weather-api.py"] temporary entrypoint

ENTRYPOINT ["tail", "-f", "/dev/null"]