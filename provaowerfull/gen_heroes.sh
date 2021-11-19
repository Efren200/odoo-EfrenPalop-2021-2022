#!/bin/bash

echo "<odoo><data>"
while read line 
do
    nom=$(echo $line | cut -d ',' -f1)
    id=$((id+1))
    stars=$(echo $line | cut -d ',' -f2)
    type=$(echo $line | cut -d ',' -f3)
    attack=$(echo $line | cut -d ',' -f4)
    defense=$(echo $line | cut -d ',' -f5)
    health=$(echo $line | cut -d ',' -f6)
    echo "<record id='hero$id' model='provaowerfull.hero'>"
    echo "<field name='name'>$nom</field>"
    echo "<field name='stars'>$stars</field>"
    echo "<field name='type'>$type</field>"
    echo "<field name='attack'>$attack</field>"
    echo "<field name='defense'>$defense</field>"
    echo "<field name='health'>$health</field>"
    if [[ $type = "Plant" ]];
    then
        echo "<field name='hero_icon'>$(base64 images/hoja.jpg)</field>"
    elif [[ $type = "Water" ]];
    then    
        echo "<field name='hero_icon'>$(base64 images/water.jpg)</field>"
    else
        echo "<field name='hero_icon'>$(base64 images/fuego.jpg)</field>"
    fi

    echo "</record>"
done
echo "</data></odoo>"