Feature: test login functionality
@stage 
    Scenario Outline: login kyn webapp

        When launch chrome browser
        Then we visit kynlogin
        When Login using <Platform> platform with <UserName> and <Password>  
        Then clickloginButton
        Then clickpushnotification
        Then clickreport
        Then clicklocation
        Then clickcontent
        Then clicktelekast
        Then clicklive request
        Then click schedule request
        Then clickuser
        Then click resource
        Then click search
        Then select kynfluencer
        Then select Kynformer
         Then select Public

    
        Examples:
            | Platform | UserName           | Password |
            | kynapp| admin@theproindia.com | prorgIN$!| 