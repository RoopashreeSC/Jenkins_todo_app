pipeline {
    agent any
    environment {
        VENV_DIR = "venv"
        PYTHON = "python"
        APP_PORT = "5000"
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/RoopashreeSC/Jenkins_todo_app.git'
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                script {
                    if (!fileExists("${VENV_DIR}")) {
                        bat "${PYTHON} -m venv ${VENV_DIR}"
                    }
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                bat """call ${VENV_DIR}\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt"""
            }
        }

        stage('Run App') {
            steps {
                bat """start cmd /c call ${VENV_DIR}\\Scripts\\activate && python app.py"""
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished!'
        }
    }
}