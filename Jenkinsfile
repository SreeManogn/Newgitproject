pipeline {
    agent any 
    stages {
        stage('Build Docker Image') {
            steps {
                echo "Building Docker Image for votingapp"
                bat "docker build -t votingapp:v1 ."
            }
        }
        stage('Docker Login') {
            steps {
                // Consider using Jenkins credentials for security
                bat 'docker login -u Sree_Manogna -p password'
            }
        }
        stage('Push Docker Image to Docker Hub') {
            steps {
                echo "Pushing Docker Image to Docker Hub"
                bat "docker tag votingapp:v1 22251a1257it258/assignment:v1"
                bat "docker push 22251a1257it258/assignment:v1"
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                echo "Deploying votingapp to Kubernetes"
                bat 'kubectl apply -f deployment.yaml --validate=false'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }
    post {
        success {
            echo 'Build, Docker push, and Kubernetes deployment successful! Artifact is ready!'
        }
        failure {
            echo 'Build or deployment failed.'
        }
    }
}
