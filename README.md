# ISSUE-TRACKER APPLICATION

This Full Stack Web application was developed as part completion of the Code Institute Full Stack Web Developer course. 
It is the milestone project for the Full Stack Frameworks with Django stream. The application attempts to follow the project brief in full.
The author has created a project based on the sample outline of project example 1; "Build an Issue Tracker" from the Project Ideas page.

Here is the manner in which the desired elements were outlined in the assignment brief;
- "Get user's feedback to guide prioritisation."
- "Get money to fund work on future features."  
- "The exciting thing is the business model that you’ve decided upon – you chose to offer the service and bug fixes for free, but ask for money 
	from your users to develop additional features."
- "The primary entity in the Issue Tracker is a ticket describing a user’s issue, and similar to Github’s issue tracker, you should allow users to 
	create tickets, comment on tickets, and show the status of the ticket (e.g. ‘to do,’ ‘doing,’ or ‘done’)."
- "As mentioned, issues come in two varieties – ‘bugs’ (which you’ll fix for free, eventually), and ‘features’ which you’d only develop if you’re 
	offered enough money."
- "To help you prioritize your work, your users will be able to upvote bugs (signifying ‘I have this too’), and upvote feature requests 
	(signifying ‘I want to have this too’)."
- " While upvoting bugs is free, to upvote a feature request, users would need to pay some money (with a minimum amount of your choice) to pay for 
	your time in working on it. In turn, you promise always to spend at least 50% of your time working on developing the highest-paid feature."
- "create a page that contains some graphs showing how many bugs or features are tended to on a daily, weekly and monthly basis, as well as the 
	highest-voted bugs and features. To enhance the user experience, use dc.js (or any other js approach) to create dynamic charts."
- " feel free to add pages describing your fictional UnicornAttractor application."

