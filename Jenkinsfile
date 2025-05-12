pipeline {
    agent any
     environment {
        SONAR_HOST_URL = 'http://sonarqube:9000'
        SONAR_LOGIN = 'your-sonar-token' // أو استخدم credentials إذا تفضل
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
                    --network --network jenkins-grid \
                    -v "$PWD":/usr/src \
                    sonarsource/sonar-scanner-cli \
                    -Dsonar.projectKey=my-project \
                    -Dsonar.sources=. \
                    -Dsonar.host.url=$SONAR_HOST_URL \
                    
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