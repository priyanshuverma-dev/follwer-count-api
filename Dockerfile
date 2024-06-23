FROM ubuntu

RUN sudo apt update -y && apt upgrade -y 
COPY . /source

RUN cd ./source && pip install -r requirements.txt
RUN fastapi run main.py --port 8080
EXPOSE 8080
CMD [ "bash" ]
