# 404: Gender Gap Not Found - Inspiring the Next Generation of Women in Tech

**404: Gender Gap Not Found** is a groundbreaking web application dedicated to celebrating the achievements of women in technology. By showcasing inspiring stories, offering valuable tech tips, and bridging the mentorship gap, our platform aims to empower the next generation of female innovators. We envision a future where diversity and inclusion drive progress—ensuring that the gender gap in tech is a challenge of the past.

Live site: [https://team-1-8284bb86c76b.herokuapp.com/](https://team-1-8284bb86c76b.herokuapp.com/)

---
![logo_readme](https://github.com/user-attachments/assets/090ae0dd-d384-4a29-825f-11549e6fcc10)![clippy2](https://github.com/user-attachments/assets/02fe2f36-1931-4280-ab35-01172097a8b9)



## User Experience

### Site Goals
Our app is designed to inspire tech innovators by:
- **Sharing Stories:** Highlighting the key milestones and achievements of women pioneers in technology.
- **Providing Tips:** Offering handy, practical tips for navigating the tech world.
- **Bridging Mentorship Gaps:** Connecting mentees with experienced mentors who can guide their professional journeys.

The web app strives to break barriers, close gender gaps, and cultivate a diverse, inclusive community where women can thrive as innovators, leaders, and changemakers. It’s not just about mentorship—it’s about building a stronger future for women in technology.

### Target Users
- **General Users:** Visitors interested in exploring milestones and biographies of women in tech.
- **Students and Learners:** Individuals looking for role models and guidance from mentors.
- **Authenticated Users:** Registered users who access additional features like mentor connections and honoring tech icons.
- **Researchers:** People seeking inspiration or detailed information about notable figures.
- **Administrators:** Those managing content such as timeline entries, biographies, and mentor connections.

---

## Design

### Colour Scheme
Retro Vibe: The design features a bold combination of Navy (#000080) and LightSkyBlue (#87CEFA) as seen in the footer gradient, evoking a nostalgic Windows 98 feel.
High Contrast: The dark navbar (bg-gray-900) paired with white text and borders ensures excellent readability on large screens.
Accent Variety: Subtle Silver (#C0C0C0) accents and well-defined hover effects add visual depth without detracting from the retro aesthetic.
We draw from a palette of colours commonly found on operating systems in the 90's, taking inspiring from the cool retro colours of the Windows 98 operating system: 
![Colour scheme](documentation/features/colours.png)

### Fonts
The site uses fonts inspired by late 1990’s Web 1.0 aesthetics. In particular:

**Gentium Book Basic**  
A timeless serif font designed for readability with elegant letterforms and extensive language support—ideal for biographies.

![Gentium Book Basic Example](https://github.com/user-attachments/assets/7a589bdb-6f04-47ea-ae07-578ec26f8ae7)

### Wireframes
Based on the user stories, we used Balsamiq to design the wireframes for the main UI, starting with mobile first.


<details>
  <summary>Header and Footer</summary>
    Here are the wireframes for the site with its header and footer:
  

</details>
<details>
  <summary>Contact a Mentor</summary>
    Here are the wireframes for contact form for connecting with a mentor:
  
  

</details>
<details>
  <summary>Timeline</summary>
    Here are the wireframes for timeline:
  
   ![Timeline](documentation/wireframes/wf_timeline_mobile.png)
      ![Timeline](documentation/wireframes/wf_timeline_ipad.png)
    ![Timeline](documentation/wireframes/wf_timeline_laptop.png)
  <summary>Laptop and Larger Screens</summary>
  Wireframes for laptops and larger screens are available here.
</details>

---

## Agile Methodology

### Kanban Board
All user stories were logged on the [Kanban Project Board](https://github.com/users/tgrey2024/projects/21) on GitHub Projects. We used this board during development and testing to track progress, assign priorities, and log significant bugs.

### User Stories
Below are the prioritized user stories for the current implementation:

| User Stories                                    | MoSCoW Priority           |  Status |
|:----------------------------------------------- |:-------------------------:|:-------:|
| User-Friendly Navigation and Responsive Design  | must have                 |   Done  |
| Display Timeline View                           | must have                 |   Done  |
| Header and Footer                               | must have                 |   Done  |
| User Authentication                             | must have                 |   Done  |
| Connect with Mentors                            | must have                 |   Done  |
| Team Page                                       | must have                 |   Done  |
| Custom Error Pages                              | should have               |   Done  |

---

## Features

- **Header and Footer:** Consistent branding and easy navigation.
- **Timeline:** A retro-inspired timeline showcasing milestones of women in tech.
- **Tips:** Practical tech tips to empower users.
- **Contact Form:** An accessible way for users to get in touch.
- **Admin Panel:** Secure administration interface for managing content.
- **Error Pages:** Custom-designed error pages that align with the site’s aesthetic.
- **Future Features:** We're constantly refining our platform to better serve our community. Upcoming enhancements include more interactive timeline features, advanced mentor matching capabilities, and a wealth of new resources to empower the next generation of tech innovators. Stay tuned for regular updates as we expand our offerings and fine-tune the user experience.

---
### Header
![Header](documentation/features/header.png)
#### Header Section Overview
The header of this project is designed with a retro-modern and responsive layout to provide easy navigation across the site, with a touch of 1980s. It includes the following key components:
### Structure and Design
#### Background Gradient
* The header has a linear gradient that transitions from a dark blue (#000080) to a light sky blue (#87CEFA), giving it a visually appealing look. The text color is white, ensuring good contrast and readability.
#### Logo
* The logo is placed on the left side and links to the home page. It's styled to ensure that it fits well in the header without distorting or overflowing, using a max-w-full and max-h-full approach.
#### Navigation Links
* The horizontal navigation menu is displayed on larger screens (medium and up, md breakpoint) with links to key pages: Home, Timeline, Mentors, Team, Login and Register. These links have hover effects for better user interaction.
* If the user is authenticated, additional links for "Logout" and "Change Password" are displayed. Otherwise, users will see the "Login" and "Register" options.
### Mobile Responsiveness
* On smaller screens, the navigation links are hidden, and a hamburger menu (navbar-burger) appears.
* When clicked, it toggles a dropdown menu (navbar-dropdown) showing the same navigation links as in the desktop version.
* The dropdown menu is styled to appear below the hamburger button with a light background and rounded corners.
### Footer
![Footer](documentation/features/footer.png)
* The footer is styled with a dark blue background (#000080), white text, and a subtle border on top.

* The text is centered, and the font is set to a monospace style (font-mono), with a small size (text-sm).

* It includes a copyright notice with the text "404 Gender Gap Not Found - Since 1900", followed by "All Rights Reserved".

* This footer is fixed at the bottom of the page (mt-auto), ensuring it stays at the bottom even if content above it is not enough to fill the screen.

### Timeline
* The timeline feature is a tribute to the trailblazing women who have shaped the world of technology through their pioneering achievements, starting with the pioneer, Ada Lovelace, often hailed as the world's first computer programmer. It presents an engaging and interactive journey through history, highlighting key figures and their groundbreaking contributions to fields like computing, engineering, game design, web accessibility and more. Each entry includes a snapshot of their life, notable accomplishments and the lasting impact of their work, providing inspiration for users of all ages. By showcasing these remarkable stories, the timeline not only honours these innovators but also encourages future generations to follow in their footsteps and continue breaking barriers in tech.

#### Read more
* The user is invited to know more about any figure by clicking on the Read more button to find out more about each tech icon.
  
#### Honor Her - Heart
* Users can honors the women featured on our timeline by giving them a heart - clicking on the heart icon.

### Tips
### Contact Mentor Form
* User may find a mentor from the pool of mentors on our mentors page.
* If a user finds no matching mentor right away, the user may click on the "Find a mentor" button
* A contact a mentor window will pop up and the user may provide his/heremial, mentor name and a message.
* The sytem will then try to match the user with a mentor.
### Admin Panel
The Admin Panel is set up for the admin or superuser to access and update the data in the database.

### Custom Error Pages
<!-- Add content for Error Pages here -->

### Future Features


## Testing

### Manual Testing
| Test Case                                        | Browser Compatibility                                  | Steps to Reproduce                                                                                      | Status |
|--------------------------------------------------|--------------------------------------------------------|---------------------------------------------------------------------------------------------------------|:------:|
| Responsive Navigation Bar (Desktop)              | Chrome, Firefox, Edge, Safari                          | 1. Open the site on a desktop browser<br>2. Verify nav links are visible and properly aligned          | ✔      |
| Responsive Navigation Bar (Mobile - Burger Menu) | Chrome (DevTools), Safari, Firefox, Edge               | 1. Open the site in a mobile viewport<br>2. Click on the burger icon<br>3. Verify dropdown appears      | ✔      |
| Home Page Rendering                              | Chrome, Firefox, Edge, Safari                          | 1. Visit the homepage URL<br>2. Verify the main content (image, text, layout) is rendered correctly       | ✔      |
| About Us Page with Team Section                  | Chrome, Firefox, Edge, Safari                          | 1. Visit `/about/` URL<br>2. Verify team members section displays correctly with images and GitHub links  | ✔      |
| User Authentication (Login/Registration Flow)    | Chrome, Firefox, Edge, Safari                          | 1. Visit login and registration pages<br>2. Submit forms with valid data<br>3. Confirm redirection to home | ✔      |
| Timeline Page Interaction                        | Chrome, Firefox, Edge, Safari                          | 1. Visit the timeline page<br>2. Interact with timeline elements and honour buttons<br>3. Verify proper functionality | ✔      |


---

## Bugs

### Known Bugs
*Details to be added:* 

---

## Technologies and Languages

### Languages Used
- **HTML5:** For site structure.
- **CSS:** For styling.
- **Python:** Provides the site’s core functionality.
- **Django:** The Python framework powering the app.
- **JavaScript:** For interactive and dynamic elements.

### Technologies
- **node.js**

### Deployment and Version Control
- **Git** and **Github:** For version control.
- **Heroku:** Hosting the web application.
- **Whitenoise:** Serving static files.
- **Cloudinary:** Image storage.

### Styling
- **Tailwind CSS:** For responsive design.
- **FlyonUI:** For styling elements like the timeline.
- **Tabler:** For icons.

### Authentication
- **Django AllAuth**

### Tools
- **VS Code:** IDE for development.
- **Balsamiq:** For wireframe creation.
- **Canva, LogoAI:** For logo and design assets.
- **Favicon.io:** For favicon generation.
- **Copilot:** AI-powered code assistance.

---

## Deployment

The web app is hosted on Heroku using Eco Dynos and is deployed via the designated GitHub repository.

**Deployment Process:**
1. Log in to your GitHub profile and **create a new repository**.
2. Open VS Code locally, connect to the workspace, and build the MVP.
3. Install the web server **gunicorn** and freeze requirements.
4. Create a new **Procfile** in the root directory specifying gunicorn as the process type.
5. Update `ALLOWED_HOSTS` in `settings.py` and set `DEBUG = False` for production. Commit and push these changes.
6. In Heroku, create a new app using a unique name and the correct region.
7. Add necessary **Config Vars** in the Heroku settings.
8. Go to the **Deploy** tab, connect the correct GitHub repository, and deploy the branch.
9. Choose **Automatic Deploy** for seamless updates.
10. Verify the deployed site using browser developer tools.
11. In the app's Resources tab, confirm Eco Dynos are in use and remove unnecessary add-ons.
12. Future changes should be pushed to GitHub and deployed on Heroku accordingly.

---

## Creating A Fork
1. On Github navigate to repository
2. click "Fork" located towards the top right corner
3. Select "owner" for the forked repo, from the dropdown menu under "owner" Under "Owner"
4. It will create forked repo under the same name as orinial by default but you can type a name in "Repository name" or add a description in "Description" box.
5. Click "Create fork" !

Forking allows you to make any changes without affecting original project. You can send the suggestions over by submitting pull request. Project owner can review the pull request before accepting the suggestions and merging them.


For more details on how to fork the repo, in order to for example suggest any changes to the project you can visit:
https://docs.github.com/en/get-started/quickstart/fork-a-repo

When you have fork to a repository you don't have access to files locally on your device, for this you will need to clone the forked repo.

## Cloning the Repository

1. On Github navigate to repository
2. Click "Code" a green button shown right above the file list
3. Copy the URL of the repo using HTTPS, SSH OR Github CLI
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory
6. Type git clone, and then paste the URL you copied earlier
7. Press enter to create local Clone

For more details on how to clone the remote repo in order to create a local copy for own use, please go to
https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository

## Credits

### Media
*Details to be added:* 

### Code
This project leverages a number of robust third-party libraries and frameworks. We use Django for backend operations, Tailwind CSS for responsive design, 98.css for a retro Windows 98 aesthetic, FlyonUI for timeline styling, and Tabler for icons. We acknowledge and appreciate the open-source community for providing these essential tools.

### Contributors
- **Kiree:** [github.com/Swewi](https://github.com/Swewi)
- **Debbie Thompson:** [github.com/debbiect246](https://github.com/debbiect246)
- **Linus Johansson:** [github.com/j0hanz](https://github.com/j0hanz)
- **Ashwinkarthik Selvaraj:** [github.com/ashwinsel](https://github.com/ashwinsel)
- **Vital Nsengiyumva:** [github.com/Vinsengi](https://github.com/Vinsengi)
- **Tripta Grey:** [github.com/tgrey2024](https://github.com/tgrey2024)

### Acknowledgements
*Details to be added:* Recognize any mentors, organizations, or tools that helped bring this project to life.