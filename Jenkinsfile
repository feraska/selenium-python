pipeline {
    agent any
    environment {
        SELENIUM_GRID_URL = "http://selenium-grid:4444"  // Use the container name
        SONARQUBE_ENV = credentials('sonarqube-token') // Jenkins credential ID if needed
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
                          -Dsonar.projectKey=my-project \
                          -Dsonar.sources=. \
                          -Dsonar.host.url=http://sonarqube:9000 \
                          -Dsonar.login=$SONARQUBE_ENV
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