07/22/2018

Working on how select method works.

07/10/2018

Created a class to retreive special keys, added a semi colon special key to test it.

Have to follow my project board and stop writing what comes from my mind...

07/08/2018

Now the webdriver server subprocess has his own class and it does not depend on the web driver anymore.

07/07/2018

Added a capabilities dictionary. It will be used to add capabilities to the browser.

Now you can use any port if it is possible, by default it will keep using port 9000.

07/04/2018

I had to change my Python version in my computer (upgraded to 3.7) because my old python changes the way I do imports.

Added a simple send keys method.

07/03/2018

I can get web elements now. Next is to make something with them.

Looking at what 'status' is for the webdriver. Right now I don't find any utility, but I will keep my get_status method, maybe
in the future it will give me something good.

07/02/2018

Made methods for maximize, minimize and full screen for the browser. I think that I need to start documenting code.

At least I could call methods from my webdriver to open, navigate and close browser.

07/01/2018

I created a close browser in my sandbox, now it is time to start working on my webdriver class.
Also I think it is time to establish some code conventions, because maybe in the future collaborators could be taken.

06/30/2018

I changed my approach, more than threading I am using subrocesses. The next problem that appeared is that the chromedriver is not closed
when the program ended, so I had to see how to close subprocesses. DONE.

Added a navigation function to my sandbox.

Starting to work on my webdriver class, my biggest challenge now is to be able to run the driver on a thread and continue the operations
in another.

Another thing I should start doing is to make this a real project with some management.

06/29/2018
Welcome to my automation project.

For now we have just some experimentation buuuut, it will grow.