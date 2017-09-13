FROM ubuntu

RUN apt-get update && apt-get -y install python-pip

RUN pip install toi

CMD toi --help
