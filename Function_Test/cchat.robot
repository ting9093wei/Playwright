*** Settings ***
Resource    ../resource/ppt.resource
Resource    ../resource/__init_resource.robot

*** Variables ***
${RESULT_ROOT_PATH}    ${EXECDIR}${/}result${/}${VERSION}
${case_name}    ${SUITE NAME.rsplit('#')[-1]}
${result_path}    ${RESULT_ROOT_PATH}${/}${case_name}

*** Test Cases ***
Open PTT C_chat by Chrome
    New Browser    chromium    headless=${False}
    New Page    https://www.ptt.cc/bbs/c_chat/index.html
    Maximize Browser Window
    Click With Options    selector=body > div.bbs-screen.bbs-content.center.clear > form > div:nth-child(2) > button
    Take Screenshot    ${result_path}${/}ptt_c_chat.png
    Sleep    2
    [Teardown]    Test Teardown

*** Keywords ***
Maximize Browser Window
    [Documentation]    This keyword is used to maximize the browser window.
    Set Viewport Size    1920    1080
Test Teardown
    [Documentation]    This keyword is used to close the browser after the test case execution.
    Close Browser