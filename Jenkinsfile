pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "chatwithpdf"
        REGISTRY_CREDENTIALS = credentials('docker-hub-credentials')
        REGISTRY = "your-docker-hub-username/chatwithpdf"
    }

    stages {
        stage('Clone repository') {
            steps {
                git 'https://github.com/OsadaInduwara/chatwithpdf.git'
            }
        }

        stage('Build Docker image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:${BUILD_NUMBER}")
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    docker.image("${DOCKER_IMAGE}:${BUILD_NUMBER}").inside {
                        sh 'pytest'
                    }
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('', REGISTRY_CREDENTIALS) {
                        docker.image("${DOCKER_IMAGE}:${BUILD_NUMBER}").push('latest')
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                // Add deployment steps here, e.g., deploy to AWS, Kubernetes, etc.
            }
        }
    }
}
