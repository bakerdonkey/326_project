# themeatbirds
## Austra
## Fall 2018

# Overview 
Austra is designed to fulfill a main goal of SPIRE, for students to determine which classes they will be taking and fill out their schedule, in a more intuitive way. Austra’s primary advantage is easily visualization how course candidates conflict and mesh with the graphical interface. Furthermore, it allows for student-oriented feedback for classes and teachers in one place. Austra has social features including profiles and comments. 

# Team Members
CJ Moynihan		    partyrico
Harrison Orne		vgaparadise
Arielle Rosenthal   ariellerosen
Sam Kochanski	    bakerdonkey

# User Interface 
Austra has a static landing page, which provides an entry point and a portal for a user to login and register. There are login and registration forms that handle different levels of authorization.

The main view has two major components - the class search and the user class session schedule. Users can search for classes here, check details of them, as well as add them to the calendar. 

The class search, on the main view, is an accordian that lists all eligible classes. When a class is selected in the accordian, it provides deeper information on the class session. The elements of the accordion are color-coded based on eligibility. There is a search bar on the top, which filters items from the accordion based on the query entered.

The user class session schedule, also on the main view, is a weekly calendar populated with all selected candidate class sessions. If multiple classes conflict, the calendar provides visual feedback.

There are views for class details and instructor details, where users can find additional information about those. 

The user profile view allows users to see details about themselves as well as add classes they’ve taken in the past. 

# Data Model

![](models.png)

Austra has four interconnected data structures -- instructors, courses, sessions, and comments. Instructors have a name field and a rating field assigned by superusers. Courses have a name, a code for quick reference (eg. COMPSCI 220), and a rating determined by users. Furthermore, course has a many-to-many relationship with itself to define a list of prerequisites. Sessions are instances of course, and as such they reference a course and an instructor. Also, they have local start and end time, days of the week they are active, and a rating based on that of the instructor and course. Comments were added to our model directly instead of an external framework because we wanted more control of them. It has a one-to-many relationship with courses not sessions because only courses can have comments. 

# URL Routes/Mappings
| PATTERN               | PERMS                                          | PURPOSE                                                                                                   |
| --------------------- | ---------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| ‘’                    | all                                            | This is an empty url route that goes to the home page                                                     |
| ‘accounts/profile/’   | signed in users                                | Users enter classes_taken and can see their details here.                                                 |
| ‘calendar’            | Signed in users                                | Users can put their classes on their calendar for next semester.                                          |
| ‘instructors/’        | all                                            | Serves as a list of instructors.                                                                          |
| ‘instructor/<int:pk>’ | all                                            | Look up a specific instructor, using its key as a url route.                                              |
| 'course/<int:pk>'     | All (only signed in can comment / doot though) | Look up a specific course, using its key as a url route.                                                  |
| 'instructor/create/'  | admin                                          | Admins are brought here to create instructors.                                                            |
| ‘course/create/’      | admin                                          | Admins are brought here to create courses.                                                                |
| ‘accounts/’           | all                                            | Django built in to allow people to sign in and sign out. Those routes are predefined through this route.  |

# Authentication/Authorization
There are two user groups - standard users and admins (superusers). Standard users can modify their schedule by selecting existing course sessions, while admins can create courses, instructors, and sessions in-app. Admins can delete instructors and classes, while users can only remove classes from their schedule. If a user is not authorized to view a page, they are redirected to login form or redirected to the main page.

# Team Choice
For our Team Choice, we implemented advanced search functionality. This is used on the Calendar and User Profile pages as a way to find what courses you are looking for. The search parameters are split by whitespace, then each term is compared to all of the course names, course codes and instructor names. Every course that has a match to any of the search terms is included, and the results are first sorted by class code, then resorted by number of hits (a course has one hit for each term that matches at least one of the categories).

Originally the search was implemented directly into the calendar view in views.py, but it was later refactored into its own seperate function. This was so that it could be easily modified and extended to the User Profile page. The low-level search is implemented using the Django's filter method, and more specifically it uses a special kind of inferencing in that Django knows that session\_\_instructor\_\_name\_\_icontains acutally refers to the Sessions that have a foreign key to all Courses, then to the instructors names that these Sessions have a Foreign key with. There is also seperate merging logic that flattens a list of seperate queries, and counts the number of hits. This is to keep track of the number of times that a course gets a 'hit', but also to ensure that if a term matches multiple categories, it still only counts as one 'hit'.

This is then passed in as a parameter for the calendar and profile\_page functions in views.py, then referenced in their templates as list variables in templates/accounts/profile.html and templates/main.html.

# Conclusion
We all started this semester without any experience with Django, three of us with a little experience with web programming at all. Therefore, everything we implemented was built on top of a wealth of new technical knowledge, design patterns, and programming methodologies. 

Like with learning anything new, there were growing pains, regrettable pitfalls, and overwhelming moments that lead to some stressful interactions between us. Specifically, our idea was a little nebulous in the beginning, so our design direction was muddled. However, by improving our communication and through actually sitting down with the explicit purpose of talking about it, we solidified our design direction and became much more productive.

If we were to do it all over again, we would focus more on the front-end design. Once its function took form, the program became too delicate to mess with without a lot of extra work. If we had a more complete design idea in the beginning, we could have accounted for this. However, we are generally satisfied with Austra and proud of our accomplishments as individuals and as a team.