## TRAVIS INTEGRATION TESTING
[![Build Status](https://travis-ci.org/KikiDow/issue-tracker-full-stack-project.svg?branch=master)](https://travis-ci.org/KikiDow/issue-tracker-full-stack-project)

## DEMO
* A live demo hosted on Heroku can be found [here](https://full-stack-django-issuetracker.herokuapp.com/)

## UX
The GitHub issue tracker was mentioned in the assignment outline, hence this developer's research for the UX began [here](https://guides.github.com/features/issues/), which then led onto 
the Bootstrap issues section [here](https://github.com/twbs/bootstrap/issues) and [here](https://github.com/twbs/bootstrap/issues/29250). After reviewing these 
two applications, the student felt a clean, minimalist approach using light and easing colours associated with a more business-like and functional approach was 
suitable for this type of application. As the key elements appear to be the presentation of a list of reported issues, the ability to drill down into these issues 
and then take appropriate actions using buttons that clearly stand out from the rest of the presentation view. Using horizontal lines to present data/issues in 
a tabular form also appeared to be a contant feature on these two sites as it allows the user to easily follow pieces of information about an issue as they read 
from left to right.

Lorem Ipsum text was used in the description of the reported issues as the author did not have the time to research various bug/feature descriptions. 
This decision was also made to ensure that text used did not distract from the design.

## Features
* The application contains an **Authentication** app. This allows the user to login, logout, register with the site and change their password.
It also provides the session control for the application.
* The application contains a bootstrap javascript **carousel**. This is used as the landing page and introduction for the application. It provides a 
basic introduction to the application and it's features in a visually appealling way.
* Upon logging in, the application presents a **paginated list** of all the issues present in the database with a brief outline of each and a link
button to bring the user to the single issue view.
* The application contains a **single issue view page** that allows the user to view all information about the issue.
* The single issue view page allows the user to **upvote** an issue if it is a bug type issue.
* The single issue view page allows the issue contributor or a staff member to **edit** and/or **delete** an issue.
* The single issue view page also allows the user to **comment** on an issue, sharing ideas or shared experiences with another user about the issue.
* This single issue view page also allows the contributor of a comment or a staff member to **edit** and/or **delete** a comment.
* If the issue is of type **feature**, the user can select to place any **quantity** of tokens into their **cart** prior to purchase.
* Users' can view the **contents** of their cart by selecting the **cart** icon.
* Users' can **amend** the contents of their cart and select to **checkout**.
* The application contains a **checkout** feature that allows the user to **purchase** the items they have placed into their cart. This is done by entering 
their details and using the **STRIPE API**.
* The application contains a **search** app. This allows the user to narrow the search results presented to them by filtering results based on; issue name,
contributor, tag, whether the issue is fixed or not and issue type.
* The applications contains a **My Contributions** page which presents the user with any issues that they have contributed towards, whether it be a BUG, 
FEATURE OR COMMENT. This allows the user to more quickly access the issues that interest them the most.
* The application contains a **progress** app. This in-built separate app presents a number of statistics to the user in graphical form. Showing the user,
what has been happening on the application.

## Features To Implement
* With more time, the developer would like to have developed and used notifications to inform the user of any changes to issues, such as issue being fixed or 
another user commenting on an issue.
* I would like to have developed a staff page on the site allowing staff members to change the status of an issue without having to go to the django-admin panel.

## Technologies
- HTML
- CSS
- JavaScript.
- jQuery.
- Python 3.6
- sqlite3.
- Bootstrap 3.7.7
- Django Full Stack Framework.
- PostGres.
- Heroku. 
- Highcharts JavaScript chart library
- Stripe Payments API.

## Testing
* A form of White Box testing was conducted by the developer using potential use cases or user stories to ensure that each link in the application followed 
the intended path. This was also done for each feature outlined in the Features section to ensure they were working as intended.
* A form of Black Box testing was done by asking both a friend and the student's mentor on the course to use the application without instruction. 
Their feedback was then used to make improvements.
* Fundamental testing was used to ensure that the stack of technologies was working together successfully. (e.g.) Retrieving one field from a document in 
the database, manipulating it with Python, passing it through the Django Full Stack framework and presenting it to the user.
* Component testing was used for each block of code developed to serve a particular function. (e.g.) In lines 191-194 of the "recipe-app-test.py" file, 
the code block is attempting to filter result by category, placing only recipes with the same category as those selected by the user in the list of 
results. This was tested with using none, single and multiple categories selected, to ensure it was producing the correct result. Similar testing 
was used on all code blocks developed/used.
* Combination testing was used to ensure that code blocks were working in conjunction to produce the intended and expected results.
* The responsiveness of the application was tested using various browsers (Chrome, Safari, Internet Explorer, FireFox) and on different devices using the 
Google Chrome "Inspect" tab.
* Automated tests were developed and conducted using the in-built Django tests package. They can be found in the test_forms.py, test_views.py and test_models.py
file of the issues app. 20 tests were developed and conducted on the issues and progress apps. 
The results of these tests can be seen in the IMAGEFILE.jpg file located in the testing folder. Alternatively, one can run these tests by entering the 
following command into their own IDE once they have cloned the repository; ```python3 manage.py test```.

## Deployment
* This project is deployed to Heroku in conjunction with Amazon Web Servcies S3 to host the static and media file as Heroku only has ephemeral memory.
* The application was deployed as follows;
1. A new app was created on Heroku with a unique name.
2. The POSTGRES database add-on was then provisioned.
3. The following packages were then installed using the ```sudo pip3 install``` command. These packages were installed to allow, Cloud9, Heroku, PostGres and AWS S3 
	interface effectively.
		** ```dj_databse_url```
		** ```gunicorn```
		** ```psycopg2```
		** ```boto3```
		** ```django-storages```
4. These packages were then passed to the requirements.txt file using the command: ```sudo pip3 freeze > requirements.txt```
5. The dj_database_url package was then imported in the settings.py file using the command: ```import dj_database_url```
6. In the settings.py file, wire the application to the new "production" database using the following command ```DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}```
	while commenting out the test database details.
7. Retrieve the database_url from the config vars in the settings panel of your new app in Heroku.
8. The ```DATABASE_URL``` environment variable in the env.py file was set using the following command: ```os.environ.setdefault("DATABASE_URL", "pretend-heroku-database-url-key")```
9. The following two commands were then run to migrate all existing migration to the new postgres database; ```python3 manage.py makemigrations``` & ```python3 manage.py migrate```.
10. The details for a new superuser/administrator for the database was then set using the command: ````python3 manage.py createsuperuser```` 
11. On a PAID AWS account, a new S3 bucket was set up, giving it an appropriate unique name, groups, policy and users, setting the property for static website hosting,
	CORS Configuration and Bucket policy. Once created, the calibration csv file was downloaded containing the access keys for the newly created bucket.
12. Add the command 'storages' to the list of ```INSTALLED_APPS``` in settings.py
13. The lines ```141-168``` were then added to settings.py to wire the application up to the newly created S3 Bucket, the two AWS access keys being set in the env.py file.
14. The file custom-storages.py was then created and two classes were declared to create a static and media folders in the S3 Bucket.
15. The command: ```python3 manage.py collectstatic``` was then used to transfer all static files to the S3 Bucket. 
16. All environment variables (e.g. STRIPE API key, AWS keys, etc) were then set in the config vars on Heroku.
17. The Heroku app was then connected to the matching GitHub repository.
18. The Procfile was then created in my IDE (Cloud9). This is used to inform Heroku what type of app it is about to recieve. Pushing to the 
	GitHub repo.
19. On Heroku, the config vars: ````DISABLE_COLLECTSTATIC```` was set to ````1````. The ```1``` represented false and is used to prevent Heroku from retrieving all static files
	from the GitHub repo.
20. The ```Deploy Branch``` option was then selected on Heroku to build the app and retrieve the Heroku address(url) of the app.
21. The address(url) of the newly created app was then added to the list of ```ALLOWED_HOSTS``` in the settings.py file. Change comited and pushed to GitHub.
22. The ```Deploy Branch``` option was selected again to re-build the app. The ```Enable Automatic Deploys``` option was also selected to automatically re-build the app
	from any new pushes of code to GitHub.
23. App now fully deployed and ready for use on Heroku using S3 Bucket. Re-populated on new database. 

* GitHub reposity for the project is located [here](https://github.com/KikiDow/issue-tracker-full-stack-project)
* The application is deployed to Heroku [here](https://full-stack-django-issuetracker.herokuapp.com/)

## Credits

### Content
* The content for the about_page.html was taken from [here](https://unicorn.com/en/software-everywhere)
    - The decision was made to use the blurbs provided from this website as they are professionally written and match the context of software
	development.
* The descriptions of all issues and comments created in the application have been done using lorem ipsum text. This was done so save time
researching appropriate descriptions of software issues whilst presenting the user/viewer with simple and non-distracting content blocks.
The lorem ipsum text used was created [here](https://www.lipsum.com/)

### Media
- The file "No-image-available.jpg" was retrieved from [here](http://izuum.com/zoomm.php)
- The file "Bug.jpg" was retrieved from [here](http://www.softwaretestingclass.com/what-should-be-done-after-a-bug-is-found/)
- The file "aboutImage1.jpg" was retrieved from [here](https://www.shutterstock.com/image-vector/software-web-development-programming-concept-abstract-1122339353)
- The file "aboutImage3.jpg" was retrieved from [here](https://www.shutterstock.com/image-photo/automation-software-technology-process-system-business-744825085)
- The file "aboutImage4.jpg" was retrieved from [here](https://www.shutterstock.com/image-photo/program-code-computer-keyboard-124888153)
- The file "contribute.jpg" was retrieved from [here](https://www.codegent.com/blog/2010/4/healthy_competition)
- The file "realBug.jpg" was retrieved from [here](https://www.rt.com/news/flame-virus-cyber-war-536/)

#### The following images were used for **sample uploads** from test users:
- The file "report.png" was retrieved from [here](https://marketplace.geotab.com/solutions/dvir-defects-alert-report)
- The file "bug1.png" was retrieved from [here](https://www.egrovesys.com/blog/what-is-bug-why-do-bugs-occur/)
- The file "bug3.jpg" was retrieved from [here](https://betanews.com/2017/02/02/bug-fixing-software-development/)
- The file "bug4.jpg" was retrieved from [here](https://www.theregister.co.uk/2018/10/22/freertos_iot_platform_security_flaws/)
- The file "bug5.jpg" was retrieved from [here](https://www.quora.com/How-can-I-report-a-bug-on-Quora)
- The file "bug6.png" was retrieved from [here](https://meta.askubuntu.com/questions/15327/revealing-bug-report-considered-answer)
- The file "feature1.jpg" was retrieved from [here](https://www.officialroms.com/miracle-box-crack-2-82-start-button-not-working/)
- The file "feature2.jpg" was retrieved from [here](https://steemit.com/utopian-io/@kebena/suggestion-add-menu-and-feature-table-in-inkscape)
- The file "feature3.jpg" was retrieved from [here](https://steemit.com/utopian-io/@kebena/suggestion-add-menu-and-feature-table-in-inkscape)

### Acknowledgements
#### References
* McCool, N. (2016). Putting It All Together - Ecommerce. Retrieved from 
	https://github.com/Code-Institute-Solutions/PuttingItAllTogether-Ecommerce
* Daly. J. (2019). Issue-Tracker. Retrieved from
	https://github.com/jordandaly/issue_tracker
* Lavi, Y. (2019). Styling-A-Django-Project. Retrieved from
	https://github.com/Code-Institute-Solutions/Styling-A-Django-Project
* Lavi, Y. (2019). AuthenticationAndAuthorisation. Retrieved from
	https://github.com/Code-Institute-Solutions/AuthenticationAndAuthorisation
* Lavi. Y. (2019). BlogAllAboutIt. Retrieved from
	https://github.com/Code-Institute-Solutions/BlogAllAboutIt
* StackOverFlow 
	https://stackoverflow.com/questions/25940811/how-to-add-anchor-to-django-url-in-template 

#### Bibliography
* Django - https://docs.djangoproject.com/en/1.7/intro/tutorial01/
* Bootstrap - https://www.w3schools.com/bootstrap/default.asp
* Bootstrap - https://getbootstrap.com/docs/3.3/
* Django Authorisation - https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/forms/


