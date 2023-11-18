# How to run given tasks

## File formate:
    Task-OF-IT-GROW-DIVISION-LTD
        - 1st task
            - Task-1.py
            - Task-2.py
            - Task-3.py
            - Task-4.pdf
        - 2nd task
            - Book Service
                - app
                    - models
                    - routers
                    - utils
            - main.py
            - docker-compose.yml

## For 1st Task:
    Create a virual inviroment
        - python3 -m venv venv
        
    Acitve the virual inviroment
        - .\venv\Scripts\activate (for windwos)
        - source venv/bin/activate (for linux or mac)
        
    Install dependenceis
        - pip install -r requirements.txt
        
    Run all Task file
        - python Task-1.py
        - python Task-2.py
        - python Task-3.py

## For 2nd Task:
    install Docker on your System

    Run docker the file
    [./Book Service]
    └─$ docker-compose up --build 

