pipeline {
    agent any
     environment {
        SONAR_HOST_URL = 'http://sonarqube:9000'
        SONAR_TOKEN = credentials('sonarqube-token') 
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
                script {
                        try {
                            // تمرير SONAR_TOKEN عبر البيئة لتجنب التحذير
                            withCredentials([string(credentialsId: 'sonarqube-token', variable: 'SONAR_TOKEN')])  {
                                sh """
                                    docker run --rm \
                                    --network jenkins-grid-network \
                                    -e SONAR_TOKEN=${SONAR_TOKEN} \
                                    -v "\$PWD":/app \
                                    -w /app \
                                    sonarsource/sonar-scanner-cli \
                                    -Dsonar.projectKey=my-project \
                                    -Dsonar.sources=. \
                                    -Dsonar.host.url=${SONAR_HOST_URL}
                                """
                            }
                        } catch (Exception e) {
                            error("SonarQube analysis failed: ${e.getMessage()}")
                        }
                    }
            }
        }
        }

        stage('Quality Gate') {
    steps {
        timeout(time: 1, unit: 'MINUTES') {
            waitForQualityGate abortPipeline: true
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