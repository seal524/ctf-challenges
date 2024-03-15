FROM ubuntu:latest

# Install netcat and python
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y build-essential socat
RUN apt-get install -y python3
RUN pip install inputimeout

#adding user
RUN adduser --disabled-password --gecos '' netcatuser
RUN chown -R root:netcatuser /home/netcatuser/
RUN chmod 750 /home/netcatuser

#copy files to WORKDIR
WORKDIR /home/netcatuser
COPY encrypted_letters.py /home/netcatuser
COPY flag.txt /home/netcatuser
COPY script.sh /home/netcatuser

#making the script executable
RUN chmod +x /home/netcatuser/script.sh


#Exposing port 8000 and making socat listen for incomming traffic on port 8000
EXPOSE 8000
CMD su -l netcatuser -c "socat -dd TCP4-LISTEN:8000,fork,reuseaddr EXEC:/home/netcatuser/script.sh"
