pipeline {
    agent any

    environment {
        SELENIUM_GRID_URL = "https://pfjlhx5t-4444.euw.devtunnels.ms/ui/"  // Use the container name
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'master', url: 'https://github.com/feraska/selenium-python.git'
            }
        }
        // stage('Install Dependencies') {
        //     steps {
        //         sh 'pip3 install -r requirements.txt'
        //     }
        // }

        stage('Run Tests') {
            steps {
                sh 'pytest --alluredir=allure-results'
            }
        }

        stage('Generate Allure Report') {
            steps {
                sh 'allure generate allure-results --clean -o allure-report'
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed.'
        }
    }
}