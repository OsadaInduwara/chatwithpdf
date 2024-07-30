pipeline {
    agent any

    stages {
        stage('SCM Checkout') {
            steps {
                retry(3) {
                    git branch: 'master', url: 'https://github.com/OsadaInduwara/chatwithpdf.git', credentialsId: 'docker-hub-credentials'
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t osadainduwara/chatwithpdf:%BUILD_NUMBER% .'
            }
        }
        stage('Login to Docker Hub') {
            steps {
                withCredentials([string(credentialsId: 'osadaid', variable: 'dockerpassword')]) {
                    bat "docker login -u osadainduwara -p %dockerpassword%"
                }
            }
        }
        stage('Push Image') {
            steps {
                bat 'docker push osadainduwara/chatwithpdf:%BUILD_NUMBER%'
            }
        }
    }
    post {
        always {
            bat 'docker logout'
        }
    }
}
