pipeline {
    agent any
   
    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh 'sonar-scanner \
                        -Dsonar.projectKey=my-project \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=http://sonarqube:9000 \
                      '  
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