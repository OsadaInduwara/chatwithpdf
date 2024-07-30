pipeline {
    agent any

    stages {
        stage('SCM Checkout') {
            steps {
                checkout scm: [
                    $class: 'GitSCM',
                    branches: [[name: '*/master']],
                    userRemoteConfigs: [[url: 'https://github.com/OsadaInduwara/chatwithpdf.git', credentialsId: 'docker-hub-credentials']]
                ]
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t chatwithpdf:${BUILD_NUMBER} .'
            }
        }
        stage('Login to Docker Hub') {
            steps {
                withCredentials([string(credentialsId: 'docker-hub-credentials', variable: 'DOCKER_PASSWORD')]) {
                    script {
                        sh "echo ${DOCKER_PASSWORD} | docker login -u osadainduwara --password-stdin"
                    }
                }
            }
        }
        stage('Push Image') {
            steps {
                sh 'osadainduwara/chatwithpdf:${BUILD_NUMBER}'
            }
        }
    }
    post {
        always {
            sh 'docker logout'
        }
    }
}
