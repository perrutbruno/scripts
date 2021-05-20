#!/bin/bash
apt-gey install -y jq

TOKEN=$(curl -s --user 'yourDOCKERHUBuser:yourDOCKERHUBpassword' "https://auth.docker.io/token?service=registry.docker.io&scope=repository:ratelimitpreview/test:pull" | jq -r .token)

#Pra esse script funcionar precisaremos do pacote jq instalado, que lê o json <3

curl -s --head -H "Authorization: Bearer $TOKEN" https://registry-1.docker.io/v2/ratelimitpreview/test/manifests/latest > /tmp/output_script2

awk '{for (I=1;I<=NF;I++) if ($I == "RateLimit-Remaining:") {print $(I+1)};}' /tmp/output_script2 > /tmp/output_script_cut2

cat /tmp/output_script_cut2 | cut -c1-3
