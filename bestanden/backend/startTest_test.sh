
# Jenkins heeft op dit moment de omgeving al gebuild. Naam docker image: groep7team/project
#verwijderen van vorige build, indien deze bestaat
docker rm -f backend_test

#uitvoeren van nieuwe build en code testing op uit voeren, volgorde is belangrijk py.test laat de build stoppen als hier een test niet van slaagt
    #pylint -f parseable -d I0011,R0801 untitled | tee pylint.out  --> Gaat over de code in de map untitled en kijkt of de conventie's van PEP8 zijn toegepast
    #py.test test.py --cov=. --cov-report xml:cov.xml --> kijkt welke code is getest geweest
    #py.test --junitxml results.xml test.py --> voert de eigenlijke unittests uit.

docker run --name backend_test groep7team/backend_test /bin/bash -c  "python manage.py jenkins --enable-coverage --settings=fipsim.settings.testing"

#Test het laatste commando. Dit zijn de unittests, deze moeten slagen of de pipeline wordt onderbroken.
exitcode=$?

#Kopiëren van de code naar testcode --> dit is nodig voor feedback in jenkins te krijgen met pylint.
docker cp backend_test:/code/. /var/jenkins_home/workspace/Test_Backend_Test/

#kopieren van results.xml (bevindt zich in de container) naar de workspace van de pipeline --> dit is nodig voor testresults weer te geven in jenkins.
docker cp backend_test:/code/production_env/reports/junit.xml /var/jenkins_home/workspace/backend_test/

#terug geven van de uitvoerstatus script, indien geslaagd gaat build verder, anders niet.
return $exitcode