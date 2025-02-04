# Jenkins Git Calculator Tester

Tento projekt obsahuje **Jenkins pipeline**, která automaticky testuje kalkulačku v Git repozitáři a zapisuje výsledek.

## 🛠️ Funkce
- Automaticky se spustí při každém pushi do repozitáře.
- Stáhne aktuální verzi repozitáře.
- Provede test kalkulačky (unit testy pomocí Pytest nebo jiného testovacího frameworku).
- Zaznamená výsledek testů do konzole Jenkins.
- Zapíše výsledek testů zpět do Git repozitáře.

## 📦 Struktura projektu
```
/your-repository/
│-- src/
│-- tests/
│-- Jenkinsfile  ✅ (definuje pipeline)
│-- README.md  ✅ (tento soubor)
```

## 🚀 Požadavky
- **Jenkins server** s podporou **pipeline**.
- **Přístup k Git repozitáři** (HTTPS nebo SSH přístup, uložené přihlašovací údaje v Jenkins).
- **Unit testy pro kalkulačku** (například v Pythonu s Pytestem nebo v jiném jazyce).

## 📝 Jenkinsfile (Příklad)
```groovy
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/your-org/your-repo.git', credentialsId: 'git-credentials'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest tests/'
            }
        }

        stage('Commit Results') {
            steps {
                sh '''
                git config --global user.email "jenkins@example.com"
                git config --global user.name "Jenkins"
                echo "Testy proběhly úspěšně" > test-results.txt
                git add test-results.txt
                git commit -m "Přidán výsledek testů"
                git push origin main
                '''
            }
        }
    }
}
```

## 📜 Testovací skript (Příklad v Pythonu)
```python
# tests/test_calculator.py
import pytest
from src.calculator import add

def test_add():
    assert add(2, 3) == 5

if __name__ == "__main__":
    pytest.main()
```

## 🏗️ Jak nastavit Jenkins Pipeline
1. **Otevřete Jenkins** a vytvořte **nový pipeline job**.
2. V **Source Code Management** vyberte **Git** a nastavte URL repozitáře.
3. V sekci **Pipeline** vyberte **Pipeline script from SCM** a jako **Branch** nastavte např. `main`.
4. Uložte a spusťte pipeline!

## ✅ Výstup z Jenkins
```
Started by user admin
[Pipeline] stage (Checkout)
[Pipeline] git
Fetching changes from the remote Git repository
[Pipeline] stage (Run Tests)
[Pipeline] sh
============================= test session starts =============================
collected 1 item

tests/test_calculator.py .                                             [100%]

============================== 1 passed in 0.01s ==============================
[Pipeline] stage (Commit Results)
Přidán výsledek testů
[Pipeline] End of Pipeline
```
