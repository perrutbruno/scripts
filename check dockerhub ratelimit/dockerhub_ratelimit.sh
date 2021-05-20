#!/bin/bash

apt-get install -y jq

TOKEN=$(curl -s --user 'yourDOCKERHUBuser:yourDOCKERHUBpassword' "https://auth.docker.io/token?service=registry.docker.io&scope=repository:ratelimitpreview/test:pull" | jq -r .token)

#Pra esse script funcionar precisamos do pacote jq instalado, pois ele lê o json <3
curl -s --head -H "Authorization: Bearer $TOKEN" https://registry-1.docker.io/v2/ratelimitpreview/test/manifests/latest > /tmp/output_script

awk '{for (I=1;I<=NF;I++) if ($I == "RateLimit-Limit:") {print $(I+1)};}' /tmp/output_script > /tmp/output_script_cut

cat /tmp/output_script_cut | cut -c1-3
