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
                bat """
                call ${VENV_DIR}\\Scripts\\activate
                python -m pip install --upgrade pip
                pip install -r requirements.txt
                """
            }
        }

        stage('Run App (Background)') {
            steps {
                bat """
                call ${VENV_DIR}\\Scripts\\activate
                start "" python app.py
                """
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished!'
        }
    }
}
