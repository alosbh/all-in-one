FROM docker.corp.jabil.org/devservices/rpi3-xwindow
# install base dependencies 
RUN apt-get update && apt-get install -y python3-dev \
	python3-requests \
	python3-pip \
	python3-pyqt5 \
	python3-RPi.GPIO \
	#python3-setuptools \
	python3-pyqt5.qtwebkit \
	#python3.pyqt5.qtsvg \
	gcc \ 
	#poppler-utils \
	&& rm -rf /var/lib/apt/lists/* \
	&& python3 -m pip install --upgrade pip \
    #&& python3 -m pip install wheel \
	#&& python3 -m pip install urllib3 \
	&& python3 -m pip install pyyaml

# install spi lib
COPY spi /home/app/spi
WORKDIR /home/app/spi
RUN python3 /home/app/spi/setup.py install

# copy script files
COPY script/. /aio/
RUN chmod +x /aio/main.py

COPY startup.sh /aio
WORKDIR /aio
RUN chmod +x /aio/startup.sh
ENV START_UP="/aio/startup.sh"