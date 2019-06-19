*** Settings ***
Library           OperatingSystem
Library           IPMILibrary
Library           WebTestlib 
Variables         config.py   

*** Test Cases ***
Cases1-IPMI-SEL
    IPMI    sel

Cases2-IPMI-SDR
    IPMI    sdr
IPMILibrary
    [Tags]  Execute
    ipmicmd    ${ipmi}    ${host}    ${interface}    ${user}    ${passwd}    sel

IPMILibrary-SDR 
    ipmicmd    ${ipmi}    ${host}    ${interface}    ${user}    ${passwd}    sdr

WebTest
    [Tags]  Execute
    WebLoginFWupdate   ${ip}

*** Keywords ***
IPMI
    [Arguments]    ${cmd}
    ${run}    Run and Return RC    ${ipmi} ${host} ${interface} ${user} ${passwd} ${cmd}
    ${result}    Run    ${ipmi} ${host} ${interface} ${user} ${passwd} ${cmd}
    ${status}    run keyword and return status    should be equal as integers    ${run}    0
    run keyword if    ${status}    Log    ${result}
    ...    ELSE    Fail
