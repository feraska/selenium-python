pipeline {
    agent any
     environment {
        SONAR_HOST_URL = 'http://sonarqube:9000'
        SONAR_TOKEN = credentials('sonarqube-token') 
    }
    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sonarServer') {
                    sh '''
                docker run --rm \
                    --network jenkins-grid-network \
                    -v "$PWD":/usr/src \
                    sonarsource/sonar-scanner-cli \
                    -Dsonar.projectKey=my-project \
                    -Dsonar.sources=. \
                    -Dsonar.host.url=$SONAR_HOST_URL \
                    -Dsonar.login=$SONAR_TOKEN
                '''
                }
            }
        }
       
        stage('Build and Run') {
            steps {
                sh 'docker build -t my-python-app .'
                sh 'docker run --rm --network jenkins-grid-network my-python-app'
            }
        }


        
   
       
       
    }

    post {
        
        always {
            echo 'Pipeline execution completed.'
        }
    }
}