FROM x11vnc/desktop

RUN apt-get -y update && apt-get -y update

EXPOSE 6080
EXPOSE 5900
