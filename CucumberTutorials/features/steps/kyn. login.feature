@login
    Scenario Outline: Create Ground task and verify whether created ground task is listed in task list page

        When launch chrome browser
        Then we visit facebooklogin
        When Login using <Platform> platform with <UserName> and <Password>
        Then create task 
        Then logout
        Examples:
            | Platform | UserName                             | Password     |
            | facebook | ajithsaravanamoorthy@theproindia.com | March@199628 