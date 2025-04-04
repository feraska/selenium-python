pipeline {
    agent any

    environment {
        SELENIUM_GRID_URL = "https://pfjlhx5t-4444.euw.devtunnels.ms/"  // Use the container name
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'master', url: 'https://github.com/feraska/selenium-python.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                     venv/bin/pip3 install -r requirements.txt
                    '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                
                venv/bin/python -m pytest -v
                 '''
            }
        }

       
    }

    post {
        always {
            echo 'Pipeline execution completed.'
        }
    }
}