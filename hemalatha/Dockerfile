# Use official Python image
FROM python:3.10-bookworm

# Set the working directory inside the container
WORKDIR /hema-docker

# Upgrade pip
RUN python3 -m pip install --upgrade pip

# Copy and install dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy the model file and app code
COPY classifier.pkl /hema-docker/
COPY . .

# Ensure the file exists and has content
RUN ls -lh /hema-docker/classifier.pkl
RUN file /hema-docker/classifier.pkl

# Start the Flask app
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
