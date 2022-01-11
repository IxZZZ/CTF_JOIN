FROM ubuntu:20.04 

RUN useradd -m secure_cloud
WORKDIR /home/secure_cloud

RUN apt update
RUN apt install -y xinetd
RUN apt install -y netcat

COPY main /home/secure_cloud/secure_cloud
COPY ./ads /home/secure_cloud/ads
COPY secure_cloud.xinetd /etc/xinetd.d/secure_cloud
COPY flag.txt /home/secure_cloud

RUN mkdir /home/secure_cloud/SANDBOX

RUN chown -R root:root /home/secure_cloud/SANDBOX
RUN chown -R root:root /home/secure_cloud/ads
RUN chown root:root /home/secure_cloud/secure_cloud
RUN chmod +x /home/secure_cloud/secure_cloud

RUN chmod 660 /etc/xinetd.d/secure_cloud

RUN service xinetd start

CMD ["/usr/sbin/xinetd", "-dontfork"]