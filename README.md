# Deploy FastAPI with Using Cloud Run
Deploy FastAPI Machine Learning model Team SapiGo with using Cloud Run

## Requirement Packages / Tools :
•	Pyenv (optional)
•	Virtualenv (optional)
•	Python 3 or up
•	Tensorflow
•	Python-multipart
•	Pillow
•	Fastapi
•	Numpy
•	Uvicorn
•	starlette
•	Google Cloud Platform Account
•	Google Cloud Platform - API Cloud Build
•	Cloud run
•	Container Images

## Local Run
```
$ python -m venv [nama-folder]
$ cd [nama-folder]
$ cd Scripts
$ activate
$ cd ..
$ git clone https://github.com/SapiGo-Team/Sapigo-CC-Model-ML-Deployment.git
$ pip install -r requirements.txt
$ uvicorn main:app --reload
```

## Deploy to Cloud Run using Cloud SDK
```
$ gcloud init
$ gcloud services enable run.googleapis.com
$ gcloud builds submit --tag gcr.io/[project-id-kalian]/sapigo-registry
$ gcloud run deploy --image gcr.io/[project-id-kalian]/Sapigo-api --platform managed --region asia-southeast2 --allow-unauthenticated sapigo-model
```

## Deploy to Cloud Run using Google Cloud Platform

1. Make sure you have an active Google Cloud Platform (GCP) account. If you don't have one yet, sign up and create a new project at https://console.cloud.google.com.

2. Ensure that you have installed the Google Cloud SDK (https://cloud.google.com/sdk) and initialized it by running the following command in the terminal or command prompt:
   ```
   gcloud init
   ```
3. Create a repository in a code management service such as GitHub or GitLab, and make sure the repository contains all the necessary files for your FastAPI application, including Dockerfile, requirements.txt, and your FastAPI application code.

4. Open the terminal or command prompt and navigate to the directory where you want to clone the FastAPI repository.

5. Clone the FastAPI repository by running the following command:
   ```
   git clone https://github.com/SapiGo-Team/Sapigo-CC-Model-ML-Deployment.git
   ```
6. After the cloning process is complete, navigate the terminal or command prompt to the newly cloned FastAPI directory.

7. Build the local Docker container by executing the following command:
   ```
   docker build -t gcr.io/[PROJECT_ID]/sapigo-registry
   ```
   Replace [PROJECT_ID] with your Google Cloud Platform project ID that you specified earlier.

8. After the build process is complete, verify that the local Docker container is running by executing the following command:
   ```
   docker run -p 8000:8000 gcr.io/[PROJECT_ID]/sapigo-registry
   ```
   Make sure there are no errors, and the FastAPI application is running successfully on localhost.

9. If the previous steps are successful, stop and delete the running Docker container by pressing Ctrl+C in the terminal or command prompt.

10. To publish the Docker container to the Google Cloud Container Registry, execute the following command:
    ```
    docker push gcr.io/[PROJECT_ID]/sapigo-registry
    ```
    The container will be uploaded to the Container Registry in the corresponding Google Cloud Platform project.

11. Next, create a Cloud Run service by running the following command in asia-southeast2 (Jakarta) region:
    ```
    gcloud run deploy --image gcr.io/[PROJECT_ID]/sapigo-registry --platform managed --region asia-southeast2 --allow-unauthenticated backendsapigo
    ```

12. GCP will prompt you to choose a region for deploying the Cloud Run service. Select the region that suits your needs.

13. After the deployment process is complete, GCP will provide a URL that can be used to access the deployed FastAPI application. Copy that URL from the output and try accessing it in a web browser or using an API testing software like Postman.

## SapiGO FastAPI Models Demo
To try the above model demo, you can open the provided link : https://backendsapigo-u7zm6m6lkq-et.a.run.app
