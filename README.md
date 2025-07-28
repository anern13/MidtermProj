# MidtermProj

docker build -t leads:latest . 
docker run -p 5000:5000 leads

# Midterm Project – DevOps Deployment

Welcome to the **Midterm DevOps Project** repository for DeployNova!  
This project showcases a Python-based application containerized with Docker and deployed on AWS using Elastic Beanstalk and ECR.

---

## 🧩 Project Overview

- **Topic**: Contact Manager
- **Language**: Python
- **Architecture**: Modular (`main.py` + `functions.py`)
- **Interface**: Flask-based web UI
- **Storage**: In-memory using Python dictionaries/lists
- **Features**:
  - Add / Edit / Delete / Display entries
  - Sort and calculate based on stored data
  - Web interface through Flask

---

## 📁 Project Structure

.
├── app/
│ ├── main.py
│ ├── functions.py
│ └── templates/
│ └── index.html
├── Dockerfile
├── requirements.txt
└── Dockerrun.aws.json (used for deployment)

yaml
Copy
Edit

---

## 🐳 Docker Configuration

### Dockerfile

Ubuntu-based image that installs Flask, sets the working directory, and runs the app on port 8080.

```Dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["python", "app/main.py"]
Flask Run Command
Your Flask app must start like this to work in Elastic Beanstalk:

python
Copy
Edit
app.run(host="0.0.0.0", port=8080)
🚀 AWS Deployment (Manual via Console)
1. AWS ECR
Created a private repository in Elastic Container Registry: midterm-proj

Built and pushed the Docker image:

bash
Copy
Edit
docker build -t midterm-proj .
docker tag midterm-proj:latest 495307862605.dkr.ecr.us-east-1.amazonaws.com/midterm-proj:latest
docker push 495307862605.dkr.ecr.us-east-1.amazonaws.com/midterm-proj:latest
2. Elastic Beanstalk (EB)
Chose deployment via AWS Console

Platform: Docker running on 64bit Amazon Linux 2

Configuration Preset: Single instance (free tier eligible)

Deployed using a Dockerrun.aws.json file zipped alone in a .zip

📄 Dockerrun.aws.json
json
Copy
Edit
{
  "AWSEBDockerrunVersion": 1,
  "Image": {
    "Name": "495307862605.dkr.ecr.us-east-1.amazonaws.com/midterm-proj:latest",
    "Update": "true"
  },
  "Ports": [
    {
      "ContainerPort": 8080
    }
  ]
}
Uploaded via Upload and Deploy

Resulting public URL:

cpp
Copy
Edit
http://<your-environment>.elasticbeanstalk.com
