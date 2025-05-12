pipeline {
    agent {
        docker {
            image 'python:3.9'  // Use the Python 3.9 Docker image for the whole pipeline
            label 'my-agent'
            args '-u root'
        }
    }

    environment {
        SELENIUM_GRID_URL = "http://selenium-grid:4444"  // Use the container name
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sonarServer') {
                    script {
                        sh '''
                            sonar-scanner \
                                -Dsonar.projectKey=my-project \
                                -Dsonar.sources=. \
                                -Dsonar.host.url=http://sonarqube:9000
                        '''
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    venv/bin/python -m pytest --cov=. --cov-report=html --cov-report=term-missing --alluredir=allure-results -v
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