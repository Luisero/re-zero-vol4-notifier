FROM python:3

WORKDIR /app

COPY . .

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

RUN apt-get update -y
RUN apt-get install -y libglib2.0-0 libnss3 libgconf-2-4 libfontconfig1 
RUN apt-get install -y google-chrome-stable
ENV ENV DISPLAY=:99
RUN pip install -r requirements.txt

RUN ls -a
CMD ["python3","main.py"]