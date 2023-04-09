*** Settings ***
Documentation     Test cases for sim_static.py
Library           OperatingSystem
Library           Process
Library           String
Library           Collections
Library           DateTime
Resource          ../lib/sysid/simulate_static.py
Resource          ../lib/sysid/sysid.py

*** Variables ***
${SIM_STATIC_PATH}    ${CURDIR}${/}..${/}lib${/}sysid${/}simulate_static.py
${SYSID_PATH}    ${CURDIR}${/}..${/}lib${/}sysid${/}sysid.py

*** Test Cases ***
Test sim_static
    [Documentation]    Test sim_static.py
    [Tags]    sim_static
    ${output}    Run Process    python    ${SIM_STATIC_PATH}    shell=${True}
    Log    ${output.stdout}
    ${y}    Convert To List    ${output.stdout}
    Log    ${y}
    ${y_shape}    Get Length    ${y}
    Log    ${y_shape}
    Should Be Equal    ${y_shape}    1000
    ${y_size}    Get Length    ${y}
    Log    ${y_size}
    Should Be Equal    ${y_size}    1000
    ${y_ndim}    Get Length    ${y}
    Log    ${y_ndim}
    Should Be Equal    ${y_ndim}    1000

Test sysid
    [Documentation]    Test sysid.py
    [Tags]    sysid
    ${output}    Run Process    python    ${SYSID_PATH}    shell=${True}
    Log    ${output.stdout}
    ${y}    Convert To List    ${output.stdout}
    Log    ${y}
    ${y_shape}    Get Length    ${y}
    Log    ${y_shape}
    Should Be Equal    ${y_shape}    1000
    ${y_size}    Get Length    ${y}
    Log    ${y_size}
    Should Be Equal    ${y_size}    1000
    ${y_ndim}    Get Length    ${y}
    Log    ${y_ndim}
    Should Be Equal    ${y_ndim}    1000