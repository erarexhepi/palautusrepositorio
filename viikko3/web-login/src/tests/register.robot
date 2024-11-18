*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username    validuser
    Set Password    ValidPass123
    Confirm Password    ValidPass123
    Submit Registration
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username    le
    Set Password    ValidPass123
    Confirm Password    ValidPass123
    Submit Registration
    Registration Should Fail With Message    Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username    validuser
    Set Password    short
    Confirm Password    short
    Submit Registration
    Registration Should Fail With Message    Password must be at least 8 characters long

Register With Valid Username And Invalid Password
    Set Username    validuser
    Set Password    onlyletters
    Confirm Password    onlyletters
    Submit Registration
    Registration Should Fail With Message    Password must include at least one number or special character

Register With Nonmatching Password And Password Confirmation
    Set Username    validuser
    Set Password    ValidPass123
    Confirm Password    DifferentPass123
    Submit Registration
    Registration Should Fail With Message    Passwords do not match

Register With Username That Is Already In Use
    Set Username    validuser
    Set Password    ValidPass123
    Confirm Password    ValidPass123
    Submit Registration
    Registration Should Succeed
    Logout
    Reset Application Create User And Go To Register Page
    Set Username    validuser
    Set Password    AnotherValidPass123
    Confirm Password    AnotherValidPass123
    Submit Registration
    Registration Should Fail With Message    Username is already taken

Login After Successful Registration
    Set Username    successfuluser
    Set Password    ValidPass123
    Confirm Password    ValidPass123
    Submit Registration
    Registration Should Succeed
    Logout
    Go To Login Page
    Set Username    successfuluser
    Set Password    ValidPass123
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username    invaliduser
    Set Password    short
    Confirm Password    short
    Submit Registration
    Registration Should Fail With Message    Password must be at least 8 characters long
    Go To Login Page
    Set Username    invaliduser
    Set Password    short
    Submit Credentials
    Login Should Fail With Message    Invalid username or password

*** Keywords ***
Set Username
    [Arguments]    ${username}
    Input Text    username    ${username}

Set Password
    [Arguments]    ${password}
    Input Text    password    ${password}

Confirm Password
    [Arguments]    ${password_confirmation}
    Input Text    password_confirmation    ${password_confirmation}

Submit Registration
    Click Button    Register

Registration Should Succeed
    Main Page Should Be Open

Registration Should Fail With Message
    [Arguments]    ${message}
    Register Page Should Be Open
    Page Should Contain    ${message}

Logout
    Wait Until Element Is Visible    link=Logout    5s
    Click Link    Logout
    Login Page Should Be Open

Go To Login Page
    Go To    ${LOGIN_URL}

Submit Credentials
    Click Button    Login

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]    ${message}
    Login Page Should Be Open
    Page Should Contain    ${message}
