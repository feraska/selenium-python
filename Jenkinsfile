pipeline {
    agent any

    environment {
        SELENIUM_GRID_URL = "http://172.17.0.3:4444"  // Use the container name
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
                    . venv/bin/activate
                    pip3 install -r requirements.txt
                    '''
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest '
            }
        }

       
    }

    post {
        always {
            echo 'Pipeline execution completed.'
        }
    }
}