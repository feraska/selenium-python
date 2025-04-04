FROM jenkins/jenkins

# Switch to root user to install necessary packages
USER root

# Update package list and install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Switch back to the Jenkins user after installation
USER jenkins