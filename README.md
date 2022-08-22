# Task 1: Software configuration
### Subtask 1: Why did I choose to participate in the challenge portfolio?
 
* Hello, my name is Maria.      

*I took part in the course because I wanted to take a new direction. I have been studying on the faculty of computer science for 3 years, but QA is something new for me. I aim to get my long-awaited first job and a chance to build a career.*

:yellow_heart: :blue_heart:

# TASK 2: selectors
Login
*//*[@id="login"]
*//input[@name= 'login' ]
*//child::div/label

Password
*//*[@id="password"]
*//input[@type= 'password' ]
*//input[@id ='password' ]

Remind password
*//*[@id="__next"]/form/div/div[1]/a
*//*[text()="Remind password"]
*//child::div/a

English
*//*[@id="__next"]/form/div/div[2]/div/div
*//li[@aria-disabled= 'false' and @data-value]
*//input[@value ='en' ]

Polski
*//*[@id="__next"]/form/div/div[2]/div/div
*//*[text()="Polski"]
*//div[@aria-haspopup= 'listbox']

Sign In
*//*[@id="__next"]/form/div/div[2]/button/span[1]
*//*[text()="Sign in"]
*//button[@type= 'submit']

