pipeline {
    agent any
     environment {
        SONAR_HOST_URL = 'http://sonarqube:9000'
        SELENIUM_HOST = 'http://selenium-grid:4444'
        //SONAR_TOKEN = credentials('sonarqube-token') 
    }
    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Check Selenium') {
            steps {
                sh 'curl -f ${SELENIUM_HOST}'
            }
        }
        
        // stage('SonarQube Analysis') {
        //     steps {
        //         withSonarQubeEnv('sonarServer') {
        //         script {
        //                 try {
        //                     // تمرير SONAR_TOKEN عبر البيئة لتجنب التحذير
        //                     withCredentials([string(credentialsId: 'jenkins-token', variable: 'SONAR_TOKEN')])  {
        //                         sh """
        //                             docker run --rm \
        //                             --network jenkins-grid-network \
        //                             -v "\$PWD":/app \
        //                             -w /app \
        //                             sonarsource/sonar-scanner-cli \
        //                             -Dsonar.sources=. \
        //                             -Dsonar.host.url=${SONAR_HOST_URL} \
        //                             -Dsonar.token=${SONAR_TOKEN} \
        //                             -Dsonar.sonar.projectKey=selenium-python

        //                         """
        //                     }
        //                 }
        //                  catch (Exception e) {
        //                     error("SonarQube analysis failed: ${e.getMessage()}")
        //                 }
                    
        //     }
        // }
        // }
        // }

   
       
        stage('Build') {
            steps {
                sh 'docker build -t my-python-app .'
                
            }
        }

        stage('Run') {
            steps {
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