pipeline {
    agent any
   
    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
       
        stage('Build and Run') {
            steps {
                sh 'docker build -t my-python-app .'
                sh 'docker run --rm my-python-app'
            }
        }

        
   
       
       
    }

    post {
        
        always {
            echo 'Pipeline execution completed.'
        }
    }
}