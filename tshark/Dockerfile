FROM python:3

RUN apt-get -y update
RUN echo "tshark-common tshark-common/install-setuid boolean true" | debconf-set-selections
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install tshark