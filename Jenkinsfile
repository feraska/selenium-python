pipeline {
    agent any

    environment {
        SELENIUM_GRID_URL = "http://selenium-grid:4444"  // Use the container name
        
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
                     venv/bin/pip install -r requirements.txt
                    '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                
                venv/bin/python -m pytest --cov=. --cov-report=html --cov-report=term-missing --alluredir=allure-results -v
                 '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh '''
                        sonar-scanner \
                        -Dsonar.projectKey=selenium-python \
                        -Dsonar.sources=. \
                        -Dsonar.sourceEncoding=UTF-8 > sonar-scanner.log 2>&1
                        cat sonar-scanner.log
                    '''
                }
            }
        }
        stage('Quality Gate') {
            steps {
                waitForQualityGate abortPipeline: true
    }
}
       
       
    }

    post {
        
        always {
            echo 'Pipeline execution completed.'
        }
    }
}