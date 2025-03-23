# 404: Gender Gap Not Found - Inspiring the Next Generation of Women in Tech

## User Experience

### Site Goals
Our app is designed to inspire the next generation of tech innovators by:
- sharing stories of women pioneers in tech
- providing handy tips into tech
- bridging the mentorship gap for women in technology by connecting mentees with mentors who can guide their professional journeys.

The web app aims to break barriers, close gender gaps and cultivate a diverse and inclusive tech community where women can thrive as innovators, leaders and changemakers. It’s not just about mentorship — it’s about building a stronger future for women in technology.

Live site: [https://team-1-8284bb86c76b.herokuapp.com/](https://team-1-8284bb86c76b.herokuapp.com/)

### Target Users
- General Users: Visitors interested in exploring the key milestones of women in tech to learn about their achievements and biographies.
- Students and Learners: People using the site to explore role models and gain guidance from mentors.
- Authenticated Users: Registered users who can access additional features like connecting with mentors and honouring women tech icons on the timeline.
- Researchers: Individuals seeking inspiration or information about notable figures featured in the timeline.
- Administrators: Users responsible for managing content like timeline entries, biographies and connections to mentors.

## Design

### Colour Scheme
<!-- Add content for Colour Scheme here -->

### Fonts
The site uses a selection of fonts inspired by Web 1.0 pages from the late 1990's:

**Gentium Book Basic**
This is a timeless serif font designed for readability, featuring elegant letterforms and support for a wide range of languages and scripts, making it ideal for the biographies.
![image](https://github.com/user-attachments/assets/7a589bdb-6f04-47ea-ae07-578ec26f8ae7)
<!-- Add content here -->

### Wireframes
Based on the user stories, we used Balsamiq to design the wireframes for the main UI, starting with mobile first.

<details>
  <summary>Mobile devices</summary>
    Here are the wireframes for mobile devices:
    
</details>
<details>
  <summary>iPad screens</summary>
    Here are the wireframes for tablets and iPads:
</details>
<details>
  <summary>Laptop and larger screens</summary>
    Here are the wireframes for larger screens and laptops:

</details>

## Agile Methodology

### Kanban Board
All user stories were logged on the [Kanban Project Board](https://github.com/users/tgrey2024/projects/21) on GitHub Projects.

We also used it during testing to log any significant bugs that need to be fixed before the deadline. These were then assigned and prioritised alongside other issues and user stories.

### User Stories
Here are all the user stories that have been prioritised for the current implementation:

| User Stories                                    | MoSCoW priority           |  Status |
|:----------------------------------------------- |:-------------------------:|:-------:|
| User-Friendly Navigation and Responsive Design  | must have                 |   Done  |
| Display Timeline View | must have                 |   Done  |
| Header and Footer  | must have                 |   Done  |
| User Authentication  | must have                 |   Done  |
| Connect with Mentors  | must have                 |   Done  |
| Team page  | must have                 |   Done  |
| Custom Error Pages  | should have                 |   Done  |

<!-- add main user stories -->

## Features

### Header and Footer
### Timeline
### Tips
### Contact Form
### Admin Panel
The Admin Panel is set up for the admin or superuser to access and update the data in the database.

### Error Pages
<!-- Add content for Error Pages here -->

### Future Features
<!-- Add content for Future Features here -->

## Testing

### Manual Testing
<!-- Add content for Manual Testing here -->

## Bugs

### Known Bugs
<!-- Add content for Known Bugs here -->

## Technologies And Languages

### Languages Used
- HTML5 - for content and structure on the site.
- CSS - for styling the site.
- Python - provides functionality for the site.
- Django - as the Python framework for the site.
- Javascript - for interactive and dynamic elements of the site.

### Technologies
- node.js

### Deployment and Version Control
- Git
- Github
- Heroku
- Whitenoise - for serving static files
- Cloudinary - for image storage

### Styling
- Tailwind CSS - for responsive design
- FlyonUI - for styling timeline, etc.
- Tabler - for icons

### Authentication
- Django AllAuth

### Tools
- VS Code - IDE for development
- Balsamiq - for wireframes
- Canva
- LogoAI - for AI logo
- Favicon.io - for favicons
- Copilot - AI content generation

## Deployment
The web app is hosted on Heroku using Eco Dynos, and is deployed via the designated Github repository.

The deployment process is as follows:
1. Login to your GitHub profile and **Create a new repository**.
2. Open VS Code locally, connect and open the workspace. Create the MVP.
3. Install web server gunicorn and freeze requirements.
4. Create a new Procfile in the root directory and specify the running of the web app with process type as gunicorn in the Procfile.
5. Add deployed apps to ALLOWED_HOSTS in settings.py, and set Debug = False. Add, commit and push to the Github repo.
6. In Heroku, create a new app using a unique name and select the correct region. 
7. Add Config Vars in Settings.
8. Go to Deploy tab, search for the correct Github repo and **Deploy Branch**.
9. Choose **Automatic Deploy**.
10. **View app** to verify that it is been deployed correctly. This deployed site can now be validated and tested e.g. in Chrome Dev Tools.
11. In the app's Resources tab, check that Eco Dynos are used and remove any unnecessary Add-ons.
12. Subsequent changes to the code will need to be pushed to the Github repo and deployed on Heroku.

### Creating A Fork
<!-- Add content for Creating A Fork here -->

### Cloning Repository
<!-- Add content for Cloning Repository here -->

## Credits

### Media
<!-- Add content for Media here -->

### Code
<!-- Add content for Code here -->

### Contributors
Kiree [github.com/Swewi](https://github.com/Swewi)

Debbie Thompson [github.com/debbiect246](https://github.com/debbiect246)

Linus Johansson [github.com/j0hanz](https://github.com/j0hanz)

Ashwinkarthik Selvaraj [github.com/ashwinsel](https://github.com/ashwinsel)

Vital Nsengiyumva [github.com/Vinsengi](github.com/Vinsengi)

Tripta Grey [github.com/tgrey2024](github.com/tgrey2024)

### Acknowledgements
<!-- Add content for Acknowledgements here -->
