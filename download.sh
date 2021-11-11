#!/bin/bash

if [ -z "$dep_username" ]
then
    echo "Start the script with an username defined"
    exit 1
fi
if [ -z "$dep_password" ]
then
    echo "Start the script with a password defined"
    exit 1
fi

# Login and get access_token
curl -s -i -X POST -F "grant_type=password" -F "userName=$dep_username" -F "password=$dep_password" -H "User-Agent: Mozilla/5.0" -H "Accept: application/json" https://api.givtapp.net/oauth2/token -o out.json

request_context=$(cat out.json|grep Request-Context|awk '{print $2}')
access_token=$(cat out.json|sed 's/{/\n/g;s/,/\n/g'|grep access_token|sed 's/:/ /g; s/"/ /g'|awk '{print $2}')
echo $request_context
echo $access_token

# Get GUID of the organisation
curl -s -i -X GET -H "Content-Type: application/json" -H "authorization: Bearer $access_token" https://api.givtapp.net/api/CollectGroupView/CollectGroup -o collectgroup.json

guid=$(cat collectgroup.json|sed 's/{/\n/g;s/,/\n/g'|grep GUID|sed 's/:/ /g; s/"/ /g'|awk '{print $2}')
echo $guid
orgId=$(cat collectgroup.json|sed 's/{/\n/g;s/,/\n/g'|grep OrgId|sed 's/:/ /g; s/"/ /g'|awk '{print $2}')
echo $orgId

#CollectGroupId: 01b6e7ef-2bbe-4bf1-a85f-a4e95856bf48
curl -s -X GET -H "Content-Type: application/json" -H "authorization: Bearer $access_token" -H "CollectGroupId: $guid" https://api.givtapp.net/api/v2/organisations/$orgId/collectgroups/$guid/payments/export?startDate=2021-11-04T14:32:47.238Z\&endDate=2021-11-11T14:32:47.238Z -o sample.csv
cat sample.csv