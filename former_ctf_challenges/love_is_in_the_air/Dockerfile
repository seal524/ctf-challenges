FROM ubuntu:latest

# Install netcat
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y build-essential socat

#adding user
RUN adduser --disabled-password --gecos '' netcatuser
RUN chown -R root:netcatuser /home/netcatuser/
RUN chmod 750 /home/netcatuser

#copy files to WORKDIR
WORKDIR /home/netcatuser
COPY love_is_in_the_air.c /home/netcatuser/
COPY song.txt /home/netcatuser/

#making the script executable
#Dersom filen må kompileres, fjærn kommentering fra linjen under og fyll inn.

RUN gcc -o /home/netcatuser/love love_is_in_the_air.c
RUN chmod +x /home/netcatuser/love


#Exposing port 8000 and making socat listen for incomming traffic on port 8000
EXPOSE 8000
CMD su -l netcatuser -c "socat -dd TCP4-LISTEN:8000,fork,reuseaddr EXEC:/home/netcatuser/love"