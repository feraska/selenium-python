pipeline {
    agent any

    environment {
        SELENIUM_GRID_URL = "https://pfjlhx5t-4444.euw.devtunnels.ms/"  // Use the container name
        // SLACK_CHANNEL = 'general'  // Set your Slack channel here
        // SLACK_COLOR_SUCCESS = 'good'  // Color code for success messages (green)
        // SLACK_COLOR_FAILURE = 'danger'  // Color code for failure messages (red)
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
                
                venv/bin/python -m pytest --alluredir=allure-results -v
                 '''
            }
        }
         stage('Generate Allure Report') {
            steps {
                sh '''
                    mkdir -p allure-report
                    allure generate allure-results --clean -o allure-report
                '''
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure(
                includeProperties: false, 
                jdk: '',
                results: [[path: 'allure-report']]
                )
            }
        }

       
    }

    post {
        // success {
        //     script {
        //         slackSend(channel: SLACK_CHANNEL, color: SLACK_COLOR_SUCCESS, message: "Build Successful: ${env.JOB_NAME} #${env.BUILD_NUMBER} - ${env.BUILD_URL}")
        //     }
        // }

        // failure {
        //     script {
        //         slackSend(channel: SLACK_CHANNEL, color: SLACK_COLOR_FAILURE, message: "Build Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER} - ${env.BUILD_URL}")
        //     }
        // }

        // unstable {
        //     script {
        //         slackSend(channel: SLACK_CHANNEL, color: 'warning', message: "Build Unstable: ${env.JOB_NAME} #${env.BUILD_NUMBER} - ${env.BUILD_URL}")
        //     }
        // }
        always {
            echo 'Pipeline execution completed.'
        }
    }
}